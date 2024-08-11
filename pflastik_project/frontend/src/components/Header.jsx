// src/components/Header.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Header.css';

const Header = () => {
  const navigate = useNavigate();

  const handleSearch = (e) => {
    if (e.key === 'Enter') {
      window.location.href = `/search?q=${e.target.value}`;
    }
  };  
  return (
    <header className="header">
      <div className="nav-left">
        <div className="logo"></div>
        <nav>
          <ul>
            <li className="dropdown">
              Disease Identification
              <ul className="dropdown-content">
                <li onClick={() => window.location.href = '/ask-ai'}>Ask AI</li>
                <li onClick={() => window.location.href = '/photo'}>Photo</li>
              </ul>
            </li>
            <li className="dropdown">
              Disease Library
              <ul className="dropdown-content">
                <li className="submenu">
                  <span onClick={() => window.location.href = '/plants'}>Plants</span>
                    <ul className="submenu-content">
                      <li onClick={() => window.location.href = '/roots'}>Roots</li>
                      <li onClick={() => window.location.href = '/seeds'}>Seeds</li>
                      <li onClick={() => window.location.href = '/flowers'}>Flowers</li>
                      <li onClick={() => window.location.href = '/leaves'}>Leaves</li>
                      <li onClick={() => window.location.href = '/stems'}>Stems</li>
                    </ul>  
                </li>
                <li className="submenu">
                  <span onClick={() => window.location.href = '/diseases'}>Diseases</span>
                  <ul className="submenu-content">
                    <li onClick={() => window.location.href = '/fungal'}>Fungal</li>
                    <li onClick={() => window.location.href = '/bacterial'}>Bacterial</li>
                    <li onClick={() => window.location.href = '/viral'}>Viral</li>
                    <li onClick={() => window.location.href = '/nematode'}>Nematode</li>
                    <li onClick={() => window.location.href = '/physiological-disorders'}>Physiological Disorders</li>
                  </ul>
                </li>
              </ul>
            </li>
            <li className="dropdown">
              Scientists
              <ul className="dropdown-content">
                <li onClick={() => window.location.href = '/publications'}>Publications</li>
                <li onClick={() => window.location.href = '/ai-tools'}>AI Tools</li>
                <li onClick={() => window.location.href = '/forum'}>Forum</li>
              </ul>
            </li>
            <li className="dropdown">
              Farmers
              <ul className="dropdown-content">
                <li onClick={() => window.location.href = '/monitoring'}>Monitoring</li>
                <li onClick={() => window.location.href = '/forum-farmers'}>Forum</li>
              </ul>
            </li>
            <li className="dropdown">
              AI
              <ul className="dropdown-content">
                <li onClick={() => window.location.href = '/ask-ai'}>Ask AI</li>
                <li onClick={() => window.location.href = '/ai-tools'}>AI Tools</li>
                <li onClick={() => window.location.href = '/learn-ai'}>Learn AI</li>
              </ul>
            </li>
            <li className="dropdown">
              Blockchain
              <ul className="dropdown-content">
                <li onClick={() => window.location.href = '/disease-reports'}>Disease Reports</li>
                <li onClick={() => window.location.href = '/scientific-report'}>Scientific Report</li>
                <li onClick={() => window.location.href = '/datasets'}>Datasets</li>
                <li onClick={() => window.location.href = '/security-info'}>Security Info</li>
              </ul>
            </li>
          </ul>
        </nav>
      </div>
      <div className="nav-right">
        <div className="search-container">
            <img src="/assets/HEADER/SEARCH_icon.png" alt="Search" className="search-icon" onClick={() => window.location.href = `/search?query=${document.querySelector('.search-rectangle').value}`} />
            <input type="text" className="search-rectangle" onKeyDown={handleSearch} />
        </div>
        <div className="translation"></div>
        <div className="menu">
          <div className="menu-icon" onClick={() => navigate('/sign-up')}>
            <div className="menu-bar"></div>
            <div className="menu-bar"></div>
            <div className="menu-bar"></div>
            <div className="menu-bar"></div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
