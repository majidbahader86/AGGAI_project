import React from 'react';
import SignUpBackground from '../components/SignUpBackground';
import SignUp from '../components/SignUp';
import Login from '../components/Login';
import '../styles/SignUpPage.css';

const SignUpPage = () => {
  return (
    <div className="signup-page">
      <div className="background-text">
        {Array(20).fill().map((_, i) => (
          <span key={i}>AggAI </span>
        ))}
      </div>
      <SignUpBackground />
      <SignUp />
      <Login />
    </div>
  );
};

export default SignUpPage;
