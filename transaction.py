class InMemoryDB:
    def __init__(self):
        self.transaction_in_progress = False
        self.transactions = {}

    def begin_transaction(self):
        self.transaction_in_progress = True
        self.transactions_copy = self.transactions.copy()

    def put(self, key, value):
        if self.transaction_in_progress:
            self.transactions_copy[key] = value
        else:
            raise ValueError("Error, transaction not in progress.")

    def get(self, key):
        if key in self.transactions:
            return self.transactions[key]
        else:
            return None

    def commit(self):
        if self.transaction_in_progress:
            self.transaction_in_progress = False
            self.transactions = self.transactions_copy
        else:
            raise ValueError("Error, transaction not in progress.")

    def rollback(self):
        if self.transaction_in_progress:
            self.transaction_in_progress = False
        else:
            raise ValueError("Error, transaction not in progress.")


# test our object now #
inmemoryDB = InMemoryDB()

inmemoryDB.get("A")

# inmemoryDB.put("A", 5)

inmemoryDB.begin_transaction()

inmemoryDB.put("A", 5)

inmemoryDB.get("A")

inmemoryDB.put("A", 6)

inmemoryDB.commit()

inmemoryDB.get("A")

# throws an error, because there is no open transaction
# inmemoryDB.commit()

# throws an error because there is no ongoing transaction
# inmemoryDB.rollback()

# should return null because B does not exist in the database
inmemoryDB.get("B")

# starts a new transaction
inmemoryDB.begin_transaction()

# Set key B’s value to 10 within the transaction
inmemoryDB.put("B", 10)

# Rollback the transaction - revert any changes made to B
inmemoryDB.rollback()

# Should return null because changes to B were rolled back
inmemoryDB.get("B")
