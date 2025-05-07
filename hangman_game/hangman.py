import random

# Words and hints
words_with_hints = {
    "python": "A popular programming language.",
    "laptop": "A portable computer.",
    "keyboard": "Used to type.",
    "umbrella": "Used in rain.",
    "satellite": "Orbits planets.",
}

# Hangman stages (visuals)
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Select a random word and hint
word, hint = random.choice(list(words_with_hints.items()))
guessed = ["_"] * len(word)
tries = 0
max_tries = len(stages) - 1
guessed_letters = []

# Game intro
print("🔠 Welcome to Hangman!")
print("💡 Hint:", hint)

# Game loop
while tries < max_tries and "_" in guessed:
    print(stages[tries])
    print("Word:", " ".join(guessed))
    print("Guessed Letters:", " ".join(guessed_letters))
    
    guess = input("📥 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for idx, letter in enumerate(word):
            if letter == guess:
                guessed[idx] = guess
    else:
        tries += 1
        print("❌ Wrong guess!")

# End of game
if "_" not in guessed:
    print("🎉 You won! The word was:", word)
else:
    print(stages[tries])
    print("💀 Game Over! The word was:", word)

#rudra narayan swain
