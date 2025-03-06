def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    total = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in total:
            total[lower_char] += 1
        else:
            total[lower_char] = 1
    return total

def sorted_chars(text):
    order_chars = count_chars(text)
    list_char = list(order_chars.items())
    list_char.sort(reverse=True, key=lambda item: item[1])
    return list_char