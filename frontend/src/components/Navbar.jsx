import { useEffect, useRef, useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { Home as HomeIcon, History as HistoryIcon, ChevronDown, LogOut, User, Menu, X } from "lucide-react";
import ThemeToggle from "./ThemeToggle.jsx";
import "./Navbar.css";

/**
 * Barre de navigation principale : logo, Home / History, thème,
 * dropdown utilisateur (déconnexion), menu mobile responsive.
 */
function Navbar() {
  const navigate = useNavigate();
  const storedUser = localStorage.getItem("user");
  const user = storedUser ? JSON.parse(storedUser) : null;

  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const dropdownRef = useRef(null);

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        setDropdownOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  const linkClass = ({ isActive }) => "nav-link" + (isActive ? " active" : "");
  const displayName = user?.username || user?.email || "Account";
  const initials = displayName.slice(0, 1).toUpperCase();

  return (
    <header className="navbar">
      <div className="navbar-inner">
        <div className="navbar-brand" onClick={() => navigate("/home")}>
          <span className="brand-dot" />
          <span>DocGen AI</span>
        </div>

        <nav className="navbar-links">
          <NavLink to="/home" className={linkClass}>
            <HomeIcon size={15} /> Home
          </NavLink>
          <NavLink to="/history" className={linkClass}>
            <HistoryIcon size={15} /> History
          </NavLink>
        </nav>

        <div className="navbar-right">
          <ThemeToggle />

          <div className="user-menu" ref={dropdownRef}>
            <button
              type="button"
              className="user-menu-trigger"
              onClick={() => setDropdownOpen((o) => !o)}
            >
              <span className="user-avatar">{initials}</span>
              <span className="navbar-user">{displayName}</span>
              <ChevronDown size={14} className={`chevron ${dropdownOpen ? "open" : ""}`} />
            </button>

            {dropdownOpen && (
              <div className="user-dropdown">
                <div className="user-dropdown-header">
                  <span className="user-avatar">{initials}</span>
                  <div>
                    <div className="user-dropdown-name">{displayName}</div>
                    {user?.email && <div className="user-dropdown-email">{user.email}</div>}
                  </div>
                </div>
                <button type="button" className="user-dropdown-item" onClick={() => navigate("/home")}>
                  <User size={15} /> My account
                </button>
                <button type="button" className="user-dropdown-item danger" onClick={handleLogout}>
                  <LogOut size={15} /> Logout
                </button>
              </div>
            )}
          </div>

          <button
            type="button"
            className="mobile-menu-toggle btn-icon"
            onClick={() => setMobileOpen((o) => !o)}
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X size={18} /> : <Menu size={18} />}
          </button>
        </div>
      </div>

      {mobileOpen && (
        <nav className="mobile-nav">
          <NavLink to="/home" className={linkClass} onClick={() => setMobileOpen(false)}>
            <HomeIcon size={16} /> Home
          </NavLink>
          <NavLink to="/history" className={linkClass} onClick={() => setMobileOpen(false)}>
            <HistoryIcon size={16} /> History
          </NavLink>
          <button type="button" className="nav-link danger" onClick={handleLogout}>
            <LogOut size={16} /> Logout
          </button>
        </nav>
      )}
    </header>
  );
}

export default Navbar;
