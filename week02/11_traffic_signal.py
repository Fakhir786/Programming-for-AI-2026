traffic_density=input("Enter traffic density as: Low, Medium, High:").strip().lower()
emergency_vehicle=input("If emergency vehicle is present type 'yes' otherwise 'no':")
green_light=20
if emergency_vehicle=="no":
  if traffic_density== "low":
    green_light=20

  elif traffic_density== "medium":
    green_light=40

  elif traffic_density== "high":
    green_light=60

  else:
    print("Unrecognized Density")
  print(f"Green Light in {green_light} seconds")
else:
  green_light=0
  print(f"Emergency Override- Green Light in {green_light} seconds")