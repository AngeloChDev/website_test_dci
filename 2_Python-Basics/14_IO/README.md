# Input/Output

## Topics covered

Reading, writing and organizing files and directories.

## Goal achieved

By the end of the exercise your CLI tool will be able to remove items from warehouses when an order is placed and keep a log of all actions taken by users and employees.

These changes will be made persistent by storing the data as JSON files in the file system.

## Steps

### Preparation

**Create the initial JSON files.**

The first thing you will have to do is save each of the data lists (`personnel` and `stock`) in two different JSON files.

These data are now stored as Python objects and this is not appropriate if you want to read and write the data.

Store these files in a new directory named `data` inside the `cli` directory. If the `data` directory does not exist, the script should create it automatically.

Create a new file in the `cli` directory that saves the two lists in two JSON files.

**Set the current code to read the new JSON files.**

Once this is done, replace the file `loader.py` with the one at [resources/mile10/loader.py](resources/mile10/loader.py). This file reads the JSON files and converts them into the objects your query tool is using.

Run your unit tests to make sure everything works. Run the query tool manually as well, in case the unit tests don't cover all features.

### Add Feature: Placing Orders

Change your code so that it actually removes the ordered items from the warehouses in the Python objects.

Make sure these changes survive the session by saving the new state of the data back into the `data/stock.json` file. To do this, you can call the method `stock.to_dict()` that will return a dictionary that you can use to override the `stock.json` file.

> It does not matter which warehouses the items are removed from, but the total amount should be correct after removing them.
>
> List all the items after placing an order and then quit, to see the total amount of items in all warehouses after the order.
>
> Search again the same item after placing an order and confirm the items removed were the correct ones.
>
> Make sure you only remove the items when the employee is authenticated and the required amount is available.

### Add Feature: Logging Actions

Now, when the user or employee end the session you should save the operations performed during that session in two other files in a new directory `cli/log/`, one for users and the other one for employees.

The content in these files should never be overwritten, every time new information is added to the log it should be added at the end of the file.

The content of both files should be using the same format, a list of messages with the following pattern:

`<user>. <operation>. <datetime>.`

Example **employees.log**:

```
Juno. Listed 5000 items. 2021-12-08 19:46:08.645093.
Juno. Searched a Cheap tablet. Ordered 13. 2021-12-08 19:46:20.061800.
Juno. Listed 4987 items. 2021-12-08 19:48:43.709709.
Martha. Listed 4987 items. 2021-12-09 14:32:32.652614.
```
