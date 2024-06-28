import pandas as pd

df = pd.read_excel('.../captions.xlsx')

words_to_search = ['ambient', 'water', 'nature', 'birds', 'noise', 'rain', 'city', 'wind', 'metal', 'people', 
          'person', 'human', 'man', 'woman', 'ambiance', 'soundscape', 'sea', 'machine', 'engine', 'car', 
          'air', 'wood', 'breath', 'traffic', 'loud', 'metal', 'glass', 'train', 'electric', 'siren', 'breeze', 
          'plastic', 'bells', 'dog', 'radio', 'gong', 'storm', 'waves', 'thunder', 'fire', 'music']

associated_sentences = {word: [] for word in words_to_search}

for index, row in df.iterrows():
    sentence = row['Selected Caption']  
    words = sentence.split()
    for word in words:
        if word in words_to_search:
            associated_sentences[word].append(sentence)

for word, sentences in associated_sentences.items():
    print(f"{word}: {len(sentences)} occurrences")
    for sentence in sentences:
        print(f"  - {sentence}")
