from os import getenv

from django.http import HttpRequest, HttpResponse


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
    # First we try to get the redirect_uri from the request.
    redirect_uri = request.headers.get("X-Original-Url")

    # If the redirect_uri is still not in the request, we try to get it
    # from the default value.
    if redirect_uri is None:
        redirect_uri = default

    # We return the redirect_uri.
    return redirect_uri
