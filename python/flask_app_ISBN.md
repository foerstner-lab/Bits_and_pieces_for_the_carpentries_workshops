## Simple flask example

- https://flask.palletsprojects.com


```shell
python -m pip install Flask
```

```shell
mkdir isnb_app
cd isnb_app
```

```isnb_app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_page():
    return "<p>Hello World!</p>"
```

```shell
export FLASK_APP=isbn_app.py
```


```shell
python -m flask run
```

Open http://127.0.0.1:5000/


```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_page():
    return "<p>Hello World!</p>"

@app.route("/info") # Information page
def show_info():
    return "<p>Some information.</p>"
```

Stop flask wit Ctrl-C

```shell
python -m flask run
```

- Open http://127.0.0.1:5000/
- Open http://127.0.0.1:5000/info
- Stop flask wit Ctrl-C

```shell
export FLASK_ENV=development
```

```shell
python -m flask run
```
- https://snarky.ca/why-you-should-use-python-m-pip/
- https://docs.python.org/3/using/cmdline.html#cmdoption-m

```isnb_app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_page():
    return "<p>Hello World!</p>"

@app.route("/info")
def show_info():
    return "<p>Some information.</p>"

@app.route("/isbn")
def isbn_display():
    return "<p>Your ISBN: </p>"
```

- https://docs.python.org/3/library/__main__.html
- Open http://127.0.0.1:5000/isbn

```isnb_app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_page():
    return "<p>Hello World!</p>"

@app.route("/info")
def show_info():
    return "<p>Some information.</p>"

@app.route("/isbn/<isbn>")
def isbn_display(isbn):
    return "<p>Your ISBN:" + isbn + "</p>"
```

- Open http://127.0.0.1:5000/isbn/8484-499
- Open http://127.0.0.1:5000/isbn/444-4444
- Read https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing

```shell
mkdir templates
```

```templates/isbn.html
<!DOCTYPE html>
<html>
<body>

<h1>ISBN check</h1>

<p>Your ISBN: </p>

</body>
</html> 
```

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start_page():
    return "<p>Hello World!</p>"

@app.route("/info")
def show_info():
    return "<p>Some information.</p>"

@app.route("/isbn/<isbn>")
def isbn_display(isbn):
    return render_template("isbn.html")
```

TBC
