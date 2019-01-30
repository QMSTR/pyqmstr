PROTO_FILES := $(shell ls proto/*.proto)
PROTO_PYTHON_FILES := $(patsubst proto/%,qmstr/service/%,$(PROTO_FILES:.proto=_pb2.py)) $(patsubst proto/%,qmstr/service/%,$(PROTO_FILES:.proto=_pb2_grpc.py))
GRPCIO_VERSION := 1.15.0

venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv -p python3 venv
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate

requirements.txt:
	echo grpcio==$(GRPCIO_VERSION) >> requirements.txt
	echo grpcio-tools==$(GRPCIO_VERSION) >> requirements.txt
	echo autopep8 >> requirements.txt

.PHONY: python_proto
python_proto: $(PROTO_PYTHON_FILES)

qmstr/service/%_pb2.py qmstr/service/%_pb2_grpc.py : venv proto/%.proto
	venv/bin/python -m grpc_tools.protoc -Iproto --python_out=./qmstr/service --grpc_python_out=./qmstr/service proto/*.proto