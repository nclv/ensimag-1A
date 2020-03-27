# Inputs arguments
set DESIGN    [lindex $argv 0]
set DEVICE    [lindex $argv 1]
set BIT_FILE  [lindex $argv 2]

# Open hardware mode
open_hw

# Connect target
connect_hw_server
refresh_hw_server
set  targets [get_hw_targets]
puts "targets: ${targets}"
current_hw_target [lindex ${targets} 0]
open_hw_target

# Select device
set  devices [get_hw_devices]
puts "devices: ${devices}"

# Program
set_property PROGRAM.FILE ${BIT_FILE} [lindex [get_hw_devices] 1]

program_hw_devices
refresh_hw_device

