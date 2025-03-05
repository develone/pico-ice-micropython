# pico-ice-micropython
Micropython for pico-ice and pico2-ice from tinyVision.ai

# To build
For riscv, you may add `-DPICO_GCC_TRIPLE=riscv64-unknown-elf` to the cmake command if your 'riscv64' compiler supports rp2350/rv32.

- `git submodule update --init lib/micropython`
- `git submodule update --init lib/pico-ice-mpy-module`
- `cd lib/pico-ice-mpy-module && git submodule update --init pico-ice-sdk && cd ../..`
- `make -C lib/micropython/mpy-cross -j4`
- `make -C lib/micropython/ports/rp2 submodules`
- `cd boards/PICO_ICE`
- `mkdir build && cd build`
- `cmake -DPICO_BOARD=pico2_ice ..` or `cmake -DPICO_BOARD=pico_ice ..` or `cmake -DPICO_BOARD=pico2_ice -DPICO_PLATFORM=rp2350-riscv ..`
- `make -j8`

## Troubleshooting

- "Cannot find function pico_find_compiler_with_triples"
This is a spurious pico-sdk error, if it happens, leave and delete the build directory, close your terminal, and repeat the process from mkdir.

# To use

- pico2-ice: 
```python
from machine import Pin
import ice
fpga = ice.fpga(cdone=Pin(40), clock=Pin(21), creset=Pin(31), cram_cs=Pin(5), cram_mosi=Pin(4), cram_sck=Pin(6), frequency=48)
file = open("bitstream.bin", "br")
fpga.start()
fpga.cram(file)
```
- pico-ice:
```python
from machine import Pin
import ice
fpga = ice.fpga(cdone=Pin(26), clock=Pin(24), creset=Pin(27), cram_cs=Pin(9), cram_mosi=Pin(8), cram_sck=Pin(10), frequency=48)
file = open("bitstream.bin", "br")
fpga.start()
fpga.cram(file)
```
