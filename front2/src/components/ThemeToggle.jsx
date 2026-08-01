import { useEffect, useState } from "react";
import { Sun, Moon } from "lucide-react";
import "./ThemeToggle.css";

const getInitialTheme = () => {
  const stored = localStorage.getItem("theme");
  if (stored === "dark" || stored === "light") return stored;
  // DocGen AI utilise un thème clair nude/terracotta par défaut.
  return "light";
};

/**
 * Bascule entre thème clair nude/terracotta (par défaut) et thème sombre
 * espresso. Le thème est appliqué via l'attribut data-theme sur <html>
 * (voir les overrides dans global.css) et persisté dans localStorage.
 */
function ThemeToggle() {
  const [theme, setTheme] = useState(getInitialTheme);

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
  }, [theme]);

  const toggle = () => setTheme((t) => (t === "dark" ? "light" : "dark"));

  return (
    <button
      type="button"
      className="theme-toggle btn-icon"
      onClick={toggle}
      aria-label={theme === "dark" ? "Switch to light mode" : "Switch to dark mode"}
      title={theme === "dark" ? "Switch to light mode" : "Switch to dark mode"}
    >
      {theme === "dark" ? <Sun size={16} /> : <Moon size={16} />}
    </button>
  );
}

export default ThemeToggle;
