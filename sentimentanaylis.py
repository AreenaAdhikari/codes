from transformers import pipeline
classifier = pipeline("sentiment-anaylsis")
text = "I LOVE HUGGING FACE API "
result = classifier(text)
print("Sentiment:",result)

