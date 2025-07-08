contact_informations = {
  "operator_company": "Pacific Drilling Inc.",
  "contact_person": "Smith John",
  "phone": "+1-555-123-4567",
  "email": "john.smith@oceanicdrilling.com",
}

for test in contact_informations.items():
  print(test)
  print(f"clé: {test[0]}, valeur: {test[1]}")

# pro tip:
# passez un peu de temps à essayer de comprendre ce qu'il se passe ici ;)
for key, value in contact_informations.items():
  print(f"clé: {key}, valeur: {value}")


