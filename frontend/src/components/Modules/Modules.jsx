import { useMemo, useState } from "react";
import { ChevronDown, Folder } from "lucide-react";
import EmptyState from "../Common/EmptyState.jsx";
import "./Modules.css";

/**
 * Regroupe `analysis.files` (liste à plat renvoyée par l'API) par
 * dossier racine, côté client — aucun nouveau champ backend requis,
 * aucune logique métier modifiée. Donne une vue "modules" sans
 * attendre un éventuel futur champ dédié côté API.
 */
function groupFilesByModule(files) {
  const groups = new Map();

  (files || []).forEach((file) => {
    const path = file.path || "";
    const segments = path.split("/");
    const moduleName = segments.length > 1 ? segments[0] : "root";

    if (!groups.has(moduleName)) {
      groups.set(moduleName, []);
    }
    groups.get(moduleName).push(file);
  });

  return Array.from(groups.entries())
    .map(([name, moduleFiles]) => ({
      name,
      files: moduleFiles,
      classCount: moduleFiles.reduce((sum, f) => sum + (f.classes?.length || 0), 0),
      functionCount: moduleFiles.reduce((sum, f) => sum + (f.functions?.length || 0), 0),
    }))
    .sort((a, b) => b.files.length - a.files.length);
}

function ModuleGroup({ module }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="module-group">
      <button type="button" className="module-group-header" onClick={() => setOpen((o) => !o)}>
        <Folder size={15} />
        <span className="module-group-name">{module.name}</span>
        <span className="module-group-count">{module.files.length} file{module.files.length > 1 ? "s" : ""}</span>
        <ChevronDown size={14} className={`module-group-chevron ${open ? "open" : ""}`} />
      </button>

      {open && (
        <ul className="module-group-files">
          {module.files.map((file) => (
            <li key={file.path} className="module-file-row">
              <span className="module-file-name">{file.path.split("/").pop()}</span>
              {file.summary && <span className="module-file-summary">{file.summary}</span>}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

function Modules({ files }) {
  const modules = useMemo(() => groupFilesByModule(files), [files]);

  if (modules.length === 0) {
    return (
      <EmptyState
        title="No modules detected"
        message="Module grouping isn't available for this analysis."
      />
    );
  }

  return (
    <div className="modules-list">
      {modules.map((module) => (
        <ModuleGroup key={module.name} module={module} />
      ))}
    </div>
  );
}

export default Modules;
