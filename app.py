from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

from flask import Flask, jsonify, render_template
import os
import re  # 정규 표현식 모듈

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
                for line in file:  # 각 줄을 읽고
                    line = line.strip()  # 공백 제거
                    # 정규 표현식으로 괄호 안과 밖의 내용을 분리
                    match = re.match(r'\[(.*?)\](.*?)\s+(\S+)\s+(\S+)', line)
                    if match:  # 정규 표현식 매칭 성공 시
                        location = match.group(1)  # 괄호 안의 내용
                        region = match.group(2).strip()  # 괄호 밖의 내용 (좌측)
                        time = match.group(3)  # 시간
                        URL = match.group(4)  # URL
                        data_list.append({'region': region, 'location': location, 'time': time, 'URL': URL})

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True)
