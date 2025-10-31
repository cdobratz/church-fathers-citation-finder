import json
import csv
from io import StringIO

def export_to_csv(matches):
    """Export matches to CSV format"""
    output = StringIO()
    
    if not matches:
        return "No matches found\n"
    
    fieldnames = ['reference', 'book', 'chapter', 'verse', 'segment', 'verseText']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    
    writer.writeheader()
    for match in matches:
        writer.writerow({
            'reference': match.get('reference', ''),
            'book': match.get('book', ''),
            'chapter': match.get('chapter', ''),
            'verse': match.get('verse', ''),
            'segment': match.get('segment', '')[:100],  # Truncate long segments
            'verseText': match.get('verseText', '')[:100]
        })
    
    return output.getvalue()

def export_to_json(matches):
    """Export matches to JSON format"""
    return json.dumps({
        'totalMatches': len(matches),
        'matches': matches
    }, indent=2, ensure_ascii=False)
