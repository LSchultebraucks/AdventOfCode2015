import hashlib

secret_key = 'yzbqklnj'

five_zeroes_hash_number = None
six_zeroes_hash_number = None

for i in range(10000000):
    msg = str(secret_key + str(i)).encode('utf-8')
    if hashlib.md5(msg).hexdigest()[:5] == '00000' and five_zeroes_hash_number is None:
        five_zeroes_hash_number = i
    if hashlib.md5(msg).hexdigest()[:6] == '000000' and six_zeroes_hash_number is None:
        six_zeroes_hash_number = i
    if five_zeroes_hash_number and six_zeroes_hash_number:
        break


print('Part one: {0}, Part two: {1}'.format(five_zeroes_hash_number, six_zeroes_hash_number))
