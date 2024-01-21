""" 
Yay! more types
https://woocommerce.github.io/woocommerce-rest-api-docs/#order-properties
"""
import typing
import datetime
from typing import TypedDict


class Billing(TypedDict):
    first_name: str
    last_name: str
    company: str
    address_1: str
    address_2: str
    city: str
    state: str
    postcode: str
    country: str
    email: str
    phone: str


class Shipping(TypedDict):
    first_name: str
    last_name: str
    company: str
    address_1: str
    address_2: str
    city: str
    state: str
    postcode: str
    country: str


class MetaData(TypedDict):
    id: int
    key: str
    value: str


class Taxes(TypedDict):
    id: int
    rate_code: str
    rate_id: str
    label: str
    compound: bool
    tax_total: str
    shipping_tax_total: str
    meta_data: list[MetaData]


class LineItems(TypedDict):
    id: int
    name: str
    product_id: str
    variation_id: str
    quantity: str
    tax_class: str
    subtotal: str
    subtotal_tax: str
    total: str
    total_tax: str
    taxes: list[Taxes]
    meta_data: list[MetaData]
    sku: str
    price: str


class TaxLines(TypedDict):
    id: int
    rate_code: str
    rate_id: str
    label: str
    compound: bool
    tax_total: str
    shipping_tax_total: str
    meta_data: list[MetaData]


class ShippingLines(TypedDict):
    id: int
    method_title: str
    method_id: str
    total: str
    total_tax: str
    taxes: list[TaxLines]
    meta_data: list[MetaData]


class FeeLines(TypedDict):
    id: int
    name: str
    tax_class: str
    tax_status: str
    total: str
    total_tax: str
    taxes: list[TaxLines]
    meta_data: list[MetaData]


class CouponLines(TypedDict):
    id: int
    code: str
    discount: str
    discount_tax: str
    meta_data: list[MetaData]


class Refunds(TypedDict):
    id: int
    reason: str
    total: str


ORDER_STATUS = typing.Literal[
    'pending', 'processing', 'on-hold', 'completed', 'cancelled', 'refunded', 'failed', 'trash']


class Order(TypedDict):
    id: int
    parent_id: int
    number: str
    order_key: str
    created_via: str
    version: str
    status: ORDER_STATUS
    currency: str
    date_created: datetime.datetime | str
    date_created_gmt: datetime.datetime | str
    date_modified: datetime.datetime | str
    date_modified_gmt: datetime.datetime | str
    discount_total: str
    discount_tax: str
    shipping_total: str
    shipping_tax: str
    cart_tax: str
    total: str
    total_tax: str
    prices_include_tax: str
    customer_id: int
    customer_ip_address: str
    customer_user_agent: str
    customer_note: str
    billing: Billing
    shipping: Shipping
    payment_method: str
    payment_method_title: str
    transaction_id: str
    date_paid: datetime.datetime | str
    date_paid_gmt: datetime.datetime | str
    date_completed: datetime.datetime | str
    date_completed_gmt: datetime.datetime | str
    cart_hash: str
    meta_data: list['MetaData']
    line_items: list["LineItems"]
    tax_lines: list["TaxLines"]
    shipping_lines: list['ShippingLines']
    fee_lines: list['FeeLines']
    coupon_lines: list['CouponLines']
    refunds: list['Refunds']
    set_paid: bool


class OrderQueryParams(TypedDict):
    context: typing.NotRequired[typing.Literal['view', 'edit']]
    page: typing.NotRequired[int]
    per_page: typing.NotRequired[int]
    search: typing.NotRequired[str]
    after: typing.NotRequired[str]
    before: typing.NotRequired[str]
    modified_after: typing.NotRequired[str]
    modified_before: typing.NotRequired[str]
    dates_are_gmt: typing.NotRequired[bool]
    exclude: typing.NotRequired[list[int]]
    include: typing.NotRequired[list[int]]
    offset: typing.NotRequired[int]
    order: typing.NotRequired[typing.Literal['asc', 'desc']]
    orderby: typing.NotRequired[typing.Literal['date', 'id', 'include', 'title', 'slug']]
    parent: typing.NotRequired[list[int]]
    parent_exclude: typing.NotRequired[list[int]]
    status: typing.NotRequired[ORDER_STATUS]
    customer: typing.NotRequired[int]
    product: typing.NotRequired[int]
    dp: typing.NotRequired[int]


def order_query_params(
    context: typing.Optional[typing.Literal['view', 'edit']] = None,
    page: typing.Optional[int] = None,
    per_page: typing.Optional[int] = None,
    search: typing.Optional[str] = None,
    after: typing.Optional[str] = None,
    before: typing.Optional[str] = None,
    modified_after: typing.Optional[str] = None,
    modified_before: typing.Optional[str] = None,
    dates_are_gmt: typing.Optional[bool] = None,
    exclude: typing.Optional[list[int]] = None,
    include: typing.Optional[list[int]] = None,
    offset: typing.Optional[int] = None,
    order: typing.Optional[typing.Literal['asc', 'desc']] = None,
    orderby: typing.Optional[typing.Literal['date', 'id', 'include', 'title', 'slug']] = None,
    parent: typing.Optional[list[int]] = None,
    parent_exclude: typing.Optional[list[int]] = None,
    status: typing.Optional[ORDER_STATUS] = None,
    customer: typing.Optional[int] = None,
    product: typing.Optional[int] = None,
    dp: typing.Optional[int] = None,
) -> OrderQueryParams:
    return {
        'context': context,
        'page': page,
        'per_page': per_page,
        'search': search,
        'after':  after,
        'before':  before,
        'modified_after':         modified_after,
        'modified_before':            modified_before,
        'dates_are_gmt':       dates_are_gmt,
        'exclude':             exclude,
        'include':            include,
        'offset':                  offset,
        'order':                         order,
        'orderby':                 orderby,
        'parent': parent,
        'parent_exclude':    parent_exclude,
        'status':          status,
        'customer':  customer,
        'product':      product,
        'dp':        dp,
    }
