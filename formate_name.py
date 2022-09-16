f_name = input("Enter your first name : ")
l_name = input("Enter your last name : ")
def formated_name(first_name,second_name):
    result= f_name.title()
    result2=l_name.title()
    print(f"your final name will be {result} {result2}")
length=len("ali ahmad")
print(f"The length of your name is {length}")

formated_name(first_name=f_name,second_name=l_name)