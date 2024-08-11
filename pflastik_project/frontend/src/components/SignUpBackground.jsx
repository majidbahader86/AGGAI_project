import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/SignUpBackground.css';

const SignUpBackground = () => {
  const navigate = useNavigate();

  return (
    <div className="signup-background">
      <img
        src="../assets/tree_tech_LOGO.png" // Replace with your logo path
        alt="AggAI Logo"
        className="aggai-logo"
        onClick={() => navigate('/')}
      />
    </div>
  );
};

export default SignUpBackground;
