import { Eye, Download, ExternalLink } from "lucide-react";
import "./DownloadButtons.css";

const downloadFile = (filename, content) => {
  if (!content) return;
  const blob = new Blob([content], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
};

const scrollToDocumentation = () => {
  document.getElementById("documentation")?.scrollIntoView({ behavior: "smooth", block: "start" });
};

/**
 * Boutons View Documentation / Download README / Open MkDocs Website,
 * utilisés dans la section Download de la page d'analyse.
 */
function DownloadButtons({ projectName, readmeContent, documentationContent, documentationUrl }) {
  return (
    <div className="download-actions">
      <button className="btn btn-secondary" onClick={scrollToDocumentation}>
        <Eye size={16} /> View Documentation
      </button>
      <button
        className="btn btn-secondary"
        onClick={() => downloadFile(`README_${projectName}.md`, readmeContent)}
        disabled={!readmeContent}
      >
        <Download size={16} /> Download README
      </button>
      <button
        className="btn btn-primary"
        onClick={() => documentationUrl && window.open(documentationUrl, "_blank", "noopener,noreferrer")}
        disabled={!documentationUrl}
      >
        <ExternalLink size={16} /> Open MkDocs Website
      </button>
    </div>
  );
}

export default DownloadButtons;
