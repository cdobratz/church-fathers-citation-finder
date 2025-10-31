class QuoteMatcher:
    def __init__(self, bible_client):
        self.bible_client = bible_client
        self.matches = {}
        self.bible_index = None  # Will cache all Bible verses
    
    def _build_bible_index(self, translation_id, translation_name):
        """Build an index of all Bible verses once for faster searching"""
        if self.bible_index is not None:
            return self.bible_index
        
        print(f"Building Bible index for {translation_name}...")
        self.bible_index = []
        
        # NT books only
        common_books = ['MAT', 'MRK', 'LUK', 'JHN', 'ACT', 'ROM', '1CO', '2CO', 'GAL', 'EPH', 'PHP', 'COL', '1TH', '2TH', '1TI', '2TI', 'TIT', 'PHM', 'HEB', 'JAS', '1PE', '2PE', '1JN', '2JN', '3JN', 'JUD', 'REV']
        
        books = self.bible_client.get_books(translation_id)
        if not books:
            return self.bible_index
        
        for book_info in books:
            book_id = book_info.get('id', '')
            if book_id not in common_books:
                continue
            
            print(f"  Indexing {book_info.get('name', book_id)}...")
            max_chapters = min(book_info.get('numberOfChapters', 50), 50)
            
            for chapter_num in range(1, max_chapters + 1):
                chapter_data = self.bible_client.get_chapter(book_id, chapter_num, translation_id)
                if not chapter_data:
                    continue
                
                verses = chapter_data.get('verses', [])
                for verse in verses:
                    verse_num = verse.get('verse', '')
                    verse_text = verse.get('text', '')
                    
                    # Normalize verse text once
                    normalized_verse = self._normalize_text(verse_text)
                    
                    self.bible_index.append({
                        'book': book_info.get('name', book_id),
                        'bookId': book_id,
                        'chapter': chapter_num,
                        'verse': verse_num,
                        'text': verse_text,
                        'normalized': normalized_verse,
                        'reference': f"{book_info.get('name', book_id)} {chapter_num}:{verse_num}",
                        'translation': translation_name
                    })
        
        print(f"Bible index built with {len(self.bible_index)} verses\n")
        return self.bible_index
    
    def find_matches(self, segments):
        """Find Bible verse matches for all segments"""
        all_matches = []
        
        print(f"Processing {len(segments)} segments against Greek Bible...")
        
        # Build the Bible index once
        translation_id = self.bible_client.greek_nt
        translation_name = 'Greek NT'
        bible_verses = self._build_bible_index(translation_id, translation_name)
        
        # Now search each segment against the index
        for segment_idx, segment in enumerate(segments):
            if len(segment.strip()) < 15:  # Skip very short segments
                continue
            
            print(f"Processing segment {segment_idx + 1}/{len(segments)}: {segment[:70]}...")
            
            # Normalize segment once
            normalized_segment = self._normalize_text(segment)
            segment_words = set(normalized_segment.split())
            
            # Check against all verses in index
            for verse_data in bible_verses:
                verse_words = set(verse_data['normalized'].split())
                common_words = segment_words & verse_words
                
                # Require at least 5 common words for a match
                if len(common_words) >= 5:
                    match = {
                        'segment': segment,
                        'book': verse_data['book'],
                        'bookId': verse_data['bookId'],
                        'chapter': verse_data['chapter'],
                        'verse': verse_data['verse'],
                        'verseText': verse_data['text'],
                        'reference': verse_data['reference'],
                        'translation': verse_data['translation']
                    }
                    
                    # Deduplicate
                    match_key = f"{verse_data['bookId']}_{verse_data['chapter']}_{verse_data['verse']}"
                    if match_key not in self.matches:
                        self.matches[match_key] = match
                        all_matches.append(match)
                        print(f"  ✓ Found match: {match['reference']}")
        
        print(f"\nTotal unique matches found: {len(all_matches)}")
        return all_matches
    
    def _normalize_text(self, text):
        """Normalize text for matching"""
        import unicodedata
        
        # Normalize
        text_norm = unicodedata.normalize('NFC', text.lower().strip())
        
        # Remove punctuation
        for char in '.,;:!?·()[]{}"\'':
            text_norm = text_norm.replace(char, '')
        
        return text_norm
