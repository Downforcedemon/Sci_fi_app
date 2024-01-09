graph TD
    subgraph Frontend [React Application]
        AA[App.js<br>Root component, defines routes] -->|Routes| BB[BookList.js<br>Fetches list of books]
        AA -->|Routes| CC[BookDetails.js<br>Fetches book details]
        BB -->|Axios GET /api/v1/books| DD[Backend API /books<br>Endpoint in BooksController.java]
        CC -->|Axios GET /api/v1/books/:id| EE[Backend API /books/:id<br>Endpoint in BooksController.java]
    end

    subgraph Backend [Java Maven Project]
        A[App.java<br>Main Application Entry Point] -->|Main Application Entry Point| B[HomeController.java<br>Manages Home Page Requests like default url]
        A -->|Main Application Entry Point| C[BooksController.java<br>Manages Book-related Requests]
        C -->|CRUD Operations| E[BooksRepository.java<br>Data Access Layer for Books]
        E -->|JPA| F[Books.java<br>Defines book Data Structure]
        B -->|Configuration Settings| D[application.properties<br>Contains Configuration Settings]
        DD --> C
        EE --> C
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#f66,stroke-width:2px
    style C fill:#9f6,stroke:#333,stroke-width:2px
    style D fill:#ff9,stroke:#333,stroke-width:2px
    style E fill:#9ff,stroke:#333,stroke-width:2px
    style F fill:#f99,stroke:#333,stroke-width:2px
    style AA fill:#f9f,stroke:#333,stroke-width:2px
    style BB fill:#ccf,stroke:#333,stroke-width:2px
    style CC fill:#ccf,stroke:#333,stroke-width:2px
    style DD fill:#fcf,stroke:#333,stroke-width:2px
    style EE fill:#fcf,stroke:#333,stroke-width:2px

