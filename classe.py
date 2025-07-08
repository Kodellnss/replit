from typing import Dict 

class drillingmachine : 
  pass

drilling_machine_two = drillingmachine()
drilling_machine_three = drillingmachine()

print(drilling_machine_two)
print(drilling_machine_three)

class Warehouse :
  def __init__(self, location, manager) : 
   self.location = location
   self.manager = manager

warehouse_one = Warehouse("Paris", "Jonh Doe")

print(warehouse_one.location)

class Warehouse :
  def __init__(self, location, manager) : 
    self.location = location
    self.manager = manager 
warehouse_two = Warehouse("Paris", "John Doe")
print(warehouse_two.manager)

class DrillingMachine:
  def __init__(self, 
               machine_id: str, 
               name: str, 
               location: str, 
               status: str, 
               specifications: Dict[str, str], 
               last_maintenance_date: str, 
               next_maintenance_due: str, 
               contact_information: Dict[str,str]
              ) -> None:
      self.machine_id = machine_id
      self.name = name
      self.location = location
      self.status = status
      self.specifications = specifications
      self.last_maintenance_date = last_maintenance_date
      self.next_maintenance_due = next_maintenance_due
      self.contact_information = contact_information
drilling_m = DrillingMachine(
  "DM-001",
  "Deep Driller 3000",
  {
      "latitude": 29.7355,
      "longitude": -95.3635,
      "region": "Gulf of Mexico",
      "country": "USA"
  },
  "active",
  {
      "depth_capacity_meters": 5000,
      "drilling_speed_meters_per_day": 200
  },
  "2024-06-01",
  "2025-06-01",
  {
      "operator_company": "OceanCore",
      "contact_person": "Emma Watson",
      "phone": "+1 555-1234",
      "email": "emma@oceancore.com"
  }
)

print(drilling_m.location)

class DrillingMachine:
  def __init__(self, machine_id, name, location, status, specifications, last_maintenance_date, next_maintenance_due, contact_information):
      self.machine_id = machine_id
      self.name = name
      self.location = location
      self.status = status
      self.specifications = specifications
      self.last_maintenance_date = last_maintenance_date
      self.next_maintenance_due = next_maintenance_due
      self.contact_information = contact_information
drilling_m = DrillingMachine(
  "DM-001",
  "Deep Driller 3000",
  {
      "latitude": 29.7355,
      "longitude": -95.3635,
      "region": "Gulf of Mexico",
      "country": "USA"
  },
  "active",
  {
      "depth_capacity_meters": 5000,
      "drilling_speed_meters_per_day": 200
  },
  "2024-06-01",
  "2025-06-01",
  {
      "operator_company": "OceanCore",
      "contact_person": "Emma Watson",
      "phone": "+1 555-1234",
      "email": "emma@oceancore.com"
  }
)

print(drilling_m.location)

class Warehouse : 
  def __init__(self,
              location : str,
              manager : str,
              storage : Dict[str, int]) -> None :
      self.location = location
      self.manager = manager
      self.storage = storage

  def avrage_storage(self) : 
    return sum(self.storage.values())/len(self.storage.values())

items = {"item1": 10, "item2": 20, "item3": 30}
warehouse_four = Warehouse("Paris", "John Doe", items)

avrage_items = warehouse_four.avrage_storage()
print(avrage_items)




  