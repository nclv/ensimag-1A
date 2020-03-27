BINS = pgcd mult fibo hello fact val_bin age affine
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

pgcd: pgcd.o fct_pgcd.o

fact: ASFLAGS += -march=rv32im 
fact: fact.o fct_fact.o

age: age.o fct_age.o

hello: hello.o fct_hello.o

affine: affine.o fct_affine.o fct_mult.o

fibo: fibo.o fct_fibo.o

val_bin: val_bin.o fct_val_bin.o

mult: mult.o fct_mult.o
