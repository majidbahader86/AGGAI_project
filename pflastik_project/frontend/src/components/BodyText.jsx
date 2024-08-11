import React from 'react';
import { Link } from 'react-router-dom'; // Use Link from react-router-dom for navigation
import '../styles/BodyText.css';

const BodyText = () => {
  return (
    <div className="body-text">
      <div className="section what-is-aggai">
        <h2>What is AggAI?</h2>
        <p>
          AggAI is an innovative platform harnessing the power of cutting-edge artificial intelligence and modern agricultural technologies to revolutionize plant disease detection and crop management. By leveraging state-of-the-art machine learning algorithms, AggAI provides precise, real-time diagnostics and actionable solutions to farmers and scientists, ensuring healthier plants and higher yields. The website and app serve as a comprehensive resource for monitoring crops, offering tailored recommendations for disease treatment and prevention based on extensive data analysis. Not just for the agricultural elite, AggAI empowers everyday users with user-friendly tools and insights, making advanced plant care accessible to all. In essence, AggAI is transforming the future of agriculture, blending scientific rigor with practical application to cultivate a smarter, greener world.
        </p>
      </div>
      
      <div className="rotating-earth-placeholder">
        
      </div>
      
      <div className="four-columns">
        <div className="section">
          <h2>Disease Identifier</h2>
          <p>
            Imagine whipping out your phone camera and becoming a plant doctor in seconds! With AggAI's Disease Identifier, you can leverage advanced AI tools to diagnose plant diseases straight from your pocket. The platform transforms your phone camera into a powerful Imaging Sensor, achieving precise diagnostics by comparing visual disease identification with sensor imaging. Simply snap a photo of the afflicted plant part, and our AI will cross-reference it with our extensive library to pinpoint the problem. For those who prefer a more conversational approach, the <Link to="/photo" className="highlight">Photo Identification</Link> or <Link to="/ask-ai" className="highlight">Ask AI</Link> feature lets you chat with our intelligent system to get insights and advice. Whether you choose Photo Identification or Ask AI, AggAI ensures you're equipped with the knowledge to tackle plant diseases head-on. It's like having a high-tech, pocket-sized botanist at your disposal!
          </p>
        </div>
        
        <div className="section">
          <h2>Disease Library</h2>
          <p>
            Dive into AggAI's extensive Disease Library, meticulously divided into two main sections: <Link to="/plants" className="highlight">Plants</Link> and <Link to="/diseases" className="highlight">Diseases</Link>. This unique partition allows for an in-depth comparison of healthy plant parts against diseased ones. On the Plants side, you'll find a wealth of information about seeds, roots, leaves, stems, and flowers, showcasing their natural state and realistic disease potential. On the Diseases side, our library covers the most common afflictions, including viral, bacterial, fungal, nematode, and physiological disorders. This comprehensive database offers unparalleled insights into the telltale signs of each disease, enabling precise identification and effective treatment. Whether you're a scientist, farmer, or curious gardener, AggAI's Disease Library is your ultimate resource for plant health and disease management.
          </p>
        </div>
        
        <div className="section">
          <h2>Scientists</h2>
          <p>
            AggAI is a treasure trove for scientists, offering specialized features tailored to their research needs. Our platform provides <Link to="/ai-tools" className="highlight">AI Tutorials</Link> specifically designed for the unique projects scientists are working on, ensuring they harness the full potential of AI in their studies. Access to public <Link to="/publications" className="highlight">Science Publications</Link> on plant diseases is readily available, alongside exclusive publications accessible only through AggAI. The <Link to="/forum" className="highlight">Scientists Forum</Link> is a vibrant hub where biologists, IT engineers, and students can exchange knowledge, ideas, and breakthroughs. This collaborative space fosters innovation and interdisciplinary synergy, pushing the boundaries of plant disease research. With AggAI, scientists have a comprehensive toolkit at their fingertips, accelerating their research and discoveries.
          </p>
        </div>
        
        <div className="section">
          <h2>Farmers</h2>
          <p>
            Farmers, welcome to your digital ally in crop management! AggAI offers a suite of features designed to support and enhance your farming practices. The <Link to="/monitoring" className="highlight">Monitoring</Link> tool allows you to track the progress of your crops by posting daily or weekly pictures, with AI providing tailored advice on their health. Stay ahead of the curve with 'Season Alerts' and 'Weather Conditions' updates, ensuring you’re prepared for any environmental changes. Get practical 'Care Tips' to optimize your crop yield and health. The <Link to="/forum-farmers" className="highlight">Farmers Forum</Link> is a dynamic space where farmers, biologists, and engineers converge to share knowledge and solutions. With AggAI, you're not just farming; you're engaging in a collaborative, high-tech agricultural revolution.
          </p>
        </div>
      </div>

      
      
      <div className="section blockchain">
        <h2>Blockchain</h2>
        <p>
          In the realm of cutting-edge research and data exchange, security is paramount. AggAI utilizes blockchain technology to safeguard your sensitive research data, ensuring it remains protected and tamper-proof. Business partners and researchers can confidently exchange data and tools, knowing they're in a secure environment. The 'Diseases Reports', 'Scientific Papers', 'Datasets', and 'Security Info' sections are all fortified with blockchain's robust security protocols. This means your valuable information is shielded from unauthorized access, providing peace of mind and fostering a trustworthy collaborative atmosphere. With AggAI's blockchain integration, you can focus on innovation, knowing your data is in safe hands.
        </p>
      </div>
    </div>
  );
};

export default BodyText;
