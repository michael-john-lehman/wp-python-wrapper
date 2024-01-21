"""
Implements interface for handling user requests
"""
import requests 
from . import types
from .api import WP_RestAPI 


class Users:

    class __User:
        ... 

    def __init__(self, api: WP_RestAPI) -> None:
        self.__api = api 
    
    def current(self) -> types.user.User | None:
        response = requests.get(self.__api.get_url('users/me', context='edit'), headers=self.__api.get_headers()) 
        if response.status_code == 200:
            return response.json()
        return None
    
    @staticmethod
    def current_from_cookie(url: str, nonce_cookie: str, headers=None):
        raise NotImplementedError()
