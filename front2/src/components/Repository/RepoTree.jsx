import { useMemo, useState } from "react";
import { Search, X } from "lucide-react";
import EmptyState from "../Common/EmptyState.jsx";
import "./RepoTree.css";

const FolderIcon = () => (
  <svg width="15" height="15" viewBox="0 0 20 20" fill="none">
    <path
      d="M2.5 5.5A1.5 1.5 0 0 1 4 4h3.6l1.4 1.8h7A1.5 1.5 0 0 1 17.5 7.3v7.2A1.5 1.5 0 0 1 16 16H4a1.5 1.5 0 0 1-1.5-1.5V5.5Z"
      stroke="#5b7dff"
      strokeWidth="1.4"
      strokeLinejoin="round"
    />
  </svg>
);

const FileIcon = () => (
  <svg width="14" height="14" viewBox="0 0 20 20" fill="none">
    <path
      d="M5 2.5h6.5L15.5 6.5V17a.5.5 0 0 1-.5.5H5A.5.5 0 0 1 4.5 17V3a.5.5 0 0 1 .5-.5Z"
      stroke="#9aa4b5"
      strokeWidth="1.4"
      strokeLinejoin="round"
    />
    <path d="M11.5 2.5V6.5H15.5" stroke="#9aa4b5" strokeWidth="1.4" strokeLinejoin="round" />
  </svg>
);

const Chevron = ({ open }) => (
  <svg
    width="11"
    height="11"
    viewBox="0 0 12 12"
    fill="none"
    className={`chevron ${open ? "open" : ""}`}
  >
    <path d="M4 2.5L8 6L4 9.5" stroke="#5b6472" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

/**
 * Filtre récursivement l'arbre par nom de fichier/dossier
 * (insensible à la casse). Un dossier est conservé si son nom
 * correspond OU si au moins un de ses descendants correspond.
 */
function filterTree(nodes, term) {
  if (!term) return nodes;
  const lowerTerm = term.toLowerCase();

  const walk = (list) =>
    list.reduce((acc, node) => {
      const isFolder = node.type === "folder" || Array.isArray(node.children);
      const nameMatches = node.name?.toLowerCase().includes(lowerTerm);

      if (isFolder) {
        const filteredChildren = walk(Array.isArray(node.children) ? node.children : []);
        if (nameMatches || filteredChildren.length > 0) {
          acc.push({ ...node, children: filteredChildren });
        }
      } else if (nameMatches) {
        acc.push(node);
      }

      return acc;
    }, []);

  return walk(nodes);
}

/**
 * Nœud récursif de l'arbre (dossier repliable ou fichier).
 * Les fichiers sont cliquables et déclenchent onFileSelect (voir FileViewer).
 * `forceOpen` : quand une recherche est active, les dossiers restent
 * dépliés pour que les résultats soient visibles sans clic manuel.
 */
function TreeNode({ node, depth, onFileSelect, selectedPath, forceOpen }) {
  const isFolder = node.type === "folder" || Array.isArray(node.children);
  const [open, setOpen] = useState(depth < 1);
  const path = node.path || node.name;
  const isOpen = forceOpen || open;

  if (!isFolder) {
    return (
      <button
        type="button"
        className={`tree-row tree-row-file ${selectedPath === path ? "selected" : ""}`}
        style={{ paddingLeft: depth * 18 + 26 }}
        onClick={() => onFileSelect && onFileSelect(node)}
      >
        <FileIcon />
        <span>{node.name}</span>
      </button>
    );
  }

  return (
    <div className="tree-branch">
      <button
        type="button"
        className="tree-row tree-row-folder"
        style={{ paddingLeft: depth * 18 }}
        onClick={() => setOpen((o) => !o)}
      >
        <Chevron open={isOpen} />
        <FolderIcon />
        <span>{node.name}</span>
      </button>

      {isOpen && (Array.isArray(node.children) ? node.children : []).map((child, index) => (
        <TreeNode
          key={child.name + index}
          node={child}
          depth={depth + 1}
          onFileSelect={onFileSelect}
          selectedPath={selectedPath}
          forceOpen={forceOpen}
        />
      ))}
    </div>
  );
}

/**
 * Affiche la structure du dépôt sous forme d'arborescence repliable,
 * avec une recherche par nom de fichier/dossier.
 * `nodes` doit être un tableau de { name, type: 'file' | 'folder', children? }.
 * `onFileSelect(node)` est appelé au clic sur un fichier (voir FileViewer).
 */
function RepoTree({ nodes, onFileSelect, selectedPath }) {
  const [search, setSearch] = useState("");

  const normalizedNodes = Array.isArray(nodes)
    ? nodes
    : nodes && typeof nodes === "object"
    ? [nodes]
    : [];

  const filteredNodes = useMemo(
    () => filterTree(normalizedNodes, search.trim()),
    [normalizedNodes, search]
  );

  if (normalizedNodes.length === 0) {
    return (
      <EmptyState
        title="No file structure available"
        message="The repository tree wasn't returned for this analysis."
      />
    );
  }

  return (
    <div className="repo-tree-wrapper">
      <div className="repo-tree-search">
        <Search size={14} />
        <input
          type="text"
          placeholder="Search files or folders..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        {search && (
          <button
            type="button"
            className="repo-tree-search-clear"
            onClick={() => setSearch("")}
            aria-label="Clear search"
          >
            <X size={13} />
          </button>
        )}
      </div>

      <div className="repo-tree">
        {filteredNodes.length === 0 ? (
          <p className="repo-tree-no-results">No file matches "{search}".</p>
        ) : (
          filteredNodes.map((node, index) => (
            <TreeNode
              key={node.name + index}
              node={node}
              depth={0}
              onFileSelect={onFileSelect}
              selectedPath={selectedPath}
              forceOpen={Boolean(search.trim())}
            />
          ))
        )}
      </div>
    </div>
  );
}

export default RepoTree;
