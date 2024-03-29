from utils.http import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(url)
        # dict json
        return result

    @classmethod
    def search_by_keyword(cls, keyword,start=0,count=15):
        url = YuShuBook.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result
