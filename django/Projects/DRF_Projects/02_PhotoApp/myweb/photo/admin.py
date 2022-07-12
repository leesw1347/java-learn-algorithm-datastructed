from django.contrib.admin import site

from .models import Photo

# Register your models here.

# 모델을 등록해준다
# 어드민 페이지에 Photo 모델을 등록한다
site.register(Photo)
