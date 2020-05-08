#connection automatique au stub GDB de QEMU
target remote :1234

# Modification du prompt gdb 
set prompt \001\033[1;36m\002(gdb-CEP) \001\033[0m\002
# Besoin de remapper le traitant d'interruption pour QEMU
#add-symbol-file ../../../tools/build/newlib/mips-elf/libgloss/mips/cep_excp.o 0x80000000 
