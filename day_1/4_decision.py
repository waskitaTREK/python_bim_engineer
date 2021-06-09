# Assign data into person
person = "Yessy"

if person == "Fahmi":           # jika person berisikan nama Fahmi
    print("Hello " + person)    # execute line ini
elif person == "Yessy":         # jika person berisikan nama Yessy
    print("Hello " + person)    # execute line ini
else:                           # jika kedua perintah diatas salah
    print("Hello Stranger")     # execute line ini


if person in ["Fahmi", "Yessy"]: # cek apakah data yg di assign sebelumnya berada dalam list yang diberikan
    print("Hello " + person)     # jika benar, execute line ini
else:                            # jika perintah diatas salah
    print("Hello stranger!")     # execute line ini


