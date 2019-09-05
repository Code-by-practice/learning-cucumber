# Protobuf

## What is Protobuf?

* Protobuf also known as Protocol Buffers are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.
* Define how you want your data to be structured, then you can use special generated code to easily write and read your structured data.
* Currently, it support generated code in Java, Python, Golang, C++.
* The latest version `proto3`, also supports golang, Ruby, JavaScript and C# etc. 

## Assigning field numbers

|Number range|Comments|
|:---|:---|
|1| Smallest field number that you can specify.|
|2^29| Largest field number that you can specify.|
|1 - 15| Take one byte to encode.|
|16 - 2047| Take two bytes to encode.|
|19000 - 19999| Are reserved for the Protocol buffers implementation. Compiler will throw error if we used this range.|

## Types

*  Here are the list of type supported [https://developers.google.com/protocol-buffers/docs/proto3#scalar](https://developers.google.com/protocol-buffers/docs/proto3#scalar)

**Notes:**

* For Enum type, first constant must be mapped with zero

## Advantages

* Fasters compare to other formats.
* RPC support.

## Disadvantages

* Lack of resources and smaller community.
* Lack of support.
* Non-human readability.

## References

* [Style guide](https://developers.google.com/protocol-buffers/docs/style)
