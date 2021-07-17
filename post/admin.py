from django.contrib import admin
from .models import (
	Post,
	IPAddress,
	Comment,
)


admin.site.register(Post)
admin.site.register(IPAddress)