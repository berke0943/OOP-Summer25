student1= {
    'first_name':'Berke',
    'last_name':'Haliloglu',
    'index_number':'35274',
    'nationality':'Turkish',
    'starting_date':'03-09-2024',
    'courses':["mathematics","English","computer science"]
    }

student2 ={
'first_name' : "Serra",
'last_name' : "Ozbek",
'index_number' : 35248,
'nationality' : "Turkey",
'starting_date' : '03.11.2024',
'courses' : ["math","computer science", "english"]
}
student3 ={
'first_name' : "Sirri",
'last_name' : "Cataloglu",
'index_number' : 34854,
'nationality' : "Turkey",
'starting_date' : '03.09.2024',
'courses' : ["math","computer science", "english"]
}
student4 ={
'first_name' : "Sandugash",
'last_name' : "Nurbolat",
'index_number' : 35176,
'nationality' : "Kazakhstan",
'starting_date' : '2024-09-01',
'courses' : ["Object-oriented programming", "Math", "Logic", "English"]
}
student5 ={
'first_name' : "Madinabonu",
'last_name' : "Jaloldinova",
'index_number' : 35485,
'nationality' : "Uzbek",
'starting_date' : '13-10-2024',
'courses' : ["Math","Basics of digital technology", "Basics of Marketing","Basics of telecommunications", "English ours II", "Ethics", "Logistics", "Object-oriented programming"]
}

students = [student1,student2, student3, student4,student5]


for student in students:
    full_name = student['first_name'] + ' ' + student['last_name']
    print(f"Name: {full_name}, Index Number: {student['index_number']}")