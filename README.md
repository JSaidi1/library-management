# Library management

**Library management** project is a simple Python **console** application that simulates library management using advanced concepts:
**inheritance**, **abstraction**, **enums**, and **exception handling**

## Version
**v1.0.0** – Initial stable release

## Features
- Feature 1: **Consult** existing documents (books and magazines) in the library
- Feature 2: **Borrow** documents
- Feature 3: **Give back** documents to library
- Feature 4: **Add Document** to library (admin action) 
- Feature 5: **Remove Document** from library (admin action)

## Installation
Clone the repository:
```bash
git clone https://github.com/JSaidi1/library-management.git
cd library-management
```

### Dependencies
No dependencies.

## Usage
To run the application:
```bash
python ./src/library_management/main.py
```

## Technologies
- Language: Python (v3.x)

## Project Structure
    library-management
    |   .gitignore
    |   README.md
    |   
    +---docs
    |   \---project-subject
    |           project python library management_en.md
    |           project python library management_en.pdf
    |           projet python gestion de bibliotheque_fr.md
    |           projet python gestion de bibliotheque_fr.pdf
    |           
    |                   
    \---src
        \---library_management
            |   main.py
            |   
            +---data
            |       documents_store_data.py
            |             
            +---enums
            |       genre.py
            |           
            +---exceptions
            |       document_already_borrowed_exception.py
            |       document_not_borrowed_exception.py
            |           
            +---interfaces
            |       borrowable.py
            |       consultable.py   
            |           
            \---models
                    book.py
                    document.py
                    magazine.py
            
                    


## Author
J.SAIDI