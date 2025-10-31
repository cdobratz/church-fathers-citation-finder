# Church Fathers Bible Citation Detector - Backend

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
```

4. Run the development server:
```bash
python run.py
```

The API will be available at http://localhost:5000

## API Endpoints

- `GET /api/health` - Health check
- `POST /api/process` - Process a PDF file
- `POST /api/download/csv` - Download results as CSV
- `POST /api/download/json` - Download results as JSON

## Deployment

### Using Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn run:app`
5. Add environment variables from `.env`

### Using Railway

1. Create new project on Railway
2. Connect GitHub repository
3. Railway will auto-detect Python and use gunicorn
4. Add environment variables
