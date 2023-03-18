
"""
Date: 1st March 2023
Project: Student library management system
"""
def display_available_books(books):
    print(f"\n{len(books)} AVAILABLE BOOKS ARE: ")
    for book in books:
        print(" ♦-- " + book)
    print("\n")


def borrow_book(name, bookname, books, track):
    if bookname not in books:
        print(
            f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
    else:
        track.append({name: bookname})
        print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
        books.remove(bookname)


def return_book(name, bookname, books, track):
    print("BOOK RETURNED : THANK YOU! \n")
    books.append(bookname)
    if {name: bookname} in track:
        track.remove({name: bookname})


def donate_book(bookname, books):
    print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
    books.append(bookname)


def request_book():
    print("So, you want to borrow book!")
    book = input("Enter name of the book you want to borrow: ")
    return book


def return_book_info():
    print("So, you want to return book!")
    name = input("Enter your name: ")
    book = input("Enter name of the book you want to return: ")
    return name, book


def donate_book_info():
    print("Okay! you want to donate book!")
    book = input("Enter name of the book you want to donate: ")
    return book


if __name__ == "__main__":

    books = ["vistas", "invention", "rich&poor", "indian", "macroeconomics", "microeconomics"]
    track = []

    print("\t\t♦♦♦♦♦♦♦ WELCOME TO THE ELITE LIBRARY ♦♦♦♦♦♦♦\n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. Exit the library system\n""")

    while (True):
        # print(track)
        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                display_available_books(books)
            elif usr_response == 2:  # borrow
                borrow_book(input("Enter your name: "), request_book(), books, track)
            elif usr_response == 3:  # return
                name, book = return_book_info()
                return_book(name, book, books, track)
            elif usr_response == 4:  # donate
                donate_book(donate_book_info(), books)
            elif usr_response == 5:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            elif usr_response == 6: #exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print(f"{e}---> INVALID INPUT! \n")
