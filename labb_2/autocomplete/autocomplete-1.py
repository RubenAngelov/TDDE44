import csv

def main():
    # Load words
    f = open('data/alphabetical_words', 'r')

    word = ""
    while word != "q":
        f.seek(0)
        word = input("Type word: ").lower()
        suggestion = autocomplete(word, f)
        print("Autocompletion finished: ", suggestion)

    f.close()

def autocomplete(input_word, f):
    """Return autocomplete suggestions."""
    candidates = find_candidates(input_word, f)
    if len(candidates) != 0:
        suggestions = ', '.join(candidates[0:3])
        return suggestions
    else:
        return "Couldn't find a suggestion"

def find_candidates(input_word, f):
    candidates = []
    word = f.readline()[:-1]
    while word != "":
        if word[0:len(input_word)] == input_word:
            candidates.append(word)
        word = f.readline()[:-1]

    return candidates


main()