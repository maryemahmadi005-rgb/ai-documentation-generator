/**
 * repositoryTree.js
 * ------------------
 *
 * Le backend renvoie `repository_tree` sous forme d'arbre imbriqué :
 *
 *   { files: ["a.py", "b.py"], dirs: { "services": { files: [...], dirs: {...} } } }
 *
 * alors que <RepoTree /> attend un tableau de nœuds :
 *
 *   [{ name, type: "file" | "folder", path, children? }]
 *
 * Ces utilitaires font la conversion, et enrichissent chaque fichier
 * avec les infos venues de `files` (summary, line_count, classes,
 * functions) pour que <FileViewer /> ait quelque chose à afficher.
 */

/**
 * Indexe la liste plate `files` (renvoyée par l'API) par chemin, pour
 * un accès O(1) pendant la conversion de l'arbre.
 *
 * @param {Array<{path: string, summary?: string, line_count?: number,
 *   classes?: string[], functions?: string[]}>} files
 */
export function indexFilesByPath(files) {
  const map = {};

  (files || []).forEach((file) => {
    if (file && file.path) {
      map[file.path] = file;
    }
  });

  return map;
}

/**
 * Convertit l'arbre imbriqué du backend (`repository_tree`) en tableau
 * de nœuds compatible avec <RepoTree />. Les fichiers sont enrichis
 * avec les données de `filesByPath` (summary, line_count, classes,
 * functions) quand elles existent.
 *
 * @param {{files?: string[], dirs?: Record<string, object>}} tree
 * @param {Record<string, object>} filesByPath — voir indexFilesByPath()
 * @param {string} basePath — usage interne (récursion)
 */
export function repositoryTreeToNodes(tree, filesByPath = {}, basePath = "") {
  if (!tree) {
    return [];
  }

  /*
   New backend format:
   [
     {
       name: "app",
       type: "folder",
       children: [...]
     }
   ]
  */
  if (Array.isArray(tree)) {
    return tree.map((node) => {
      const path = basePath
      ? `${basePath}/${node.name}`
      : node.name;

    const isFile = node.type === "file";

    return {
      name: node.name,
      type: isFile
        ? "file"
        : node.type === "directory"
          ? "folder"
          : "folder",
      path,

      ...(isFile
        ? {
            summary: filesByPath[path]?.summary,
            line_count: filesByPath[path]?.line_count,
            classes: filesByPath[path]?.classes,
            functions: filesByPath[path]?.functions,
          }
        : {
            children: repositoryTreeToNodes(
              node.children || [],
              filesByPath,
              path
            ),
          }),
    };
  });
}


  /*
   Old backend format:
   {
     files: [],
     dirs: {}
   }
  */
  if (typeof tree === "object") {

    const folderNodes = Object.entries(tree.dirs || {})
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([folderName, child]) => {

        const path = basePath
          ? `${basePath}/${folderName}`
          : folderName;

        return {
          name: folderName,
          type: "folder",
          path,
          children: repositoryTreeToNodes(
            child,
            filesByPath,
            path
          ),
        };
      });


    const fileNodes = (tree.files || [])
      .sort()
      .map((fileName) => {

        const path = basePath
          ? `${basePath}/${fileName}`
          : fileName;

        const info = filesByPath[path];

        return {
          name: fileName,
          type: "file",
          path,
          summary: info?.summary,
          line_count: info?.line_count,
          classes: info?.classes,
          functions: info?.functions,
        };
      });


    return [
      ...folderNodes,
      ...fileNodes
    ];
  }


  return [];
}