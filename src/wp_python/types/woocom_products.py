""" 
Product Properties nicely typed out for you, what do you say? thank you
"""
from typing import TypedDict , Literal, Final 

class Downloadable(TypedDict) : 
    """
    ## Product - Downloads properties
    
    Attribute	Type	Description
    
    
    `id`	string	File ID.
    `name`	string	File name.
    `file`	string	File URL.
    """
    id	: str 
    name : str
    file :	str 

class Dimensions(TypedDict) : 
    """
    ## Product - Dimensions properties
    
    
    Attribute	Type	Description
    
    `length`	string	Product length.
    `width`	string	Product width.
    `height`	string	Product height.
    
    """
    length	: str 
    width	: str 
    height	: str 

class Categories(TypedDict) : 
    id	: str 
    name : str # READ ON:Y 
    slug : str # READ ONLY 

class Tags(TypedDict) : 
    id	: str 
    name : str # READ ON:Y 
    slug : str # READ ONLY 

class Images(TypedDict) : 
    id	: str 
    date_created : str # Read only 
    date_created_gmt : str 	# Read only 
    date_modified : str	# Read only 
    date_modified_gmt : str # Read only 
    src	: str 
    name : str 
    alt : str 

class DefaultAttributes(TypedDict) : 
    id	: int 
    name : str 
    options	: str  

class Attributes(TypedDict) : 
    id	: int 
    name : str 
    position : int 
    visible	 : bool 
    variation : bool 
    options	: list[str] 

class MetaData(TypedDict) : 
    id	: int 
    key	 : str 
    value : str 

PRODUCT_TYPE = Literal['simple', 'grouped', 'external', 'variable']
PRODUCT_STATUS = Literal['draft', 'pending', 'private', 'publish']
PRODUCT_CATALOG_VISIBILYT = Literal['visble', 'catalog', 'search', 'hidden'] 

