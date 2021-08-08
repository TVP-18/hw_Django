from django.shortcuts import render, redirect
from books.models import Book
from datetime import datetime


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'

    books = Book.objects.all()

    context = {'books': books}

    return render(request, template, context)


def books_date_view(request, year, month, day):
    template = 'books/books_date.html'

    books = Book.objects.filter(pub_date=datetime(year, month, day)).all()

    # данные для пагинации
    date_next = Book.objects.filter(pub_date__gt=datetime(year, month, day)).order_by('pub_date').first()
    date_preview = Book.objects.filter(pub_date__lt=datetime(year, month, day)).order_by('-pub_date').first()

    context = {
        'books': books,
        'page_next': get_page(date_next),
        'page_preview': get_page(date_preview),
    }

    return render(request, template, context)


def get_page(date):
    page = ''
    if date is not None:
        page = f'{date.pub_date.year}-{date.pub_date.month:02d}-{date.pub_date.day:02d}'
    return page


