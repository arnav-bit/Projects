from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
def  word_cloud(data,bgcolor,title):
    plt.figure(figsize = (10,10))
    with open('words.txt') as f:
        stopwords = f.read().split(" ")
    my_stopwords = set(STOPWORDS)
    my_stopwords.update(stopwords)
    word_cloud = WordCloud(stopwords= my_stopwords,collocations=False,background_color = bgcolor, max_words = 200,  max_font_size = 50)
    word_cloud.generate(' '.join(data))
    plt.imshow(word_cloud)
    plt.axis('off')

def word_count(str):
    counts = dict()
    words=str
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def entries_to_remove(entries, repeated_words):
    for key in entries:
        if key in repeated_words:
            del repeated_words[key]
