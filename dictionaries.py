#Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guiter="Page")

# print(band)
# print(band2)
# print(type(band))
# print(len(band))

#Acess in Dictionaries

# print(band["vocals"])
# print(band.get("guitar"))

#List all keys
# print(band.keys())

#list all values
# print(band.values())

#List key/value pairs as tuples
# print(band.items())

#Verify existence of a key
# print("guitar" in band)
# print("triangle" in band)

#Change values
band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})
# print(band)

#Remove items
# print(band.pop("bass"))
# print(band)

band["drums"] = "Bonham"
# print(band)

# print(band.popitem())
# print(band)

#Delete and Clear items

del band["drums"]
# print(band)

band2.clear()
# print(band2)

del band2

#Copy Dictionaries

# band2 = band #Creates a reference, not a copy
# print("Bad copy!")
# print(band2)
# print(band)
# band2["drums"] = "Dave"
# print(band)

band2 = band.copy() #Creates a copy
#print("Good copy!")
band2["drums"] = "Dave"
# print(band)
# print(band2)

#Copy using dict constructor function

band3 = dict(band)
#print("Also a good copy!")

#Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band4 = {
    "member1": member1,
    "member2": member2
}

# print(band4)

# print(band4["member1"]["name"])

#Sets

nums = { 1, 2, 3, 4}
nums2 = set((1,2,3,4))

# print(nums, nums2, type(nums), len(nums))

#No duplicates allowed in sets

nums3 = {1,2,2,3}
# print(nums3)

#True value is a dupe(duplicate) of 1 and False is a dupe of 0

nums = {1, True, 2, False, 3, 4, 0}
# print(nums)

#Check if a value is in a set
# print(2 in nums)

##Cannot refer to an element in the set with an index position or with a key

#Adding a new element to a set

nums.add(8)
# print(nums)

#Add elements from one set to another

morenums = {5, 6, 7}
nums.update(morenums)
# print(nums)

##Can use update with lists, tuples and dictionaries as well

#merge 2 sets to create a new set

one = {1,2,3}
two = {2,3,5,6,7}

newset = one.union(two)
# print(newset)

#keep only the duplicates
# one.intersection_update(two)
# print(one)

#keep everything except the duplicates
# one.symmetric_difference_update(two)
# print(one)

