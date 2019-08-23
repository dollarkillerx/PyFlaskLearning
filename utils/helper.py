def is_isbn(q):
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    qs = q.replace('-', '')
    if '-' in q and len(qs) == 10 and qs.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
