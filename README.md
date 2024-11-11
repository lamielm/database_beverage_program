# Assignment 5 - Update the Assignment 1 with Beverages to use a database instead of a CSV

## Author

Landon Lamie

## Description

Either modify what I have in my Assignment 1 key, which is included here, or bring in your files and use those to do the work.

You are going to take the Assignment 1 we did with the Beverage List .CSV and update it to work with a database in conjunction with the CSV. In addition, the UI must be updated to accommodate some new features that were not in assignment 1.

The program should continually run until the user decides to exit (entering a certain character on the keyboard).

The program should allow the following functionality:

1. Loads the information about the Beverages from the CSV file and populates the database. This should only be done if the database file does not already exist. Otherwise, it does nothing as the DB already exists. A message to the user indicating such might be useful.
2. Allow the user to print the entire list of beverages.
3. Allow the user to search for a beverage by the beverage id, and print out the beverage if found. Error message if not.
4. Allow the user to add a new beverage to the list. It should show a nice error message if the user tries to add a beverage with a primary key `id` that is already in the DB.
5. (NEW) Allow the user to update an existing beverage. This will require prompting the user for the information needed for the update.
6. (NEW) Allow the user to delete an existing beverage. It should show a nice error if the delete can not complete. (Deleting by `id` is good enough. If you would like to offer other searches for deletion you can, but are not required to.)

Add the SQLAlchemy package to your project via a virtual environment and PIP. Be sure to dump your installed packages to a requirements.txt file. If I can't easily restore your packages, I may not grade your assignment.

Alter the `Beverage` class to work with SQLAlchemy and set the existing `id` field up as the primary key for the class. In the in-class we were able to add a new field called `id` that was the primary key of the data model. In this assignment, there is already an `id` field. It however, is a string. Not an int. Lower in the README is some information on how to adjust for this change.

You should transform the `BeverageCollection` class into a Repository API. You should rename the class from `BeverageCollection` to `BeverageRepository`. You should make the `BeverageRepository` become a class that sits between the code in the `main` function / `UI` class and the newly altered `Beverage` class. Pretty much the same spot as it did before as `BeverageCollection`. The new `BeverageRepository` will contain all of the SQLAlchemy work. Essentially any work that uses that package should be in the repository class. This way if you ever needed to change the library from SQLAlchemy to something else, there would only be one file that would need to change.

Update the class called `UserInterface` to include any new methods that are required to facilitate the above functionality.

You should also change the option to load the CSV file to an option to initially set up and pre-load the database with some data. In fact, that option to set up the database and pre-load the database with the contents of the CSV file should only be allowed to run if the database does not already exist. Once the database is created and loaded, the user should not be able to run that option again.


Solution Requirements:

* 5 modules (`beverage.py`, `main.py`, `program.py`, `user_interface.py`, `utils.py`)
* 4 classes (`Beverage`, `BeverageRepository`, `CSVProcessor`, and `UserInterface`.
* Repurposed and renamed `BeverageCollection` to `BeverageRepository`
* Read functionality
* Insert functionality
* Update functionality
* Delete functionality
* UI Class to handle I/O

## Notes
In order to make the existing `id` field of the `Beverage` class the primary key, you just need to pass the kwarg for primary key to the field definition. Much like we did for the `id` we added in the in-class. The only difference being that instead of the field being an `Integer`, it will be a `String`.
EX:
```python
id = Column(String(255), primary_key=True)
```

The `active` field for the `Beverage` class should be defined as a `Boolean` field. We did not do one of these in the in-class, but it should be fairly similar to the others we have done. If you need some reference material on how to defined field types, you can refer to the following link. Additionally, you can ask me.

[SQLAlchemy](https://docs.sqlalchemy.org/en/20/core/types.html)

---
REMEMBER TO DUMP YOUR `requirements.txt` FILE.
If I can not restore your packages easily, I will not grade the assignment.

---

## Grading
| Feature                                 | Points |
|-----------------------------------------|--------|
| Updated Beverage class                  | 10     |
| Insert Functionality                    | 10     |
| Update Functionality                    | 10     |
| Delete Functionality                    | 10     |
| List All                                | 10     |
| Search                                  | 10     |
| Repurpose BeverageCollection as API     | 10     |
| UI is updated correctly                 | 10     |
| Handle Errors                           | 5      |
| DB Connection                           | 5      |
| Documentation                           | 5      |
| README                                  | 5      |
| **Total**                               | **100**|

## Outside Resources Used



## Known Problems, Issues, And/Or Errors in the Program

I'm looking for better explanation the "Read, Inser, Update, Delete" functionality portions.  Should I have a delete option?  Or an update option that asks user "Would you like to update an item?