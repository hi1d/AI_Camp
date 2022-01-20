from django.shortcuts import render, redirect
from .models import TweetModel, TweetComment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView

# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')
    

def tweet(request):
    if request.method =='GET':
        user = request.user.is_authenticated
        if user:
            tweets = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'tweets':tweets})
        else:
            return redirect('/sign-in')
    elif request.method =='POST':
        user = request.user
        content = request.POST.get('my-content', '')
        tags = request.POST.get('tag','').split(',')

        if content == '':
            tweets = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html',{'error_msg':'빈 칸을 입력해주세요.','tweets':tweets})
        
                
        my_tweet = TweetModel.objects.create(author = user,content = content)
        for tag in tags:
            tag = tag.strip()
            if tag != '':
                my_tweet.tags.add(tag)

        my_tweet.save()

        return redirect('/tweet')

@login_required
def delete_tweet(request,id):
    tweet = TweetModel.objects.get(id=id)
    tweet.delete()
    return redirect('/tweet')

def detail_tweet(request,id):
    user = request.user.is_authenticated
    if user:
        tweet = TweetModel.objects.get(id=id)
        comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
        return render(request, 'tweet/tweet_detail.html',{'tweet':tweet,'comments':comment})
    else:
        return redirect('/sign-in')


def write_comment(request,id):
    user = request.user
    if user:
        TweetComment.objects.create(
            tweet_id = id,
            author = user,
            comment = request.POST.get('comment', '')
        )
        return redirect(f'/tweet/{id}')
    else:
        return redirect('sign-in')

@login_required
def delete_comment(request,id):
    comment = TweetComment.objects.get(id=id)
    comment.delete()
    return redirect(f'/tweet/{comment.tweet_id}')

class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = TweetModel

    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context