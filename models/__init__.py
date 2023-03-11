from models.engine import file_storage
storage = file_storage.FileStorage()
cls_init = file_storage.FileStorage.cls_init
storage.reload()