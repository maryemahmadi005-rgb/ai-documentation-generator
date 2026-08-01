import { useEffect, useMemo, useState } from "react";
import api from "../api/axios.js";
import Navbar from "../components/Navbar.jsx";
import Footer from "../components/Footer.jsx";
import SearchBar from "../components/SearchBar.jsx";
import StatusFilter from "../components/StatusFilter.jsx";
import HistoryTable from "../components/HistoryTable.jsx";
import Loader from "../components/Common/Loader.jsx";
import ErrorMessage from "../components/Common/ErrorMessage.jsx";
import EmptyState from "../components/Common/EmptyState.jsx";
import "./History.css";

const STATUS_GROUPS = {
  completed: ["completed", "success"],
  processing: ["running", "processing", "pending"],
  failed: ["failed", "error"],
};

function History() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [query, setQuery] = useState("");
  const [statusFilter, setStatusFilter] = useState("all");

  useEffect(() => {
    const fetchHistory = async () => {
      setLoading(true);
      setError("");
      try {
        const response = await api.get("/analyze/history");
        const data = Array.isArray(response.data)
          ? response.data
          : response.data.analyses || response.data.data || [];
        setItems(data);
      } catch (err) {
        setError("Unable to load your analysis history.");
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, []);

  const filteredItems = useMemo(() => {
    let result = items;

    if (statusFilter !== "all") {
      const accepted = STATUS_GROUPS[statusFilter] || [];
      result = result.filter((item) => accepted.includes((item.status || "").toLowerCase()));
    }

    if (query.trim()) {
      const q = query.trim().toLowerCase();
      result = result.filter((item) => {
        const name = (item.project_name || item.name || "").toLowerCase();
        const repo = (item.github_url || item.repo_url || item.git_info?.repo_url || "").toLowerCase();
        return name.includes(q) || repo.includes(q);
      });
    }

    return result;
  }, [items, query, statusFilter]);

  return (
    <div className="page-container">
      <Navbar />

      <div className="content-wrapper">
        <div className="history-page-header">
          <span className="eyebrow">History</span>
          <h1>Your previous analyses</h1>
          <p>Every repository you've analyzed, with its status and detected architecture.</p>

          {!loading && !error && items.length > 0 && (
            <div className="history-toolbar">
              <SearchBar value={query} onChange={setQuery} placeholder="Search by project or repository..." />
              <StatusFilter value={statusFilter} onChange={setStatusFilter} />
            </div>
          )}
        </div>

        {loading && <Loader message="Loading your history..." />}

        {!loading && error && <ErrorMessage message={error} />}

        {!loading && !error && items.length === 0 && (
          <EmptyState
            title="No analysis yet"
            message="Generate your first documentation from the Home page."
          />
        )}

        {!loading && !error && items.length > 0 && filteredItems.length === 0 && (
          <EmptyState title="No matches" message="Try a different search term or status filter." />
        )}

        {!loading && !error && filteredItems.length > 0 && <HistoryTable items={filteredItems} />}
      </div>

      <Footer />
    </div>
  );
}

export default History;
