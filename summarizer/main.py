import tkinter as tk
import nltk 
#nltk is a natural language processing toolkit
from textblob import TextBlob
#THis is for sentimental analysis
from newspaper import Article


def summarize():

    url = utext.get('1.0', "end").strip()

    ar = Article(url)

    ar.download()
    ar.parse()
    ar.nlp()
    # ALl natural language processing libraries are doing heavy lifting for us
    #nothing fancy

    title.config(state='normal')
    author.config(state='normal')
    publish.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', ar.title)

    author.delete('1.0', 'end')
    author.insert('1.0', ar.authors)

    publish.delete('1.0', 'end')
    publish.insert('1.0', ar.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', ar.summary)


    # NOw sentimental analysys part -
    analysis = TextBlob(ar.text)

    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publish.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


def clear_fields():
    title.delete('1.0', 'end')
    author.delete('1.0', 'end')
    publish.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')
    utext.delete('1.0', 'end')

# # NOw we will build a GUI using TK 

root = tk.Tk()
root.title("Post Summarizer")
root.geometry('1200x650')

tlable = tk.Label(root, text = "TITLE")
tlable.pack()

title = tk.Text(root, height = 1, width=140)
title.config(state='disabled', bg='black' , foreground="white")
title.pack()

alable = tk.Label(root, text = "AUTHOR")
alable.pack()

author = tk.Text(root, height = 1, width=140)
author.config(state='disabled', bg='black' , foreground="white")
author.pack()

plable = tk.Label(root, text = "PUBLISHING DATE")
plable.pack()

publish = tk.Text(root, height = 1, width=140)
publish.config(state='disable', bg='black' , foreground="white")
publish.pack()

slable = tk.Label(root, text = "SUMMARY")
slable.pack()

summary = tk.Text(root, height = 20, width=140)
summary.config(state='disabled', bg='black' , foreground="white")
summary.pack()


selable = tk.Label(root, text = "SUMMARY")
selable.pack()

sentiment = tk.Text(root, height = 1, width=140)
sentiment.config(state='disabled', bg='black' , foreground="white")
sentiment.pack()

ulable = tk.Label(root, text = "ENTER URL HERE")
ulable.pack()

utext = tk.Text(root, height = 1, width=140)
utext.pack()


btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()


btn_clear = tk.Button( text="Clear", command=clear_fields, font=('Helvetica', 14, 'bold'))
btn_clear.pack()


root.mainloop()
