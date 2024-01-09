import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar/NavBar';
import BooksPage from './pages/BooksPage';

import ProjectsPage from './pages/Projectspage';
import PlanetSearch from './pages/PlanetSearch';


const App = () => (
  <Router>
    <NavBar />
    <Routes>
      
      <Route path="/books" element={<BooksPage />} />
      <Route path="/projects" element={<ProjectsPage />} />
      <Route path="/projects/planetsearch" element={<PlanetSearch />} />
      {/* other routes */}
    </Routes>
  </Router>
);

export default App;
