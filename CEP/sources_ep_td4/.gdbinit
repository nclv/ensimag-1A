#connection automatique au stub GDB de QEMU
target remote :1234

# Modification du prompt gdb 
set prompt \001\033[1;36m\002(gdb-CEP) \001\033[0m\002
