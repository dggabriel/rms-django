# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_username = models.TextField()
    account_password = models.CharField(max_length=128)
    person = models.ForeignKey('People', models.DO_NOTHING)
    last_login = models.ForeignKey('LoginHistory', models.DO_NOTHING, blank=True, null=True)
    previous_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Affiliation(models.Model):
    aff_id = models.AutoField(primary_key=True)
    aff_name = models.TextField()
    address_line_1 = models.TextField()
    address_line_2 = models.TextField(blank=True, null=True)
    address_city = models.TextField()
    address_province = models.TextField(blank=True, null=True)
    primary_phone_number = models.IntegerField()
    alternate_phone_number = models.IntegerField(blank=True, null=True)
    primary_email_address = models.TextField()
    alternate_email_address = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    cluster = models.TextField(blank=True, null=True)
    parent = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'affiliation'


class AssetCategories(models.Model):
    asset_category_id = models.AutoField(primary_key=True)
    asset_name = models.CharField(max_length=512, blank=True, null=True)
    asset_description1 = models.CharField(max_length=512)
    asset_description2 = models.CharField(max_length=512, blank=True, null=True)
    asset_units_of_measure = models.CharField(max_length=128)
    property_number = models.CharField(max_length=128)
    serial_number = models.CharField(max_length=128, blank=True, null=True)
    brand_name = models.CharField(max_length=256, blank=True, null=True)
    asset_class_id = models.IntegerField()
    asset_unit_cost = models.TextField(blank=True, null=True)  # This field type is a guess.
    office_responsibility_code = models.CharField(max_length=128, blank=True, null=True)
    unit_owner = models.CharField(max_length=128, blank=True, null=True)
    acquisition_document = models.ForeignKey('Documents', models.DO_NOTHING, blank=True, null=True)
    mr_document = models.ForeignKey('Documents', models.DO_NOTHING, related_name='assetcategories_mr_document_set', blank=True, null=True)
    inspection_document = models.ForeignKey('Documents', models.DO_NOTHING, related_name='assetcategories_inspection_document_set', blank=True, null=True)
    asset_remarks = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_categories'
        db_table_comment = 'office responsibility code - perhaps change to affiliation FK?\nmr - updates table?\n\nredundant with assets'


class AssetClasses(models.Model):
    asset_class_id = models.AutoField(primary_key=True)
    asset_class_name = models.CharField(max_length=32, blank=True, null=True)
    asset_class_description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_classes'


class AssetLocations(models.Model):
    asset_location_id = models.BigAutoField(primary_key=True)
    asset = models.ForeignKey('Assets', models.DO_NOTHING)
    location = models.ForeignKey(Affiliation, models.DO_NOTHING)
    move_date = models.DateTimeField()
    inserted_by = models.ForeignKey('People', models.DO_NOTHING, db_column='inserted_by')

    class Meta:
        managed = False
        db_table = 'asset_locations'


