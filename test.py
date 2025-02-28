word = input("Введите букву: ")
string = input("Найти самое короткое слово: ")

def find_shortest_word(word, string):
    words = string.split()
    shortest_word = None
    shortest_word_len = float("inf")
    
    for w in words:
        if w.startswith(word) and len(w) < shortest_word_len:
            shortest_word = w
            shortest_word_len = len(w)
    
    return shortest_word

