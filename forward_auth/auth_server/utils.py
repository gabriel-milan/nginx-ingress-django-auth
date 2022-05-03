from os import getenv

from django.http import HttpRequest

from forward_auth.auth_server.models import Token


def get_public_uri() -> str:
    """
    Get the public URI.

    Returns:
        The public URI.
    """
    return getenv("DJANGO_AUTH_PUBLIC_URI", "")


def get_redirect_uri(request: HttpRequest, default: str = None) -> str:
    """
    Get the redirect_uri from the request.

    Args:
        request: The request object.
        default: The default value to return if the redirect_uri is not found.

    Returns:
        The redirect_uri from the request.
    """
    # First we try to get the redirect_uri from the request headers.
    redirect_uri = request.headers.get("X-Original-Url")

    # Then we try to get from the URL parameters
    if redirect_uri is None:
        redirect_uri = request.GET.get("rd", None)

    # If the redirect_uri is still not in the request, we try to get it
    # from the default value.
    if redirect_uri is None:
        redirect_uri = default

    # We return the redirect_uri.
    return redirect_uri


def is_authenticated(request: HttpRequest) -> bool:
    """
    Check if the user is authenticated either through sessions
    or Bearer token.

    Args:
        request: The request object.

    Returns:
        True if the user is authenticated, False otherwise.
    """
    if request.user.is_authenticated:
        return True
    token = request.headers.get("Authorization")
    if token is not None:
        try:
            token = token.split("Bearer ")[1]
            token_obj: Token = Token.objects.get(token=token)
            if token_obj.active:
                return True
        except Token.DoesNotExist:
            return False
        except IndexError:
            return False
    return False
