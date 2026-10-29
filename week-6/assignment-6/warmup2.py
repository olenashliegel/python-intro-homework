def celsius_to_fahrenheit(c):
  """Convert celsius to fahrenheit"""
  return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
  """Convert fahrenheit to celsius"""
  return (f - 32) * 5/9

def display_result (units_of_measurement, temp_value):
  """Display result"""
  if units_of_measurement.lower() == "c":
    print (f"{temp_value}°C = {celsius_to_fahrenheit(temp_value):.1f}°F")
  else:
    print (f"{temp_value}°F = {fahrenheit_to_celsius(temp_value):.1f}°C")

if __name__ == "__main__":
  celsius_unit = "C"
  fahrenheit_unit = "F"
  display_result (celsius_unit, 0)
  display_result (celsius_unit, 100)
  display_result (fahrenheit_unit, 75)
  display_result (fahrenheit_unit, 0)
