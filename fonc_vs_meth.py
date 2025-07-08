warehouse_one = {
    "Location": "Paris",
    "surface_area": 1040,
    "manager": "Tom Felton",
    "n_employees": 12,
    "storage": {"item1": 24, "item2": 42, "item3": 56},
 }

def qte_emp(w : dict) -> dict : 
    storage = w["storage"]
    total_s = storage["item1"] + storage["item2"] + storage["item3"]
    w["storage "] = total_s
    return w
print(qte_emp(warehouse_one))

warehouse_two = {
    "Location": "Paris",
    "surface_area": 2000,
    "manager": "Emma Watson",
    "storage": {"item1": 98, "item2": 150},
 }
print(qte_emp(warehouse_two))

    