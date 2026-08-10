import { BarChart3, FileCode2, FolderTree, Layers3, Sparkles } from "lucide-react";
import StatCard from "./Overview/StatCard.jsx";

function Statistics({ statistics }) {
  const normalized = statistics || {};

  const displayStats = [
    { label: "Files", value: normalized.total_files ?? normalized.totalFiles ?? normalized.files ?? "-", icon: FileCode2 },
    { label: "Lines", value: normalized.total_lines ?? normalized.totalLines ?? normalized.lines ?? "-", icon: Layers3 },
    { label: "Classes", value: normalized.classes ?? normalized.total_classes ?? "-", icon: FolderTree },
    { label: "Functions", value: normalized.functions ?? normalized.total_functions ?? "-", icon: Sparkles },
    { label: "Avg. complexity", value: normalized.complexity_score ?? normalized.average_complexity_score ?? normalized.averageComplexity ?? "-", icon: BarChart3 },
  ];

  return (
    <div className="stat-grid">
      {displayStats.map((stat) => (
        <StatCard key={stat.label} label={stat.label} value={stat.value} icon={stat.icon} />
      ))}
    </div>
  );
}

export default Statistics;
