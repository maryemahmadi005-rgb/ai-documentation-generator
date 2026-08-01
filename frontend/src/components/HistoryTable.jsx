import { useNavigate } from "react-router-dom";
import { CheckCircle2, Loader2, XCircle, Layers, ArrowUpRight } from "lucide-react";
import "./HistoryTable.css";

const STATUS_CONFIG = {
  completed: { label: "Completed", icon: CheckCircle2, className: "badge-success" },
  success: { label: "Completed", icon: CheckCircle2, className: "badge-success" },
  running: { label: "Processing", icon: Loader2, className: "badge-warning", spin: true },
  processing: { label: "Processing", icon: Loader2, className: "badge-warning", spin: true },
  pending: { label: "Processing", icon: Loader2, className: "badge-warning", spin: true },
  failed: { label: "Failed", icon: XCircle, className: "badge-error" },
  error: { label: "Failed", icon: XCircle, className: "badge-error" },
};

const formatDate = (value) => {
  if (!value) return "-";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleDateString("en-US", { day: "2-digit", month: "short", year: "numeric" });
};

/**
 * Tableau d'historique des analyses : Project name / Date / Status /
 * Architecture / Actions, avec badges de statut et navigation vers
 * la page de détail.
 */
function HistoryTable({ items }) {
  const navigate = useNavigate();

  return (
    <div className="card history-table-card">
      <div className="history-table-wrap">
        <table className="history-table">
          <thead>
            <tr>
              <th>Project</th>
              <th>Date</th>
              <th>Status</th>
              <th>Architecture</th>
              <th className="th-actions">Actions</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item, index) => {
              const statusKey = (item.status || "").toLowerCase();
              const statusInfo = STATUS_CONFIG[statusKey] || {
                label: item.status || "Unknown",
                icon: Layers,
                className: "badge-neutral",
              };
              const StatusIcon = statusInfo.icon;
              const projectName = item.project_name || item.name || "Untitled project";
              const architecture = item.detected_architecture || "-";

              return (
                <tr key={item.id || index}>
                  <td>
                    <span className="cell-project">{projectName}</span>
                  </td>
                  <td className="cell-muted">{formatDate(item.created_at || item.date)}</td>
                  <td>
                    <span className={`badge ${statusInfo.className}`}>
                      <StatusIcon size={12} className={statusInfo.spin ? "spin-icon" : ""} />
                      {statusInfo.label}
                    </span>
                  </td>
                  <td className="cell-muted">{architecture}</td>
                  <td className="th-actions">
                    <button
                      type="button"
                      className="btn btn-secondary btn-sm"
                      onClick={() => navigate(`/analysis/${item.id}`, { state: { analysis: item } })}
                    >
                      View Details <ArrowUpRight size={14} />
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default HistoryTable;
