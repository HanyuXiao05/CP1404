"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    #print(data)
    display_detail(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_list = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data_list.append(parts)
    input_file.close()
    return data_list

def display_detail(data):
    '''display the detail of subject information'''
    max_course_length = max(len(i[0]) for i in data)
    max_name_length = max(len(i[1]) for i in data)
    max_student_length = max(len(str(i[2])) for i in data)
    for i in data:
        print(f'{i[0]:<{max_course_length}} is taught by {i[1]:<{max_name_length}} and has {i[2]:>{max_student_length}} students')
    

main()