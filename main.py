import sys
from stats import count_words, count_characters, sort_char_counts

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def main():
    # ✅ Verificamos que se pase un argumento
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # ✅ Tomamos el path desde los argumentos
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    sorted_chars = sort_char_counts(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()