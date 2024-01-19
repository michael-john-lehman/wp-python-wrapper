import typing 


USER_CONTEXTS = typing.Literal['embed', 'view', 'edit']

class User(typing.TypedDict) : 
    id : int # Context: embed, view, edit
    username : str # Context: edit
    name : str # Context: embed, view, edit
    first_name : str # Context: edit
    last_name : str #Context: edit
    email : str # Context: edit
    url : str #Context: embed, view, edit
    description : str #Context: embed, view, edit
    link : str #Context: embed, view, edit
    locale : str #Context: edit
    nickname : str # Context : edit 
    slug : str # context embed, view, edit 
    registered_date : str # context : edit 
    roles : list # Context: edit
    capabilities : dict # Context: edit
    extra_capabilities : dict # Context : edit 
    avatar_urls : dict # Context: embed, view, edit 
    meta : dict # Context : view, edit 


