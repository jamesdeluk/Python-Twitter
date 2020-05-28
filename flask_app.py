from flask import Flask, request
import tweepy
from peredutwitter_flask import tweepysearch

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def tweeptweep():
    if request.method == "POST":
        search = None
        number = None
        search = request.form["search"]
        number = request.form["number"]
        result = tweepysearch(search, number)
        return '''
            <html>
                <body>
                    <p>{result}</p>
                    <p><a href="/">Again</a>
                </body>
            </html>
        '''.format(result=result)

    return '''
        <html>
            <body>
                <p>Enter your numbers:</p>
                <form method="post" action=".">
                    <p><input name="search" /></p>
                    <p><input name="number" /></p>
                    <p><input type="submit" value="Search" /></p>
                </form>
            </body>
        </html>
    '''