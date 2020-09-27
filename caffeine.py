# params
halflife = 5 # hours
daily_intake = 150 # mg
max_days_to_simulate = 30
blood_caffeine = 0 # starting uncaffeinated
tol = 0.001 # iteration tolerance

# scratch
old_bcl = 0 # holder for old blood caffeine level
num_halfs = 24.0 / halflife
print(f"assuming {num_halfs} half-lifes of caffeine occur daily")

for i in range(max_days_to_simulate):
    blood_caffeine += daily_intake
    blood_caffeine = blood_caffeine / 2**num_halfs
    print(f"blood caffeine level at end of day {i}: {blood_caffeine}")
    if blood_caffeine - old_bcl < tol:
        break
    old_bcl = blood_caffeine
