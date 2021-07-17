# Standard library import
from django.contrib.sitemaps import Sitemap

# Local import
from .models import Post

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated