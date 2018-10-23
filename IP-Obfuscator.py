#!/usr/bin/env python3
import argparse
import re

NAME, AUTHOR, VERSION = \
    'IP Obfuscator  ', 'Author: Omer Ramić <@sp_omer>', '0.1f'


def obscure_ip(ip):
    for match in re.finditer(r'((?P<a>\d+)\.)((?P<b>\d+)\.)((?P<c>\d+)\.)'
                             '(?P<d>\d+)', ip):
        print(str(int(match.group('a'))*256**3 +
                                int(match.group('b'))*256**2 +
                                int(match.group('c'))*256 +
                                int(match.group('d'))))
        print(str(hex(int(match.group('a'))*256**3 +
                                int(match.group('b'))*256**2 +
                                int(match.group('c'))*256 +
                                int(match.group('d')))))
        print(re.sub('o', '', str(oct(int(match.group('a')) *
                                   256**3+int(match.group('b'))*256**2 +
                                   int(match.group('c'))*256 +
                                   int(match.group('d'))))))
        print(re.sub('o', '', str(oct(int(match.group('a')))) +
                                   '.'+str(oct(int(match.group('b'))))+'.' +
                                   str(oct(int(match.group('c'))))+'.' +
                                   str(oct(int(match.group('d'))))))
        print(re.sub('o', '0000000',
                                   str(oct(int(match.group('a'))))+'.' +
                                   str(oct(int(match.group('b'))))+'.' +
                                   str(oct(int(match.group('c'))))+'.' +
                                   str(oct(int(match.group('d'))))))
        print(str(hex(int(match.group('a'))))+'.' +
              str(hex(int(match.group('b'))))+'.' +
              str(hex(int(match.group('c'))))+'.' +
              str(hex(int(match.group('d')))))
        print(re.sub('x', 'x00000000',
              str(hex(int(match.group('a'))))+'.' +
              str(hex(int(match.group('b'))))+'.' +
              str(hex(int(match.group('c'))))+'.' +
              str(hex(int(match.group('d'))))))
        print(str(hex(int(match.group('a'))))+'.' +
              str(hex(int(match.group('b'))))+'.' +
              str(hex(int(match.group('c'))))+'.'+match.group('d'))
        print(str(hex(int(match.group('a'))))+'.' +
              str(hex(int(match.group('b'))))+'.' +
              match.group('c')+'.'+match.group('d'))
        print(str(hex(int(match.group('a'))))+'.' +
              match.group('b')+'.'+match.group('c')+'.'+match.group('d'))
        print(match.group('a')+'.' +
              str(hex(int(match.group('b'))))+'.' +
              str(hex(int(match.group('c'))))+'.' +
              str(hex(int(match.group('d')))))
        print(match.group('a')+'.'+match.group('b')+'.' +
              str(hex(int(match.group('c'))))+'.' +
              str(hex(int(match.group('d')))))
        print(match.group('a')+'.'+match.group('b')+'.' +
              match.group('c')+'.'+str(hex(int(match.group('d')))))
        print(re.sub('o', '', str(oct(int(match.group('a')))) +
              '.'+str(oct(int(match.group('b'))))+'.' +
              str(oct(int(match.group('c'))))+'.'+match.group('d')))
        print(re.sub('o', '', str(oct(int(match.group('a')))) +
              '.'+str(oct(int(match.group('b'))))+'.' +
              match.group('c')+'.'+match.group('d')))
        print(re.sub('o', '', str(oct(int(match.group('a')))) +
              '.'+match.group('b')+'.'+match.group('c')+'.'+match.group('d')))
        print(re.sub('o', '', match.group('a')+'.' +
              str(oct(int(match.group('b'))))+'.' +
              str(oct(int(match.group('c'))))+'.' +
              str(oct(int(match.group('d'))))))
        print(re.sub('o', '', match.group('a')+'.' +
              match.group('b')+'.'+str(oct(int(match.group('c'))))+'.' +
              str(oct(int(match.group('d'))))))
        print(re.sub('o', '', match.group('a')+'.' +
              match.group('b')+'.'+match.group('c')+'.' +
              str(oct(int(match.group('d'))))))
        print(str(hex(int(match.group('a'))))+'.' +
              str(hex(int(match.group('b'))))+'.'+str(int(match.group('c')) *
              256+int(match.group('d'))))
        print(str(hex(int(match.group('a'))))+'.' +
              str(int(match.group('b'))*256**2+int(match.group('c'))*256 +
              int(match.group('d'))))
        print(re.sub('o', '', str(oct(int(match.group('a')))) +
              '.'+str(oct(int(match.group('b')))))+'.' +
              str(int(match.group('c'))*256+int(match.group('d'))))
        print(re.sub('o', '', str(oct(int(match.group('a'))))) +
              '.'+str(int(match.group('b'))*256**2+int(match.group('c'))*256 +
                      int(match.group('d'))))
        print(str(hex(int(match.group('a'))))+'.' +
              re.sub('o', '', str(oct(int(match.group('b')))))+'.' +
              str(int(match.group('c'))*256+int(match.group('d'))))
        print(re.sub('o', '', str(oct(int(match.group('a'))))) +
              '.'+str(hex(int(match.group('b'))))+'.' +
              str(int(match.group('c'))*256+int(match.group('d'))))

       # print('IPv4 mapping into IPv6 - not resolving as IPv4 do')
        print('::ffff:'+str(hex(int(match.group('a'))*256**3 +
              int(match.group('b'))*256**2+int(match.group('c'))*256 +
              int(match.group('d'))))[2:])
        print('0:0:0:0:0:ffff:'+str(hex(int(match.group('a')) *
              256**3+int(match.group('b'))*256**2+int(match.group('c'))*256 +
              int(match.group('d'))))[2:])
        print('0000:0000:0000:0000:0000:ffff:' +
              str(hex(int(match.group('a'))*256**3+int(match.group('b'))*256 **
                  2+int(match.group('c'))*256+int(match.group('d'))))[2:])
        print('0000:0000:0000:0000:0000:ffff:'+ip)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=NAME+VERSION, epilog=AUTHOR)
    parser.add_argument('--ip',
                        dest='ip',
                        help='Targeted IP (e.g. \'127.0.0.1\')')
    args = parser.parse_args()
    if args.ip:
        obscure_ip(args.ip)
    else:
        parser.print_help()
