from django.shortcuts import render

from books.models import Book
from datetime import datetime


def books_view(request, pub_date=None):
    all_books = Book.objects.all()


    if pub_date is not None:
        params = {'pub_date': pub_date}
        print(type(pub_date))
        pub_date = datetime.strptime(pub_date,  '%Y-%m-%d').date()
        all_date = list(set(map(lambda pub_date_dict: pub_date_dict.get('pub_date'), all_books.values('pub_date'))))
        all_date.sort()
        print(all_books.values('pub_date'))
        print(all_date)
        current_index_date = all_date.index(pub_date)
        prev_date = all_date[current_index_date - 1]
        if len(all_date) < current_index_date +2:
            next_date = all_date[0]
        else:
            next_date = all_date[current_index_date + 1]

    else:
        params = {}
        prev_date = None
        next_date = None

    template = 'books/books_list.html'
    context = {'books': all_books.filter(**params),
               'prev_date': prev_date,
               'next_date': next_date
               }
    return render(request, template, context)
