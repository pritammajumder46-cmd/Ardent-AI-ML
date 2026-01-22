# Write a program to add a new key-value pair to an existing dictionary

student_data = {
    'Marks': {
        'Misti Sarkar' : 95, 
        'Pritam Majumder' : 89,
        'Santanu Das' : 90,
        'Amrita Das' : 90
    }
}
print(f"\nStudent marks data : {student_data}")

student_data.update({
    'Grade' : {
        'Misti Sarkar': 'A+',
        'Pritam Majumder' : 'A+',
        'Santanu Das' : 'A+',
        'Amrita Das' : 'A+'
    }
})
print(f"Updated and added Grade in student Dictionary :{student_data}\n")