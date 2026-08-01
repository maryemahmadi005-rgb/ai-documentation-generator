import "./StatCard.css";

/**
 * Petite carte statistique utilisée dans la section Overview de la
 * page d'analyse (Project Name, Architecture, Confidence, ...).
 */
function StatCard({ label, value, tone = "neutral", icon: Icon }) {
  return (
    <div className={`stat-card tone-${tone}`}>
      <div className="stat-card-top">
        {Icon && (
          <span className="stat-icon">
            <Icon size={15} />
          </span>
        )}
        <span className="stat-label">{label}</span>
      </div>
      <span className="stat-value" title={typeof value === "string" ? value : undefined}>
        {value ?? "-"}
      </span>
    </div>
  );
}

export default StatCard;
