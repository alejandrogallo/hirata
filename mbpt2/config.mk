mbpt2_SOURCES = $(wildcard mbpt2/*.in)
mbpt2_TARGETS = \
$(patsubst %.in,%.cpp,$(mbpt2_SOURCES)) \

mbpt2: $(mbpt2_TARGETS) ## Create mbpt2 equations

clean-mbpt2:
	-@rm -v $(mbpt2_TARGETS)
