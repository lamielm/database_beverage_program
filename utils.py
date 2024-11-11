"""Program Utilities"""

# Internal Imports
from errors import AlreadyImportedError


class CSVProcessor:
    """CSV Processing Class"""

    def __init__(self):
        """Constructor"""
        self._has_been_imported = False

    def import_csv(self, beverage_collection, path_to_csv_file, session):
        """Import CSV and populate beverage collection"""

        # If already imported, raise AlreadyImportedError
        if self._has_been_imported:
            raise AlreadyImportedError

        # With open of file
        with open(path_to_csv_file, "r", encoding="utf-8") as file:
            # Priming line read
            line = file.readline().replace("\n", "")
            # While the line is not None
            while line:
                # Process the line.
                self._process_line(line, beverage_collection)
                # Read next line.
                line = file.readline().replace("\n", "")
            # All lines read and processed, flip flag to true.
            self._has_been_imported = True
        # Removed the session.commit from the "add" method as it was slowing down my program.  It committed after every object.
        session.commit()

    def _process_line(self, line, beverage_collection):
        """Process a line from a CSV file"""

        # Split line by comma
        parts = line.split(",")

        # Assign each part to a var
        item_id = parts[0]
        name = parts[1]
        pack = parts[2]
        price = float(parts[3])
        active = parts[4] == "True"

        # Add a new beverage to the collection with the properties of what was read in.
        beverage_collection.add(item_id, name, pack, price, active)
