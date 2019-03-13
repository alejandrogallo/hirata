ccsdtq_SOURCES = $(wildcard ccsdtq/*.in)
ccsdtq_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsdtq_SOURCES)) \
$(patsubst %.in,%-prepend.cpp,$(ccsdtq_SOURCES)) \
$(patsubst %.in,%-prepend-nocomment.cpp,$(ccsdtq_SOURCES)) \

ccsdtq: $(ccsdtq_TARGETS) ## Create ccsdtq equations

clean-ccsdtq:
	-@rm -v $(ccsdtq_TARGETS)

ccsdtq/E-prepend.cpp: ccsdtq/E.in
	hirata -f $< -o $@ --prepend 'energy[""] = '
ccsdtq/T1-prepend.cpp: ccsdtq/T1.in
	hirata -f $< -o $@ --prepend '(*Rai)["bi"] = '
ccsdtq/T2-prepend.cpp: ccsdtq/T2.in
	hirata -f $< -o $@ --prepend '(*Rabij)["cdij"] = '
ccsdtq/T3-prepend.cpp: ccsdtq/T3.in
	hirata -f $< -o $@ --prepend '(*Rabcijk)["edfijk"] = '
ccsdtq/T4-prepend.cpp: ccsdtq/T4.in
	hirata -f $< -o $@ --prepend '(*Rabcdijkl)["edfijk"] = '

%-nocomment.cpp: %.cpp
	sed "/^\/\//d; /^\$$/d;" $< > $@
