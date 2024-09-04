from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    data_dir = 'data'  # 데이터 파일들이 위치한 디렉토리
    data_list = []

    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    region = lines[0].strip()
                    location = lines[1].strip()
                    data_list.append({'region': region, 'location': location})

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True)
