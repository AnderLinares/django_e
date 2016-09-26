class CoreFormset(object):
    @staticmethod
    def formset_checklist_inventory(formset, checklist_detail):
        for form in formset.forms:
            form.save(checklist_detail=checklist_detail, commit=False)

    @staticmethod
    def formset_checklist_photo(formset, checklist_detail):
        for form in formset.forms:
            form.save(checklist_detail=checklist_detail, commit=False)

    @staticmethod
    def formset_checklist_labour(formset, checklist_detail):
        for form in formset.forms:
            form.save(checklist_detail=checklist_detail, commit=False)

    @staticmethod
    def formset_checklist_labour_employee(formset, labour_checklist):
        for form in formset.forms:
            form.save(labour_checklist=labour_checklist, commit=False)