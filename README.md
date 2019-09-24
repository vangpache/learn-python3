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

    *adding items to a list*

    ```
    mylist.append(6)
    --> mylist = [1, 2, 3, 4, 5, 6]
    ```
1. Objects