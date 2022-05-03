from uuid import uuid4

from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=255, unique=True, default=uuid4)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    active = models.BooleanField(default=True)
    last_used_at = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return f"Token {self.token}, active: {self.active}"

    def __repr__(self):
        return self.__str__()
