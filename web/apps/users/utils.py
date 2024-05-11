from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .repository import UserRepository
from .services import UserService

user_service = UserService(UserRepository())


@require_http_methods(['GET'])
def check_username(request):
    username = request.GET.get('value')
    is_available: bool = user_service.check_username_availability(username)
    return JsonResponse({'is_available': is_available})


@require_http_methods(['GET'])
def check_email(request):
    email = request.GET.get('value')
    is_available: bool = user_service.check_email_availability(email)
    return JsonResponse({'is_available': is_available})
