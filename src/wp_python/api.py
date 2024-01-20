import woocommerce 

from .types import WooComAuth , WP_RestAPIAuth

class WooComAPI(woocommerce.API) : 
    """ 
    Changes the initialised parameters to use the `WooCommerceRestAPIAuthentication` TypeDict. 
    """

    def __init__(self, config : WooComAuth) :
        super().__init__(
            url=config["url"],
            consumer_key=config["consumer_key"],
            consumer_secret=config["consumer_secret"],
            wp_api=config.get('wp_api', True),
            version=config.get('version',"wc/v3") 
        ) 

    def serialise_query_params(self, params : dict, not_instance) : 
        """
        Serialises the dictionary of query parameters.

        i.e. `{'page' : 5, 'exclude' : [50]}` -> `page=5&exclude=[50]`
        """
        ...
        query = [] 
        for key in params : 
            
            if params[key] and not isinstance(params[key], not_instance) : 
                param = f'{key}={params[key]}'
                query.append(param) 
        query = '&'.join(query) 
        return query 
                



class WP_RestAPI : 

    def __init__(self, config : WP_RestAPIAuth) -> None:
        self.__domain = config['domain']
        self.__username = config['username'] 
        self.__password = config['application_pwd'] 
        self.__https = config.get('https', True)
        self.__version = config.get('version', 'wp/v2') 
    
    def get_url(self, endpoint : str, **kwargs) : 
        url_params = '' 
        for key in kwargs : 
            url_params += f'{key}={kwargs.get(key)}&'
        return f'{"https" if self.__https else "http"}://{self.__username}:{self.__password}@{self.__domain}/wp-json/{self.__version}/{endpoint}?{url_params}'  
    
    # need to change this at some point
    def get_headers(self) : 
        return {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36})'} 
