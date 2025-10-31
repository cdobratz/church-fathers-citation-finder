# Church Fathers Bible Citation Detector

An MVP web application that detects biblical quotations from the Septuagint (LXX) in early Church Father texts, starting with Clement of Alexandria.

## Features

- ✅ Upload Greek PDF texts
- ✅ Automatic text extraction and cleaning
- ✅ Quote detection against Septuagint via Open Bible API
- ✅ Interactive results display
- ✅ Export to CSV/JSON
- ✅ No account required

## Project Structure

```
church-fathers-mvp/
├── backend/          # Python Flask API
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── requirements.txt
│   └── run.py
├── frontend/         # React + Vite
│   ├── src/
│   │   ├── components/
│   │   └── styles/
│   ├── package.json
│   └── index.html
└── README.md
```

## Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python run.py
```

Backend runs on http://localhost:5000

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

Frontend runs on http://localhost:3000

## Usage

1. Open http://localhost:3000
2. Upload a Greek PDF (e.g., Clement of Alexandria)
3. Wait for processing (~10-30 seconds depending on text length)
4. View results with clickable verse references
5. Download as CSV or JSON

## Deployment

### Backend (Render/Railway)

1. Push code to GitHub
2. Create new web service
3. Connect repository
4. Set environment variables
5. Deploy

### Frontend (Vercel/Netlify)

1. Push code to GitHub
2. Import project
3. Set build command: `npm run build`
4. Set publish directory: `dist`
5. Deploy

## Tech Stack

- **Backend**: Python, Flask, PyPDF2, pdfplumber
- **Frontend**: React, Vite
- **API**: Open Bible API (https://bible.helloao.org)
- **Deployment**: Render (backend), Vercel (frontend)

## MVP Limitations

- Only supports PDF files
- Only searches common biblical books (for performance)
- Exact text matching (no fuzzy matching)
- Greek text only (Septuagint)
- No user accounts or history

## Future Enhancements

- Fuzzy matching and lemmatization
- Support for more Church Fathers
- Multiple Bible translations
- User accounts and search history
- Improved performance with caching
- HTML and plain text upload support

## License

MIT

## Credits

Built using the Free Use Bible API
