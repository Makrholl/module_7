class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                low = file.read().lower()
                for i in punctuation:
                    low = low.replace(i, "")
                words = low.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        word_positions = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            position = words.index(word)+1
            word_positions[file_name] = position

        return word_positions

    def count(self, word):
        word = word.lower()
        word_counts = {}

        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('text'))  # Найти позицию слова "text"
print(finder2.count('text'))  # Подсчитать количество слова "text"
