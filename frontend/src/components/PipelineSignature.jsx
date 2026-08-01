import "./PipelineSignature.css";

/**
 * Illustration "signature" du produit : un flux animé reliant le dépôt
 * GitHub, le moteur d'analyse IA et la documentation générée. Ce même
 * motif (nœuds reliés par un trait animé) réapparaît dans le composant
 * PipelineProgress pendant l'analyse, pour une identité visuelle cohérente.
 */
function PipelineSignature() {
  return (
    <div className="pipeline-signature">
      <svg viewBox="0 0 420 300" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
          className="flow-path"
          d="M70 150 C 130 150, 130 70, 190 70 C 250 70, 250 150, 310 150 C 340 150, 350 150, 360 150"
          stroke="url(#flowGradient)"
          strokeWidth="2.5"
          strokeDasharray="6 8"
        />
        <path
          className="flow-path flow-path-alt"
          d="M70 150 C 130 150, 130 230, 190 230 C 250 230, 250 150, 310 150"
          stroke="url(#flowGradient)"
          strokeWidth="2.5"
          strokeDasharray="6 8"
        />

        <defs>
          <linearGradient id="flowGradient" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stopColor="#2e5eff" />
            <stop offset="100%" stopColor="#7c8fff" />
          </linearGradient>
        </defs>

        {/* Node: Repository */}
        <g className="signature-node" transform="translate(30, 122)">
          <rect width="80" height="56" rx="16" fill="#ffffff" stroke="#e6ebf5" strokeWidth="1.5" />
          <g transform="translate(28, 16)" stroke="#2e5eff" strokeWidth="1.6" fill="none" strokeLinecap="round" strokeLinejoin="round">
            <path d="M12 2 L2 7 L2 17 L12 22 L22 17 L22 7 Z" />
            <path d="M2 7 L12 12 L22 7" />
            <path d="M12 12 L12 22" />
          </g>
        </g>

        {/* Node: AI Engine */}
        <g className="signature-node signature-node-center" transform="translate(150, 40)">
          <rect width="80" height="60" rx="18" fill="#2e5eff" />
          <circle cx="40" cy="30" r="12" fill="none" stroke="#ffffff" strokeWidth="2" />
          <circle cx="40" cy="30" r="4" fill="#ffffff" />
        </g>

        {/* Node: Documentation */}
        <g className="signature-node" transform="translate(310, 122)">
          <rect width="80" height="56" rx="16" fill="#ffffff" stroke="#e6ebf5" strokeWidth="1.5" />
          <g transform="translate(26, 14)" stroke="#7c8fff" strokeWidth="1.6" fill="none" strokeLinecap="round" strokeLinejoin="round">
            <rect x="0" y="0" width="22" height="28" rx="2" />
            <path d="M5 7 H17 M5 13 H17 M5 19 H12" />
          </g>
        </g>

        {/* Node: Architecture (lower) */}
        <g className="signature-node" transform="translate(150, 202)">
          <rect width="80" height="56" rx="16" fill="#ffffff" stroke="#e6ebf5" strokeWidth="1.5" />
          <g transform="translate(24, 14)" stroke="#5b6472" strokeWidth="1.6" fill="none" strokeLinecap="round" strokeLinejoin="round">
            <rect x="0" y="16" width="10" height="12" />
            <rect x="14" y="8" width="10" height="20" />
            <rect x="28" y="0" width="10" height="28" />
          </g>
        </g>
      </svg>
    </div>
  );
}

export default PipelineSignature;
