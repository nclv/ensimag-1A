set_param project.enableReportConfiguration 0
load_feature core
current_fileset
xsim {work.tb_PO} -wdb {tb_PO_isim_beh.wdb} -autoloadwcfg -tclbatch {./run.tcl}
