from flask import Flask, render_template, request
from ConfAPI import ask_question


app = Flask(__name__, template_folder='./Templates', static_folder='./Static')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    raw_msg = request.get_json()
    # print(f"{msg}")
    msg = raw_msg.get('data')
    # print(f"{msg}")
    res = ask_question(msg)
    response = {'response': True,
                'message': res}
    return response


if __name__ == '__main__':
    app.run()