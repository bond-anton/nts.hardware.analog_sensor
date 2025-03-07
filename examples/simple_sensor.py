from nts.hardware.analog_sensor import LinearSensor


if __name__ == "__main__":
    my_sensor = LinearSensor("LinearSensor", gain=2, offset=0)
    voltage = 3.3
    value = my_sensor.convert_voltage(voltage)

    print(f"Sensor reading {voltage} V. Sensor data: {value}.")
