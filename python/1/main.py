def main():
    with open('input.txt') as f:
        lines = f.readlines()

    most_calories = 0
    current_calories = 0
    for l in lines:
        if l == '\n':
            if current_calories > most_calories:
                most_calories = current_calories
            
            current_calories = 0
        else:
            current_calories += int(l.replace('\n', ''))
    
    print(most_calories)
        

if __name__ == '__main__':
    main()
