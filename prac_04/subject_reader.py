"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_records = load_subject_data(FILENAME)
    # print(subject_records)

    # Display the structured output using the new function
    display_subjects_details(subject_records)

def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    all_subjects =[]

    input_file = open(filename)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        subject_record = [parts[0], parts[1], int(parts[2])]
        # print(data)  # See if that worked
        # print("----------")

        # Append this individual list to our main list
        all_subjects.append(subject_record)

    input_file.close()

    return all_subjects

def display_subjects_details(subjects_list):
    """Display each subject details formatted in clean sentences."""
    for subject in subjects_list:
        # Unpack the items from each inner list
        subject_code = subject[0]
        lecturer_name = subject[1]
        students_count = subject[2]

        # Print using f-string alignment to match your spacing layout
        print(f"{subject_code} is taught by {lecturer_name:<13} and has {students_count:>3} students")

main()
