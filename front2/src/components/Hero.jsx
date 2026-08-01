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
    <section className="hero-centered">
      <motion.div
        className="hero-copy"
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.55, ease: [0.22, 1, 0.36, 1] }}
      >
        <span className="eyebrow">
          <Sparkles size={13} /> AI-Powered Documentation Engine
        </span>
        <h1> Generate Professional Documentation From Any Repository</h1>
        <p className="hero-subtitle">
           DocGen AI analyzes your GitHub repository, detects its architecture,
           and generates accurate technical documentation automatically.
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
