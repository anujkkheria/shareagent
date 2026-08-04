from tools.provider.mock_provider import mock_provider


def mock_tool():
    """
    This is a mock tool function that utilizes the mock provider.
    This has to be utilized for testing and development purposes. It is not intended for production use.

    """
    return mock_provider()
