ccsd_t_SOURCES = $(wildcard ccsd_t/*.in)
ccsd_t_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsd_t_SOURCES)) \
$(patsubst %.in,%.cpp,$(ccsd_t_SOURCES)) \
$(patsubst %.in,%-prepend.cpp,$(ccsd_t_SOURCES)) \
$(patsubst %.in,%-prepend-nocomment.cpp,$(ccsd_t_SOURCES)) \

ccsd_t: $(ccsd_t_TARGETS) ## Create ccsd_t equations

clean-ccsd_t:
	-@rm -v $(ccsd_t_TARGETS)

ccsd_t/E-prepend.cpp: ccsd_t/E.in
	hirata -f $< -o $@ --prepend 'energy[""] = '
ccsd_t/T1-prepend.cpp: ccsd_t/T1.in
	hirata -f $< -o $@ --prepend '(*Rai)["bi"] = '
ccsd_t/T2-prepend.cpp: ccsd_t/T2.in
	hirata -f $< -o $@ --prepend '(*Rabij)["cdij"] = '

%-nocomment.cpp: %.cpp
	sed "/^\/\//d; /^\$$/d;" $< > $@
