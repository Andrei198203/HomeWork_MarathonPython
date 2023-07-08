coll_1 = ['2', 5, 'Hello', 10]
coll_2 = [1,2,3,3]
coll_1.extend(coll_2)

coll_2.insert(1, 'world')
print(coll_1,coll_2)
print(coll_2.count(3))
print(coll_2[1:2])
