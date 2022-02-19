""" A basic client demonstrating how to use pysolarmanv5."""
from pysolarmanv5.pysolarmanv5 import PySolarmanV5
import time
import json

def main():
    """Create new PySolarman instance, using IP address and S/N of data logger

    Only IP address and S/N of data logger are mandatory parameters. If port,
    mb_slave_id, and verbose are omitted, they will default to 8899, 1 and 0
    respectively.
    """
    modbus = PySolarmanV5(
        "192.168.4.69", 1722428994, port=8899, mb_slave_id=1, verbose=1
    )

    start = 0x20c
    end = 0x240
    amount = end - start
    finish = end - 0x0

    #data = modbus.read_holding_registers(register_addr=start, quantity=amount)
    data = modbus.read_holding_registers(register_addr=start, quantity=50)

    print(data)

    dataDict = dict(
        Inverter_Freq = data[0x20c-start] / 100.0,
        Battery_ChargeDischargePwr = data[0x20d-start] * 10.0,
        Battery_Cycles = data[0x22c-start],
        Battery_ChrgLevel = data[0x210-start],
        Battery_Temp = data[0X211-start],
        Grid_IO_Pwr = data[0x212-start] * 10.0,
        House_Consumption_Pwr = data[0x213-start] * 10.0,
        Internal_IO_Pwr = data[0x214-start] *10.0,
        PV_Generation_Pwr = data[0x215-start] *10.0,
        EPS_Output_V = data[0x216-start] / 10.0,
        EPS_Output_Pwr = data[0x217-start] * 10.0,
        TodayGeneratedSolar_Wh = data[0x218-start] * 10.0,
        TodaySoldSolar_Wh = data[0x219-start] * 10.0,
        TodayBoughtGrid_Wh = data[0x21a-start] * 10.0,
        TodayConsumption_Wh = data[0x21b-start] * 10.0,
        TotalLoadConsumptionH = data[0x222-start] * 0xffff,
        TotalLoadConsumption = (data[0x222-start] * 0xffff) + data[0x223-start],
        InverterInternalTemp = data[0x238-start],
        InverterHeatsinkTemp = data[0x239-start]
    )
    
    print(json.dumps(dataDict))
    

    # """Query six input registers, results as a list"""
    # print(modbus.read_input_registers(register_addr=33022, quantity=6))

    # """Query six holding registers, results as list"""
    # print(modbus.read_holding_registers(register_addr=43000, quantity=6))

    # """Query single input register, result as an int"""
    # print(modbus.read_input_register_formatted(register_addr=33035, quantity=1))

    # """Query single input register, apply scaling, result as a float"""
    # print(
    #     modbus.read_input_register_formatted(register_addr=33035, quantity=1, scale=0.1)
    # )

    # """Query two input registers, shift first register up by 16 bits, result as a signed int, """
    # print(
    #     modbus.read_input_register_formatted(register_addr=33079, quantity=2, signed=1)
    # )

    # """Query single holding register, apply bitmask and bitshift left (extract bit1 from register)"""
    # print(
    #     modbus.read_holding_register_formatted(
    #         register_addr=43110, quantity=1, bitmask=0x2, bitshift=1
    #     )
    # )


if __name__ == "__main__":
    main()