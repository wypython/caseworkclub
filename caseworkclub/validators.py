from django.core.validators import RegexValidator

phone_regex = r'0[0-9]{10}'
phone_validator= RegexValidator(regex=phone_regex,message="Phonenumber must be 11 digits long and start with 0")

membership_number_regex = r'[A-Z]\d{5}'
membership_number_validator = RegexValidator(regex=membership_number_regex,message="NUT Membership Numbers have a capital letter and five digits.")
