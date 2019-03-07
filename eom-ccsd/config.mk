eom_ccsd_SOURCES = $(wildcard eom-ccsd/*.in)
eom_ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(eom_ccsd_SOURCES)) \
eom-ccsd/contracted \
eom-ccsd/intermediates \
eom-ccsd/factors \
eom-ccsd/diagonal \

eom_ccd_SOURCES = $(patsubst eom-ccsd%,eom-ccd%,$(eom_ccsd_SOURCES))
eom_ccd_TARGETS = \
$(eom_ccd_SOURCES) \
$(patsubst eom-ccsd%,eom-ccd%,$(eom_ccsd_TARGETS)) \

eom-ccd/%.in: eom-ccsd/%.in
	@echo Creating $@ from $<
	@mkdir -p $(dir $@)
	sed "/t\s*(\s*[ph][0-9]\s\+[ph][0-9]\s*)/d" $< > $@

eom-ccd: $(eom_ccd_TARGETS) ## Create eom-ccd equations
eom-ccsd: $(eom_ccsd_TARGETS) ## Create eom-ccsd equations

clean-eom-ccsd:
	-@rm -v $(eom_ccsd_TARGETS)

clean-eom-ccd:
	-@rm -v $(eom_ccd_TARGETS)
