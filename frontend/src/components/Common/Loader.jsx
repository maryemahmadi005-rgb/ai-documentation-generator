import "./Loader.css";

function Loader({ message = "Chargement en cours..." }) {
  return (
    <div className="loader-container">
      <div className="spinner" />
      <p className="loader-message">{message}</p>
    </div>
  );
}

export default Loader;
