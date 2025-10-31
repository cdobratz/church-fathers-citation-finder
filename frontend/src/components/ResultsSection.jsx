import { useState } from 'react'

function ResultsSection({ results, onNewAnalysis, onDownload }) {
  const [selectedMatch, setSelectedMatch] = useState(null)

  return (
    <div className="results-section">
      <div className="results-header">
        <h2>{results.totalMatches} Biblical Citations Found</h2>
        <button className="new-analysis-button" onClick={onNewAnalysis}>
          New Analysis
        </button>
      </div>

      <div className="results-list">
        {results.matches.map((match, index) => (
          <div
            key={index}
            className="result-item"
            onClick={() => setSelectedMatch(match)}
          >
            <div className="result-reference">{match.reference}</div>
            <div className="result-excerpt">
              {match.segment.substring(0, 100)}...
            </div>
          </div>
        ))}
      </div>

      <div className="download-section">
        <button
          className="download-button"
          onClick={() => onDownload('csv')}
        >
          Download CSV
        </button>
        <button
          className="download-button"
          onClick={() => onDownload('json')}
        >
          Download JSON
        </button>
      </div>

      {selectedMatch && (
        <div className="modal-overlay" onClick={() => setSelectedMatch(null)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <h3>{selectedMatch.reference}</h3>
            <div className="modal-text">
              <h4>Verse Text:</h4>
              <p>{selectedMatch.verseText}</p>
              <h4>Context from Clement:</h4>
              <p>{selectedMatch.segment}</p>
            </div>
            <button
              className="modal-close"
              onClick={() => setSelectedMatch(null)}
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

export default ResultsSection
