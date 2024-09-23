#Python dictionary using dict() 'constructor'
student = {
    'name' : 'Ibrahim',
    'Reg_no': 17,
    'email': 'haroibrahim349@gmail.com'
}
#print(student)
#print(student["email"])
#a = student.get('phone_no','does not exist')
#print(a)
#for key in student.keys():
   # print(key)
##  print(value)
for key, value in student.items():
    #print(key, ":" ,value)
    print (str(key)+ ":" + str(value))