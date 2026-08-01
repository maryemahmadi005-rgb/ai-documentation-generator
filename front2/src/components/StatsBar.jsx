import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import "./StatsBar.css";

function AnimatedValue({ value, suffix = "", prefix = "" }) {
  const [displayed, setDisplayed] = useState(0);

  useEffect(() => {
    const numericValue = Number(value);
    if (!Number.isFinite(numericValue)) {
      setDisplayed(0);
      return;
    }

    const duration = 800;
    const startTime = performance.now();

    const tick = (time) => {
      const progress = Math.min(1, (time - startTime) / duration);
      const eased = 1 - Math.pow(1 - progress, 3);
      setDisplayed(Math.round(numericValue * eased));
      if (progress < 1) {
        window.requestAnimationFrame(tick);
      }
    };

    window.requestAnimationFrame(tick);
  }, [value]);

  return (
    <span>
      {prefix}
      {displayed}
      {suffix}
    </span>
  );
}

function StatsBar({ items }) {
  return (
    <motion.div
      className="stats-bar"
      initial={{ opacity: 0, y: 18 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.45, delay: 0.08 }}
    >
      <div className="stats-bar__header">
        <p className="eyebrow">Repository insights</p>
        <h2>Instantly surfaced metrics</h2>
      </div>

      <div className="stats-grid">
        {items.map((item) => (
          <div key={item.label} className="stat-card">
            <div className="stat-value">
              <AnimatedValue value={item.value} prefix={item.prefix} suffix={item.suffix} />
            </div>
            <div className="stat-label">{item.label}</div>
          </div>
        ))}
      </div>
    </motion.div>
  );
}

export default StatsBar;
