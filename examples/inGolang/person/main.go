package main

import (
	"fmt"
	"github.com/the-code-experiments/experiment-protobuf/blob/master/examples/inGolang/person"
)

func main() {
	Person()
}

func Person() {
	person := profilepb.Person{
		username: "hegdeashwin",
		first_name: "Ashwin",
		last_name: "Hegde"
	}

	fmt.Println(person)
}