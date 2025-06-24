import time
import nltk
from nltk.corpus import words
from collections import defaultdict

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

def filter_candidates(candidates, green, yellow, banned):
    filtered = []

    for word in candidates:
        valid = True

        # green check
        for i in range(5):
            if green[i] != '_' and word[i] != green[i]:
                valid = False
                break

        # yellow check
        for letter, bad_pos in yellow.items():
            if letter not in word:
                valid = False
                break
            for pos in bad_pos:
                if word[pos] == letter:
                    valid = False
                    break
            if not valid:
                break

        # banned (gray) check
        if any(c in banned for c in word if c not in green and c not in yellow.keys()):
            valid = False

        if valid:
            filtered.append(word)

    return filtered

def brute_force(answer):
    start_time = time.time()
    green = ['_'] * 5
    yellow = defaultdict(list)
    banned = set()
    candidates = all_words.copy()
    tries = 0

    while candidates:
        guess = candidates[0]
        candidates = candidates[1:]
        tries += 1

        feedback = get_feedback(guess, answer)
        print(f"Tebakan {tries}: ", end="")
        print_colored_feedback(guess, feedback)

        for i in range(5):
            c = guess[i]
            if feedback[i] == 'green':
                green[i] = c
            elif feedback[i] == 'yellow':
                if i not in yellow[c]:
                    yellow[c].append(i)
            elif feedback[i] == 'gray':
                if c not in green and c not in yellow.keys():
                    banned.add(c)

        if guess == answer:
            break

        # Update filter kandidat
        candidates = filter_candidates(candidates, green, yellow, banned)

    duration = time.time() - start_time
    print(f"\n[Brute Force] Jawaban ditemukan: {answer.upper()} dalam {tries} langkah ({duration:.4f} detik)")


# TESTING
# if __name__ == "__main__":
#     target = "green"
#     if target not in all_words:
#         print(f"Kata {target} tidak ditemukan.")
#     else:
#         brute_force(target)