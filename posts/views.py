from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

list_post = [
    {
        'title': 'Java',
        'content': 'Java la ngon ngu tuyet voi de hoc ve OOP'
    },
    {
        'title': 'Python',
        'content': 'Python la ngon ngu tuyet voi, no cuc de de lam ra mot thu gi do hay ho chi voi vai dong code'
    },
    {
        'title': 'Rush',
        'content': 'Rush la ngon ngu voi hieu suat an tuong, toi du dinh hoc ngon ngu nay de emmbed vao Python'
    }
]


# Create your views here.
def list_all_post(request):
    html = ''
    for index, post in enumerate(list_post):
        html += f'''
            <div>
                <h1>{index + 1} - {post['title']} </h1>
                <p> {post['content']}</p>
            </div>
        '''
    return HttpResponse(html)


def list_one_post(request, id):
    id -= 1
    if id >= len(list_post) or id < 0:
        return HttpResponseNotFound("<h1> Không tồn tại Bài post này !!! </h1>")
    html = f'''
        <div>
            <h1>{id + 1} - {list_post[id]['title']} </h1>
            <p> {list_post[id]['content']}</p>
        </div>
    '''
    return HttpResponse(html)
