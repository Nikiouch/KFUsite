from django.template import Library
from django.core.urlresolvers import resolve
import string
register = Library()
@register.filter
def is_current_page_view(request, page):
	view_name = resolve(request.path).view_name.split('.').pop() # Полное имя - вместе с именем приложения, что не очень
	# print(name)
	return view_name == page