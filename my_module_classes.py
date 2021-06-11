class Billy(object):
    
    LI_activities = ['How does reading your favorite book sound?\n',
                    'Would you be open to meditating?\n',
                    'Sometimes, I like to watch an episode of my favorite show. How does that sound?\n',
                    'A brisk walk to the corner of your street may help?\n',
                    'Adult coloring books are all the rage!/n']
    
    LI_index = 0
    
    HI_activities = ["How does working out sound to you? Endorphins are great!\n",
                     "Hmm, maybe getting a massage is more up your alley?\n",
                     "Sometimes some alone time is best. Are you open to going to dinner by yourself?\n",
                     "Then I definitely reccomend going on a hike by yourself!\n",
                     "Some retail therapy never hurt anyone, why don't you go shopping?\n"]
    
    HI_index = 0
    
    
    def __init__(self):
        pass
    
    def high_intensity(self):
        
        """Create my first function that will assess whether Billy should offer high intensity destressing activities
           Assesses if there are no more HI activites it can recommend then exits chatbot if none were helpful """
        
        if self.HI_index >= len(self.HI_activities):
            #len of HI_index cannot exceed the amount of HI_activities 
            result = ("Sorry my ideas weren't helpful. Maybe my next update will fix that!")
        else:
            result = self.HI_activities[self.HI_index]
            #indexes through list of activities to offer them to the user 
            self.HI_index = (self.HI_index + 1)
        
        return result 
    
    def low_intensity(self):
        
        """ Creates second function to assess if Billy should offer low intensity destressing activities 
            Assess if there are no more options to be given and will exit chatbot if none were helpful"""
        
        if self.LI_index >= len(self.LI_activities):
            result = ("Sorry my ideas weren't helpful. Maybe my next update will fix that!")
        else:
            result = self.LI_activities[self.LI_index]
            self.LI_index = (self.LI_index + 1) 
        
        return result 
        
        
        
    def hi_billy (self):
        
        """ Introduces the chatbot to User
            Asks for name and how often the user engages in destressing activities
            Billy will reccommend HI activities or LI activites based on how often the user partakes in destressing activities
            Billy will keep listing more intense or less intense activities until User answers yes 
            Once user replies with yes or exceeds the options of activites chatbot will stop"""
        
        name = input("Hi, I'm Billy! What's your name?\n") 
         
        print('Good to meet you '+ name + " I'm your friendly chatbot that helps you find relaxing activities to help you destress!\n")
        destress = input(" How many times a week do you destress?\n")
         
        while not destress.isnumeric():
            destress = input("What's that Gibberish? I need a number please!\n")
        destress = int(destress)
            #makes sure that destress is an int of hours and not anything else 
        if destress > 5:
             
            response = ''
            #
            while response.lower().strip() == 'no' or len(response) == 0:
                
                #Converted all input to lowercase and got rid of periods and white space in order to run one check
                #Looked at project online for choose your own adventure and saw this technique https://github.com/sophiewfrancis/Choose-Your-Own-Adventure-Final/blob/master/ProjectNotebook.ipynb
                
                done = self.low_intensity()
                
                #checks to see if ideas are out and returns a chatbot exit statement
                
                if done == "Sorry my ideas weren't helpful. Maybe my next update will fix that!":
                    print("Sorry my ideas weren't helpful. Maybe my next update will fix that!")
                    break
                else:
                    response = input( done + "yes or no?\n")
                    if response.lower().strip() == 'yes':
                        final_response = print("Glad I could help. Come talk again soon!\n")

                        break
                    else:
                        #checks to see if more ideas from the list are needed
                        print("Well, how about I reccomend some other activities!\n")
        if destress <= 5:
             
            response = ''
                 
            while response.lower().strip() == 'no' or len(response) == 0:
                done = self.high_intensity()
                if done == "Sorry my ideas weren't helpful. Maybe my next update will fix that!":
                    print("Sorry my ideas weren't helpful. Maybe my next update will fix that!")
                    break
                else:
                    response = input( done + "yes or no?\n")
                    if response.lower().strip() == 'yes':
                        final_response = print("Glad I could help. Come talk again soon!\n")
                        break
                    else:
                        print("Well, how about I reccomend some other activities!\n")
