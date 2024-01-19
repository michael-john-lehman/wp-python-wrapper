import typing

class WooComAuth(typing.TypedDict) : 
    """ 
    
    Keys:
        Required
        `consumer_key` (str) : The ID/key for the secret 
        `consumer_secret` (str) : The secret, the one that is only shown once.
        `url` (str) :  The url of the site. e.g https://github.com 

        Optional

        `wp_api` (bool) :   
        
        `version` ("wc/v3") :   
    
    """
    consumer_key : str 
    consumer_secret : str 
    url : str 

    wp_api : typing.Optional[bool]
    version : typing.Optional[typing.Literal["wc/v3"]] 

class WP_RestAPIAuth(typing.TypedDict) : 
    domain : str 
    username : str 
    application_pwd : str
    version : typing.Optional[typing.Literal['wp/v2']] 
    https : typing.Optional[bool] 