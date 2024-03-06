# Develop an in-memory LRU cache service which lets applications create a collection with a default capacity. At any point of time there can be multiple collections within the cache, each being accessed by a different application.
# Applications can access the cache service via REST APIs and should be able to do the following actions:
# Create a collection
# Update capacity of the collection
# Put data
# Get data

class LruCache:
    def __init__(self, cap):
        self.cache = {}
        self.default_cap = cap

    def put(self,app, data):
        if self.default_cap == 0:
            print("No more data can be added to this application")
            return
        if app not in self.cache:
            self.cache[app] = [data]
        elif len(self.cache[app]) == self.default_cap:
            self.cache[app].pop(0)
            self.cache[app].append(data)
            # print("No more data can be added to this application")
        else:
            self.cache[app].append(data)


    def update_cap(self,cap):
        self.default_cap = cap







