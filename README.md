# Experiment Protobuffers

```
pip install protobuf
```

**Generate language code from using protoc and .proto file**

```
cd simple

For Python:
protoc -I=python --python_out=python proto/person.proto

For Java:
protoc -I=java --java_out=java proto/person.proto

For JS:
protoc -I=js --js_out=js proto/person.proto

For Golang:
protoc -I=golang --go_out=golang proto/person.proto
```

Use PyCharm
```
cd examples/inPython

For Python:
protoc -I=person/ --python_out=person/ person/person.proto

```