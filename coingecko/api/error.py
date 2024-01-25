class CoinGeckoAPIErrorHandler:
    def __init__(self, response):
        self.response = response

    @classmethod
    def handle_response(cls, response):
        if response.status_code == 400:
            raise GeckoAPIBadRequest(response.status_code, response.json())
        elif response.status_code == 401:
            raise GeckoAPIUnauthorized(response.status_code, response.json())
        elif response.status_code == 429:
            raise GeckoAPITooManyRequests(response.status_code, response.json())
        elif response.status_code == 500:
            raise GeckoAPIInternalServerError(response.status_code, response.json())
        elif response.status_code == 503:
            raise GeckoAPIServiceUnavailable(response.status_code, response.json())
        else:
            raise GeckoAPIException(response.status_code, response.json())


class GeckoAPIException(Exception):
    def __init__(self, status_code = None, error_message = None):
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self):
        return f"{self.status_code}: {self.error_message}"

class GeckoAPIBadRequest(GeckoAPIException):
    def __init__(self, status_code = None, error_message = None):
        super().__init__(status_code, error_message)

class GeckoAPIUnauthorized(GeckoAPIException):
    def __init__(self, status_code = None, error_message = None):
        super().__init__(status_code, error_message)

class GeckoAPITooManyRequests(GeckoAPIException):
    def __init__(self, status_code = None, error_message = None):
        super().__init__(status_code, error_message)

class GeckoAPIInternalServerError(GeckoAPIException):
    def __init__(self, status_code = None, error_message = None):
        super().__init__(status_code, error_message)

class GeckoAPIServiceUnavailable(GeckoAPIException):
    def __init__(self, status_code = None, error_message = None):
        super().__init__(status_code, error_message)
