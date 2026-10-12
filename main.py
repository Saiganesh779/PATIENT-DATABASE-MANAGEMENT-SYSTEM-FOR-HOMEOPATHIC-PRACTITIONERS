
import csv


class PatientDatabase:

    def __init__(self, filename="patients.csv"):
        self.filename = filename
        self.patients = {}
        self.load_data()

    def save_data(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "name",
                "book_number",
                "page_number",
                "phone",
                "dob"
            ])

            for name, details in self.patients.items():
                writer.writerow([
                    name,
                    details["book_number"],
                    details["page_number"],
                    details["phone"],
                    details["dob"]
                ])

    def load_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    self.patients[row["name"]] = {
                        "book_number": row["book_number"],
                        "page_number": row["page_number"],
                        "phone": row["phone"],
                        "dob": row["dob"]
                    }

        except FileNotFoundError:
            pass

    def add_patient(self, name, book_number, page_number, phone, dob):

        if name in self.patients:
            print(f"Patient '{name}' already exists.")
            return

        if not phone.isdigit():
            print("Invalid phone number. Please enter digits only.")
            return

        # Check DOB format
        try:
            parts = dob.split("-")

            if len(parts) != 3:
                raise ValueError

            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])

            if not (1900 <= year <= 2026):
                raise ValueError

            if not (1 <= month <= 12):
                raise ValueError

            if not (1 <= day <= 31):
                raise ValueError

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            return

        self.patients[name] = {
            "book_number": book_number,
            "page_number": page_number,
            "phone": phone,
            "dob": dob
        }

        self.save_data()

        print(f"Patient '{name}' added successfully.")

    def find_patient(self, search_term, search_type="name"):

        found = False

        for name, details in self.patients.items():

            if (
                search_type == "name"
                and name.lower() == search_term.lower()
            ) or (
                search_type == "phone"
                and details["phone"] == search_term
            ) or (
                search_type == "dob"
                and details["dob"] == search_term
            ):

                found = True

                print("\nPatient:", name)
                print("Book Number:", details["book_number"])
                print("Page Number:", details["page_number"])
                print("Phone Number:", details["phone"])
                print("Date of Birth:", details["dob"])

        if not found:
            print(
                f"No patient found with "
                f"{search_type}: {search_term}"
            )

    def list_patients(self):

        if not self.patients:
            print("No patients in the database.")
            return

        for name, details in self.patients.items():

            print("\nName:", name)
            print("Book Number:", details["book_number"])
            print("Page Number:", details["page_number"])
            print("Phone Number:", details["phone"])
            print("Date of Birth:", details["dob"])


def main():

    database = PatientDatabase()

    while True:

        print("\nMenu:")
        print("1. Add Patient")
        print("2. Find Patient by Name")
        print("3. Find Patient by Phone Number")
        print("4. Find Patient by Date of Birth")
        print("5. List All Patients")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("Enter patient's name: ")
            book_number = input("Enter book number: ")
            page_number = input("Enter page number: ")
            phone = input("Enter phone number: ")
            dob = input(
                "Enter date of birth (YYYY-MM-DD): "
            )

            database.add_patient(
                name,
                book_number,
                page_number,
                phone,
                dob
            )

        elif choice == "2":

            name = input(
                "Enter patient's name to find: "
            )

            database.find_patient(
                name,
                search_type="name"
            )

        elif choice == "3":

            phone = input(
                "Enter patient's phone number to find: "
            )

            database.find_patient(
                phone,
                search_type="phone"
            )

        elif choice == "4":

            dob = input(
                "Enter patient's date of birth "
                "(YYYY-MM-DD) to find: "
            )

            database.find_patient(
                dob,
                search_type="dob"
            )

        elif choice == "5":

            database.list_patients()

        elif choice == "6":

            print("Exiting program.")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()