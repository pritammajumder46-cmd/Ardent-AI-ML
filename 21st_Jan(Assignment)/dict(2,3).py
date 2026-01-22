# Given a dictionary of students and marks, update the marks of one student

student_data = {
    'Marks': {
        'Misti Sarkar' : 95, 
        'Pritam Majumder' : 89,
        'Santanu Das' : 90,
        'Amrita Das' : 90
    }
}
print(f"\nStudent marks data : {student_data}")
student_data['Marks']['Misti Sarkar'] = 99
print(f"Updated student marks data :{student_data}\n")

# Add a new key grade to an existing dictionary and assign it a value.

student_data.update({
    'Grade' : {
        'Misti Sarkar': 'A+',
        'Pritam Majumder' : 'A+',
        'Santanu Das' : 'A+',
        'Amrita Das' : 'A+'
    }
})
print(f"Updated and added Grade in student Dictionary :{student_data}\n")
