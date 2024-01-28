a = { "name" : "john",
      "age" : 23,
      66 : "is 66",
      72 : 27
      }

print(a)
for i in a:
    print(f"{i} : {a[i]}")

# list syntax
a = [[10,20],[30,40]]
print(a[0][1])

# tuple syntax (immutable)
a = ((10,20),(30,40))
print(a[0][1])
