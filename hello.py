from flask import Flask
from wordpuzzle import WordPuzzle
app = Flask(__name__)

@app.route('/')
def index():
    return word("GDPR")

@app.route('/word/<word>')
def word(word):
    puzzle = WordPuzzle(10,10,word)

    html_string = "<html>\n"
    html_string += "<head><style>body { font-family: Courier; }</style></head>\n"
    html_string += "<body>\n"
    html_string += "<h1>Find \"{}\"</h1>\n".format(word)
    html_string += "<div id=\"puzzle-div\">\n"
    html_string += puzzle.html_string()
    html_string += "</div>\n"
    html_string += "<div  id=\"solution-div\" hidden>\n"
    html_string += "Location: {}\n".format(puzzle.solution)
    html_string += "</div>\n"
    html_string += "\n</body>\n</html>"

    return html_string