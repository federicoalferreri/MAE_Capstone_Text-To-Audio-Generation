import pandas as pd
from collections import Counter
import re

word_freq_df = pd.read_excel('word_freq_final.xlsx')

word_freq_dict = dict(zip(word_freq_df['Parola'], word_freq_df['Frequenza']))
print(word_freq_dict)

df = pd.read_excel('.../clotho_captions_evaluation.xlsx') # path captions file

def calculate_caption_score(caption, word_freq_dict):
    words = caption.split()
    score = sum(word_freq_dict.get(word, 0) for word in words)
    return score

selected_captions = []

for index, row in df.iterrows():
    max_score = 0
    selected_caption = None
    for col in range(1, 6):
        caption = row[col]
        caption_score = calculate_caption_score(caption, word_freq_dict)
        if caption_score > max_score:
            min_score = caption_score
            selected_caption = caption
    selected_captions.append(selected_caption)
    

selected_df = pd.DataFrame({'file_name': df[df.columns[0]], 'Selected Caption': selected_captions})

selected_df.to_excel('captions.xlsx', index=False)

print("Selected captions  saved as 'captions.xlsx'")


