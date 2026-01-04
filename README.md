This code displays a list of course numbers and the end-user can key one in to get the instructor, room, and time for the course:

START

Create dictionary Rooms with course_number and room_number
Create dictionary Instructors with course_number and instructor_name
Create dictionary Times with course_number and meeting_time

Start Loop 
    End users may not know the course number, so display what is available
    Display "Available Courses" and list all keys from the rooms dictionary

    Prompt user: "Enter a course number (or Q to quit)"
    Convert input to uppercase and remove extra spaces

    IF user entered "Q"
        Display "Program exited."
        exit loop
    ENDIF

    IF course_number exists in rooms and instructors and times
        Display "Course Information"
        Display Course Number
        Display Room Number from ROOMS
        Display Instructor from INSTRUCTORS
        Display Meeting Time from TIMES
    ELSE
        Display "Error: Course number not found."
    ENDIF
End Loop

END
