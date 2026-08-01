import "./SearchBar.css";

/**
 * Barre de recherche contrôlée, utilisée sur la page History pour filtrer
 * les analyses par nom de projet ou URL de dépôt.
 */
function SearchBar({ value, onChange, placeholder = "Search..." }) {
  return (
    <div className="search-bar">
      <svg width="16" height="16" viewBox="0 0 20 20" fill="none" className="search-icon">
        <circle cx="9" cy="9" r="6.5" stroke="currentColor" strokeWidth="1.6" />
        <path d="M14 14L18 18" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
      </svg>
      <input
        type="text"
        className="search-input"
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
      {value && (
        <button type="button" className="search-clear" onClick={() => onChange("")} aria-label="Clear search">
          ×
        </button>
      )}
    </div>
  );
}

export default SearchBar;
