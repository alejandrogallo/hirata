cisd_SOURCES = $(wildcard cisd/*.in)
cisd_TARGETS = \
$(patsubst %.in,%.cpp,$(cisd_SOURCES)) \
$(patsubst %.in,%.cpp,$(cisd_SOURCES)) \
$(patsubst %.in,%-prepend.cpp,$(cisd_SOURCES)) \
$(patsubst %.in,%-prepend-nocomment.cpp,$(cisd_SOURCES)) \

cisd: $(cisd_TARGETS) ## Create cisd equations

clean-cisd:
	-@rm -v $(cisd_TARGETS)

cisd/E-prepend.cpp: cisd/E.in
	hirata -f $< -o $@ --prepend 'energy[""] = '
cisd/T1-prepend.cpp: cisd/T1.in
	hirata -f $< -o $@ --prepend '(*Rai)["bi"] = '
cisd/T2-prepend.cpp: cisd/T2.in
	hirata -f $< -o $@ --prepend '(*Rabij)["cdij"] = '

%-nocomment.cpp: %.cpp
	sed "/^\/\//d; /^\$$/d;" $< > $@
