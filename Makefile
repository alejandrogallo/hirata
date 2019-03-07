include mbpt1/config.mk
include mbpt2/config.mk
include ccsd/config.mk
include eom-ccsd/config.mk
include ccsdt/config.mk
include eom-ccsdt/config.mk

ifdef QUIET
FD_OUTPUT = >> log.txt 2>&1
endif

.DEFAULT_GOAL = help

ALL_EQS = ccsd ccsdt eom-ccsd eom-ccsdt lambda-ccsd mbpt1 mbpt2
CLEAN_TARGETS = $(patsubst %,clean-%,$(ALL_EQS))

all: $(ALL_EQS) ## Create all equations

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

clean: $(CLEAN_TARGETS)
