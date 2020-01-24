set_param project.enableReportConfiguration 0
load_feature core
current_fileset
xsim {work.tb_div_freq} -wdb {tb_div_freq_isim_beh.wdb} -autoloadwcfg -tclbatch {./run.tcl}
