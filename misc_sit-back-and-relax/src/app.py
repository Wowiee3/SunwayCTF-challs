from flask import Flask, Response, render_template

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


@app.route('/', defaults={'path': ''}, methods=['BREW'])
@app.route('/<path:path>', methods=['BREW'])
def flag(path):
    return Response(render_template('index.html', flag=True), status=418)

@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def hint(path):
    return Response("Quite close! But it is deprecated, RFC 2324.", status=503)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1338)
