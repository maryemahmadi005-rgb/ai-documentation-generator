import { motion } from "framer-motion";
import { FolderSearch, BrainCircuit, Layers, BookOpenCheck } from "lucide-react";
import "./FeatureCards.css";

const FEATURES = [
  {
    icon: FolderSearch,
    title: "Repository Analysis",
    description: "Deep scan of your codebase — files, folders, dependencies and languages used.",
  },
  {
    icon: BrainCircuit,
    title: "AI Code Understanding",
    description: "Large language models read the code to understand what it actually does.",
  },
  {
    icon: Layers,
    title: "Architecture Detection",
    description: "Automatically identifies the architectural pattern behind your project.",
  },
  {
    icon: BookOpenCheck,
    title: "Documentation Builder",
    description: "Turns the analysis into clear, structured, ready-to-share documentation.",
  },
];

/**
 * Grille de cartes présentant les capacités principales du produit.
 */
function FeatureCards() {
  return (
    <section className="feature-section">
      <div className="section-heading">
        <span className="eyebrow">Capabilities</span>
        <h2>Everything needed to document a codebase</h2>
      </div>

      <div className="feature-grid">
        {FEATURES.map((feature, index) => {
          const Icon = feature.icon;
          return (
            <motion.div
              key={feature.title}
              className="feature-card card"
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.5, delay: index * 0.08, ease: [0.22, 1, 0.36, 1] }}
            >
              <div className="feature-icon">
                <Icon size={22} />
              </div>
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
            </motion.div>
          );
        })}
      </div>
    </section>
  );
}

export default FeatureCards;
