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
			minValue, minIndex := min(topThreeElves)

			if currentElf > minValue {
				topThreeElves[minIndex] = currentElf
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


func min(arr []int) (int, int) {
	min := arr[0]
	minIndex := 0

	for i, value := range arr {
		if value < min {
			min = value
			minIndex = i
		}
	}

	return min, minIndex
}
