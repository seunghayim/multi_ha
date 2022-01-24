from flask import Flask
import json, requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/data1/')
def FlaskData():
    keyValue = r"V6lQYKtQODdLI8HPFUM%2FF1fi2FGeE%2FbXr142ghKq1Vfzozi42DXMWVzP9Hp9GI%2FI%2F1%2BbUud5Pa4JVwsu653Y8Q%3D%3D"
    address = r"%EC%A4%91%EB%9E%91%EA%B5%AC"
    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += f"page=1&perPage=10"
    dataURL += f"&cond%5BorgZipaddr%3A%3ALIKE%5D={address}"
    dataURL += f"&serviceKey={keyValue}"
    
    dataResult = requests.get(dataURL)
    return json.loads(str(dataResult))


if __name__ == "__main__":
    app.run(debug=True)
 

데이터 안나옵니다..
