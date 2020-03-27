set_param project.enableReportConfiguration 0
load_feature core
current_fileset
xsim {work.tb_VGA} -wdb {tb_VGA_isim_beh.wdb} -autoloadwcfg -tclbatch {./run.tcl}
