"""
Implements async interface for handling user requests
"""
import aiohttp 

from . import types
from .api import WP_RestAPI 


class Users : 

    class __User :
        ... 

    def __init__(self, api : WP_RestAPI) -> None:
        self.__api = api 

    # need to add errors and shit 
    async def current(self) -> types.user.User : 
        async with aiohttp.ClientSession(headers=self.__api.get_headers()) as session : 
            async with session.get(self.__api.get_url('users/me', context='edit')) as response : 
                if response.status == 200 : 
                    return await response.json() 
                return None  
            

