from flask import Flask, request
from api import get_recom

# get_recom("full stack wev developer")
app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/search_course/', methods=['POST','GET'])
def search():
    print("hi")
    # print(request.args.get("title"))
    title = request.args.get('title')
    # print(request)
    # print(title)
    ans = str(get_recom(title))
    return ans

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)