class Product(TypedDict) : 
    """
    
    ## Product properties

    ## Attribute	Type	Description

    `id`	integer	Unique identifier for the resource.READ-ONLY

    `name`	string	Product name.

    `slug`	string	Product slug.

    `permalink`	string	Product URL.READ-ONLY

    `date_created`	date-time	The date the product was created, in the site's timezone.READ-ONLY

    `date_created_gmt`	date-time	The date the product was created, as GMT.READ-ONLY

    `date_modified`	date-time	The date the product was last modified, in the site's timezone.READ-ONLY

    `date_modified_gmt`	date-time	The date the product was last modified, as GMT.READ-ONLY

    `type`	string	Product type. Options: simple, grouped, external and variable. Default is simple.

    `status`	string	Product status (post status). Options: draft, pending, private and publish. Default is publish.

    `featured`	boolean	Featured product. Default is false.

    `catalog_visibility`	string	Catalog visibility. Options: visible, catalog, search and hidden. Default is visible.

    `description`	string	Product description.

    `short_description`	string	Product short description.

    `sku`	string	Unique identifier.

    `price`	string	Current product price.READ-ONLY

    `regular_price`	string	Product regular price.

    `sale_price`	string	Product sale price.

    `date_on_sale_from`	date-time	Start date of sale price, in the site's timezone.

    `date_on_sale_from_gmt`	date-time	Start date of sale price, as GMT.

    `date_on_sale_to`	date-time	End date of sale price, in the site's timezone.

    `date_on_sale_to_gmt`	date-time	End date of sale price, as GMT.

    `price_html`	string	Price formatted in HTML.READ-ONLY

    `on_sale`	boolean	Shows if the product is on sale.READ-ONLY

    `purchasable`	boolean	Shows if the product can be bought.READ-ONLY

    `total_sales`	integer	Amount of sales.READ-ONLY

    `virtual`	boolean	If the product is virtual. Default is false.

    `downloadable`	boolean	If the product is downloadable. Default is false.

    `downloads`	array	List of downloadable files. See Product - Downloads properties

    `download_limit`	integer	Number of times downloadable files can be downloaded after purchase. Default is -1.

    `download_expiry`	integer	Number of days until access to downloadable files expires. Default is -1.

    `external_url`	string	Product external URL. Only for external products.

    `button_text`	string	Product external button text. Only for external products.

    `tax_status`	string	Tax status. Options: taxable, shipping and none. Default is taxable.

    `tax_class`	string	Tax class.

    `manage_stock`	boolean	Stock management at product level. Default is false.

    `stock_quantity`	integer	Stock quantity.

    `stock_status`	string	Controls the stock status of the product. Options: instock, outofstock, onbackorder. Default is instock.

    `backorders`	string	If managing stock, this controls if backorders are allowed. Options: no, notify and yes. Default is no.

    `backorders_allowed`	boolean	Shows if backorders are allowed.READ-ONLY

    `backordered`	boolean	Shows if the product is on backordered.READ-ONLY

    `sold_individually`	boolean	Allow one item to be bought in a single order. Default is false.

    `weight`	string	Product weight.

    `dimensions`	object	Product dimensions. See Product - Dimensions properties

    `shipping_required`	boolean	Shows if the product need to be shipped.READ-ONLY

    `shipping_taxable`	boolean	Shows whether or not the product shipping is taxable.READ-ONLY

    `shipping_class`	string	Shipping class slug.

    `shipping_class_id`	integer	Shipping class ID.READ-ONLY

    `reviews_allowed`	boolean	Allow reviews. Default is true.

    `average_rating`	string	Reviews average rating.READ-ONLY

    `rating_count`	integer	Amount of reviews that the product have.READ-ONLY

    `related_ids`	array	List of related products IDs.READ-ONLY

    `upsell_ids`	array	List of up-sell products IDs.

    `cross_sell_ids`	array	List of cross-sell products IDs.

    `parent_id`	integer	Product parent ID.

    `purchase_note`	string	Optional note to send the customer after purchase.

    `categories`	array	List of categories. See Product - Categories properties

    `tags`	array	List of tags. See Product - Tags properties

    `images`	array	List of images. See Product - Images properties

    `attributes`	array	List of attributes. See Product - Attributes properties

    `default_attributes`	array	Defaults variation attributes. See Product - Default attributes properties

    `variations`	array	List of variations IDs.READ-ONLY

    `grouped_products`	array	List of grouped products ID.

    `menu_order`	integer	Menu order, used to custom sort products.

    `meta_data`	array	Meta data. See Product - Meta data properties

    
    
    Product - Dimensions properties
    Attribute	Type	Description
    length	string	Product length.
    width	string	Product width.
    height	string	Product height.
    Product - Categories properties
    Attribute	Type	Description
    id	integer	Category ID.
    name	string	Category name.READ-ONLY
    slug	string	Category slug.READ-ONLY
    Product - Tags properties
    Attribute	Type	Description
    id	integer	Tag ID.
    name	string	Tag name.READ-ONLY
    slug	string	Tag slug.READ-ONLY
    Product - Images properties
    Attribute	Type	Description
    id	integer	Image ID.
    date_created	date-time	The date the image was created, in the site's timezone.READ-ONLY
    date_created_gmt	date-time	The date the image was created, as GMT.READ-ONLY
    date_modified	date-time	The date the image was last modified, in the site's timezone.READ-ONLY
    date_modified_gmt	date-time	The date the image was last modified, as GMT.READ-ONLY
    src	string	Image URL.
    name	string	Image name.
    alt	string	Image alternative text.
    Product - Attributes properties
    Attribute	Type	Description
    id	integer	Attribute ID.
    name	string	Attribute name.
    position	integer	Attribute position.
    visible	boolean	Define if the attribute is visible on the "Additional information" tab in the product's page. Default is false.
    variation	boolean	Define if the attribute can be used as variation. Default is false.
    options	array	List of available term names of the attribute.
    Product - Default attributes properties
    Attribute	Type	Description
    id	integer	Attribute ID.
    name	string	Attribute name.
    option	string	Selected attribute term name.
    Product - Meta data properties
    Attribute	Type	Description
    id	integer	Meta ID.READ-ONLY
    key	string	Meta key.
    value	string	Meta value.
    
    
    """
    id	: int # READ ONLY 
    name : str
    slug : str 
    permalink : str	
    date_created : str # Read only 
    date_created_gmt : str 	# Read only 
    date_modified : str	# Read only 
    date_modified_gmt : str # Read only 
    type : PRODUCT_TYPE
    status : PRODUCT_STATUS
    featured : bool	
    catalog_visibility : PRODUCT_CATALOG_VISIBILYT
    description	: str 	
    short_description : str 
    sku	: str 
    price : str # READ only 
    regular_price : str 
    sale_price	: str 
    date_on_sale_from : str 
    date_on_sale_from_gmt : str 
    date_on_sale_to	: str 
    date_on_sale_to_gmt	: str 
    price_html : str # read only 
    on_sale	: bool # read only 
    purchasable	: bool # read only 
    total_sales	: int	# read onn;y 
    virtual	: bool 
    downloadable : bool 
    downloads : list[Downloadable]
    download_limit	: int 
    download_expiry	: int 
    external_url : str 
    button_text	: str 
    tax_status	: Literal['taxable', 'shipping', 'none']
    tax_class : str 
    manage_stock : bool 
    stock_quantity	: int 
    stock_status : Literal['instock', 'outofstock', 'onbackorder']
    backorders	: Literal['no', 'notify', 'yes'] 
    backorders_allowed	: bool # Readonly 
    backordered	: bool # read only 
    sold_individually : bool 
    weight	: str  
    dimensions	: Dimensions
    shipping_required	: bool #READ-ONLY
    shipping_taxable	: bool # READ-ONLY
    shipping_class	: str 
    shipping_class_id	: int # Read only 
    reviews_allowed	: bool 
    average_rating	: str # read only 
    rating_count	: int #READ-ONLY
    related_ids	 : list[int] # READ ONLY 
    upsell_ids	: list[int] # READ ONLY 
    cross_sell_ids	: list[int] # READ ONLY 
    parent_id : int 
    purchase_note : str 
    categories	: list[Categories] 
    tags    : list[Tags] 
    images	: list[Images]
    attributes	: list[Attributes]
    default_attributes	: list[DefaultAttributes]
    variations	: list[int] 
    grouped_products : list[int] 
    menu_order	: int 
    meta_data : list[MetaData] 


