package scifimuseum.com;

public class BookDTO {
    private String title;
    private String author;

    // Default no-argument constructor
    public BookDTO() {
    }

    // Constructor with parameters
    public BookDTO(String title, String author) {
        this.title = title;
        this.author = author;
    }

    // Getter and setter for title
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    // Getter and setter for author
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
}

