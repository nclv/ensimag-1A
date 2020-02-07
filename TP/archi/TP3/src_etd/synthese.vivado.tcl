# Input arguments
set DEVICE         [lindex $argv 0]
set TOP            [lindex $argv 1]
set TOP_ENTITY     [lindex $argv 2]

source read_prj.vivado.tcl
read_prj ${TOP}.prj
if [file exists "${TOP}_${DEVICE}.xdc"] {
	read_xdc ${TOP}_${DEVICE}.xdc
} else {
# horloge clk à 125MHz
	read_xdc clock.xdc
}
# Detect XPM memory
auto_detect_xpm

# Start synthesis
synth_design -top ${TOP_ENTITY} -part ${DEVICE}
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
exit
