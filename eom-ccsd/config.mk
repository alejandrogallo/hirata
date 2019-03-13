eom_ccsd_SOURCES = $(wildcard eom-ccsd/*.in)
eom_ccsd_TARGETS = \
$(patsubst %.in,%.cpp,$(eom_ccsd_SOURCES)) \
eom-ccsd/contracted \
eom-ccsd/intermediates \
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
	-@rm -rv $(eom_ccsd_TARGETS)

clean-eom-ccd:
	-@rm -rv $(eom_ccd_TARGETS)

%/diagonal:
	mkdir -p $@
	tools/create-diagonal-eom.sh $* $(FD_OUTPUT)

%/contracted:
	mkdir -p $@
	tools/create-contracted-eom.sh $* $(FD_OUTPUT)

%/intermediates:
	mkdir -p $@
	tools/create-intermediates-eom.sh $* $(FD_OUTPUT)

