from django.utils.translation import ugettext_lazy as _

CODE_TEXT_EDIT = 'EDIT'
TEXT_MSG_SUCCESS = _('Data saved correctly')
TEXT_MSG_ERROR = _('There was an error saving information')
TEXT_MSG_WARNING = _('It required to complete required fields')
STATUS_MSG_TAGS = {
    'success': TEXT_MSG_SUCCESS,
    'error': TEXT_MSG_ERROR,
    'warning': TEXT_MSG_WARNING,
}

NAME_SELECT_DEFAULT = _('--Choose--')
SELECT_DEFAULT_ = [('', NAME_SELECT_DEFAULT)]
SELECT_DEFAULT = (('', NAME_SELECT_DEFAULT),)
DISABLED = 'DISABLED'
ENABLED = 'ENABLED'
STATUS_MODEL1 = (
    (ENABLED, _('Enabled')),
    (DISABLED, _('Disabled')),
)

# ITEMS IDENTITY DOCUMENT
CODE_DOCUMENT_DNI = 'DOC-1'
CODE_DOCUMENT_RUC = 'DOC-2'
CODE_DOCUMENT_PASSPORT = 'DOC-3'
SIS_DOCUMENT_DNI_STRING = (CODE_DOCUMENT_DNI, _('DNI'))
SIS_DOCUMENT_RUC_STRING = (CODE_DOCUMENT_RUC, _('RUC'))
SIS_DOCUMENT_PASSPORT_STRING = (CODE_DOCUMENT_PASSPORT, _('PASSPORT'))
TYPE_IDENTITY_DOCUMENT_OPTIONS = (
    SIS_DOCUMENT_DNI_STRING, SIS_DOCUMENT_RUC_STRING, SIS_DOCUMENT_PASSPORT_STRING
)

# ITEMS TRIBUTE PERSON
CODE_TRIBUTE_PERSON_NATURAL = 'PERS-1'
CODE_TRIBUTE_PERSON_JURIDICAL = 'PERS-2'
SIS_TRIBUTE_PERSON_NATURAL_STRING = (CODE_TRIBUTE_PERSON_NATURAL, _('Natural'))
SIS_TRIBUTE_PERSON_JURIDICAL_STRING = (CODE_TRIBUTE_PERSON_JURIDICAL, _('Legal'))

TRIBUTE_PERSON_OPTIONS = (
    SIS_TRIBUTE_PERSON_NATURAL_STRING, SIS_TRIBUTE_PERSON_JURIDICAL_STRING
)

# ITEMS GENDER
CODE_GENDER_MALE = 'GEN-1'
CODE_GENDER_FEMALE = 'GEN-2'
SIS_GENDER_MALE_STRING = (CODE_GENDER_MALE, _('Male'))
SIS_GENDER_FEMALE_STRING = (CODE_GENDER_FEMALE, _('Female'))
TYPE_GENDER_OPTIONS = (
    SIS_GENDER_MALE_STRING, SIS_GENDER_FEMALE_STRING
)

# ITEMS CIVIL STATUS
CODE_CIVIL_STATUS_SINGLE = 'CVS-1'
CODE_CIVIL_STATUS_MARRIED = 'CVS-2'
CODE_CIVIL_STATUS_WIDOWED = 'CVS-3'
CODE_CIVIL_STATUS_DIVORCED = 'CVS-4'
CODE_CIVIL_STATUS_SEPARATED = 'CVS-5'
SIS_CIVIL_STATUS_SINGLE_STRING = (CODE_CIVIL_STATUS_SINGLE, _('Single'))
SIS_CIVIL_STATUS_MARRIED_STRING = (CODE_CIVIL_STATUS_MARRIED, _('Married'))
SIS_CIVIL_STATUS_WIDOWED_STRING = (CODE_CIVIL_STATUS_WIDOWED, _('Widowed'))
SIS_CIVIL_STATUS_DIVORCED_STRING = (CODE_CIVIL_STATUS_DIVORCED, _('Divorced'))
SIS_CIVIL_STATUS_SEPARATED_STRING = (CODE_CIVIL_STATUS_SEPARATED, _('Separated'))
TYPE_CIVIL_STATUS_OPTIONS = (
    SIS_CIVIL_STATUS_SINGLE_STRING, SIS_CIVIL_STATUS_MARRIED_STRING, SIS_CIVIL_STATUS_WIDOWED_STRING,
    SIS_CIVIL_STATUS_DIVORCED_STRING, SIS_CIVIL_STATUS_SEPARATED_STRING
)

