import { useEffect, useState } from "react";
import { useParams, useLocation } from "react-router-dom";
import { motion } from "framer-motion";
import { LayoutDashboard, Layers, FolderTree, FileText, BookMarked, Sparkles, Download, FolderGit2, Link2, Percent, FileCode2, Activity, Boxes, GitBranch, Network, Package } from "lucide-react";
import api from "../api/axios.js";
import Navbar from "../components/Navbar.jsx";
import Footer from "../components/Footer.jsx";
import Sidebar from "../components/Sidebar.jsx";
import SectionCard from "../components/SectionCard.jsx";
import ProjectInfo from "../components/Overview/ProjectInfo.jsx";
import StatCard from "../components/Overview/StatCard.jsx";
import ArchitectureCard from "../components/Architecture/ArchitectureCard.jsx";
import MermaidDiagram from "../components/Architecture/MermaidDiagram.jsx";
import Technologies from "../components/Overview/Technologies.jsx";
import GitInfo from "../components/Overview/GitInfo.jsx";
import Modules from "../components/Modules/Modules.jsx";
import RepoTree from "../components/Repository/RepoTree.jsx";
import FileViewer from "../components/Repository/FileViewer.jsx";
import MarkdownViewer from "../components/Documentation/MarkdownViewer.jsx";
import DownloadButtons from "../components/Documentation/DownloadButtons.jsx";
import AISummary from "../components/Summary/AISummary.jsx";
import Loader from "../components/Common/Loader.jsx";
import ErrorMessage from "../components/Common/ErrorMessage.jsx";
import "./AnalysisResult.css";
import { repositoryTreeToNodes, indexFilesByPath } from "../utils/repositoryTree";
function AnalysisResult() {
  const { id } = useParams();
  const location = useLocation();

  const [analysis, setAnalysis] = useState(location.state?.analysis || null);
  const [loading, setLoading] = useState(!location.state?.analysis);
  const [error, setError] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);

  useEffect(() => {
    const hasDocContent = (a) =>
      a && (a.document?.content || a.readme_content || a.readme || a.documentation_content);

    const hasProjectInfo = (a) => a && (a.project_name || a.name) && (a.github_url || a.repo_url);

    const loadMissingData = async () => {
      try {
        let base = location.state?.analysis || null;

        if (!base) {
          setLoading(true);
          const listResponse = await api.get("/analyze/history");
          console.log("Analysis history response data:", listResponse?.data);
          const list = Array.isArray(listResponse.data)
            ? listResponse.data
            : listResponse.data.analyses || listResponse.data.data || [];
          base =
            list.find((item) =>
              String(item?.id ?? item?.analysis_id ?? item?.analysis?.id) === String(id)
            ) || null;
        }

        // /analyze/history (Analysis.to_dict()) ne renvoie a priori que
        // project_id, pas le nom du projet ni son URL GitHub : on va les
        // chercher via GET /projects si nécessaire.
        if (base && !hasProjectInfo(base) && base.project_id) {
          try {
            const projectsResponse = await api.get("/projects");
            const projects = Array.isArray(projectsResponse.data)
              ? projectsResponse.data
              : projectsResponse.data.projects || [];
            const matchingProject = projects.find(
              (p) => String(p.id) === String(base.project_id)
            );
            if (matchingProject) {
              base = {
                ...base,
                project_name: matchingProject.name,
                github_url: matchingProject.github_url,
              };
            }
          } catch (projectErr) {
            // Impossible de résoudre le nom du projet : on garde les données de base.
          }
        }

        if (!hasDocContent(base)) {
          try {
            const docsResponse = await api.get("/documents", { params: { analysis_id: id } });
            const docData = docsResponse.data.document || docsResponse.data;
            base = { ...(base || {}), document: docData };
          } catch (docErr) {
            // Documentation non disponible séparément : on garde les données de base.
          }
        }

        if (!base) {
          setError("This analysis could not be found.");
        } else {
          setAnalysis(base);
        }
      } catch (err) {
        console.error("Unable to load this analysis:", err);
        setError(
          err.response?.data?.message ||
          err.response?.data?.error ||
          err.response?.data?.detail ||
          err.message ||
          "Unable to load this analysis."
        );
      } finally {
        setLoading(false);
      }
    };

    loadMissingData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [id]);

  if (loading) {
    return (
      <div className="page-container">
        <Navbar />
        <div className="content-wrapper">
          <Loader message="Loading analysis details..." />
        </div>
      </div>
    );
  }

  if (error || !analysis) {
    return (
      <div className="page-container">
        <Navbar />
        <div className="content-wrapper">
          <ErrorMessage message={error || "Analysis not found."} />
        </div>
      </div>
    );
  }

  const projectName = analysis.project_name || analysis.name || "Untitled project";
  const repoUrl = analysis.github_url || analysis.repo_url || analysis.git_info?.repo_url || "-";
  // detected_architecture est le nom de champ réel renvoyé par l'API
  // (GET /api/analyses/:id comme POST /api/analyze). Les autres clés
  // du fallback restent au cas où la forme de la réponse évolue.
  const architectureName =
    analysis.detected_architecture ||
    analysis.architecture?.type ||
    analysis.architecture ||
    "Not detected";
  const confidence =
    analysis.architecture_confidence ?? analysis.confidence ?? analysis.architecture?.confidence ?? null;
  const score = analysis.architecture_score ?? analysis.score ?? analysis.architecture?.score ?? null;
  // files_count est le vrai nom de champ (files_analyzed n'existe pas côté API).
  const filesAnalyzed = analysis.files_count ?? analysis.files_analyzed ?? analysis.stats?.files ?? null;
  const directories = analysis.directories_count ?? analysis.stats?.directories ?? null;
  const technologies = Array.isArray(analysis.technologies) ? analysis.technologies : [];
  const status = analysis.status || "unknown";

  const architectureExplanation = analysis.architecture?.explanation || analysis.architecture_explanation || "No explanation provided by the analysis.";
  const mermaidCode = analysis.architecture?.diagram || analysis.mermaid_diagram || null;

  // Diagrammes additionnels : aucun de ces champs n'est renvoyé par le
  // backend actuel (seul le diagramme d'architecture existe). Cette
  // liste ne fait qu'écouter plusieurs noms plausibles par type, pour
  // que la section s'active automatiquement le jour où le backend les
  // ajoute — sans qu'il faille retoucher le frontend.
  const extraDiagrams = [
    {
      key: "data-flow",
      title: "Data flow diagram",
      code: analysis.data_flow_diagram || analysis.diagrams?.data_flow || null,
    },
    {
      key: "dependency",
      title: "Dependency diagram",
      code: analysis.dependency_diagram || analysis.diagrams?.dependency || null,
    },
    {
      key: "repository",
      title: "Repository structure diagram",
      code: analysis.repository_diagram || analysis.diagrams?.repository || null,
    },
  ].filter((diagram) => Boolean(diagram.code));

  const filesByPath = indexFilesByPath(analysis.files);
  const repoNodes = repositoryTreeToNodes(
    analysis.repository_tree,
    filesByPath
  );
  // Un seul document est généré par analyse (analysis.document, format markdown) :
  // README et Documentation en sont donc la même source de contenu.
  const readmeContent = analysis.readme_content || "";
  const documentationContent =
    analysis.documentation_content || analysis.documentation?.content || "";
  // file_path est un chemin serveur (pas forcément une URL ouvrable directement
  // dans le navigateur) : à adapter si le backend expose une vraie route de
  // téléchargement/consultation statique pour ce fichier.
  const documentationUrl =
    analysis.documentation_url || analysis.documentation?.url || null;

  const aiSummary = analysis.ai_summary || analysis.summary || "";

  return (
    <div className="page-container">
      <Navbar />

      <div className="content-wrapper analysis-layout">
        <Sidebar />

        <main className="analysis-content">
          <ProjectInfo projectName={projectName} repoUrl={repoUrl} status={status} />

          <SectionCard id="overview" title="Overview" description="Key facts about this analysis at a glance." icon={LayoutDashboard}>
            <motion.div
              className="stat-grid"
              initial="hidden"
              animate="show"
              variants={{ show: { transition: { staggerChildren: 0.05 } } }}
            >
              {[
                { label: "Project Name", value: projectName, icon: FolderGit2 },
                 { label: "Confidence", value: confidence !== null ? `${confidence}%` : "-", icon: Percent },
                { label: "Files analyzed", value: filesAnalyzed ?? "-", icon: FileCode2 },
                { label: "Directories", value: directories ?? "-", icon: FolderTree },
                {
                  label: "Status",
                  value: status,
                  icon: Activity,
                  tone: status.toLowerCase() === "success" || status.toLowerCase() === "completed" ? "success" : "neutral",
                },
              ].map((stat) => (
                <motion.div
                  key={stat.label}
                  variants={{ hidden: { opacity: 0, y: 8 }, show: { opacity: 1, y: 0 } }}
                >
                  <StatCard label={stat.label} value={stat.value} icon={stat.icon} tone={stat.tone} />
                </motion.div>
              ))}
            </motion.div>
          </SectionCard>

          <SectionCard id="architecture" title="Architecture" description="Detected architecture pattern and reasoning." icon={Layers}>
            <ArchitectureCard
              name={architectureName}
              confidence={confidence}
              score={score}
              explanation={architectureExplanation}
              diagramCode={mermaidCode}
            />
          </SectionCard>

          {extraDiagrams.length > 0 && (
            <SectionCard id="diagrams" title="Diagrams" description="Additional diagrams generated for this analysis." icon={Network}>
              <div className="diagrams-grid">
                {extraDiagrams.map((diagram) => (
                  <MermaidDiagram key={diagram.key} code={diagram.code} title={diagram.title} />
                ))}
              </div>
            </SectionCard>
          )}

          <SectionCard id="repository" title="Repository" description="Project structure detected during analysis." icon={FolderTree}>
            <div className="repository-grid">
              <RepoTree nodes={repoNodes} onFileSelect={setSelectedFile} selectedPath={selectedFile?.path || selectedFile?.name} />
              {selectedFile && (
                <FileViewer file={selectedFile} />
                )}
            </div>
          </SectionCard>

          <SectionCard id="modules" title="Modules" description="Files grouped by top-level module." icon={Package}>
            <Modules files={analysis.files} />
          </SectionCard>

          <SectionCard id="technologies" title="Technologies" description="Languages and frameworks detected in the codebase." icon={Boxes}>
            <Technologies technologies={technologies} />
          </SectionCard>

          {analysis.git_info && Object.values(analysis.git_info).some(Boolean) && (
            <SectionCard 
            id="git-info" 
            title="Git Information" 
            description="Repository metadata at the time of analysis."
            icon={GitBranch}
            >
              <GitInfo metadata={analysis.git_info} />
              </SectionCard>
            )}

          <SectionCard id="documentation" title="Documentation" description="Generated technical documentation." icon={FileText}>
            <MarkdownViewer content={documentationContent} />
          </SectionCard>

          <SectionCard id="readme" title="README" description="Generated README.md file." icon={BookMarked}>
            <MarkdownViewer content={readmeContent} />
          </SectionCard>

          <SectionCard id="ai-summary" title="AI Summary" description="Natural-language summary produced by the AI model." icon={Sparkles}>
            <AISummary summary={aiSummary} />
          </SectionCard>

          <SectionCard id="download" title="Download" description="Export or open the generated documentation." icon={Download}>
            <DownloadButtons
              projectName={projectName}
              readmeContent={readmeContent}
              documentationContent={documentationContent}
              documentationUrl={documentationUrl}
            />
          </SectionCard>
        </main>
      </div>

      <Footer />
    </div>
  );
}

export default AnalysisResult;
