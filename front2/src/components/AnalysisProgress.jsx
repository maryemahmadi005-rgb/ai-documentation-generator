import { useEffect, useMemo, useState } from "react";
import { motion } from "framer-motion";
import { CheckCircle2, LoaderCircle, Circle } from "lucide-react";
import "./AnalysisProgress.css";

const STEP_DEFINITIONS = [
  { label: "Cloning repository", detail: "Pulling the repository snapshot" },
  { label: "Analyzing project structure", detail: "Scanning folders and files" },
  { label: "Running AI analysis", detail: "Understanding the codebase" },
  { label: "Detecting architecture", detail: "Identifying the system pattern" },
  { label: "Generating documentation", detail: "Writing the technical narrative" },
  { label: "Building site", detail: "Packaging the docs for delivery" },
];

function AnalysisProgress({ active = false }) {
  const [stepIndex, setStepIndex] = useState(0);
  const [elapsed, setElapsed] = useState(0);

  useEffect(() => {
    if (!active) {
      setStepIndex(0);
      setElapsed(0);
      return undefined;
    }

    const stepTimer = window.setInterval(() => {
      setStepIndex((previous) => (previous < STEP_DEFINITIONS.length - 1 ? previous + 1 : previous));
    }, 1400);

    const clockTimer = window.setInterval(() => {
      setElapsed((previous) => previous + 1);
    }, 1000);

    return () => {
      window.clearInterval(stepTimer);
      window.clearInterval(clockTimer);
    };
  }, [active]);

  const progressPercent = useMemo(() => {
    if (!active) return 16;
    return Math.min(92, Math.round(((stepIndex + (stepIndex < STEP_DEFINITIONS.length - 1 ? 0.2 : 0.8)) / STEP_DEFINITIONS.length) * 100));
  }, [active, stepIndex]);

  const formatElapsed = (seconds) => {
    const minutes = String(Math.floor(seconds / 60)).padStart(2, "0");
    const secs = String(Math.floor(seconds % 60)).padStart(2, "0");
    return `${minutes}:${secs}`;
  };

  return (
    <motion.div
      className="analysis-progress-card"
      initial={{ opacity: 0, y: 18 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.45 }}
    >
      <div className="analysis-progress-card__header">
        <div>
          <p className="eyebrow">Live analysis</p>
          <h2>Current analysis status</h2>
        </div>
        <div className="analysis-timer">{formatElapsed(elapsed)}</div>
      </div>

      <div className="analysis-progress-track">
        <div className="analysis-progress-fill" style={{ width: `${progressPercent}%` }} />
      </div>

      <div className="analysis-progress-meta">
        <span>{progressPercent}% complete</span>
        <span>{active ? "Processing in real time" : "Ready to start"}</span>
      </div>

      <ul className="analysis-step-list">
        {STEP_DEFINITIONS.map((step, index) => {
          const state = index < stepIndex ? "done" : index === stepIndex && active ? "active" : "pending";
          return (
            <li key={step.label} className={`analysis-step ${state}`}>
              <span className="analysis-step-marker">
                {state === "done" ? <CheckCircle2 size={16} /> : state === "active" ? <LoaderCircle size={16} className="spin" /> : <Circle size={14} />}
              </span>
              <span>
                <strong>{step.label}</strong>
                <small>{step.detail}</small>
              </span>
            </li>
          );
        })}
      </ul>
    </motion.div>
  );
}

export default AnalysisProgress;
