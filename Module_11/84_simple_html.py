from bs4 import beautifulSoup

# Parsing is a programing term for understanding something that has a structure

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1> this is a title </h1>
<p class="subtitle"> text here with class.</p>
<p></p>
<ul>
     <li>Rolf</li>
     <li>charlie</li>
     <li>Jen</li>
     <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = beautifulSoup(SIMPLE_HTML, 'html.parser') # HTML parser is all the document

print(simple_soup.find('h1'))
print(simple_soup.find('h1').string)


def find_title():
     h1_tag = simple_soup.find(h1)
     print(h1_tag.string)

def find_list_items():
     list_items = simple_soup.find_all('li')
     list_contents = [e.string for w in list_items]
     print(list_items)     

def find_paragraph():
     paragraph = simple_soup.find('p', {'class': 'subtitle'})
     print(paragraph.string)


def find_other_paragraph():
     paragraphs = simple_soup.find_all('p')
     other_paragraphs = [p for p in paragraphs if 'subtle' not in p.atrrs.get('class', [] )]
     print(other_paragraphs[0].string)




find_title()
find_list_items()
find_paragraph()
find_other_paragraph()