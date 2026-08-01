import { motion } from "framer-motion";
import { Sparkles, Cpu, ShieldCheck, Zap } from "lucide-react";
import "./HeroSection.css";

function HeroSection({ children }) {
  return (
    <section className="hero-section">
      <motion.div
        className="hero-copy"
        initial={{ opacity: 0, y: 24 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
      >
        <div className="hero-badge">
          <Sparkles size={14} /> AI-powered documentation engine
        </div>

        <h1>
          GitHub to Docs.
          <span> Instantly.</span>
        </h1>

        <p className="hero-subtitle">
          Analyze any GitHub repository and generate professional technical documentation with AI in minutes.
        </p>

        {children}

        <div className="hero-proof-row">
          <div className="hero-proof-item">
            <Cpu size={16} /> Architecture-aware
          </div>
          <div className="hero-proof-item">
            <ShieldCheck size={16} /> Production-ready output
          </div>
          <div className="hero-proof-item">
            <Zap size={16} /> Lightning fast setup
          </div>
        </div>
      </motion.div>

      <motion.div
        className="hero-visual"
        initial={{ opacity: 0, scale: 0.96 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.7, delay: 0.12, ease: [0.22, 1, 0.36, 1] }}
      >
        <div className="hero-grid-card">
          <div className="hero-grid-card__header">
            <span className="dot" />
            <span className="dot" />
            <span className="dot" />
          </div>

          <div className="hero-grid-card__body">
            <div className="preview-panel">
              <p className="preview-label">AI Documentation Engine</p>
              <h3>Ready to analyze your repository</h3>
              <div className="preview-tags">
                <span>GitHub</span>
                <span>AI Analysis</span>
                <span>Documentation</span>
              </div>
            </div>

            <div className="preview-stack">
              <div className="preview-bar large" />
              <div className="preview-bar" />
              <div className="preview-bar" />
            </div>
          </div>
        </div>
      </motion.div>
    </section>
  );
}

export default HeroSection;
