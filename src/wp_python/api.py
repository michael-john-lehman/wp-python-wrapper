import woocommerce 

from .types import WooCommerceRestAPIAuthentication 

class API(woocommerce.API) : 
    """ 
    Changes the initialised parameters to use the `WooCommerceRestAPIAuthentication` TypeDict. 
    """

    def __init__(self, config : WooCommerceRestAPIAuthentication) :
        super().__init__(
            url=config["url"],
            consumer_key=config["consumer_key"],
            consumer_secret=config["consumer_secret"],
            wp_api=config.get('wp_api', True),
            version=config.get('version',"wc/v3") 
        ) 

