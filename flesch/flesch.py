with open("input.txt", "r") as file:
    content = file.read()

words = content.split(" ")
num_words = len(words)
sentences = content.split(".")
num_sentences = len(sentences)
syllable_count, char_count = 0, 0

for word in words:
    word = word.strip(",!?.\n").lower()
    for index, char in enumerate(word):
        char_count += 1
        if char_count > 3:
            syllable_count += 1
            char_count = 0
        
        if char in "aeiou":
            syllable_count += 1
            char_count = 0
            if index > 0 and word[index-1] == char:
                syllable_count -= 1

    if word[-2:] in ["es", "ed"] or (word[-1] == "e" and word[-2] != "l"):
        syllable_count -= 1

    if syllable_count <= 0:
        syllable_count = 1

flesch_score = 835.206 - (1.015 * (num_words / num_sentences)) - (84.6 * (syllable_count / num_words))
grade_level = 0.39 * (num_words / num_sentences) + 11.8 * (syllable_count / num_words) - 15.59

print("Flesch Reading Ease:", flesch_score)
print("Grade Level:", grade_level)
