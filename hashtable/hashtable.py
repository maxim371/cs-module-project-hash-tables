class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.initial_capacity = capacity
        self.num_keys = 0
        self.num_item = 0
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.get_load_factor

    def update_load_factor(self):
        #how much space is consumed?
        self.load_factor = self.num_item/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        fnv = 2**40 + 2**8 + 0xb3
        hash = 14695981039346656037
        for x in key:
            hash = hash * fnv
            hash = hash ^ ord(x)
        return hash & 0xFFFFFFFFFFFFFFFF


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + 5) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """


        
        hashed_key = self.hash_index(key)
        link = HashTableEntry(key, value)

        node = self.storage[hashed_key]
        if node is None:
            self.storage[hashed_key] = link
            self.num_keys += 1
            return

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            prev.next = link
            self.num_keys += 1

        else:
            node.value = value

   

    def make_storage(self):
        new_storage = [None] * self.capacity

        for i in range(len(self.storage)):
            node = self.storage[i]

            while node is not None:
                hashed_key = self.hash_index(node.key)
                new_storage[hashed_key] = node
                node = node.next
        self.storage = new_storage



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #get hash_key
        hashed_key = self.hash_index(key)

        #get value stored at the hashed_key
        node = self.storage[hashed_key]

        if node.key == key:
            self.storage[hashed_key] = node.next
            self.num_keys -= 1
            self.size_check()
            return

        #traverse linkedlist until key is found or end is reached

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            print(f'{key} was not found')
            return None

        #Remove linkedpair node from chain
        prev.next = node.next
        self.num_keys -= 1
        self.size_check()


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #compute hash
        hashed_key = self.hash_index(key)

        #get first node in linkedlist storage
        node = self.storage[hashed_key]

        #traverse linkedlist until key found/end reached
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value




    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #get storage as it currently exist
        old_storage = self.storage

        #if no capacity is given
        if new_capacity is None:
            #set capacity to double required size
            new_capacity = len(self.storage) * 2

        #re-create storage with new length
        self.storage = [None] * new_capacity
        #re-create capacity
        self.capacity = new_capacity
        #for each item in old storage
        for node in old_storage:
            while node is not None:
                self.put(node.key, node.value)
                self.num_item -= 1
                node = node.next
        self.update_load_factor()



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
