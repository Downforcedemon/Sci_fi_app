// src/NavBar.js
import React  from "react";
import { Link } from "react-router-dom"; 
import './NavBar.css';   

const navBar = () => (
    <nav>
        <Link to="/" className="nav-link">Home</Link>
        <Link to="/books"className="nav-link-books">Books</Link>
        <Link to="/projects" className="nav-link-books">Projects</Link>
    </nav>
);

export default navBar;

