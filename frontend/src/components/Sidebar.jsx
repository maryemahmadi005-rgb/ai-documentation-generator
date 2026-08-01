import { useEffect, useState } from "react";
import "./Sidebar.css";

const ITEMS = [
  { id: "overview", label: "Overview" },
  { id: "architecture", label: "Architecture" },
  { id: "diagrams", label: "Diagrams" },
  { id: "repository", label: "Repository" },
  { id: "modules", label: "Modules" },
  { id: "technologies", label: "Technologies" },
  { id: "git-info", label: "Git Information" },
  { id: "documentation", label: "Documentation" },
  { id: "readme", label: "README" },
  { id: "ai-summary", label: "AI Summary" },
  { id: "download", label: "Download" },
];

/**
 * Sidebar de navigation de la page d'analyse. Met en surbrillance la
 * section actuellement visible (IntersectionObserver) et scrolle en
 * douceur vers la section cliquée.
 */
function Sidebar() {
  const [activeId, setActiveId] = useState("overview");

  useEffect(() => {
    const sections = ITEMS.map((item) => document.getElementById(item.id)).filter(Boolean);

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        });
      },
      { rootMargin: "-30% 0px -55% 0px", threshold: 0 }
    );

    sections.forEach((section) => observer.observe(section));
    return () => observer.disconnect();
  }, []);

  const handleClick = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "start" });
      setActiveId(id);
    }
  };

  return (
    <aside className="analysis-sidebar">
      <nav>
        <ul>
          {ITEMS.map((item) => (
            <li key={item.id}>
              <button
                type="button"
                className={`sidebar-link ${activeId === item.id ? "active" : ""}`}
                onClick={() => handleClick(item.id)}
              >
                {item.label}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
}

export default Sidebar;
