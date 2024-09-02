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