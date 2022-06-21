import pandas as pd

python = pd.read_html('https://en.wikipedia.org/wiki/Python_(programming_language)')

print(len(python))
