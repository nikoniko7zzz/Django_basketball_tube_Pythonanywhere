from django.db import models
from .account_models import User
from .item_models import Item


class Comment(models.Model):
    """動画に紐づくコメント"""

    comment_text = models.CharField(default='', max_length=1000) # コメント
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 投稿者Userモデルpk
    target = models.ForeignKey(Item, on_delete=models.CASCADE) # 対象動画Itemモデルpk
    created_at = models.DateTimeField(auto_now_add=True) # 作成日 自動作成
    updated_at = models.DateTimeField(auto_now=True) ## 更新日 自動作成

    def __str__(self):
        return self.comment_text[:20]
