""" 
For usage with the asyncio module.
"""
import json 
import logging 
import aiohttp

from wp_python.types import WP_RestAPIAuth

from .types import WooComAuth
from .api import WooComAPI, WP_RestAPI
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

class WooComAsyncAPI(WooComAPI) : 
    """
    Changes the request methods to use the aiohttp module, useful if you want to use the normal API class given from the woocommerce.API class.

    This does make the methods into async context managers so use like  

    ```python
    async with api.get('orders') as response : 
        data = await response.json() 
    ```
    """
    def __init__(self, config: WooComAuth):
        super().__init__(config)
        auth = None 
        headers = {
            "user-agent": f"{self.user_agent}",
            "accept": "application/json",
            "content-type" : "application/json;charset=utf-8" 
        }
        if self.is_ssl is True and self.query_string_auth is False:
            auth = aiohttp.BasicAuth(self.consumer_key, self.consumer_secret)
        self.session = aiohttp.ClientSession(
            auth=auth,
            headers=headers,
        ) 

    def get_url(self, endpoint) : 
        url : str = self.url
        api = "wc-api"
        if url.endswith("/") is False:
            url = f"{url}/"
        if self.wp_api:
            api = "wp-json"
        return f"{url}{api}/{self.version}/{endpoint}"
    
    @asynccontextmanager
    async def request(self, method, endpoint, data, params=None, **kwargs) : 
        url = self.get_url(endpoint)
        if data is not None:
            data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        match method : 
            case "GET" : 
                yield await self.session.get(url)
            case "POST" : 
                yield await self.session.post(url, data=data)
            case "PATCH" : 
                yield await self.session.patch(url , data=data)
            case "DELETE" : 
                yield await self.session.delete(url)
            case "PUT" : 
                yield await self.session.put(url,data=data) 

    @asynccontextmanager
    async def get(self, endpoint, **kwargs):
        """ Get requests """
        async with self.request("GET", endpoint, None, **kwargs) as response : 
            yield response 

    @asynccontextmanager
    async def post(self, endpoint, data, **kwargs):
        """ POST requests """
        async with self.request("POST", endpoint, data, **kwargs) as response : 
            yield response 

    @asynccontextmanager
    async def put(self, endpoint, data, **kwargs):
        """ PUT requests """
        async with self.request("PUT", endpoint, data, **kwargs) as response : 
            yield response 

    @asynccontextmanager
    async def delete(self, endpoint, **kwargs):
        """ DELETE requests """
        async with self.request("DELETE", endpoint, None, **kwargs) as response : 
            yield response 

    async def close(self) : 
        await self.session.close()

class WP_RestAsyncAPI(WP_RestAPI) : 

    def __init__(self, config: WP_RestAPIAuth) -> None:
        super().__init__(config) 
        self.session = aiohttp.ClientSession(headers=self.get_headers()) 

    async def close(self) : 
        await self.session.close()