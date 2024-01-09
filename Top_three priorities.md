1. Setup a version control system on github.
  DONE
  
  # extra steps --> setup CI/CD with github Actions 
  For later --> 
2. Select a build tool like Mavel e for managing dependencies
  DONE
  
3. Database setup
  DONE 


4. Create a basic backend
A --> initialize the project with Spring book or manually set it up
DONE

B --> Defind the schema in SQL
Done

C --> develp API --> two endpoints --> GET /books  to list all books  and POST /books to add a new book
Done

D --> implement basic CRUD operations  --> to add books to database
DONE 

E. customasize whitehall space page ---> https://www.baeldung.com/spring-boot-custom-error-page

F. create a service layer to fetch information in the books. 
#  Booksrepository --> to fetch data 
#  BookController --> add methods to handle web request. For e.g, @GetMapping("/books")
# format the data, return the data as JSON/HTML
DONE DONE DONE DONE DONE DONE DONE 

# Created BookService.java --> middle layer between BooksController(handling http) and BookRepository(direct db ops) ---> fetch all books
# Bookrepository ---> injected Bookservice instance
DONE DONE DONE DONE DONE DONE DONE 
# FEATURE --> SEARCH
# BookRepository --> add custom query method that allows search by book title
# bookservice ---> include a method that uses bookrepository method
# bookscontroller --> add end point to handle book search requests

5. DEVELOP FRONTEND  DEVELOP FRONTEND DEVELOP FRONTEND DEVELOP FRONTEND DEVELOP FRONTEND DEVELOP FRONTEND DEVELOP FRONTEND DEVELOP FRONTEND DEVELOP FRONTEND 

A --> web app Html/css/javascript   or java desktop app
B --> create interface to display the list of books of fetched fom your backend
C --> implement a simple form for adding new books to the databse 
D --> map the UI to URL
E ---> UI ---> html, that displays the data,angular/react
DONE DONE DONE DONE DONE DONE 

# Bookscontroller and HomeControllers are keys to handle HTTP requests and REACT/JS
will interact with these.     
# UI Components --> book list, details, search bar, navigation bar. 
# State of app --> useState/usecontext of React
# Data Fetching --> Axios to make http request to backend endpoint
# Routing --> navations with React router
# Forms and user input --> adding/editing book
# Styling --> css in js library
# error handling
# performance --> minimize re-renders, code-splitting,lazy loading components,bundle size

# steps --> install node.js and npm ---> 


6. get specific data from the backend. 
# 