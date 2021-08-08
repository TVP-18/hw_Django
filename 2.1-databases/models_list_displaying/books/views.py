from django.shortcuts import render, redirect
from books.models  import Book
from datetime import datetime

def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'

    books = Book.objects.all()

    context = {'books': books}

    return render(request, template, context)


def books_date_view(request, year, month, day):
    template = 'books/books_list.html'

    books = Book.objects.filter(pub_date=datetime(year, month, day)).all()

    date_next = Book.objects.filter(pub_date__gt=datetime(year, month, day)).order_by('pub_date').first()

    context = {
        'books': books,
        'date_next': date_next,
    }

    return render(request, template, context)