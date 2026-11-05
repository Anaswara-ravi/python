# dictionary is a store values as a key value pairs


# -ordered 
# -unindexed
# -allow duplication for values ,keyas should be unique
# -values are mutable
# -keys should be hashable
# -values can be of any type





stude = {
    "name": "abhi",
    "course": "python",
    "student id": "sssuu32",
    "age": 44,
    "hobbies": ["reading", "sleeping"]
}

print(stude)
print(type(stude))

d1 = {}
s1 = set()

print(type(d1))
print(type(s1))

stude["name"] = "rahul"  # Change existing value

stude["skills"] = ["communication", "teamwork"]  # Add new key with list

print(stude)

stude.update({"course":"python full stack"})
stude.update({"place":"pkd"})
stude.setdefault("age",22)
stude.pop("skills")
stude.popitem()
print(stude)


print(stude.keys)
print(stude.values)
print(stude.items)


for key, value in stude.items():
    print(f"{key:<10}:{value}")

#converting of dictionary into other like list ,tuple

d2=[]
d2=dict([('emp_no',3445),('emp_name',"kathik"),("dep","software")])
print(d2)

copy_stud=stude.copy()






run time error
