import wmi #normal c'est pour Windows

def get_cpu_temperature():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()
        
        for temp in temperature_info:
            temperature = (temp.CurrentTemperature / 10.0) - 273.15  # Convert to Celsius
            print(f"CPU Temperature: {temperature:.2f} °C")
            return temperature

    except Exception as e:
        print(f"Could not get CPU temperature: {e}")
        return None

get_cpu_temperature()




