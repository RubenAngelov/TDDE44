import med
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
    best_candidate = next(words_reader)
    best_levenshtein_distance = med.minimum_edit_distance(input_word, best_candidate[0])
    for word in words_reader:
        lavenshtein_distance = med.minimum_edit_distance(input_word, word[0]) 
        if best_levenshtein_distance > lavenshtein_distance:
            best_levenshtein_distance = lavenshtein_distance
            best_candidate = word

    return best_candidate[0]

def candidate_with_highest_freq(candidates):
    sorted_candidates = sorted(candidates, key = lambda candidate : candidate[1], reverse=True)
    return sorted_candidates[0:3]

main()