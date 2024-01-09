// src/BookForm.js
import React, { useState } from 'react';
import axios from 'axios';

const BookForm = ({ onBookAdded }) => {
  const [title, setTitle] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://localhost:8080', { title })
      .then(() => {
        onBookAdded();
        setTitle('');
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={title} 
        onChange={e => setTitle(e.target.value)} 
        placeholder="Book title" 
      />
      <button type="submit">Add Book</button>
    </form>
  );
};

export default BookForm;
