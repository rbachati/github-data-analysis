class PullRequest:
    def __init__(self, title, number, body, state, created_at, closed_at, user):
        self.title = title
        self.number = number
        self.body = body
        self.state = state
        self.created_at = created_at
        self.closed_at = closed_at
        self.user = user

    def __str__(self):
        return f"PR: {self.title}, Number: {self.number}, State: {self.state}, Created At: {self.created_at}, Closed At: {self.closed_at}, User: {self.user}"

    def to_csv_row(self):
        return f"{self.title},{self.number},{self.body},{self.state},{self.created_at},{self.closed_at},{self.user}"
