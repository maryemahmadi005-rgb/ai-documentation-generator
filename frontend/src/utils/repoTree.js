/**
 * Le backend (GitAnalyzer) renvoie l'arborescence sous la forme :
 *   { files: ["a.py", "b.py"], dirs: { "src": { files: [...], dirs: {...} } } }
 * (voir services/analyzers/git_analyzer.py et le commentaire du modèle
 * Analysis.repository_tree). RepoTree.jsx attend, lui, un tableau de
 * nœuds { name, type: 'file' | 'folder', children? }. Cette fonction
 * convertit le premier format vers le second.
 */
export function convertBackendTree(structure) {
  if (!structure || typeof structure !== "object") return null;

  const files = Array.isArray(structure.files) ? structure.files : [];
  const dirs = structure.dirs && typeof structure.dirs === "object" ? structure.dirs : {};

  const fileNodes = [...files].sort().map((name) => ({ name, type: "file" }));

  const folderNodes = Object.keys(dirs)
    .sort()
    .map((name) => ({
      name,
      type: "folder",
      children: convertBackendTree(dirs[name]) || [],
    }));

  const nodes = [...folderNodes, ...fileNodes];
  return nodes.length > 0 ? nodes : null;
}
