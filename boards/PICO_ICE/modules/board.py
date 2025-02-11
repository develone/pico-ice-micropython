import machine, os

fpga_spi = None
pmod_spi = None
i2c = None
fpga_uart = None

if "pico2-ice" in os.uname().machine:
	fpga_spi = machine.SPI(0)
	pmod_spi = machine.SPI(1)
	i2c = machine.I2C(1)
elif "pico-ice" in os.uname().machine:
	fpga_spi = machine.SPI(1)
	pmod_spi = machine.SPI(0)
	i2c = machine.I2C(0)
	fpga_uart = machine.UART(0)

del machine
del os
