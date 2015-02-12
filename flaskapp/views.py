from flaskapp import app
from flask import render_template

@app.route('/')
def index():
    return 'Welcome Page!'

@app.route('/svgtest')
def svgtest():
	return '''
<!DOCTYPE html>
<html>
<body>

<svg height="100" width="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  Sorry, your browser does not support inline SVG.  
</svg> 
 
</body>
</html>'''

@app.route('/evoart')
def svgtest2():
	svg='<circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="blue" />'
	return render_template('evoart.svg', svg=svg)
