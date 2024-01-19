import datetime
from typing import TypedDict
import typing

class Billing(TypedDict) : 
    first_name : str
    last_name : str
    company	: str
    address_1 : str
    address_2 : str
    city : str
    state : str
    postcode : str
    country	: str
    email : str
    phone : str

class Shipping(TypedDict) : 
    first_name	: str 
    last_name : str 
    company : str 
    address_1 : str 
    address_2 : str 
    city : str 
    state : str 
    postcode : str 
    country : str 

ORDER_STATUS = typing.Literal['pending', 'processing', 'on-hold', 'completed', 'cancelled', 'refunded', 'failed' , 'trash']

class Order(TypedDict) : 
    id : int 
    parent_id : int 
    number : str 
    order_key : str 
    created_via	: str 
    version	: str 
    status : ORDER_STATUS
    currency : str 
    date_created : datetime.datetime | str 
    date_created_gmt : datetime.datetime | str 
    date_modified : datetime.datetime | str 
    date_modified_gmt	: datetime.datetime | str 
    discount_total	: str 
    discount_tax	: str 
    shipping_total	: str 
    shipping_tax	: str 
    cart_tax	: str 
    total	: str 
    total_tax	: str 
    prices_include_tax : str 
    customer_id	: int 
    customer_ip_address	: str 
    customer_user_agent	: str 
    customer_note	: str 
    billing	: Billing
    shipping : Shipping
    payment_method	: str 
    payment_method_title : str 	
    transaction_id	: str 
    date_paid	: datetime.datetime | str 
    date_paid_gmt : datetime.datetime | str 
    date_completed	: datetime.datetime | str 
    date_completed_gmt	: datetime.datetime | str 
    cart_hash : str 
    meta_data : list['MetaData']
    line_items	: list["LineItems"]
    tax_lines	: list["TaxLines"]
    shipping_lines : list['ShippingLines']
    fee_lines : list['FeeLines']
    coupon_lines : list['CouponLines']
    refunds	: list['Refunds']
    set_paid : bool 
