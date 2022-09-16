"""Module with class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class:
    Class that defines all common attributes/methods
    for other classes.
    """

    # Public Attributes
    id = str(uuid4())  # creates unique id for each basemodel
    created_at = datetime.now()  # time of when instance created
    updated_at = datetime.now()

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

        dic = {}

        # we also need what is in __dict__ to be inside dic
        dic = self.__dict__
        dic["id"] = self.id
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = str(self.created_at.isoformat())
        dic["updated_at"] = str(self.updated_at.isoformat())
        return dic
