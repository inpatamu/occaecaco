# List of hourly solar radiation values for 24 hours (in kWh/m^2)
hourly_solar_radiation_values = [
    0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
    1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8
]

# Calculate the total daily solar radiation by summing up hourly values
total_daily_solar_radiation = sum(hourly_solar_radiation_values)

# Print the result
print(f"Total daily solar radiation: {total_daily_solar_radiation} kWh/m^2")
