# Run a test server.
from flask import Flask, jsonify

from simple_page.models import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

# @app.route('/')
# def hello_world():
#     return '''<!DOCTYPE html>
#             <html>
#             <head>
#             <style>
#             table, th, td {
#                 border: 1px solid black;
#             }
#             </style>
#             </head>
#             <body>
#
#             <table style="width:100%">
#               <tr>
#                 <td>Jill</td>
#                 <td>Smith</td>
#                 <td>50</td>
#               </tr>
#               <tr>
#                 <td>Eve</td>
#                 <td>Jackson</td>
#                 <td>94</td>
#               </tr>
#               <tr>
#                 <td>John</td>
#                 <td>Doe</td>
#                 <td>80</td>
#               </tr>
#                 <tr>
#                 <td>Alok</td>
#                 <td>Nath</td>
#                 <td>30</td>
#               </tr>
#                   <tr>
#                 <td>Shekhar</td>
#                 <td>Gupta</td>
#                 <td>26</td>
#               </tr>
#             </table>
#
#             </body>
#             </html>
#             '''


from flask import request, Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)


@app.route('/json')
def some_json_returner():
    print request
    return jsonify({}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
