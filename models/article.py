class article:
    def __init__(
        self,
        title: str,
        url: str,
        source: str,
        published_at: str,
        summary: str,
        provider: str,
    ):
        self.title = title
        self.url = url
        self.source = source
        self.published_at = published_at
        self.summary = summary
        self.provider = provider
    def __repr__(self):
        return f"Article(title={self.title}, url={self.url}, source={self.source}, published_at={self.published_at}, summary={self.summary}, provider={self.provider})"