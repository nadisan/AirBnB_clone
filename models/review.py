#!/usr/bin/python3
"""Model that adda user attributes by to base model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines class that inherits from BaseModel"""
    
    place_id = ''
    user_id = ''
    text = ''
