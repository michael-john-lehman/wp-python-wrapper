""" 
For usage with the asyncio module.
"""
import json 
import logging 
import aiohttp
from .api import WooComAPI
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
        auth = None
        headers = {
            "user-agent": f"{self.user_agent}",
            "accept": "application/json"
        }
        if self.is_ssl is True and self.query_string_auth is False:
            auth = aiohttp.BasicAuth(self.consumer_key, self.consumer_secret)
        if data is not None:
            data = json.dumps(data, ensure_ascii=False).encode('utf-8')
            headers["content-type"] = "application/json;charset=utf-8"
        async with aiohttp.ClientSession(
            auth=auth,
            headers=headers,
            ) as Session : 
            match method : 
                case "GET" : 
                    yield await Session.get(url)
                case "POST" : 
                    yield await Session.post(url, data=data)
                case "PATCH" : 
                    yield await Session.patch(url , data=data)
                case "DELETE" : 
                    yield await Session.delete(url)
                case "PUT" : 
                    yield await Session.put(url,data=data) 
    
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

