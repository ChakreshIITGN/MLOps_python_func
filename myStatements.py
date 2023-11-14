my_list = ["apple","cherry","lemon"]
my_dict = {"drink":"coffee","milk":"whole"}

for item in my_list:

    print(f'My favourite fruit is {item}')

for _,value in my_dict.items():

    print(f"My favourite thing to drink is {value}")


#my_dict = my_dict
#my_dict2 = my_dict
'''
    There is a pragmatic error in the abovr two lines leading to a bad coding practice - 

    In Python, when you write `d = {1: 2, 2: 3}`, you are creating a dictionary `d` with keys `1` and `2` and corresponding values `2` and `3`. Now, let's analyze the statements `d = d` and `d1 = d`:

    1. **`d = d`:**
    - This statement assigns the dictionary `d` to itself. After this statement, the variable `d` still refers to the same dictionary. However, it doesn't create a new copy of the dictionary; it just makes the variable `d` point to itself.

    ```python
    d = {1: 2, 2: 3}
    d = d  # Now, 'd' still refers to the same dictionary {1: 2, 2: 3}
    ```

    2. **`d1 = d`:**
    - This statement assigns the dictionary `d` to a new variable `d1`. After this statement, both `d` and `d1` refer to the same dictionary. If you modify the dictionary through either `d` or `d1`, the changes will be reflected in both variables.

    ```python
    d = {1: 2, 2: 3}
    d1 = d  # Both 'd' and 'd1' now refer to the same dictionary {1: 2, 2: 3}
    ```

    In summary, there's nothing inherently wrong with these statements, but you should be aware of how Python handles assignments. If you want to create a copy of the dictionary to have independent variables, you can use the `copy` method or the `dict()` constructor:

    ```python
    # Create a shallow copy
    d1 = d.copy()

    # Or use the dict() constructor
    d1 = dict(d)
    ```

    These methods create a new dictionary with the same key-value pairs, allowing you to modify one dictionary without affecting the other.
 
'''