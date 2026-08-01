import { motion } from "framer-motion";
import { Github, ArrowRight } from "lucide-react";
import "./RepositoryInput.css";

function RepositoryInput({ githubUrl, onChange, onSubmit, analyzing, error }) {
  return (
    <form className="repository-form" onSubmit={onSubmit} noValidate>
      <label className="repository-input-shell">
        <Github size={18} className="repository-input-icon" />
        <input
          type="text"
          value={githubUrl}
          onChange={(event) => onChange(event.target.value)}
          placeholder="https://github.com/organization/repository"
          disabled={analyzing}
        />
      </label>

      <motion.button
        type="submit"
        className="repository-button"
        whileHover={{ y: -2, scale: 1.01 }}
        whileTap={{ scale: 0.98 }}
        disabled={analyzing}
      >
        {analyzing ? "Analyzing..." : "Analyze Repository"}
        <ArrowRight size={18} />
      </motion.button>

      {error ? <p className="repository-error">{error}</p> : null}
    </form>
  );
}

export default RepositoryInput;
