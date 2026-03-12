import os
from database import Database
from logger import log
import time


class Boot:

    def boot(self):

        print("\nMiniDB v1.0")
        time.sleep(0.9)

        print("Loading database engine...")
        time.sleep(0.9)

        print("Initializing storage...")
        time.sleep(0.8)

        print("System ready.\n")
        time.sleep(0.6)

        print("Type 'help' to see commands.")
        print("press 'exit' to leave\n")

        log (f"Data Base Started.")

    def main(self):

        self.boot()

        db = Database()

        commands = {
                    "help": db.help,
                    "create_table": db.create_table,
                    "view_table_data": db.view_data,
                    "show_tables": db.show_tables,
                    "delete_table": db.delete_table,
                    "insert": db.insert,
                    "select": db.select,
                    "update": db.update,
                    "delete": db.delete
                    }   

        while True:

            command = input("DB> ").strip()

            log (f"User used '{command}'.")

            if not command:
                continue

            if command == "exit":
                print("Shutting down DataBase...")

                log(" DataBase shut down successfully")
                break

            if command == "clear":
                os.system("cls" if os.name == "nt" else "clear")

                log ("Chat cleared.")
                continue

            parts = command.split()
            cmd = parts[0]

            if cmd in commands:
                commands[cmd](parts)

            else:
                print("Unknown command. Type 'help'.")

                log ("Invalid command type.")

b = Boot()

if __name__ == "__main__":
    b.main()