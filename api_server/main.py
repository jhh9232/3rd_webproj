import webcrawl as wc
from flask import Flask
from flask_cors import CORS
import json

FINAL_URL = "http://www.jobkorea.co.kr/recruit/joblist?menucode=duty"

#CNT = 1~17
# newcomers = {
#     "web":[], #1            웹프로그래머
#     "application":[], #2    응용프로그래머
#     "system":[], #3         시스템 프로그래머
#     "database":[], #4       DBA 데이터베이스
#     "network":[], #5        네트워크, 서버, 보안
#     "webplan":[], #6        웹기획 PM
#     "webmarketing":[], #7   웹마케팅
#     "contents":[], #8       컨텐츠, 사이드운영
#     "htmlui":[], #9         HTML, 퍼블리싱, UI개발
#     "webdesign":[], #10     웹디자인
#     "tester":[], #11        QA테스터, 검증
#     "game":[], #12          게임
#     "erp":[], #13           ERP, 시스템 설계 및 분석
#     "teacher":[], #14       IT, 디자인, 컴퓨터 강사
#     "video":[], #15         동영상제작, 편집
#     "bigdata_ai":[], #16    빅데이터, 인공지능(AI)
#     "sw_hw":[], #17         소프트웨어 하드웨어
# }


app = Flask(__name__)
CORS(app)
newcomers=[]
@app.route('/', methods=['GET'])
def get_world():
    news=[]
    for i in range(1, 18):
        news += newcomers[i]
    print(len(news))
    
    return json.dumps(news, ensure_ascii=False)

@app.route('/web', methods=['GET'])
def web():
    return json.dumps(newcomers[1], ensure_ascii=False)

@app.route('/application', methods=['GET'])
def application():
    return json.dumps(newcomers[2], ensure_ascii=False)

@app.route('/system', methods=['GET'])
def system():
    return json.dumps(newcomers[3], ensure_ascii=False)

@app.route('/database', methods=['GET'])
def database():
    return json.dumps(newcomers[4], ensure_ascii=False)

@app.route('/network', methods=['GET'])
def network():
    return json.dumps(newcomers[5], ensure_ascii=False)

@app.route('/webplan', methods=['GET'])
def webplan():
    return json.dumps(newcomers[6], ensure_ascii=False)

@app.route('/webmarketing', methods=['GET'])
def webmarketing():
    return json.dumps(newcomers[7], ensure_ascii=False)

@app.route('/contents', methods=['GET'])
def contents():
    return json.dumps(newcomers[8], ensure_ascii=False)

@app.route('/htmlui', methods=['GET'])
def htmlui():
    return json.dumps(newcomers[9], ensure_ascii=False)

@app.route('/webdesign', methods=['GET'])
def webdesign():
    return json.dumps(newcomers[10], ensure_ascii=False)

@app.route('/tester', methods=['GET'])
def tester():
    return json.dumps(newcomers[11], ensure_ascii=False)

@app.route('/game', methods=['GET'])
def game():
    return json.dumps(newcomers[12], ensure_ascii=False)

@app.route('/erp', methods=['GET'])
def erp():
    return json.dumps(newcomers[13], ensure_ascii=False)

@app.route('/teacher', methods=['GET'])
def teacher():
    return json.dumps(newcomers[14], ensure_ascii=False)

@app.route('/video', methods=['GET'])
def video():
    return json.dumps(newcomers[15], ensure_ascii=False)

@app.route('/bigdata_ai', methods=['GET'])
def bigdata_ai():
    return json.dumps(newcomers[16], ensure_ascii=False)

@app.route('/sw_hw', methods=['GET'])
def sw_hw():
    return json.dumps(newcomers[17], ensure_ascii=False)

@app.errorhandler(404)
def not_found(error):
    return "{}"



if __name__ == '__main__':
    newcomers = wc.Parse_Job(FINAL_URL)
    app.run(host='0.0.0.0', port=5505)

#print(newcomers)
