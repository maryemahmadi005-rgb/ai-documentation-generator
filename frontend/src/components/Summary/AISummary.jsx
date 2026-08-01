import EmptyState from "../Common/EmptyState.jsx";
import MarkdownViewer from "../Documentation/MarkdownViewer.jsx";
import "./AISummary.css";

/**
 * Affiche le résumé généré par le modèle IA (`analysis.ai_summary`).
 *
 * Ce champ est désormais une analyse globale structurée en Markdown
 * (## Objectif du projet, ## Technologies utilisées, ## Architecture,
 * ## Modules principaux, ## Flux de données, ## Recommandations),
 * générée côté backend — plus une simple concaténation de résumés
 * fichier par fichier. On délègue donc le rendu à <MarkdownViewer />
 * (déjà utilisé pour le README) plutôt qu'un <p> brut, sinon les "##"
 * s'affichent tels quels au lieu d'être des titres.
 */
function AISummary({ summary }) {
  if (!summary) {
    return (
      <EmptyState title="No summary yet" message="The AI summary for this project isn't available." />
    );
  }

  return (
    <div className="ai-summary-text">
      <MarkdownViewer content={summary} />
    </div>
  );
}

export default AISummary;
