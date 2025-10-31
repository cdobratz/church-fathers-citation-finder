import { useState } from 'react'
import UploadSection from './components/UploadSection'
import ProcessingSection from './components/ProcessingSection'
import ResultsSection from './components/ResultsSection'
import './styles/App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

function App() {
  const [stage, setStage] = useState('upload') // 'upload', 'processing', 'results'
  const [file, setFile] = useState(null)
  const [results, setResults] = useState(null)
  const [error, setError] = useState(null)
  const [progress, setProgress] = useState('')

  const handleFileSelect = (selectedFile) => {
    setFile(selectedFile)
    setError(null)
  }

  const handleUpload = async () => {
    if (!file) return

    setStage('processing')
    setError(null)
    setProgress('Uploading and Extracting Text...')

    const formData = new FormData()
    formData.append('file', file)

    try {
      setProgress('Querying Bible Verses...')
      
      const response = await fetch(`${API_URL}/process`, {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.error || 'Failed to process document')
      }

      const data = await response.json()
      
      setProgress('Complete!')
      setResults(data)
      setStage('results')
    } catch (err) {
      console.error('Error processing document:', err)
      setError(err.message)
      setStage('upload')
    }
  }

  const handleNewAnalysis = () => {
    setStage('upload')
    setFile(null)
    setResults(null)
    setError(null)
    setProgress('')
  }

  const handleDownload = async (format) => {
    try {
      const response = await fetch(`${API_URL}/download/${format}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ matches: results.matches }),
      })

      if (!response.ok) {
        throw new Error('Download failed')
      }

      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `bible_citations.${format}`
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (err) {
      console.error('Download error:', err)
      alert('Failed to download file')
    }
  }

  return (
    <div className="app">
      <header className="header">
        <h1>Church Fathers Bible Citation Detector</h1>
        <p className="subtitle">Detect Biblical quotations in early Church writings</p>
      </header>

      <main className="main-content">
        {stage === 'upload' && (
          <UploadSection
            onFileSelect={handleFileSelect}
            onUpload={handleUpload}
            file={file}
            error={error}
          />
        )}

        {stage === 'processing' && (
          <ProcessingSection progress={progress} />
        )}

        {stage === 'results' && results && (
          <ResultsSection
            results={results}
            onNewAnalysis={handleNewAnalysis}
            onDownload={handleDownload}
          />
        )}
      </main>

      <footer className="footer">
        <p>MVP • Clement of Alexandria • Septuagint (LXX)</p>
      </footer>
    </div>
  )
}

export default App
