import { Github } from "lucide-react";
import "./ProjectInfo.css";

/**
 * Bandeau de titre en haut de la page d'analyse : nom du projet,
 * URL du dépôt et statut. Les statistiques détaillées vivent dans
 * les StatCard juste en dessous.
 */
function ProjectInfo({ projectName, repoUrl, status }) {
  const badgeClass = () => {
    const s = (status || "").toLowerCase();
    if (s === "success" || s === "completed" || s === "terminé") return "badge-success";
    if (s === "failed" || s === "error" || s === "échec") return "badge-error";
    if (s === "pending" || s === "en cours") return "badge-warning";
    return "badge-neutral";
  };

  return (
    <div className="project-info">
      <span className="eyebrow">Analysis result</span>
      <div className="project-info-title">
        <h1>{projectName}</h1>
        {status && <span className={`badge ${badgeClass()}`}>{status}</span>}
      </div>
      <p className="project-info-url">
        <Github size={13} /> {repoUrl}
      </p>
    </div>
  );
}

export default ProjectInfo;
