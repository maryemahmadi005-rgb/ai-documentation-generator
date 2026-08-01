/**
 * Le backend n'expose pas (encore) de structure de fichiers ni
 * d'informations Git en JSON structuré : ces informations sont noyées en
 * texte libre dans le Markdown généré ("Structure du projet", "Informations
 * Git"). Ces fonctions les extraient en secours, pour éviter des sections
 * vides côté UI quand l'info existe déjà, juste sous forme de texte.
 */

/**
 * Extrait le bloc ASCII "Structure du projet" (arborescence en ├── / └──)
 * et le transforme en tableau de nœuds { name, type, children }.
 */
export function extractRepoTree(markdown) {
  if (!markdown) return null;

  const allLines = markdown.split("\n");
  const headingIndex = allLines.findIndex((l) => /structure du projet/i.test(l));
  if (headingIndex === -1) return null;

  const lines = [];
  for (let i = headingIndex + 1; i < allLines.length; i += 1) {
    const line = allLines[i];
    if (/[├└]──/.test(line)) {
      lines.push(line.replace(/```/g, "").trimEnd());
    } else if (lines.length > 0) {
      // On s'arrête à la première ligne qui casse le bloc d'arborescence.
      break;
    }
    // sinon : ligne vide / code fence avant le premier "├──", on continue.
  }

  if (lines.length === 0) return null;

  const root = [];
  const stack = [{ depth: -1, children: root }];

  lines.forEach((line) => {
    const match = line.match(/^((?:[│ ]{0,4})*)(├──|└──)\s*(.+)$/);
    if (!match) return;

    const prefix = match[1] || "";
    const name = match[3].trim();
    const depth = Math.floor(prefix.length / 4);
    const isFolder = name.endsWith("/");

    const node = {
      name: isFolder ? name.slice(0, -1) : name,
      type: isFolder ? "folder" : "file",
      children: isFolder ? [] : undefined,
    };

    while (stack.length && stack[stack.length - 1].depth >= depth) {
      stack.pop();
    }

    const parent = stack[stack.length - 1] || { children: root };
    parent.children.push(node);

    if (isFolder) {
      stack.push({ depth, children: node.children });
    }
  });

  return root.length > 0 ? root : null;
}

/**
 * Extrait le bloc "Informations Git" (Branche / Commit / Auteur / Nombre
 * de commits) sous forme d'objet { branch, commit, author, commitsCount }.
 */
export function extractGitInfo(markdown) {
  if (!markdown) return null;

  const allLines = markdown.split("\n");
  const headingIndex = allLines.findIndex((l) => /informations git/i.test(l));
  if (headingIndex === -1) return null;

  const block = [];
  for (let i = headingIndex + 1; i < allLines.length; i += 1) {
    const line = allLines[i];
    if (/^#/.test(line) || (block.length > 0 && line.trim() === "")) break;
    if (line.trim() !== "") block.push(line);
  }

  const text = block.join("\n");
  const get = (label) => {
    const m = text.match(new RegExp(`${label}\\s*:\\s*(.+)`, "i"));
    return m ? m[1].trim() : null;
  };

  const info = {
    branch: get("Branche"),
    commit: get("Commit"),
    author: get("Auteur"),
    commitsCount: get("Nombre de commits"),
  };

  return Object.values(info).some(Boolean) ? info : null;
}
