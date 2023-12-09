def find_max_speciality(patients):
    specialities = {"P": "Paediatrics", "E": "ENT", "O":"Orthopadics"}
    speciality_count = {}
    for patient in patients:
        speciality = patient[1]
        speciality_count[speciality] = speciality_count.get(speciality,0) + 1
    max_count = 0
    max_speciality = None
    for speciality,count in speciality_count.items():
        if(count > max_count):
            max_count = count
            max_speciality = speciality
    return specialities.get(max_speciality,"Unkowm")

patients = [ ("222","P"),("223","E"),("333","O"),("444","P"),("555","E"),("777","P")]
max_speciality = find_max_speciality(patients)
print(f"Most of the patients attended hospital for the treatment of {max_speciality}.")