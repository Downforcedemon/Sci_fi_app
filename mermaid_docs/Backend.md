graph LR
    A[Client] -->|Request /books| B[BooksController]
    B -->|Fetch data| C[BookService]
    C -->|Use| D[BookRepository]
    D -->|Interact with| E[Database]
    B -->|Return Data| F[Format Data]
    F -->|JSON/HTML| A
    G[UI Layer] -->|Fetch Data from API| B
    G -->|Display Data| A

