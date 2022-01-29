from django.core.management import BaseCommand
from Forum.models import Post, Comment


MOCK_DATA = [
    {
        "title": "This is a post.",
        "body": "This is the body of a post.",
        "comments": ["This is a comment of a post.", "This is a another comment of a post."]
    },
    {
        "title": "This is a another post.",
        "body": "This is the body of another post.",
        "comments": ["This is a comment of another post.", "I love playing chess!."]
    },
]

class Command(BaseCommand):
    help = "Loads default data."

    def handle(self, *args, **kwargs):
        if Post.objects.exists():
            print("The table is already populated.")
            return
        print("Creating forum data.")
        for sample_post in MOCK_DATA:
            post = Post()
            post.title = sample_post.get("title", "This is a sample title so the insertion does not fail.")
            post.body = sample_post.get("body", "This is a sample body so the insertion does not fail.")
            post.save()
            for sample_comment in sample_post.get("comments", ["Sample comment to prevent insertion failures."]):
                comment = Comment()
                comment.body = sample_comment
                comment.post = post
                comment.save()
        print("The insertions are completed.")
