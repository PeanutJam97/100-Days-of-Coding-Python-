import pandas as pd

data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")

print(data_dict)

data_dict.remove(data_dict[1])

df = pd.DataFrame(data_dict)
df.to_csv(".\data\words_to_learn.csv", index=False)