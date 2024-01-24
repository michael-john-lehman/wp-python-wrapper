from . import types
from .types.woocom_orders import order_query_params as query_params
from .api import WooComAPI 

query_params()


class Orders:

    def __init__(self, api: WooComAPI) -> None:
        """
        args:
            api (WooComAPI) :
        """
        self.__api = api

    def order(self, _id: int) -> types.orders.Order:
        response = self.__api.get(f'orders/{_id}')
        if response.status_code != 200:
            raise Exception()
        return response.json()

    def orders(self, params: types.orders.OrderQueryParams) -> list[types.orders.Order]:
        response = self.__api.get(f'orders?{self.__api.serialise_query_params(params, Orders)}')
        if response.status_code != 200:
            raise Exception()
        return response.json()
