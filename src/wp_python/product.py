import queue

from . import types
from .types.woocom_products import product_query_params as query_params
from .api import WooComAPI 


class ProductBatchUpdater:

    @staticmethod
    def gather_from_queues(size: int, *args: queue.Queue):
        arrays = [[] for x in range(0, len(args))]
        arrays = tuple(arrays)
        for index, Q in enumerate(args):
            while not Q.empty():
                for _index_2 in range(0, size):
                    if Q.empty():
                        break
                    if not Q.empty():
                        arrays[index].append(Q.get())
                    if sum(len(x) for x in arrays) >= 100:
                        yield arrays
                        arrays = [[] for x in range(0, len(args))]
                        arrays = tuple(arrays)
        if sum(len(x) for x in arrays) > 0:
            yield arrays

    def __init__(self, api: WooComAPI):
        self.__api = api
        self.__create = queue.Queue[types.products.Product]()
        self.__update = queue.Queue[types.products.Product]()
        self.__delete = queue.Queue[int]()

    def append_create(self, data: types.products.Product):
        self.__create.put(data)

    def append_update(self, data: types.products.Product):
        self.__update.put(data)

    def append_delete(self, data: int):
        self.__delete.put(data)

    def flush(self):
        for data in self.gather_from_queues(100, self.__create, self.__update, self.__delete):
            create, update, delete = data
            self.__api.post("products/batch", {
                'create': create,
                'update': update,
                'delete': delete
            })



class Products:

    DEFAULT_PAGE_SIZE = 30

    def __init__(self, api: WooComAPI):
        self.__api = api 

    def get(self, _id: int) -> types.products.Product | None:
        response = self.__api.get(f'products/{id}')
        if response.status_code == 200:
            return response.json()  
        return None  
    
    def products(self, params: types.products.ProductGetQuery) -> list[types.products.Product] | None:
        response = self.__api.get(f'products?{self.__api.serialise_query_params(params, not_instance=Products)}')
        if response.status_code == 200:
            return response.json()

    def batch(self, create: bool = None, update: bool = None, delete: bool = None):
        def inner():
            ...
        return inner

