import { useEffect, useRef, useState } from "react";
import "./MermaidDiagram.css";

let mermaidIdCounter = 0;

/**
 * Rend un diagramme Mermaid à partir du code fourni par le backend
 * (ex: analysis.architecture.diagram). Chargement dynamique de la
 * librairie "mermaid" pour ne pas alourdir le bundle si aucun diagramme
 * n'est présent. `title` permet de réutiliser ce composant pour
 * plusieurs types de diagrammes (Architecture, Data Flow, Dependency,
 * Repository Tree) si le backend venait à les renvoyer.
 */
function MermaidDiagram({ code, title = "Architecture diagram" }) {
  const containerRef = useRef(null);
  const [aerror, setError] = useState(false);

  useEffect(() => {
    if (!code) return;
    let cancelled = false;

    (async () => {
      try {
        const mermaidModule = await import("mermaid");
        const mermaid = mermaidModule.default;
        mermaid.initialize({ startOnLoad: false, theme: "neutral", securityLevel: "strict" });

        mermaidIdCounter += 1;
        const id = `mermaid-diagram-${mermaidIdCounter}`;
        const { svg } = await mermaid.render(id, code);

        if (!cancelled && containerRef.current) {
          containerRef.current.innerHTML = svg;
          setError(false);
        }
      } catch (err) {
        if (!cancelled) setError(true);
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [code]);

  if (!code) return null;

  return (
    <div className="mermaid-diagram-card card">
      <h3>{title}</h3>
      {error ? (
        <p className="mermaid-error">Le diagramme n'a pas pu être généré.</p>
      ) : (
        <div className="mermaid-container" ref={containerRef} />
      )}
    </div>
  );
}

export default MermaidDiagram;
