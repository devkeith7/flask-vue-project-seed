
# Example Data Object

from data_object.base_data_object import BaseDataObject
from data_store.database_driver.mysql_driver import MySqlDriver


class ExampleDataObject(BaseDataObject):
	"""
	Example Data Object
	"""


	TABLE_NAME = 'example'
	DEFAULT_DB_DRIVER_CLASS = MySqlDriver
	DEFAULT_CACHE_DRIVER_CLASS = None


	# Subclass specific methods go here...
