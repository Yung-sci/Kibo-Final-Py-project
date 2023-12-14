# Simple Ticket Reservation System without

# Create a dictionary to store reservation history.
reservation_history = {}

# Initialize available seats.
available_seats = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

# Main Program

while True:
    print("1. Display Available Seats")
    print("2. Book a Seat")
    print("3. Cancel Booking")
    print("4. View Reservation History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # 1. Display Available Seats
    if choice == "1":
        print("Available Seats:")
        for seat in available_seats:
            print(seat, end=" ")
        print("\n")

    # 2. Book a Seat
    elif choice == "2":
        seat_to_book = input("Enter the seat you want to book: ")
        if seat_to_book in available_seats:
            available_seats.remove(seat_to_book)
            print(f"Seat {seat_to_book} booked successfully.")

            # Store reservation in history
            if "guest" not in reservation_history:
                reservation_history["guest"] = []
            reservation_history["guest"].append({"seat": seat_to_book})
        else:
            print(f"Seat {seat_to_book} is not available.")

    # 3. Cancel Booking
    elif choice == "3":
        seat_to_cancel = input("Enter the seat you want to cancel: ")
        if seat_to_cancel not in available_seats:
            available_seats.append(seat_to_cancel)
            print(f"Booking for seat {seat_to_cancel} canceled.")
        else:
            print(f"Seat {seat_to_cancel} is not booked.")

    # 4. View Reservation History
    elif choice == "4":
        if "guest" in reservation_history:
            print("Your Reservation History:")
            for reservation in reservation_history["guest"]:
                print(f"Seat: {reservation['seat']}")
        else:
            print("No reservation history found.")

    # 5. Exit
    elif choice == "5":
        print("Exiting the Ticket Reservation System. Goodbye!")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
