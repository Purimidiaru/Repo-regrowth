import React, { useState, useEffect } from 'react';
import anime from 'animejs';

const ThemeToggle = ({ theme, toggleTheme }) => {
  const sunPath =
    "M55 27.5C55 42.6878 42.6878 55 27.5 55C12.3122 55 0 42.6878 0 27.5C0 12.3122 12.3122 0 27.5 0C42.6878 0 55 12.3122 55 27.5Z";
  const moonPath =
    "M16 27.5C16 42.6878 27.5 52.5 27.5 55C12.3122 55 0 42.6878 0 27.5C0 12.3122 12.3122 0 27.5 0C27.5 0 16 12.3122 16 27.5Z";

  const [toggle, setToggle] = useState(theme === 'dark');

  useEffect(() => {
    const timeline = anime.timeline({
      duration: 300,
      easing: "easeOutExpo",
    });

    timeline
      .add({
        targets: ".sun",
        d: [{ value: toggle ? moonPath : sunPath }],
      })
      .add(
        {
          targets: "#darkMode",
          rotate: toggle ? 320 : 0,
        },
        "-= 150"
      )
      .add(
        {
          targets: "body",
          backgroundColor: toggle ? "rgb(22,22,22)" : "rgb(255,255,255)",
          color: toggle ? "rgb(255,255,255)" : "rgb(22,22,22)",
        },
        "-= 150"
      );
  }, [toggle]);

  const handleToggle = () => {
    setToggle(!toggle);
    toggleTheme();
  };

  return (
    <div className="ml-auto flex items-center" style={{ padding: '0 16px' }}>
      <svg
        id="darkMode"
        onClick={handleToggle}
        width="35"  
        height="35"
        viewBox="0 0 55 55"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        style={{ cursor: "pointer" }}
      >
        <path
          className="sun"
          d={sunPath}
          fill="#FBD301"
          fillOpacity="0.91"
        />
      </svg>
    </div>
  );
};

export default ThemeToggle;
