bookDB = [
{'bookid': 1, 'title': 'Thor', 'author': 'Stan Lee', 'publishYear': 2017, 'genre': 'adventure'},
{'bookid': 2, 'title': 'Batman', 'author': 'Bruce Ven', 'publishYear': 2014, 'genre': 'S.I-F.I'},
{'bookid': 3, 'title':  'The counjuring',  'author': 'Chad Hayes', 'publishYear':2013, 'genre': 'horror'},
{'bookid': 4, 'title': 'A Suitable Boy ', 'author':  'Vikram Seth', 'publishYear': 1993, 'genre': 'novel'},
{'bookid': 5, 'title': 'Gitanjali',       'author':  'ravindranath tagaore','publishYear':1913, 'genre':'poem'}
]
id = 1
def addBook():
    global id
    id += 1
    title = input("Enter Your Book Name: ")
    author = input("Enter author name: ")
    # Loop until a valid integer is provided
    while True:
        publishYear_input = input("Enter Publish Year: ")
        if publishYear_input.isdigit():
            publishYear = int(publishYear_input)
            break
        else:
            print("Please enter a valid integer for the Publish Year.")

    genre = input("Enter the genre: ")
    booksInfo = {
        "bookid": id,
        "title": title,
        "author": author,
        "publishYear": publishYear,
        "genre": genre
    }
    bookDB.append(booksInfo)
    print(bookDB)
    while True:
        moreBookadding = input("Do you Want to add more books(yes/no): ").lower()
        if(moreBookadding == "yes"):
            addBook()
            break
        elif(moreBookadding == "no"):
            main()
            break
        else:
            print("Invalid Input! Enter Again")

def removeBook():
    while True:
        getingBookId = input("Enter Your Book id: ")
        if getingBookId.isdigit():
            bookId = int(getingBookId)
            break
        else:
            print("Please enter a valid integer for Book Id.")

    for BooksInfoElement in bookDB:
        if x:= BooksInfoElement["bookid"] == bookId:
            print(BooksInfoElement)
            bookDB.remove(BooksInfoElement)
    print(bookDB)
def updatebook():

    while True:
        update_option = input("Enter 'id' to update by book ID, 'title' to update by title, 'author' to update by author: ").lower()
        if update_option in ['id', 'title', 'author']:
            break
        else:
            print("Invalid input! Please enter 'id', 'title', or 'author'.")

    if update_option == 'id':
        while True:
            book_id_input = input("Enter the book ID to update: ")
            if book_id_input.isdigit():
                book_id = int(book_id_input)
                break
            else:
                print("Please enter a valid integer for the book ID.")
    else:
        search_term = input(f"Enter the {update_option} of the book to update: ")

    # Find the book to update
    found_books = []
    for book in bookDB:
        if update_option == 'id':
            if book['bookid'] == book_id:
                found_books.append(book)
        elif update_option == 'title':
            if book['title'].lower() == search_term.lower():
                found_books.append(book)
        elif update_option == 'author':
            if book['author'].lower() == search_term.lower():
                found_books.append(book)

    if not found_books:
        print("No books found.")
        return

    print("Books Found:")
    for index, book in enumerate(found_books):
        print(f"{index + 1}. {book}")

    while True:
        book_index_input = input("Enter the index of the book to update: ")
        if book_index_input.isdigit():
            book_index = int(book_index_input)
            if 1 <= book_index <= len(found_books):
                break
            else:
                print("Invalid index. Please enter a valid index.")
        else:
            print("Please enter a valid integer for the index.")

    book_to_update = found_books[book_index - 1]

    # Prompt the user for updated information
    new_title = input("Enter the new title (press Enter to keep current): ")
    if new_title:
        book_to_update['title'] = new_title

    new_author = input("Enter the new author (press Enter to keep current): ")
    if new_author:
        book_to_update['author'] = new_author

    while True:
        new_publish_year_input = input("Enter the new publication year (press Enter to keep current): ")
        if not new_publish_year_input:
            break
        elif new_publish_year_input.isdigit():
            new_publish_year = int(new_publish_year_input)
            break
        else:
            print("Please enter a valid integer for the publication year.")

    if 'new_publish_year' in locals():
        book_to_update['publishYear'] = new_publish_year

    new_genre = input("Enter the new genre (press Enter to keep current): ")
    if new_genre:
        book_to_update['genre'] = new_genre

    print("Book Updated Successfully.")
    print(bookDB)
   
def list():
    print(bookDB)

def search_book_by():
    search_book = input("Enter the title,author,genre. You want to search for: ").lower()
    found_book = []
    for book in bookDB:
        if search_book in book['title'].lower() or search_book in book['author'].lower() or search_book in book['genre'].lower():
            found_book.append(book)
    if found_book :
        for found_books in found_book:
            print("title",found_books['title'])
            print("author",found_books['author'])
            print("genre",found_books['genre'])
            print("publishYear",found_books['publishYear'])

    else:
            print("No books found matching the search.")
    
     
def main():
    choice = int(input("Enter the choice number between 1 to 5 : "))
    if choice == 1:
        print("Add the book in your DB:")
        (addBook())
    elif choice == 2:
        print("To remove your book: ")
        removeBook()
    elif choice == 3:
         print("To update your book: ")
         updatebook()
    elif choice == 4:
        print("Showing all libirary:")
        list()
    elif choice == 5:
        print("Search your own choice book: ")
        search_book_by()

main()