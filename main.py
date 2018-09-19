from flask import Flask, request
from caesar import rotate_string
app = Flask(_name_)
app.config ['DEBUG']= True
form = """<!DOCTYPE html>

        <html>
            <head>
                <style>
                    form {
                        background-color: #eee;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        font: 16px sans-serif;
                        border-radius: 10px;
                    }
                    textarea {
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }
                </style>
            </head>
            <body>
                <form method ='POST'>
                    <label>type=text 
                        <input name="TEXT" type="text"/>
                    </label> 
                    <br>
                    <label>type=text 
                        <input name'"Rotate By" type="text"/>
                    </label>
                    <br>
                    
            </body>
        </html>"""

@app.route("/")
def index ():
    return form.format("")

@app.route("/")
def encrypt ():
    return form.format (rotate_string(text,rot))
app.run()