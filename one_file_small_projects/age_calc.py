'''
Creates a simple program that reads your age and calculates 
how old you are in decades and years
'''

'''Loop while to read, save and convert the user input for three times,
if fails, the application shuts down.'''
# create variable to loop control
i = 3

while True:
    # try: reads the input user, save it in the user_age converting into int
    try:
        user_age = input("Enter your age: ")
        age = int(user_age)
        break
    
    # exception: the application prints a message error and control the loop
    except Exception as e:
        i -= 1
        print(f'Invalid number, you have {i} attempts left')
        if i==0:
            print('Shutting down...')
            exit(1)

# calculate the values
decades = age // 10
years = age % 10

# creates a string variable with the text to be displayed
display_text = f'Age: {age}\nDecades: {decades}\nYears: {years}'

# prints the result in the terminal
print(display_text)
