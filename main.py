from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form method='POST'>
        <label for="rotation">Rotate by:</label>
            <input type="text" name="rot" value="0" id="rotation">
            <textarea name="text">{0}</textarea>
        <input type="submit" value="submit"> 
    </form>   
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")
@app.route("/", methods=['post'])
def encrypt():
    text= request.form['text']
    rot= int(request.form['rot'])
    encrypted_string=rotate_string(text, rot)
    return form.format(encrypted_string)

app.run()