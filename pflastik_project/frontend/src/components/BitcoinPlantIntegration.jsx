import React from 'react';

const BitcoinPlantIntegration = () => {
    return (
        <div>
            <div className="card">
                <h2>Bitcoin-Plant Integration</h2>
                <div className="card-content">
                    <p>Merge your Bitcoin data into your favorite plant for innovative care and funding.</p>
                    <div id="bitcoin-plant-info">Select your favorite plant and enter your Bitcoin address below:</div>
                    <select id="plant-name">
                        <option value="">Select a plant</option>
                        <option value="rose">Rose</option>
                        <option value="sunflower">Sunflower</option>
                        <option value="cactus">Cactus</option>
                        <option value="orchid">Orchid</option>
                        <option value="ficus">Ficus</option>
                    </select>
                    <input type="text" id="bitcoin-address" placeholder="Bitcoin Address" />
                    <button className="btn">Link Bitcoin to Plant</button>
                </div>
            </div>
        </div>
    );
};

export default BitcoinPlantIntegration;
