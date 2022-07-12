import django.core.handlers.wsgi
from django.shortcuts import render , get_object_or_404 , redirect

# 데이터베이스에서 데이터를 꺼내 템플릿으로 전달하기도 하지만, 템플릿을
# 보이게 하는 역할도 수행한다.
from photo.forms import PhotoForm
from photo.models import Photo


# Create your views here.

def photo_list(request: django.core.handlers.wsgi.WSGIRequest):
    photos = Photo.objects.all()  # Django ORM 기능을 통해서 Photo 클래스 내 있는 데이터를 전부 가져온다
    # print(photos)
    return render(request=request ,
                  template_name="photo/photo_list.html" ,
                  context={
                      "photos": photos
                  })


# photo_detail.html을 렌더링해주기 위해서 사용하는 뷰함수
def photo_detail(request: django.core.handlers.wsgi.WSGIRequest , pk: int):
    """
    get_object_or_404() 는 모델로부터 데이터를 찾아보고 만약 찾는 데이터가 없다면 404 에러를 반환한다
    :param request: django request client 객체
    :param pk: 찾으려는 model의 pk id
    :return:
    """
    photo = get_object_or_404(klass=Photo , pk=pk)  # photo_detail로 들어오면 여기서 처리한다
    return render(request=request ,
                  template_name="photo/photo_detail.html" ,
                  context={
                      "photo": photo
                  })


# forms.py를 활용해서 포스트를 작성하는 기능을 작성한다
def photo_post(request: django.core.handlers.wsgi.WSGIRequest):
    """
    :param request: django request client 객체
    :return:
    """
    form = PhotoForm()
    method: str = request.method
    if method == "POST":
        form = PhotoForm(request.POST)

        # 폼에 맞춰 잘 작성된 데이터인지 재차 확인한다
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()  # db에 PhotoForm 데이터를 입력한다

            # 다시 다른 페이지로 이동 시키기 위해서 사용한다
            print(photo.pk)
            return redirect(to="photo_detail" , pk=photo.pk)

    # POST 메소드로 들어온게 아니면 해당 페이지로 들어온 사용자일테니, 폼을 제공하여 맞이한다.
    return render(request=request , template_name="photo/photo_post.html" , context={
        "form": form
    })


# 사진 수정 기능
def photo_edit(request: django.core.handlers.wsgi.WSGIRequest , pk: int):
    photo = get_object_or_404(klass=Photo , pk=pk)
    print("포토 상태 " , photo)
    method: str = request.method

    form: PhotoForm = PhotoForm()
    if method == "POST":
        form: PhotoForm = PhotoForm(data=request.POST , instance=photo)

        # PhotoForm 폼으로부터 제대로 된 값을 입력 받았다면, 아래 로직을 실행한다
        if form.is_valid():
            # form.pk는 업데이트 전후로 동일하다
            photo = form.save(commit=False)
            photo.save()  # 기존에 존재하던 photo의 form 데이터를 업데이트한다
            return redirect(to="photo_detail" , pk=photo.pk)

    return render(request=request ,
                  template_name="photo/photo_post.html" ,
                  context={
                      "form": form
                  })
