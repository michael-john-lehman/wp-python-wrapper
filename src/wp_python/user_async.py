"""
Implements async interface for handling user requests
"""
import aiohttp 

from . import types
from .api_async import WP_RestAsyncAPI 


class Users:

    class __User:
        ... 

    def __init__(self, api: WP_RestAsyncAPI) -> None:
        self.__api = api 

    # need to add errors and shit 
    async def current(self) -> types.user.User | None:
        async with self.__api.session.get(self.__api.get_url('users/me', context='edit')) as response:
            if response.status == 200:
                return await response.json() 
            return None  
            

