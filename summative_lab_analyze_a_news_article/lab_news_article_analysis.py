import re
from collections import Counter
from pathlib import Path

def read_article(file_path):
    """Read the contents of the news article file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None

def count_specific_word(text, target_word):
    """Count occurrences of a specific word in the text."""
    # Convert to lowercase and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(target_word.lower())

def find_most_common_word(text):
    """Find the most frequently occurring word in the text."""
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)[0]
    return most_common[0], most_common[1]

def calculate_avg_word_length(text):
    """Calculate the average word length excluding punctuation."""
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)

def count_paragraphs(text):
    """Count number of paragraphs based on empty lines."""
    # Split by multiple newlines and filter out empty paragraphs
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    return len(paragraphs)

def count_sentences(text):
    """Count number of sentences based on punctuation."""
    # Split by sentence-ending punctuation followed by space or newline
    sentences = re.split(r'[.!?]+(?:\s+|\n|$)', text)
    # Filter out empty strings and whitespace-only strings
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

def analyze_article(file_path, target_word="the"):
    """Perform complete text analysis on the article."""
    # Read the article
    text = read_article(file_path)
    if text is None:
        return

    # Perform analyses
    word_count = count_specific_word(text, target_word)
    common_word, common_count = find_most_common_word(text) or ("N/A", 0)
    avg_length = calculate_avg_word_length(text)
    paragraph_count = count_paragraphs(text)
    sentence_count = count_sentences(text)

    # Display results
    print("\n=== News Article Text Analysis Results ===")
    print(f"Occurrences of '{target_word}': {word_count}")
    print(f"Most common word: '{common_word}' (appears {common_count} times)")
    print(f"Average word length: {avg_length} characters")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")

def main():
    # Assuming the uploaded .txt file is named 'news_article.txt'
    file_path = "news_article.txt"
    
    # Check if file exists
    if not Path(file_path).exists():
        print("Please ensure the news article text file is in the correct directory.")
        return

    # Analyze the article with default target word "the"
    analyze_article(file_path, "the")

if __name__ == "__main__":
    main()