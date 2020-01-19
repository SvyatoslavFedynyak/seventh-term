package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	file, err := ioutil.ReadFile("data/passwords.txt")
	if err != nil {
		fmt.Print(err)
	}
	passwords := string(file)
	fmt.Println(passwords)
}
