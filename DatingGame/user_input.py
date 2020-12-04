# Part 1 : Asks for user info
import random

print('Welcome to Dating Simulator 2020')
gender = str(input('Are you Male or Female?(M/F) : '))
partner_gender=str(input('Are you interest in Male or Female?(M/F) : '))
name = str(input("What's your name? ")) 
age = int(input("What's your age? "))


print(f"Hi {name}, let's move on to some other questions regarding your dating preferences")
print("Make your choices by answering 1 or 2.")
list_of_chosen_types=[]
type_1 = int(input("Do you prefer your partner to be 1) atlethic or 2) artistic?  "))
if type_1==1:
    list_of_chosen_types.append("atlethic")
elif type_1==2:
    list_of_chosen_types.append("artistic")

type_2 = int(input("Do you prefer your partner to be an 1) introvert or 2) extrovert?  "))
if type_2==1:
    list_of_chosen_types.append("introvert")
elif type_2==2:
    list_of_chosen_types.append("extrovert")

type_3 = int(input("Do you prefer your partner to be 1) adventurous or 2) conservative?  "))
if type_3==1:
    list_of_chosen_types.append("adventurous")
elif type_3==2:
    list_of_chosen_types.append("conservative")
# Part 2 : Generating character profile
list_of_all_types = ['athletic', 
                     'artistic', 
                     'introvert', 
                     'extrovert', 
                     'adventurous', 
                     'conservative']
#list_of_non_types = [x for x in list_of_all_types if x not in list_of_chosen_types]
list_of_ages = list(range(age if age <= 21 else age - 3, age+5))
list_of_jobs = ['Accountant', 
                'Social worker', 
                'Computer Scientist', 
                'Teacher', 
                'Sales manager', 
                'Architect', 
                'Research scientist', 
                'Entreprenuer', 
                'Doctor', 
                'Nurse', 
                'Cafe Owner', 
                'Model', 
                'Dentist',
                "Interior Designer",
                "Engineer",
                "Influencer",
                "Freelance Photographer"]
list_of_male_names = ['Justin', 
                      'Xavier', 
                      'Damien',
                      'Adrian',
                      'Ryan',
                      'Nicholas',
                      'Alex',
                      'Joshua',
                      'De Ren',
                      'Joseph',
                      'Zi Long',
                      'Wei Jie',
                      'Karthik',
                      'Muhammad',
                      'Danial',
                      'Ahmad',
                      'Rohit',
                      'Sean',
                      'Michael',
                      'Wen Hao',
                      'Zhen Rong',
                      'Isaac',
                      'Hasrul',
                      'Eric',
                      'Ian',
                      'Christopher']
list_of_female_names = ['Melody',
                        'Melodie',
                        'Hui Min',
                        'Rachel',
                        'Jia Wen',
                        'Jasmine',
                        'Michelle',
                        'Ashley',
                        'Jayati',
                        'Maya',
                        'Nichole',
                        'Sarah',
                        'Atika',
                        'Anyana',
                        'Jing Yi',
                        'Grace',
                        'Jing Wen',
                        'Emily',
                        'Mei ling',
                        'Joyce',
                        'Samatha',
                        'Isabelle',
                        'Suraya',
                        'Trishna']                      
list_of_pickup_lines = []  # is male and female pickup lines gonna be diff or same?

partner_1={"name":"","age":"","occupation":"","personality":""}
partner_2={"name":"","age":"","occupation":"","personality":""}
partner_3={"name":"","age":"","occupation":"","personality":""}
# partner_1={"name":"Max","age":"22","occupation":"Chef","pickup_line":"I'll cook for you for the rest of your life!"} 
# partner_2={"name":"Joey","age":"24","occupation":"Engineer","pickup_line":"I'll fix it for you!"}
# partner_3={"name":"Melodee","age":"22","occupation":"Pilot","pickup_line":"Love it!"}# should we add a short character description?

print('Now let introduce your 3 partners')
print("--------------------------------")
partners=[partner_1,partner_2, partner_3]
for partner in partners:
    partner["occupation"] = random.choice(list_of_jobs)
    partner["age"] = random.choice(list_of_ages)
    partner["name"] = random.choice(list_of_male_names if partner_gender.upper() == 'M' else list_of_female_names)
    personality_type=random.choice(list_of_chosen_types)
    partner["personality"] = personality_type
    list_of_chosen_types.remove(personality_type)
partner_no=1
for partner in partners:
    print(str(partner_no)+")")
    partner_no+=1
    for key,value in partner.items():
        print(f"{key:<15}  {value}")
    print("--------------------------------")
    print()



# Part 3: Scenario Time!

