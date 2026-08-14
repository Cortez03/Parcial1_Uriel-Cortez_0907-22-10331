class User:
    def __init__(self, user_id, name, email, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

class Comment:
    def __init__(self, comment_id, message):
        self.comment_id = comment_id
        self.message = message

class History:
    def __init__(self, history_id, action):
        self.history_id = history_id
        self.action = action

class Article:
    def __init__(self, article_id, title, content, author):
        self.article_id = article_id
        self.title = title
        self.content = content
        self.author = author

class Ticket:
    def __init__(self, ticket_id, title, requester):
        self.ticket_id = ticket_id
        self.title = title
        self.requester = requester
        self.technician = None
        self.comments = []
        self.history = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def log_history(self, action):
        self.history.append(History(len(self.history) + 1, action))