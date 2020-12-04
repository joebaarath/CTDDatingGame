# Part 1 : Asks for user info
import random
import sys

def choose_options(qns, options):
    option = ""
    option = input(qns)
    if option not in options:
        message = f'{option} is an invalid option! options are '
        for i in range(len(options)):
            message += options[i]+', '
        print( message + '\nPlease try again.')
        option = choose_options(qns, options)
    return option


player_profile = {'gender':'', 'partner_gender':'', 'name':"", 'age':0}                      
print('Welcome to Dating Simulator 2020') #prints Welcome Message
set_qns_and_answers = [['Are you Male or Female?(M/F) :', ['M','F']],
                      ['Are you interest in Male or Female?(M/F) :', ['M','F']]]
for i, value in enumerate(['gender', 'partner_gender']): #asks basic gender info
    player_profile[value] = choose_options(set_qns_and_answers[i][0], set_qns_and_answers[i][1])
#gender = choose_options(set_qns_and_answers[0][0], set_qns_and_answers[0][1])
#partner_gender=str(input('Are you interest in Male or Female?(M/F) : ')) 
 
while True:
    try:
        player_profile['name'] = str(input("What's your name? "))
        if len(player_profile['name']) == 0 or player_profile['name'].isnumeric() :
            raise Exception
        player_profile['age'] = int(input("What's your age? "))
    except:
        print('invalid input')
    else:
        if player_profile['age'] > 15:
            break
        else:
            print('You are underaged. Seek parental guidance.')
            sys.exit()

print(f"Hi {player_profile['name']}, let's move on to some other questions regarding your dating preferences")
print("Make your choices by answering 1 or 2.")
types_qns_and_answers = [["Do you prefer your partner to be 1) athletic or 2) artistic?  ", ['1','2']],
                         ["Do you prefer your partner to be an 1) introvert or 2) extrovert?  ", ['1','2']],
                         ["Do you prefer your partner to be 1) adventurous or 2) conservative?  ",['1','2']]]
list_of_chosen_types=[]
list_of_all_types = [['athletic', 'artistic'], 
                     ['introvert','extrovert'], 
                     ['adventurous','conservative']]
for i in range(3):
     chosen_type = int(choose_options(types_qns_and_answers[i][0], types_qns_and_answers[i][1]))
     list_of_chosen_types.append(list_of_all_types[i][chosen_type-1])
     
   
# type_1 = int(input("Do you prefer your partner to be 1) athletic or 2) artistic?  "))
# if type_1==1:
#     list_of_chosen_types.append("athletic")
# elif type_1==2:
#     list_of_chosen_types.append("artistic")

# type_2 = int(input("Do you prefer your partner to be an 1) introvert or 2) extrovert?  "))
# if type_2==1:
#     list_of_chosen_types.append("introvert")
# elif type_2==2:
#     list_of_chosen_types.append("extrovert")

# type_3 = int(input("Do you prefer your partner to be 1) adventurous or 2) conservative?  "))
# if type_3==1:
#     list_of_chosen_types.append("adventurous")
# elif type_3==2:
#     list_of_chosen_types.append("conservative")
# Part 2 : Generating character profile

#list_of_non_types = [x for x in list_of_all_types if x not in list_of_chosen_types]
list_of_ages = list(range(player_profile['age'] if player_profile['age'] <= 23 else player_profile['age'] - 5, player_profile['age'] +5))
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
list_of_male_pickup_lines = []  # Melodee fill this in!
list_of_female_pickup_lines = []  # Melodee fill this in!

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
    partner["name"] = random.choice(list_of_male_names if player_profile['partner_gender'] == 'M' else list_of_female_names)
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
partner_choices = [["Please make your choice now   ",['1','2','3']]]
chosen_partner_no= int(choose_options(partner_choices[0][0], partner_choices[0][1]))
chosen_partner = partners[chosen_partner_no-1]
# if chosen_partner_no==1:
#     chosen_partner=partner_1
# elif chosen_partner_no==2:
#     chosen_partner=partner_2
# elif chosen_partner_no==3:
#     chosen_partner=partner_3

# Part 3: Scenario Time!
print(f"You have chosen {chosen_partner['name']}! \nAre you ready to unlock this new journey in knowing {chosen_partner['name']}? ")
# add time lag (press enter to continue story)

print(f"You have just received your first message from  {chosen_partner['name']}! ") 
print("Make your choices by answering 1 or 2.")
print(f"Heyyyy {player_profile['name']} :)")

""" list_of_questions=[[f"I am {chosen_partner['name']}! Looking forward to seeing you tommorow!"],
                    ["So do you have any idea where we should head tomorrow?"],
                    ["So would you like try out some food at a cafe? Or do you wanna head to the beach?"],
                    ["Sounds good! Do you want me to pick you up from your house?"]]
                    
list_of_ans=[["Me too~", "Yes of course! Always excited to meet new friends"],
                ["idk ><","Anywhere that's fun sounds great!"],
                ["Let's go to the cafe then~","Yup! I want to go to Sentosa!"],
                ["Errr it's fine! That sounds pretty inconvenient for you! I'll see you at the beach then!","Sure! See you tomorrow!"]] """

list_of_questions=[[f"I am {chosen_partner['name']}! Looking forward to seeing you tommorow!","Me too~", "Yes of course! Always excited to meet new friends"],
                    ["So do you have any idea where we should head tomorrow?","idk ><","Anywhere that's fun sounds great!"],
                    ["So would you like try out some food at a cafe? Or do you wanna head to the beach?","Let's go to the cafe then~","Yup! I want to go to Sentosa!"],
                    ["Sounds good! Do you want me to pick you up from your house?","Errr it's fine! That sounds pretty inconvenient for you! I'll see you at there!","Sure! See you tomorrow!"]]
                    

score=0
list_of_all_types = ['athletic', 
                     'artistic', 
                     'introvert', 
                     'extrovert', 
                     'adventurous', 
                     'conservative']
list_of_extrovert=['athletic','extrovert','adventurous']
list_of_introvert=[ x for x in list_of_all_types if x not in list_of_extrovert]
for x in range(0,len(list_of_questions)):
    print(list_of_questions[x][0])
    print("1)",list_of_questions[x][1])
    print("2)",list_of_questions[x][2])
    choice=int(choose_options('',['1','2']))
    if chosen_partner["personality"] in list_of_introvert:
        if choice==1:
            score+=1
            #print(score)
        elif choice==2:
            score-=1
            #print(score)
    elif chosen_partner["personality"] in list_of_extrovert:
        if choice==1:
            score-=1
            #print(score)
        elif choice==2:
            score+=1
            #print(score)
        """ print(list_of_questions[x+][0])
        print(list_of_questions[x][1])
        print(list_of_questions[x][2]) """

if score>-2:
    print(f"Have fun on your date with {chosen_partner['name']} tomorrow! ")
elif score <= -2:
    print("Game over bro")