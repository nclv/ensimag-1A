set_param project.enableReportConfiguration 0
load_feature core
current_fileset
xsim {work.tb_system} -wdb {tb_system_isim_beh.wdb} -view {{magic.wcfg}} -tclbatch {./run.tcl}
