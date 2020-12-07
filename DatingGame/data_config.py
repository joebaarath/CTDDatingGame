class data_config():

    def __init__(self):
        self.colors = {
                        'white':    "\033[1;37m",
                        'yellow':   "\033[1;33m",
                        'green':    "\033[1;32m",
                        'blue':     "\033[1;34m",
                        'cyan':     "\033[1;36m",
                        'red':      "\033[1;31m",
                        'magenta':  "\033[1;35m",
                        'black':      "\033[1;30m",
                        'darkwhite':  "\033[0;37m",
                        'darkyellow': "\033[0;33m",
                        'darkgreen':  "\033[0;32m",
                        'darkblue':   "\033[0;34m",
                        'darkcyan':   "\033[0;36m",
                        'darkred':    "\033[0;31m",
                        'darkmagenta':"\033[0;35m",
                        'darkblack':  "\033[0;30m",
                        'off':        "\033[0;0m"
                    }
        self.player_profile_questions =  {
                                            "gender" : ['What is your gender?\n\n[M] Male\n[F] Female\n\nChoice: ', ['M','F']],
                                            "partner_gender" : ['Who are you interested in?\n\n[M] Male Partner\n[F] Female Partner\n\nChoice: ', ['M','F']],
                                            "name" : "What's your Name?\n\nName: ",
                                            "age" : "What's your Age?\n\nAge: "
                                        }

        self.partner_preference_questions = [
                                                ["What do you prefer more in a partner?\nMy partner has to be:\n\n[1] Athletic\n[2] Artistic\n\nChoice: ", ['1','2']],
                                                ["What do you prefer more in a partner?\nMy partner has to be:\n\n[1] Introvert\n[2] Extrovert\n\nChoice: ", ['1','2']],
                                                ["What do you prefer more in a partner?\nMy partner has to be:\n\n[1] Adventurous\n[2] Conservative\n\nChoice: ",['1','2']]
                                            ]

        self.list_of_all_types = [['Athletic', 'Artistic'], 
                    ['Introvert','Extrovert'], 
                    ['Adventurous','Conservative']]

        self.list_of_jobs = ['Accountant', 
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
                    
        self.list_of_male_names = ['Justin', 
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

        self.list_of_female_names = ['Melody',
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

        self.list_of_male_pickup_lines = ["malepickupline1","malepickupline2","malepickupline3"]  # Melodee fill this in!
        self.list_of_female_pickup_lines = ["femalepickupline1","femalepickupline2","femalepickupline3"]  # Melodee fill this in!

        self.plotline = '''{
                            "scenarios": [
                                {
                                    "id": 1,
                                    "mcqs": [
                                        {
                                            "id": 1,
                                            "question": "You have just received your first message from _partner_!_br_Make your choices by answering 1 or 2._br__br_Heyyyy _player_ :)_br_I am _partner_!_br_Looking forward to seeing you tommorow, _player_!",
                                            "options": [
                                                {
                                                    "id": 1,
                                                    "option": "Me too~",
                                                    "personality_type": "Athletic",
                                                    "response_positive": "",
                                                    "response_negative": "",
                                                    "jump_to_mcq_id": null
                                                },
                                                {
                                                    "id": 2,
                                                    "option": "Yes of course! Always excited to meet new friends",
                                                    "personality_type": "Artistic",
                                                    "response_positive": "",
                                                    "response_negative": "",
                                                    "jump_to_mcq_id": null
                                                }
                                            ]
                                        },
                                        {
                                            "id": 2,
                                            "question": "So do you have any idea where we should head tomorrow?",
                                            "options": [
                                                {
                                                    "id": 1,
                                                    "option": "idk ><",
                                                    "personality_type": "Introvert",
                                                    "response_positive": "Hehehe me too",
                                                    "response_negative": "Okay.",
                                                    "jump_to_mcq_id": null
                                                },
                                                {
                                                    "id": 2,
                                                    "option": "Anywhere that's fun sounds great!",
                                                    "personality_type": "Extrovert",
                                                    "response_positive": "Yeahhh",
                                                    "response_negative": "",
                                                    "jump_to_mcq_id": null
                                                }
                                            ]
                                        },
                                        {
                                            "id": 3,
                                            "question": "So would you like try out some food at a cafe?_br_Or do you wanna head to the beach?",
                                            "options": [
                                                {
                                                    "id": 1,
                                                    "option": "Let's go to the cafe then~",
                                                    "personality_type": "Conservative",
                                                    "response_positive": "Yess!!",
                                                    "response_negative": "Okay.",
                                                    "jump_to_mcq_id": null
                                                },
                                                {
                                                    "id": 2,
                                                    "option": "Yup! I want to go to Sentosa!",
                                                    "personality_type": "Adventurous",
                                                    "response_positive": "YEAHHH!!",
                                                    "response_negative": "Okay.",
                                                    "jump_to_mcq_id": null
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "id": 2,
                                    "mcqs": [
                                        {
                                            "id": 1,
                                            "question": "how's life?",
                                            "options": [
                                                {
                                                    "id": 1,
                                                    "option": "Strong like me",
                                                    "personality_type": "Athletic",
                                                    "response_positive": "Oooh wow!",
                                                    "response_negative": "Okay.",
                                                    "jump_to_mcq_id": null
                                                },
                                                {
                                                    "id": 2,
                                                    "option": "Beautiful marvelous",
                                                    "personality_type": "Artistic",
                                                    "response_positive": "I like!",
                                                    "response_negative": "Okay.",
                                                    "jump_to_mcq_id": null
                                                }
                                            ]
                                        },
                                        {
                                            "id": 2,
                                            "question": "what's life?",
                                            "options": [
                                                {
                                                    "id": 1,
                                                    "option": "2Strong like me",
                                                    "personality_type": "Athletic",
                                                    "response_positive": "Oooh wow!",
                                                    "response_negative": "Okay.",
                                                    "jump_to_mcq_id": null
                                                },
                                                {
                                                    "id": 2,
                                                    "option": "2Beautiful marvelous",
                                                    "personality_type": "Artistic",
                                                    "response_positive": "I like!",
                                                    "response_negative": "Okay.",
                                                    "jump_to_mcq_id": null
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                        '''
