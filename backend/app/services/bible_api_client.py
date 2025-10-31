import requests
import os
import time

class BibleAPIClient:
    def __init__(self):
        self.base_url = os.getenv('BIBLE_API_BASE_URL', 'https://bible.helloao.org/api')
        self.septuagint = 'grc_bre'  # Brenton Septuagint (Greek OT)
        self.greek_nt = 'grc_sbl'  # SBL Greek New Testament
        self.cache = {}
    
    def get_available_translations(self):
        """Get list of available Bible translations"""
        try:
            response = requests.get(f"{self.base_url}/available_translations.json")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching translations: {e}")
            return []
    
    def get_books(self, translation='BSB'):
        """Get list of books in a translation"""
        cache_key = f"books_{translation}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            url = f"{self.base_url}/{translation}/books.json"
            print(f"Fetching books from: {url}")
            response = requests.get(url, timeout=10)
            print(f"Response status: {response.status_code}")
            print(f"Response length: {len(response.content)}")
            response.raise_for_status()
            data = response.json()
            books = data.get('books', [])
            print(f"Found {len(books)} books")
            self.cache[cache_key] = books
            return books
        except Exception as e:
            print(f"Error fetching books from {translation}: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
            return []
    
    def get_book_info(self, book_id, translation='BSB'):
        """Get info about a specific book"""
        books = self.get_books(translation)
        for book in books:
            if book.get('id') == book_id:
                return book
        return None
    
    def get_chapter(self, book, chapter, translation='BSB'):
        """Get a specific chapter from the Bible"""
        cache_key = f"{translation}_{book}_{chapter}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            url = f"{self.base_url}/{translation}/{book}/{chapter}.json"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Extract verses from content array
            chapter_content = data.get('chapter', {}).get('content', [])
            verses = []
            for item in chapter_content:
                if item.get('type') == 'verse':
                    verse_num = item.get('number')
                    # Handle nested content - can be strings or dicts
                    verse_content = item.get('content', [])
                    text_parts = []
                    for content_item in verse_content:
                        if isinstance(content_item, str):
                            text_parts.append(content_item)
                        elif isinstance(content_item, dict):
                            # Extract text from nested structures (like footnotes, etc.)
                            text_parts.append(content_item.get('text', ''))
                    verse_text = ' '.join(text_parts)
                    verses.append({
                        'verse': verse_num,
                        'text': verse_text
                    })
            
            chapter_data = {'verses': verses}
            self.cache[cache_key] = chapter_data
            
            # Small delay to respect rate limits
            time.sleep(0.05)
            
            return chapter_data
        except Exception as e:
            print(f"Error fetching chapter {book} {chapter}: {e}")
            return None
    
    def search_text_in_verse(self, verse_text, search_text):
        """Check if search text appears in verse (case-insensitive, normalized)"""
        import unicodedata
        
        # Normalize both texts
        verse_norm = unicodedata.normalize('NFC', verse_text.lower())
        search_norm = unicodedata.normalize('NFC', search_text.lower())
        
        # Remove common punctuation
        for char in '.,;:!?·':
            verse_norm = verse_norm.replace(char, ' ')
            search_norm = search_norm.replace(char, ' ')
        
        # Check if search text is in verse
        return search_norm in verse_norm
