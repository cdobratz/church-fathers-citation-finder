import re
import unicodedata

class TextProcessor:
    def process_text(self, raw_text):
        """Clean and segment Greek text"""
        # Normalize Unicode
        text = unicodedata.normalize('NFC', raw_text)
        
        # Remove footnotes and page numbers
        text = self._remove_footnotes(text)
        
        # Clean extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Split into segments (sentences/clauses)
        segments = self._segment_text(text)
        
        # Filter out very short segments
        segments = [s for s in segments if len(s.strip()) > 10]
        
        return segments
    
    def _remove_footnotes(self, text):
        """Remove common footnote patterns"""
        # Remove numbered footnotes
        text = re.sub(r'\d+', '', text)
        
        # Remove common footnote markers
        text = re.sub(r'[\[\]\(\)\{\}]', '', text)
        
        return text
    
    def _segment_text(self, text):
        """Split text into logical segments"""
        # Split on Greek sentence terminators
        # Greek uses · (middle dot), ; (question mark), and . (period)
        segments = re.split(r'[.;·]', text)
        
        # Clean each segment
        segments = [s.strip() for s in segments if s.strip()]
        
        return segments
