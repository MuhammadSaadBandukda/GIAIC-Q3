
def display_menu():
    menu="""
        Welcome to your Personal Library Manager!  
        1. Add a book  
        2. Remove a book  
        3. Search for a book  
        4. Display all books  
        5. Display statistics  
        6. Exit  
        """ 
    print(menu)         
    return input("Enter your choice: ")

def add_book(books:list[dict]):
    title=input("Enter the book tittle: ")
    author=input("Enter the book author: ")
    year=input("Enter the book year: ")
    genre=input("Enter the book genre: ")
    while True:
        innput = input("Have youu read that book Y/N: ")
        if innput == 'Y' or innput == 'y':
            isRead=True
            break
        elif innput == 'N' or innput == 'n':
            isRead=False
            break
        else:
            print("PLease Enter 'Y' or 'N'")

    new_book = {
        "title":title,
            "author":author,
            "publication_year":year,
            "genre":genre,
            "isRead":isRead
    }
    books.append(new_book)
    # print(books)

def remove_book(books:list[dict]):
    title=input("Enter the book title to remove: ")
    count = 0
    for book in books:
        if title == book["title"]:
            count+=1
            books.remove(book)
    if (count>0):
        print(f"{count} book removed!...")
    else:
        print("No book found with such a title")
    

def sync_data(file, books):
    for book in books:
        line = f"{book['title']}|{book['author']}|{book['publication_year']}|{book['genre']}|{book['isRead']}\n"
        file.write(line)


def read_data(file) -> list[dict]:
    books = []
    for line in file:
        parts = line.strip().split('|')
        if len(parts) == 5:
            title, author, year, genre, isRead = parts
            books.append({
                "title": title,
                "author": author,
                "publication_year": year,
                "genre": genre,
                "isRead": isRead == "True"
            })
    return books

    

def display_books(books: list[dict]):
    for i, book in enumerate(books, start=1):
        read_status = "Read" if book['isRead'] else "Not Read"
        print(f"{i}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} [{read_status}]\n")

def display_statistics(books: list[dict]):
    print(f"Total books: {len(books)}")
    count = 0
    for book in books:    
        if book['isRead']:
            count+=1
    per = count/len(books)*100
    print(f"Read Percentage: {per}")


def search_book(books:list[dict]):
    message = """Search By: 
1.Title
2.Author
Enter Your Choice:
"""
    search_by = int(input(message))
    if search_by == 1:
        title = input("Enter title: ")
        count = 0
        for book in books:
            if title in book['title']:
                count+=1
                print(f"{count}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} {book['isRead']}")
            
    elif search_by == 2:
        author = input("Enter author: ")
        count = 0
        for book in books:
            if author in book['author']:
                count+=1
                print(f"{count}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} {book['isRead']}")
    else:
        print("Invalid Choice...")
    
