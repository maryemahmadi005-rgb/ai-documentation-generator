import "./StatusFilter.css";

const OPTIONS = [
  { value: "all", label: "All statuses" },
  { value: "completed", label: "Completed" },
  { value: "processing", label: "Processing" },
  { value: "failed", label: "Failed" },
];

/**
 * Simple filtre par statut (Completed / Processing / Failed) pour
 * la page History.
 */
function StatusFilter({ value, onChange }) {
  return (
    <select className="status-filter form-control" value={value} onChange={(e) => onChange(e.target.value)}>
      {OPTIONS.map((option) => (
        <option key={option.value} value={option.value}>
          {option.label}
        </option>
      ))}
    </select>
  );
}

export default StatusFilter;
