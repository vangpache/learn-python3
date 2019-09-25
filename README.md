# learn-python3
## Basic Hello World w/ Variables & Types:
1. How to make a variable (do variables have types?)
1. Write to console

## Data Structures and Loops:
1. Lists
Python3 'lists' are similar to arrays.
- indices start at 0
- lists are iterated using 'for' and 'while' loops
- loops can also use 'else', 'break', 'continue'

    *ex: myList = [1, 2, 3, 4, 5]*
    ```
    mylist[0] --> 1
    mylist[1] --> 2
    mylist[2] --> 3
    mylist[3] --> 4
    mylist[4] --> 5
    ```

    *ex: for loop (similar to for of loop)*
    ```
    for x in mylist:
        print(x)
    ```
    prints: 1, 2, 3, 4, 5

    *ex: while loop*
    ```
    count = 0
    while count < 5:
        print(count)
        count += 1
    ```
    prints: 0, 1, 2, 3, 4

    #### *adding items to a list*

    ```
    mylist.append(6)
    --> mylist = [1, 2, 3, 4, 5, 6]
    ```
## Functions and Conditionals:

```
#Conditional Statement
num = 7
if num == 5:
    print("Number is 5")
else:
    if num == 11:
        print("Number is 11")
    else:
        if num == 7:
            print("Number is 7")
        else:
            print("Number isn't 5, 11 or 7")

#Function
def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y

sum = add_numbers(3, 5)
print(sum)

#And Operator
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)

#Or Operator
print(1 == 2 or 1 == 1)

#Boolean Not - takes in only one argument and inverts it
print(not 1 == 1)
```

## WhiteBoard problem example:
#### FizzBuzz:
```
y = [3, 5, 15, 4]

for x in y:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0: 
        print("Buzz")
        continue
    print(x)
```

## Instructions to Install Python3  using Homebrew on Mac osx:
1. Open the terminal and confirm that Homebrew is correctly installed by typing in the command: 
    ```
    $ brew doctor
    ```
    If Homebrew is correctly installed the response should be: ```Your system is ready to brew.```

1. Install python3 using the command:
    ```
    $ brew install python3
    ```
    Once Python3 is installed, you may want to confirm you've installed the latest version by typing in the command:
    ```
    $ python3 --version
    ```

1. To open the Python shell from the command line, type:
    ```
    $ python3
    ```

1. Notes:
    - You can also download Python3 here: https://www.python.org/download/releases/3.0/
    - Visual Studio Code requires an extension for Python3. You can find that here: https://marketplace.visualstudio.com/items?itemName=ms-python.python
    - Python3 cheatsheet: https://ehmatthes.github.io/pcc/cheatsheets/README.html 

