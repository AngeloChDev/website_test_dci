# Exceptions

## Topics covered

Catching and raising exceptions.

## Goal achieved

You will define your own exceptions when logical errors are produced in your Django project and catch them later to manage them.

## Description

Where to define and catch exceptions will depend a lot on the implementation. Explore your code to identify where to raise and catch exceptions.

Exceptions are often useful in the following situations:

### Raise exceptions on required arguments

When a class requires an argument to be provided on instantiation, sometimes we may want to customize the type of exception and message provided.

**Example:**

Replace the validation of the arguments in the `stock.classes.Employee` class of the solution provided.

Although it works fine right now, the way we notify the caller about a missing argument (`user_name` and `password`) is not appropriate for using in a script.

Instead of printing a message to the console and returning `None` when an argument is missing in the class constructor, it should raise a custom exception.

This way, a parent script using this class could catch and identify the error to find a solution.

Therefore, define a custom exception in the `classes.py` file named `MissingArgument`. This class should have two properties: `argument` and `message`.

The first property will contain the name of the missing argument in the failing instance, and the second property will contain a brief custom message.

When this exception is raised (when the class gets instantiated), both properties must be defined using arguments.

When failing, the output message should look like this:

```
stock.classes.MissingArgument: {argument} is missing. {message}.
```
Examples:
```
stock.classes.MissingArgument: user_name is missing. An employee can not be anonymous.
```
```
stock.classes.MissingArgument: password is missing. An employee requires authentication.
```

Use the Python console to create employees without a user name or password and manually test your exceptions.

Then, add the following test to your `stock.tests` and run it. If it fails, fix it and run it again until it passes.

```python
from . import classes
def test_class_exceptions(self):
    """Test classes exceptions."""
    # An Employee without a user_name raises a MissingArgument exception
    with self.assertRaises(classes.MissingArgument) as context:
        classes.Employee(password="password")
    self.assertEqual(context.exception.argument, "user_name")
    # An Employee without a password raises a MissingArgument exception
    with self.assertRaises(classes.MissingArgument) as context:
        classes.Employee(user_name="Username")
    self.assertEqual(context.exception.argument, "password")
```

### Replace conditional checks with try/except

In some occasions we may use a conditional statement to check if something exists so that we can decide if we need to update it or create it.

Because in Python it is usually "better to ask forgiveness than permission", replace those blocks of code with `try/except` blocks.

**Example:**

In some places of our solution we check if an element already exists in the output to decide if we have to increment its counter or create the new entry.

This happens in the function `stock.views.search_item`:

```python
exists = [i for i in items
          if str(item) == str(i["name"])]
if not exists:
    items.append({
        "name": str(item),
        "amount": 1
    })
else:
    exists[0]["amount"] += 1
```

But also happens in `stock.views.CategoryList.get_context_data`.

Instead of using a conditional statement, use a `try/except` statement to increment the counter at first and create the new entry if it fails.

Then, manually confirm it works by doing a search and inspecting the category list in the browser.

### Raising other exceptions

Some events may not be technically errors, but in some occasions we may want to treat them as such.

**Example:**

You can raise a custom exception on the `stock.views.search_item` function when a search returns 0 results and then catch this exception in the view to use a different template when there are no results.
