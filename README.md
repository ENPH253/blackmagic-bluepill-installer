# Blue Pill Black Magic Installer

This PlatformIO project installs Black Magic debugger firmware on a Blue Pill STM32F103C8 board. It builds a dummy program, then a pre-upload script replaces the binaries with prebuilt binaries for Black Magic. It can be uploaded using the serial bootloader, an STLink, or another Black Magic - you will need to change `platformio.ini` accordingly.

This build of Black Magic uses the SWD pins to connect to the debug target, so you will not be able to reflash the microcontroller through SWD while Black Magic is running. Instead, use the jumpers to enter the serial bootloader, and then reflash either using the bootloader itself or another SWD adapter.

To connect to another Blue Pill, connect the pins on the debug header straight across - SWCLK to SWCLK, SWDIO to SWDIO, and GND to GND. Connect 3V3 to 3V3 only if you need to power the target. In `platformio.ini`, set `upload_protocol` and `debug_tool` to blackmagic, and `upload_port`/`debug_port` to the serial port that the device provides.

There are actually two serial ports that show up from the device. One is for debugging and uploading code, and the other goes to a hardware serial port so you can use this as a USB-serial adapter at the same time. (TODO: figure out what pins these are.) You want the former, which is most likely the lower numbered one.

To build the Black Magic firmware yourself, find the source code at https://github.com/fb39ca4/blackmagic, and build with the make option `PROBE_HOST=bluepill` The particular commit the binaries were built from here is:

https://github.com/fb39ca4/blackmagic/tree/5e0f4d8d8aa661b011bddad31ffee1115692e273