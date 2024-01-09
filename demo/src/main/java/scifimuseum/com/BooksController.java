package scifimuseum.com;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1")
@CrossOrigin(origins = "http://localhost:3000")
public class BooksController {
    
    @Autowired
    private BookService bookService;

    @GetMapping("/books")
    public ResponseEntity<List<Books>> getAllBooks(){
        List<Books> allBooks = bookService.findAllBooks();
        return ResponseEntity.ok(allBooks);
    }

    @GetMapping("/books/search")
    public ResponseEntity<List<Books>> searchBooksByTitle(@RequestParam String title){
        List<Books> booksByTitle = bookService.searchBooksByTitle(title);
        return ResponseEntity.ok(booksByTitle);
    }

    @GetMapping("/books/search/author")
    public ResponseEntity<List<BookDTO>> searchBooksByAuthor(@RequestParam String author){
        List<BookDTO> booksByAuthor = bookService.searchBooksByAuthor(author);
        return ResponseEntity.ok(booksByAuthor);
    }
}

