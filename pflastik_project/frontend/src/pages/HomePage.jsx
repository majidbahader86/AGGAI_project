// src/pages/HomePage.jsx
import React from 'react';
import Header from '../components/Header';
import HeroImage from '../components/HeroImage';
import BodyText from '../components/BodyText';
import Footer from '../components/Footer';
import Background from '../components/Background';
import BodyImage from '../components/BodyImage';
import '../styles/HomePage.css';

const HomePage = () => {
  return (
    <div className="page-container">
      <Header />
      <Background />
      <div className="content-wrapper">
        <HeroImage />
        <BodyText />
        <BodyImage />        
      </div>
      <Footer />
    </div>
  );
};

export default HomePage;

