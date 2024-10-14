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
	topThreeElves := make([]int, 3)

	for _, line := range strings.Split(string(content), "\n") {
		number, err := strconv.Atoi(line)
		currentElf += number

		if err != nil {
			for i, elf := range topThreeElves {
				if currentElf > elf {
					topThreeElves[i] = currentElf
					break
				}
			}

			currentElf = 0
		}
	}

	calorieSum := 0
	for _, value := range topThreeElves {
		calorieSum += value
	}

	fmt.Println(calorieSum)
}
