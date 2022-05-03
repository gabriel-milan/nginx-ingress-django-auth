from django.contrib import admin

from forward_auth.auth_server.models import Token

admin.site.register(Token)
