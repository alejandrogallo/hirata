
ccsd_SOURCES = $(wildcard ccsd/*.in)
ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(ccsd_SOURCES)) \
$(patsubst %.in,%-fock.cpp,$(ccsd_SOURCES)) \
$(patsubst %.in,%-uncomment-fock.cpp,$(ccsd_SOURCES))

eom-ccd: ## Create eom-ccd equations
eom-ccsd: ## Create eom-ccsd equations


ccsd: $(ccsd_TARGETS) ## Create ccsd equations

%.cpp: %.in
	./hirata.py -o $@ -f $<

%-fock.cpp: %.in
	./hirata.py --fock -o $@ -f $<

%-uncomment-fock.cpp: %.in
	./hirata.py --no-comment --fock -o $@ -f $<

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

