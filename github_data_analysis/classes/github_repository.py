class GitHubRepository:
    def __init__(self, name, owner, description, homepage, license, forks, watchers, date_of_collection):
        self.name = name
        self.owner = owner
        self.description = description
        self.homepage = homepage
        self.license = license
        self.forks = forks
        self.watchers = watchers
        self.date_of_collection = date_of_collection

    def __str__(self):
        return f"{self.owner}/{self.name}: {self.description} ({self.watchers})"

    def to_csv_row(self):
        return [self.name, self.owner, self.description, self.homepage, self.license, self.forks, self.watchers, self.date_of_collection]