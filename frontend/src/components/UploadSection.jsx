import { useRef } from 'react'

function UploadSection({ onFileSelect, onUpload, file, error }) {
  const fileInputRef = useRef(null)

  const handleDragOver = (e) => {
    e.preventDefault()
    e.stopPropagation()
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    
    const droppedFile = e.dataTransfer.files[0]
    if (droppedFile && droppedFile.type === 'application/pdf') {
      onFileSelect(droppedFile)
    } else {
      alert('Please upload a PDF file')
    }
  }

  const handleFileInput = (e) => {
    const selectedFile = e.target.files[0]
    if (selectedFile) {
      onFileSelect(selectedFile)
    }
  }

  const handleClick = () => {
    fileInputRef.current?.click()
  }

  return (
    <div className="upload-section">
      <div
        className={`upload-area ${file ? 'has-file' : ''}`}
        onDragOver={handleDragOver}
        onDrop={handleDrop}
        onClick={handleClick}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept=".pdf"
          onChange={handleFileInput}
          style={{ display: 'none' }}
        />
        
        <div className="upload-icon">📄</div>
        
        {file ? (
          <div className="file-info">
            <p className="file-name">{file.name}</p>
            <p className="file-size">{(file.size / 1024).toFixed(2)} KB</p>
          </div>
        ) : (
          <>
            <p className="upload-text">Drag and drop your PDF here</p>
            <p className="upload-subtext">or click to browse</p>
            <p className="upload-hint">Upload Greek text from Clement of Alexandria</p>
          </>
        )}
      </div>

      {error && (
        <div className="error-message">
          ⚠️ {error}
        </div>
      )}

      {file && (
        <button className="upload-button" onClick={onUpload}>
          Analyze Document
        </button>
      )}
    </div>
  )
}

export default UploadSection
