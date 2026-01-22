# Create a dictionary with student roll numbers as keys and names as values. Display the dictionary.

student_data = {
    100 : 'Pritam Majumder' ,
    101 : 'Misti Sarkar', 
    102 : 'Angika Banerjee'
}

for keys,values in student_data.items():
    print(f"{keys} : {values}")