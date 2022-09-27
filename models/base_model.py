"""Module with class"""

from datetime import datetime
from uuid import uuid4

import models


class BaseModel:
    """
    BaseModel class:
    Class that defines all common attributes/methods
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """constructor for instance"""
        # we need to save the kwargs value in __dict__ b/c
        # it hold will be the storing all of the attributes
        # but before saving we need to change the values of
        # created_at and updated_at to datetime b/c they are strings
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                # each key of kwargs is an attribute name
                # ach value of kwargs is the value of this attribute name

        else:
            # Public Attributes
            self.id = str(uuid4())  # creates unique id for each basemodel
            self.created_at = datetime.now()  # time of when instance created
            self.updated_at = datetime.now()

            # if it’s a new instance (not from a dictionary representation),
            # add a call to the method new(self) on storage
            models.storage.new(self)

    def __str__(self):
        """
        prints the class name,
        the id,
        and dictionery of the attributes for instance
        """
        info = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return info

    # Public methods

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance

            This method be the first piece of the
            serialization/deserialization process:
        """

        # Note: using self.__dict__,
        # only instance attributes set will be returned
        # so now we want dictionery of every info
        # we also need what is in __dict__ to be inside dic
        dic = self.__dict__.copy()
        # dic["id"] = self.id
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        # no need of str() b/c isoformat returns a string
        return dic
