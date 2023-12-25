class GitHubUser:
    def __init__(self, username, num_repositories, num_followers, num_following, num_contributions):
        self.username = username
        self.num_repositories = num_repositories
        self.num_followers = num_followers
        self.num_following = num_following
        self.num_contributions = num_contributions

    def __str__(self):
        return f"User: {self.username}, Repos: {self.num_repositories}, Followers: {self.num_followers}, Following: {self.num_following}, Contributions: {self.num_contributions}"

    def to_csv_row(self):
        return f"{self.username},{self.num_repositories},{self.num_followers},{self.num_following},{self.num_contributions}"
