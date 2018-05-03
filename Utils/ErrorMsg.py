class ErrorMsg():
    def errormsg_invalid_permission(self, field_name='auth_token'):
        return "'%s' in header does not have write permissions" % field_name

    def msg_invalid_range(self, key_name, key_value):

        if str(key_name).lower() == 'daily_price':
            spl_char = '='
        else:
            spl_char = ''
        return "Key '%s' must have a value >%s 0 and <= 500, got value %s" % (
            key_name, spl_char, key_value)

    def msg_invalid_type_int(self, key_name, key_value):
        return "Expected key '%s' having non-empty string/unicode value, got type <type 'int'> with value %s" % (
            key_name, key_value)

    def msg_invalid_type_unicode(self, key_name, key_value):
        if str(key_name).lower() in ('power_rating', 'daily_price'):
            expected_data_type = 'integer'
        else:
            expected_data_type = 'string/unicode'

        return "Expected key '%s' having non-empty %s value, got type <type 'unicode'> with value %s" % (
            key_name, expected_data_type, key_value)

    def msg_missing_wrong_input_data(self):
        return "Bad Request: Missing/Wrong Input data"
