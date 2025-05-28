from pydantic import BaseModel, Field
from typing import Annotated, Optional, List, Union, Literal

class AddOns(BaseModel):
    name: Annotated[str, Field(description="name of the add-on provided with the item")]
    add_on_price: Annotated[int, Field(description="price of the add-on given in menu")]

class Items(BaseModel):
    name: Annotated[str, Field(description="name of the item under a category")]
    description: Annotated[Optional[str], Field(description="constituents/ingredients used in the item", default=None)]
    price: Annotated[Union[int, List[int]], Field(description="price of the item in int or list of prices of the item if and only if more than one price is given")]
    type: Annotated[Optional[Literal['Veg', 'Non-veg', 'Both']], Field(description="Indicates the type of food item as Veg, Non-veg or Both", default=None)]
    add_ons: Annotated[Optional[List[AddOns]], Field(description="different ingredients available to customize the main item", default=None)]

class MenuCategories(BaseModel):
    id: Annotated[int, Field(description="unique sequential id for each category")]
    name: Annotated[str, Field(description="name of the category as per menu")]
    items: List[Items]

class RestaurantDetails(BaseModel):
    name: Annotated[Optional[str], Field(description="name of the restaurant from menu", default=None)]
    area: Annotated[Optional[str], Field(description="name of the area from the address as per menu", default=None)]
    categories: Annotated[List[MenuCategories], Field(description="different categories provided by the restaurant")]