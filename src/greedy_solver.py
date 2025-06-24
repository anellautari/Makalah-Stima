import time
import nltk
from nltk.corpus import words
from collections import Counter, defaultdict

all_words = [w.lower() for w in words.words() if len(w) == 5 and w.isalpha()]

# Warna ANSI
GREEN = '\033[92m'
YELLOW = '\033[93m'
GRAY = '\033[90m'
RESET = '\033[0m'

def get_feedback(guess, answer):
    feedback = ['gray'] * 5
    answer_chars = list(answer)

    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = 'green'
            answer_chars[i] = None

    for i in range(5):
        if feedback[i] == 'gray' and guess[i] in answer_chars:
            feedback[i] = 'yellow'
            answer_chars[answer_chars.index(guess[i])] = None

    return feedback

def print_colored_feedback(guess, feedback):
    result = ""
    for i in range(5):
        if feedback[i] == 'green':
            result += GREEN + guess[i].upper() + RESET
        elif feedback[i] == 'yellow':
            result += YELLOW + guess[i].upper() + RESET
        else:
            result += GRAY + guess[i].upper() + RESET
    print(result)

def most_informative_word(word_list, banned, used):
    # Prioritaskan huruf yang belum pernah dicoba
    freqs = Counter()
    for word in word_list:
        unique_letters = set(word) - banned - used
        freqs.update(unique_letters)

    max_score = -1
    best_word = word_list[0]

    for word in word_list:
        score = sum(freqs[c] for c in set(word))
        if score > max_score:
            max_score = score
            best_word = word

    return best_word

def filter_candidates(word_list, green, yellow, banned):
    filtered = []

    for word in word_list:
        valid = True

        # green check
        for i in range(5):
            if green[i] != '_' and word[i] != green[i]:
                valid = False
                break

        # yellow check
        for letter, bad_pos in yellow.items():
            if letter not in word or any(word[p] == letter for p in bad_pos):
                valid = False
                break

        # banned (gray) check
        if any(c in banned for c in word if c not in green and c not in yellow):
            valid = False

        if valid:
            filtered.append(word)

    return filtered

def greedy(answer):
    start_time = time.time()
    green = ['_'] * 5
    yellow = defaultdict(list)
    banned = set()
    used_letters = set()
    candidates = all_words.copy()
    tries = 0

    guess = most_informative_word(candidates, banned, used_letters)

    while guess:
        tries += 1
        feedback = get_feedback(guess, answer)
        print(f"Tebakan {tries}: ", end="")
        print_colored_feedback(guess, feedback)

        for i in range(5):
            c = guess[i]
            used_letters.add(c)
            if feedback[i] == 'green':
                green[i] = c
            elif feedback[i] == 'yellow':
                yellow[c].append(i)
            else:
                if c not in green and c not in yellow:
                    banned.add(c)

        if guess == answer:
            break

        candidates = filter_candidates(candidates, green, yellow, banned)
        guess = most_informative_word(candidates, banned, used_letters)

    duration = time.time() - start_time
    print(f"\n[Greedy] Jawaban ditemukan: {answer.upper()} dalam {tries} langkah ({duration:.4f} detik)")


# TESTING
# if __name__ == "__main__":
#     # Kata yang akan diuji
#     target = "green"
#     if target not in all_words:
#         print(f"Kata {target} tidak ada di kamus.")
#     else:
#         greedy(target)