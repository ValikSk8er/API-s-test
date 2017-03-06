import random


def candidate_name():
        return 'Name_' + str(random.randint(1000, 9999))


def candidate_position():
        return 'Position_' + str(random.randint(1000, 9999))

candidate_data = [
    ['valid_name_and_position', candidate_name(), candidate_position()],
    ['absent_name', '', candidate_position()],
    ['absent_position', candidate_name(), ''],
    ['absent_name_and_position', '', '']
]

symbols_for_candidates_name_or_position = ['~', '`', '!', '@', '#', '$', '%', '^', '&',
                                           '*', '()', ',', '?', '|', '/', '\\', '+', '-',
                                           '_', '[]', '{}', '<>', '\'', '\"',  '=']

candidates_keys = [candidate[0] for candidate in candidate_data]

invalid_ides = [0, ' ', '21.1', '(21)', '[21]', '{21}', '<21>', '21a', '21~', '21\'', '21`',
                '!21', '@21', '#21', '$21', '%21', '2^1', '2&1', '21/', '21\\', '21*1',
                '2,1', '21?12', '21|', '2+1', '2-1', '2_1',  '2\'1', '2\"1',  '=21']

invalid_headers = {
    'invalid_type': ['content-', 'application/json'],
    'invalid_format': ['content-type', 'applic'],
    'absent_format': ['content-type', '']
}


