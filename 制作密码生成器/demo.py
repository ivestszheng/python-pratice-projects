import random

def get_upper():
    '''
    生成大写字母
    :return:
    '''
    count = random.randint(1, 3)
    return random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=count)

def get_special_char():
    '''
    生成特殊符号
    :return:
    '''
    count = random.randint(1,3)
    return random.choices('!@$%^&*()_+~', k=count)

def get_lower(count):
    '''
    生成小写字母和数字
    :param count:
    :return:
    '''
    string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return random.choices(string, k=count)

def generate_password(length):
    '''
    生成指定长度的密码
    :param length:
    :return:
    '''

    if length < 6:
        length = 6

    lst = []
    upper_lst = get_upper()     # 大写
    special_char = get_special_char()      # 特殊字符
    lst.extend(upper_lst)
    lst.extend(special_char)

    surplus_count = length - len(lst)
    lower_lst = get_lower(surplus_count)
    lst.extend(lower_lst)
    # 将顺序打乱
    random.shuffle(lst)
    return ''.join(lst)


if __name__ == '__main__':
    print(generate_password(8))
    print(generate_password(5))
    print(generate_password(12))