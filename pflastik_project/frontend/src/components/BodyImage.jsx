import React from 'react';
import cropsImage from '../assets/BODY_IMAGE/cROPS.png';
import roboPillImage from '../assets/BODY_IMAGE/robo_pill.png';
import '../styles/BodyImage.css';

const BodyImage = () => {
  return (
    <div className="body-image-container">
      <div className="crops" style={{ backgroundImage: `url(${cropsImage})` }}></div>
      <div className="robo-pill" style={{ backgroundImage: `url(${roboPillImage})` }}></div>
    </div>
  );
};

export default BodyImage;

