from django.contrib import admin
from .models import Trail
from .models import User
from .models import UserHike
# from .models import Post

# Register your models here.
admin.site.register(Trail)
admin.site.register(User)
admin.site.register(UserHike)

# admin.site.register(Post)
