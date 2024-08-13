import React, { useState } from 'react';
import Navbar from './Navbar';

function App() {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  return (
    <div>
      <Navbar theme={theme} toggleTheme={toggleTheme} />
    </div>
  );
}

export default App;
