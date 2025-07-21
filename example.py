import random

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do what you can, with what you have, where you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "Keep your face always toward the sunshipune—and shadows will fall behind you.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "You are never too old to set another goal or to dream a new dream.",
    "Believe you can and you're halfway there.",
    "What we think, we become.",
    "Act as if what you do makes a difference. It does.",
    "Quality is not an act, it is a habit.",
    "The best way to get started is to quit talking and begin doing.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don't stop when you're tired. Stop when you're done.",
    "Little things make big days.",
    "It's going to be hard, but hard does not mean impossible.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it."
]

# Randomly pick and print 20 unique quotes
unique_quotes = random.sample(quotes, 20)
for i, quote in enumerate(unique_quotes, 1):
    print(f"{i}. {quote}")
