#!/usr/bin/python3
""" Model that creates a unique file storage for the application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
