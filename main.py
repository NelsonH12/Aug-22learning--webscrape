import pandas as pd
Simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)")
print(Simpsons [2])