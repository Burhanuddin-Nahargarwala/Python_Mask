def mask_number(phn_no):
    last_3_digits = phn_no[7:]
    mask_string = 7 * "X"
    masked_num = mask_string + last_3_digits
    return masked_num

phn_no = "8876543221"
masked_num = mask_number(phn_no)

print(masked_num)
