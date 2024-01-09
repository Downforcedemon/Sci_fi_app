import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BooksPage = () => {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBooks = async () => {
      setError(null); // Reset error state before new request
      try {
        const response = await axios.get('http://localhost:8080/api/v1/books/search/author', {
          params: { author: 'Iain M. Banks' }
        });
        setBooks(response.data);
      } catch (err) {
        console.error('Error fetching books', err);
        setError('Failed to load books. Please try again later.');
      }
    };

    fetchBooks();
  }, []); // The empty array means this effect runs once on component mount

  return (
    <div>
      <h1>Books by Iain M. Banks</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {books.map((book) => (
          // Assuming each book has a unique 'id' or similar field
          <li key={book.id || book.title}> 
            <strong>Title:</strong> {book.title} <br />
            <strong>Author:</strong> {book.author}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BooksPage;

