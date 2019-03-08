ccsd_SOURCES = $(wildcard ccsd/*.in)
ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsd_SOURCES)) \
$(patsubst %.in,%.cpp,$(ccsd_SOURCES)) \
$(patsubst %.in,%-prepend.cpp,$(ccsd_SOURCES)) \
$(patsubst %.in,%-prepend-nocomment.cpp,$(ccsd_SOURCES)) \

ccsd: $(ccsd_TARGETS) ## Create ccsd equations

clean-ccsd:
	-@rm -v $(ccsd_TARGETS)

ccsd/E-prepend.cpp: ccsd/E.in
	hirata -f $< -o $@ --prepend 'energy[""] = '
ccsd/T1-prepend.cpp: ccsd/T1.in
	hirata -f $< -o $@ --prepend '(*Rai)["bi"] = '
ccsd/T2-prepend.cpp: ccsd/T2.in
	hirata -f $< -o $@ --prepend '(*Rabij)["cdij"] = '

%-nocomment.cpp: %.cpp
	sed "/^\/\//d; /^\$$/d;" $< > $@
