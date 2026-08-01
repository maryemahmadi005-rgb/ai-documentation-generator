import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";
import GithubVisual from "./GithubVisual.jsx";
import "./Hero.css";

/**
 * Section hero de la page Home. Le formulaire (ou le composant de
 * progression pendant l'analyse) est injecté via `children` pour garder
 * Hero purement présentationnel.
 */
function Hero({ children }) {
  return (
    <section className="hero-grid">
      <motion.div
        className="hero-copy"
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.55, ease: [0.22, 1, 0.36, 1] }}
      >
        <span className="eyebrow">
          <Sparkles size={13} /> AI-Powered Documentation Engine
        </span>
        <h1>Turn Any GitHub Repository Into Professional Documentation With AI</h1>
        <p className="hero-subtitle">
          DocGen AI clones your repository, reads and understands the code,
          detects the underlying software architecture, and uses AI to
          generate clear, accurate technical documentation — automatically,
          in minutes.
        </p>

        {children}
      </motion.div>

      <motion.div
        className="hero-visual"
        initial={{ opacity: 0, scale: 0.94 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.6, delay: 0.15, ease: [0.22, 1, 0.36, 1] }}
      >
        <GithubVisual />
      </motion.div>
    </section>
  );
}

export default Hero;
