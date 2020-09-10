class Country(object):
    __slots__ = "country_code","country_name","country_border_codes","country_border_names"

    def __init__(self,cd, cn):
        self.country_code = cd
        self.country_name = cn
        self.country_border_codes = []
        self.country_border_names = []

    @property
    def country_n(self):
        return  self.country_name

    def __str__(self):
        return "{} {} {}".format(self.country_code,self.country_name,self.country_border_names)


       