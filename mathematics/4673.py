if __name__ == "__main__":

    self_list = []

    for num in range(1, 10001):
        num_s = str(num)
        number = num
        for i in range(len(num_s)):
            number += int(num_s[i])

        if number <= 10000:
            self_list.append(number)

    self_list.sort()
    self_list = set(self_list)

    self_list = list(self_list)
    idx = 0
    for i in range(1, 10001):
        if self_list[idx] == i:
            idx += 1
        else:
            print(i)

