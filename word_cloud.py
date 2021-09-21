import sys, os
import wordcloud
os.chdir(sys.path[0])
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# stopword_id
stopwords_id = StopWordRemoverFactory().get_stop_words()

# read text
df = pd.read_feather(r"C:\Users\ROG\Documents\akosta\df_clean.feather")
text = df["text"].str.encode("utf-8")

wc = WordCloud(
    background_color="white",
    stopwords=stopwords_id,
    height=800,
    width=600
)


wc.generate(text)

wc.to_file("wc_output.png")

print(text)

