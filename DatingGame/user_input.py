# Part 1 : Asks for user info

""" print('Welcome to Dating Simulator 2020')
gender = str(input('Are you Male or Female?(M/F) : '))
partner_gender=str(input('Are you interest in Male or Female?(M/F) : '))
name = str(input("What's your name? "))
age = int(input("What's your age? "))
print(
    f"Hi {name}, let's move on to some other question regarding your dating preferences")
""" 
"""type_1=
type_2=
type_3=  """
# Part 2 : Generating character profile
#list_of_ages = list(range(age, age+10))
list_of_jobs = []
list_of_male_names = []
list_of_female_names = []
list_of_pickup_lines = []  # is male and female pickup lines gonna be diff or same?

partner_1={"name":"","age":"","occupation":"","pickup_line":""}
partner_2={"name":"","age":"","occupation":"","pickup_line":""}
partner_1={"name":"Max","age":"22","occupation":"Chef","pickup_line":"I'll cook for you for the rest of your life!"} 
partner_2={"name":"Joey","age":"24","occupation":"Engineer","pickup_line":"I'll fix it for you!"}
partner_3={"name":"Melodee","age":"22","occupation":"Pilot","pickup_line":"Love it!"}# should we add a short character description?
print('Now let introduce your 3 partners')
print("--------------------------------")
partners=[partner_1,partner_2, partner_3]
partner_no=1
for partner in partners:
    print(str(partner_no)+")")
    partner_no+=1
    for key,value in partner.items():
        print(f"{key:<15}  {value}")
    print("--------------------------------")
    print()
#print(f'{x:02} {x*x:3} {x*x*x:4}')


# Part 3: Scenario Time!