# ITEMS BREVETE
CODE_BREVETE_A1 = 'BRT-1'
CODE_BREVETE_A2 = 'BRT-2'
SIS_BREVETE_A1_STRING = (CODE_BREVETE_A1, _('A1'))
SIS_BREVETE_A2_STRING = (CODE_BREVETE_A2, _('A2'))
TYPE_BREVETE_OPTIONS = (
    SIS_BREVETE_A1_STRING, SIS_BREVETE_A2_STRING
)

# ITEMS CONTRIBUTION SYSTEM

CODE_CONTRIBUTION_ONP = 'CTS-1'
CODE_CONTRIBUTION_AFP = 'CTS-2'
CODE_CONTRIBUTION_ESSALUD = 'CTS-3'
CODE_CONTRIBUTION_EPS = 'CTS-4'
CODE_CONTRIBUTION_SCTR_SALUD = 'CTS-5'
CODE_CONTRIBUTION_SCTR_PENSION = 'CTS-6'
SIS_CONTRIBUTION_ONP_STRING = (CODE_CONTRIBUTION_ONP, _('ONP'))
SIS_CONTRIBUTION_AFP_STRING = (CODE_CONTRIBUTION_AFP, _('AFP'))
SIS_CONTRIBUTION_ESSALUD_STRING = (CODE_CONTRIBUTION_ESSALUD, _('ESSALUD'))
SIS_CONTRIBUTION_EPS_STRING = (CODE_CONTRIBUTION_EPS, _('EPS'))
SIS_CONTRIBUTION_SCTR_SALUD_STRING = (CODE_CONTRIBUTION_SCTR_SALUD, _('SCTR-SALUD'))
SIS_CONTRIBUTION_SCTR_PENSION_STRING = (CODE_CONTRIBUTION_SCTR_PENSION, _('SCTR-PENSION'))

TYPE_CONTRIBUTION_SYSTEM__OPTIONS = (
    SIS_CONTRIBUTION_ONP_STRING, SIS_CONTRIBUTION_AFP_STRING, SIS_CONTRIBUTION_ESSALUD_STRING,
    SIS_CONTRIBUTION_EPS_STRING, SIS_CONTRIBUTION_SCTR_SALUD_STRING, SIS_CONTRIBUTION_SCTR_PENSION_STRING
)

# ITEMS TYPE VIA
CODE_TYPE_VIA_ITEM1 = 'VIA-1'
CODE_TYPE_VIA_ITEM2 = 'VIA-2'
CODE_TYPE_VIA_ITEM3 = 'VIA-3'
CODE_TYPE_VIA_ITEM4 = 'VIA-4'
CODE_TYPE_VIA_ITEM5 = 'VIA-5'
CODE_TYPE_VIA_ITEM6 = 'VIA-6'
CODE_TYPE_VIA_ITEM7 = 'VIA-7'
SIS_TYPE_VIA_STRING1 = (CODE_TYPE_VIA_ITEM1, _('VIA URBANA'))
SIS_TYPE_VIA_STRING2 = (CODE_TYPE_VIA_ITEM2, _('VIA INTER-URBANA'))
SIS_TYPE_VIA_STRING3 = (CODE_TYPE_VIA_ITEM3, _('VIA TRAVESIA'))
SIS_TYPE_VIA_STRING4 = (CODE_TYPE_VIA_ITEM4, _('VIA CARRETERA'))
SIS_TYPE_VIA_STRING5 = (CODE_TYPE_VIA_ITEM5, _('VIA TRAVESIA'))
SIS_TYPE_VIA_STRING6 = (CODE_TYPE_VIA_ITEM6, _('VIA AUTO-PISTA'))
SIS_TYPE_VIA_STRING7 = (CODE_TYPE_VIA_ITEM7, _('VIA PEAJE'))

