# If input is int
def digits_counter(number_to_cnt_digs, cnt=0):
    if number_to_cnt_digs == 0:
        return cnt
    else:
        return digits_counter(number_to_cnt_digs // 10, cnt + 1)

# Also use
# return len(str(number_to_cnt_digs))
