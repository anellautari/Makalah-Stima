import random
import nltk
from nltk.corpus import words
from brute_force_solver import brute_force
from greedy_solver import greedy

nltk.download('words')
all_words = [w.lower() for w in words.words() if len(w) == 5 and w.isalpha()]

def valid_word(word):
    return word.isalpha() and len(word) == 5 and word.lower() in all_words

def get_target_word():
    while True:
        choice = input("\nPilih cara menentukan kata target:\n1. Acak dari kamus\n2. Input manual\nMasukkan pilihan (1/2): ")
        if choice == "1":
            return random.choice(all_words)
        elif choice == "2":
            word = input("Masukkan kata target (5 huruf, alfabetik, ada di kamus): ").lower()
            if valid_word(word):
                return word
            else:
                print("Kata tidak valid. Harus 5 huruf alfabet dan ada di kamus.")
        else:
            print("Pilihan tidak valid. Masukkan 1 atau 2.")

def get_algorithm_choice():
    while True:
        algo = input("\nPilih algoritma:\n1. Brute Force\n2. Greedy\nMasukkan pilihan (1/2): ")
        if algo == "1":
            return "brute force"
        elif algo == "2":
            return "greedy"
        else:
            print("Pilihan tidak valid. Masukkan 1 atau 2.")

def main():
    print("🎮 Selamat datang di Wordle Solver!")
    print("Program ini akan menyelesaikan Wordle menggunakan algoritma brute force dan greedy.\n")

    while True:
        target = get_target_word()
        algo = get_algorithm_choice()
        print(f"\nMenyelesaikan Wordle untuk kata: {target.upper()} dengan algoritma: {algo.title()}\n")

        if algo == "brute force":
            brute_force(target)
        else:
            greedy(target)

        again = input("\nIngin bermain lagi? (Y/N): ").strip().lower()
        if again != 'y':
            print("\n👋 Terima kasih telah menggunakan Wordle Solver. Sampai jumpa!\n")
            break

if __name__ == "__main__":
    main()
