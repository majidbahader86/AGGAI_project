import React from 'react';
import '../styles/PlantsContainers.css';
import { useNavigate } from 'react-router-dom';

const PlantsContainers = () => {
  const navigate = useNavigate();

  const containerData = [
    { name: 'Seeds', image: '../assets/Seeds.png', route: '/seeds' },
    { name: 'Roots', image: '../assets/Roots.png', route: '/roots' },
    { name: 'Leaves', image: '../assets/Leaves.png', route: '/leaves' },
    { name: 'Stems', image: '../assets/Stems.png', route: '/stems' },
    { name: 'Flowers', image: '../assets/Flowers.png', route: '/flowers' }
  ];

  return (
    <div className="plants-containers">
      {containerData.map((container, index) => (
        <div 
          key={index} 
          className="plant-container" 
          onClick={() => navigate(container.route)}
        >
          <span className="plant-name">{container.name}</span>  
          <img src={container.image} alt={container.name} className="plant-image"/>
        </div>
      ))}
    </div>
  );
};

export default PlantsContainers;
