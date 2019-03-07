ccsdt_SOURCES = $(wildcard ccsdt/*.in)
ccsdt_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsdt_SOURCES)) \
$(patsubst %.in,%-prepend.cpp,$(ccsdt_SOURCES)) \

ccsdt: $(ccsdt_TARGETS) ## Create ccsdt equations

clean-ccsdt:
	-@rm -v $(ccsdt_TARGETS)

ccsdt/E-prepend.cpp: ccsdt/E.in
	hirata -f $< -o $@ --prepend 'energy[""] = '

ccsdt/T1-prepend.cpp: ccsdt/T1.in
	hirata -f $< -o $@ --prepend '(*Rai)["bi"] = '

ccsdt/T2-prepend.cpp: ccsdt/T2.in
	hirata -f $< -o $@ --prepend '(*Rabij)["cdij"] = '

ccsdt/T3-prepend.cpp: ccsdt/T3.in
	hirata -f $< -o $@ --prepend '(*Rabcijk)["edfijk"] = '
