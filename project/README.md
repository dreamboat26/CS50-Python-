# __LIBRARY MANAGEMENT SYSTEM__
#### Video Demo:  <https://youtu.be/UCvXYcmUIf8>

## __Definition__
 This project is an interactive shell providing the user to borrorw, return,donate books from the library system.

 Project structure :
 - project.py
 - test_project.py
 - README.md

## __Usage__

```  python project.py```
```  python test_python.py ```

♦♦♦♦♦♦♦ WELCOME TO THE ELITE LIBRARY ♦♦♦♦♦♦♦

CHOOSE WHAT YOU WANT TO DO:-
1. Listing all books
2. Borrow books
3. Return books
4. Donate books
5. Track books
6. Exit the library system
Enter your choice:
```
## __Functioning__

the project.py contains 8 functions including the main function.

### __display_available_books__function:
This function simply displays the available list of books in the library giving the user idea about which books he can purchase.

#### __borrow_book__ function : this function takes four arguments and allows the user to borror the book he wants from the given avaliable books list.

#### __return_book__ function : this function takes in four arguments and allows the user to return the book issued under his name. The book returned then can be seen in the list of available books for purchase.

#### __donate_book__ function: This function allow the user to donate his/her books to the library for use by the readers. The added book name will be visible in the list of books available for purchase.

#### __request_book__ function :This function allows the user to borrow the book.

#### __return_book_info__function: This function helps the system to keep track of the books returned by the reader which can be then made available to the readers for further use and purchase.
#### ___donate_book_info__ function :This function allows us to keep track of the donated books list and information.

#### There is also implementation of while loop to take in the choices from the user with a choice to exit from the library system. This project would provide a basis for more development and can be further imporved and worked upon. We can also further include GUI features which will make the user experience more better. This is a simple implementation of the basics of Python to make a library management system. There is also implementation of pytest to check the working of different functions by adding unit test cases.
```
### Author : Mahule Roy