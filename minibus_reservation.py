class Minibus:
    def __init__(self, id, stops, seats):
        """
        Constructor to initialize Minibus attributes.
        :param id: Unique ID for the Minibus
        :param stops: List of stops the Minibus will pass through
        :param seats: Total number of seats in the Minibus
        """
        self.id = id
        self.stops = stops
        self.seats = [None] * seats  # Initialize all seats as None (available)

    def reserve_seat(self, client_name):
        """
        Reserve a seat for a client if available.
        :param client_name: Name of the client making the reservation
        :return: True if the reservation is successful, False otherwise
        """
        for i in range(len(self.seats)):
            if self.seats[i] is None:  # Check for an available seat
                self.seats[i] = client_name  # Assign the seat to the client
                return True
        return False  # No available seats

    def available_seats(self):
        """
        Get the count of available seats in the Minibus.
        :return: Number of available seats
        """
        return self.seats.count(None)

    def display_info(self):
        """
        Display Minibus details.
        """
        print(f"Minibus ID: {self.id}")
        print(f"Stops: {', '.join(self.stops)}")
        print(f"Available Seats: {self.available_seats()}/{len(self.seats)}")


# List to store all Minibus objects
minibuses = []

def add_minibus():
    """
    Add a new Minibus to the system (Admin functionality).
    """
    id = input("Enter Minibus ID: ")
    stops = input("Enter stops (comma-separated): ").split(",")  # Convert input to list of stops
    seats = int(input("Enter number of seats: "))
    minibuses.append(Minibus(id, stops, seats))  # Create and store the Minibus object
    print("Minibus added successfully!")

def client_booking():
    """
    Book a seat for a client based on Minibus ID.
    """
    minibus_id = input("Enter Minibus ID: ")
    client_name = input("Enter your name: ")
    for bus in minibuses:  # Search through the Minibuses
        if bus.id == minibus_id:  # Check if the Minibus ID matches
            if bus.reserve_seat(client_name):  # Attempt to reserve a seat
                print("Seat reserved successfully!")
            else:
                print("No available seats.")
            return
    print("Minibus not found.")  # If the Minibus ID doesn't exist

def display_all_minibuses():
    """
    Display all Minibuses and their details.
    """
    if not minibuses:  # Check if the list is empty
        print("No minibuses available.")
        return
    for bus in minibuses:  # Display information for each Minibus
        bus.display_info()
        print("-" * 30)

def main_menu():
    """
    Main menu for the reservation system.
    """
    while True:
        print("\nMain Menu:")
        print("1. Add Minibus (Admin)")
        print("2. Book Seat (Client)")
        print("3. Display All Minibuses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_minibus()
        elif choice == "2":
            client_booking()
        elif choice == "3":
            display_all_minibuses()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
