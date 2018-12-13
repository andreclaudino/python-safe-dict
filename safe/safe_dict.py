
class SafeDict(dict):

    def __init__(self, dictionary:dict = {}, default=None, **kwargs):
        super().__init__(**dictionary, **kwargs)
        self.default = default

    def __getitem__(self, key):
        return self.get(key, self.default)
