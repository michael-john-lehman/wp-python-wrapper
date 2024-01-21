from . import types 
from .types.woocom_products import product_query_params as query_params
from .api_async import WooComAsyncAPI 


class Products:

    DEFAULT_PAGE_SIZE = 30

    def __init__(self, api: WooComAsyncAPI):
        self.__api = api 

    async def get(self, _id: int) -> types.products.Product | None:
        async with self.__api.get(f'products/{_id}') as response:
            if response.status == 200:
                return await response.json()
    
    async def products(self, params : types.products.ProductGetQuery) -> list[types.products.Product] | None:
        async with self.__api.get(f'products?{self.__api.serialise_query_params(params, not_instance=Products)}') \
                as response:
            if response.status == 200:
                return await response.json()

