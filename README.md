# Church Fathers Biblical Citation Finder

An MVP application that identifies biblical quotations and allusions in Greek Church Fathers texts by matching them against the Greek New Testament.

## 📖 Overview

This tool helps scholars and researchers automatically detect New Testament citations in patristic Greek literature. Upload a PDF containing Greek text (such as writings from the Church Fathers), and the application will:

- Extract and segment the text
- Search for biblical quotations in the Greek New Testament (SBL Greek NT)
- Display matching verses with references
- Export results to CSV or JSON

## ✨ Features

### Current MVP Features
- **PDF Text Extraction**: Upload Greek language PDF documents
- **Greek New Testament Search**: Searches across all 27 NT books (Matthew - Revelation)
- **Intelligent Matching**: Uses word-overlap algorithm to find quotations and allusions
- **Real-time Processing**: See matches as they're discovered
- **Export Options**: Download results as CSV or JSON
- **Greek Text Support**: Full Unicode normalization for accurate Greek text matching

### Translation Used
- **Greek New Testament**: SBL Greek New Testament (grc_sbl) via [bible.helloao.org API](https://bible.helloao.org)

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- npm or yarn

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ChurchFathers
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Frontend Setup**
```bash
cd frontend
npm install
```

4. **Environment Configuration**

Backend `.env`:
```env
FLASK_APP=run.py
FLASK_ENV=development
BIBLE_API_BASE_URL=https://bible.helloao.org/api
```

Frontend `.env`:
```env
VITE_API_URL=http://localhost:5001
```

### Running the Application

**Development Mode:**

1. Start the backend (from `backend/` directory):
```bash
python run.py
```

2. Start the frontend (from `frontend/` directory):
```bash
npm run dev
```

3. Open browser to `http://localhost:5173`

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
docker-compose up --build
```

Access the application at `http://localhost:5173`

### Manual Docker Build

**Backend:**
```bash
cd backend
docker build -t church-fathers-backend .
docker run -p 5001:5001 church-fathers-backend
```

**Frontend:**
```bash
cd frontend
docker build -t church-fathers-frontend .
docker run -p 5173:5173 church-fathers-frontend
```

## 📁 Project Structure

```
ChurchFathers/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   └── main_routes.py      # API endpoints
│   │   ├── services/
│   │   │   ├── bible_api_client.py # Bible API integration
│   │   │   ├── matcher.py          # Citation matching logic
│   │   │   ├── pdf_processor.py    # PDF text extraction
│   │   │   └── text_processor.py   # Text segmentation
│   │   └── utils/
│   │       └── export.py           # CSV/JSON export
│   ├── run.py                      # Flask application entry
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.jsx      # Upload interface
│   │   │   ├── ResultsDisplay.jsx  # Results viewer
│   │   │   └── ExportButtons.jsx   # Export controls
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🔧 How It Works

### 1. Text Processing
- Extracts text from uploaded PDF using PyMuPDF
- Segments text into meaningful chunks (paragraphs, sentences)
- Normalizes Greek Unicode characters

### 2. Bible Indexing
- On first run, fetches and indexes all Greek NT verses (~7,959 verses)
- Caches normalized verse text for fast searching
- Builds in-memory search index

### 3. Matching Algorithm
- Compares each text segment against all indexed verses
- Uses word-overlap detection (minimum 5 common words)
- Handles Greek diacritics and punctuation variations
- Deduplicates results

### 4. Results Display
- Shows matched verse reference (e.g., "Matthew 5:3")
- Displays the original segment and matched verse text
- Provides export options

## 📊 API Endpoints

### `POST /api/process`
Upload and process a PDF document

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (PDF file)

**Response:**
```json
{
  "success": true,
  "totalMatches": 42,
  "segments_processed": 251,
  "matches": [
    {
      "segment": "Greek text segment...",
      "book": "Matthew",
      "bookId": "MAT",
      "chapter": 5,
      "verse": 3,
      "verseText": "μακάριοι οἱ πτωχοὶ τῷ πνεύματι...",
      "reference": "Matthew 5:3",
      "translation": "Greek NT"
    }
  ]
}
```

### `GET /api/health`
Health check endpoint

### `POST /api/download/csv`
Export results as CSV

### `POST /api/download/json`
Export results as JSON

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework
- **PyMuPDF (fitz)**: PDF text extraction
- **Requests**: HTTP client for Bible API
- **Python 3.12**: Runtime environment

### Frontend
- **React 18**: UI framework
- **Vite**: Build tool and dev server
- **Axios**: HTTP client
- **CSS3**: Styling

### External APIs
- **bible.helloao.org**: Greek Bible text source

## 📝 Configuration

### Matching Sensitivity
Adjust minimum word overlap in `backend/app/services/matcher.py`:
```python
# Line 85: Require at least 5 common words for a match
if len(common_words) >= 5:
```

### Books to Search
Modify the book list in `backend/app/services/matcher.py`:
```python
common_books = ['MAT', 'MRK', 'LUK', 'JHN', ...]
```

## 🔮 Future Enhancements

- [ ] Add Septuagint (Greek OT) support
- [ ] Implement fuzzy matching for paraphrases
- [ ] Support for multiple Greek NT translations
- [ ] Verse context display (surrounding verses)
- [ ] Batch processing of multiple PDFs
- [ ] Save/load search sessions
- [ ] Advanced filtering and sorting options
- [ ] Statistical analysis of citation patterns
- [ ] Support for non-PDF formats (TXT, DOCX)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 🙏 Acknowledgments

- Church Fathers text provided by [jtauber link](https://jtauber.github.io/apostolic-fathers/)
- Greek Bible text API provided by [bible.helloao.org](https://bible.helloao.org)
- SBL Greek New Testament text

## 📞 Support

For questions or issues, please open an issue on GitHub.

---

**Note**: This is an MVP (Minimum Viable Product). The matching algorithm is optimized for exact quotations and close paraphrases. Results may require scholarly verification.
