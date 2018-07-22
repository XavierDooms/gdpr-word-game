from flask import Flask
from wordpuzzle import WordPuzzle
app = Flask(__name__)

@app.route('/')
def index():
    html_string = "<html>\n"
    html_string += "<head><style>body { font-family: Courier; }</style></head>\n"
    html_string += "<body>\n"
    html_string += "<h1>Find \"GDPR\"</h1>\n"
    html_string += "<div>\n"
    html_string += matrix_to_string(create_checked_matrix(10,30))
    html_string += "</div>\n"
    html_string += "<div hidden>\n"
    html_string += "Location: {}\n".format(get_solution())
    html_string += "</div>\n"
    html_string += "\n</body>\n</html>"

    return html_string

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