class data_config():

    def __init__(self):
        self.player_profile_questions =  {
                                            "gender" : ['Are you Male or Female?(M/F) :', ['M','F']],
                                            "partner_gender" : ['Are you interested in Male or Female?(M/F) :', ['M','F']]
                                        }

        self.partner_preference_questions = [
                                                ["Do you prefer your partner to be 1) athletic or 2) artistic?  ", ['1','2']],
                                                ["Do you prefer your partner to be an 1) introvert or 2) extrovert?  ", ['1','2']],
                                                ["Do you prefer your partner to be 1) adventurous or 2) conservative?  ",['1','2']]
                                            ]

        self.list_of_all_types = [['athletic', 'artistic'], 
                    ['introvert','extrovert'], 
                    ['adventurous','conservative']]

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
