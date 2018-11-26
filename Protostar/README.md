# Protostar

## About

Protostar introduces the following in a friendly way:

* Network programming
* Byte order
* Handling sockets
* Stack overflows
* Format strings
* Heap overflows

The above is introduced in a simple way, starting with simple memory corruption and modification, function redirection, and finally executing custom shellcode.

In order to make this as easy as possible to introduce Address Space Layout Randomisation and Non-Executable memory has been disabled. If you are interested in covering ASLR and NX memory, please see the Fusion page.

## Download

Download the ISO from [Google Drive](https://drive.google.com/open?id=1ydZi-KADeqOIAGUV5TSafg9JDk-fWcjS).

## Getting started

Once the virtual machine has booted, you are able to log in as the “user” account with the password “user” (without the quotes).

The levels to be exploited can be found in the /opt/protostar/bin directory.

For debugging the final levels, you can log in as root with password “godmode” (without the quotes)

## Core Files

README! The `/proc/sys/kernel/core_pattern` is set to `/tmp/core.%s.%e.%p`. This means that instead of the general ./core file you get, it will be in a different directory and different file name.

