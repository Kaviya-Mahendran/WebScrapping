import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# --- Step 1: Load CSV ---
csv_file = "Pennsylvania.csv"  # your CSV file name
df = pd.read_csv(csv_file)


print("Columns in CSV:", df.columns)
print(df.head())

# --- Step 2: Clean and Analyze Text ---
purpose_column = 'Category'  # Column describing charity purpose

# Combine all text
all_text = ' '.join(df[purpose_column].dropna().astype(str)).lower()

# Remove punctuation and stop words
stop_words = {"a", "an", "the", "in", "for", "to", "and", "of", "with",
              "on", "is", "by", "its", "or", "from", "that"}
cleaned_text = re.sub(r'[^a-z\s]', '', all_text)
words = [w for w in cleaned_text.split() if w not in stop_words and len(w) > 2]

# Count word frequency
word_counts = Counter(words)
top_words = word_counts.most_common(10)

print("\nTop 10 words in charity categories:")
for word, count in top_words:
    print(f"- {word}: {count}")

# --- Step 3: Saving cleaned CSV ---
cleaned_csv_path = "charities_cleaned.csv"
df.to_csv(cleaned_csv_path, index=False)
print(f"\nCleaned CSV saved as '{cleaned_csv_path}'")

# --- Step 4: Bar Chart ---
words_bar, counts_bar = zip(*top_words)
plt.figure(figsize=(8,5))
plt.bar(words_bar, counts_bar, color='skyblue')
plt.title('Top 10 Words in Pennsylvania Charity Categories')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
bar_chart_path = "charity_word_freq.png"
plt.savefig(bar_chart_path)
plt.show()
print(f"Bar chart saved as '{bar_chart_path}'")

# --- Step 5: Optional Word Cloud ---
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
wordcloud_path = "charity_wordcloud.png"
plt.savefig(wordcloud_path)
plt.show()
print(f"Word Cloud saved as '{wordcloud_path}'")
