from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Book, Genre
from .forms import BookForm

def book_list(request):
    search_query = request.GET.get('q', '')
    genre_filter = request.GET.get('genre', '')
    page_number = request.GET.get('page', 1)

    books = Book.objects.select_related('genre').all()
    
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) | 
            Q(author__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    if genre_filter:
        books = books.filter(genre__name=genre_filter)

    # Pagination
    paginator = Paginator(books, 12)  # Show 12 books per page
    page_obj = paginator.get_page(page_number)

    genres = Genre.objects.all()
    context = {
        'books': page_obj,
        'genres': genres,
        'search_query': search_query,
        'genre_filter': genre_filter,
    }
    return render(request, 'books/book_list.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
