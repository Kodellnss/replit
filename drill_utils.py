from typing import Dict
import json 

with open("fichier.json", "r") as fichier :
  fichier = json.load(fichier)
with open("fich.json", "r") as fich :
  fich = json.load(fich)

def fonction_km (fichier : dict ) -> dict : 
  conversion = fichier["specifications"]["depth_capacity_miles"] * 1.609
  fichier["specifications"]["depth_capacity_miles"] = conversion
  return fichier

print(fonction_km(fichier))

def fonction_date (fichier : dict) -> dict : 
  bd = "/".join(fichier["last_maintenance_date"].split("-")[::-1]) 
  fichier["last_maintenance_date"] = bd
  return fichier
print(fonction_date(fichier))

def ajout_info (fichier : dict) -> dict : 
  fichier["contact_information"] = fich["contact_information"]
  return fichier
print(ajout_info(fichier))

def machine_format(fichier : dict) -> dict : 
  l,c = fichier["machine_id"].split("-")
  c_fill = c.zfill(3)
  fichier["machine_id"] = l + "-" + c_fill
  return fichier
print(machine_format(fichier))



