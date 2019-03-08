.DEFAULT_GOAL = help

ALL_EQS = $(shell find -name config.mk | xargs dirname | sed 's/[.].//')
CLEAN_TARGETS = $(patsubst %,clean-%,$(ALL_EQS))
CONFIG_FILES = $(patsubst %,./%/config.mk,$(ALL_EQS))

include $(CONFIG_FILES)

all: $(ALL_EQS) ## Create all equations

%.cpp: %.in
	hirata -o $@ -f $<

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
