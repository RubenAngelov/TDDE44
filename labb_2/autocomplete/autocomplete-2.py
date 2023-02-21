import csv


def main():
    f = open('data/alphabetical.csv', 'r')
    words_reader = csv.reader(f, delimiter=',')

    word = ""
    while True:
        # Reset file index.
        f.seek(0)

        word = input("Type word: ").lower()
        if word == "q":
            break
        
        suggestion = autocomplete(word, words_reader)
        print("Autocompletion finished: ", suggestion)

    f.close()


def autocomplete(input_word, words_reader):
    """Return autocomplete suggestions."""

    candidates = find_candidates(input_word, words_reader)
    if len(candidates) != 0:
        three_best = n_candidates_with_highest_freq(candidates, 3)
        suggestions = ', '.join([sugg[0] for sugg in three_best])
        return suggestions
    else:
        return "Couldn't find a suggestion"


def find_candidates(input_word, words_reader):
    """Returns a list of all words that start with the same letters as the input word."""
    
    candidates = []
    for word in words_reader:
        if word[0].startswith(input_word):
            candidates.append(word)

    return candidates


def n_candidates_with_highest_freq(candidates, n):
    """Sorts the given candidates based on the frequencies associated with the words."""
    
    sorted_candidates = sorted(candidates, key = lambda candidate : int(candidate[1]), reverse = True)
    return sorted_candidates[0:n]


main()
