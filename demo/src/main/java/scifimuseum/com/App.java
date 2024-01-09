package scifimuseum.com;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import java.util.List;

@SpringBootApplication
public class App {

    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(App.class, args);    
        BooksRepository bookRepository = context.getBean(BooksRepository.class);
        List<Books> books = bookRepository.findAll();
        books.forEach(System.out::println);
    }
}

