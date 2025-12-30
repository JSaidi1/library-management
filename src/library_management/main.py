import sys
from data.documents_store_data import DocumentStore, list_documents
from exceptions.document_not_borrowed_exception import DocumentNotBorrowedException
from exceptions.document_already_borrowed_exception import DocumentAlreadyBorrowedException
from models.book import Book
from models.magazine import Magazine
from enums.genre import Genre



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

def display_list(liste_documents):
    """Display documents (books and magazines) in documents list."""
    print("\nCurrent documents list:")
    cpt = 1
    for document in liste_documents:
        print(cpt,". ", end="")
        document.show_informations()
        cpt += 1

def choose_document(liste_documents) -> int | None:
    nbr_of_docs = len(liste_documents)

    display_list(liste_documents)

    if nbr_of_docs != 0:
        # Get indexes of docs in liste_documents
        while(1):
            user_document_choice = input("\nPlease choose the document number (or set '0' to exit): ")

            try:
                user_document_choice = int(user_document_choice)  # Try to convert input to an integer
                if 1 <= user_document_choice <= nbr_of_docs:
                    return user_document_choice
                else:
                    if user_document_choice == 0:
                        print("You chose to exit.")
                        break
                    else:
                        print(f"{user_document_choice} is not a valid value (it must be between 1 & {nbr_of_docs})")
            except Exception:
                print(f"{user_document_choice}' is not a valid value (it must be an integer)")
    else:
        print("Currently, documents list is empty! You can only 'add document'.")

def remove_document() -> Book | Magazine | None:
    """Return a document to remove from the list: book or magazine."""
    while(1):
        document_type = input("\nWhat type of document to remove? book(1), magazine(2), to exit set 'q': ")

        if document_type == "1":
            print("You chose to remove a book:")
            title = input("Set title of the book: ")
            year_of_publication = int(input("Set year of publication of the book: "))
            author = input("Set author of the book: ")
            nb_pages = int(input("Set nbre of pages of the book: "))
            while(1):
                genre = input("Set genre of the book (NOVEL or SCIENCE_FICTION or FANTASY): ").lower()
                if genre == "novel":
                    genre = Genre.NOVEL
                    break
                elif genre == "science_fiction":
                    genre = Genre.SCIENCE_FICTION
                    break
                elif genre == "fantasy":
                    genre = Genre.FANTASY
                    break
                else:
                    print(f"genre '{genre}' is not valid.")
            return Book(title, year_of_publication, author, nb_pages, genre)
        
        elif document_type == "2":
            print("You chose to remove a magazine:")
            title = input("Set the title of the magazine: ")
            year_of_publication = int(input("Set the year of publication of the magazine: "))
            number = int(input("Set the number of the magazine: "))
            return Magazine(title, year_of_publication, number)
        
        elif document_type == "q":
            print("You chose to stop removing document.")
            break
        else:
            print(f"Invalid value: '{document_type}")
    return None

def add_document() -> Book | Magazine | None:
    """Return a document to add to list: book or magazine."""

    while(1):
        document_type = input("\nWhat type of document to add? book(1), magazine(2), to exit set 'q': ")

        if document_type == "1":
            print("You chose to add a book:")
            title = input("Set title of the book: ")
            year_of_publication = int(input("Set year of publication of the book: "))
            author = input("Set author of the book: ")
            nb_pages = int(input("Set nbre of pages of the book: "))
            while(1):
                genre = input("Set genre of the book (NOVEL or SCIENCE_FICTION or FANTASY): ").lower()
                if genre == "novel":
                    genre = Genre.NOVEL
                    break
                elif genre == "science_fiction":
                    genre = Genre.SCIENCE_FICTION
                    break
                elif genre == "fantasy":
                    genre = Genre.FANTASY
                    break
                else:
                    print(f"genre '{genre}' is not valid.")
            return Book(title, year_of_publication, author, nb_pages, genre)
        
        elif document_type == "2":
            print("You chose to add a magazine:")
            title = input("Set the title of the magazine: ")
            year_of_publication = int(input("Set the year of publication of the magazine: "))
            number = int(input("Set the number of the magazine: "))
            return Magazine(title, year_of_publication, number)
        
        elif document_type == "q":
            print("You chose to stop adding document.")
            break
        else:
            print(f"Invalid value: '{document_type}")
        return None
    
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
            if document_id != None:
                list_documents[document_id-1].consult()
            print("\n")
        elif choosen_action == "2":
            print("\nYou chose: '2. Borrow': ")
            #Borrow
            document_id = choose_document(list_documents)
            if document_id != None:
                if hasattr(list_documents[document_id-1], "borrow"):
                    try:
                        list_documents[document_id-1].borrow()
                    except DocumentAlreadyBorrowedException as e:
                        print(e)
                else:
                    print(f"The document is not borrowable:")
                    list_documents[document_id-1].show_informations()
            print("\n")
        elif choosen_action == "3":
            print("\nYou chose: '3. Give back': ")
            #Give back
            document_id = choose_document(list_documents)
            if document_id != None:
                if hasattr(list_documents[document_id-1], "give_back"):
                    try:
                        list_documents[document_id-1].give_back()
                    except DocumentNotBorrowedException as e:
                        print(e)
                else:
                    print(f"The document is not borrowable (you cannot give it back):")
                    list_documents[document_id-1].show_informations()
            print("\n")
        elif choosen_action == "4":
            print("\nYou chose: 'Add Document (admin)': ")
            #Add Document
            display_list(list_documents)
            doc_to_add = add_document()
            if doc_to_add != None:
                DocumentStore.add_document(doc_to_add)
        elif choosen_action == "5":
            print("\nYou chose: 'Remove Document (admin)': ")
            #Remove Document
            if len(list_documents) != 0:
                display_list(list_documents)
                doc_to_remove = remove_document()
                if doc_to_remove != None:
                    DocumentStore.remove_document(doc_to_remove)
            else:
                print("Currently, documents list is empty! You can only 'add document'.")
        else:
            print(f"\nError: choice not valid (or not exists yet): '{choosen_action}'")


# =================================================================================================================
#                                                   MAIN                            
# =================================================================================================================
def main():
    display_menu()



if __name__ == "__main__":
    main()
