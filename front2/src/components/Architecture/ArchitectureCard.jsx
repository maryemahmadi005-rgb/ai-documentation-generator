import StatCard from "../Overview/StatCard.jsx";
import MermaidDiagram from "./MermaidDiagram.jsx";
import "./ArchitectureCard.css";

function ArchitectureCard({ name, confidence, diagramCode }) {
  return (
    <div className="architecture-card">
      <div className="stat-grid stat-grid-compact">
        <StatCard 
          label="Architecture" 
          value={name} 
          tone="brand" 
        />

        <StatCard 
          label="Confidence" 
          value={confidence !== null ? `${confidence}%` : "-"} 
        />
      </div>

      <MermaidDiagram code={diagramCode} />
    </div>
  );
}

export default ArchitectureCard;