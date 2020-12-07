import random
import sys
import matplotlib.pyplot as plt
from data_config import *
from game_class import *
from termcolor import colored

def choose_options(qns_and_options):
    question = qns_and_options[0]
    options = [str(o) for o in qns_and_options[1]] 
    option = ""
    option = str(input(question)).upper()
    if option not in options:
        message = f'{option} is an invalid option! options are '
        for i in range(len(options)):
            message += options[i]
            if(i < len(options)-1):
                message += ', '
        print( message + '\nPlease try again.')
        option = choose_options(qns_and_options)
    return option

def display_image(url):
     img = plt.imread(url)
     plt.imshow(img)
     plt.axis("off")
     plt.show()

def randomize_partners(current_player: player(), game_config: data_config() , num_of_partners: int() = 3 ):
    list_of_ages = list(range(current_player.age if current_player.age <= 23 else current_player.age - 5, current_player.age +5))
    partners = []
    temp_list_of_partner_ages = []
    temp_list_of_partner_occupations = []
    temp_list_of_partner_names = []

    for index in range(num_of_partners):
        p = partner()

        #force unique age
        random_age = random.choice(list_of_ages)
        while random_age in temp_list_of_partner_ages:
            random_age = random.choice(list_of_ages)
        temp_list_of_partner_ages.append(random_age)
        p.age = random_age

        #force unique name
        random_occupation = random.choice(game_config.list_of_jobs)
        while random_occupation in temp_list_of_partner_occupations:
            random_occupation = random.choice(game_config.list_of_jobs)
        temp_list_of_partner_occupations.append(random_occupation)
        p.occupation = random_occupation

        #force unique occupation
        random_name = random.choice(game_config.list_of_male_names if current_player.partner_gender == 'M' else game_config.list_of_female_names)
        while random_name in temp_list_of_partner_names:
            random_name = random.choice(game_config.list_of_male_names if current_player.partner_gender == 'M' else game_config.list_of_female_names)
        temp_list_of_partner_names.append(random_name)
        p.name = random_name

        p.gender = current_player.partner_gender

        temp_player_preferred_partner_types = current_player.preferred_partner_types[:]
        if(game_config.list_of_all_types[index][0] in current_player.preferred_partner_types):
            #Get 1 to be the opposite personality and 2 to be the same
            temp_player_preferred_partner_types.remove(game_config.list_of_all_types[index][0])
            temp_player_preferred_partner_types.append(game_config.list_of_all_types[index][1])
        else:
            #Get 1 to be the opposite personality and 2 to be the same
            temp_player_preferred_partner_types.remove(game_config.list_of_all_types[index][1])
            temp_player_preferred_partner_types.append(game_config.list_of_all_types[index][0])
        
        p.personality_types = sorted(temp_player_preferred_partner_types[:])

        

        partners.append(p)

    return partners

def end_game():
    end_game_option = choose_options(['Would you like to play again?\n\n[1] Restart\n[2] Exit the game\n\nChoice: ', ['1','2']])
    if  end_game_option == '1':
        main()
    else:
        sys.exit(0)

def string_validation(question):
        try:
            user_input = input(question)
            if len(user_input) == 0 or user_input.isnumeric() :
                raise Exception
            return user_input
        except KeyboardInterrupt:
            # quit
            sys.exit(0)
        except:
            print('Please enter a valid name')
            string_validation(question)

def age_validation(question):
        try:
            age = int(input(question))
        except KeyboardInterrupt: #purpose?
            # quit
            sys.exit(0)
        except:
            print('Please enter a valid number')
            print(age)
            age_validation(question)
        else:
            if age <= 13:
                print(colored('You are underaged. Seek parental guidance.','red',attrs=['bold']))
                display_image('https://www.imda.gov.sg/-/media/Imda/Images/Content/Regulation-Licensing-and-Consultations/Content-Standards-and-classification/Classification-Rating/PG13-Rating.png?la=en&hash=FDB0D0A4021A703C98A3E791D1EA3E9494BB70A7')
                end_game()
            return age

def display_partners(partners: []):
    print('Now let introduce your 3 lovely partners...')
    print("----------------------------------------------------------------")
    
    partner_no=1
    for p in partners:
        p_num_and_title = f"[{str(partner_no)}]"
        p_num_and_title = "{:<15}".format(p_num_and_title)
        print(f"{p_num_and_title}{p.name}")
        print("{:<15}".format(f"Age")+ str(p.age))
        print("{:<15}".format(f"Occupation")+ p.occupation)
        
        personalities = ""
        for pt in p.personality_types:
            personalities += ", " + pt
        personalities = personalities[2:]

        print("{:<15}".format(f"Personality")+ personalities)
        partner_no+=1

        #temp fix: convert class to dict
        # partnerdict = {key:value for key, value in p.__dict__.items() if not key.startswith('__') and not callable(key)}

        # for key,value in partnerdict.items():
        #     print(f"{key:<15}  {value}")
        print("----------------------------------------------------------------")
    print()
    

