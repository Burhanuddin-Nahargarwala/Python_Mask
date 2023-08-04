def mask_name(name):
    first_name = name.split()[0]
    last_name = name.split()[1]
    masked_first_name = first_name[0] + "X" * (len(first_name) - 2) + first_name[-1]
    masked_last_name = last_name[0] + "X" * (len(last_name) - 2) + last_name[-1]
    masked_full_name = masked_first_name + " " + masked_last_name
    return masked_full_name

name = "Stanley Richards"
masked_name = mask_name(name)

print("Shyam")

print(masked_name)
