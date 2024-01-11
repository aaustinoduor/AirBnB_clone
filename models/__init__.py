"""High level initialization of attributes"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
