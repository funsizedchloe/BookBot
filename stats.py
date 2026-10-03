def get_word_count(text):
        words = text.split()
        return len(words)
def get_char_count(text) -> dict[str, int]:
	char_count = {}
	for char in text.lower():
		char_count[char] = char_count.get(char, 0) + 1
	return char_count
def sort_on(pair: tuple[str, int]) -> int:
	return pair[1]
def chars_dict_to_sorted_list(counts: dict[str, int]) -> list[tuple[str, int]]:
	result = []
	for key in counts:
		count = counts[key]
		pair = (key, count)
		result.append(pair)
	sorted_result = sorted(result, reverse=True, key=sort_on)
	return sorted_result
