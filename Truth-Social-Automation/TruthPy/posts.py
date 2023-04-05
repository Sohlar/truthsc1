import markdownify

class Post:
    def __init__(self, id, created_at, reply_to, url, replies, likes, content,account):
        self.id = id
        self.created_at = created_at
        self.reply_to = reply_to
        self.url = url
        self.replies = replies
        self.likes = likes
        self.content = markdownify.markdownify(content)
        self.account = account

    async def reply(self, user, text):
        return await user.post(text, in_reply_to_id=self.id)

