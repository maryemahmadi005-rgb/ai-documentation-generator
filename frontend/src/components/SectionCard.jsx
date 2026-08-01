import { motion } from "framer-motion";
import "./SectionCard.css";

/**
 * Enveloppe standard pour chaque section de la page d'analyse
 * (Overview, Architecture, Repository, ...). Fournit l'ancre utilisée
 * par la Sidebar pour le scroll fluide, un titre cohérent, et la carte.
 */
function SectionCard({ id, title, description, icon: Icon, children }) {
  return (
    <section id={id} className="analysis-section">
      <div className="analysis-section-heading">
        {Icon && (
          <span className="section-icon">
            <Icon size={18} />
          </span>
        )}
        <div>
          <h2>{title}</h2>
          {description && <p>{description}</p>}
        </div>
      </div>
      <motion.div
        className="card section-card-body"
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-80px" }}
        transition={{ duration: 0.45, ease: [0.22, 1, 0.36, 1] }}
      >
        {children}
      </motion.div>
    </section>
  );
}

export default SectionCard;
