graph TD
    A("NavBar Component") -->|Click on 'Books' link| B("BooksPage Component")
    B -->|Axios GET request to '/api/v1/books'| C("Backend /api/v1/books Endpoint")
    C -->|Response with all books| B
    B -->|Displays books in list format| D("Books List")

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#fcf,stroke:#333,stroke-width:2px
    style D fill:#cfc,stroke:#333,stroke-width:2px

