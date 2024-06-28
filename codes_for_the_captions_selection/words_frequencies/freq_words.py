import pandas as pd
from collections import Counter
import re
import json


df = pd.read_excel('.../clotho_captions_evaluation.xlsx') # path captions file

df = df.iloc[:, 1:]

word_counter = Counter()

for index, row in df.iterrows():
    for col in df.columns[0:]:  
        caption = str(row[col])  
        words = re.findall(r'\b\w+\b', caption.lower())
        word_counter.update(words)
        print("counted column: ", col)
    print("counted row: ", index)

word_freq_dict = dict(word_counter)

df = pd.DataFrame(list(word_freq_dict.items()), columns=['Parola', 'Frequenza'])

df.to_excel('word_freq.xlsx', index=False)

print("File Excel saved as 'word_freq.xlsx'")
