include mbpt1/config.mk
include mbpt2/config.mk
include ccsd/config.mk
include ccsdt/config.mk

eom_ccsd_SOURCES = $(wildcard eom-ccsd/*.in)
eom_ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(eom_ccsd_SOURCES)) \
eom-ccsd/contracted \
eom-ccsd/intermediates \
eom-ccsd/factors \
eom-ccsd/diagonal \

eom_ccsdt_SOURCES = $(wildcard eom-ccsdt/*.in)
eom_ccsdt_TARGETS = \
$(patsubst %.in,%.cpp,$(eom_ccsdt_SOURCES)) \
eom-ccsdt/contracted \
eom-ccsdt/intermediates \
eom-ccsdt/factors \
eom-ccsdt/diagonal \

eom_ccd_SOURCES = $(patsubst eom-ccsd%,eom-ccd%,$(eom_ccsd_SOURCES))
eom_ccd_TARGETS = \
$(eom_ccd_SOURCES) \
$(patsubst eom-ccsd%,eom-ccd%,$(eom_ccsd_TARGETS)) \



lambda_ccsd_SOURCES = $(wildcard lambda-ccsd/*.in)
lambda_ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(lambda_ccsd_SOURCES)) \


ifdef QUIET
FD_OUTPUT = >> log.txt 2>&1
endif

.DEFAULT_GOAL = help

ALL_EQS = eom-ccd eom-ccsd ccsd ccsdt

all: $(ALL_EQS) ## Create all equations

eom-ccd/%.in: eom-ccsd/%.in
	@echo Creating $@ from $<
	@mkdir -p $(dir $@)
	sed "/t\s*(\s*[ph][0-9]\s\+[ph][0-9]\s*)/d" $< > $@

%/diagonal:
	mkdir -p $@
	tools/create-diagonal-eom.sh $* $(FD_OUTPUT)

%/factors:
	mkdir -p $@
	tools/create-factors.sh $* $(FD_OUTPUT)

%/contracted:
	mkdir -p $@
	tools/create-contracted-eom.sh $* $(FD_OUTPUT)

ccsd/intermediates:
	mkdir -p $@
	ccsd/scripts/create-intermediates.sh ccsd $(FD_OUTPUT)

%/intermediates:
	mkdir -p $@
	tools/create-intermediates-eom.sh $* $(FD_OUTPUT)

eom-ccd: $(eom_ccd_TARGETS) ## Create eom-ccd equations

eom-ccsd: $(eom_ccsd_TARGETS) ## Create eom-ccsd equations

eom-ccsdt: $(eom_ccsdt_TARGETS) ## Create eom-ccsdt equations

lambda_ccsd: $(lambda_ccsd_TARGETS) ## Create lambda ccsd equations

%.cpp: %.in
	hirata -o $@ -f $< $(FD_OUTPUT)

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
	-git clean -xf
	-git clean -xf
