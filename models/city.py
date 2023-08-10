#!/usr/bin/python3
"""Model that adda user attributes by to base model"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines class that inherits from BaseModel"""
    state_id = ''
    name = ''
