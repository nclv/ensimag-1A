set_param project.enableReportConfiguration 0
load_feature core
current_fileset
xsim {work.tb_lecture_memoire} -wdb {tb_lecture_memoire_isim_beh.wdb} -autoloadwcfg -tclbatch {./run.tcl}
