set_param project.enableReportConfiguration 0
load_feature core
current_fileset
xsim {work.tb_PGCD} -wdb {tb_PGCD_isim_beh.wdb} -autoloadwcfg -tclbatch {./run.tcl}