class AssetSpecifications(models.Model):
    specification_id = models.BigAutoField(primary_key=True)
    specification_property = models.TextField()
    asset = models.ForeignKey('Assets', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'asset_specifications'


class AssetStatusChanges(models.Model):
    asset_status_change_id = models.BigAutoField(primary_key=True)
    asset = models.ForeignKey('Assets', models.DO_NOTHING)
    asset_status = models.ForeignKey('AssetStatuses', models.DO_NOTHING)
    effectivity_date = models.DateTimeField()
    updated_by = models.ForeignKey('People', models.DO_NOTHING, db_column='updated_by')
    remarks = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_status_changes'


class AssetStatuses(models.Model):
    asset_status_id = models.AutoField(primary_key=True)
    asset_status_name = models.CharField(max_length=128, blank=True, null=True)
    asset_status_description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_statuses'
        db_table_comment = 'condemnation\nrepair\nworking\noutside-office\n'


class Assets(models.Model):
    asset_name = models.CharField(max_length=512, blank=True, null=True)
    asset_description1 = models.CharField(max_length=512)
    asset_description2 = models.CharField(max_length=512, blank=True, null=True)
    asset_units_of_measure = models.CharField(max_length=128)
    property_number = models.CharField(max_length=128)
    serial_number = models.CharField(max_length=128, blank=True, null=True)
    brand_name = models.CharField(max_length=256, blank=True, null=True)
    asset_unit_cost = models.TextField(blank=True, null=True)  # This field type is a guess.
    mr_document = models.ForeignKey('Documents', models.DO_NOTHING, blank=True, null=True)
    acquisition_inspection_document = models.ForeignKey('Documents', models.DO_NOTHING, related_name='assets_acquisition_inspection_document_set', blank=True, null=True)
    asset_remarks = models.CharField(max_length=512, blank=True, null=True)
    officer_in_charge = models.ForeignKey('Staff', models.DO_NOTHING)
    condemnation_document = models.ForeignKey('Documents', models.DO_NOTHING, related_name='assets_condemnation_document_set', blank=True, null=True)
    accountable_enduser = models.ForeignKey('People', models.DO_NOTHING)
    asset_id = models.BigAutoField(primary_key=True)
    inspection_approval = models.BooleanField(blank=True, null=True)
    asset_condemned = models.CharField(max_length=512, blank=True, null=True)
    asset_class = models.ForeignKey(AssetClasses, models.DO_NOTHING)
    asset_specification = models.ForeignKey(AssetSpecifications, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BudgetAllocation(models.Model):
    budget_id = models.BigAutoField(primary_key=True)
    budget_request = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    total_amount = models.TextField()  # This field type is a guess.
    budget_approved = models.BooleanField()
    doc = models.ForeignKey('Documents', models.DO_NOTHING)
    date_created = models.DateField()
    amount_remaining = models.TextField(blank=True, null=True)  # This field type is a guess.
    budget_allocation_request = models.BooleanField(blank=True, null=True)
    budget_allocation_request_type = models.SmallIntegerField(blank=True, null=True, db_comment='0 - initial request\n1 - realignment')
    updated_budget = models.ForeignKey('self', models.DO_NOTHING, db_column='updated_budget', related_name='budgetallocation_updated_budget_set', blank=True, null=True, db_comment='if no realignment -> null')

    class Meta:
        managed = False
        db_table = 'budget_allocation'


class BudgetItem(models.Model):
    budget_item_id = models.BigAutoField(primary_key=True)
    type = models.SmallIntegerField(db_comment='0-PS\n1-MOOE\n2-CO')
    subtype = models.TextField()
    amount = models.TextField()  # This field type is a guess.
    budget = models.ForeignKey(BudgetAllocation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'budget_item'
        db_table_comment = 'elements of line-item budget'


class BudgetUtilization(models.Model):
    utilization_id = models.BigAutoField(primary_key=True)
    approved_budget = models.ForeignKey(BudgetAllocation, models.DO_NOTHING)
    debit_from_fcm = models.ForeignKey('FundingSources', models.DO_NOTHING)
    amount = models.TextField()  # This field type is a guess.
    particulars = models.TextField()
    budget_item = models.ForeignKey(BudgetItem, models.DO_NOTHING)
    person_to_credit = models.ForeignKey('People', models.DO_NOTHING, db_column='person_to_credit')
    utilization_approval = models.BooleanField()
    request_date = models.DateField()
    approval_date = models.DateField(blank=True, null=True)
    utilization_doc = models.ForeignKey('Documents', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_utilization'


class ContractJdAssoc(models.Model):
    contract_to_jd_id = models.BigIntegerField(primary_key=True)
    contract = models.ForeignKey('StaffContracts', models.DO_NOTHING)
    jd = models.ForeignKey('JobDescription', models.DO_NOTHING)
    jd_code = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'contract_jd_assoc'


class DailyTimeRecord(models.Model):
    dtr_id = models.BigAutoField(primary_key=True)
    dtr_date = models.DateField()
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    time_in_am = models.TimeField()
    time_out_am = models.TimeField()
    time_in_pm = models.TimeField()
    time_out_pm = models.TimeField()
    from_taskboard = models.BooleanField()
    dtr_doc = models.ForeignKey('Documents', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_time_record'
        unique_together = (('dtr_date', 'staff', 'from_taskboard'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DlrcServiceList(models.Model):
    dlrc_service_id = models.AutoField(primary_key=True)
    service_name = models.TextField()
    service_description = models.TextField(blank=True, null=True)
    date_established = models.DateField()
    date_removed = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dlrc_service_list'


class DocumentTracker(models.Model):
    dt_id = models.BigAutoField(primary_key=True, db_comment='dts number')
    dt_doc = models.ForeignKey('Documents', models.DO_NOTHING)
    doc_status = models.SmallIntegerField(db_comment='0 Pending\n1 Ongoing\n2 Done\n3 Onhold\n4 Cancelled\n5 For Endorsement\n6 For Followup\n7 Forwarded to\n8 Recieved by\n9 Released to\n10 Returned by\n11 Replaced')
    date_updated = models.DateTimeField()
    dt_office = models.ForeignKey(Affiliation, models.DO_NOTHING, db_comment='fk to affiliation')

    class Meta:
        managed = False
        db_table = 'document_tracker'


class Documents(models.Model):
    doc_created = models.DateTimeField(blank=True, null=True)
    doc_id = models.BigAutoField(primary_key=True)
    doc_title = models.TextField()
    doc_type = models.SmallIntegerField(db_comment='0 - dtr\n1 - certificate of service\n\n10 - contract of service\n11 - job orders\n12 - ??? assignment memo\n\n20 - mm service request events\n21 - mm service request rentals\n\n100 - CV')
    doc_online = models.BooleanField()
    doc_approval = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'
        db_table_comment = 'ilcd processes'


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    event_description = models.TextField(blank=True, null=True)
    date_started = models.DateTimeField()
    date_ended = models.DateTimeField()
    request = models.ForeignKey('MmServiceRequests', models.DO_NOTHING, blank=True, null=True)
    point_person = models.ForeignKey('People', models.DO_NOTHING, blank=True, null=True)
    cancelled = models.BooleanField(blank=True, null=True)
    mm_service_request_to_ilc_service = models.ForeignKey('MmServiceRequestToIlcService', models.DO_NOTHING, blank=True, null=True)
    service_type = models.TextField(blank=True, null=True)
    venue = models.TextField(blank=True, null=True)
    production_staff = models.ForeignKey('People', models.DO_NOTHING, related_name='events_production_staff_set', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class FileToDocument(models.Model):
    file = models.OneToOneField('Files', models.DO_NOTHING, primary_key=True)  # The composite primary key (file_id, doc_id) found, that is not supported. The first column is selected.
    doc = models.ForeignKey(Documents, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'file_to_document'
        unique_together = (('file', 'doc'),)


class Files(models.Model):
    file_id = models.BigAutoField(primary_key=True)
    file_url = models.TextField()
    file_type = models.CharField(max_length=6)
    file_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'files'


class FundingSources(models.Model):
    fcm_id = models.AutoField(primary_key=True)
    fcm_number = models.TextField()
    amount = models.TextField()  # This field type is a guess.
    budget = models.ForeignKey(BudgetAllocation, models.DO_NOTHING)
    type = models.SmallIntegerField(db_comment='0 - PS\n1 - MOOE\n2 - CO')
    fcm_doc = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funding_sources'


class IlcServiceList(models.Model):
    ilc_service_id = models.AutoField(primary_key=True)
    service_name = models.TextField()
    service_description = models.TextField(blank=True, null=True)
    date_established = models.DateField()
    date_removed = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ilc_service_list'


class IlcdServiceCost(models.Model):
    cost_id = models.BigAutoField(primary_key=True)
    service_cost = models.TextField()  # This field type is a guess.
    cost_type = models.IntegerField(db_comment='0 - fixed\n1 - hourly\n2 - daily\n3 - monthly')

    class Meta:
        managed = False
        db_table = 'ilcd_service_cost'


class IskpaceLocationToIskpaceService(models.Model):
    location = models.OneToOneField('IskpaceLocations', models.DO_NOTHING, primary_key=True)  # The composite primary key (location_id, service_id) found, that is not supported. The first column is selected.
    service = models.ForeignKey('IskpaceServices', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iskpace_location_to_iskpace_service'
        unique_together = (('location', 'service'),)


class IskpaceLocations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=100, blank=True, null=True)
    location_desc = models.CharField(max_length=1000, blank=True, null=True)
    street_address = models.CharField(max_length=200, blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)
    contact_number = models.CharField(max_length=50, blank=True, null=True)
    location_coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'iskpace_locations'


class IskpaceServices(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100, blank=True, null=True)
    service_desc = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iskpace_services'


class ItemCategories(models.Model):
    item_category_id = models.AutoField(primary_key=True)
    item_category_name = models.CharField(max_length=128)
    item_category_description = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'item_categories'


class JobDescription(models.Model):
    jd_id = models.AutoField(primary_key=True)
    job_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'job_description'


class LoginHistory(models.Model):
    login_id = models.BigAutoField(primary_key=True)
    session_start_date_time = models.DateTimeField()
    account = models.ForeignKey(Accounts, models.DO_NOTHING, blank=True, null=True)
    session_end_data_time = models.DateTimeField(blank=True, null=True)
    logged_in_service = models.ForeignKey(IlcServiceList, models.DO_NOTHING, db_column='logged_in_service', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_history'


class MmServiceAssetRental(models.Model):
    asset = models.OneToOneField(Assets, models.DO_NOTHING, primary_key=True)  # The composite primary key (asset_id, service_id) found, that is not supported. The first column is selected.
    service = models.ForeignKey('MmServiceRequests', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mm_service_asset_rental'
        unique_together = (('asset', 'service'),)


class MmServiceRequestToIlcService(models.Model):
    mm_service_request = models.ForeignKey('MmServiceRequests', models.DO_NOTHING)
    ilc_service = models.ForeignKey(IlcServiceList, models.DO_NOTHING)
    mm_service_request_to_ilc_service_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mm_service_request_to_ilc_service'


class MmServiceRequests(models.Model):
    service_id = models.BigAutoField(primary_key=True)
    service_name = models.CharField(blank=True, null=True)
    contact_person = models.ForeignKey('People', models.DO_NOTHING)
    service_request_from = models.ForeignKey(Affiliation, models.DO_NOTHING, db_column='service_request_from', blank=True, null=True)
    date_requested = models.DateField()
    date_approved = models.DateField(blank=True, null=True)
    start_implementation_date = models.DateTimeField()
    end_implementation_date = models.DateTimeField()
    total_cost = models.TextField(blank=True, null=True)  # This field type is a guess.
    payment = models.ForeignKey('Payments', models.DO_NOTHING, blank=True, null=True)
    request_doc = models.ForeignKey(Documents, models.DO_NOTHING)
    approval_doc = models.ForeignKey(Documents, models.DO_NOTHING, related_name='mmservicerequests_approval_doc_set', blank=True, null=True)
    service_cancellation = models.BooleanField()
    event_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mm_service_requests'


class Payments(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    pay_to_account = models.BigIntegerField()
    amount = models.TextField()  # This field type is a guess.
    receipt_doc = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class People(models.Model):
    person_id = models.BigAutoField(primary_key=True)
    given_name = models.TextField()
    middle_name = models.TextField(blank=True, null=True)
    family_name = models.TextField()
    address_line_1 = models.TextField(blank=True, null=True)
    address_line_2 = models.TextField(blank=True, null=True)
    address_city = models.TextField(blank=True, null=True)
    address_province = models.TextField(blank=True, null=True)
    primary_contact_number = models.IntegerField(blank=True, null=True)
    alternate_contact_number = models.IntegerField(blank=True, null=True)
    primary_email_address = models.CharField(blank=True, null=True)
    alternate_email_address = models.CharField(blank=True, null=True)
    primary_email_address_domain = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people'


class PeopleToAffiliation(models.Model):
    aff = models.OneToOneField(Affiliation, models.DO_NOTHING, primary_key=True)  # The composite primary key (aff_id, person_id) found, that is not supported. The first column is selected.
    person = models.ForeignKey(People, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'people_to_affiliation'
        unique_together = (('aff', 'person'),)


class ServiceToServiceCost(models.Model):
    service = models.OneToOneField(IlcServiceList, models.DO_NOTHING, primary_key=True)  # The composite primary key (service_id, cost_id) found, that is not supported. The first column is selected.
    cost = models.ForeignKey(IlcdServiceCost, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_to_service_cost'
        unique_together = (('service', 'cost'),)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    employee_number = models.BigIntegerField(blank=True, null=True)
    current_contract = models.ForeignKey('StaffContracts', models.DO_NOTHING, blank=True, null=True , related_name='+')
    position = models.CharField()
    person = models.ForeignKey(People, models.DO_NOTHING)
    active = models.BooleanField()
    cv_doc = models.ForeignKey(Documents, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'staff'


class StaffContracts(models.Model):
    contract_id = models.BigAutoField(primary_key=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    contract_doc_id = models.BigIntegerField()
    contract_start_date = models.DateField()
    contract_end_date = models.DateField(blank=True, null=True)
    contract_type = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_contracts'


class SupplyItems(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_category = models.ForeignKey(ItemCategories, models.DO_NOTHING)
    item_name = models.CharField(max_length=512)
    item_description = models.CharField(max_length=512)
    item_unit_of_measure = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'supply_items'


class SupplyReceipts(models.Model):
    supply_receipt_id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(SupplyItems, models.DO_NOTHING)
    ris_document = models.ForeignKey(Documents, models.DO_NOTHING)
    receipt_date = models.DateTimeField()
    item_quantity = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supply_receipts'


class SupplyReconciliations(models.Model):
    reconciliation_id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(SupplyItems, models.DO_NOTHING)
    item_quantity = models.BigIntegerField(blank=True, null=True)
    reconciliation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'supply_reconciliations'


class Taskboard(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    task_description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField()
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    jd_tag = models.ForeignKey(ContractJdAssoc, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taskboard'


class TaskboardToDtr(models.Model):
    dtr = models.OneToOneField(DailyTimeRecord, models.DO_NOTHING, primary_key=True)  # The composite primary key (dtr_id, task_id) found, that is not supported. The first column is selected.
    task = models.ForeignKey(Taskboard, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taskboard_to_dtr'
        unique_together = (('dtr', 'task'),)


class UccServiceList(models.Model):
    ucc_service_id = models.AutoField(primary_key=True)
    service_name = models.TextField()
    service_description = models.TextField(blank=True, null=True)
    date_established = models.DateField()
    date_removed = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ucc_service_list'
