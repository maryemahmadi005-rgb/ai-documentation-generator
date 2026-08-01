import "./EmptyState.css";

/**
 * État vide générique : icône discrète, message, et action optionnelle.
 * Utilisé quand l'historique, l'arborescence ou un contenu est absent.
 */
function EmptyState({ title = "Nothing here yet", message, action }) {
  return (
    <div className="empty-state">
      <div className="empty-state-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
          <path
            d="M4 7h16M4 12h10M4 17h7"
            stroke="currentColor"
            strokeWidth="1.6"
            strokeLinecap="round"
          />
        </svg>
      </div>
      <h4>{title}</h4>
      {message && <p>{message}</p>}
      {action && <div className="empty-state-action">{action}</div>}
    </div>
  );
}

export default EmptyState;
