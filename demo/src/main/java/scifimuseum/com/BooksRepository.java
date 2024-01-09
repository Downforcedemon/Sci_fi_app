package scifimuseum.com;

import org.springframework.stereotype.Repository;
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query; 


@Repository
public interface BooksRepository extends JpaRepository<Books, Long> {
    
    List<Books> findByTitleContainingIgnoreCase(String title);
    // use JPQL to query the database
    @Query("SELECT new scifimuseum.com.BookDTO(b.title, b.author) FROM Books b WHERE b.author = ?1")
    List<BookDTO> findBooksByAuthor(String author); 
}


