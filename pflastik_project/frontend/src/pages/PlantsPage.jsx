import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import PlantsPageBackground from '../components/PlantsPageBackground';
import PlantsContainers from '../components/PlantsContainers';
import PlantsText from '../components/PlantsText';
import '../styles/PlantsPage.css';

const PlantsPage = () => {
  return (
    <div className="plants-page">
      <Header />
      <PlantsPageBackground />
      <PlantsText />
      <PlantsContainers />
      <Footer />
    </div>
  );
};

export default PlantsPage;

