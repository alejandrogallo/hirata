mbpt1_SOURCES = $(wildcard mbpt1/*.in)
mbpt1_TARGETS = \
$(patsubst %.in,%.cpp,$(mbpt1_SOURCES)) \

mbpt1: $(mbpt1_TARGETS) ## Create mbpt1 equations

clean-mbpt1:
	-@rm -v $(mbpt1_TARGETS)
