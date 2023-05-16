import os
import nltk.tokenize
nltk.download('punkt')

def tokenize_deutsch(text):
    return nltk.tokenize.word_tokenize(text, language='german')

def split_text_into_paragraphs(text, max_tokens=4096):
    tokens = tokenize_deutsch(text)
    paragraphs = []
    current_paragraph = []

    for token in tokens:
        current_paragraph.append(token)
        if len(current_paragraph) >= max_tokens:
            paragraphs.append(' '.join(current_paragraph))
            current_paragraph = []

    if current_paragraph:
        paragraphs.append(' '.join(current_paragraph))

    return paragraphs

def process_file(file_path, output_dir):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    paragraphs = split_text_into_paragraphs(text)

    for i, paragraph in enumerate(paragraphs):
        output_file = os.path.join(output_dir, f'paragraph_{i}.txt')
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(paragraph)

if __name__ == "__main__":
    input_file_path = '/Users/jonasb./Downloads/text.txt'
    output_directory = '/Users/jonasb./Downloads/Cowabunga Localizations v10.2.0'
    process_file(input_file_path, output_directory)