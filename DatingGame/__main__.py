import random
import sys
import matplotlib.pyplot as plt
from data_config import *

class player():
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0
        self.partner_gender = ""
        self.preferred_partner_types = []

class partner():
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0
        self.occupation = ""
        self.personality_type = ""

def choose_options(qns_and_options):
    question = qns_and_options[0]
    options = qns_and_options[1]
    option = ""
    option = input(question)
    if option not in options:
        message = f'{option} is an invalid option! options are '
        for i in range(len(options)):
            message += options[i]
            if(i < len(options)-1):
                message += ', '
        print( message + '\nPlease try again.')
        option = choose_options(qns_and_options)
    return option

def randomizePartners(current_player: player(), game_config: data_config() , numOfPartners: int() = 3 ):
    list_of_ages = list(range(current_player.age if current_player.age <= 23 else current_player.age - 5, current_player.age +5))

    temp_player_preferred_partner_types = current_player.preferred_partner_types[:]
    partners = []

    for index in range(numOfPartners):
        p = partner()
        p.age = random.choice(list_of_ages)
        p.occupation = random.choice(game_config.list_of_jobs)
        p.gender = current_player.partner_gender
        p.name = random.choice(game_config.list_of_male_names if current_player.partner_gender == 'M' else game_config.list_of_female_names)
        p.personality_type = random.choice(temp_player_preferred_partner_types)
        temp_player_preferred_partner_types.remove(p.personality_type)
        partners.append(p)

    return partners

def end_game():
    end_game_option = choose_options(['Do you want to 1)restart or 2)exit the game? :', ['1','2']])
    if  end_game_option == '1':
        main()
    else:
        sys.exit()

def main():    
    #Creates a new game settings class object
    game_config = data_config()
    current_player = player()
                     
    print('Welcome to Dating Simulator 2020') 
    current_player.gender = choose_options((game_config.player_profile_questions["gender"]))
    current_player.partner_gender = choose_options((game_config.player_profile_questions["partner_gender"]))
    
    while True:
        try:
            current_player.name = str(input("What's your name? "))
            if len(current_player.name) == 0 or current_player.name.isnumeric() :
                raise Exception
            current_player.age = int(input("What's your age? "))
        except:
            print('invalid input')
        else:
            if current_player.age > 13:
                break
            else:
                print('You are underaged. Seek parental guidance.')
                img = plt.imread('https://www.imda.gov.sg/-/media/Imda/Images/Content/Regulation-Licensing-and-Consultations/Content-Standards-and-classification/Classification-Rating/PG13-Rating.png?la=en&hash=FDB0D0A4021A703C98A3E791D1EA3E9494BB70A7')
                plt.imshow(img)
                plt.show()
                end_game()

    print(f"Hi {current_player.name}, let's move on to some other questions regarding your dating preferences")
    print("Make your choices by answering 1 or 2.")
    
    for i in range(3):
        chosen_type = int(choose_options(game_config.partner_preference_questions[i]))
        current_player.preferred_partner_types.append(game_config.list_of_all_types[i][chosen_type-1])
        
    #list_of_non_types = [x for x in list_of_all_types if x not in player.preferred_partner_types]
    list_of_ages = list(range(current_player.age if current_player.age <= 23 else current_player.age - 5, current_player.age +5))
    
    # partner_1={"name":"Max","age":"22","occupation":"Chef","pickup_line":"I'll cook for you for the rest of your life!"} 
    # partner_2={"name":"Joey","age":"24","occupation":"Engineer","pickup_line":"I'll fix it for you!"}
    # partner_3={"name":"Melodee","age":"22","occupation":"Pilot","pickup_line":"Love it!"}# should we add a short character description?

    print('Now let introduce your 3 partners')
    print("--------------------------------")
    partners= randomizePartners(current_player, game_config , 3)
    partner_no=1

    for p in partners:
        print(str(partner_no)+")")
        partner_no+=1

        #temp fix: convert class to dict
        partnerdict = {key:value for key, value in p.__dict__.items() if not key.startswith('__') and not callable(key)}

        for key,value in partnerdict.items():
            print(f"{key:<15}  {value}")
        print("--------------------------------")
        print()

    partner_choices = ["Please make your choice now   ",['1','2','3']]
    chosen_partner_no= int(choose_options(partner_choices))
    chosen_partner: partner() = partners[chosen_partner_no-1]
    # if chosen_partner_no==1:
    #     chosen_partner=partner_1
    # elif chosen_partner_no==2:
    #     chosen_partner=partner_2
    # elif chosen_partner_no==3:
    #     chosen_partner=partner_3

    # Part 3: Scenario Time!
    print(f"You have chosen {chosen_partner.name}! \nAre you ready to unlock this new journey in knowing {chosen_partner.name}? ")
    # add time lag (press enter to continue story)

    print(f"You have just received your first message from  {chosen_partner.name}! ") 
    print("Make your choices by answering 1 or 2.")
    print(f"Heyyyy {current_player.name} :)")

    """ list_of_questions=[[f"I am {chosen_partner['name']}! Looking forward to seeing you tommorow!"],
                        ["So do you have any idea where we should head tomorrow?"],
                        ["So would you like try out some food at a cafe? Or do you wanna head to the beach?"],
                        ["Sounds good! Do you want me to pick you up from your house?"]]
                        
    list_of_ans=[["Me too~", "Yes of course! Always excited to meet new friends"],
                    ["idk ><","Anywhere that's fun sounds great!"],
                    ["Let's go to the cafe then~","Yup! I want to go to Sentosa!"],
                    ["Errr it's fine! That sounds pretty inconvenient for you! I'll see you at the beach then!","Sure! See you tomorrow!"]] """

    list_of_questions=[[f"I am {chosen_partner.name}! Looking forward to seeing you tommorow!","Me too~", "Yes of course! Always excited to meet new friends"],
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
        choice=int(choose_options(['',['1','2']]))
        if chosen_partner.personality_type in list_of_introvert:
            if choice==1:
                score+=1
                #print(score)
            elif choice==2:
                score-=1
                #print(score)
        elif chosen_partner.personality_type in list_of_extrovert:
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
        print(f"Have fun on your date with {chosen_partner.name} tomorrow! ")
        img = plt.imread('https://upload.wikimedia.org/wikipedia/commons/e/e6/Finger_heart.png')
        plt.imshow(img)
        plt.show()
      
    elif score <= -2:
        print("Game over bro")
        img = plt.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Broken_heart.svg/166px-Broken_heart.svg.png')
        plt.imshow(img)
        plt.show()
        
    end_game()
    
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()