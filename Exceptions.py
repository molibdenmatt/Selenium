while True:
    try:
        print("Give me the first number: ")
        first_number = int(input())
        print("Give me the second number")
        second_number = int(input())
        print(first_number + second_number)
        break
    except ValueError:
        print("Only numbers are allowed!")
        continue
