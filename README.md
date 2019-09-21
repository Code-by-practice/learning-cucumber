# Experiment Protobuffers

Cover the basics of protobuf creation, generation and usage.

## Prerequisites

* Protobuf compiler (protoc) [https://github.com/protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf)


## How to write and compile .proto file?

To generate code for specific langauge from .proto file we'll be using protoc compiler.

**Python**

```
cd simple/ && mkdir python
protoc --python_out=python proto/person.proto
```

**Golang**

```
cd simple/ && mkdir golang
protoc --go_out=golang proto/person.proto
```

**JavaScript**

```
cd simple/ && mkdir javascript
protoc --js_out=javascript proto/person.proto
```

**Java**

```
cd simple/ && mkdir java
protoc --java_out=java proto/person.proto
```

## How to run the examples?

**Generate language code from using protoc and .proto file**

cd examples/inPython
protoc -I=person/ --python_out=person/ person/person.proto

cd examples/inGolang
protoc -I=person/ --go_out=person/ person/person.proto
```

## References

* [https://developers.google.com/protocol-buffers/docs/proto3](https://developers.google.com/protocol-buffers/docs/proto3)