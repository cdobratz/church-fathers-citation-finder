from flask import Blueprint, request, jsonify
from app.services.pdf_processor import PDFProcessor
from app.services.text_processor import TextProcessor
from app.services.bible_api_client import BibleAPIClient
from app.services.matcher import QuoteMatcher
import traceback

bp = Blueprint('main', __name__, url_prefix='/api')

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Server is running'}), 200

@bp.route('/process', methods=['POST'])
def process_document():
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.pdf'):
            return jsonify({'error': 'Only PDF files are supported in MVP'}), 400
        
        # Extract text from PDF
        pdf_processor = PDFProcessor()
        raw_text = pdf_processor.extract_text(file)
        
        if not raw_text:
            return jsonify({'error': 'Could not extract text from PDF'}), 400
        
        # Process and segment text
        text_processor = TextProcessor()
        segments = text_processor.process_text(raw_text)
        
        # Query Bible API and find matches
        bible_client = BibleAPIClient()
        matcher = QuoteMatcher(bible_client)
        
        matches = matcher.find_matches(segments)
        
        # Prepare response
        response = {
            'success': True,
            'totalMatches': len(matches),
            'matches': matches,
            'segments_processed': len(segments)
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        print(f"Error processing document: {str(e)}")
        traceback.print_exc()
        return jsonify({
            'error': 'An error occurred while processing the document',
            'details': str(e)
        }), 500

@bp.route('/download/<format>', methods=['POST'])
def download_results(format):
    try:
        data = request.get_json()
        
        if format == 'csv':
            from app.utils.export import export_to_csv
            csv_data = export_to_csv(data.get('matches', []))
            return csv_data, 200, {
                'Content-Type': 'text/csv',
                'Content-Disposition': 'attachment; filename=bible_citations.csv'
            }
        
        elif format == 'json':
            from app.utils.export import export_to_json
            json_data = export_to_json(data.get('matches', []))
            return json_data, 200, {
                'Content-Type': 'application/json',
                'Content-Disposition': 'attachment; filename=bible_citations.json'
            }
        
        else:
            return jsonify({'error': 'Invalid format. Use csv or json'}), 400
            
    except Exception as e:
        print(f"Error generating download: {str(e)}")
        return jsonify({'error': str(e)}), 500
