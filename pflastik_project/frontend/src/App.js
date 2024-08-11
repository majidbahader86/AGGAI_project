import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import SignUpPage from './pages/SignUpPage';
import AskAiPage from './pages/AskAiPage';
import PhotoPage from './pages/PhotoPage';
import PlantsPage from './pages/PlantsPage';
import DiseasesPage from './pages/DiseasesPage';
import RootsPage from './pages/RootsPage';
import SeedsPage from './pages/SeedsPage';
import LeavesPage from './pages/LeavesPage';
import FlowersPage from './pages/FlowersPage';
import StemsPage from './pages/StemsPage';
import FungalPage from './pages/FungalPage';
import BacterialPage from './pages/BacterialPage';
import ViralPage from './pages/ViralPage';
import NematodePage from './pages/NematodePage';
import PhysiologicalDisorderPage from './pages/PhysiologicalDisorderPage';
import PublicationsPage from './pages/PublicationsPage';
import AiToolsPage from './pages/AiToolsPage';
import ForumPage from './pages/ForumPage';
import MonitoringPage from './pages/MonitoringPage';
import ForumPageFarmers from './pages/ForumPageFarmers';
import LearnAiPage from './pages/LearnAiPage';
import DiseaseReportsPage from './pages/DiseaseReportsPage';
import ScientificReportPage from './pages/ScientificReportPage';
import DatasetPage from './pages/DatasetPage';
import SecurityInfoPage from './pages/SecurityInfoPage';
import PrivacyPolicyPage from './pages/PrivacyPolicyPage';
import TermsOfServicePage from './pages/TermsOfServicePage';
import CookieSettingsPage from './pages/CookieSettingsPage';
import SubscriptionPolicyPage from './pages/SubscriptionPolicyPage';
import SitemapPage from './pages/SitemapPage';
import ContactPage from './pages/ContactPage';
import FAQPage from './pages/FAQPage';
import SubscriptionPage from './pages/SubscriptionPage';
import AboutUsPage from './pages/AboutUsPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/sign-up" element={<SignUpPage />} />
        <Route path="/ask-ai" element={<AskAiPage />} />
        <Route path="/photo" element={<PhotoPage />} />
        <Route path="/plants" element={<PlantsPage />} />
        <Route path="/diseases" element={<DiseasesPage />} />
        <Route path="/roots" element={<RootsPage />} />
        <Route path="/seeds" element={<SeedsPage />} />
        <Route path="/leaves" element={<LeavesPage />} />
        <Route path="/flowers" element={<FlowersPage />} />
        <Route path="/stems" element={<StemsPage />} />
        <Route path="/fungal" element={<FungalPage />} />
        <Route path="/bacterial" element={<BacterialPage />} />
        <Route path="/viral" element={<ViralPage />} />
        <Route path="/nematode" element={<NematodePage />} />
        <Route path="/physiological-disorders" element={<PhysiologicalDisorderPage />} />
        <Route path="/publications" element={<PublicationsPage />} />
        <Route path="/ai-tools" element={<AiToolsPage />} />
        <Route path="/forum" element={<ForumPage />} />
        <Route path="/monitoring" element={<MonitoringPage />} />
        <Route path="/forum-farmers" element={<ForumPageFarmers />} />
        <Route path="/learn-ai" element={<LearnAiPage />} />
        <Route path="/disease-reports" element={<DiseaseReportsPage />} />
        <Route path="/scientific-report" element={<ScientificReportPage />} />
        <Route path="/datasets" element={<DatasetPage />} />
        <Route path="/security-info" element={<SecurityInfoPage />} />
        <Route path="/privacy-policy" element={<PrivacyPolicyPage />} />
        <Route path="/terms-of-service" element={<TermsOfServicePage />} />
        <Route path="/cookie-settings" element={<CookieSettingsPage />} />
        <Route path="/subscription-policy" element={<SubscriptionPolicyPage />} />
        <Route path="/sitemap" element={<SitemapPage />} />
        <Route path="/contact" element={<ContactPage />} />
        <Route path="/faq" element={<FAQPage />} />
        <Route path="/subscription" element={<SubscriptionPage />} />
        <Route path="/about-us" element={<AboutUsPage />} />
      </Routes>
    </Router>
  );
}

export default App;
