// src/BookList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BookList = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8080/api/v1/books') // Adjust URL based on your backend
      .then(response => {
        setBooks(response.data);
      })
      .catch(error => {
        console.error('Error fetching books:', error); // error handling 
      });
  }, []);

  return (
    <div>
      <h2>Book List</h2>
      {books.map(book => <div key={book.id}>{book.title}</div>)}
    </div>
  );
};

export default BookList;
