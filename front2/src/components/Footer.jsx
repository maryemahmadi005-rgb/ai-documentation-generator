import "./Footer.css";

/**
 * Pied de page simple, affiché en bas des pages authentifiées.
 */
function Footer() {
  return (
    <footer className="app-footer">
      <div className="app-footer-inner">
        <span className="brand-dot" />
        <span>DocGen AI — AI-powered technical documentation</span>
        <span className="footer-year">© {new Date().getFullYear()}</span>
      </div>
    </footer>
  );
}

export default Footer;
