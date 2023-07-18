#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui


#person = Person(0, 0)
#Create instance of main social network object
ai_social_network = SocialNetwork()
#ai_social_network.add_current_user(person)

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.current_user = ai_social_network.create_account()
            

        elif choice == "2":
            user = input("Enter name of account you want to manage: ")
            current_user = ai_social_network.get_current_user(user)
            inner_menu_choice = social_network_ui.manageAccountMenu()

            while True:
                if inner_menu_choice == "1":
                    print("Edit details")
                    current_user.name = input("Write your new username: ")
                    current_user.age = input("Write new age: ")


                elif inner_menu_choice == "2":
                    name = input("Who would you like to add? ")
                    print("This user is now your friend: ")
                    current_user.add_friend(name)
                    
                  
                elif inner_menu_choice == "3":
                     current_user.view_friendlist()
                     

                elif inner_menu_choice == "4":
                    message_choice = social_network_ui.manageMessagesMenu()
                    while True:
                        if message_choice == "1":
                           print(current_user.messages) 
                         

                        elif message_choice == "2":
                            friend_name = input("Enter the name of your friend: ")
                            friend = ai_social_network.get_current_user(friend_name)
                            current_user.send_message(friend)

                        elif message_choice == "3":
                            break
                        message_choice = social_network_ui.manageMessagesMenu()

                    

                elif inner_menu_choice == "5":
                    break    
        
                elif inner_menu_choice == "6":
                    name = input("Who would you like to block? ")
                    current_user.block_friend(name)
                    current_user.view_blocklist()
                    break

                elif inner_menu_choice == "7":
                     current_user.view_blocklist()
                     break
                             
                
                inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
