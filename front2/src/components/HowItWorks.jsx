import { motion } from "framer-motion";
import { GitBranch, Cpu, FileText, Share2 } from "lucide-react";
import "./HowItWorks.css";

const STEPS = [
  {
    icon: GitBranch,
    title: "Connect Repository",
    description: "Paste any public GitHub repository URL to get started — no setup required.",
  },
  {
    icon: Cpu,
    title: "AI Code Analysis",
    description: "DocGen AI clones the code, reads the project structure, and understands it with AI.",
  },
  {
    icon: FileText,
    title: "Documentation Generation",
    description: "Architecture is detected and a clear, structured technical documentation is written.",
  },
  {
    icon: Share2,
    title: "Export & Share",
    description: "Download the README, browse the full docs, or share the generated documentation.",
  },
];

/**
 * Section "How it works" : les 4 étapes du pipeline, présentées comme un
 * parcours numéroté et relié par une ligne horizontale.
 */
function HowItWorks() {
  return (
    <section className="how-it-works">
      <div className="section-heading">
        <span className="eyebrow">How it works</span>
        <h2>From repository to documentation in four steps</h2>
      </div>

      <div className="steps-row">
        {STEPS.map((step, index) => {
          const Icon = step.icon;
          return (
            <motion.div
              key={step.title}
              className="step-card"
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-60px" }}
              transition={{ duration: 0.5, delay: index * 0.1, ease: [0.22, 1, 0.36, 1] }}
            >
              <div className="step-number">{String(index + 1).padStart(2, "0")}</div>
              <div className="step-icon">
                <Icon size={20} />
              </div>
              <h3>{step.title}</h3>
              <p>{step.description}</p>
            </motion.div>
          );
        })}
      </div>
    </section>
  );
}

export default HowItWorks;
