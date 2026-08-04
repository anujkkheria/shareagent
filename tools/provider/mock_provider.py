from models.article import article


def mock_provider():
    return [
        article(
            "Stock A sees a surge in demand",
            "https://example.com/stock-a-news",
            "Example News",
            "2026-08-01",
            "Stock A has seen a significant increase in demand due to positive market trends.",
            "MockProvider",
        ),
        article(
            "Stock B faces regulatory challenges",
            "https://example.com/stock-b-news",
            "Example News",
            "2026-08-02",
            "Stock B is facing regulatory challenges that may impact its growth prospects.",
            "MockProvider",
        ),
    ]
