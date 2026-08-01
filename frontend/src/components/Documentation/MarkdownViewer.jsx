import "./MarkdownViewer.css";

/**
 * Convertisseur Markdown -> HTML volontairement minimal (pas de
 * dépendance externe) : titres, gras/italique, code inline et blocs,
 * listes, citations, liens et séparateurs. Couvre l'essentiel d'un
 * README généré automatiquement.
 */
function escapeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function renderInline(text) {
  let out = escapeHtml(text);
  out = out.replace(/`([^`]+)`/g, "<code>$1</code>");
  out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  out = out.replace(/(?<!\*)\*([^*]+)\*(?!\*)/g, "<em>$1</em>");
  out = out.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
  return out;
}

function markdownToHtml(markdown) {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const html = [];
  let inCodeBlock = false;
  let codeLines = [];
  let listBuffer = [];
  let listType = null;

  const flushList = () => {
    if (listBuffer.length) {
      const tag = listType === "ol" ? "ol" : "ul";
      html.push(`<${tag}>${listBuffer.map((li) => `<li>${renderInline(li)}</li>`).join("")}</${tag}>`);
      listBuffer = [];
      listType = null;
    }
  };

  lines.forEach((rawLine) => {
    const line = rawLine;

    if (line.trim().startsWith("```")) {
      if (inCodeBlock) {
        html.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
        codeLines = [];
        inCodeBlock = false;
      } else {
        flushList();
        inCodeBlock = true;
      }
      return;
    }

    if (inCodeBlock) {
      codeLines.push(line);
      return;
    }

    const heading = line.match(/^(#{1,6})\s+(.*)/);
    if (heading) {
      flushList();
      const level = heading[1].length;
      html.push(`<h${level}>${renderInline(heading[2])}</h${level}>`);
      return;
    }

    if (/^\s*---+\s*$/.test(line)) {
      flushList();
      html.push("<hr/>");
      return;
    }

    const quote = line.match(/^>\s?(.*)/);
    if (quote) {
      flushList();
      html.push(`<blockquote>${renderInline(quote[1])}</blockquote>`);
      return;
    }

    const ordered = line.match(/^\s*\d+\.\s+(.*)/);
    const unordered = line.match(/^\s*[-*]\s+(.*)/);
    if (ordered) {
      if (listType !== "ol") flushList();
      listType = "ol";
      listBuffer.push(ordered[1]);
      return;
    }
    if (unordered) {
      if (listType !== "ul") flushList();
      listType = "ul";
      listBuffer.push(unordered[1]);
      return;
    }

    flushList();

    if (line.trim() === "") {
      return;
    }

    html.push(`<p>${renderInline(line)}</p>`);
  });

  flushList();
  if (inCodeBlock && codeLines.length) {
    html.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
  }

  return html.join("\n");
}

function MarkdownViewer({ content }) {
  if (!content) {
    return <p className="markdown-empty">Aucun contenu Markdown disponible.</p>;
  }

  return (
    <div
      className="markdown-viewer"
      dangerouslySetInnerHTML={{ __html: markdownToHtml(content) }}
    />
  );
}

export default MarkdownViewer;
