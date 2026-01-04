def main():
    # Dictionary: course number and room number
    rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    # Dictionary: course number and instructor
    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    # Dictionary: course number and meeting time
    times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    # Loop until the user chooses to quit
    while True:
        # Display available course numbers
        print("\nAvailable Courses:", ", ".join(rooms.keys()))

        # Prompt user for course number
        course = input("Enter a course number (or Q to quit): ").strip().upper()

        # Quit option
        if course == "Q":
            print("\nProgram exited.")
            break

        # Validate course exists in all dictionaries and if so, print the information for the end user
        if course in rooms and course in instructors and course in times:
            print("\nCourse Information")
            print("------------------")
            print(f"Course Number: {course}")
            print(f"Room Number: {rooms[course]}")
            print(f"Instructor: {instructors[course]}")
            print(f"Meeting Time: {times[course]}")
        else:
            print("Course number not found.")


if __name__ == "__main__":
    main()


