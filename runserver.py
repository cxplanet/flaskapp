from flaskapp import app

# Note: NEVER RUN WITH DEBUG AS TRUE IN PRODUCTION. IT
# ALLOWS CODE INJECTION TO OCCUR

app.debug = True
app.run(host='0.0.0.0')
