import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


VALID_EVENT_TYPES = ["wedding", "corporate", "birthday"]
VALID_STATUSES    = ["planning", "ongoing", "completed", "cancelled"]


class SocialCanvas:

    def add_event(self):
        print("\n--- Add New Event ---")
        event_name = input("Enter event name: ").strip()
        event_date = input("Enter event date (YYYY-MM-DD): ").strip()

        print(f"Event types: {', '.join(VALID_EVENT_TYPES)}")
        event_type = input("Enter event type: ").strip().lower()
        if event_type not in VALID_EVENT_TYPES:
            print(f"Invalid event type. Choose from: {', '.join(VALID_EVENT_TYPES)}")
            return

        location = input("Enter location: ").strip()
        budget   = input("Enter budget (or press Enter to skip): ").strip()
        budget   = float(budget) if budget else None
        user_id  = input("Enter user ID: ").strip()

        try:
            conn   = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO events (user_id, event_name, event_type, event_date, location, budget, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (user_id, event_name, event_type, event_date, location, budget, "planning"))
            conn.commit()
            cursor.close()
            conn.close()
            print(f"\nEvent '{event_name}' added successfully!")
        except Exception as e:
            print(f"Error adding event: {e}")

    def view_events(self):
        try:
            conn   = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT event_id, event_name, event_type, event_date, location, budget, status
                FROM events
                ORDER BY event_date ASC
            """)
            events = cursor.fetchall()
            cursor.close()
            conn.close()

            if not events:
                print("\nNo events found.")
            else:
                print("\n--- Upcoming Events ---")
                for idx, (event_id, name, etype, date, location, budget, status) in enumerate(events, start=1):
                    budget_str = f"₦{budget:,.2f}" if budget else "N/A"
                    print(f"{idx}. [{event_id}] {name} | {etype} | {date} | {location} | Budget: {budget_str} | Status: {status}")

            return events

        except Exception as e:
            print(f"Error fetching events: {e}")
            return []

    def update_status(self):
        print("\n--- Update Event Status ---")
        events = self.view_events()
        if not events:
            return

        try:
            event_index = int(input("\nEnter the event number to update: ")) - 1
            if 0 <= event_index < len(events):
                event_id   = events[event_index][0]
                event_name = events[event_index][1]

                print(f"Statuses: {', '.join(VALID_STATUSES)}")
                new_status = input("Enter new status: ").strip().lower()

                if new_status not in VALID_STATUSES:
                    print(f"Invalid status. Choose from: {', '.join(VALID_STATUSES)}")
                    return

                conn   = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE events SET status = %s WHERE event_id = %s",
                    (new_status, event_id)
                )
                conn.commit()
                cursor.close()
                conn.close()
                print(f"Status for '{event_name}' updated to '{new_status}'.")
            else:
                print("Invalid event number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error updating status: {e}")

    def delete_event(self):
        print("\n--- Delete Event ---")
        events = self.view_events()
        if not events:
            return

        try:
            event_index = int(input("\nEnter the event number to delete: ")) - 1
            if 0 <= event_index < len(events):
                event_id   = events[event_index][0]
                event_name = events[event_index][1]

                confirm = input(f"Are you sure you want to delete '{event_name}'? (y/n): ").strip().lower()
                if confirm != "y":
                    print("Deletion cancelled.")
                    return

                conn   = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM events WHERE event_id = %s", (event_id,))
                conn.commit()
                cursor.close()
                conn.close()
                print(f"Event '{event_name}' deleted successfully!")
            else:
                print("Invalid event number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error deleting event: {e}")

    def menu(self):
        while True:
            print("\n--- Social Canvas: Event Management ---")
            print("1. Add Event")
            print("2. View Events")
            print("3. Update Event Status")
            print("4. Delete Event")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_event()
            elif choice == "2":
                self.view_events()
            elif choice == "3":
                self.update_status()
            elif choice == "4":
                self.delete_event()
            elif choice == "5":
                print("Exiting Social Canvas. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    app = SocialCanvas()
    app.menu()