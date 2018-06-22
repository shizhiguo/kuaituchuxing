# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    balance = models.BigIntegerField()
    enterprise_balance = models.BigIntegerField()
    bail = models.BigIntegerField()
    withdrawal_amount = models.BigIntegerField()
    not_withdrawal_amount = models.BigIntegerField()
    receipt_money = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    total_consumption_person = models.BigIntegerField()
    total_consumption_enterprise = models.BigIntegerField()
    promote_money = models.BigIntegerField()
    car_bail = models.IntegerField()
    bike_bail = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account'


class AccountCopy(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    balance = models.BigIntegerField()
    enterprise_balance = models.BigIntegerField()
    bail = models.BigIntegerField()
    withdrawal_amount = models.BigIntegerField()
    not_withdrawal_amount = models.BigIntegerField()
    receipt_money = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    total_consumption_person = models.BigIntegerField()
    total_consumption_enterprise = models.BigIntegerField()
    promote_money = models.BigIntegerField()
    car_bail = models.IntegerField()
    bike_bail = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account_copy'


class AccountWater(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.BigIntegerField()
    operator_type = models.IntegerField()
    user_id = models.BigIntegerField()
    income = models.IntegerField()
    money = models.IntegerField()
    before_balance = models.IntegerField()
    after_balance = models.IntegerField()
    style = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    order_serial_number = models.CharField(max_length=30)
    order_id = models.BigIntegerField(db_column='order_Id')  # Field name made lowercase.
    enterprise_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'account_water'


class AppInitConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    version_ios = models.CharField(max_length=20)
    version_android = models.CharField(max_length=20)
    version_android_staff = models.CharField(max_length=20)
    version_ios_staff = models.CharField(max_length=20)
    download_href = models.CharField(max_length=50)
    advertise_href = models.CharField(max_length=50)
    start_image_id = models.BigIntegerField()
    force_update_ios = models.IntegerField()
    force_update_android = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'app_init_config'


class AppPicture(models.Model):
    picture_id = models.IntegerField(primary_key=True)
    picture_type = models.IntegerField()
    click_url = models.CharField(max_length=50)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_picture'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AwardRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    award_id = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'award_record'


class BigDiscountCoupons(models.Model):
    id = models.BigAutoField(primary_key=True)
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    type = models.IntegerField()
    code = models.CharField(max_length=256)
    num = models.IntegerField()
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    small_deadline = models.IntegerField()
    small_start_time = models.DateTimeField()
    small_end_time = models.DateTimeField()
    big_deadline = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    pub_time = models.DateTimeField()
    effect_time = models.DateTimeField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()
    is_prize = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'big_discount_coupons'


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    picture = models.BigIntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license_tag = models.CharField(max_length=20)
    car_computer_unique = models.CharField(max_length=20)
    car_computer_password = models.CharField(max_length=100)
    control_center_supplier = models.CharField(max_length=50)
    supplier_id = models.BigIntegerField()
    control_center_factory = models.CharField(max_length=50)
    ccid = models.CharField(max_length=20)
    status = models.IntegerField()
    electricty = models.IntegerField()
    mileage = models.IntegerField()
    totalmileage = models.BigIntegerField(db_column='totalMileage')  # Field name made lowercase.
    maintainmileage = models.BigIntegerField(db_column='maintainMileage')  # Field name made lowercase.
    longitude = models.FloatField()
    latitude = models.FloatField()
    grade_id = models.BigIntegerField()
    park_id = models.BigIntegerField()
    insurance_maturity_time = models.DateTimeField()
    annual_survey_time = models.DateTimeField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    standard_mileage = models.IntegerField()
    company_by_risk = models.IntegerField()
    abatement = models.IntegerField()
    voltage = models.FloatField()
    seat = models.IntegerField()
    area_code = models.CharField(max_length=10)
    elec_module = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'car'


class CarChargeRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    sn = models.CharField(max_length=50, blank=True, null=True)
    charge_start_time = models.DateTimeField(blank=True, null=True)
    charge_end_time = models.DateTimeField(blank=True, null=True)
    before_voltage = models.IntegerField(blank=True, null=True)
    after_voltage = models.IntegerField(blank=True, null=True)
    before_time = models.BigIntegerField(blank=True, null=True)
    after_time = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    before_status = models.CharField(max_length=255, blank=True, null=True)
    after_status = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_charge_record'


class CarDispatch(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    car_id = models.BigIntegerField()
    status = models.BigIntegerField()
    from_park_id = models.BigIntegerField()
    from_latitude = models.FloatField()
    from_longitude = models.FloatField()
    to_park_id = models.BigIntegerField()
    to_latitude = models.FloatField()
    to_longitude = models.FloatField()
    description = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'car_dispatch'


class CarGrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    valuation_rule_id = models.BigIntegerField()
    description = models.CharField(max_length=10)
    code = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    effect_start_time = models.DateTimeField()
    effect_end_time = models.DateTimeField()
    morning_millisecond = models.BigIntegerField()
    night_millisecond = models.BigIntegerField()
    friday_millisecond = models.BigIntegerField()
    friday_afternoon = models.CharField(max_length=20)
    morning_str = models.CharField(max_length=20)
    night_str = models.CharField(max_length=20)
    full_night_minutes = models.IntegerField()
    full_day_minutes = models.IntegerField()
    full_week_night_minutes = models.IntegerField()
    full_week_day_minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'car_grade'


class CarTrajectory(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    type = models.IntegerField()
    car_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    latitude = models.TextField()
    longitude = models.TextField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'car_trajectory'


class CfnewCar(models.Model):
    car_id = models.IntegerField(blank=True, null=True)
    oldstatus = models.IntegerField(db_column='oldStatus', blank=True, null=True)  # Field name made lowercase.
    newstatus = models.IntegerField(db_column='newStatus', blank=True, null=True)  # Field name made lowercase.
    license_tag = models.CharField(max_length=200, blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cfnew_car'


class Complaint(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    picture = models.CharField(max_length=50)
    content = models.TextField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    deal_status = models.IntegerField()
    business_type = models.IntegerField()
    deal_service_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    tags = models.CharField(max_length=100)
    platform = models.IntegerField()
    app_version = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    relation_work_order_id = models.BigIntegerField()
    license_tag = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=300, blank=True, null=True)
    user_feedback = models.CharField(max_length=60, blank=True, null=True)
    is_free = models.IntegerField()
    area_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'complaint'


class ComplaintTag(models.Model):
    user_id = models.BigIntegerField()
    business_type = models.IntegerField()
    name = models.CharField(max_length=50)
    is_default = models.IntegerField()
    is_online = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    sequence = models.IntegerField()
    is_upload_photo = models.IntegerField()
    repair_type_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'complaint_tag'


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    distributable_money = models.BigIntegerField()
    money = models.BigIntegerField()
    status = models.IntegerField()
    enterprise_id = models.BigIntegerField()
    pid = models.BigIntegerField()
    operator = models.CharField(max_length=10)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    department_contact_person = models.CharField(max_length=5)
    department_contact_phone = models.CharField(max_length=20)
    total_consumption_department = models.BigIntegerField()
    user_id = models.BigIntegerField()
    type = models.IntegerField(db_column='TYPE')  # Field name made lowercase.
    display = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'department'


class DepartmentUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    department_id = models.BigIntegerField()
    enterprise_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    operator = models.CharField(max_length=10)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    display = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'department_user'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Enterprise(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    status = models.IntegerField()
    scale = models.IntegerField()
    nature = models.IntegerField()
    corporation = models.CharField(max_length=10)
    contacts = models.CharField(max_length=10)
    contact_phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=128)
    license = models.BigIntegerField()
    distributable_money = models.BigIntegerField()
    balance = models.BigIntegerField()
    credit_limit = models.IntegerField()
    cooperate_start_time = models.DateTimeField()
    cooperate_end_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    saler_id = models.BigIntegerField()
    area_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'enterprise'


class EnterpriseAccountWater(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.IntegerField()
    money = models.BigIntegerField()
    enterprise_id = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'enterprise_account_water'


class ExceptionOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    order_num = models.CharField(max_length=30)
    operator = models.CharField(max_length=20)
    exception_status = models.IntegerField()
    exception_situation = models.IntegerField()
    exception_remarks = models.CharField(max_length=512)
    create_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'exception_order'


class ExceptionOrderLog(models.Model):
    order_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    exception_status = models.IntegerField()
    exception_type = models.IntegerField()
    remark = models.CharField(max_length=90)
    action = models.PositiveIntegerField()
    sys_uid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'exception_order_log'


class GeoCity(models.Model):
    citycode = models.BigAutoField(primary_key=True)
    cityname = models.CharField(max_length=100)
    provcode = models.BigIntegerField()
    baiduid = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'geo_city'


class GeoCountry(models.Model):
    countrycode = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=100)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    chinese_alias = models.CharField(max_length=50)
    english_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'geo_country'


class GeoProvince(models.Model):
    provcode = models.BigAutoField(primary_key=True)
    provname = models.CharField(max_length=100)
    provalias = models.CharField(max_length=100)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'geo_province'


class GeoTown(models.Model):
    towncode = models.BigAutoField(primary_key=True)
    townname = models.CharField(max_length=100)
    provcode = models.BigIntegerField()
    citycode = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'geo_town'


class InitPicture(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform = models.IntegerField()
    app_type = models.IntegerField()
    start_page = models.CharField(max_length=100)
    welcome_page_first = models.CharField(max_length=100)
    welcome_page_second = models.CharField(max_length=100)
    welcome_page_third = models.CharField(max_length=100)
    welcome_page_fourth = models.CharField(max_length=100)
    welcome_page_fifth = models.CharField(max_length=100)
    to_advertise = models.IntegerField()
    advertise_url = models.CharField(max_length=100)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'init_picture'


class Invite(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    invited_user_id = models.BigIntegerField()
    small_discount_coupons_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    invite_coupon_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invite'


class InvoiceApply(models.Model):
    id = models.BigAutoField(primary_key=True)
    other_id = models.BigIntegerField()
    other_type = models.IntegerField()
    invoice_type = models.IntegerField()
    image_id = models.BigIntegerField()
    address = models.CharField(max_length=200)
    head_type = models.IntegerField()
    head_name = models.CharField(max_length=200)
    apply_mount = models.BigIntegerField()
    service_id = models.BigIntegerField()
    status = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    order_ids = models.CharField(max_length=500)
    tracking_num = models.CharField(max_length=128)
    user_name = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=15)
    invoice_content = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'invoice_apply'


class Kefu(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=10)
    type = models.IntegerField()
    contact = models.CharField(max_length=15)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    operator = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'kefu'


class KtAdminPromote(models.Model):
    promote_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    frozen = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    small_picture = models.IntegerField()
    big_picture = models.IntegerField()
    user_id = models.IntegerField()
    create_time = models.DateTimeField()
    area_code = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'kt_admin_promote'


class KuaituAdminBailConfig(models.Model):
    bail_money = models.IntegerField()
    business_type = models.IntegerField()
    country_code = models.CharField(max_length=10)
    area_code = models.CharField(max_length=10)
    effect_start_time = models.DateTimeField()
    effect_end_time = models.DateTimeField()
    create_time = models.DateTimeField()
    bail_free = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_admin_bail_config'


class KuaituAdminBaseCarbonEmission(models.Model):
    car_value = models.FloatField()
    bike_value = models.FloatField()
    unit = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_admin_base_carbon_emission'


class KuaituAdminBaseSwitch(models.Model):
    operation_code = models.CharField(max_length=50)
    operation_name = models.CharField(max_length=50)
    is_open = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_admin_base_switch'


class KuaituAdminCityOperation(models.Model):
    area_code = models.CharField(max_length=10)
    is_online = models.PositiveIntegerField()
    city_name = models.CharField(max_length=50)
    is_bike = models.PositiveIntegerField()
    is_car = models.PositiveIntegerField()
    bike_range = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    ad_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'kuaitu_admin_city_operation'


class KuaituAppAdvertise(models.Model):
    h5_title = models.CharField(max_length=50)
    h5_url = models.CharField(max_length=500)
    content = models.CharField(max_length=50)
    status = models.IntegerField()
    create_user_id = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    page_type = models.IntegerField()
    area_code = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'kuaitu_app_advertise'


class KuaituAppMsg(models.Model):
    code = models.CharField(max_length=255)
    msg = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kuaitu_app_msg'


class KuaituBike(models.Model):
    id = models.BigAutoField(primary_key=True)
    picture = models.BigIntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    bike_type = models.IntegerField()
    license_tag = models.CharField(unique=True, max_length=20)
    bike_machine_unique = models.CharField(unique=True, max_length=20)
    bike_machine_password = models.CharField(max_length=100)
    bike_machine_supplier = models.CharField(max_length=50)
    supplier_id = models.IntegerField()
    bike_machine_factory = models.CharField(max_length=50)
    ccid = models.CharField(max_length=20)
    use_status = models.IntegerField()
    lock_status = models.IntegerField()
    bike_status = models.IntegerField()
    battery = models.IntegerField()
    total_mileage = models.BigIntegerField()
    geocode = models.CharField(max_length=15)
    longitude = models.FloatField()
    latitude = models.FloatField()
    kuaitu_bike_valuation_rule = models.BigIntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    area_code = models.CharField(max_length=10)
    is_online = models.PositiveIntegerField()
    bike_machine_key = models.CharField(max_length=100)
    lock_type = models.PositiveIntegerField()
    auto_report_longitude = models.FloatField()
    auto_report_latitude = models.FloatField()
    auto_report_time = models.DateTimeField()
    device_id = models.CharField(max_length=20)
    ad_code = models.CharField(max_length=10)
    create_user_id = models.BigIntegerField()
    update_user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike'


class KuaituBikeCheck(models.Model):
    id = models.BigAutoField(primary_key=True)
    check_no = models.CharField(max_length=20)
    repair_no = models.CharField(max_length=20)
    bike_no = models.CharField(max_length=20)
    lock_id = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_code = models.CharField(max_length=10)
    lock_type = models.PositiveIntegerField()
    lock_status = models.IntegerField()
    bike_status = models.IntegerField()
    user_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    battery = models.IntegerField()
    factory_test = models.PositiveIntegerField()
    check_status = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_check'


class KuaituBikeDispatch(models.Model):
    id = models.BigAutoField(primary_key=True)
    dispatch_no = models.CharField(max_length=20)
    bike_no = models.CharField(max_length=20)
    lock_id = models.CharField(max_length=20)
    before_longitude = models.FloatField()
    before_latitude = models.FloatField()
    before_user_id = models.BigIntegerField()
    before_create_time = models.DateTimeField()
    after_longitude = models.FloatField()
    after_latitude = models.FloatField()
    after_user_id = models.BigIntegerField()
    after_create_time = models.DateTimeField()
    dispatch_status = models.IntegerField()
    area_code = models.CharField(max_length=20, blank=True, null=True)
    ad_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_dispatch'


class KuaituBikeHotspot(models.Model):
    area_code = models.CharField(max_length=10)
    hotspot_name = models.CharField(max_length=50)
    fence_list = models.TextField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_hotspot'


class KuaituBikeInitOnline(models.Model):
    id = models.BigAutoField(primary_key=True)
    bike_no = models.CharField(max_length=20)
    lock_id = models.CharField(max_length=20)
    bike_machine_password = models.CharField(max_length=100)
    bike_machine_key = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_code = models.CharField(max_length=10)
    lock_type = models.PositiveIntegerField()
    user_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    ad_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_init_online'


class KuaituBikeInitSumTemp(models.Model):
    id = models.BigAutoField(primary_key=True)
    sum_date = models.CharField(max_length=10)
    area_code = models.CharField(max_length=10)
    day_init_num = models.BigIntegerField()
    day_del_num = models.BigIntegerField()
    sum_init_num = models.BigIntegerField()
    sum_del_num = models.BigIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_init_sum_temp'


class KuaituBikeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    bike_id = models.BigIntegerField(blank=True, null=True)
    bike_no = models.CharField(max_length=20, blank=True, null=True)
    lock_no = models.CharField(max_length=20, blank=True, null=True)
    lock_type = models.IntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    order_no = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    area_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    operation_type = models.IntegerField(blank=True, null=True)
    error_type = models.IntegerField(blank=True, null=True)
    error_code = models.CharField(max_length=20, blank=True, null=True)
    error_msg = models.CharField(max_length=255, blank=True, null=True)
    platform = models.IntegerField(blank=True, null=True)
    bluetooth_version = models.CharField(max_length=255, blank=True, null=True)
    phone_model = models.CharField(max_length=255, blank=True, null=True)
    phone_sys_version = models.CharField(max_length=255, blank=True, null=True)
    app_version = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()
    operation_exe = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_log'


class KuaituBikeLuckyPacket(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    bike_id = models.BigIntegerField(blank=True, null=True)
    bike_no = models.CharField(max_length=20)
    lock_id = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_code = models.CharField(max_length=10)
    lock_type = models.PositiveIntegerField()
    receive_user_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    status = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hotspot_id = models.BigIntegerField(blank=True, null=True)
    hotspot_name = models.CharField(max_length=200)
    return_name = models.CharField(max_length=200)
    is_receive_task = models.IntegerField()
    prize_amount = models.CharField(max_length=200)
    is_receive_prize = models.BigIntegerField(blank=True, null=True)
    source_type = models.IntegerField()
    biz_type = models.IntegerField()
    biz_id = models.CharField(max_length=200)
    create_order_id = models.BigIntegerField(blank=True, null=True)
    create_user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_lucky_packet'


class KuaituBikeLuckyPacketConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    bike_no = models.CharField(max_length=20)
    type = models.IntegerField()
    status = models.IntegerField()
    create_user_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_lucky_packet_config'


class KuaituBikeLuckyPacketLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    bike_id = models.BigIntegerField(blank=True, null=True)
    bike_no = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()
    user_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_lucky_packet_log'


class KuaituBikeMissing(models.Model):
    id = models.BigAutoField(primary_key=True)
    bike_id = models.BigIntegerField()
    bike_no = models.CharField(max_length=20)
    user_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    source_type = models.IntegerField(blank=True, null=True)
    missing_status = models.IntegerField()
    biz_no = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_missing'


class KuaituBikeOperationLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    bike_id = models.BigIntegerField()
    bike_no = models.CharField(max_length=20)
    lock_id = models.CharField(max_length=20)
    operation_type = models.IntegerField()
    reason = models.CharField(max_length=256)
    area_code = models.CharField(max_length=10)
    longitude = models.FloatField()
    latitude = models.FloatField()
    user_id = models.BigIntegerField()
    user_area_code = models.CharField(max_length=10)
    user_longitude = models.FloatField()
    user_latitude = models.FloatField()
    create_time = models.DateTimeField()
    hotspot_id = models.IntegerField(blank=True, null=True)
    biz_no = models.CharField(max_length=20)
    ad_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_operation_log'


class KuaituBikeRelieve(models.Model):
    relieve_id = models.BigAutoField(primary_key=True)
    relieve_create_time = models.DateTimeField()
    id = models.BigIntegerField()
    picture = models.BigIntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    bike_type = models.IntegerField()
    license_tag = models.CharField(max_length=20)
    bike_machine_unique = models.CharField(max_length=20)
    bike_machine_password = models.CharField(max_length=100)
    bike_machine_supplier = models.CharField(max_length=50)
    supplier_id = models.IntegerField()
    bike_machine_factory = models.CharField(max_length=50)
    ccid = models.CharField(max_length=20)
    use_status = models.IntegerField()
    lock_status = models.IntegerField()
    bike_status = models.IntegerField()
    battery = models.IntegerField()
    total_mileage = models.BigIntegerField()
    geocode = models.CharField(max_length=15)
    longitude = models.FloatField()
    latitude = models.FloatField()
    kuaitu_bike_valuation_rule = models.BigIntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    area_code = models.CharField(max_length=10)
    is_online = models.PositiveIntegerField()
    bike_machine_key = models.CharField(max_length=100)
    lock_type = models.PositiveIntegerField()
    auto_report_longitude = models.FloatField()
    auto_report_latitude = models.FloatField()
    auto_report_time = models.DateTimeField()
    device_id = models.CharField(max_length=20)
    ad_code = models.CharField(max_length=10)
    create_user_id = models.BigIntegerField()
    update_user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_relieve'


class KuaituBikeRepair(models.Model):
    id = models.BigAutoField(primary_key=True)
    repair_no = models.CharField(max_length=20)
    bike_no = models.CharField(max_length=20)
    lock_id = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_code = models.CharField(max_length=10)
    lock_type = models.PositiveIntegerField()
    lock_status = models.IntegerField()
    bike_status = models.IntegerField()
    user_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    battery = models.IntegerField()
    factory_test = models.PositiveIntegerField()
    bike_repair_type = models.CharField(max_length=20)
    bike_repair_msg = models.CharField(max_length=200)
    bike_repair_pic = models.CharField(max_length=500)
    source_type = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_repair'


class KuaituBikeRepairType(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_repair_type'


class KuaituBikeScrap(models.Model):
    scrap_id = models.BigAutoField(primary_key=True)
    scrap_time = models.DateTimeField()
    scrap_src = models.BigIntegerField()
    id = models.BigIntegerField()
    picture = models.BigIntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    bike_type = models.IntegerField()
    license_tag = models.CharField(max_length=20)
    bike_machine_unique = models.CharField(max_length=20)
    bike_machine_password = models.CharField(max_length=100)
    bike_machine_supplier = models.CharField(max_length=50)
    supplier_id = models.IntegerField()
    bike_machine_factory = models.CharField(max_length=50)
    ccid = models.CharField(max_length=20)
    use_status = models.IntegerField()
    lock_status = models.IntegerField()
    bike_status = models.IntegerField()
    battery = models.IntegerField()
    total_mileage = models.BigIntegerField()
    geocode = models.CharField(max_length=15)
    longitude = models.FloatField()
    latitude = models.FloatField()
    kuaitu_bike_valuation_rule = models.BigIntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    area_code = models.CharField(max_length=10)
    is_online = models.PositiveIntegerField()
    bike_machine_key = models.CharField(max_length=100)
    lock_type = models.PositiveIntegerField()
    auto_report_longitude = models.FloatField()
    auto_report_latitude = models.FloatField()
    auto_report_time = models.DateTimeField()
    device_id = models.CharField(max_length=20)
    ad_code = models.CharField(max_length=10)
    create_user_id = models.BigIntegerField()
    update_user_id = models.BigIntegerField()
    batch_no = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_scrap'


class KuaituBikeValuationRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    week_day_price = models.IntegerField()
    week_night_price = models.IntegerField()
    weekend_day_price = models.IntegerField()
    weekend_night_price = models.IntegerField()
    ceiling_seconds = models.BigIntegerField()
    ceiling_price = models.BigIntegerField()
    is_ceiling = models.IntegerField()
    is_on_special = models.IntegerField()
    special_price = models.IntegerField()
    rule_status = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    area_code = models.CharField(max_length=10)
    billing_cycle = models.IntegerField()
    external = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_valuation_rule'


class KuaituBikeWls(models.Model):
    id = models.BigAutoField(primary_key=True)
    bike_id = models.BigIntegerField()
    bike_no = models.CharField(max_length=20)
    lock_id = models.CharField(max_length=20)
    wls_platform = models.PositiveIntegerField()
    update_batch = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    area_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'kuaitu_bike_wls'


class KuaituConcessionCard(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    description = models.CharField(max_length=255)
    picture = models.BigIntegerField()
    status = models.IntegerField()
    use_days = models.BigIntegerField()
    user_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    area_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'kuaitu_concession_card'


class KuaituDrawLotteryCollect(models.Model):
    id = models.BigAutoField(primary_key=True)
    draw_count = models.IntegerField()
    draw_user_count = models.IntegerField()
    receive_user_count = models.IntegerField()
    area_code = models.CharField(max_length=10)
    collect_time = models.DateField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_draw_lottery_collect'


class KuaituEggRanking(models.Model):
    user_id = models.IntegerField(primary_key=True)
    egg_num = models.IntegerField()
    ranking = models.IntegerField()
    last_valid_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_egg_ranking'


class KuaituEggRecord(models.Model):
    user_id = models.IntegerField()
    type = models.IntegerField()
    friend_user_id = models.IntegerField()
    egg_num = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_egg_record'


class KuaituMmaPrizeConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    business_coupon_id = models.IntegerField()
    business_id = models.IntegerField()
    user_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    modify_id = models.BigIntegerField()
    modify_time = models.DateTimeField()
    area_code = models.CharField(max_length=10)
    status = models.IntegerField()
    day_count = models.IntegerField()
    prize_proportion = models.IntegerField()
    total_count = models.IntegerField()
    type = models.IntegerField()
    show_style = models.IntegerField()
    additional = models.CharField(max_length=255)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_mma_prize_config'


class KuaituOrderConcessionCard(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    user_concession_card_id = models.BigIntegerField()
    concession_card_name = models.CharField(max_length=255)
    final_money = models.IntegerField()
    special_money = models.IntegerField()
    create_time = models.DateTimeField()
    area_code = models.CharField(max_length=10)
    ad_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kuaitu_order_concession_card'


class KuaituOrderSpecial(models.Model):
    order_id = models.IntegerField()
    special_id = models.IntegerField()
    special_name = models.CharField(max_length=255)
    final_money = models.IntegerField()
    special_money = models.IntegerField()
    is_coupon_pay = models.IntegerField()
    no_coupon_pay_reason = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_order_special'


class KuaituParkFence(models.Model):
    park_id = models.IntegerField()
    fence_range = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    show_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_park_fence'


class KuaituRefundBailConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    area_code = models.CharField(max_length=20)
    ad_code = models.CharField(max_length=20)
    status = models.IntegerField()
    content = models.CharField(max_length=200)
    button_one_name = models.CharField(max_length=200)
    button_one_url = models.CharField(max_length=200)
    button_one_title = models.CharField(max_length=200)
    button_two_name = models.CharField(max_length=200)
    button_two_url = models.CharField(max_length=200)
    button_two_title = models.CharField(max_length=200)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_refund_bail_config'


class KuaituRefundBailReward(models.Model):
    id = models.BigAutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_code = models.CharField(max_length=20)
    ad_code = models.CharField(max_length=20)
    status = models.IntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    reward_type = models.IntegerField()
    create_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    opertion_id = models.BigIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'kuaitu_refund_bail_reward'


class KuaituTemporaryBike(models.Model):
    license_tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kuaitu_temporary_bike'


class KuaituUserCardCoupons(models.Model):
    id = models.BigAutoField(primary_key=True)
    business_coupon_id = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    user_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    use_time = models.DateTimeField()
    business_id = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_user_card_coupons'


class KuaituUserConcessionCard(models.Model):
    id = models.BigAutoField(primary_key=True)
    concession_card_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    pay_type = models.IntegerField()
    create_time = models.DateTimeField()
    status = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    amount = models.BigIntegerField()
    trade_no = models.CharField(unique=True, max_length=32)
    area_code = models.CharField(max_length=10)
    ad_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'kuaitu_user_concession_card'


class KuaituUserMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    message_type = models.IntegerField()
    function_type = models.IntegerField()
    content_type = models.IntegerField()
    additional = models.CharField(max_length=100)
    status = models.IntegerField()
    weight = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_user_message'


class KuaituUserParkRemind(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    park_id = models.BigIntegerField()
    status = models.IntegerField()
    area_code = models.CharField(max_length=10)
    cancel_type = models.IntegerField()
    push_car_idstr = models.CharField(max_length=300)
    remind_minutes = models.IntegerField()
    create_time = models.DateTimeField()
    cancel_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_user_park_remind'


class KuaituUserPrize(models.Model):
    id = models.BigAutoField(primary_key=True)
    prize_user_id = models.BigIntegerField(blank=True, null=True)
    prize_longitude = models.FloatField()
    prize_latitude = models.FloatField()
    prize_address_name = models.CharField(max_length=200)
    prize_area_code = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    is_receive_prize = models.BigIntegerField(blank=True, null=True)
    source_type = models.IntegerField()
    prize_id = models.BigIntegerField(blank=True, null=True)
    prize_name = models.CharField(max_length=50, blank=True, null=True)
    business_id = models.IntegerField()
    business_name = models.CharField(max_length=200)
    biz_type = models.IntegerField()
    biz_id = models.IntegerField()
    business_coupon_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kuaitu_user_prize'


class KuaituUserViolationDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    bike_id = models.BigIntegerField()
    violation_type = models.IntegerField()
    status = models.IntegerField()
    user_id = models.BigIntegerField()
    modify_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    debit = models.BigIntegerField()
    debit_time = models.DateTimeField()
    license_tag = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'kuaitu_user_violation_details'


class KuaituWechatUnionid(models.Model):
    appid = models.CharField(max_length=200)
    openid = models.CharField(max_length=200)
    unionid = models.CharField(max_length=200)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuaitu_wechat_unionid'


class KuaituWechatUser(models.Model):
    openid = models.CharField(max_length=200)
    head_image = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=20)
    status = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    nickname = models.CharField(max_length=100)
    sex = models.IntegerField()
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    unionid = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'kuaitu_wechat_user'


class LogMobileChange(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    old_mobile = models.BigIntegerField()
    new_mobile = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'log_mobile_change'


class LogWorkReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    sys_user_id = models.BigIntegerField()
    car_id = models.BigIntegerField()
    work_order_id = models.BigIntegerField()
    car_license = models.CharField(max_length=40)
    image_id = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=500)
    operator_id = models.BigIntegerField()
    status = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'log_work_report'


class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    ext = models.CharField(max_length=5)
    size = models.BigIntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'media'


class Newtable(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newtable'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    operator = models.BigIntegerField()
    operator_type = models.IntegerField()
    operator_info = models.CharField(max_length=256)
    car_id = models.BigIntegerField()
    order_num = models.CharField(max_length=30)
    status = models.IntegerField()
    on_park_id = models.BigIntegerField()
    on_location_name = models.CharField(max_length=50)
    on_latitude = models.FloatField()
    on_longitude = models.FloatField()
    on_mileage = models.IntegerField()
    is_abatement = models.IntegerField()
    abatement = models.IntegerField()
    is_company_by_risk = models.IntegerField()
    company_by_risk = models.IntegerField()
    down_park_id = models.BigIntegerField()
    down_location_name = models.CharField(max_length=50)
    down_latitude = models.FloatField()
    down_longitude = models.FloatField()
    down_mileage = models.IntegerField()
    pay_type = models.IntegerField()
    mileage = models.IntegerField()
    real_price = models.IntegerField()
    order_time = models.DateTimeField()
    start_billing_time = models.DateTimeField()
    end_billing_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    remarks = models.CharField(max_length=256)
    version = models.BigIntegerField()
    order_business_type = models.IntegerField()
    order_price = models.IntegerField()
    coupon_id = models.BigIntegerField()
    promote_money = models.IntegerField()
    is_invoice = models.IntegerField()
    platform = models.IntegerField()
    display = models.IntegerField()
    carbon_emission = models.IntegerField()
    numerical = models.IntegerField()
    day_minutes = models.IntegerField()
    day_money = models.IntegerField()
    night_minutes = models.IntegerField()
    night_money = models.IntegerField()
    timeout_minutes = models.IntegerField()
    timeout_money = models.IntegerField()
    day_special_amount = models.IntegerField()
    day_special_sub = models.IntegerField()
    business_week_special_amount = models.IntegerField()
    business_week_special_sub = models.IntegerField()
    weekend_special_amount = models.IntegerField()
    weekend_special_sub = models.IntegerField()
    full_week_special_amount = models.IntegerField()
    full_week_special_sub = models.IntegerField()
    is_exception = models.IntegerField()
    pause_money = models.IntegerField()
    area_code = models.CharField(max_length=20)
    ad_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersFreezeLog(models.Model):
    order_id = models.BigIntegerField()
    status = models.IntegerField()
    finish_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders_freeze_log'


class OrdersOperatorLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    ip = models.CharField(max_length=50)
    reason = models.CharField(max_length=256)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders_operator_log'


class Package(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    p_key = models.CharField(db_column='P_KEY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    coupons_id = models.CharField(db_column='COUPONS_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='START_TIME', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'package'


class Park(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    status = models.IntegerField()
    type = models.IntegerField()
    enterprise_id = models.BigIntegerField()
    location_name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    geo_code = models.CharField(max_length=12)
    total_seat = models.IntegerField()
    available_car = models.IntegerField()
    available_seat = models.IntegerField()
    start_time = models.CharField(max_length=30)
    end_time = models.CharField(max_length=30)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    citycode = models.BigIntegerField(blank=True, null=True)
    provcode = models.BigIntegerField()
    towncode = models.BigIntegerField()
    countrycode = models.BigIntegerField()
    area_name = models.CharField(max_length=200)
    park_level = models.IntegerField()
    regist_car = models.IntegerField()
    operate_range = models.IntegerField()
    area_code = models.CharField(max_length=10)
    park_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'park'


class PushMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    type = models.IntegerField()
    style = models.IntegerField()
    status = models.IntegerField()
    last_user_id = models.BigIntegerField()
    finish_time = models.DateTimeField()
    effective_time = models.DateTimeField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'push_message'


class RechargeOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    money = models.IntegerField()
    account_id = models.BigIntegerField()
    style = models.IntegerField()
    status = models.IntegerField()
    third_pay_order_no = models.CharField(max_length=128)
    type = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    user_id = models.BigIntegerField()
    coupon_id = models.BigIntegerField()
    trade_no = models.CharField(max_length=32)
    promote_money = models.IntegerField()
    platform = models.IntegerField()
    area_code = models.CharField(max_length=10)
    total_money = models.IntegerField()
    third_status = models.IntegerField()
    business_type = models.IntegerField()
    submit_third_time = models.DateTimeField()
    refund_money = models.IntegerField()
    refund_promote = models.IntegerField()
    refunding_money = models.IntegerField()
    refunding_promote = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recharge_order'


class RechargeTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    recharge_price = models.BigIntegerField()
    extra_price = models.BigIntegerField()
    remarks = models.CharField(max_length=50)
    is_active = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recharge_template'


class SmallDiscountCoupons(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons'


class SmallDiscountCoupons1(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_1'


class SmallDiscountCoupons10(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_10'


class SmallDiscountCoupons11(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_11'


class SmallDiscountCoupons12(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_12'


class SmallDiscountCoupons2(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_2'


class SmallDiscountCoupons3(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_3'


class SmallDiscountCoupons4(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_4'


class SmallDiscountCoupons5(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_5'


class SmallDiscountCoupons6(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_6'


class SmallDiscountCoupons7(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_7'


class SmallDiscountCoupons8(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_8'


class SmallDiscountCoupons9(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    icon = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    style = models.IntegerField()
    code = models.CharField(max_length=256)
    uid = models.BigIntegerField(blank=True, null=True)
    used_uid = models.BigIntegerField(blank=True, null=True)
    account_water_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    discount = models.FloatField()
    denomination = models.IntegerField()
    status = models.IntegerField()
    deadline = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    effect_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    version = models.BigIntegerField()
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'small_discount_coupons_9'


class StaffAnnouncement(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    info = models.CharField(max_length=300, blank=True, null=True)
    image = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=60, blank=True, null=True)
    recommend = models.IntegerField(blank=True, null=True)
    pub_group = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_announcement'


class StaffBikeExamine(models.Model):
    id = models.BigAutoField(primary_key=True)
    staff_user_id = models.IntegerField()
    kuaitu_bike_id = models.BigIntegerField()
    operate = models.CharField(max_length=300)
    examine_result = models.IntegerField()
    examine_time = models.DateTimeField()
    online_time = models.DateTimeField()
    license_tag = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'staff_bike_examine'


class StaffBikeOrder(models.Model):
    user_id = models.IntegerField()
    work_type = models.IntegerField()
    create_user_id = models.IntegerField()
    level = models.IntegerField()
    instruction = models.CharField(max_length=500)
    order_num = models.CharField(unique=True, max_length=30)
    status = models.IntegerField()
    is_online = models.IntegerField()
    description = models.CharField(max_length=500)
    requirement = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    receive_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    expect_minutes = models.IntegerField()
    timeout_minutes = models.IntegerField()
    relation_order_id = models.BigIntegerField()
    area_code = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=20)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    distribute_type = models.IntegerField()
    title = models.CharField(max_length=20)
    bike_ids = models.CharField(max_length=500)
    send_group = models.CharField(max_length=50)
    task_types = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_bike_order'


class StaffBikeOrderLog(models.Model):
    staff_bike_order_id = models.IntegerField()
    user_id = models.IntegerField()
    car_bike_action = models.IntegerField()
    car_bike_result = models.IntegerField()
    car_order_time = models.DateTimeField()
    license_tag = models.CharField(max_length=20)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_bike_order_log'


class StaffCarOrder(models.Model):
    order_num = models.CharField(unique=True, max_length=30)
    work_type = models.IntegerField()
    title = models.CharField(max_length=500)
    user_id = models.IntegerField()
    create_user_id = models.IntegerField()
    level = models.IntegerField()
    instruction = models.CharField(max_length=500)
    status = models.IntegerField()
    is_online = models.IntegerField()
    description = models.CharField(max_length=500)
    requirement = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    receive_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    expect_minutes = models.IntegerField()
    timeout_minutes = models.IntegerField()
    relation_order_id = models.BigIntegerField()
    area_code = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    distribute_type = models.IntegerField()
    car_id = models.BigIntegerField()
    car_status = models.IntegerField()
    send_group = models.CharField(max_length=50)
    version = models.BigIntegerField()
    task_types = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_car_order'


class StaffCarOrderLog(models.Model):
    staff_car_order_id = models.IntegerField()
    user_id = models.IntegerField()
    car_order_action = models.IntegerField()
    car_order_result = models.IntegerField()
    car_order_time = models.DateTimeField()
    license_tag = models.CharField(max_length=20)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_car_order_log'


class StaffCarSendGroup(models.Model):
    group_name = models.CharField(max_length=30)
    area_code = models.CharField(max_length=11)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff_car_send_group'


class StaffDictionary(models.Model):
    id = models.BigAutoField(primary_key=True)
    keyvalue = models.CharField(db_column='keyValue', max_length=50, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_dictionary'


class StaffDuty(models.Model):
    sys_uid = models.IntegerField(blank=True, null=True)
    duty_time = models.CharField(max_length=8, blank=True, null=True)
    duty_img = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_duty'


class StaffNotice(models.Model):
    create_time = models.DateTimeField(blank=True, null=True)
    workorder_id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=120, blank=True, null=True)
    pub_user = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    area_code = models.CharField(max_length=10, blank=True, null=True)
    business_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'staff_notice'


class StaffNoticeType(models.Model):
    type_id = models.PositiveIntegerField(blank=True, null=True)
    type_info = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_notice_type'


class StaffOrderTask(models.Model):
    staff_order_id = models.IntegerField()
    task_type = models.IntegerField()
    image_ids = models.CharField(max_length=50)
    instruction = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    dispatch_id = models.IntegerField()
    location_name = models.CharField(max_length=50)
    level = models.IntegerField()
    order_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_order_task'


class StaffPushNews(models.Model):
    user_id = models.IntegerField()
    workorder_id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=300, blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    business_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_push_news'


class StaffTaskDispatch(models.Model):
    from_park_id = models.BigIntegerField()
    from_latitude = models.FloatField()
    from_longitude = models.FloatField()
    to_park_id = models.BigIntegerField()
    to_latitude = models.FloatField()
    to_longitude = models.FloatField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff_task_dispatch'


class StaffUser(models.Model):
    name = models.CharField(max_length=20)
    status = models.IntegerField()
    user_type = models.IntegerField()
    business_type = models.IntegerField()
    phone_num = models.CharField(max_length=20)
    identity_card_num = models.CharField(max_length=18)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    platform = models.IntegerField()
    app_version = models.CharField(max_length=10)
    drive_number = models.CharField(max_length=18)
    order_number = models.IntegerField()
    franchisee_id = models.IntegerField()
    area_code = models.CharField(max_length=100)
    id_card_img = models.CharField(max_length=20)
    driver_license_img = models.CharField(max_length=10)
    driver_license_file_no = models.BigIntegerField()
    driver_license_level = models.CharField(max_length=10)
    id_card_valid = models.DateField()
    driver_license_valid = models.DateField()
    auto_receive_status = models.IntegerField()
    tokean = models.CharField(max_length=200, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_user'


class StaffUserCoordinate(models.Model):
    user_id = models.IntegerField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_user_coordinate'


class StaffUserSignin(models.Model):
    user_id = models.IntegerField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    signin_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_user_signin'


class StaffUserWorkOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    car_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    remaker = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(unique=True, blank=True, null=True)
    upload_pic = models.CharField(max_length=500, blank=True, null=True)
    fail_type = models.CharField(max_length=30, blank=True, null=True)
    approve_user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_user_work_order'


class SysResource(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    parent_id = models.BigIntegerField(blank=True, null=True)
    parent_ids = models.CharField(max_length=20, blank=True, null=True)
    permission = models.CharField(max_length=20, blank=True, null=True)
    available = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    operator = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sys_resource'


class SysRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=100)
    role_code = models.IntegerField()
    description = models.CharField(max_length=100)
    available = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    operator = models.CharField(max_length=100)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleResource(models.Model):
    id = models.BigAutoField(primary_key=True)
    sys_role_id = models.BigIntegerField()
    sys_resource_id = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_role_resource'


class SysUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    status = models.IntegerField()
    phone_num = models.CharField(max_length=20)
    identity_card_num = models.CharField(max_length=20)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    locked = models.IntegerField()
    operator = models.CharField(max_length=100)
    is_enterprise = models.IntegerField()
    enterprise_id = models.BigIntegerField()
    login_ip = models.CharField(max_length=20)
    last_login_time = models.DateField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    plantform = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'
        unique_together = (('id', 'username'),)


class SysUserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    sys_user_id = models.BigIntegerField()
    sys_role_id = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class TempUser(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_num = models.CharField(max_length=255, blank=True, null=True)
    idid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'temp_user'


class Tempage(models.Model):
    identity_card_num = models.CharField(max_length=20)
    age1 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempage'


class Temparea(models.Model):
    city_name = models.CharField(max_length=50)
    sum1 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'temparea'


class Tempgender(models.Model):
    identity_card_num = models.CharField(max_length=20)
    bit17 = models.CharField(max_length=1, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempgender'


class Tempprice(models.Model):
    mon = models.CharField(max_length=7, blank=True, null=True)
    city_name = models.CharField(max_length=50)
    yuan = models.DecimalField(max_digits=36, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempprice'


class Tmphouruser(models.Model):
    hour = models.CharField(max_length=7, blank=True, null=True)
    user_id = models.BigIntegerField()
    num = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tmphouruser'


class Tmpmonuser(models.Model):
    mon = models.CharField(db_column='Mon', max_length=7, blank=True, null=True)  # Field name made lowercase.
    user_id = models.BigIntegerField()
    count_field = models.BigIntegerField(db_column='count(*)')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'tmpmonuser'


class Tmpuserbill(models.Model):
    user_id = models.BigIntegerField()
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmpuserbill'


class Tmpuservalid(models.Model):
    userid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tmpuservalid'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    picture = models.BigIntegerField()
    identity_positive_picture = models.BigIntegerField()
    identity_opposite_picture = models.BigIntegerField()
    driving_licence_picture = models.BigIntegerField()
    gender = models.IntegerField()
    age = models.IntegerField()
    status = models.IntegerField()
    phone_num = models.CharField(max_length=15)
    password = models.CharField(max_length=256)
    device_token = models.CharField(max_length=256)
    platform = models.IntegerField()
    identity_card_num = models.CharField(max_length=20)
    driving_licence_num = models.CharField(max_length=20)
    numerical = models.BigIntegerField()
    location = models.CharField(max_length=128)
    login_ip = models.CharField(max_length=50)
    is_enterprise = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    last_login_time = models.DateTimeField()
    version = models.BigIntegerField()
    full_name = models.CharField(max_length=10)
    identity_status = models.IntegerField()
    license_status = models.IntegerField()
    enterprise_id = models.BigIntegerField()
    nationality = models.CharField(max_length=10)
    date_of_birth = models.CharField(max_length=15)
    identity_card_period_of_validity = models.CharField(max_length=15)
    driving_licence_period_of_validity = models.CharField(max_length=15)
    file_number = models.CharField(max_length=20)
    quasi_driving_type = models.CharField(max_length=15)
    licensing_of_time = models.CharField(max_length=15)
    examination_department = models.CharField(max_length=15)
    carbon_emission = models.IntegerField()
    area_code = models.CharField(max_length=10)
    is_bike_bail_free = models.IntegerField()
    bike_bail_free_reason = models.IntegerField()
    commit_license_time = models.DateTimeField()
    examine_time = models.DateTimeField()
    examine_user_id = models.BigIntegerField()
    source = models.IntegerField()
    ad_code = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'


class UserArpuTmp(models.Model):
    user_id = models.BigIntegerField()
    user_arpu = models.DecimalField(max_digits=37, decimal_places=4, blank=True, null=True)
    arpu_range = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_arpu_tmp'


class UserLogin(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    type = models.IntegerField()
    log_ip = models.CharField(max_length=50)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_login'


class UserStatInfo(models.Model):
    user_id = models.BigIntegerField()
    gender = models.IntegerField()
    age = models.IntegerField()
    user_status = models.IntegerField()
    user_platform = models.IntegerField()
    identity_card_num = models.CharField(max_length=20)
    driving_licence_num = models.CharField(max_length=20)
    is_enterprise = models.IntegerField()
    create_time = models.DateTimeField()
    last_login_time = models.DateTimeField()
    user_area_code = models.CharField(max_length=10)
    is_bike_bail_free = models.IntegerField()
    bike_bail_free_reason = models.IntegerField()
    ad_code = models.CharField(max_length=10)
    account_id = models.BigIntegerField(blank=True, null=True)
    balance = models.BigIntegerField(blank=True, null=True)
    bail = models.BigIntegerField(blank=True, null=True)
    car_bail = models.IntegerField(blank=True, null=True)
    bike_bail = models.IntegerField(blank=True, null=True)
    car_id = models.BigIntegerField(blank=True, null=True)
    order_status = models.IntegerField(blank=True, null=True)
    pay_type = models.IntegerField(blank=True, null=True)
    real_price = models.IntegerField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=256, blank=True, null=True)
    order_business_type = models.IntegerField(blank=True, null=True)
    order_platform = models.IntegerField(blank=True, null=True)
    order_area_code = models.CharField(max_length=20, blank=True, null=True)
    order_ad_code = models.CharField(max_length=20, blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    recharge_order_account_id = models.BigIntegerField(blank=True, null=True)
    style = models.IntegerField(blank=True, null=True)
    recharge_order_status = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    recharge_order_user_id = models.BigIntegerField(blank=True, null=True)
    recharge_order_platform = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_stat_info'


class UserTmp1(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_tmp1'


class ValuationRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    min_day = models.BigIntegerField()
    min_night = models.BigIntegerField()
    week_min_day = models.BigIntegerField()
    week_min_night = models.BigIntegerField()
    maximum_day = models.BigIntegerField()
    weekend_offers = models.BigIntegerField()
    maximum_week = models.BigIntegerField()
    business_week_rent = models.BigIntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    area_code = models.CharField(max_length=10)
    special_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'valuation_rule'


class VersionControl(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform = models.IntegerField()
    type = models.IntegerField()
    version_num = models.CharField(max_length=10)
    style = models.IntegerField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    update_title = models.CharField(max_length=50)
    update_content = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'version_control'


class WechatActivityOrder(models.Model):
    activity_type = models.IntegerField()
    openid = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    kuaitu_user = models.IntegerField()
    kuaitu_phone = models.CharField(max_length=20)
    grant_coupon = models.IntegerField()
    join_person_count = models.IntegerField()
    money = models.IntegerField()
    status = models.IntegerField()
    order_num = models.CharField(max_length=30)
    create_time = models.DateTimeField()
    person_code = models.CharField(max_length=255)
    sign_up_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wechat_activity_order'


class WechatActivityOrderSummary(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=20)
    user_id = models.BigIntegerField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    order_second = models.BigIntegerField(blank=True, null=True)
    openid = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wechat_activity_order_summary'


class WechatUserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    user_type = models.IntegerField()
    openid = models.CharField(max_length=200)
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wechat_user_info'


class WorkOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    user_type = models.BigIntegerField()
    work_type = models.BigIntegerField()
    car_dispatch_id = models.BigIntegerField()
    operator = models.BigIntegerField()
    level = models.IntegerField()
    instruction = models.CharField(max_length=500)
    car_id = models.BigIntegerField()
    order_num = models.CharField(max_length=30)
    status = models.IntegerField()
    description = models.CharField(max_length=500)
    requirement = models.CharField(max_length=500)
    customer_phone = models.CharField(max_length=20)
    order_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    create_time = models.DateTimeField()
    version = models.BigIntegerField()
    car_status = models.IntegerField()
    relation_order_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'work_order'
