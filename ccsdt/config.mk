ccsdt_SOURCES = $(wildcard ccsdt/*.in)
ccsdt_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsdt_SOURCES)) \

ccsdt: $(ccsdt_TARGETS) ## Create ccsdt equations

clean-ccsdt:
	-@rm -v $(ccsdt_TARGETS)
