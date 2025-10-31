function ProcessingSection({ progress }) {
  return (
    <div className="processing-section">
      <div className="spinner"></div>
      <h2>Processing Your Document</h2>
      <p className="progress-text">{progress}</p>
      <div className="progress-bar">
        <div className="progress-fill"></div>
      </div>
    </div>
  )
}

export default ProcessingSection
