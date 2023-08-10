#!/usr/bin/python3
"""Model that adda user attributes by to base model"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines class that inherits from BaseModel"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