TYPE_TYPE_VIA_OPTIONS = (
    SIS_TYPE_VIA_STRING1, SIS_TYPE_VIA_STRING2, SIS_TYPE_VIA_STRING3,
    SIS_TYPE_VIA_STRING4, SIS_TYPE_VIA_STRING5, SIS_TYPE_VIA_STRING6,
    SIS_TYPE_VIA_STRING7
)

# ITEMS TYPE ZONA
CODE_TYPE_ZONE_ITEM1 = 'ZNE-1'
CODE_TYPE_ZONE_ITEM2 = 'ZNE-2'
CODE_TYPE_ZONE_ITEM3 = 'ZNE-3'
SIS_TYPE_ZONE_STRING1 = (CODE_TYPE_ZONE_ITEM1, _('ZONA RESIDENCIAL'))
SIS_TYPE_ZONE_STRING2 = (CODE_TYPE_ZONE_ITEM2, _('ZONA COMERCIAL'))
SIS_TYPE_ZONE_STRING3 = (CODE_TYPE_ZONE_ITEM3, _('VIA TRAVESIA'))

TYPE_TYPE_ZONE_OPTIONS = (
    SIS_TYPE_ZONE_STRING1, SIS_TYPE_ZONE_STRING2, SIS_TYPE_ZONE_STRING3,

)

# ITEMS TYPE QUALIFICATION
CODE_QUALIFICATION_VERY_BAJA = 'QAL-1'
CODE_QUALIFICATION_BAJA = 'QAL-2'
CODE_QUALIFICATION_MEDIA = 'QAL-3'
CODE_QUALIFICATION_ALTA = 'QAL-4'
CODE_QUALIFICATION_VERY_ALTA = 'QAL-5'
SIS_QUALIFICATION_VERY_BAJA_STRING = (CODE_QUALIFICATION_VERY_BAJA, _('MUY_BAJA'))
SIS_QUALIFICATION_BAJA_STRING = (CODE_QUALIFICATION_BAJA, _('BAJA'))
SIS_QUALIFICATION_MEDIA_STRING = (CODE_QUALIFICATION_MEDIA, _('MEDIA'))
SIS_QUALIFICATION_ALTA_STRING = (CODE_QUALIFICATION_ALTA, _('ALTA'))
SIS_QUALIFICATION_VERY_ALTA_STRING = (CODE_QUALIFICATION_VERY_ALTA, _('MUY_ALTA'))

TYPE_QUALIFICATION_OPTIONS = (
    SIS_QUALIFICATION_VERY_BAJA_STRING, SIS_QUALIFICATION_BAJA_STRING, SIS_QUALIFICATION_MEDIA_STRING,
    SIS_QUALIFICATION_ALTA_STRING, SIS_QUALIFICATION_VERY_ALTA_STRING
)

# ITEMS TYPE kinship
CODE_KINSHIP_ITEM1 = 'KSP-1'
CODE_KINSHIP_ITEM2 = 'KSP-2'
CODE_KINSHIP_ITEM3 = 'KSP-3'
SIS_KINSHIP_STRING1 = (CODE_KINSHIP_ITEM1, _('Hijo'))
SIS_KINSHIP_STRING2 = (CODE_KINSHIP_ITEM2, _('esposo(a)'))
SIS_KINSHIP_STRING3 = (CODE_KINSHIP_ITEM3, _('conviviente'))

TYPE_KINSHIP_OPTIONS = (
    SIS_KINSHIP_STRING1, SIS_KINSHIP_STRING2, SIS_KINSHIP_STRING3
)

# ITEMS TYPE EXP RECORD
CODE_EXP_RECORD_ITEM1 = 'EXR-1'
CODE_EXP_RECORD_ITEM2 = 'EXR-2'
CODE_EXP_RECORD_ITEM3 = 'EXR-3'
SIS_EXP_RECORD_STRING1 = (CODE_EXP_RECORD_ITEM1, _('Certificado'))
SIS_EXP_RECORD_STRING2 = (CODE_EXP_RECORD_ITEM2, _('Boleta'))
SIS_EXP_RECORD_STRING3 = (CODE_EXP_RECORD_ITEM3, _('Planilla'))

