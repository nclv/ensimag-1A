
proc read_prj {filename} {
	puts "Read $filename"

	set fp [open $filename r]
	set file_data [read $fp]
	set lines [split $file_data "\n"]

	foreach line $lines {
		if {[regexp {(\w+)\s+(\w+)\s+\"(.+)\"}  ${line}  matched  fmt lib src]} {
			puts "Read: $fmt $lib $src"
			if {$fmt=="vhdl"} {
				read_vhdl -library $lib $src
			}
		}
	}

	close $fp
}

