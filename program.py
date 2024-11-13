"""Program code"""

# Internal imports.
from beverage import Beverage, BeverageRepository, session
from errors import AlreadyImportedError
from user_interface import UserInterface
from utils import CSVProcessor
import os
  

# Set a constant for the path to the CSV file
PATH_TO_CSV = "./datafiles/beverage_list.csv"


def main(*args):
    """Method to run program"""

    # Create an instance of User Interface class
    ui = UserInterface()

    # Create an instance of the BeverageRepository class.
    beverage_collection = BeverageRepository()

    # Create an instance of the CSVProcessor class.
    csv_processor = CSVProcessor()

    # Create the database if it doens't already exist
    if not os.path.exists("./db.sqlite3"):
        # Create the database
        beverage_collection.create_database()
    
    # Check to see if there are any records in the DB.  If not, upload Beverages and put them into the DB.
    if session.query(Beverage).first() is None:
        # Load the CSV File
        try:
            csv_processor.import_csv(beverage_collection, PATH_TO_CSV)
            ui.display_import_success()
        except AlreadyImportedError:
            ui.display_already_imported_error()
        except FileNotFoundError:
            ui.display_file_not_found_error()
        except EOFError:
            ui.display_empty_file_error()

    # Display the Welcome Message to the user.
    ui.display_welcome_greeting()

    # Display the Menu and get the response. Store the response in the choice
    # integer. This is the 'primer' run of displaying and getting.
    choice = ui.display_menu_and_get_response()

    

    # While the choice is not exit program
    while choice != 6:
        if choice == 1:
            # Print Entire List Of Items
            all_item_string = str(beverage_collection)
            if all_item_string:
                ui.display_all_items(all_item_string)
            else:
                ui.display_all_items_error()

        elif choice == 2:
            # Search for an Item
            item_found = False
            while item_found != True: # Make an escape if you don't want to search for things anymore
                search_query = ui.get_search_query()
                if search_query == "x":
                    break
                else:
                    item_info = beverage_collection.find_by_id(search_query)
                if item_info: # Make it so that if DB is empty, it states that. Currently crashes program.
                    ui.display_item_found(item_info)
                    item_found = True
                else:
                    ui.display_item_found_error()

        elif choice == 3:
            # Collect information for a new item and add it to the collection
            new_item_info = ui.get_new_item_information()
            if beverage_collection.find_by_id(new_item_info[0]) is None:
                beverage_collection.add(
                    new_item_info[0],
                    new_item_info[1],
                    new_item_info[2],
                    float(new_item_info[3]),
                    new_item_info[4] == "True",
                )
                ui.display_add_beverage_success()
            else:
                ui.display_beverage_already_exists_error()

        elif choice == 4:
            # Update an existing beverage
            item_found = False
            while item_found != True:
                search_query = ui.get_search_query()
                if search_query == "x":
                    break
                item_info = beverage_collection.find_by_id(search_query)
                if item_info:
                    ui.display_item_found(item_info)
                    item_found = True
                    updated_info = ui.update_existing_item_information()
                    beverage_collection.update_existing(
                        search_query, 
                        updated_info[0], 
                        updated_info[1], 
                        updated_info[2],
                        updated_info[3],
                        )
                else:
                    ui.display_item_found_error()

        elif choice == 5:
            # Delete an existing beverage
            item_found = False
            while item_found != True:
                search_query = ui.get_search_query()
                if search_query == "x":
                    break
                item_info = beverage_collection.find_by_id(search_query)
                if item_info:
                    ui.display_item_found(item_info)
                    item_found = True
                    beverage_collection.delete_existing(item_info.id)
                else:
                    ui.display_item_found_error()

        # Get the new choice of what to do from the user.
        choice = ui.display_menu_and_get_response()