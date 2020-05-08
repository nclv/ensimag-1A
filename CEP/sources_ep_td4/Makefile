BINS = abr tri_nain tri_nain_opt tri_nain_superopt

RVDIR = /matieres/3MMCEP/riscv
AS = $(RVDIR)/bin/riscv32-unknown-elf-gcc
ASFLAGS = -g -c
CC = $(AS)
CFLAGS = -nostdinc -Wall -Wextra -g -std=c99 -mabi=ilp32 -mcmodel=medany -ffunction-sections -fdata-sections -g
CFLAGS += -I$(RVDIR)/include
LD = $(AS)
LDFLAGS = -L$(RVDIR)/lib -L$(RVDIR)/lib/cep_riscv_no_it
LDFLAGS += -T cep.ld -nostartfiles -nostdlib -static -Wl,--nmagic -Wl,--gc-sections

.PHONY: all

all: $(BINS)

%.o: %.S
	$(AS) $(ASFLAGS) -o $@ $<

%.o: %.s
	$(AS) $(ASFLAGS) -o $@ $<

OBJS = $(foreach f, $(BINS), $(addsuffix .o, $f)) \
	$(foreach f, $(BINS), $(addprefix fct_, $(addsuffix .o, $f)))

.PHONY: clean
clean:
	$(RM) $(BINS) $(OBJS) $(TMPOBJS)
CFLAGS=-O3

abr: abr.o fct_abr.o
tri_nain: tri_nain.o fct_tri_nain.o
tri_nain_opt: tri_nain_opt.o fct_tri_nain.o
tri_nain_superopt: tri_nain_superopt.o fct_tri_nain.o

tri_nain_opt.o: tri_nain.c
	$(CC) $(CFLAGS) -DOPT -c -o $@ $<

tri_nain_superopt.o: tri_nain.c
	$(CC) $(CFLAGS) -DSUPEROPT -c -o $@ $<
