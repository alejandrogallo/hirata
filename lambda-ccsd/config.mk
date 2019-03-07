lambda_ccsd_SOURCES = $(wildcard lambda-ccsd/*.in)
lambda_ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(lambda_ccsd_SOURCES)) \

lambda-ccsd: $(lambda_ccsd_TARGETS) ## Create lambda ccsd equations

clean-lambda-ccsd:
	-@rm -v $(lambda_ccsd_TARGETS)
