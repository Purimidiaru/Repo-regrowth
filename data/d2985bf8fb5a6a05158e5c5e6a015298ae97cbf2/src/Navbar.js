import React from 'react';
import ThemeToggle from './ThemeToggle';

const Navbar = ({ theme, toggleTheme }) => {
  return (
    <nav
      className={`shadow-lg ${
        theme === 'light' ? 'bg-white text-gray-800' : 'bg-gray-800 text-white'
      }`}
      style={{ backgroundColor: theme === 'dark' ? 'rgb(127, 127, 127)' : '' }}
    >
      <div className="container mx-auto px-6 py-3">
        <div className="flex justify-between items-center w-full">
          {/* Profil et nom, aligné à gauche */}
          <div className="flex items-center">
            <img
              src="/assets/profile.jpg"
              alt="Profile"
              className="w-12 h-12 rounded-full mr-4"
            />
            <div className="text-lg font-semibold">
              Dam Quang Thanh Paul
            </div>
          </div>

          {/* Section centrale, décalée à 40% */}
          <div className="flex-1 flex justify-start items-center space-x-8" style={{ marginLeft: '20%' }}>
            <a
              href="#"
              className="flex items-center"
              style={{ fontSize: '16px', minWidth: '100px' }}
            >
              <img
                src="/assets/cv-icon.png"
                alt="CV Icon"
                className="w-6 h-6 mr-2"
              />
              <span>Resume</span>
            </a>
            <a
              href="#"
              className="flex items-center"
              style={{ fontSize: '16px', minWidth: '100px' }}
            >
              <img
                src="/assets/projects-icon.png"
                alt="Projects Icon"
                className="w-6 h-6 mr-2"
              />
              <span>Projects</span>
            </a>
            <a
              href="#"
              className="flex items-center"
              style={{ fontSize: '16px', minWidth: '100px' }}
            >
              <img
                src="/assets/github-icon.png"
                alt="Code Source Icon"
                className="w-6 h-6 mr-2"
              />
              <span>Source</span>
            </a>
          </div>

          {/* Switcher de thème, aligné à droite */}
          <div className="flex items-center">
            <ThemeToggle theme={theme} toggleTheme={toggleTheme} />
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
