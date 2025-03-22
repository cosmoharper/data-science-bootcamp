# pythonAssessment.py
import re
from collections import Counter
from pathlib import Path

def read_article(file_path):
    """Read the contents of the news article file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None

def count_specific_word(text, target_word):
    """Count occurrences of a specific word in the text using a for loop."""
    words = re.findall(r'\b\w+\b', text.lower())
    count = 0
    # Using for loop as requested
    for word in words:
        if word == target_word.lower():
            count += 1
    return count

def find_most_common_word(text):
    """Find the most frequently occurring word in the text."""
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
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    return len(paragraphs)

def count_sentences(text):
    """Count number of sentences based on punctuation."""
    sentences = re.split(r'[.!?]+(?:\s+|\n|$)', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

def display_results(target_word, word_count, common_word, common_count, 
                   avg_length, paragraph_count, sentence_count):
    """Display analysis results."""
    print("\n=== News Article Text Analysis Results ===")
    print(f"Occurrences of '{target_word}': {word_count}")
    print(f"Most common word: '{common_word}' (appears {common_count} times)")
    print(f"Average word length: {avg_length} characters")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")

def analyze_article(file_path):
    """Perform text analysis with user interaction."""
    # Read the article
    text = read_article(file_path)
    if text is None:
        print(f"Error: Could not read file {file_path}")
        return

    # Using while loop for user input
    analyzing = True
    while analyzing:
        # Get target word from user with conditional
        target_word = input("\nEnter a word to count (or 'quit' to exit): ")
        if target_word.lower() == 'quit':
            analyzing = False
            print("Analysis complete. Goodbye!")
            continue
        
        # Perform analyses
        word_count = count_specific_word(text, target_word)
        common_result = find_most_common_word(text)
        common_word, common_count = common_result if common_result else ("N/A", 0)
        avg_length = calculate_avg_word_length(text)
        paragraph_count = count_paragraphs(text)
        sentence_count = count_sentences(text)

        # Display results
        display_results(target_word, word_count, common_word, common_count,
                       avg_length, paragraph_count, sentence_count)

def main():
    file_path = "news_article.txt"
    
    # Conditional to check file existence
    if not Path(file_path).exists():
        print("Please ensure the news article text file is in the correct directory.")
        return

    print("Welcome to News Article Analyzer")
    analyze_article(file_path)

if __name__ == "__main__":
    main()