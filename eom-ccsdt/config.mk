eom_ccsdt_SOURCES = $(wildcard eom-ccsdt/*.in)
eom_ccsdt_TARGETS = \
$(patsubst %.in,%.cpp,$(eom_ccsdt_SOURCES)) \
eom-ccsdt/contracted \
eom-ccsdt/intermediates \
eom-ccsdt/factors \
eom-ccsdt/diagonal \

eom-ccsdt: $(eom_ccsdt_TARGETS) ## Create eom-ccsdt equations

clean-eom-ccsdt:
	-@rm -v $(eom_ccsdt_TARGETS)

%/diagonal:
	mkdir -p $@
	tools/create-diagonal-eom.sh $* $(FD_OUTPUT)

%/factors:
	mkdir -p $@
	tools/create-factors.sh $* $(FD_OUTPUT)

%/contracted:
	mkdir -p $@
	tools/create-contracted-eom.sh $* $(FD_OUTPUT)

%/intermediates:
	mkdir -p $@
	tools/create-intermediates-eom.sh $* $(FD_OUTPUT)

