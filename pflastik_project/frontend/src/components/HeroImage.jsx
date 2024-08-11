import React from 'react';
import youngPlant from '../assets/HERO_IMAGE/young_plant.png';
import dataGraphMesh from '../assets/HERO_IMAGE/DATA_GRAPH_MESH.png';
import '../styles/HeroImage.css';

const HeroImage = () => {
  return (
    <div className="hero-container">
      <div className="young-plant" style={{ backgroundImage: `url(${youngPlant})` }}></div>
      <div className="data-graph-mesh" style={{ backgroundImage: `url(${dataGraphMesh})` }}></div>
      <div className="aggai">AggAI</div>
    </div>
  );
};

export default HeroImage;
