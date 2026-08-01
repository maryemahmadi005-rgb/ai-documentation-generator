import { Github, ArrowRight } from "lucide-react";
import PipelineProgress from "./Architecture/PipelineProgress.jsx";
import ErrorMessage from "./Common/ErrorMessage.jsx";
import "./GenerateForm.css";

/**
 * Formulaire de saisie de l'URL GitHub. Pendant l'analyse, affiche
 * PipelineProgress à la place du formulaire. Purement contrôlé par les
 * props : toute la logique et l'appel API restent dans la page Home.
 */
function GenerateForm({ githubUrl, onChange, onSubmit, analyzing, error }) {
  if (analyzing) {
    return (
      <div className="card hero-progress-card">
        <PipelineProgress active={analyzing} />
      </div>
    );
  }

  return (
    <>
      <form onSubmit={onSubmit} className="hero-form" noValidate>
        <div className="hero-input-wrap">
          <Github size={17} className="hero-input-icon" />
          <input
            type="text"
            className="form-control hero-input"
            placeholder="https://github.com/organization/repository"
            value={githubUrl}
            onChange={(e) => onChange(e.target.value)}
            disabled={analyzing}
          />
        </div>
        <button type="submit" className="btn btn-primary btn-lg" disabled={analyzing}>
          Analyze Repository <ArrowRight size={17} />
        </button>
      </form>

      {error && <ErrorMessage message={error} className="hero-alert" />}
    </>
  );
}

export default GenerateForm;
