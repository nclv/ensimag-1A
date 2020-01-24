# Input arguments
set DEVICE         [lindex $argv 0]
set TOP            [lindex $argv 1]
set TARGET         [lindex $argv 2]
set ENABLE_MEM     [expr [lindex $argv 3]]


source read_prj.vivado.tcl
read_prj ${TOP}.prj
#
# Reading constraint file (.xdc file)
read_xdc ${TOP}_${DEVICE}.xdc

# Detect XPM memory
auto_detect_xpm

# Start synthesis
synth_design -top ${TOP} -part ${DEVICE}
report_utilization -file ${TOP}_utilization.rpt
report_timing_summary -file ${TOP}_timing.rpt

get_ports *

set filename "${TOP}_summary.rpt"
set fileId [open $filename "w"]
if { [get_clocks] != "" } {
	puts -nonewline $fileId "Clock  | " 
	puts $fileId [get_property -min PERIOD [get_clocks]];
	puts -nonewline $fileId "Slack  | "
	puts $fileId [get_property SLACK [get_timing_paths]];
}
close $fileId

#TODO factoriser cette partie en utilisant synthese.vivado.tcl

# Run logic optimization
opt_design
#write_checkpoint -force opt_design.dcp

# Placing
place_design -directive Quick
#write_checkpoint -force place_design.dcp

# Routing
route_design -directive Quick -ultrathreads
write_checkpoint -force route_design.dcp

if { ${ENABLE_MEM} } {
    # Generate MMI map
    set MMI_FILE ${TOP}.mmi
    write_mem_info -force ${MMI_FILE}
}

# Create bitstream
write_bitstream -force ${TARGET}

exit
