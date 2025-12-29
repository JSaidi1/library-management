import sys
from data.documents_store_data import list_documents


# =================================================================================================================
#                                                   FUNCTIONS                            
# =================================================================================================================
def menu():
    return """
    ====== LIBRARY MANAGEMENT ======
    1. Consult 
    2. Borrow 
    3. Give back
    4. Add Document (admin) 
    5. Remove Document (admin)
    0. Exit
    ==================================
    """

def display_list(liste_documents) -> dict:
    cpt = 1
    for document in liste_documents:
        print(cpt,". ", end="")
        document.show_informations()
        cpt += 1

def choose_document(liste_documents):
    display_list(liste_documents)

    # Get indexes of docs in liste_documents
    user_document_choice = int(input("\nPlease choose the document number (book/magazine): "))

    return user_document_choice

def display_menu():
    
    while(1):
        print(menu())
        choosen_action = input("Choose action to execute (1 or 2 or ... or '0' to exit): ")

        if choosen_action == "0":
            print("\nYou chose to exit. Bye, see you!")
            break
        elif choosen_action == "1":
            print("\nYou chose: '1. Consult': ")
            #Consult
            document_id = choose_document(list_documents)
            list_documents[document_id-1].consult()
            print("\n")
        elif choosen_action == "2":
            print("\nYou chose: '2. Borrow': ")
            #Borrow
            document_id = choose_document(list_documents)
            if hasattr(list_documents[document_id-1], "borrow"):
                list_documents[document_id-1].borrow()
            else:
                print(f"The document is not borrowable:")
                list_documents[document_id-1].show_informations()
            print("\n")
        elif choosen_action == "3":
            print("\nYou chose: '3. Give back': ")
            #Give back

        elif choosen_action == "4":
            print("\nYou chose: 'Add Document (admin)': ")
            #Add Document

        elif choosen_action == "5":
            print("\nYou chose: 'Remove Document (admin)': ")
            #Remove Document

        else:
            print(f"\nError: choice not valid (or not exists yet): '{choosen_action}'")

# =================================================================================================================
#                                                   MAIN                            
# =================================================================================================================
def main():
    display_menu()



if __name__ == "__main__":
    main()
