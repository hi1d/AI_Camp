from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import re
app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017/")

db = client.dbStock


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/codes', methods=['GET'])
def get_codes():
    codes_group = db.codes.distinct("group")
    codes_code = db.codes.distinct("code")
    codes_name = db.codes.distinct("name")
    doc = {
        'group': codes_group,
        'code': codes_code,
        'name': codes_name
    }

    return jsonify({'group': doc})


@app.route('/codes/search', methods=['POST'])
def codes_search():
    market_receive = request.form['market']
    sector_receive = request.form['sector']
    tag_receive = request.form['tag']
    target = list(db.stocks.find(
        {'sector': sector_receive, 'market': market_receive, 'tag': tag_receive}, {'_id': False}))

    return jsonify({'target': target})


@app.route('/show_info', methods=['POST'])
def show_info():
    code_receive = request.form['code']

    url = 'https://finance.naver.com/item/main.naver?code='+code_receive
    print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    count = soup.select_one(
        '#chart_area > div.rate_info > div > p.no_today > em > span').text
    total_count = soup.select_one(
        '#_market_sum').text
    # total = re.sub('[^0-9가-힣]+', '', total_count)
    total = total_count
    print(total)
    per = soup.select_one(
        '#tab_con1 > div:nth-child(5) > table > tbody:nth-child(2) > tr > td > em').text
    doc = {
        'count': count,
        'total_count': total,
        'per': per
    }
    return jsonify({'target': doc})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
