#!/usr/bin/python3
"""
City Class from Models Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class handles all application cities"""
    state_id = ""
    name = ""