TYPE_EXP_RECORD_OPTIONS = (
    SIS_EXP_RECORD_STRING1, SIS_EXP_RECORD_STRING2, SIS_EXP_RECORD_STRING3
)

# ITEMS TYPE POLiCE RECORD
CODE_POLICE_RECORD_ITEM1 = 'PLR-1'
CODE_POLICE_RECORD_ITEM2 = 'PLR-2'
SIS_POLICE_RECORD_STRING1 = (CODE_POLICE_RECORD_ITEM1, _('Con antecendentes'))
SIS_POLICE_RECORD_STRING2 = (CODE_POLICE_RECORD_ITEM2, _('Sin antecendentes'))

TYPE_POLICE_RECORD_OPTIONS = (
    SIS_POLICE_RECORD_STRING1, SIS_POLICE_RECORD_STRING2
)

# ITEMS TYPE CORRELATIVE
CODE_CORRELATIVE_FACTURA = 'CRT-1'
CODE_CORRELATIVE_BOLETA = 'CRT-2'
CODE_CORRELATIVE_QUOTATION = 'CRT-3'
CODE_CORRELATIVE_CHECKLIST = 'CRT-4'
SIS_CORRELATIVE_STRING1 = (CODE_CORRELATIVE_FACTURA, _('Factura'))
SIS_CORRELATIVE_STRING2 = (CODE_CORRELATIVE_BOLETA, _('Boleta'))
SIS_CORRELATIVE_STRING3 = (CODE_CORRELATIVE_QUOTATION, _('Cotizacion'))
SIS_CORRELATIVE_STRING4 = (CODE_CORRELATIVE_CHECKLIST, _('Checklist'))

TYPE_CORRELATIVE_OPTIONS = (
    SIS_CORRELATIVE_STRING1, SIS_CORRELATIVE_STRING2, SIS_CORRELATIVE_STRING3,
    SIS_CORRELATIVE_STRING4
)

# ITEMS TYPE BLOOD RECORD
CODE_BLOOD_RECORD_ITEM1 = 'BLR-1'
CODE_BLOOD_RECORD_ITEM2 = 'BLR-2'
CODE_BLOOD_RECORD_ITEM3 = 'BLR-3'
SIS_BLOOD_RECORD_STRING1 = (CODE_BLOOD_RECORD_ITEM1, _('Toxicologico'))
SIS_BLOOD_RECORD_STRING2 = (CODE_BLOOD_RECORD_ITEM2, _('Alcoholemia'))
SIS_BLOOD_RECORD_STRING3 = (CODE_BLOOD_RECORD_ITEM3, _('Toxicológico/Alcoholemia'))

TYPE_BLOOD_RECORD_OPTIONS = (
    SIS_BLOOD_RECORD_STRING1, SIS_BLOOD_RECORD_STRING2, SIS_BLOOD_RECORD_STRING3
)

# ITEMS STATUS FILE RECORD
STATUS_FILE_RECORD_NEGATIVE = 'STBLR-1'
STATUS_FILE_RECORD_POSITIVE = 'STBLR-2'
SIS_STATUS_FILE_RECORD_NEGATIVE_STRING = (STATUS_FILE_RECORD_NEGATIVE, _('Negative'))
SIS_STATUS_FILE_RECORD_POSITIVE_STRING = (STATUS_FILE_RECORD_POSITIVE, _('Positive'))

STATUS_FILE_RECORD_OPTIONS = (
    SIS_STATUS_FILE_RECORD_NEGATIVE_STRING, SIS_STATUS_FILE_RECORD_POSITIVE_STRING
)

