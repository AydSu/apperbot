# pip install -U spacy
# python -m spacy download en_core_web_sm

#example of run. python myprogram.py input.txt output.html
from sys import stdin, argv
import spacy

input_text = ''

with open(argv[1]) as f:
    input_text = f.read()
    
input_text = input_text.replace('/', ' ')

nlp = spacy.load("en_core_web_sm")
doc = nlp(input_text)

texts = []
poses=[]

for token in doc:
    texts.append(token.text)
    poses.append(token.pos_)

counter_dict = {}

for text, pos in zip(texts, poses):
    if (pos == 'NUM' or pos == 'PROPN'):
        value = int(counter_dict.get(text) or 0)
        counter_dict.update({text: value + 1})

print(counter_dict)

html = """
<!DOCTYPE html>
<html>
<body>

%insert%

</body>
</html>
"""

insert = ''
for key in counter_dict.keys():
    insert += f'<h1 style="text-align:right;">{key}: {counter_dict[key]}</h1> \n'

html = html.replace('%insert%', insert)

with open(argv[2], 'w') as f:
    f.write(html)
