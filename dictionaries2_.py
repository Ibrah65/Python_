#Patients details in calculating dictionaries
patient_details= {
    'name' : 'mutahi',
    'id': 783927,
    'location':'kiambu'
}
print(patient_details)
print(patient_details['name'])
x = patient_details.get('county', 'does not exist')
print(x)
#for key in student.keys():
   # print(key)
##  print(value)
for key, value in patient_details.items():
    #print(key, ":" ,value)
    print (str(key)+ ":" + str(value))