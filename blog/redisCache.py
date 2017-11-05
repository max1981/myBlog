from django.conf import settings
from django.core.cache import cache
from blog.models import Blog
def read_from_cache(blogID):
    key = 'BlogID'+blogID
    value = cache.get(key)
    if value == None:
        value = Blog.objects.get(id=blogID)
        cache.set(key,value,settings.NEVER_REDIS_TIMEOUT)

    return value

#write cache user id
def write_to_cache(blogID,value):
    key = 'BlogID'+blogID
    cache.set(key, value, settings.NEVER_REDIS_TIMEOUT)
    print 'write',cache.get(key)
    # data = Blog.objects.get(id=blogID)
    # data.like = value
    # data.save()
    value.save()

def syn_click_value(blogID,value):
    value = cache.get('BlogID'+blogID)
    data = Blog.object.get(id=blogID)

