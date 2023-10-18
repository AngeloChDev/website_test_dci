# Testing

## Topics covered

Unit tests.

## Goal achieved

By the end of the exercise you will have defined a set of unit tests to ensure the classes, objects and some of the functions in the main script work as expected.

When you do further changes in future occasions, you can always run the tests again to make sure nothing broke during the changes.

## Data

You will use the data and code already produced so far in the individual project.

## Description

This time the aim of the exercise is not to refactor the code, but you may need to change small things to make your code pass all tests.

Create a new directory named `tests` where you will define tests for the classes and the main script.

Create tests for the following:

### 1. Classes

1. The **naming of all classes**. Make sure there are 4 classes named User, Employee, Warehouse and Item.
1. The **class inheritance** between User and Employee. Make sure an Employee inherits from the User.
1. The **User class**. Test the following:
    - A user can be created without any argument, in which case it will be named `Anonymous`.
    - A user can be created with a `user_name`, and its `_name` property should have the same value.
    - A user can be created with a `user_name` and a `password` and the password will have no effect.

    In all cases, the property `is_authenticated` should be automatically set to `False`. Calling the `authenticate` method will still set `is_authenticated` to `False`.

1. The **Employee class**. Test the following:
    - An employee without a `password` or a `user_name` is treated as a standard user (`is_authenticated` is always `False` and `head_of` is `None`).
    - An employee with a `user_name` and `password` will have the `is_authenticated` property set to `True` after calling `authenticate` with the appropriate password. The `head_of` will be set to an empty list.
    - An employee with `user_name`, `password` and `head_of` arguments, will have a `head_of` property as a list with `Employee` objects.

1. The **Warehouse class**. Test the following:
    - A warehouse can be created with no argument and the property `id` is set to `None`.
    - A warehouse can be created with a `warehouse_id` argument and the property `id` contains the same value.
    - When a warehouse is created, the `stock` property is a list, an empty one.
    - Make sure the method `occupancy` returns the same as the length of the `stock` property.
    - When the `add_item` method is used with an `Item` object, the total amount of items in stock is increased.
    - The `search` method works as expected.
        - Add a couple of items and then execute a search that returns only some of them. Test the result of the `search` method.
        - Make sure the search works on the combination of the item fields `state` and `category`.
        - Make sure the search is case insensitive.

1. The **Item class**. Test the following:

    - Make sure the `state`, `category` and `date_of_stock` arguments are stored as properties of the object.
    - Make sure that when we cast the object into a string (when the \__str__ method is called), the text shows the combination of `state` and `category`.

### 2. Query script

Test the functions in your query script to make sure it returns or prints the expected values.

To test the query script you will have to mock the way the `input` and `print` functions work. Copy the following code at the top of your test file.

```
from contextlib import contextmanager


@contextmanager
def mock_input(mock):
    original_input = __builtins__.input
    __builtins__.input = lambda _: mock
    yield
    __builtins__.input = original_input


@contextmanager
def mock_output(mock):
    original_print = __builtins__.print
    __builtins__.print = lambda *value: [mock.append(val) for val in value]
    yield
    __builtins__.print = original_print
```

These two functions will temporarily replace the built-in functions `input` and `print`.

The `mock_input` function takes an argument that will be the value the simulated user inputs.

The `mock_output` function replaces the print function with a lambda function that simply appends each text passed to the print function as an element in the `mock` list.

On your tests, you can use the `mock_input` function in the following way:

```
def a_function_to_be_tested()
    return input("Answer yes or no")

class MyTest(unittest.TestCase):

    def test_a_function_to_be_tested(self):
        with mock_input("yes"):
            answer = a_function_to_be_tested()
            self.assertEqual(answer, "yes")
```

And you can use the `mock_output` function in the following way:

```
def a_function_to_be_tested()
    answer = input("Answer yes or no")
    print(answer)

class MyTest(unittest.TestCase):

    def test_a_function_to_be_tested(self):
        with mock_input("yes"):
            answer = []
            with mock_output(answer):
                a_function_to_be_tested()
                self.assertEqual(answer[0], "yes")
```

Test at least the following functions:

1. **get_user**

    - When the user answers with a name that is not in the employees list, the `_name` of the user is the given one and the object returned by the function is an instance of the User class but not an instance of the Employee class.
    - When the user answers with a name that is in the employees list, the `_name` of the user is the given one and the object returned by the function is an instance of the User class as well as an instance of the Employee class.

2. **get_selected_operation**

    - Make sure the output printed contains all the options available.
    - Make sure the function returns the chosen operation.

3. **list_items_by_warehouse**

    - Make sure the function returns a string saying "Listed 5000 items".
    - Make sure the last lines of the printed output are:

        Total items in warehouse 1:
        1346
        Total items in warehouse 2:
        1258
        Total items in warehouse 3:
        1173
        Total items in warehouse 4:
        1223

4. **search_item**

    - Confirm that the call to this function returns the same amount of results for each warehouse as a search on each `warehouse.search` method.

5. **print_warehouse_list**

    - Check the amount of items printed for each warehouse. It should be equal to the amount of items in stock in that warehouse.

6. **employees_only**

    - Make sure the decorator works as expected by calling the decorated function `place_an_order` with a user that is not an employee. Then confirm that it does not print anything and returns `None`.
