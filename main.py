from stats import get_word_count
from stats import get_char_count
from stats import chars_dict_to_sorted_list
import sys

def get_book_text(path):
	with open(path) as f:
    		file_contents = f.read()
	return file_contents
def print_report(path, count, sorted_list):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        for char, count in sorted_list:
                if char.isalpha():
                        print(f"{char}: {count}")
        print("============= END ===============")
def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	read = get_book_text(book_path)
	num_words = get_word_count(read)
		
	char = get_char_count(read)
	
	char_count = chars_dict_to_sorted_list(char)
	print_report(book_path, num_words, char_count)

main()
