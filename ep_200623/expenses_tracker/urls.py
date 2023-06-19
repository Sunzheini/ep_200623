from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from ep_200623.expenses_tracker.views import index_with_profile, index_no_profile, \
    create_expense, edit_expense, delete_expense, \
    profile, edit_profile, delete_profile


"""
•	http://localhost:8000/ - home page
•	http://localhost:8000/create/ - create expense page
•	http://localhost:8000/edit/<id>/ - edit expense page
•	http://localhost:8000/delete/<id>/ - delete expense page
•	http://localhost:8000/profile/ - profile page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - delete profile page
"""


urlpatterns = [
    path('', index_with_profile, name='index with profile'),
    path('no-profile/', index_no_profile, name='index no profile'),

    path('create-expense/', create_expense, name='create expense'),
    path('edit-expense/<int:pk>/', edit_expense, name='edit expense'),
    path('delete-expense/<int:pk>/', delete_expense, name='delete expense'),

    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
