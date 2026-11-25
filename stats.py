seen_letters: dict[str, int] = {}

def get_num_words(text: str):
    word_count = len(text.split())
    print(f"Found {word_count} total words")

def get_letter_count(text: str) -> dict[str, int]:
    lower_text = text.lower()
    
    for letter in lower_text:
        
        if letter not in seen_letters:
            seen_letters[letter] = 1

        else:
            seen_letters[letter] += 1

    return(seen_letters)

def sort_on(data: tuple[str, int]) -> int:
    return data[1]

def chars_dict_to_sorted_list(counted_char: dict[str, int]) -> list[tuple[str, int]]:
    sort_list = []

    for char, count in counted_char.items():
        sort_list.append((char, count))

    sort_list = sorted(sort_list, reverse=True, key=sort_on)

    return sort_list