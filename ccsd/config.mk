ccsd_SOURCES = $(wildcard ccsd/*.in)
ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsd_SOURCES)) \

ccsd: $(ccsd_TARGETS) ## Create ccsd equations

clean-ccsd:
	-@rm -v $(ccsd_TARGETS)

ccsd/intermediates:
	mkdir -p $@
	ccsd/scripts/create-intermediates.sh ccsd $(FD_OUTPUT)
