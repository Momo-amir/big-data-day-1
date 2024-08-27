import sys
from collections import Counter
import re

# RUN python word_count.py AChristmasCarol_CharlesDickens_English.txt

def word_count(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        # Remove punctuation and split text into words
        words = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?\b", text)

        # Count the total number of words
        total_words = len(words)

        # Count the occurrences of each word
        word_counter = Counter(words)

        # Sort the words by frequency in descending order
        sorted_word_counts = word_counter.most_common()

        # Output the total word count to the console
        print(f"Total word count: {total_words}\n")

        # Output the word counts to the console in descending order
        for word, count in sorted_word_counts:
            print(f"{word} : {count}")

        # Write the output to 'output.txt'
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(f"Total word count: {total_words}\n\n")
            for word, count in sorted_word_counts:
                output_file.write(f"{word} : {count}\n")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <filename>")
    else:
        word_count(sys.argv[1])
