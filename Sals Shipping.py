# Tables of prices were given in Codecademy.

weight = 41.5

# Ground Shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground cost is: " + str(cost_ground))

# Premium Shipping

cost_ground_premium = 125.0
print("Premium cost is: " + str(cost_ground_premium))

# Drone Shipping

if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Drone cost is: " + str(cost_drone))