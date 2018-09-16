from tkinter import *

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")

root=Tk()
textBox=Text(root, height=2, width=10)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
text = textBox.get("1.0", "end-1c");
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()
root.mainloop()

subscription_key = '2d13b660f424471bbbe96de33506de36'
assert subscription_key

sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)

https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': text}]}

  

exit();

