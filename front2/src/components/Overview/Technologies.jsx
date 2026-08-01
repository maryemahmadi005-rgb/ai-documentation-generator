import EmptyState from "../Common/EmptyState.jsx";
import "./Technologies.css";

/**
 * Affiche `analysis.technologies` (liste de strings, ex:
 * ["Python", "JavaScript (React)"]) sous forme de badges.
 */
function Technologies({ technologies }) {
  if (!Array.isArray(technologies) || technologies.length === 0) {
    return (
      <EmptyState
        title="No technologies detected"
        message="Technologies couldn't be inferred from the analyzed files."
      />
    );
  }

  return (
    <div className="technologies-list">
      {technologies.map((tech) => (
        <span key={tech} className="technology-badge">
          {tech}
        </span>
      ))}
    </div>
  );
}

export default Technologies;
