#An Insurance company follows following rules to calculate premium.
# 	a.	If a person’s health is excellent and the person is between 25 and 35 years of age and lives in a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed Rs. 2 lakhs.
# 	b.	If a person satisfies all the above conditions except that the sex is female then the premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
# 	c.	If a person’s health is poor and the person is between 25 and 35 years of age and lives in a village and is a male cannot exceed Rs. 10,000.
# 	d.	In all other cases the person is not insured.
# Write a program to output whether the person should be insured or not, his/her premium rate and maximum amount for which he/she can be insured.

Person_Health = input("Enter health is excellent or poor:")
Person_Age = int(input("Enter age:"))
Person_Gender = input("Enter male or Female:")
Person_Native = input("Enter city or village:")
if(Person_Health == "excellent" and 25<=Person_Age<=35 and Person_Native == "city" ):
  if(Person_Gender == "male"):
    print("Premium is Rs.800 and cannot exceed Rs.2 lakhs ")
  else:
     print("Premium is Rs.300 and cannot exceed Rs.1 lakh ")
elif(Person_Health == "poor" and 25<=Person_Age<=35 and Person_Native == "village"):
  if(Person_Gender == "male"):
    print("cannot exceed Rs.10,000")
  else:
    print("Person is not insured")
else: 
  print("Person is not insured")