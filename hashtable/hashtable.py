class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # find a HashTableEntry based on a given key if it exists
    # and return the value
    def find(self, key):
        # start at the head of the list
        cur = self.head

        # loop through each HashTableEntry until we find the key
        while cur is not None:
            if cur.key == key:
                # if we find the node return it
                return cur

            cur = cur.next

        # if key not found return None
        return None

    # adds a node to the head of the list
    def insert_at_head(self, node):
        # set the node's next to the head
        node.next = self.head

        # set the head to point to the newly added node
        self.head = node

    # inserts a new HashTableEntry or overwrites the value if it exists
    def insert_or_overwrite(self, key, value):
        # check to see if the key exists already
        node = self.find(key)

        # if the key doesn't exist make a new entry
        if node is None:
            self.insert_at_head(HashTableEntry(key, value))
        # otherwise overwrite the value
        else:
            node.value = value

    def delete(self, key):
        cur = self.head
        # check if the node we are removing is the head
        if cur.key == key:
            # if it's the head move the head to the next node
            self.head = cur.next

            return cur

        # keep track of the prev and cur nodes as we move through the list
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next

                return cur

            else:
                prev = cur
                cur = cur.next


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity if capacity > MIN_CAPACITY else MIN_CAPACITY
        self.table = [LinkedList()] * self.capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # (load factor) = (number of elements) / (number of slots)
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        h = 5381

        for b in key:
            h = ((h << 5) + h) + ord(b)

        return h & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # find the index the key will be stored at
        index = self.hash_index(key)

        # check if the key already exists
        entry = self.table[index].find(key)

        if entry is not None:
            # if it does overwrite the value
            self.table[index].insert_or_overwrite(key, value)

        else:
            # otherwise increase the count of items in the table
            self.count += 1

            # check to see if a resize is needed
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
                # update index for this key since it will be based of capacity
                index = self.hash_index(key)

        # insert the new item
        self.table[index].insert_or_overwrite(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # find the index this key is stored at
        index = self.hash_index(key)

        # assign the value at the index to None (delete the value stored there)
        if self.table[index] is not None:
            self.table[index].delete(key)
            self.count -= 1
            # check to see if a resize is needed
            if self.get_load_factor() < 0.2:
                # find new reduced capacity
                new_capacity = self.capacity / 2

                # if reduced capacity is >= to MIN_CAPACITY then we can resize
                if new_capacity >= MIN_CAPACITY:
                    self.resize(int(new_capacity))
        else:
            print('Warning: key not found in table!')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # find the index the key is stored in
        index = self.hash_index(key)

        entry = self.table[index].find(key)

        # if nothing is stored at this index return None
        if entry is None:
            return None
        # return the value stored at that index in the list
        else:
            return entry.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # set a ref to the old table
        old_table = self.table

        # update the capacity with the new_capacity
        self.capacity = new_capacity

        # create a new empty table
        self.table = [LinkedList()] * self.capacity

        # reset the count
        self.count = 0

        # loop through all values in old table and insert into the new table
        for i in old_table:
            cur = i.head

            while cur is not None:
                self.put(cur.key, cur.value)
                cur = cur.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
