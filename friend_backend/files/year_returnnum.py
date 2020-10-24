import re
from ctypes import *
import struct


class Year(object):

    def __init__(self):
        self.dll = cdll.LoadLibrary("../files/c_files/test.dll")
        self.dll.main.restype = c_int
        self.dll.main.argtypes = [c_int, POINTER(c_char_p)]

    def __predict(self, result):
        predict_result = ""
        hex_result = '{:08x}'.format(result)
        str_result = str(hex_result)

        return str_result

    @staticmethod
    def get_key_data(message):
        tmp_result = message.split(' ')
        date = tmp_result[0]
        sex = tmp_result[1]

        predict = tmp_result[2]
        number_date = re.split(r'(\D+)', date)
        y = number_date[0]
        m = number_date[2]
        d = number_date[4]
        t = number_date[6]
        s = "0"
        # predict = number_predict[2]
        # print(y, m, d, t, s, actual_sex, predict)
        return y, m, d, t, s, sex, predict

    def result(self, msg):
        y, m, d, t, s, sex, predict = self.get_key_data(msg)

        args = [
            bytes("", encoding="utf-8"),
            bytes(y, encoding="utf-8"),
            bytes(m, encoding="utf-8"),
            bytes(d, encoding="utf-8"),
            bytes(t, encoding="utf-8"),
            bytes(s, encoding="utf-8"),
            bytes(sex, encoding="utf-8"),
            bytes(predict, encoding="utf-8")
        ]

        ArrayType = c_char_p * len(args)
        args_array = ArrayType(*args)
        result = self.dll.main(len(args_array), args_array)
        predict_result = self.__predict(result)
        return str(predict_result)

    def __del__(self):
        pass

if __name__ == "__main__":
    dll = Year()
    result = dll.result("1988-8-6-9 0 2018")
    print(result)
