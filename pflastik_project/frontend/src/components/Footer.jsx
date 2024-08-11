import React from 'react';
import '../styles/Footer.css';

import treeTechLogo from '../assets/FOOTER/tree_tech_logo_footer.png';
import twitterLogo from '../assets/FOOTER/Twitter_new_X_logo.png';
import linkedinLogo from '../assets/FOOTER/Linkedin_circle_black-512.png';
import discordLogo from '../assets/FOOTER/DISCORD.png';
import appleAppLogo from '../assets/FOOTER/APPLE_APP.png';
import googlePlayLogo from '../assets/FOOTER/Google-Play-Logo-PNG-Photos.png';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <img src={treeTechLogo} alt="Tree Tech Logo" className="footer-logo" onClick={() => window.location.href = '/'} />
        <div className="footer-links">
          <a href="/privacy-policy">Privacy Policy</a>
          <a href="/terms-of-service">Terms of Service</a>
          <a href="/cookie-settings">Cookie Settings</a>
          <a href="/subscription-policy">Subscription Policy</a>
          <a href="/sitemap">Sitemap</a>
          <a href="/contact">Contact</a>
          <a href="/faq">FAQ</a>
          <a href="/subscription">Subscription</a>
          <a href="/about-us">About Us</a>
        </div>
        <div className="footer-app-links">
          <a href="https://www.apple.com/app-store/"><img src={appleAppLogo} alt="Apple App" /></a>
          <a href="https://play.google.com/store/apps?hl=en&pli=1"><img src={googlePlayLogo} alt="Google Play" /></a>
        </div>
        <div className="footer-social">
          <a href="https://x.com/ai_agg"><img src={twitterLogo} alt="Twitter" /></a>
          <a href="https://www.linkedin.com/in/aggai-corp-46555b31b/"><img src={linkedinLogo} alt="LinkedIn" /></a>
          <a href="https://discord.com/channels/@agg_ai"><img src={discordLogo} alt="Discord" /></a>
        </div>
        <div className="footer-copyright">
          <p>© 2024 AggAI</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
