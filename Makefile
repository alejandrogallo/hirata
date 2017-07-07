
ccsd_SOURCES = $(wildcard ccsd/*.in)
ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsd_SOURCES)) \
$(patsubst %.in,%-fock.cpp,$(ccsd_SOURCES)) \
$(patsubst %.in,%-uncomment-fock.cpp,$(ccsd_SOURCES))

ccsdt_SOURCES = $(wildcard ccsdt/*.in)
ccsdt_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsdt_SOURCES)) \
$(patsubst %.in,%-fock.cpp,$(ccsdt_SOURCES)) \
$(patsubst %.in,%-uncomment-fock.cpp,$(ccsdt_SOURCES))

eom_ccsd_SOURCES = $(wildcard eom-ccsd/*.in)
eom_ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(eom_ccsd_SOURCES)) \
$(patsubst %.in,%-fock.cpp,$(eom_ccsd_SOURCES)) \
$(patsubst %.in,%-uncomment-fock.cpp,$(eom_ccsd_SOURCES)) \
eom-ccsd/contracted

eom_ccd_SOURCES = $(patsubst eom-ccsd%,eom-ccd%,$(eom_ccsd_SOURCES))
eom_ccd_TARGETS = \
$(eom_ccd_SOURCES) \
$(patsubst eom-ccsd%,eom-ccd%,$(eom_ccsd_TARGETS)) \

ifdef QUIET
FD_OUTPUT = >> log.txt 2>&1
endif

.DEFAULT_GOAL = help

ALL_EQS = eom-ccd eom-ccsd ccsd cssdt

all: $(ALL_EQS) ## Create all equations

eom-ccd/%.in: eom-ccsd/%.in
	@echo Creating $@ from $<
	@mkdir -p $(dir $@)
	sed "/t\s*(\s*[ph][0-9]\s\+[ph][0-9]\s*)/d" $< > $@

%/contracted:
	mkdir -p $@
	tools/create-contracted-eom.sh $* $(FD_OUTPUT)

eom-ccd: $(eom_ccd_TARGETS) ## Create eom-ccd equations

eom-ccsd: $(eom_ccsd_TARGETS) ## Create eom-ccsd equations

ccsd: $(ccsd_TARGETS) ## Create ccsd equations

ccsdt: $(ccsdt_TARGETS) ## Create ccsdt equations

%.cpp: %.in
	./hirata.py -o $@ -f $< $(FD_OUTPUT)

%-fock.cpp: %.in
	./hirata.py --fock -o $@ -f $< $(FD_OUTPUT)

%-uncomment-fock.cpp: %.in
	./hirata.py --no-comment --fock -o $@ -f $< $(FD_OUTPUT)

test:
	python -m unittest discover tests/

help: ## Prints help for targets with comments
	@$(or $(AWK),awk) ' \
		BEGIN {FS = ":.*?## "}; \
		/^## *<<HELP/,/^## *HELP/ { \
			help=$$1; \
			gsub("#","",help); \
			if (! match(help, "HELP")) \
				print help ; \
		}; \
		/^[a-zA-Z0-9_\-.]+:.*?## .*$$/{ \
			printf "\033[36m%-30s\033[0m %s\n", $$1, $$2 ; \
		};' \
		$(MAKEFILE_LIST)

clean:
	git clean -xf
	git clean -xfd

# This is used for printing defined variables from Some other scripts. For
# instance if you want to know the value of the PDF_VIEWER defined in the
# Makefile, then you would do
#    make print-PDF_VIEWER
# and this would output PDF_VIEWER=mupdf for instance.
FORCE:
print-%:
	@echo '$*=$($*)'
