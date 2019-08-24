# Experiment Protobuffers

**Generate language code from using protoc and .proto file**

```
cd simple

For Python execute:
protoc -I=proto --python_out=python proto/person.proto

For Java execute:
protoc -I=proto --java_out=java proto/person.proto

For JS execute:
protoc -I=proto --js_out=js proto/person.proto

For Golang execute:
protoc -I=proto --go_out=golang proto/person.proto
```

