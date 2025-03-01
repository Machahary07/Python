def calc():
    print('')
    print('╭┈ • ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ ୨୧ ୨୧ ୨୧ ୨୧ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ • ┈╮')
    print('SIMPLE PYTHON CALCULATOR THAT ACTUALLY WORK & ROAST YOU FOR MISTAKES. ENJOY!')
    print('╰┈ • ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ ୨୧ ୨୧ ୨୧ ୨୧ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ • ┈╯')
    print('')
    try:
        count = int(input('How many numbers you want to calculate: '))
        if count < 2:
            print('Ahmm.. Excuse me u need to kindly enter at least 2 numbers.')
            return
        numbers = [float(input(f'Enter number {i+1}: ')) for i in range(count)]
        operation = input('Enter operation (+, -, *, /): ')

        if operation == '/':
            if count > 2:
                print('Duhhh Division only works with 2 numbers. Input 2 nums & try Again Dude.')
                return
            if 0 in numbers[1:]:
                print("Division by zero? You trying to break math? Try Again Dude.")
                return
        
        result = numbers[0]
        for num in numbers[1:]:
            result = eval(f'{result} {operation} {num}')

        print()
        print(f"Result: {result} Thank you!")
        print()
        print('♡ ∩_∩') 
        print('(„• ֊ •„)♡')
        print('|￣U U￣')
        print()
    except ValueError:
        print("Invalid input. Numbers only, my dude.")
    except Exception as e:
        print(f"Error: {e}")

calc()