def main():    
    game_config = data_config()
    current_player = player()

    ###### START OF SECTION 1: GAME CUSTOMIZATION ######
    print()
    print(colored('Welcome to Dating Simulator 2020','cyan',attrs = ['bold']))
    print()
    current_player.name = string_validation(game_config.player_profile_questions["name"])
    print()
    current_player.age = age_validation(game_config.player_profile_questions["age"])
    print()
    current_player.gender = choose_options((game_config.player_profile_questions["gender"]))
    print()
    current_player.partner_gender = choose_options((game_config.player_profile_questions["partner_gender"]))

    print()
    print(f"Hi {current_player.name}, let's move on to some other questions regarding your dating preferences")
    print("Make your choices by answering 1 or 2.")
    print()
    
    #Gets Personality Type Preferences from user
    for i in range(3):
        chosen_type = int(choose_options(game_config.partner_preference_questions[i]))
        current_player.preferred_partner_types.append(game_config.list_of_all_types[i][chosen_type-1])
        print()
        
    partners= randomize_partners(current_player, game_config , 3)
    display_partners(partners)
    partner_choices = ["Who would you like to meet?\n\nChoice: ",['1','2','3']]
    chosen_partner_no= int(choose_options(partner_choices))
    chosen_partner: partner() = partners[chosen_partner_no-1]
    print()
    print(f"You have chosen {chosen_partner.name}! \nAre you ready to unlock this new journey in knowing {chosen_partner.name}?\n")
    print("Press [ENTER] to continue!")
    input("")

    ###### END OF SECTION 1: GAME CUSTOMIZATION ######

    ###### START OF SECTION 2: STORY TIME ######

    updated_plotline = game_config.plotline.replace("_player_",current_player.name).replace("_partner_",chosen_partner.name)
    storyline = JsonConvert.FromJSON(updated_plotline)

    for scenario in storyline.scenarios:
        print(f"Start of Scenario {scenario.id}\n")
        mcq_id = 1
        while mcq_id <= len(scenario.mcqs):
            print(scenario.mcqs[mcq_id-1].question.replace("_br_","\n"))
            print()
            option_ids=[]
            for option in scenario.mcqs[mcq_id-1].options:
                print(f"[{option.id}] {option.option}")
                option_ids.append(option.id)
            print()
            choice=int(choose_options(['Reply: ',option_ids]))
            selected_option = scenario.mcqs[mcq_id-1].options[choice-1]
            print()
            # Check if selected_option made has any follow up action
            # 1) Does choice personality match with partner? (if so add score and response_positive if exist)
            if(selected_option.personality_type in chosen_partner.personality_types):
                current_player.score += 1
                if(selected_option.response_positive != None and selected_option.response_positive != ""):
                    print(selected_option.response_positive)
            # 2) Does choice personality not match with partner? (if so minus score and response_negative if exist)
            else:
                current_player.score += -2
                if(selected_option.response_negative != None and selected_option.response_negative != ""):
                    print(selected_option.response_negative)
            # 3) Does jump_to_mcq_id exist? if so jump else continue
            if(selected_option.jump_to_mcq_id != None and selected_option.jump_to_mcq_id != 0):
                if(selected_option.jump_to_mcq_id < 0):
                    break
                else:
                    mcq_id = selected_option.jump_to_mcq_id
            else:
                mcq_id += 1
            
        print(f"End of Scenario {scenario.id}\n\n")

        #Check if score is sufficient for player to proceed
        if current_player.score > 1 and scenario.id == len(storyline.scenarios):
            #display final win scene
            print(f"*2 years later*")
            print(f"{chosen_partner.name} and {current_player.name} have been married and now have a new kid! Yay!")
            print()
            print(f"Congrat you have won the game!")
            print(f"Hope you had fun!")
            print()
            pass
        elif current_player.score > 1:
            #display round win scene
            print(f"Have fun on your date with {chosen_partner.name} tomorrow! ")
            display_image('https://upload.wikimedia.org/wikipedia/commons/e/e6/Finger_heart.png')
            print()
            pass
        else:
            #display lose scene
            print("She ghosted you")
            print("Game over bro")
            display_image('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Broken_heart.svg/166px-Broken_heart.svg.png')
            print()
            break

    end_game()

    ###### END OF SECTION 2: STORY TIME ######
    
if __name__ == '__main__':
    main()