# ITEMS TYPE UNIT MEASUREMENT
CODE_MEASUREMENT_PURCHASE_LIQUID_UNIT = 'UPM-1'
CODE_MEASUREMENT_PURCHASE_SOLID_UNIT = 'UPM-2'
CODE_MEASUREMENT_TRANSPORT_UNIT = 'UPM-3'
CODE_MEASUREMENT_DELIVERY_UNIT = 'UPM-4'
CODE_MEASUREMENT_STORAGE_UNIT = 'UPM-5'
SIS_MEASUREMENT_PURCHASE_LIQUID_UNIT_STRING = (CODE_MEASUREMENT_PURCHASE_LIQUID_UNIT, _('Purchase Liquid Unit'))
SIS_MEASUREMENT_PURCHASE_SOLID_UNIT_STRING = (CODE_MEASUREMENT_PURCHASE_SOLID_UNIT, _('Purchase Solid Unit'))
SIS_MEASUREMENT_TRANSPORT_UNIT_STRING = (CODE_MEASUREMENT_TRANSPORT_UNIT, _('Transport Unit'))
SIS_MEASUREMENT_DELIVERY_UNIT_STRING = (CODE_MEASUREMENT_DELIVERY_UNIT, _('Delivery Unit'))
SIS_MEASUREMENT_STORAGE_UNIT_STRING = (CODE_MEASUREMENT_STORAGE_UNIT, _('Storage Unit'))

TYPE_UNIT_MEASUREMENT_OPTIONS = (
    SIS_MEASUREMENT_PURCHASE_LIQUID_UNIT_STRING, SIS_MEASUREMENT_PURCHASE_SOLID_UNIT_STRING,
    SIS_MEASUREMENT_TRANSPORT_UNIT_STRING, SIS_MEASUREMENT_DELIVERY_UNIT_STRING,
    SIS_MEASUREMENT_STORAGE_UNIT_STRING
)

# ITEMS VEHICLE STATUS
CODE_VEHICLE_LIGHTWEIGHT = 'VHL-1'
CODE_VEHICLE_HEAVY = 'VHL-2'
SIS_VEHICLE_LIGHTWEIGHT_STRING = (CODE_VEHICLE_LIGHTWEIGHT, _('Lightweight'))
SIS_VEHICLE_HEAVY_STRING = (CODE_VEHICLE_HEAVY, _('Heavy'))

TYPE_CLASS_VEHICLE_OPTIONS = (
    SIS_VEHICLE_LIGHTWEIGHT_STRING, SIS_VEHICLE_HEAVY_STRING,
)


# ITEMS SERVICES STATUS
CODE_SERVICES_MAINTENANCE = 'MAINTENANCE'
CODE_SERVICES_SERVICE = 'SERVICE'
SIS_SERVICES_MAINTENANCE_STRING = (CODE_SERVICES_MAINTENANCE, _('Maintenance'))
SIS_SERVICES_SERVICE_STRING = (CODE_SERVICES_SERVICE, _('Service'))

TYPE_SERVICES_OPTIONS = (
    SIS_SERVICES_MAINTENANCE_STRING, SIS_SERVICES_SERVICE_STRING
)


# ITEMS TALLER DOCUMENT STATUS
CODE_TALLER_SOLICITUDE_ENTRY = 'ENTRY'
CODE_TALLER_SOLICITUDE_EXIT = 'EXIT'
SIS_TALLER_SOLICITUDE_ENTRY_STRING = (CODE_TALLER_SOLICITUDE_ENTRY, _('Entry'))
SIS_TALLER_SOLICITUDE_EXIT_STRING = (CODE_TALLER_SOLICITUDE_EXIT, _('Exit'))

TYPE_TALLER_SOLICITUDE_OPTIONS = (
    SIS_TALLER_SOLICITUDE_ENTRY_STRING, SIS_TALLER_SOLICITUDE_EXIT_STRING
)

# ITEMS TALLER REQUISITION STATUS
CODE_TALLER_REQUISITION_PENDING = 'PENDING'
CODE_TALLER_REQUISITION_SENT = 'SENT'
SIS_TALLER_SOLICITUDE_PENDING_STRING = (CODE_TALLER_REQUISITION_PENDING, _('Pending'))
SIS_TALLER_SOLICITUDE_SENT_STRING = (CODE_TALLER_REQUISITION_SENT, _('Sent'))

TYPE_TALLER_REQUISITION_OPTIONS = (
    SIS_TALLER_SOLICITUDE_PENDING_STRING, SIS_TALLER_SOLICITUDE_SENT_STRING
)