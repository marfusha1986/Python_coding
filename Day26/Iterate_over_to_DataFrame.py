student_dict = {
    'student':['Angela','James','Lily'],
    'score':[56,76,98]
}

#Looping through dictionary
for (key,value) in student_dict.items():
    print(key)
    print(value)

import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)


#Loop through DataFrame
# for (key,value) in student_df.items():
#     print(key)
#     print(value)

#Loop through rows of a DataFrame
for(index,row) in student_df.iterrows():
    if row.student == 'Angela':
        print(row.score)
    print(row)
    print(row.student)


