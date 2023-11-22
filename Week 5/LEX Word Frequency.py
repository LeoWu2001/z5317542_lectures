# Create a function to find the most common word and its frequency in a text file

def most_common(file_path):
    # Context manager
    with open(file_path) as file:
        # Counting word frequency
        counts = dict()
        for line in file:
            # Analysing each line and splitting the line into individual words
            words = line.split()

            for word in words:
                # Counting the individual words from each line
                counts[word] = counts.get(word,0) + 1

        # Finding the most frequent word
        max_count = None
        max_word = None

        for word, count in counts.items():
            if max_count is None or count > max_count:
                max_word = word
                max_count = count

        return (f"The most frequent word was {max_word}, which appeared {max_count} times")
