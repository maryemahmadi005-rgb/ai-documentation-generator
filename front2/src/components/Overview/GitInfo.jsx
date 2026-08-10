import { GitBranch, GitCommit, User, Hash, Link as LinkIcon } from "lucide-react";
import EmptyState from "../Common/EmptyState.jsx";
import "./GitInfo.css";

/**
 * Carte "Git Information", à partir de `analysis.metadata`
 * (is_git_repo, branch, last_commit_hash,
 * last_commit_author, total_commits, remotes).
 */
function GitInfo({ metadata }) {
  if (
    !metadata ||
    (
      !metadata.branch &&
      !metadata.last_commit_hash &&
      !metadata.last_commit_author &&
      !metadata.total_commits &&
      !metadata.remotes?.length
    )
  ) {
    return (
      <EmptyState
        title="No Git information"
        message="This analysis doesn't include Git metadata."
      />
    );
  }

  const rows = [
    {
      icon: GitBranch,
      label: "Branch",
      value: metadata.branch,
    },
    {
      icon: Hash,
      label: "Commit",
      value: metadata.last_commit_hash,
    },
    {
      icon: User,
      label: "Author",
      value: metadata.last_commit_author,
    },
    {
      icon: GitCommit,
      label: "Commits",
      value: metadata.total_commits,
    },
    {
      icon: LinkIcon,
      label: "Remote",
      value: metadata.remotes?.[0],
    },
  ];

  return (
    <div className="git-info-card">
      {rows.map(({ icon: Icon, label, value }) => (
        <div key={label} className="git-info-row">
          <span className="git-info-icon">
            <Icon size={15} />
          </span>

          <span className="git-info-label">
            {label}
          </span>

          <span className="git-info-value">
            {value ?? "-"}
          </span>
        </div>
      ))}
    </div>
  );
}

export default GitInfo;