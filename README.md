# Blue Pill Black Magic Installer

This PlatformIO project installs Black Magic debugger firmware on a Blue Pill STM32F103C8 board. It builds a dummy program, then a pre-upload script replaces the binaries with prebuilt binaries for Black Magic. It can be uploaded using the serial bootloader, an STLink, or another Black Magic - you will need to change `platformio.ini` accordingly.

This build of Black Magic uses the SWD pins to connect to the debug target, so you will not be able to reflash the microcontroller through SWD while Black Magic is running. Instead, use the jumpers to enter the serial bootloader, and then reflash either using the bootloader itself or another SWD adapter.

To connect to another Blue Pill, connect the pins on the debug header straight across - SWCLK to SWCLK, SWDIO to SWDIO, and GND to GND. Connect 3V3 to 3V3 only if you need to power the target. In `platformio.ini`, set `upload_protocol` and `debug_tool` to blackmagic, and `upload_port`/`debug_port` to the serial port that the device provides.

There are actually two serial ports that show up from the device. One is for debugging and uploading code, and the other goes to a hardware serial port so you can use this as a USB-serial adapter at the same time. (TODO: figure out what pins these are.) You want the former, which is most likely the lower numbered one.

To build the Black Magic firmware yourself, find the source code at https://github.com/blacksphere/blackmagic, and build with the make option `PROBE_HOST=swlink`. To create a binary that does not depend on the DFU bootloader, replace `0x8002000` with `0x800000` in `src/platforms/swlink/Makefile.inc`

The particular commit the binaries included here were built from is:

https://github.com/blacksphere/blackmagic/commit/805464db23cf07f085d5042f46e01b4c9e7b62fd