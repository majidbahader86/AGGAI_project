import React, { useState } from 'react';
import '../styles/SignUp.css';

const SignUp = () => {
    const [userType, setUserType] = useState('Scientist');
  
    const renderFormFields = () => {
      switch (userType) {
        case 'Scientist':
          return (
            <div>
              <div className="left-field">
                <input type="text" placeholder="Name" />
                <input type="email" placeholder="Email" />
              </div>
              <div className="right-field">
                <input type="text" placeholder="Username" />
                <input type="password" placeholder="Password" />
              </div>
              <div className="middle-field">
                <input type="text" placeholder="Research Center/University" />
              </div>
            </div>
          );
        case 'Farmer':
          return (
            <div>
              <div className="left-field">
                <input type="text" placeholder="Name" />
                <input type="email" placeholder="Email" />
              </div>
              <div className="right-field">
                <input type="text" placeholder="Username" />
                <input type="password" placeholder="Password" />
              </div>
              <div className="middle-field">
                <input type="text" placeholder="Kolkhoze" />
              </div>
            </div>
          );
        case 'Plant Lover':
          return (
            <div>
              <div className="left-field">
                <input type="text" placeholder="Name" />
                <input type="email" placeholder="Email" />
              </div>
              <div className="right-field">
                <input type="text" placeholder="Username" />
                <input type="password" placeholder="Password" />
              </div>
            </div>
          );
        default:
          return null;
      }
    };
  
    return (
      <div className="signup-container">
        <div className="signup-header">
          <span>SignUp</span>
          <div className="user-type-select-container">
            <select
              className="user-type-select"
              value={userType}
              onChange={(e) => setUserType(e.target.value)}
            >
              <option value="Scientist">Scientist</option>
              <option value="Farmer">Farmer</option>
              <option value="Plant Lover">Plant Lover</option>
            </select>
          </div>
        </div>
        <div className="signup-form">
          {renderFormFields()}
        </div>
      </div>
    );
  };

  export default SignUp;