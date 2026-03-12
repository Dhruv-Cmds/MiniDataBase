import os
import json
from logger import log

# easy to use it again
BASE_DIR = "database"

class Database:

    # Main help cmd center
    def help(self ,args):

        print("\nAvailable commands\n")

        print("Database:")
        print(" create_table")
        print(" view_table_data")
        print(" show_tables")
        print(" delete_table\n")

        print("Data:")
        print(" insert")
        print(" select")
        print(" update")
        print(" delete\n")

        print("System:")
        print(" clear")
        print(" help")
        print(" exit\n")

    # From here can create_table
    def create_table(self, args):

        table_name = input("Enter Table name: ").strip()

        columns = input("Enter columns (comma separated): ").strip()

        # Used to creat all intermediate level directories in specified path
        os.makedirs(BASE_DIR, exist_ok=True)

        file_path = f"{BASE_DIR}/{table_name}.json"

        data = {
            "columns": ["id"] + columns.split(","),
            "rows": []
        }

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Table '{table_name}' created successfully.")

        log(f"Table '{table_name}' created successfully.")
        

    # From here can see table
    def show_tables(self, args):

        if not os.path.exists(BASE_DIR):

            print("No tables exist.")

            log("No tables exist.")

            return

        tables = os.listdir(BASE_DIR)

        if not tables:
            print("No tables found.")

            log("No tables found.")

            return

        print("\nTables:\n")

        for table in tables:
            print(table.replace(".json", ""))

            log(table.replace(".json", ""))
    
    # Used to check specific data inside .json file
    def view_data(self ,args):

        table_name = input("Enter Table name to see: ").strip()

        file_path = f"{BASE_DIR}/{table_name}.json"

        if not os.path.exists(file_path):
            print("Invalid file path")

            log ("File path not found.")
        
        else:
        
            with open(file_path, "r") as f:
                data = json.load(f)

            print(json.dumps(data, indent=4))

            log(f"Data added to file successfully.")

            print(f"\nTable '{table_name}' seen.")

            log(f"\nTable '{table_name}' seen.")

    # From here can delete table 
    def delete_table(self, args):
        
        table_name = input("Enter Table name to delete: ").strip()

        file_path = f"{BASE_DIR}/{table_name}.json"

        if not os.path.exists(file_path):

            print("Invalid file path")

            log ("File path not found.")
        
        else:

            # To insure user really want to delete folder
            confirm = input("Are you sure to delete folder? (y/n): ").strip().lower() # lower ensure user input stay small

            # Permission check
            if confirm == 'y':
                os.remove(file_path)
                print(f"\nTable '{table_name}' Deleted successfully.")

                log(f"\nTable '{table_name}' Deleted successfully.")
                
            elif confirm == 'n':
                print("Delete command Terminated.")

                log("Delete command Terminated.")
                return

    def insert(self, args):
       
        table_name = input("Enter Table name to insert information: ").strip()

        file_path = f"{BASE_DIR}/{table_name}.json"

        if not os.path.exists(file_path):
            print("Invalid file path")

            log ("File path not found.")
        
        else:

            with open(file_path, "r") as f:
                data = json.load(f)

            row = {}

            #auto generate id
            new_id = str(len(data["rows"]) + 1)
            row["id"] = new_id

            for column in data["columns"]:
                if column == "id":
                    continue

                value = input(f"{column}: ")
                row[column] = value

            # allow new columns dynamically
            extra = input("Add new column? (name=value or blank): ").strip()

            if "=" in extra:
                key, value = extra.split("=", 1)

                if key not in row:  # prevent overwrite
                    if key not in data["columns"]:
                        data["columns"].append(key)

                    row[key] = value
                else:
                    print("Column already exists")

                    log("Column already exists")

            elif extra:
                print("Invalid column format")

                log("Invalid column format")

            data["rows"].append(row)

            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)

            print("Data inserted successfully.")

            log("Data inserted successfully.")

    def select(self, args):

        table_name = input("Enter Table name to view: ").strip()

        file_path = f"{BASE_DIR}/{table_name}.json"

        if not os.path.exists(file_path): 
            print("Invalid file path")

            log ("File path not found.")
        
        else:

            with open(file_path, "r") as f:
                data = json.load(f)

            if not data["rows"]:
                print("No data to show.")
                log("No data to show.")
                return

            for row in data["rows"]:

                print(row)

                log(f'{row}')

    def update(self, args):

        table_name = input("Enter Table name: ").strip()

        file_path = f"{BASE_DIR}/{table_name}.json"

        if not os.path.exists(file_path): 
            print("Invalid file path")

            log ("File path not found.")
        
        else:

            with open(file_path, "r") as f:
                data = json.load(f)

            student_id = input("Enter id to update: ").strip()

            for row in data["rows"]:
                if row["id"] == student_id:
                    for column in data["columns"]:
                        if column != "id":
                            new_value = input(f"New {column}: ")
                            row[column] = new_value

            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)

            print("Row updated.")

            log("Row updated.")

    def delete(self, args):
    
        table_name = input("Enter Table name: ").strip()

        file_path = f"{BASE_DIR}/{table_name}.json"

        if not os.path.exists(file_path): 
            print("Invalid file path")

            log ("File path not found.")
        
        else:

            with open(file_path, "r") as f:
                data = json.load(f)

            student_id = input("Enter id to delete: ").strip()

            # verify row exists
            exists = any(row["id"] == student_id for row in data["rows"])

            if not exists:
                print("Student not found.")

                log("Student not found.")
                return
            
            confirm = input("Are you sure (y/n): ").strip().lower() # lower ensure user input stay small

            if confirm == 'y':
                data["rows"] = [row for row in data["rows"] if row["id"] != student_id]

                with open(file_path, "w") as f:
                    json.dump(data, f, indent=4)

                print("Row deleted.")

                log("Row deleted.")
            
            elif confirm == 'n':
                print("Delete command Terminated.")

                log("Delete command Terminated.")
            
            else:
                return