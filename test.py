student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame

print(student_data_frame.to_dict())
