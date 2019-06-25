#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class XBMGenerator:
    def __init__(self, invert=True):
        self.invert = invert

        self.input_filepath = '../data/test.csv'
        self.input = []

        self.xbm_hex_array = []

        self.output = []
        self.output_filepath = '../data/test.xbm'

    def read_array(self):
        with open(self.input_filepath, 'r') as f:
            self.input = f.read().splitlines()

    def create_xbm(self):
        xbm_width = len(self.input[0].split(','))
        xbm_height = len(self.input)

        self.output.append(f"#define test_width {xbm_width}")
        self.output.append(f"#define test_height {xbm_height}")
        self.output.append('static char test_bits[] = {')

        for line in self.input:
            line_array = line.split(',')
            if self.invert is True:
                line_array = [str(int(bit)^1) for bit in line_array]
            byte_array = []
            for i, bit in enumerate(line_array, start=1):
                byte_array.append(bit)
                if i % 8 == 0:
                    byte_array = ''.join(reversed(byte_array))
                    hex_value = hex(int(byte_array, 2))
                    self.xbm_hex_array.append(hex_value)
                    byte_array = []

        self.output.append(', '.join(self.xbm_hex_array))
        self.output.append('};')

    def write_xbm(self):
        with open(self.output_filepath, 'w', encoding='ascii') as xbm_file:
            xbm_file.write('\n'.join(self.output))

    def debug_print(self):
        print(*self.input, sep="\n")
        print(*self.output, sep="\n")
        print(f"Total length: {len(self.xbm_hex_array)}")


if __name__ == '__main__':
    xbm_generator = XBMGenerator(invert=True)
    xbm_generator.read_array()
    xbm_generator.create_xbm()
    xbm_generator.write_xbm()
    xbm_generator.debug_print()
