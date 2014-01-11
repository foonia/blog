from google.appengine.ext import ndb

class Post(ndb.Model):
    category = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    tags = ndb.StringProperty(repeated=True)

    @classmethod
    def get_lastest(cls, count):
        return cls.query().order(-cls.date).fetch(count)

    def get_pre(self):
        return Post.query().filter(Post.date < self.date).fetch(1)[0]

    def get_next(self):
        return Post.query().filter(Post.date < self.date).fetch(1)[0]

    def get_addr(self):
        return '/blog/%d' % self.key.id()

    @classmethod
    def get_tagged_post(cls, tag):
        return cls.query().filter(Post.tags in tag)

    def get_tags(self):
        return ''.join(['<a href="/posts/%s">%s</a>' % (tag, tag) for tag in self.tags])
