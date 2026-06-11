from stores import retail_store

class TestStores:
    def test_store_initializatino(self):
        """
        Confirm class instatiates with the correct attributes
        """

        store = retail_store((0,1), "A", 15)

        assert len(store.location) == 2
        assert type(store.brand) == str
        assert type(store.brand) == int