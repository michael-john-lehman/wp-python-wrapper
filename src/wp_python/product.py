from . import types 
from .types.woocom_products import product_query_params as query_params
from .api import WooComAPI 


class Products : 

    DEFAULT_PAGE_SIZE = 30

    def __init__(self, api : WooComAPI) : 
        self.__api = api 

    def get(self, id : int) -> types.products.Product | None  : 
        response = self.__api.get(f'products/{id}')
        if response.status_code == 200 : 
            return response.json()  
        return None  
    
    def products(self, params : types.products.ProductGetQuery) -> list[types.products.Product] | None : 
        response = self.__api.get(f'products?{self.__api.serialise_query_params(params, not_instance=Products)}')
        if response.status_code == 200 : 
            return response.json() 

