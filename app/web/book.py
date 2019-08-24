from flask import jsonify, request
from app.forms.book import SearchForm

from app.controller.yushu_book import YuShuBook
from utils.helper import is_isbn

from . import web


# 注册蓝图


@web.route('/book/search')
def search():
    '''
    :param q: 普通关键字 isbn
    :param page: 分页
    :return:
    '''
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        # isbn 13 13个0~9的数值组成
        # isbn10 10个0~9数字组成 包含一些 '-'
        isbn_or_key = is_isbn(form.q.data)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(form.q.data)
        else:
            result = YuShuBook.search_by_keyword(form.q.data, form.page.data)
        return jsonify(result)
    else:
        return jsonify(form.errors), 400
