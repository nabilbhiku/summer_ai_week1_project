# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        print("Creating ...")
        name = input("What is your name?")
        age = input("What is your age?")
        user = Person(name, age)
        self.list_of_people.append(user)
    

    def send_message(prsn,message):
        #for loop to search in self.list_of_people
        prsn.messages.append(message)

    def get_current_user(self,name):
        for person in self.list_of_people:
            if name == person.id:
                return person
    




class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.blocklist = []
        self.messages=[]

    def add_friend(self, person_object):
        self.friendlist.append(person_object) 
        print(self.friendlist)
        #implement adding friend. Hint add to self.friendlist

    def block_friend(self, person_object):
        self.blocklist.append(person_object)
        

    def view_friendlist(self):
        print("Your friendlist: ")
        print(self.friendlist)
        
    def view_blocklist(self):
        print("Your blocked friends are: ")
        print(self.blocklist)

    def edit_details(self):
        new_age = input("Enter new age: ")
        new_name = input("Enter new name: ")
        self.id = new_name
        self.year = new_age
        
    def send_message(self, person_object):
        message = input("Enter your message: ")
        person_object.messages.append(message)
        print("Message sent!")
        pass

