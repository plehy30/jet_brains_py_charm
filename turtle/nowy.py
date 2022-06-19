powitanie = "Witam"
typ_zmiennej = type(powitanie)
print(typ_zmiennej)

name = "Brian"
age = 30
specjalne_powitanie = "Witaj %s!, lat %d" % (name, age)
print(specjalne_powitanie)

nowe_powitanie=f"Witaj {name}, lat {age}!"
print(nowe_powitanie)
