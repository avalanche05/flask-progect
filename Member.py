import json


class Member:
    def __init__(self, firstname, lastname, photo_link, profession_list):
        self.firstname = firstname
        self.lastname = lastname
        self.photo_link = photo_link
        self.profession_list = profession_list

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
