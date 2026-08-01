import EmptyState from "../Common/EmptyState.jsx";
import "./FileViewer.css";

/**
 * Affiche les infos du fichier sélectionné dans RepoTree.
 *
 * Le backend ne renvoie jamais `content` (pas d'endpoint dédié au
 * contenu brut), mais `utils/repositoryTree.js` enrichit déjà chaque
 * fichier avec `summary`/`line_count`/`classes`/`functions` (issus de
 * `analysis.files`) — c'est ce qu'on affiche ici.
 */
function FileViewer({ file }) {
  if (!file) {
    return (
      <EmptyState
        title="No file selected"
        message="Select a file in the repository tree to preview its content."
      />
    );
  }

  const hasSummary = Boolean(file.summary);
  const hasClasses = Array.isArray(file.classes) && file.classes.length > 0;
  const hasFunctions = Array.isArray(file.functions) && file.functions.length > 0;

  return (
    <div className="file-viewer">
      <div className="file-viewer-header">
        <span className="file-viewer-name">{file.name}</span>
        {file.path && <span className="file-viewer-path">{file.path}</span>}
      </div>

      {file.content ? (
        <pre className="file-viewer-content">{file.content}</pre>
      ) : hasSummary ? (
        <div className="file-viewer-summary">
          <p className="file-viewer-summary-text">{file.summary}</p>

          {(hasClasses || hasFunctions) && (
            <div className="file-viewer-meta">
              {hasClasses && (
                <p className="file-viewer-meta-row">
                  <span className="file-viewer-meta-label">Classes</span>
                  {file.classes.join(", ")}
                </p>
              )}
              {hasFunctions && (
                <p className="file-viewer-meta-row">
                  <span className="file-viewer-meta-label">Functions</span>
                  {file.functions.join(", ")}
                </p>
              )}
            </div>
          )}

          {typeof file.line_count === "number" && (
            <p className="file-viewer-line-count">{file.line_count} lines</p>
          )}
        </div>
      ) : (
        <EmptyState
          title="Preview not available"
          message="This file's content wasn't included in the analysis response."
        />
      )}
    </div>
  );
}

export default FileViewer;
