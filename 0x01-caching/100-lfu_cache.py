#!/usr/bin/python3
"""LFU cache."""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """creates a LFUCache cache system without limit.

    methods:
        put(key, item): adds a key/value pair to cache
        get(key): gets the key value from cache
    """

    def __init__(self):
        """Init object."""
        super().__init__()
        self.uses = dict()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item
            item: The item to be added
        """
        if (key is None or item is None):
            return

        if (len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys()):
            discard_key = min(self.uses, key=self.uses.get)
            del self.cache_data[discard_key]
            del self.uses[discard_key]
            print("DISCARD: {}".format(discard_key))
        if (key in self.cache_data.keys()):
            self.uses[key] += 1
        else:
            self.uses[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to be retrieved
        """
        if (key is None or key not in self.cache_data.keys()):
            return
        self.uses[key] += 1
        return self.cache_data.get(key)
