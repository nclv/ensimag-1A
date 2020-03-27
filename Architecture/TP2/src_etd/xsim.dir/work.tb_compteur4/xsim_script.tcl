set_param project.enableReportConfiguration 0
load_feature core
current_fileset
xsim {work.tb_compteur4} -wdb {tb_compteur4_isim_beh.wdb} -autoloadwcfg -tclbatch {./run.tcl}
