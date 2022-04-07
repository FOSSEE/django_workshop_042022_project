from django.shortcuts import render, redirect

from .models import Book, BookStatus, Member
from .forms import StatusForm

def books(request):
	all_books = Book.objects.all()
	return render(
		request,
		'library_manager/books.html',
		context={'all_books': all_books}
	)

def members(request):
	all_members = Member.objects.all()
	return render(
		request,
		'library_manager/members.html',
		context={'all_members': all_members}
	)

def status(request):
	all_statuses = BookStatus.objects.all()
	return render(
		request,
		'library_manager/statuses.html',
		context={'all_statuses': all_statuses}		
	)

def new_status(request):
	if request.method == "POST":
		form = StatusForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('statuses')
		else:
			return redirect('statuses')
	else:
		form = StatusForm()
		return render(
			request,
			'library_manager/new_status.html',
			context={'form': form}
		)