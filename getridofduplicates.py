student_names = {'id1':
        {'name': ['Sara'],
        'class' : ['V'],
        'student_integrations' : ['math,english,science']},     
        'id2':
        {'name': ['David'],
        'class' : ['V'],
        'student_integrations' : ['math,english,science']},    
        'id3':
       {'name': ['Sara'],
        'class' : ['V'],
        'student_integrations' : ['math,english,science']},    
        'id4':
        {'name': ['Suarya'],
        'class' : ['V'],
        'student_integrations' : ['math,english,science']},
     }
result={}
for key,value in student_names.items():
    if value not in result.values():
        result[key]= value
print(result)

