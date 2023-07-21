def main():
    with open('input.txt') as f:
        lines = f.readlines()

    elf_calories = []
    current_calories = 0
    for l in lines:
        if l == '\n':
           elf_calories.append(current_calories) 
           current_calories = 0
        else:
            current_calories += int(l.replace('\n', ''))
    
    print(sum(sorted(elf_calories, reverse=True)[0:3])) 

if __name__ == '__main__':
    main()
