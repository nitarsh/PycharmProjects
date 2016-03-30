from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
}
</style>
</head>
<body>

<table style="width:100%">
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Doe</td>
    <td>80</td>
  </tr>
    <tr>
    <td>Alok</td>
    <td>Nath</td>
    <td>30</td>
  </tr>
      <tr>
    <td>Shekhar</td>
    <td>Gupta</td>
    <td>26</td>
  </tr>
</table>

</body>
</html>
'''




if __name__ == '__main__':
    app.run()
