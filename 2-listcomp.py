# listcomp vs. map / filter

print(f"Using listcomp ... leichter zu lesen")
symbols = '$¢£¥€¤'
ascii = [ord(s) for s in symbols if ord(s) > 127]
print (f"using listcomp: {ascii}")

print(f"Using map/filter ...")
ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(f"Using map/filter: {ascii}")

print(f"Cartesisches Produkt ...")
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
#tshirts = [(color, size) for color in colors for size in sizes]

for tshirts in (f"{color} {size}" for color in colors for size in sizes):
    print (f"tshirts: {tshirts}")
