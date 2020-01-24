set_param project.enableReportConfiguration 0
load_feature core
current_fileset
xsim {work.tb_AC} -wdb {tb_AC_isim_beh.wdb} -autoloadwcfg -tclbatch {./run.tcl}
