skumriq_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())
palamud_price = skumriq_price * 1.6
safrid_price = caca_price * 1.8
midi_price = 7.50
palamud_ppk = palamud_kg * palamud_price
safrid_ppk = safrid_kg * safrid_price
midi_ppk = midi_kg * 7.50
total = (palamud_ppk + safrid_ppk + midi_ppk)
print("{:.2f}".format(total))
