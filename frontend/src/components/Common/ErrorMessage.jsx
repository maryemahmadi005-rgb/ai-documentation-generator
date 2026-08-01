/**
 * Bloc d'erreur réutilisable. Simple wrapper autour de la classe .alert-error
 * du design system, pour éviter de répéter le markup partout.
 */
function ErrorMessage({ message, className = "" }) {
  if (!message) return null;
  return <div className={`alert alert-error ${className}`.trim()}>{message}</div>;
}

export default ErrorMessage;
