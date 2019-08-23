'''
    Create By DollarKiller
'''
from flask import Flask, jsonify
from config import conf
from utils.helper import is_isbn
from controller.yushu_book import YuShuBook

app = Flask(__name__)


@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
    :param q: 普通关键字 isbn
    :param page: 分页
    :return:
    '''
    # isbn 13 13个0~9的数值组成
    # isbn10 10个0~9数字组成 包含一些 '-'
    isbn_or_key = is_isbn(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q,page)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=conf.DEBUG)
