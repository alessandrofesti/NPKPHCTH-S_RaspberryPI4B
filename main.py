from pymodbus.client.sync import ModbusSerialClient as ModbusClient

def get_sensor_values():
    # Use a breakpoint in the code line below to debug your script.

    # Configura il client Modbus
    client = ModbusClient(method='rtu',
                          port='/dev/ttyUSB0',
                          baudrate=4800,
                          stopbits=1,
                          bytesize=8,
                          parity='N',
                          timeout=1)

    # Connessione al dispositivo
    if client.connect():
        print("Connected to the sensor")

        # Effettua la lettura dal sensore
        try:
            # Leggi 7 registri a partire dall'indirizzo 0 (Humidity, Temperature, EC, pH, N, P, K)
            response = client.read_input_registers(address=0, count=7, unit=1)

            if not response.isError():

                humidity = response.getRegister(0) / 10.0  # Umidità in percentuale
                temperature = response.getRegister(1) / 10.0  # Temperatura in °C
                ec = response.getRegister(2)  # EC in us/cm
                ph = response.getRegister(3) / 10.0  # pH
                nitrogen = response.getRegister(4)  # Azoto in mg/kg
                phosphorus = response.getRegister(5)  # Fosforo in mg/kg
                potassium = response.getRegister(6)  # Potassio in mg/kg

                print(f"Humidity: {humidity}%")
                print(f"Temperature: {temperature}°C")
                print(f"EC: {ec} µS/cm")
                print(f"pH: {ph}")
                print(f"Nitrogen (N): {nitrogen} mg/kg")
                print(f"Phosphorus (P): {phosphorus} mg/kg")
                print(f"Potassium (K): {potassium} mg/kg")
            else:
                print("Sensor read error:", response)
        finally:
            client.close()
    else:
        print("Failed to connect to the sensor")


if __name__ == '__main__':
    get_sensor_values()

