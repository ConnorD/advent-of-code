package main

import (
	"strconv"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	content, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	currentElf := 0
	maxElf := 0

	for _, line := range strings.Split(string(content), "\n") {
		number, err := strconv.Atoi(line)
		currentElf += number

		if err != nil {
			if currentElf > maxElf {
				maxElf = currentElf
			}

			currentElf = 0
		}
	}

	fmt.Println(maxElf)
}
