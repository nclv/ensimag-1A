TOP 	  = auto
#Liste des TOP autorisés
TOP_OK	  = auto auto_unparmin auto_implicite decod_nrzi 

ifndef TOP_ENTITY
	TOP_ENTITY = $(TOP)
endif

FPGA	  = xc7z010-clg400-1

SIMU_WDB  = $(TB_ENTITY)_isim_beh.wdb

REPORTS = $(filter %.rpt, $(wildcard *))

TOCLEAN = $(filter %log %.jou \
                   %.mmi \
                   $(addsuffix .prj,$(TOP_OK)) %.wdb xvhdl% xelab% xsim% vivado% updatemem% usage_statistics_webtalk%,$(wildcard *))

TOCLEAN += $(REPORTS)

TOPOLISH = $(TOCLEAN) download.bit $(wildcard _*) $(wildcard *.dcp) .Xil $(wildcard /tmp/*.xilwvdat)


VERB     := 0
q         = $(if $(filter 1, $(VERB)),$1,\
				$(if $(2),@echo $2 && $1 > $3 2>&1, @$1))

ifdef MEM_FILE
	TARGET:=golden.bit
	MMI_FILE:=$(TOP).mmi
else
	TARGET:=download.bit
endif

# Verification que l'environement de Xilinx Vivado a bien été sourcé
ifeq ($(origin XILINX_VIVADO), undefined)
  $(error "Outils Xilinx introuvables, lancez d'abord la commande: source /bigsoft/Xilinx/Vivado/2019.1/settings64.sh")
endif
XILINX_PREFIX := $(XILINX_VIVADO)/bin/

# Verification que le TOP est autorisé
ifeq ($(filter $(TOP),$(TOP_OK)),)
  $(error Toplevel $(TOP) inconnu)
endif

# Les Toplevels du TP
  TOP_REEL	:= $(TOP)
  TB_ENTITY	:= tb_$(TOP_ENTITY)
  PRJ  		:= tb_$(TOP).prj


COMMON_DIR ?= .
VHD_TB := $(shell sed -e 's/vhdl work "\(.*\)"/\1 /' $(PRJ))
VHD_SRC := $(shell grep -i -v -- "$(TB_ENTITY)" $(PRJ) > $(TOP).prj ; sed -e 's/vhdl work "\(.*\)"/\1 /' $(TOP).prj)


all: analyse

.PHONY: analyse elaboration synthese synthese run_fpga clean realclean cleanreports

## Regles de simulation

analyse: $(VHD_TB)
	@echo "  Analyse"
	@$(XILINX_PREFIX)xvhdl -prj $(PRJ) -nolog | tee $@.log | grep -E "ERROR" ; exit $$(( ! $$? ))

elaboration: analyse
	$(call q,\
	    $(XILINX_PREFIX)xelab work.$(TB_ENTITY) -nolog -debug typical \
	    , "  Elaboration",$@.log)

run_simu: elaboration
	$(call q,\
	    $(XILINX_PREFIX)xsim work.$(TB_ENTITY) -nolog -gui -wdb $(SIMU_WDB) $(MAGIC_VIEW) -tclbatch $(COMMON_DIR)/run.tcl\
	    , "  Simulation",$@.log)


## Regles de synthese

ifdef MEM_FILE
ENABLE_MEM := 1
download.bit: $(TARGET) $(MEM_FILE) $(MMI_FILE)
	$(call q, $(XILINX_PREFIX)updatemem -debug -force --meminfo $(MMI_FILE) --data $(MEM_FILE) --proc $(MEM_ID) --bit $< --out $@\
	    , "  MAJ du fichier de configuration", $@.mem.log)
else
ENABLE_MEM := 0
endif


synthese: $(TOP)_utilization.rpt $(TOP)_timing.rpt $(TOP)_summary.rpt 
	@echo "Rapport d'utilisation disponible dans $(TOP)_utilization.rpt"
	@echo "Rapport de timing disponible dans $(TOP)_timing.rpt"
	@python3 parse_report.py $^

$(TOP)_utilization.rpt $(TOP)_timing.rpt $(TOP)_summary.rpt: $(COMMON_DIR)/synthese.vivado.tcl $(MEM_FILE) $(VHD_SRC)
	$(call q, \
	    $(XILINX_PREFIX)vivado -nolog -nojournal -mode batch -source $< -tclargs $(FPGA) $(TOP_REEL) $(TOP_ENTITY)\
	    , "  Synthese",$@.log)


$(TARGET): $(COMMON_DIR)/bitstream.vivado.tcl $(VHD_SRC) $(TOP)_$(FPGA).xdc
	$(call q, \
	    $(XILINX_PREFIX)vivado -nolog -nojournal -mode batch -source $< -tclargs $(FPGA) $(TOP_REEL) $@ $(ENABLE_MEM) \
	    , "  Génération du bitstream",$@.log)

run_fpga: download.bit $(COMMON_DIR)/programFPGA.vivado.tcl
	$(call q, \
	    $(XILINX_PREFIX)vivado -nolog -nojournal -mode batch -source $(COMMON_DIR)/programFPGA.vivado.tcl -nolog -nojournal \
	                           -tclargs $(FPGA) $(TOP_REEL) $< \
	    , "  Programmation",prog.log )

$(TOP)_$(FPGA).xdc:
	$(error Programmation non prévue pour le toplevel $(TOP_REEL))

cleanreports:
	$(call q, rm -rf $(REPORTS),)

clean: 
	$(call q, rm -rf $(TOCLEAN),)

realclean: clean cleanreports 
	$(call q, rm -rf $(TOPOLISH),)
