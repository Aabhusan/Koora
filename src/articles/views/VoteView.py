from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseServerError
from articles.models import Article, Tag, Vote
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
import json
from utils.decorators import fail_safe

class VoteView(View):

    def get(self, request):
        return HttpResponse('What you up to ?')

    fail_safe(for_model=User)
    def post(self, request):
        data = json.loads(request.body)
        user_id = data['user_id']
        article_id = data['article_id']
        vote_type = data['vote_type']

        try:
            content_type = ContentType.objects.get_for_model(Article)
            article = Article.objects.get(id=article_id)
            user = User.objects.get(id=user_id)
        except:
            return JsonResponse({
                'status' : 500
            })
        
        try:
            vote = Vote.objects.of_instance(article).get(user=user)
        except Vote.DoesNotExist:
            vote = False

        if vote:
            print('Has a vote already ', vote_type)
            if (vote.is_upvote and vote_type == 'up') or (not vote.is_upvote and vote_type == 'down'):
                print('conflict vote lol')
                vote.delete()
            elif vote.is_upvote:
                print('remove up')
                vote.is_upvote = False
                vote.save()
            else:
                print('remove down')
                vote.is_upvote = True
                vote.save()
        else:
            is_upvote = True if vote_type == 'up' else False
            vote = Vote.objects.create(object_id=article_id, user=user, content_type=content_type, is_upvote=is_upvote)
            vote.save()

        data = {
            'status' : 200,
            'vote_count' : article.vote_count
        }
        return JsonResponse(data)
    