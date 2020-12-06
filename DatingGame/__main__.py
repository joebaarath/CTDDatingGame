import random
import sys
import matplotlib.pyplot as plt
from data_config import *
import json
from types import SimpleNamespace

class player():
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0
        self.partner_gender = ""
        self.preferred_partner_types = []
        self.score = 0

class partner():
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0
        self.occupation = ""
        self.personality_types = []


class JsonConvert(object):
    mappings = {}
     
    @classmethod
    def class_mapper(clsself, d):
        for keys, cls in clsself.mappings.items():
            if keys.issuperset(d.keys()):   # are all required arguments present?
                return cls(**d)
        else:
            # Raise exception instead of silently returning None
            raise ValueError('Unable to find a matching class for object: {!s}'.format(d))
     
    @classmethod
    def complex_handler(clsself, Obj):
        if hasattr(Obj, '__dict__'):
            return Obj.__dict__
        else:
            raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(Obj), repr(Obj)))
 
    @classmethod
    def register(clsself, cls):
        clsself.mappings[frozenset(tuple([attr for attr,val in cls().__dict__.items()]))] = cls
        return cls
 
    @classmethod
    def ToJSON(clsself, obj):
        return json.dumps(obj.__dict__, default=clsself.complex_handler, indent=4)
 
    @classmethod
    def FromJSON(clsself, json_str):
        return json.loads(json_str, object_hook=clsself.class_mapper)
     
    @classmethod
    def ToFile(clsself, obj, path):
        with open(path, 'w') as jfile:
            jfile.writelines([clsself.ToJSON(obj)])
        return path
 
    @classmethod
    def FromFile(clsself, filepath):
        result = None
        with open(filepath, 'r') as jfile:
            result = clsself.FromJSON(jfile.read())
        return result

@JsonConvert.register
class option(object):
    def __init__(self, id:int=None, option:str="", personality_type:str="", response_positive:str="", response_negative:str="", jump_to_mcq_id:int=None):
        self.id = id
        self.option = option
        self.personality_type = personality_type
        self.response_positive = response_positive
        self.response_negative = response_negative
        self.jump_to_mcq_id = jump_to_mcq_id
        return

@JsonConvert.register
class mcq(object):
    def __init__(self, id:int=None, question:str="", options:[option]=None):
        self.id = id
        self.question = question
        self.options = [] if options is None else options
        return
 
@JsonConvert.register
class scenario(object):
    def __init__(self, id:int=None, mcqs:[mcq]=None):
        self.id = id
        self.mcqs = [] if mcqs is None else mcqs
        return

@JsonConvert.register
class story(object):
    def __init__(self, scenarios:[scenario]=None):
        self.scenarios = [] if scenarios is None else scenarios
        return

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

def randomize_partners(current_player: player(), game_config: data_config() , num_of_partners: int() = 3 ):
    list_of_ages = list(range(current_player.age if current_player.age <= 23 else current_player.age - 5, current_player.age +5))

    
    partners = []

    for index in range(num_of_partners):
        p = partner()
        p.age = random.choice(list_of_ages)
        p.occupation = random.choice(game_config.list_of_jobs)
        p.gender = current_player.partner_gender
        p.name = random.choice(game_config.list_of_male_names if current_player.partner_gender == 'M' else game_config.list_of_female_names)

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
    end_game_option = choose_options(['Would you like to play again?\n[1] Restart\n[2] Exit the game\n\nChoice: ', ['1','2']])
    if  end_game_option == '1':
        main()
    else:
        sys.exit()

def string_validation(question):
        try:
            user_input = input(question)
            if len(user_input) == 0 or user_input.isnumeric() :
                raise Exception
            return user_input
        except:
            print('Please enter a valid name')
            string_validation(question)

def age_validation(question):
        try:
            age = int(input(question))
            if age <= 13:
                print('You are underaged. Seek parental guidance.')
                img = plt.imread('https://www.imda.gov.sg/-/media/Imda/Images/Content/Regulation-Licensing-and-Consultations/Content-Standards-and-classification/Classification-Rating/PG13-Rating.png?la=en&hash=FDB0D0A4021A703C98A3E791D1EA3E9494BB70A7')
                plt.imshow(img)
                plt.show()
                end_game()
            return age
        except:
            print('Please enter a valid number')
            age_validation(question)
            

def main():    
    game_config = data_config()
    current_player = player()

    print()
    print('Welcome to Dating Simulator 2020')
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
    
    for i in range(3):
        chosen_type = int(choose_options(game_config.partner_preference_questions[i]))
        current_player.preferred_partner_types.append(game_config.list_of_all_types[i][chosen_type-1])
        print()
        
    print()
    print('Now let introduce your 3 partners')
    print("----------------------------------------------------------------")
    partners= randomize_partners(current_player, game_config , 3)
    partner_no=1

    for p in partners:
        print(str(partner_no)+")")
        partner_no+=1

        #temp fix: convert class to dict
        partnerdict = {key:value for key, value in p.__dict__.items() if not key.startswith('__') and not callable(key)}

        for key,value in partnerdict.items():
            print(f"{key:<15}  {value}")
        print("----------------------------------------------------------------")
        print()

    partner_choices = ["Please make your choice now\n\nChoice: ",['1','2','3']]
    chosen_partner_no= int(choose_options(partner_choices))
    chosen_partner: partner() = partners[chosen_partner_no-1]
    print()

    # Part 3: Scenario Time!
    print(f"You have chosen {chosen_partner.name}! \nAre you ready to unlock this new journey in knowing {chosen_partner.name}?\n")
    print("Press [ENTER] to continue!")
    input("")
    print()
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
            choice=int(choose_options(['Reply:',option_ids]))
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
            print(f"Congrat you have won the game!")
            print(f"Hope you had fun!")
            pass
        elif current_player.score > 1:
            #display round win scene
            print(f"Have fun on your date with {chosen_partner.name} tomorrow! ")
            img = plt.imread('https://upload.wikimedia.org/wikipedia/commons/e/e6/Finger_heart.png')
            plt.imshow(img)
            plt.show()
            pass
        else:
            #display lose scene
            print("She ghosted you")
            print("Game over bro")
            img = plt.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Broken_heart.svg/166px-Broken_heart.svg.png')
            plt.imshow(img)
            plt.show()
            print()
            break

    end_game()
    
if __name__ == '__main__':
    main()