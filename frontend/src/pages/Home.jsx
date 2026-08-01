import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios.js";
import Navbar from "../components/Navbar.jsx";
import Footer from "../components/Footer.jsx";
import Hero from "../components/Hero.jsx";
import GenerateForm from "../components/GenerateForm.jsx";
import HowItWorks from "../components/HowItWorks.jsx";
import FeatureCards from "../components/FeatureCards.jsx";
import "./Home.css";

/**
 * Déduit un nom de projet lisible à partir de l'URL GitHub
 * (ex: "https://github.com/owner/my-repo" -> "my-repo").
 */
function extractProjectName(url) {
  const cleaned = url.trim().replace(/\/+$/, "").replace(/\.git$/, "");
  const parts = cleaned.split("/");
  return parts[parts.length - 1] || cleaned;
}

function Home() {
  const navigate = useNavigate();
  const [githubUrl, setGithubUrl] = useState("");
  const [analyzing, setAnalyzing] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async (e) => {
    e.preventDefault();
    setError("");

    if (!githubUrl.trim()) {
      setError("Please enter a valid GitHub repository URL.");
      return;
    }

    const storedUser = localStorage.getItem("user");
    const user = storedUser ? JSON.parse(storedUser) : null;
    const userId = user?.id ?? user?.user_id;

    if (!userId) {
      setError("Your session seems invalid. Please log in again.");
      return;
    }

    setAnalyzing(true);
    try {
      // L'API exige user_id, name ET github_url sur /projects. On crée donc
      // d'abord le projet pour récupérer son id, avant d'appeler /analyze.
      const projectResponse = await api.post("/projects", {
        user_id: userId,
        name: extractProjectName(githubUrl),
        github_url: githubUrl.trim(),
      });

      const projectData = projectResponse.data.project || projectResponse.data;
      const projectId = projectData.id ?? projectData.project_id;

      if (!projectId) {
        throw new Error("no_project_id");
      }

      const response = await api.post("/analyze", {
        project_id: projectId,
        github_url: githubUrl.trim(),
      });

      console.log("Analyze response data:", response?.data);

      const payload = response?.data ?? {};
      const analysisPayload = payload.analysis ?? payload;
      const analysisId =
        analysisPayload?.id ??
        payload?.analysis_id ??
        payload?.id ??
        projectId;

      const analysis = {
        ...analysisPayload,
        id: analysisId,
        analysis_id: analysisId,
        ...payload,
        project_name: extractProjectName(githubUrl),
        github_url: githubUrl.trim(),
      };

      console.log("Normalized analysis payload:", analysis);

      navigate(`/analysis/${analysisId}`, { state: { analysis } });
    } catch (err) {
      console.error("Analyze request failed:", err);
      const message =
        err.response?.data?.message ||
        err.response?.data?.error ||
        err.response?.data?.detail ||
        err.message ||
        "Something went wrong while analyzing this repository.";
      setError(message);
      setAnalyzing(false);
    } finally {
      setAnalyzing(false);
    }
  };

  return (
    <div className="page-container">
      <Navbar />

      <div className="content-wrapper hero-wrapper">
        <Hero>
          <GenerateForm
            githubUrl={githubUrl}
            onChange={setGithubUrl}
            onSubmit={handleGenerate}
            analyzing={analyzing}
            error={error}
          />
        </Hero>

        <HowItWorks />
        <FeatureCards />
      </div>

      <Footer />
    </div>
  );
}

export default Home;
