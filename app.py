from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test_api():
    if request.method == 'GET':
        # 返回一个简单的消息
        return jsonify({'message': 'GET 请求成功！', 'data': '这里可以放一些数据'})

        # 如果是POST请求
    elif request.method == 'POST':
        # 获取JSON数据
        data = request.json
        print(f'getData {data}')
        # 返回接收到的数据，以及一个确认消息
        return jsonify({'message': 'POST 请求成功！', 'received_data': data})

        # 其他请求类型处理（可选）
    else:
        return jsonify({'message': '不支持的请求类型'})


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
