import React from 'react';
import '../styles/Login.css';

const Login = () => {
  return (
    <div className="login-container">
      <div className="login-header">
        <span>Login</span>
      </div>
      <div className="login-form">
        <input type="text" placeholder="Username" />
        <input type="password" placeholder="Password" />
      </div>
    </div>
  );
};

export default Login;
