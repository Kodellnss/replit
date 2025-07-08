def zfill_machine_id(machine_id: str) -> str :
  l,c = machine_id.split("-")
  c_f = c.zfill(3)
  return l + "-" + c_f