import React from 'react';

const FormSection = ({ activeForm }) => {
    return (
        <div>
            {activeForm === 'plantDiseaseForm' && (
                <div id="plantDiseaseForm" className="card">
                    <h2>Add Plant Disease Information</h2>
                    <form id="diseaseForm">
                        <input type="text" placeholder="Plant Disease Info" />
                        <button type="submit" className="btn">Submit Plant Disease Info</button>
                    </form>
                </div>
            )}
            {activeForm === 'paperForm' && (
                <div id="paperForm" className="card">
                    <h2>Sign Paper to Chain</h2>
                    <form id="paperForm">
                        <input type="text" placeholder="Paper Information" />
                        <button type="submit" className="btn">Sign Paper to Chain</button>
                    </form>
                </div>
            )}
            {activeForm === 'datasetForm' && (
                <div id="datasetForm" className="card">
                    <h2>Sign Dataset to Chain</h2>
                    <form id="datasetForm">
                        <input type="text" placeholder="Dataset Information" />
                        <button type="submit" className="btn">Sign Dataset to Chain</button>
                    </form>
                </div>
            )}
        </div>
    );
};

export default FormSection;
