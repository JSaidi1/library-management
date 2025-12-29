# =================================================================================================================
#                                                   FUNCTIONS                            
# =================================================================================================================
def display_menu():
    print("""
        ==========================================================================
        Available actions: 
        1. Consult 
        2. Borrow 
        3. Give back
        4. Add Document (admin) 
        5. Remove Document (admin)
        0. Exit
        ==========================================================================
        """)
    
    while(1):
        choosen_action = input("Choose action to execute (1 or 2 or ... or '0' to exit: ")

        if choosen_action == "0":
            print("\nYou chose to exit. Bye, see you!")
            break
        elif choosen_action == "1":
            print("\nYou chose: '1. Consult'")
            #Consult
            break
        elif choosen_action == "2":
            print("\nYou chose: '2. Borrow'")
            #Borrow
            break
        elif choosen_action == "3":
            print("\nYou chose: '3. Give back'")
            #Give back
            break
        elif choosen_action == "4":
            print("\nYou chose: 'Add Document (admin)'")
            #Add Document
            break
        elif choosen_action == "5":
            print("\nYou chose: 'Remove Document (admin)'")
            #Remove Document
            break
        else:
            print(f"\nError: choice not valid (or not exists yet): '{choosen_action}'")

# =================================================================================================================
#                                                   MAIN                            
# =================================================================================================================
def main():
    display_menu()



if __name__ == "__main__":
    main()