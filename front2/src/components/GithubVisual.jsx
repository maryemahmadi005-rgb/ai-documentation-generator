import { Github } from "lucide-react";
import "./GithubVisual.css";

function GithubVisual() {
  return (
    <div className="github-visual">

      <div className="code-window">

        <div className="code-window-bar">
          <span className="dot dot-red" />
          <span className="dot dot-yellow" />
          <span className="dot dot-green" />

          <span className="code-window-path">
            <Github size={13} />
            GitHub Repository
          </span>
        </div>


        <div className="code-window-body">

          <div className="scan-line" />

          <div className="code-line muted">
            // cloning repository...
          </div>

          <div className="code-line muted">
            // analyzing source code...
          </div>

          <div className="code-line muted">
            // generating documentation...
          </div>

        </div>

      </div>

    </div>
  );
}

export default GithubVisual;