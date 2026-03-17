em_dict = {}
print(type(em_dict))

em_dict = {"name": "Dhiwagar", "age": 22, "is_active": True}
print(em_dict)
print(em_dict.get("names", "Not Found"))
em_dict["name"] = "Dhiwagar S"
print(em_dict)
em_dict["phone_no"] = 8903681665
print(em_dict)
editing = {"name": "Dhiwagar", "age": 22, "is_active": True}
editing["name"] = "Dhiwagar S" 
editing["phone_no"] = 8903681665
print(editing)
del editing["age"]
print(editing)
pop_operation = editing.pop("is_active")
print(pop_operation)
editing.clear()
print(editing)