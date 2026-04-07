def word_count_file(input_file, output_file):
    word_count = {}
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for word in line.split():
                word_count[word] = word_count.get(word, 0) + 1

    with open(output_file, 'w') as f:
        for word, count in word_count.items():
            f.write(f"{word}: {count}\n")

if __name__ == "__main__":
    word_count_file("data/input.txt", "outputs/output.txt")
