from flask import Flask
from matrixgenerator import create_checked_matrix, matrix_to_string, get_solution
app = Flask(__name__)

@app.route('/')
def index():
    html_string = "<html>\n"
    html_string += "<head><style>body { font-family: Courier; }</style></head>\n"
    html_string += "<body>\n"
    html_string += "<h1>Find \"GDPR\"</h1>\n"
    html_string += "<div>\n"
    html_string += matrix_to_string(create_checked_matrix(10,10))
    html_string += "</div>\n"
    html_string += "<div hidden>\n"
    html_string += "Location: {}\n".format(get_solution())
    html_string += "</div>\n"
    html_string += "\n</body>\n</html>"

    return html_string

@app.route('/hello')
def hello():
    return 'Hello, World'