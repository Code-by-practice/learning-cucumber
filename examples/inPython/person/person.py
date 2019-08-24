import person.person_pb2 as person_pb2

person = person_pb2.Person()

person.username = "hegdeashwin"
person.first_name = "Ashwin"
person.last_name = "Hegde"

# Enum
person.role = person_pb2.ENGINEER

# Date
person.birthdate.year = 1988
person.birthdate.month = 8
person.birthdate.month = 26

print(person)

# Write the object to a file, writebytes

with open("person.bin", "wb") as f:
    bytesAsString = person.SerializeToString()
    f.write(bytesAsString)

with open("person.bin", "rb") as f:
    person_read = person_pb2.Person().FromString(f.read())

print(person_read)
print(person_read.username)

