package scifimuseum.com;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class BookService {
    @Autowired
    private BooksRepository bookRepository;

    public List<Books> findAllBooks(){
        return bookRepository.findAll();
    }
    
    public List<Books> searchBooksByTitle(String title){
        return bookRepository.findByTitleContainingIgnoreCase(title);
    }
    
    public List<BookDTO> searchBooksByAuthor(String author){
        return bookRepository.findBooksByAuthor(author);
    }
}
