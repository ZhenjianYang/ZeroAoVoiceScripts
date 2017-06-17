import codecs
import struct, os

code_name = 'cn_psp_sjis'
sjis2ucs = [0] * 0x10000
ucs2sjis = [0] * 0x10000


def jis2sjis(jis):
    sjis = jis

    if sjis >= 0x100:
        jis_h = jis >> 8
        jis_l = jis & 0xFF

        jis_h -= 0x21

        jis_l += 0x7E if jis_h & 1 else 0x1F
        jis_l += 1 if 0x7F <= jis_l <= 0x9D else 0

        jis_h >>= 1
        jis_h += 0x81 if jis_h <= 0x1E else 0xC1

        sjis = jis_h << 8 | jis_l

    return  sjis

def init_map():
    dir_py = os.path.split(os.path.realpath(__file__))[0]

    path = dir_py + '/jis2ucs.bin'
    file = open(path, 'rb')
    for jis in range(len(sjis2ucs)):
        short = file.read(2)
        if not short:
            break
        ucs, = struct.unpack('<H', short)
        if ucs != 0:
            sjis = jis2sjis(jis)
            sjis2ucs[sjis] = ucs
    file.close()

    path = dir_py + '/ucs2jis.bin'
    file = open(path, 'rb')
    for ucs in range(len(sjis2ucs)):
        short = file.read(2)
        if not short:
            break
        jis, = struct.unpack('<H', short)
        if jis != 0:
            sjis = jis2sjis(jis)
            ucs2sjis[ucs] = sjis
    file.close()


init_map()


class Codec(codecs.Codec):
    def encode(self, ucs_str, errors='strict'):
        output = bytearray()

        for i in range(len(ucs_str)):
            c = ucs_str[i]
            if c == '¤':
                c = '♪'
            elif c == '⊥':
                c = '㈱'
            sjis = ucs2sjis[ord(c)]

            if sjis == 0 and ord(c) != 0:
                raise UnicodeEncodeError(code_name, ucs_str, i, i+1, 'No mapping sjis found')

            if sjis >= 0x100:
                output.append(sjis >> 8)
            output.append(sjis & 0xFF)

        return bytes(output), len(output)

    def decode(self, byte_array, errors='strict'):
        output = []
        i = 0
        while i < len(byte_array):
            j = i
            sjis = byte_array[i]
            i += 1
            if 0x81 <= sjis <= 0x9F or 0xE0 <= sjis:
                sjis *= 0x100
                sjis += byte_array[i]
                i += 1

            ucs = sjis2ucs[sjis]
            if ucs == 0 and sjis != 0:
                raise UnicodeDecodeError(code_name, byte_array, j, j+1, 'No mapping ucs found')

            output.append(chr(ucs))

        return ''.join(output), len(output)


def search_function(codec_name):
    if codec_name == code_name:
        return getregentry()
    else:
        return None


def getregentry():
    return codecs.CodecInfo(
        name=code_name,
        encode=Codec().encode,
        decode=Codec().decode,
    )


def search_function(codec_name):
    if codec_name == code_name:
        return getregentry()
    else:
        return None


def register():
    codecs.register(search_function)


def get_name():
    return code_name
