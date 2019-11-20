from decimal import Decimal

class Column:
    def __init__(self, name, kind, description=""):
        self._name = name
        self._kind = kind
        self._description = description
        
    def __str__(self): 
        _str = "col: {} : {} {}".format(self._name, self._kind, self._description)
        return _str

    def validate(self, data):
        if self._kind == 'bigint':
            if insistance(data, int):
                return True
            return False
        elif self._kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif self._kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True

class PrimaryKey(Column):
    def __init__(self, name, kind, description=None):
        super().__init__(name, kind, description=description)
        self.is_pk = True

class Relationship:
    def __init__(self, name, _from, to, on):
        self._name = name
        self._from = _from
        self._to = to
        self._on = on

class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def add_column(self, name, kind, description=""):
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        relationship = Relationship(name, self, to, on)
        self._references.append(Relationship)

    def add_referenced(self, name, by, on):
        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)
        