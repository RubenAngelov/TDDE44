import csv

def main():
    # Load words
    f = open('data/alphabetical.csv', 'r')

    word = ""
    while word != "q":
        f.seek(0)
        words_reader = csv.reader(f, delimiter=',')
        word = input("Type word: ").lower()
        suggestion = autocomplete(word, words_reader)
        print("Autocompletion finished: ", suggestion)

    f.close()

def autocomplete(input_word, words_reader):
    """Return autocomplete suggestions."""
    candidates = find_candidates(input_word, words_reader)
    if len(candidates) != 0:
        three_best = candidate_with_highest_freq(candidates)
        suggestions = ', '.join([sugg[0] for sugg in three_best])
        return suggestions
    else:
        return "Couldn't find a suggestion"

def find_candidates(input_word, words_reader):
    candidates = []
    for word in words_reader:
        if word[0][0:len(input_word)] == input_word:
            candidates.append(word)

    return candidates

def candidate_with_highest_freq(candidates):
    sorted_candidates = sorted(candidates, key = lambda candidate : candidate[1], reverse=True)
    return sorted_candidates[0:3]


main()