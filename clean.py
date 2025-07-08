machine_one = {
  "machine_id": "DM-001",
  "name": "Deep Driller 3000",
  "location": {
    "latitude": 29.7355,
    "longitude": -95.3635,
    "region": "Gulf of Mexico",
    "country": "USA"
  },
  "status": "Operational",
  "specifications": {
    "type": "Offshore",
    "depth_capacity_meters": 10000,
    "drilling_speed_meters_per_day": 300,
    "crew_size": 40,
    "power_source": ["Diesel, Electric"]
  },
  "last_maintenance_date": "10/07/2024",
  "next_maintenance_due": "10/12/2024",
  "contact_information": {
    "operator_company": "Oceanic Drilling Inc.",
    "contact_person": "John Smith",
    "phone": "+1-555-123-4567",
    "email": "john.smith@oceanicdrilling.com"
  }
}

machine_two = {
  "machine_id": "DM-2",
  "name": "Land Rover 200",
  "location": {
    "latitude": 37.7749,
    "longitude": -107.9090,
    "region": "San Juan Basin",
    "country": "USA"
  },
  "status": "Under Maintenance",
  "specifications": {
    "type": "Onshore",
    "depth_capacity_miles": 7,
    "drilling_speed_miles_per_day": 0.3,
    "crew_size": 25,
    "power_source": "Electric"
  },
  "last_maintenance_date": "2024-07-15",
  "next_maintenance_due": "2025-01-15"
}

def harmonize_machines(machine_two : dict) -> dict :
  return machine_two

def miles_to_meters(machine_two : dict) -> dict :
  machine_two["specifications"]["depth_capacity_miles"] = machine_two["specifications"]["depth_capacity_miles"] * 1.609
  return machine_two
print(miles_to_meters(machine_two))

def fonction_date(machine_two : dict) -> dict :
  sp = machine_two["last_maintenance_date"].split("-")
  sp_rev = sp[::-1]
  machine_two["last_maintenance_date"] = "/".join(sp_rev)
  return machine_two
print(fonction_date(machine_two))

def put_contact_info(machine_two : dict) -> dict : 
  machine_two["contact_information"] = machine_one["contact_information"]
  return machine_two

def format_machine_id(machine_two : dict) -> dict : 
  m = machine_two["machine_id"].split("-")
  m[1] = m[1].zfill(3)
  machine_two["machine_id"] = "-".join(m)
  return machine_two
print(format_machine_id(machine_two))