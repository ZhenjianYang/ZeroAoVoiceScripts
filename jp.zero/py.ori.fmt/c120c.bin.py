from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c120c.bin",                # FileName
        "c120c",                    # MapName
        "c120c",                    # Location
        0x001A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 26, 0, 10, 0, 11],
    )

    BuildStringList((
        "c120c",                  # 0
        "クーニャ",               # 1
        "オーゼル",               # 2
        "ビショップ",             # 3
        "クワイン老人",           # 4
        "アミサ",                 # 5
        "グレイス",               # 6
        "レインズ",               # 7
        "水上バスガイド",         # 8
        "ミスラ",                 # 9
        "ヤーチー",               # 10
        "ミサ",                   # 11
        "商工会役員",             # 12
        "進行役",                 # 13
        "商工会係員",             # 14
        "ロイ",                   # 15
        "ロイ",                   # 16
        "メイリン",               # 17
        "メイリン",               # 18
        "モルス会長",             # 19
        "パーラ夫人",             # 20
        "モモ",                   # 21
        "エルサ",                 # 22
        "エマ捜査官",             # 23
        "アントン",               # 24
        "リックス",               # 25
        "見物客",                 # 26
        "男の子",                 # 27
        "見物客",                 # 28
        "見物客",                 # 29
        "見物客",                 # 30
        "見物客",                 # 31
        "女の子",                 # 32
        "見物客",                 # 33
        "見物客",                 # 34
        "アレサ",                 # 35
        "ステファン",             # 36
        "大道芸人",               # 37
        "歌手",                   # 38
        "ヴァルド",               # 39
        "ルガノフ",               # 40
        "ジェド",                 # 41
        "ヒューイ",               # 42
        "スラッシュ",             # 43
        "キリカ",                 # 44
        "レクター",               # 45
        "水上バス",               # 46
        "エステル",               # 47
        "ヨシュア",               # 48
        "ワジ",                   # 49
        "アッバス",               # 50
        "テスタメンツの青年",     # 51
        "テスタメンツの青年",     # 52
        "テスタメンツの青年",     # 53
        "テスタメンツの青年",     # 54
        "テスタメンツの青年",     # 55
        "バイパーの青年",         # 56
        "バイパーの青年",         # 57
        "バイパーの青年",         # 58
        "バイパーの青年",         # 59
        "バイパーの青年",         # 60
        "客",                     # 61
        "客",                     # 62
        "客",                     # 63
        "客",                     # 64
        "客",                     # 65
        "客",                     # 66
        "客",                     # 67
        "客",                     # 68
        "客",                     # 69
        "客",                     # 70
        "青年",                   # 71
        "青年",                   # 72
        "警官",                   # 73
        "警官",                   # 74
        "ツァイト",               # 75
        "SE制御",                 # 76
        "中央広場",               # 77
        "西通り",                 # 78
        "行政区",                 # 79
        "住宅街",                 # 80
        "歓楽街",                 # 81
        "東通り",                 # 82
        "旧市街",                 # 83
        "港湾区",                 # 84
        "ＩＢＣ",                 # 85
        "駅前通り",               # 86
        "裏通り",                 # 87
        "ウルスラ間道",           # 88
        "東クロスベル街道",       # 89
        "西クロスベル街道",       # 90
        "マインツ山道",           # 91
    ))

    AddCharChip((
        "chr/ch22100.itc",                   # 00
        "chr/ch25200.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "apl/ch50168.itc",                   # 03
        "chr/ch21500.itc",                   # 04
        "chr/ch28100.itc",                   # 05
        "chr/ch06000.itc",                   # 06
        "chr/ch34600.itc",                   # 07
        "chr/ch27000.itc",                   # 08
        "chr/ch21200.itc",                   # 09
        "chr/ch22800.itc",                   # 0A
        "chr/ch23200.itc",                   # 0B
        "chr/ch27600.itc",                   # 0C
        "chr/ch27602.itc",                   # 0D
        "chr/ch32200.itc",                   # 0E
        "chr/ch32500.itc",                   # 0F
        "chr/ch24200.itc",                   # 10
        "chr/ch24600.itc",                   # 11
        "chr/ch22000.itc",                   # 12
        "chr/ch21000.itc",                   # 13
        "chr/ch24500.itc",                   # 14
        "chr/ch21900.itc",                   # 15
        "chr/ch23900.itc",                   # 16
        "chr/ch21300.itc",                   # 17
        "chr/ch20300.itc",                   # 18
        "chr/ch20600.itc",                   # 19
        "chr/ch20800.itc",                   # 1A
        "chr/ch20900.itc",                   # 1B
        "chr/ch21202.itc",                   # 1C
        "chr/ch21502.itc",                   # 1D
        "chr/ch20700.itc",                   # 1E
        "chr/ch30500.itc",                   # 1F
        "chr/ch37300.itc",                   # 20
        "chr/ch37400.itc",                   # 21
        "chr/ch02100.itc",                   # 22
        "chr/ch30800.itc",                   # 23
        "chr/ch31700.itc",                   # 24
        "chr/ch10400.itc",                   # 25
        "chr/ch27100.itc",                   # 26
    ))

    DeclNpc(-3519,   0,       8720,    90,   257,  0x0, 0,   0,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-10470,  0,       13340,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52470,  2000,    21149,   90,   257,  0x0, 0,   2,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(39669,   -2500,   -19379,  180,  277,  0x0, 0,   3,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(38439,   -2490,   -18079,  135,  261,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(180,     -680,    4130,    135,  389,  0x0, 0,   6,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1590,    -699,    3920,    135,  389,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(42450,   -2500,   2329,    235,  261,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(15300,   0,       12979,   180,  261,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(19780,   0,       -3299,   270,  261,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(19780,   0,       -6090,   270,  261,  0x0, 0,   38,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-16500,  0,       -9050,   180,  277,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(5539,    -699,    1009,    270,  261,  0x0, 0,   5,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-15890,  0,       -6059,   225,  261,  0x0, 0,   13,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(-17450,  0,       -9449,   135,  405,  0x0, 0,   9,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-15890,  0,       -6059,   225,  469,  0x0, 0,   28,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-18590,  0,       -699,    225,  389,  0x0, 0,   4,   0,   0,   3,   0,   31,  255,  0)
    DeclNpc(-14390,  0,       -7840,   225,  469,  0x0, 0,   29,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-16149,  0,       -10960,  0,    277,  0x0, 0,   26,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(-17540,  0,       -11369,  45,   405,  0x0, 0,   27,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(21450,   0,       3299,    0,    389,  0x0, 0,   30,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(21450,   0,       4690,    180,  389,  0x0, 0,   37,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(-17799,  0,       13369,   180,  389,  0x0, 0,   31,  0,   0,   0,   0,   46,  255,  0)
    DeclNpc(-5380,   2000,    20700,   180,  261,  0x0, 0,   32,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(-6130,   2000,    22040,   180,  261,  0x0, 0,   33,  0,   0,   0,   0,   48,  255,  0)
    DeclNpc(-7289,   -9,      -8520,   270,  261,  0x0, 0,   16,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(-9149,   -9,      -8520,   90,   261,  0x0, 0,   17,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(-17909,  0,       920,     45,   261,  0x0, 0,   18,  0,   0,   9,   0,   37,  255,  0)
    DeclNpc(829,     -699,    1980,    90,   261,  0x0, 0,   19,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(300,     -699,    -1679,   90,   261,  0x0, 0,   20,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(1169,    -699,    -3099,   45,   261,  0x0, 0,   21,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(1870,    -699,    -3809,   45,   261,  0x0, 0,   22,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(40790,   -2500,   -1309,   315,  389,  0x0, 0,   23,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(40000,   -2500,   0,       135,  389,  0x0, 0,   9,   0,   0,   0,   0,   43,  255,  0)
    DeclNpc(27329,   0,       12109,   90,   389,  0x0, 0,   24,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(27329,   0,       10479,   90,   389,  0x0, 0,   25,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(8250,    100,     79,      270,  453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(8250,    100,     79,      270,  453,  0x0, 0,   15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(150,     0,       -9970,   180,  389,  0x0, 0,   34,  0,   0,   0,   0,   50,  255,  0)
    DeclNpc(-1929,   0,       -10229,  270,  389,  0x0, 0,   35,  0,   0,   0,   0,   51,  255,  0)
    DeclNpc(330,     0,       -11890,  0,    389,  0x0, 0,   36,  0,   0,   0,   0,   52,  255,  0)
    DeclNpc(-1399,   0,       -11710,  45,   405,  0x0, 0,   36,  0,   0,   0,   0,   54,  255,  0)
    DeclNpc(1450,    0,       -11210,  90,   405,  0x0, 0,   35,  0,   0,   0,   0,   55,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 58,  33.0,                  0.0,                   -3.5,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.0,                 -0.0,                  0.699999988079071,     1.0])
    DeclEvent(0x0000, 0, 65,  -10.0,                 22.5,                  1.0,                   225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.3333334922790527,    -2.25,                 -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 66,  -20.0,                 -17.0,                 -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.0,                   5.6666669845581055,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 65,  -14.5,                 18.0,                  0.0,                   56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.9000000953674316,    -6.0,                  -0.0,                  1.0])

    DeclActor(19200,   250,     20500,   2000,    19200,   1250,    20500,   0x007C, 0,  86, 0x0000)
    DeclActor(68620,   -2500,   15400,   1200,    68040,   -3500,   11820,   0x007C, 0,  56, 0x0000)
    DeclActor(34000,   -2500,   3400,    1500,    34000,   -1500,   3400,    0x007C, 0,  57, 0x0000)
    DeclActor(77440,   -2500,   19770,   1200,    77440,   -1000,   19770,   0x007C, 0,  85, 0x0000)
    DeclActor(-16630,  0,       -6860,   1200,    -15890,  1500,    -6060,   0x007E, 0,  25, 0x0000)
    DeclActor(-14890,  0,       -8480,   1200,    -14390,  1200,    -7840,   0x007E, 0,  32, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "中央広場")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "西通り")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "住宅街")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "歓楽街")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "東通り")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "旧市街")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "駅前通り")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "裏通り")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_F78",          # 00, 0
        "Function_1_1030",         # 01, 1
        "Function_2_10A5",         # 02, 2
        "Function_3_11DF",         # 03, 3
        "Function_4_120A",         # 04, 4
        "Function_5_1235",         # 05, 5
        "Function_6_12D2",         # 06, 6
        "Function_7_12FD",         # 07, 7
        "Function_8_137A",         # 08, 8
        "Function_9_13A0",         # 09, 9
        "Function_10_13CB",        # 0A, 10
        "Function_11_1D94",        # 0B, 11
        "Function_12_2021",        # 0C, 12
        "Function_13_2318",        # 0D, 13
        "Function_14_29A9",        # 0E, 14
        "Function_15_2CA7",        # 0F, 15
        "Function_16_2F24",        # 10, 16
        "Function_17_31A6",        # 11, 17
        "Function_18_31F6",        # 12, 18
        "Function_19_34EC",        # 13, 19
        "Function_20_3731",        # 14, 20
        "Function_21_3F59",        # 15, 21
        "Function_22_45AD",        # 16, 22
        "Function_23_4B5B",        # 17, 23
        "Function_24_5121",        # 18, 24
        "Function_25_5614",        # 19, 25
        "Function_26_5629",        # 1A, 26
        "Function_27_5E3D",        # 1B, 27
        "Function_28_5EEF",        # 1C, 28
        "Function_29_5F79",        # 1D, 29
        "Function_30_62BC",        # 1E, 30
        "Function_31_6794",        # 1F, 31
        "Function_32_67C7",        # 20, 32
        "Function_33_6BDA",        # 21, 33
        "Function_34_773F",        # 22, 34
        "Function_35_77CD",        # 23, 35
        "Function_36_79A2",        # 24, 36
        "Function_37_7AEA",        # 25, 37
        "Function_38_7CDA",        # 26, 38
        "Function_39_7EE8",        # 27, 39
        "Function_40_8045",        # 28, 40
        "Function_41_81C6",        # 29, 41
        "Function_42_836F",        # 2A, 42
        "Function_43_83D3",        # 2B, 43
        "Function_44_8442",        # 2C, 44
        "Function_45_8553",        # 2D, 45
        "Function_46_871E",        # 2E, 46
        "Function_47_8C5F",        # 2F, 47
        "Function_48_92AD",        # 30, 48
        "Function_49_97A6",        # 31, 49
        "Function_50_98E1",        # 32, 50
        "Function_51_9B75",        # 33, 51
        "Function_52_9C74",        # 34, 52
        "Function_53_9D28",        # 35, 53
        "Function_54_9E16",        # 36, 54
        "Function_55_9F42",        # 37, 55
        "Function_56_A014",        # 38, 56
        "Function_57_A0E8",        # 39, 57
        "Function_58_A7DB",        # 3A, 58
        "Function_59_B0E0",        # 3B, 59
        "Function_60_CDE3",        # 3C, 60
        "Function_61_CE12",        # 3D, 61
        "Function_62_CE64",        # 3E, 62
        "Function_63_CEB6",        # 3F, 63
        "Function_64_CF03",        # 40, 64
        "Function_65_CF95",        # 41, 65
        "Function_66_D0A9",        # 42, 66
        "Function_67_D1BD",        # 43, 67
        "Function_68_D201",        # 44, 68
        "Function_69_D231",        # 45, 69
        "Function_70_D275",        # 46, 70
        "Function_71_D2A5",        # 47, 71
        "Function_72_D4C0",        # 48, 72
        "Function_73_FF02",        # 49, 73
        "Function_74_FF87",        # 4A, 74
        "Function_75_1031E",       # 4B, 75
        "Function_76_10D7D",       # 4C, 76
        "Function_77_1135C",       # 4D, 77
        "Function_78_13433",       # 4E, 78
        "Function_79_14777",       # 4F, 79
        "Function_80_1487B",       # 50, 80
        "Function_81_14897",       # 51, 81
        "Function_82_148BA",       # 52, 82
        "Function_83_14E3C",       # 53, 83
        "Function_84_1541F",       # 54, 84
        "Function_85_15445",       # 55, 85
        "Function_86_154D5",       # 56, 86
    ))


    def Function_0_F78(): pass

    label("Function_0_F78")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_FB8"),
        (1, "loc_FC4"),
        (2, "loc_FD0"),
        (3, "loc_FDC"),
        (4, "loc_FE8"),
        (5, "loc_FF4"),
        (6, "loc_1000"),
        (SWITCH_DEFAULT, "loc_100C"),
    )


    label("loc_FB8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FC4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FD0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FDC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FE8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FF4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_1000")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_100C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_1018")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_102F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_102F")

    Return()

    # Function_0_F78 end

    def Function_1_1030(): pass

    label("Function_1_1030")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10A4")
    OP_95(0xFE, 17490, 0, 8720, 1000, 0x0)
    OP_95(0xFE, 17490, 0, -4030, 1000, 0x0)
    OP_95(0xFE, 12440, 0, -8720, 1000, 0x0)
    OP_95(0xFE, -3520, 0, -8720, 1000, 0x0)
    OP_95(0xFE, -3520, 0, 8720, 1000, 0x0)
    Jump("Function_1_1030")

    label("loc_10A4")

    Return()

    # Function_1_1030 end

    def Function_2_10A5(): pass

    label("Function_2_10A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11DE")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 10000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 8000, 0x0)
    Jump("Function_2_10A5")

    label("loc_11DE")

    Return()

    # Function_2_10A5 end

    def Function_3_11DF(): pass

    label("Function_3_11DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1209")
    OP_94(0xFE, 0xFFFFB9BA, 0x992, 0xFFFFB118, 0xFFFFF628, 0x3E8)
    Sleep(300)
    Jump("Function_3_11DF")

    label("loc_1209")

    Return()

    # Function_3_11DF end

    def Function_4_120A(): pass

    label("Function_4_120A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1234")
    OP_94(0xFE, 0xA5FA, 0xFFFFCAA4, 0x965A, 0xFFFFB73A, 0x320)
    Sleep(700)
    Jump("Function_4_120A")

    label("loc_1234")

    Return()

    # Function_4_120A end

    def Function_5_1235(): pass

    label("Function_5_1235")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12D1")
    OP_95(0xFE, -17830, 0, -4570, 1000, 0x0)
    OP_95(0xFE, -13440, 0, -9920, 1000, 0x0)
    OP_95(0xFE, 12710, 0, -9920, 1000, 0x0)
    OP_95(0xFE, 18920, 0, -4320, 1000, 0x0)
    OP_95(0xFE, 18920, 0, 9980, 1000, 0x0)
    OP_95(0xFE, -13010, 0, 9980, 1000, 0x0)
    OP_95(0xFE, -17820, 0, 4570, 1000, 0x0)
    Jump("Function_5_1235")

    label("loc_12D1")

    Return()

    # Function_5_1235 end

    def Function_6_12D2(): pass

    label("Function_6_12D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FC")
    OP_94(0xFE, 0x1F22, 0x546, 0x7D9, 0xFFFFF7FE, 0x3E8)
    Sleep(300)
    Jump("Function_6_12D2")

    label("loc_12FC")

    Return()

    # Function_6_12D2 end

    def Function_7_12FD(): pass

    label("Function_7_12FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1379")
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(6000)
    Jump("Function_7_12FD")

    label("loc_1379")

    Return()

    # Function_7_12FD end

    def Function_8_137A(): pass

    label("Function_8_137A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_139F")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    Jump("Function_8_137A")

    label("loc_139F")

    Return()

    # Function_8_137A end

    def Function_9_13A0(): pass

    label("Function_9_13A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13CA")
    OP_94(0xFE, 0xFFFFB46A, 0x730, 0xFFFFBE92, 0xFFFFFD08, 0x3E8)
    Sleep(300)
    Jump("Function_9_13A0")

    label("loc_13CA")

    Return()

    # Function_9_13A0 end

    def Function_10_13CB(): pass

    label("Function_10_13CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FD")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148D")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1460")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_147F")

    label("loc_1460")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_147F")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_147F")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15FD")

    label("loc_148D")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_155C")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152F")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_154E")

    label("loc_152F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154E")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_154E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15FD")

    label("loc_155C")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D5")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_15F4")

    label("loc_15D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F4")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_15F4")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15FD")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16B3")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x13, 1230, -690, 3680, 135)
    ClearChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x15, -18840, 0, -5150, 180)
    SetChrChipByIndex(0x15, 0xC)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 0, 0, 0)
    ClearChrFlags(0x15, 0x10)
    SetChrPos(0x21, 37750, -2500, 1640, 90)
    SetChrPos(0x22, 37750, -2500, 240, 90)
    SetChrFlags(0x25, 0x10)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x1A, 7780, 100, -80, 270)
    Jump("loc_1D34")

    label("loc_16B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1822")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x14, 0x0, 0x0)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x13, -10690, 0, -9230, 45)
    SetChrPos(0x21, 5840, 2000, 22000, 315)
    SetChrFlags(0x21, 0x10)
    SetChrPos(0x22, 5840, 2000, 23400, 270)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x24, 0x10)
    SetChrFlags(0x26, 0x10)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x1A, 1470, -700, 1200, 90)
    SetChrPos(0x2E, 4490, 2000, 23330, 90)
    SetChrPos(0x2F, 6200, -260, 2760, 135)
    SetChrPos(0x30, 4150, -700, 980, 90)
    SetChrPos(0x31, 3660, -700, -1420, 225)
    SetChrPos(0x32, 4330, 2000, 21140, 45)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2F, 0x10)
    SetChrFlags(0x30, 0x10)
    ClearChrFlags(0x31, 0x10)
    ClearChrFlags(0x32, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FB")
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x13, -17390, 0, -9830, 135)
    ClearChrFlags(0x13, 0x10)

    label("loc_17FB")

    SetChrPos(0x1F, -15840, 0, 5890, 270)
    SetChrPos(0x20, -14160, -10, 7230, 135)
    Jump("loc_1D34")

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19D5")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x2D, 0x80)
    BeginChrThread(0x2D, 0, 0, 8)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    SetChrChipByIndex(0x15, 0xC)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C2")
    SetChrFlags(0x15, 0x10)
    Jump("loc_18C7")

    label("loc_18C2")

    ClearChrFlags(0x1A, 0x10)

    label("loc_18C7")

    SetChrPos(0x21, 5840, 2000, 22000, 0)
    SetChrPos(0x22, 5840, 2000, 23400, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_193C")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x10)
    SetChrPos(0x16, 17000, 0, -8570, 45)
    SetChrPos(0x13, 15160, 0, -9180, 315)
    Jump("loc_19A4")

    label("loc_193C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198A")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    Jump("loc_19A4")

    label("loc_198A")

    ClearChrFlags(0x17, 0x80)
    SetChrSubChip(0x17, 0x2)
    SetChrPos(0x13, -18110, 0, -5400, 135)

    label("loc_19A4")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x1F, -15840, 0, 5890, 270)
    SetChrPos(0x20, -14160, -10, 7230, 270)
    Jump("loc_1D34")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A91")
    ClearChrFlags(0x2C, 0x80)
    BeginChrThread(0x2C, 0, 0, 7)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x21, 12500, 0, 11930, 0)
    SetChrPos(0x22, 10900, 0, 11720, 90)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x25, 0x10)
    OP_93(0x27, 0x13B, 0x0)
    SetChrFlags(0x27, 0x10)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x1A, -16250, 0, -10660, 315)
    SetChrPos(0x13, -19060, 0, -5540, 0)
    SetChrPos(0x23, -14280, 0, 7050, 315)
    BeginChrThread(0x23, 0, 0, 0)
    Jump("loc_1D34")

    label("loc_1A91")

    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1D34")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrFlags(0x2F, 0x80)
    SetChrBattleFlags(0x2F, 0x8000)
    SetChrFlags(0x30, 0x80)
    SetChrBattleFlags(0x30, 0x8000)
    SetChrFlags(0x31, 0x80)
    SetChrBattleFlags(0x31, 0x8000)
    SetChrFlags(0x32, 0x80)
    SetChrBattleFlags(0x32, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x1A, -12260, 0, -10460, 45)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -14190, 0, -10860, 45)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, -7110, 0, -9730, 45)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x22, -7510, 0, -8540, 45)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x26, -4900, 2000, 22900, 120)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrPos(0x27, -4900, 2000, 24200, 120)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, 13300, 0, 12600, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 13500, 0, 11300, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -4500, 0, 14100, 135)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x24, -2700, -350, 6100, 45)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrPos(0x25, -2000, -500, 5350, 45)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_4B(0x23, 0xFF)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrPos(0x23, -3150, 0, 15000, 135)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 2700, -400, 5500, 0)

    label("loc_1D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1D48")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 74)
    Jump("loc_1D6B")

    label("loc_1D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1D5C")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 78)
    Jump("loc_1D6B")

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1D6B")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 83)

    label("loc_1D6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D93")
    SetChrPos(0x0, -19600, 0, -27950, 0)

    label("loc_1D93")

    Return()

    # Function_10_13CB end

    def Function_11_1D94(): pass

    label("Function_11_1D94")

    ClearMapObjFlags(0x4, 0x10)
    OP_66(0x2, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DC5")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE2")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1DE2")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E1A")
    ClearMapObjFlags(0x5, 0x4)
    Jump("loc_1EE6")

    label("loc_1E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1E28")
    Jump("loc_1EE6")

    label("loc_1E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E93")
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_71(0x9, 0x12C, 0x12C, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E8E")
    OP_65(0x4, 0x1)

    label("loc_1E8E")

    Jump("loc_1EE6")

    label("loc_1E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1EAB")
    ClearMapObjFlags(0xD, 0x4)
    OP_65(0x5, 0x1)
    Jump("loc_1EE6")

    label("loc_1EAB")

    ClearMapObjFlags(0x5, 0x4)
    OP_65(0x5, 0x1)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_71(0x9, 0x12C, 0x12C, 0x0, 0x0)

    label("loc_1EE6")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 68040, -3500, 11820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E1(0x13DE4, 0x0, 0x71E8)
    OP_E1(0x13C54, 0x0, 0xD1B0)
    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 27000, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 2500, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -18500, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_11_1D94 end

    def Function_12_2021(): pass

    label("Function_12_2021")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20BB")

    #C0001
    ChrTalk(
        0xFE,
        "……ねえ聞いた？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "今日は最後に\x01",
            "お菓子つかみ大会があるらしいわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0003
    ChrTalk(
        0xFE,
        (
            "楽しみよね～。\x01",
            "ぜひ参加しなくっちゃ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2314")

    label("loc_20BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2126")

    #C0004
    ChrTalk(
        0xFE,
        "あら、また不良達が出てる……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "あの子たちって、もしかして\x01",
            "人前で目立ちたいのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2314")

    label("loc_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2191")

    #C0006
    ChrTalk(
        0xFE,
        (
            "今日のステージは\x01",
            "飛び入り参加ＯＫなんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "うふふ、私も挑戦してみようかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2314")

    label("loc_2191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_225F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21F6")

    #C0008
    ChrTalk(
        0xFE,
        (
            "せっかく面白そうな事を\x01",
            "やっているんだもの。\x01",
            "いい場所を確保しなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225A")

    label("loc_21F6")


    #C0009
    ChrTalk(
        0xFE,
        (
            "うーん、人がたくさん居て\x01",
            "ステージがよく見えないのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "どこかいい場所はないかしら。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_225A")

    Jump("loc_2314")

    label("loc_225F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_229A")

    #C0011
    ChrTalk(
        0xFE,
        (
            "今日は何をやるのかしら。\x01",
            "楽しみだわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2314")

    label("loc_229A")


    #C0012
    ChrTalk(
        0xFE,
        (
            "昨日はそこのステージで\x01",
            "ライブがあって\x01",
            "すっごく盛り上がっちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "うふふ、私催し物とかって\x01",
            "目が無いのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2314")

    TalkEnd(0xFE)
    Return()

    # Function_12_2021 end

    def Function_13_2318(): pass

    label("Function_13_2318")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2325")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2383")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2383")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A3")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29A0")

    label("loc_23A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B7")
    Jump("loc_29A0")

    label("loc_23B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_24B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_241E")

    #C0014
    ChrTalk(
        0xFE,
        (
            "君たちも食していきたまえ。\x01",
            "記念祭最後の一品だぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B2")

    label("loc_241E")


    #C0015
    ChrTalk(
        0xFE,
        (
            "記念祭の最終日には\x01",
            "毎年ミシュラムで遊ぶ客が多いのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "港湾公園もいつになく賑わっている。\x01",
            "……ふふ、麺の打ちがいも\x01",
            "あるというものだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24B2")

    Jump("loc_29A0")

    label("loc_24B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_24F4")

    #C0017
    ChrTalk(
        0xFE,
        (
            "なんと酷い歌だ……\x01",
            "これでは営業妨害だぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A0")

    label("loc_24F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_288B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2581")

    #C0018
    ChrTalk(
        0xFE,
        (
            "窃盗の犯人が\x01",
            "捕まったそうではないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "フン、悪事を働けば\x01",
            "必ず報いを受けるのだ。\x01",
            "犯人め、反省するがよい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2886")

    label("loc_2581")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_280C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275E")

    #C0020
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、少しお話を\x01",
            "伺ってもいいですか？\x02\x03",

            "窃盗事件について\x01",
            "捜査をしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "むむ、話は聞いている。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "私の店に来たら\x01",
            "すぐに取り押さえてやるぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003Fあの、そう言う事ではなくて。\x01",
            "犯人の心当たりなんかは……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "むむむ、心当たりか……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "全く無いな。\x01",
            "何せ、この人ごみだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#0101Fそうですよね……\x01",
            "あの、ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xB)
    Jump("loc_2807")

    label("loc_275E")


    #C0028
    ChrTalk(
        0xFE,
        (
            "祭り中に犯行を繰り返すなど、\x01",
            "犯人は下種な奴にちがいない。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "私の店に来たら\x01",
            "すぐに取り押さえてやるぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0000F（ここの店は\x01",
            "  被害に遭いそうに無いかもな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2807")

    Jump("loc_2886")

    label("loc_280C")


    #C0031
    ChrTalk(
        0xFE,
        (
            "昨日から屋台を狙った\x01",
            "窃盗事件が相次いでいるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "むむむ……けしからん話だ。\x01",
            "この私がとっ捕まえてくれよう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2886")

    Jump("loc_29A0")

    label("loc_288B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2924")

    #C0033
    ChrTalk(
        0xFE,
        (
            "親父くさい屋台では、\x01",
            "さすがにジェラートや\x01",
            "ポップコーンには負けてしまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "……だが構うものか。\x01",
            "私は信念に基づいて屋台を開くのだ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A0")

    label("loc_2924")


    #C0035
    ChrTalk(
        0xFE,
        (
            "君たちも騙されたと思って\x01",
            "私の麺を食してみたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "フ……判ったかね？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "そんじょそこらの麺とは\x01",
            "訳が違うのだよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A0")

    Jump("loc_2325")

    label("loc_29A5")

    TalkEnd(0xFE)
    Return()

    # Function_13_2318 end

    def Function_14_29A9(): pass

    label("Function_14_29A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A0F")

    #C0038
    ChrTalk(
        0xFE,
        "今日は家族連れの人が多いね。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "やっぱり締めは\x01",
            "ミシュラムに遊びに行くのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA3")

    label("loc_2A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A78")

    #C0040
    ChrTalk(
        0xFE,
        "徒歩には徒歩の良さがあるんだよな。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "……そりゃま、歩くのは大変だけどさ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AE3")

    label("loc_2A78")


    #C0042
    ChrTalk(
        0xFE,
        (
            "こんな時、徒歩の配達だと\x01",
            "裏道や抜け道が使えるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "導力車の配達屋\x01",
            "なんかには負けないぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2AE3")

    Jump("loc_2CA3")

    label("loc_2AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B30")

    #C0044
    ChrTalk(
        0xFE,
        (
            "ふう……今のうちに\x01",
            "配達を進めておかないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA9")

    label("loc_2B30")


    #C0045
    ChrTalk(
        0xFE,
        (
            "……パレードの交通規制で\x01",
            "配達が遅れちゃいそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "パレードが始まるまでに\x01",
            "できるだけ頑張っておかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2BA9")

    Jump("loc_2CA3")

    label("loc_2BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2C5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2C00")

    #C0047
    ChrTalk(
        0xFE,
        (
            "そんなにパワーが余ってるなら\x01",
            "仕事を手伝ってほしいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C58")

    label("loc_2C00")


    #C0048
    ChrTalk(
        0xFE,
        (
            "公園の真ん中で\x01",
            "ドタバタ騒ぎがあったんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "不良達のやりそうな事だよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2C58")

    Jump("loc_2CA3")

    label("loc_2C5D")


    #C0050
    ChrTalk(
        0xFE,
        "記念祭の間もお休みがないんだ。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "……こういうのって辛いよね。\x02",
    )

    CloseMessageWindow()

    label("loc_2CA3")

    TalkEnd(0xFE)
    Return()

    # Function_14_29A9 end

    def Function_15_2CA7(): pass

    label("Function_15_2CA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2D19")

    #C0052
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "孫娘には悪いが\x01",
            "ワシはハイカラな遊びは\x01",
            "嫌いなんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D80")

    label("loc_2D19")


    #C0054
    ChrTalk(
        0xFE,
        (
            "ＩＢＣめ……\x01",
            "ワシの釣り場を……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "ミシュラムだかなんだか知らんが、\x01",
            "腹が立つ連中じゃわい……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2D80")

    Jump("loc_2F20")

    label("loc_2D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2DC0")

    #C0056
    ChrTalk(
        0xFE,
        (
            "ったく騒がしいのぉ……\x01",
            "頭にくるわい……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F20")

    label("loc_2DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2DFF")

    #C0057
    ChrTalk(
        0xFE,
        (
            "……嫌じゃ。\x01",
            "ワシはパレードなんぞ興味ない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F20")

    label("loc_2DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E40")

    #C0058
    ChrTalk(
        0xFE,
        (
            "ワシは余生を\x01",
            "こうやって過ごすと決めたんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F20")

    label("loc_2E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2EA5")

    #C0059
    ChrTalk(
        0xFE,
        (
            "あの水上バスを\x01",
            "動かしとるのはＩＢＣらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "……決めた、ＩＢＣは嫌いじゃ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F20")

    label("loc_2EA5")


    #C0061
    ChrTalk(
        0xFE,
        "だああ……！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "ったく～～……\x01",
            "騒がしい連中じゃのォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "こっちは釣りを楽しんどるんじゃ。\x01",
            "見て分からんのかい！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2F20")

    TalkEnd(0xFE)
    Return()

    # Function_15_2CA7 end

    def Function_16_2F24(): pass

    label("Function_16_2F24")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2FAA")

    #C0064
    ChrTalk(
        0xFE,
        (
            "ミシュラムかぁ……\x01",
            "わたしも行ってみたいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "えへへ、でも\x01",
            "おじいちゃんがこの調子じゃ\x01",
            "頼んでも無理だよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A2")

    label("loc_2FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_300F")

    #C0066
    ChrTalk(
        0xFE,
        "あれ？　何だかさわがしいなぁ……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "ステージの方で\x01",
            "何かやってるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A2")

    label("loc_300F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_306E")

    #C0068
    ChrTalk(
        0xFE,
        (
            "噂だとね、今年のパレードは\x01",
            "すっごいんだって！\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "ね、一緒に見に行こうよ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_31A2")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_30E3")

    #C0070
    ChrTalk(
        0xFE,
        (
            "おじいちゃんと\x01",
            "遊びに行こうと思ったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "こうなったら\x01",
            "テコでも動かないのよね。\x01",
            "ふう～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31A2")

    label("loc_30E3")

    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0072
    ChrTalk(
        0xFE,
        "おじいちゃんも一緒に回ろうよ！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xB,
        "……嫌じゃ。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "わたし行ってみたい所があるの。\x01",
            "ね、連れて行ってよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        "……嫌じゃ。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "もう～、ホントに頑固なんだから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x10)

    label("loc_31A2")

    TalkEnd(0xFE)
    Return()

    # Function_16_2F24 end

    def Function_17_31A6(): pass

    label("Function_17_31A6")

    TalkBegin(0xFE)

    #C0077
    ChrTalk(
        0xFE,
        "パシャ、パシャ……！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "うん、この写真は\x01",
            "文化面には使えそうかな♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_31A6 end

    def Function_18_31F6(): pass

    label("Function_18_31F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_END)), "loc_334E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3291")

    #C0079
    ChrTalk(
        0xD,
        (
            "#2100Fあ、そうそう。\x01",
            "写真の方は十分撮れたら\x01",
            "通信社の受付に渡しちゃって。\x02\x03",

            "#2109Fよろしく頼んだからね～♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    Jump("loc_3349")

    label("loc_3291")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0080
    ChrTalk(
        0xD,
        (
            "#2100Fさーて、昨日に引き続き、\x01",
            "記念祭のホットなシーンを\x01",
            "捉えまくるわよ～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 300)

    #C0081
    ChrTalk(
        0xD,
        "#2109Fレインズ君、付いてきなさいっ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)

    #C0082
    ChrTalk(
        0xE,
        "りょ、了解です！\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 6)

    label("loc_3349")

    Jump("loc_34E8")

    label("loc_334E")


    #C0083
    ChrTalk(
        0xD,
        (
            "#2100Fはろはろー、昨日はお疲れさま！\x02\x03",

            "#2109F昨日のレースは早速、\x01",
            "面白い記事に仕上げといたわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0006Fグレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0306Fやっぱり記事に\x01",
            "しちまうんスか……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xD,
        (
            "#2104Fそそ、記念祭の最終日に出る\x01",
            "臨時特別号に載るはずよ。\x02\x03",

            "#2100F君たちの活躍もアピールしたから\x01",
            "楽しみにしといてね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0006F（絶対、持ち上げといて\x01",
            "  落としそうな気がする……）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        "#0200F（まあ、いつものパターンですね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 0)

    label("loc_34E8")

    TalkEnd(0xFE)
    Return()

    # Function_18_31F6 end

    def Function_19_34EC(): pass

    label("Function_19_34EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_356F")

    #C0089
    ChrTalk(
        0xFE,
        (
            "ミシュラム行き水上バス、\x01",
            "間もなく到着となりま～す。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "ご利用のお客様は\x01",
            "もうしばらくお待ちくださいませ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_356F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_35E1")

    #C0091
    ChrTalk(
        0xFE,
        (
            "ふう、私も家族で\x01",
            "遊びに行きたいものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "……記念祭が終わったら\x01",
            "お休みを申請しようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_35E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3652")

    #C0093
    ChrTalk(
        0xFE,
        (
            "ミシュラム行きの水上バス、\x01",
            "まもなく出航となりま～す！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "ご利用の方はお急ぎくださいませ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_3652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36C7")

    #C0095
    ChrTalk(
        0xFE,
        (
            "ミシュラム行き水上バス、\x01",
            "到着まであと５分少々となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "どうか今しばらくお待ちくださ～い。\x02",
    )

    CloseMessageWindow()
    Jump("loc_372D")

    label("loc_36C7")


    #C0097
    ChrTalk(
        0xFE,
        (
            "ミシュラム行き水上バス\x01",
            "乗り場はこちらになりまーす！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "ご利用のお客様は\x01",
            "お急ぎくださいませ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372D")

    TalkEnd(0xFE)
    Return()

    # Function_19_34EC end

    def Function_20_3731(): pass

    label("Function_20_3731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_375B")
    Call(0, 82)
    Return()

    label("loc_375B")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3768")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F55")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_37C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37E6")
    OP_AF(0x7D)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F50")

    label("loc_37E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37FA")
    Jump("loc_3F50")

    label("loc_37FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F50")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3926")

    #C0099
    ChrTalk(
        0xFE,
        (
            "あなたたちで窃盗犯を\x01",
            "捕まえてくれたんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "うふふ、やるわね。\x01",
            "感謝しちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1C6, 1)

    #C0102
    ChrTalk(
        0xFE,
        (
            "持って行きなさい。\x01",
            "ほんのお礼よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        "#0100Fありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 1)
    Jump("loc_3F50")

    label("loc_3926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F5")

    #C0104
    ChrTalk(
        0xFE,
        (
            "うふふ、いらっしゃい。\x01",
            "ミスラのジェラート店にようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "私のジェラートは一級品よ。\x01",
            "レミフェリアじゃ『公室御用達』とまで\x01",
            "言われた店なのだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "良かったら味見してらっしゃい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 4)
    Jump("loc_3F50")

    label("loc_39F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B69")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AE3")

    #C0107
    ChrTalk(
        0xFE,
        "今日で記念祭も最後ね。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "うふふ、折角だから\x01",
            "ウチのジェラートの作り方を\x01",
            "教えてあげるわ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x13)
    Jump("loc_3B64")

    label("loc_3AE3")


    #C0111
    ChrTalk(
        0xFE,
        "祭りも今日で最終日……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "さすらいのジェラート屋ミスラも\x01",
            "今日限りで消えてしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "お買い求めになるなら今のうちよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3B64")

    Jump("loc_3F50")

    label("loc_3B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3BDF")

    #C0114
    ChrTalk(
        0xFE,
        (
            "パレードとは聞いていたけれど\x01",
            "これほどとはね……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "本当にクロスベル人は\x01",
            "派手なのがお好きなのね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F50")

    label("loc_3BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3E19")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C5B")

    #C0116
    ChrTalk(
        0xFE,
        (
            "さて、そろそろパレードが\x01",
            "始まるそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "うふふ、客も増えそうね。\x01",
            "私も楽しみだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E14")

    label("loc_3C5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CE0")

    #C0118
    ChrTalk(
        0xFE,
        (
            "……まさか客の相手をしている時を\x01",
            "狙われるとは思わなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        "私とした事がとんだ失態ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E14")

    label("loc_3CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3D52")

    #C0120
    ChrTalk(
        0xFE,
        (
            "クロスベルは\x01",
            "最高にエキサイティングね。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "うふふ、祭りが\x01",
            "終わってしまうのが哀しいくらいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E14")

    label("loc_3D52")


    #C0122
    ChrTalk(
        0xFE,
        (
            "世界中の人間が\x01",
            "クロスベルを目指してやってくる。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "そして存分に夢を見て\x01",
            "自分達の国へ帰っていく……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "ふふ、本当に面白い土地ね。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "いままで訪れた中で\x01",
            "最高にエキサイティングだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_3E14")

    Jump("loc_3F50")

    label("loc_3E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3E82")

    #C0126
    ChrTalk(
        0xFE,
        (
            "うふふ、昨日は\x01",
            "大変だったようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "こっちの方にも\x01",
            "噂が流れてきてたわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ECB")

    label("loc_3E82")


    #C0128
    ChrTalk(
        0xFE,
        "あら昨日のヒーローたちじゃない。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "どう、お安くしておくけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_3ECB")

    Jump("loc_3F50")

    label("loc_3ED0")


    #C0130
    ChrTalk(
        0xFE,
        (
            "私のジェラートは一級品よ。\x01",
            "レミフェリアじゃ『公室御用達』とまで\x01",
            "言われた店なのだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        "良かったら味見してらっしゃい。\x02",
    )

    CloseMessageWindow()

    label("loc_3F50")

    Jump("loc_3768")

    label("loc_3F55")

    TalkEnd(0xFE)
    Return()

    # Function_20_3731 end

    def Function_21_3F59(): pass

    label("Function_21_3F59")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A9")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FC4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3FC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE4")
    OP_AF(0x7C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45A4")

    label("loc_3FE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FF8")
    Jump("loc_45A4")

    label("loc_3FF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_40DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_406A")

    #C0132
    ChrTalk(
        0xFE,
        "……ステーキはどうカナ。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "お祭りの最後、楽しまないとネ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_406A")


    #C0134
    ChrTalk(
        0xFE,
        "今日でお祭り最後なんだネ。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "僕らも何だか寂しいヨ。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "こういう気持ちを\x01",
            "名残惜しいというのカナ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_40D8")

    Jump("loc_45A4")

    label("loc_40DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4114")

    #C0137
    ChrTalk(
        0xFE,
        (
            "オヤ……\x01",
            "ステージの方が騒がしいナ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A4")

    label("loc_4114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_450F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4188")

    #C0138
    ChrTalk(
        0xFE,
        (
            "ハイ、いらっしゃい。\x01",
            "串焼きはいかがカナ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "とびきりおいしい\x01",
            "串焼きステーキだヨ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_450A")

    label("loc_4188")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_442C")

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、少しお話を\x01",
            "伺ってもいいですか？\x02\x03",

            "窃盗事件について\x01",
            "捜査をしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "そ、その話カ。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "ウチは大丈夫だと思うケド。\x01",
            "妹と２人で店番をやっているしネ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "１人だと、どうしても\x01",
            "隙が出来てしまう。\x01",
            "その点２人なら、守りは万全。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        (
            "#0101Fこの付近で怪しい人物を\x01",
            "見かけたりもしていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "そ、それは……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "さっきからあそこに\x01",
            "赤ジャージの青年が来ててネ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "あれが、気になってるヨ。\x01",
            "一体何者カナ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        "#0300Fあの連中は、まあ別口だぜ。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        (
            "#0203Fセコい窃盗事件を起こすような\x01",
            "タイプではないかと。\x02\x03",

            "#0200Fまあ、彼らが問題を起こしたら\x01",
            "別件で通報してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "りょ、了解ダヨ。\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xC)
    Jump("loc_44A0")

    label("loc_442C")


    #C0151
    ChrTalk(
        0xFE,
        (
            "記念祭、お客さんも多いし\x01",
            "怪しい人物と言われても分からないネ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "……ウチには窃盗犯、\x01",
            "来ない事を祈ってるヨ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44A0")

    Jump("loc_450A")

    label("loc_44A5")


    #C0153
    ChrTalk(
        0xFE,
        (
            "僕らはクロスベルの\x01",
            "祭りに合わせて\x01",
            "東の方から来たんダ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "思ったとおり、\x01",
            "とても売れているヨ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_450A")

    Jump("loc_45A4")

    label("loc_450F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_454F")

    #C0155
    ChrTalk(
        0xFE,
        "妹は客寄せが得意デネ。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "とても助かるヨ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45A4")

    label("loc_454F")


    #C0157
    ChrTalk(
        0xFE,
        "ヤ、串焼きステーキはどうカナ。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "おいしくて食べやすい\x01",
            "サイコロステーキだヨ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A4")

    Jump("loc_3F66")

    label("loc_45A9")

    TalkEnd(0xFE)
    Return()

    # Function_21_3F59 end

    def Function_22_45AD(): pass

    label("Function_22_45AD")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B57")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4618")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4638")
    OP_AF(0x7C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B52")

    label("loc_4638")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_464C")
    Jump("loc_4B52")

    label("loc_464C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B52")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_46E9")

    #C0159
    ChrTalk(
        0xFE,
        (
            "えーっ、もしかしてあの人が\x01",
            "ステージの主催者だったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "案外普通のオジーサマじゃない。\x01",
            "ちょっとビックリね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B52")

    label("loc_46E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4786")

    #C0161
    ChrTalk(
        0xFE,
        (
            "ホイさ、本日は\x01",
            "ドリンクセットもありィ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "喉が渇いたお客さん、\x01",
            "いらっしゃいやせんか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "ドリンクセット、\x01",
            "お買い得でやんすぜィ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B52")

    label("loc_4786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4968")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_485C")

    #C0164
    ChrTalk(
        0xFE,
        (
            "例の連続窃盗犯、\x01",
            "捕まったらしいじゃん？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "やれやれ、これでちょっとは\x01",
            "安心してお商売ができるわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "まあクロスベルって\x01",
            "何かとトラブルが多いし。\x01",
            "特にお祭中は気が抜けないけど～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4963")

    label("loc_485C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4922")

    #C0167
    ChrTalk(
        0xFE,
        (
            "商工会の人が\x01",
            "窃盗犯に気を付けるように\x01",
            "言ってきてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "やっぱクロスベルは\x01",
            "治安がイマイチねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "売り上げ盗られちゃたまんないし、\x01",
            "気ぃ張ってかないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4963")

    label("loc_4922")


    #C0170
    ChrTalk(
        0xFE,
        (
            "今日は警察の人が\x01",
            "ウロウロしてんのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "何かあるの～？\x02",
    )

    CloseMessageWindow()

    label("loc_4963")

    Jump("loc_4B52")

    label("loc_4968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_49D7")

    #C0172
    ChrTalk(
        0xFE,
        (
            "さあ買うなら\x01",
            "早くしておくんなせえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "もたもたしてっと\x01",
            "日が暮れちゃいやすぜっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A60")

    label("loc_49D7")


    #C0174
    ChrTalk(
        0xFE,
        (
            "ヘイそこの兄さん、\x01",
            "小腹が空いていたりはしないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "そんなトキには\x01",
            "串焼きステーキでやんしょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "祭りを楽しく回れますぜ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_4A60")

    Jump("loc_4B52")

    label("loc_4A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4AC6")

    #C0177
    ChrTalk(
        0xFE,
        "祭りとくりゃあ串焼きですぜ！\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "串片手に回りゃあ\x01",
            "楽しさ倍増ですぜ、兄さん！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B52")

    label("loc_4AC6")


    #C0179
    ChrTalk(
        0xFE,
        (
            "ヤアめでてえ、めでてえ。\x01",
            "今日はめでてて祭りでやんすねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "祭りとくりゃあ串焼きステーキ！\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "さあ兄さん方もいかがでやんすか！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_4B52")

    Jump("loc_45BA")

    label("loc_4B57")

    TalkEnd(0xFE)
    Return()

    # Function_22_45AD end

    def Function_23_4B5B(): pass

    label("Function_23_4B5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_4BEA")

    #C0182
    ChrTalk(
        0xFE,
        (
            "無事に犯人が\x01",
            "捕まったそうじゃな！\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "わはは、よかったわい。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "これでワシらも安心して\x01",
            "祭りを楽しめるというもんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_511D")

    label("loc_4BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4C60")

    #C0185
    ChrTalk(
        0xFE,
        (
            "モルスの奴は\x01",
            "中々の名スピーチをするんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "わはは、始める前は\x01",
            "緊張するとか愚痴るんじゃがな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_511D")

    label("loc_4C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4D2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CB8")

    #C0187
    ChrTalk(
        0xFE,
        "おお？　なんじゃ……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        "ステージの方が騒がしいのう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D29")

    label("loc_4CB8")


    #C0189
    ChrTalk(
        0xFE,
        (
            "いやはや、さすが遊撃士じゃ。\x01",
            "素早い仕事振りじゃのう！\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "これで市民にも\x01",
            "楽しんでもらえようぞ。\x01",
            "わははは！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D29")

    Jump("loc_511D")

    label("loc_4D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_503D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DFE")
    OP_93(0xFE, 0x87, 0x0)

    #C0191
    ChrTalk(
        0xFE,
        (
            "どうじゃ、ひと働きした後は\x01",
            "気持ちのええもんじゃろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "どれ、今日はワシが酒を奢ってやろう。\x01",
            "わはは、酒はいいぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x17,
        (
            "ううっ、いらねえッスよ！\x01",
            "オレまだギリギリ未成年！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5038")

    label("loc_4DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_4E86")

    #C0194
    ChrTalk(
        0xFE,
        "この辺りは異常なしじゃな。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "ふむ……といっても\x01",
            "犯人の目星もついておらんし。\x01",
            "単に見回ることしかできんがのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5038")

    label("loc_4E86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_4FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F04")

    #C0196
    ChrTalk(
        0xFE,
        (
            "出店を出しとるモンに\x01",
            "注意を呼びかけてこんとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "どれ、ワシらでもう一回りしてくるか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_4F9D")

    label("loc_4F04")


    #C0198
    ChrTalk(
        0xFE,
        (
            "ワシらも露天をやっとった頃は\x01",
            "よう盗人と戦ったもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "しかし……今回は\x01",
            "祭りを台無しにする無粋な輩じゃ。\x01",
            "手加減無用で引っ捕らえてやらんとの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F9D")

    Jump("loc_5038")

    label("loc_4FA2")


    #C0200
    ChrTalk(
        0xFE,
        (
            "この港湾公園でも\x01",
            "ミスラさんの出店が\x01",
            "窃盗犯にやられたそうじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "やれやれ、めでたい祭りの\x01",
            "最中じゃというのに。\x01",
            "興ざめな事をする輩じゃわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5038")

    Jump("loc_511D")

    label("loc_503D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_50AB")

    #C0202
    ChrTalk(
        0xFE,
        (
            "そういやこいつ、\x01",
            "可愛いお孫さんがいたんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "どーれどれ。\x01",
            "ワシが一緒に遊んでやろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_511D")

    label("loc_50AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50BD")
    Call(0, 33)
    Jump("loc_511D")

    label("loc_50BD")


    #C0204
    ChrTalk(
        0xFE,
        (
            "パーラさんはその昔\x01",
            "ワシらのアイドルだったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "わはは、モルスの奴が\x01",
            "羨ましいわい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_511D")

    TalkEnd(0xFE)
    Return()

    # Function_23_4B5B end

    def Function_24_5121(): pass

    label("Function_24_5121")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_530C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_519A")

    #C0206
    ChrTalk(
        0xFE,
        (
            "今朝は我らが商工会会長に\x01",
            "一言ご挨拶をお願いします！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A, 500)

    #C0207
    ChrTalk(
        0xFE,
        "──どうぞ、会長！\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x0)
    Jump("loc_5307")

    label("loc_519A")


    #C0208
    ChrTalk(
        0xFE,
        "えー、皆さんに残念なお知らせです。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "楽しい記念祭も\x01",
            "本日で最後となってしまいました！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0210
    ChrTalk(
        0xFE,
        (
            "それでは最終日の\x01",
            "ケジメということで～……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "我らがクロスベル商工会会長に\x01",
            "一言ご挨拶をお願いします！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A, 500)

    #C0212
    ChrTalk(
        0xFE,
        "──どうぞ、会長！\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x0)
    SetScenarioFlags(0x1, 2)

    label("loc_5307")

    Jump("loc_5610")

    label("loc_530C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5395")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_538D")

    #C0213
    ChrTalk(
        0xFE,
        (
            "うおお、また何をやってるんだ\x01",
            "あんた達はーっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "すぐにステージから降りろっ！\x01",
            "降りてくれ～っ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5390")

    label("loc_538D")

    Call(0, 53)

    label("loc_5390")

    Jump("loc_5610")

    label("loc_5395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_542F")

    #C0215
    ChrTalk(
        0xFE,
        (
            "さあ最高点を記録するのは\x01",
            "どのチームなのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "本日のステージは飛び込み歓迎！\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "自信をお持ちの方は\x01",
            "手を挙げちゃってくださ～い！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5610")

    label("loc_542F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_54AE")

    #C0218
    ChrTalk(
        0xFE,
        (
            "昨日は酷い目にあったが\x01",
            "今日の催し物は順調だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "昨日の詫びも兼ねて\x01",
            "楽しんでもらわなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_552C")

    label("loc_54AE")


    #C0220
    ChrTalk(
        0xFE,
        (
            "イエーイ、次なる大道芸は\x01",
            "間一髪の脱出劇だーっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "さあそれでは皆さんの中から\x01",
            "１名に手伝って頂きましょう……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x14, 0x10)

    label("loc_552C")

    Jump("loc_5610")

    label("loc_5531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_55A1")

    #C0222
    ChrTalk(
        0xFE,
        (
            "クイズ大会の準備には\x01",
            "もう少し掛かるんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "お兄さん方、そう焦らず\x01",
            "待っててくれよなっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5610")

    label("loc_55A1")


    #C0224
    ChrTalk(
        0xFE,
        (
            "イエーイ、お兄さん方。\x01",
            "ちょーっと待ってくれよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "今ハッピークイズ大会の\x01",
            "準備をしてる所だからさ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_5610")

    TalkEnd(0xFE)
    Return()

    # Function_24_5121 end

    def Function_25_5614(): pass

    label("Function_25_5614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5625")
    Call(0, 30)
    Jump("loc_5628")

    label("loc_5625")

    Call(0, 26)

    label("loc_5628")

    Return()

    # Function_25_5614 end

    def Function_26_5629(): pass

    label("Function_26_5629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5677")
    Call(0, 77)
    Return()

    label("loc_5677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56A0")
    Call(0, 75)
    Return()

    label("loc_56A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5726")
    TalkBegin(0x15)

    #C0226
    ChrTalk(
        0x15,
        (
            "ロイ君とメイリンちゃんが\x01",
            "手伝ってくれて助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x15,
        (
            "何だかんだ言ってロイ君も\x01",
            "頑張ってくれるじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Jump("loc_5E3C")

    label("loc_5726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5998")
    TalkBegin(0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_57CB")

    #C0228
    ChrTalk(
        0xFE,
        "皆さん、どうもお世話になりました！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "しかし……出店の皆さんには\x01",
            "ご迷惑を掛けてしまいました。\x01",
            "何か補償をしてあげたい所ですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5990")

    label("loc_57CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_587C")

    #C0230
    ChrTalk(
        0xFE,
        (
            "毎年記念祭には\x01",
            "トラブルが多いんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "……連続窃盗事件とは。\x01",
            "我々にはどうしようもありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "すみませんが皆さん、\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5990")

    label("loc_587C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_5936")

    #C0233
    ChrTalk(
        0xFE,
        (
            "このままでは\x01",
            "出店をたたむ人も\x01",
            "出てくるかもしれません……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "せっかくのお祭りに\x01",
            "そんな事にはしたくないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "どうか、皆さんに\x01",
            "お願いできないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5990")

    label("loc_5936")


    #C0236
    ChrTalk(
        0xFE,
        (
            "はあ、注意を\x01",
            "呼びかけているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "やはりどなたかの\x01",
            "手を借りない事には……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5990")

    TalkEnd(0x15)
    Jump("loc_5E3C")

    label("loc_5998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5B7D")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x15)
    ClearChrFlags(0x15, 0x10)
    TurnDirection(0x15, 0x0, 0)
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A35")
    Jump("loc_5A7F")

    label("loc_5A35")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A55")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A7F")

    label("loc_5A55")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A75")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A7F")

    label("loc_5A75")

    OP_52(0x15, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A7F")

    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5B06")

    #C0238
    ChrTalk(
        0x15,
        (
            "ふう、それにしても\x01",
            "凄い混みようだなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x15,
        (
            "僕一人じゃ\x01",
            "忙しくて仕方ないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B71")

    label("loc_5B06")


    #C0240
    ChrTalk(
        0x15,
        (
            "会長の息子さんは\x01",
            "大企業を経営なさってるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x15,
        (
            "でも孫のロイ君は\x01",
            "反発しちゃってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_5B71")

    SetChrSubChip(0x15, 0x0)
    TalkEnd(0x15)
    Jump("loc_5E3C")

    label("loc_5B7D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x15)
    ClearChrFlags(0x15, 0x10)
    TurnDirection(0x15, 0x0, 0)
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C11")
    Jump("loc_5C5B")

    label("loc_5C11")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C31")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C5B")

    label("loc_5C31")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C51")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C5B")

    label("loc_5C51")

    OP_52(0x15, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C5B")

    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D27")

    #C0242
    ChrTalk(
        0x15,
        (
            "やあどうも、こちらは\x01",
            "クロスベル商工会のテントだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x15,
        (
            "市民の方も\x01",
            "参加してくれちゃってＯＫさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x15,
        (
            "抽選や景品交換なんかも\x01",
            "催しているんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 5)
    Jump("loc_5E35")

    label("loc_5D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_5D93")

    #C0245
    ChrTalk(
        0x15,
        (
            "会長たちは昔は\x01",
            "独立した露店商だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x15,
        (
            "なんだか当時の様子が\x01",
            "目に浮かぶようだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E35")

    label("loc_5D93")


    #C0247
    ChrTalk(
        0x15,
        (
            "会長たちは昔は\x01",
            "市場で露店を開いていたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x15,
        (
            "ライバルにして商売仲間……\x01",
            "みんなそんな関係だったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x15,
        (
            "ふふ、当時の様子が\x01",
            "目に浮かぶようだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_5E35")

    SetChrSubChip(0x15, 0x0)
    TalkEnd(0x15)

    label("loc_5E3C")

    Return()

    # Function_26_5629 end

    def Function_27_5E3D(): pass

    label("Function_27_5E3D")

    TalkBegin(0xFE)

    #C0250
    ChrTalk(
        0xFE,
        "うーん、いい眺め。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "出店回るのに疲れてたから\x01",
            "ここでちょっと休憩してるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "ちょっと賑やかな場所を離れると\x01",
            "クロスベル市もなかなか\x01",
            "雰囲気があっていい場所よね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_5E3D end

    def Function_28_5EEF(): pass

    label("Function_28_5EEF")

    TalkBegin(0xFE)

    #C0253
    ChrTalk(
        0xFE,
        (
            "この町もアルモリカ村も\x01",
            "良い所ばかりじゃないし\x01",
            "悪い所ばかりでもない、か……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "……村の子にお土産でも\x01",
            "買ってってやろうかな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_5EEF end

    def Function_29_5F79(): pass

    label("Function_29_5F79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_60A4")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6009")

    #C0255
    ChrTalk(
        0xFE,
        "あ、犯人捕まったのか？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "……な、なんだ。\x01",
            "意外と早かったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "ほっ……な、なら良かったぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6098")

    label("loc_6009")


    #C0258
    ChrTalk(
        0xFE,
        (
            "出店が襲われてるって聞いたから\x01",
            "オレすげー心配してたんだけど……\x01",
            "意外と早く捕まったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "そんならいいや。\x01",
            "……早く店番に戻ろっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6098")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_62B8")

    label("loc_60A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_613B")

    #C0260
    ChrTalk(
        0xFE,
        (
            "ええと、次はっと……\x01",
            "もう一度ミスラさんの所も\x01",
            "見に行っとくかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "一度狙われた店は大丈夫だと思うけど\x01",
            "……やっぱ心配だしさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B8")

    label("loc_613B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6220")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61CB")

    #C0262
    ChrTalk(
        0xFE,
        (
            "オレ、ちょっと\x01",
            "この辺りを見回ってくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "連続窃盗犯らしいし……\x01",
            "やっぱ出店の人とか心配だしさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6214")

    label("loc_61CB")


    #C0264
    ChrTalk(
        0xFE,
        (
            "見回りくらいならオレにもできるしな。\x01",
            "……オレちょっと回ってくるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6214")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_62B8")

    label("loc_6220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_62B8")

    #C0265
    ChrTalk(
        0xFE,
        (
            "メイリンが出店見たいって\x01",
            "言ったから来ただけだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "オレ、商工会なんて\x01",
            "興味ねえし～。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "……爺ちゃん、オヤジには\x01",
            "黙っといてくれよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62B8")

    TalkEnd(0xFE)
    Return()

    # Function_29_5F79 end

    def Function_30_62BC(): pass

    label("Function_30_62BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6484")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6359")
    Jump("loc_63A3")

    label("loc_6359")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6379")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_63A3")

    label("loc_6379")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6399")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_63A3")

    label("loc_6399")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63A3")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6412")

    #C0268
    ChrTalk(
        0x17,
        "らっしゃーい。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x17,
        "抽選と景品交換は今日までだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6478")

    label("loc_6412")


    #C0270
    ChrTalk(
        0x17,
        (
            "……人手が足りないからって\x01",
            "ずっと受付を任されてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x17,
        (
            "とほほ、オレって\x01",
            "流されやすいよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6478")

    SetChrSubChip(0x17, 0x0)
    TalkEnd(0x17)
    Jump("loc_6793")

    label("loc_6484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_668B")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6521")
    Jump("loc_656B")

    label("loc_6521")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6541")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_656B")

    label("loc_6541")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6561")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_656B")

    label("loc_6561")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_656B")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65F0")

    #C0272
    ChrTalk(
        0x17,
        "うお～、なんて人の数だ……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x17,
        (
            "オレも誘導とか\x01",
            "手伝ったほうがいいのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667F")

    label("loc_65F0")


    #C0274
    ChrTalk(
        0x17,
        (
            "相変わらず\x01",
            "遊撃士はすげーよなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x17,
        "っていうか凄い人の数だよな……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x17,
        (
            "パレードのせいか？\x01",
            "オレも誘導とか\x01",
            "手伝ったほうがいいのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_667F")

    SetChrSubChip(0x17, 0x0)
    TalkEnd(0x17)
    Jump("loc_6793")

    label("loc_668B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6793")
    TalkBegin(0x17)
    SetChrSubChip(0x17, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6720")

    #C0277
    ChrTalk(
        0x17,
        (
            "くそー、良く考えりゃあ\x01",
            "なぜオレが手伝わなきゃならんのだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x17,
        (
            "商売なんて興味ねえって\x01",
            "言ってるのにさぁ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_678C")

    label("loc_6720")


    #C0279
    ChrTalk(
        0x17,
        (
            "何か事件が立て続けに\x01",
            "起きてるみたいだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x17,
        (
            "しゃ、しゃあねえな。\x01",
            "オレも店番くらいは手伝うかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678C")

    SetChrSubChip(0x17, 0x2)
    TalkEnd(0x17)

    label("loc_6793")

    Return()

    # Function_30_62BC end

    def Function_31_6794(): pass

    label("Function_31_6794")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_67C3")

    #C0281
    ChrTalk(
        0xFE,
        (
            "わーい！\x01",
            "お店たくさんなの～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67C3")

    TalkEnd(0xFE)
    Return()

    # Function_31_6794 end

    def Function_32_67C7(): pass

    label("Function_32_67C7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x19)
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x0, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_685B")
    Jump("loc_68A5")

    label("loc_685B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_687B")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68A5")

    label("loc_687B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_689B")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68A5")

    label("loc_689B")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68A5")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6917")

    #C0282
    ChrTalk(
        0x19,
        "いらしゃませー！\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x19,
        (
            "けーひんこうかん、\x01",
            "うけつけだよー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD2")

    label("loc_6917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_69D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6974")

    #C0284
    ChrTalk(
        0x19,
        "いまのがぱれーど？\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    #C0285
    ChrTalk(
        0x19,
        "すごかったねー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_69CD")

    label("loc_6974")


    #C0286
    ChrTalk(
        0x19,
        "ゆーげきしの人、すごかったのー！\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x19,
        (
            "ぱぱぱーってすいりして、\x01",
            "捕まえちゃったのー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69CD")

    Jump("loc_6BD2")

    label("loc_69D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6BD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6B37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_6A78")

    #C0288
    ChrTalk(
        0x19,
        "兄たんたち、かっこよかったよー。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x19,
        (
            "せーふくの人に\x01",
            "びしってあいさつするの、\x01",
            "すごくかっこいいのー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    Jump("loc_6B32")

    label("loc_6A78")


    #C0290
    ChrTalk(
        0x19,
        "兄たんたち、かっこよかったよー。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x19,
        (
            "でもワンちゃんは\x01",
            "もっとかっこよかったのー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_6B32")

    Jump("loc_6BD2")

    label("loc_6B37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6BA0")

    #C0292
    ChrTalk(
        0x19,
        "メイリンがお店番してるのー。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x19,
        (
            "兄たんたち、キキコミに\x01",
            "行ってきて大丈夫なのー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BD2")

    label("loc_6BA0")


    #C0294
    ChrTalk(
        0x19,
        "兄たんとお店番なのー。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x19,
        "いらしゃませー！\x02",
    )

    CloseMessageWindow()

    label("loc_6BD2")

    SetChrSubChip(0x19, 0x0)
    TalkEnd(0x19)
    Return()

    # Function_32_67C7 end

    def Function_33_6BDA(): pass

    label("Function_33_6BDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C28")
    Call(0, 77)
    Return()

    label("loc_6C28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C51")
    Call(0, 75)
    Return()

    label("loc_6C51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6CEB")

    #C0296
    ChrTalk(
        0xFE,
        "やれやれ、ついに最終日か……\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "挨拶は苦手なのじゃが。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x14, 0xFF)
    TurnDirection(0x14, 0xFE, 500)

    #C0298
    ChrTalk(
        0x14,
        (
            "いいからビシッと\x01",
            "決めちゃってくださいよ、会長！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_93(0x14, 0x10E, 0x0)
    Jump("loc_773B")

    label("loc_6CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6EBA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6D3C")

    #C0299
    ChrTalk(
        0xFE,
        (
            "おお、また君たちか……！\x01",
            "乱暴はやめたまえよ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB5")

    label("loc_6D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D65")

    #C0300
    ChrTalk(
        0xFE,
        "おや、君らか。\x02",
    )

    CloseMessageWindow()

    label("loc_6D65")


    #C0301
    ChrTalk(
        0xFE,
        (
            "いや実は、先ほど遊撃士に\x01",
            "窃盗犯を捕まえて貰った所でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "ははは、良かった良かった。\x01",
            "これでようやく祭りも楽しめよう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EB2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E40")

    #C0303
    ChrTalk(
        0x101,
        (
            "#0005F（あ……あの事件\x01",
            "  解決してしまったのか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E75")

    label("loc_6E40")


    #C0304
    ChrTalk(
        0x101,
        (
            "#0005F（事件……？\x01",
            "  窃盗事件があったのか……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E75")


    #C0305
    ChrTalk(
        0x104,
        (
            "#0306F（しまったな……遊撃士に\x01",
            "  先を越されるとは……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EB2")

    SetScenarioFlags(0x1, 4)

    label("loc_6EB5")

    Jump("loc_773B")

    label("loc_6EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_745D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6F5F")

    #C0306
    ChrTalk(
        0xFE,
        (
            "いや、しかし世話になったな。\x01",
            "これでようやく祭りも楽しめよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "ははは、良かった良かった。\x01",
            "わしもよい若者と\x01",
            "知り合ったものじゃて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7458")

    label("loc_6F5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7175")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70D4")

    #C0308
    ChrTalk(
        0xFE,
        (
            "被害があった店舗は\x01",
            "中央広場、行政区、\x01",
            "歓楽街と港湾公園にも１つずつじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "……まあ無事な店舗にも\x01",
            "話を聞いておくと、\x01",
            "何かの参考になるかも知れんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#0005Fなるほど……そうですね。\x01",
            "一通り聞き込んでみます。\x02\x03",

            "#0001F終わったら戻ってきますから\x01",
            "このまま待機していてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "うむ、了解じゃ。\x01",
            "こちらも何かあれば\x01",
            "すぐに知らせよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_7170")

    label("loc_70D4")


    #C0312
    ChrTalk(
        0xFE,
        (
            "被害があった店舗は\x01",
            "中央広場、行政区、\x01",
            "歓楽街と港湾公園にも１つずつじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "……まあ無事な店舗にも\x01",
            "話を聞いておくと、\x01",
            "何かの参考になるかも知れんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7170")

    Jump("loc_7458")

    label("loc_7175")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_7419")

    #C0314
    ChrTalk(
        0x1A,
        (
            "出店を狙う連続窃盗犯……\x01",
            "商工会としても\x01",
            "これ以上放っては置けん。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x1A,
        (
            "何より、このままでは\x01",
            "祭りを楽しみに来た客にも\x01",
            "迷惑が掛かってしまうじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x1A,
        (
            "君たちで犯人を\x01",
            "捕まえてはくれんかね。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【断る】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_735A")
    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 198)
    SetChrPos(0x15, -16920, 0, -9360, 198)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_0D()
    Call(0, 76)
    Return()

    label("loc_735A")


    #C0317
    ChrTalk(
        0x101,
        (
            "#0006Fすみません、今は仕事が\x01",
            "立て込んでまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x1A,
        "そうか、なら仕方がないな。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x1A,
        (
            "手が空いたらまた来てくれんか。\x01",
            "次の被害が出る前に\x01",
            "何としても解決したいんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x1A, 0x13B, 0x0)
    OP_93(0x15, 0x87, 0x0)
    Jump("loc_7458")

    label("loc_7419")


    #C0320
    ChrTalk(
        0xFE,
        "困ったのう……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "これでは祭りを\x01",
            "楽しむ所ではないわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7458")

    Jump("loc_773B")

    label("loc_745D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7559")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0322
    ChrTalk(
        0xFE,
        (
            "おやロイじゃないか。\x01",
            "来ておったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x16,
        (
            "メイリンが\x01",
            "遊びたいって言うから……\x01",
            "オヤジには黙っといてくれよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "はっはっ、なに\x01",
            "あやつも祭りの日まで\x01",
            "騒がしくは言わんじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "今日はゆっくり\x01",
            "遊んで行きなさい。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_773B")

    label("loc_7559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_773B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E2")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0326
    ChrTalk(
        0x13,
        (
            "おお、パーラさん\x01",
            "久し振りじゃなぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x13,
        (
            "しかし……モルスの奴は\x01",
            "上手くやりおったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x13,
        (
            "ワシらの中ではアイドルじゃった\x01",
            "パーラさんと持っていくとはのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x1B,
        "あらあら、大げさですこと。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x1A,
        (
            "セルベットや、\x01",
            "酒はその位にしておかんと\x01",
            "わしがひっぱたくぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x13,
        (
            "わはは、怖い怖い。\x01",
            "会長殿は相変わらずの\x01",
            "オシドリ夫婦じゃのう。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_4C(0x13, 0xFF)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x10)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 4)
    Jump("loc_773B")

    label("loc_76E2")


    #C0332
    ChrTalk(
        0xFE,
        (
            "やれやれ、わしの友人は\x01",
            "お調子者ばかりなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        "一度ひっぱたいてやろうかのう。\x02",
    )

    CloseMessageWindow()

    label("loc_773B")

    TalkEnd(0xFE)
    Return()

    # Function_33_6BDA end

    def Function_34_773F(): pass

    label("Function_34_773F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_77C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_775D")
    Call(0, 33)
    Jump("loc_77C9")

    label("loc_775D")


    #C0334
    ChrTalk(
        0xFE,
        (
            "商工会の皆さんとは\x01",
            "私もお付き合いがあるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "ふふ、何年経っても\x01",
            "皆さん変わっていないのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C9")

    TalkEnd(0xFE)
    Return()

    # Function_34_773F end

    def Function_35_77CD(): pass

    label("Function_35_77CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7848")

    #C0336
    ChrTalk(
        0xFE,
        (
            "おっほん、わが子の\x01",
            "頼みでは仕方が無いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "今日はテーマパークで\x01",
            "ぱーっと遊ぶとしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_799E")

    label("loc_7848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_78C0")

    #C0338
    ChrTalk(
        0xFE,
        "はわわ、こんな怖い人に……\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "む、息子よ。\x01",
            "ひとことお礼を言ったら\x01",
            "パパと向こうに行こうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_799E")

    label("loc_78C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_791F")

    #C0340
    ChrTalk(
        0xFE,
        "もうすぐパレードが始まるぞ！\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "私はパレードが\x01",
            "子供の頃から大好きなんだ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_799E")

    label("loc_791F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7971")

    #C0342
    ChrTalk(
        0xFE,
        (
            "むむむ……屋台のお姉さん、\x01",
            "うちの母さんより\x01",
            "美人じゃないか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_799E")

    label("loc_7971")


    #C0343
    ChrTalk(
        0xFE,
        (
            "よおし、今日は\x01",
            "屋台を見て回るぞーっ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_799E")

    TalkEnd(0xFE)
    Return()

    # Function_35_77CD end

    def Function_36_79A2(): pass

    label("Function_36_79A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7A00")

    #C0344
    ChrTalk(
        0xFE,
        (
            "これからおっきな船にのって\x01",
            "ミシュラムに行くんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "……わ～い！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AE6")

    label("loc_7A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_7A3B")

    #C0346
    ChrTalk(
        0x22,
        "わーい、おにーちゃんありがと！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A3E")

    label("loc_7A3B")

    Call(0, 50)

    label("loc_7A3E")

    Jump("loc_7AE6")

    label("loc_7A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7A9A")

    #C0347
    ChrTalk(
        0xFE,
        "おまつり、おまつり～！\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "おまつりっていったら\x01",
            "パレードだよねー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE6")

    label("loc_7A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7ACA")

    #C0349
    ChrTalk(
        0xFE,
        "パパぁ、どうしちゃったの～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AE6")

    label("loc_7ACA")


    #C0350
    ChrTalk(
        0xFE,
        "わーい、おまつりだ～！\x02",
    )

    CloseMessageWindow()

    label("loc_7AE6")

    TalkEnd(0xFE)
    Return()

    # Function_36_79A2 end

    def Function_37_7AEA(): pass

    label("Function_37_7AEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7B4B")

    #C0351
    ChrTalk(
        0xFE,
        (
            "今日はミシュラムに行く人が\x01",
            "多いみたいだね。\x01",
            "オレも流れに乗ってみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CD6")

    label("loc_7B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7C0A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7BC9")

    #C0352
    ChrTalk(
        0xFE,
        (
            "中央広場の方で\x01",
            "窃盗犯が捕まったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "めでたい日に悪い事をする奴が\x01",
            "いるもんだなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C05")

    label("loc_7BC9")


    #C0354
    ChrTalk(
        0xFE,
        (
            "出店の人が\x01",
            "困ってるみたいだったよ。\x01",
            "何かあったのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C05")

    Jump("loc_7CD6")

    label("loc_7C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7C83")

    #C0355
    ChrTalk(
        0xFE,
        (
            "アイスにジュース、\x01",
            "ポップコーンに串焼き……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "祭りはいい……\x01",
            "道行く人みんなと\x01",
            "乾杯したい気分だよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CD6")

    label("loc_7C83")


    #C0357
    ChrTalk(
        0xFE,
        "祭りだ、祭りだ～っ！\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "今楽しまずしてどうする。\x01",
            "キミらもぱーっとやれよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CD6")

    TalkEnd(0xFE)
    Return()

    # Function_37_7AEA end

    def Function_38_7CDA(): pass

    label("Function_38_7CDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7D31")

    #C0359
    ChrTalk(
        0xFE,
        (
            "商工会の会長さんって\x01",
            "あれで切れ者らしいよ。\x01",
            "挨拶も楽しみだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE4")

    label("loc_7D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7D68")

    #C0360
    ChrTalk(
        0xFE,
        (
            "わわわ～っ！？\x01",
            "何だ君たちは～っ！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE4")

    label("loc_7D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7DE2")

    #C0361
    ChrTalk(
        0xFE,
        (
            "さっきのコンビも素晴らしかったが\x01",
            "この歌手も中々だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "どっちに点数を上げるか\x01",
            "迷ってしまうなぁ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE4")

    label("loc_7DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7E48")

    #C0363
    ChrTalk(
        0xFE,
        (
            "おお～、素晴らしい\x01",
            "パフォーマンスだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "これは点数の方も\x01",
            "期待させてくれるよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE4")

    label("loc_7E48")


    #C0365
    ChrTalk(
        0xFE,
        (
            "これから商工会主催の\x01",
            "ハッピークイズ大会があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "商品は豪華ミシュラム宿泊セット！\x01",
            "商工会の商品券も当たるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        "ふふふ、見逃せないねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_7EE4")

    TalkEnd(0xFE)
    Return()

    # Function_38_7CDA end

    def Function_39_7EE8(): pass

    label("Function_39_7EE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7F2D")

    #C0368
    ChrTalk(
        0xFE,
        "キャーッ、会長さんだ！\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        "がんばってーっ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8041")

    label("loc_7F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7F93")

    #C0370
    ChrTalk(
        0xFE,
        (
            "ええっ、この前の\x01",
            "不良たちじゃない！？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "なんでステージなんかに\x01",
            "来てるのよう！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8041")

    label("loc_7F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7FED")

    #C0372
    ChrTalk(
        0xFE,
        "今日は飛び込みＯＫなんですって！\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        "あたしも挑戦してみようかなぁ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8041")

    label("loc_7FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_801B")

    #C0374
    ChrTalk(
        0xFE,
        "キャー、頑張ってぇ～ッ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8041")

    label("loc_801B")


    #C0375
    ChrTalk(
        0xFE,
        "ゼッタイ当ててやるんだから～っ！\x02",
    )

    CloseMessageWindow()

    label("loc_8041")

    TalkEnd(0xFE)
    Return()

    # Function_39_7EE8 end

    def Function_40_8045(): pass

    label("Function_40_8045")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_807A")

    #C0376
    ChrTalk(
        0xFE,
        "今日でお祭りも終わりなのね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_81C2")

    label("loc_807A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_80B3")

    #C0377
    ChrTalk(
        0xFE,
        (
            "ちょ、ちょっと！？\x01",
            "どうなってるの！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81C2")

    label("loc_80B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_80F4")

    #C0378
    ChrTalk(
        0xFE,
        (
            "歌も上手かったけど……\x01",
            "美人なのが羨ましいわ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81C2")

    label("loc_80F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_817B")

    #C0379
    ChrTalk(
        0xFE,
        (
            "このステージは\x01",
            "クロスベル商工会が催してるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "参加者には出店で使える\x01",
            "割引チケットも出るの！\x01",
            "見逃せないわ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81C2")

    label("loc_817B")


    #C0381
    ChrTalk(
        0xFE,
        "あらら、豪華景品ですって！\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "これは参加しなきゃ\x01",
            "絶対ソンだわ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81C2")

    TalkEnd(0xFE)
    Return()

    # Function_40_8045 end

    def Function_41_81C6(): pass

    label("Function_41_81C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8228")

    #C0383
    ChrTalk(
        0xFE,
        (
            "お爺さんなのに\x01",
            "ちょっとカックイイ人ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        "あの人が会長さんだったんだ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_836B")

    label("loc_8228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_82A0")

    #C0385
    ChrTalk(
        0xFE,
        (
            "パレードの後に\x01",
            "あの人たちが乗り込んできたの！\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "パレードのイキオイで\x01",
            "火がついちゃったのかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_836B")

    label("loc_82A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_82EB")

    #C0387
    ChrTalk(
        0xFE,
        (
            "パレードまで時間あるもんね。\x01",
            "もうちょっと見ていこっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_836B")

    label("loc_82EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8319")

    #C0388
    ChrTalk(
        0xFE,
        "ママ、ちょっと意地汚いよ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_836B")

    label("loc_8319")


    #C0389
    ChrTalk(
        0xFE,
        (
            "昨日はライブがすっごかったけど、\x01",
            "今日もなにかやってるみたいよ。\x01",
            "楽しみねっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_836B")

    TalkEnd(0xFE)
    Return()

    # Function_41_81C6 end

    def Function_42_836F(): pass

    label("Function_42_836F")

    TalkBegin(0xFE)

    #C0390
    ChrTalk(
        0xFE,
        "ようやく待ちに待ったミシュラムよ㈱\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "たった１０分の待ち時間が\x01",
            "長く感じちゃうわね～㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_836F end

    def Function_43_83D3(): pass

    label("Function_43_83D3")

    TalkBegin(0xFE)

    #C0392
    ChrTalk(
        0xFE,
        (
            "ドキドキ……\x01",
            "彼女とミシュラムに行くんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "最終日はミシュラムへ！\x01",
            "ここ２、３年の定番だよね？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_83D3 end

    def Function_44_8442(): pass

    label("Function_44_8442")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_84A7")

    #C0394
    ChrTalk(
        0xFE,
        (
            "うーん、やっぱり\x01",
            "アイスかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "でもパパなら\x01",
            "タンメンの方がスキかも……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_854F")

    label("loc_84A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_84FC")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0396
    ChrTalk(
        0xFE,
        "あ、あのね……\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        "パレード、すごかったよ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_854F")

    label("loc_84FC")


    #C0398
    ChrTalk(
        0xFE,
        "今日はママとお出掛けなの。\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "えへへ……ママと\x01",
            "遊びに来るの、ひさしぶり……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_854F")

    TalkEnd(0xFE)
    Return()

    # Function_44_8442 end

    def Function_45_8553(): pass

    label("Function_45_8553")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_85AD")

    #C0400
    ChrTalk(
        0xFE,
        (
            "主人に何か\x01",
            "お土産を買って帰らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        "何がいいかしらねぇ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_871A")

    label("loc_85AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_862E")

    #C0402
    ChrTalk(
        0xFE,
        (
            "アルカンシェルを\x01",
            "見れなかったのは残念だけど\x01",
            "パレードは楽しめたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "ふふ、来年は\x01",
            "主人も誘ってこようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_871A")

    label("loc_862E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_867C")

    #C0404
    ChrTalk(
        0xFE,
        "モモ、次はどこに行く？\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        "あのお店なんか行ってみようか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_871A")

    label("loc_867C")

    TurnDirection(0xFE, 0x0, 0)

    #C0406
    ChrTalk(
        0xFE,
        (
            "ふふ、店は夫に任せて\x01",
            "娘と出てきちゃったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "折角だし家族でって\x01",
            "言ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "あの人、騒ぐのは\x01",
            "肌に合わないらしいから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xB4, 0x0)
    SetScenarioFlags(0x1, 7)

    label("loc_871A")

    TalkEnd(0xFE)
    Return()

    # Function_45_8553 end

    def Function_46_871E(): pass

    label("Function_46_871E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_886A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_87AD")

    #C0409
    ChrTalk(
        0xFE,
        (
            "ふう、私は港湾公園の\x01",
            "警備を続行するのみです。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "悔しいですが……\x01",
            "ミシュラムの件は\x01",
            "一課でも黙過事項ですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8865")

    label("loc_87AD")


    #C0411
    ChrTalk(
        0xFE,
        (
            "今日はミシュラム行きの\x01",
            "客が多いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#0001F（やっぱり\x01",
            "  《黒の競売会》の事は\x01",
            "  掴んでるのかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        "#0101F（ええ、捜査一課だものね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_8865")

    Jump("loc_8C5B")

    label("loc_886A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 6)), scpexpr(EXPR_END)), "loc_89E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_88E6")

    #C0415
    ChrTalk(
        0xFE,
        (
            "私が警戒に当たっていることは\x01",
            "一応市民には伏せられた事項です。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        "あまり話しかけないで下さい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_89E3")

    label("loc_88E6")


    #C0417
    ChrTalk(
        0xFE,
        (
            "私が警戒に当たっていることは\x01",
            "一応市民には伏せられた事項です。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "あまり話しかけないで下さい。\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        (
            "#0003F（そういや……\x01",
            "  昨日ライブに来た時も\x01",
            "  気付かなかったな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x104,
        (
            "#0300F（気配を消して監視や尾行するのは\x01",
            "  捜査一課の十八番みてえだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_89E3")

    Jump("loc_8C5B")

    label("loc_89E8")


    #C0421
    ChrTalk(
        0xFE,
        (
            "特務支援課……\x01",
            "またウロウロしているようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0422
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、あなたは確か\x01",
            "一課の捜査官の……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        "#0300Fこんな所で記念祭の警備ッスか？\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "……創立記念祭には\x01",
            "無防備な群集が各地に出現します。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "加えて内外から訪れる\x01",
            "多数の有力者や資産家……\x01",
            "テロの可能性も拭えませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x102,
        (
            "#0100Fその警戒のために……\x01",
            "一課も大変ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "ええ、それは勿論。\x01",
            "あなた方と違って\x01",
            "お気楽な部署ではありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0428
    ChrTalk(
        0x103,
        "#0200F（微妙にイヤミ臭い人ですね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 6)

    label("loc_8C5B")

    TalkEnd(0xFE)
    Return()

    # Function_46_871E end

    def Function_47_8C5F(): pass

    label("Function_47_8C5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_8CDE")

    #C0429
    ChrTalk(
        0xFE,
        (
            "自分の才能のなさを突きつけられ、\x01",
            "サイフまで落として……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        "……僕が何をしたっていうんだろう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D8E")

    label("loc_8CDE")


    #C0431
    ChrTalk(
        0xFE,
        (
            "今日、リベールに帰ろうと\x01",
            "思ってたんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "どうやらサイフを\x01",
            "落としてしまったみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "……僕が何をしたっていうんだろう。\x01",
            "空の女神は僕が嫌いなのかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_8D8E")

    Jump("loc_92A9")

    label("loc_8D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_8E1A")

    #C0434
    ChrTalk(
        0xFE,
        (
            "……ポエマーとしての活動は\x01",
            "もうやめることにするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "ちょっと早いけど……\x01",
            "もうリベールに帰ろうかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8ECA")

    label("loc_8E1A")


    #C0436
    ChrTalk(
        0xFE,
        (
            "みんな、僕のポエムを聞くと\x01",
            "小首をかしげて去っていくんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "僕には創作の才能は\x01",
            "なかったってことなのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "……ポエマーとしての活動は\x01",
            "もうやめることにするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_8ECA")

    Jump("loc_92A9")

    label("loc_8ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_907A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_8F66")

    #C0439
    ChrTalk(
        0xFE,
        (
            "……さっきから、\x01",
            "誰も僕のポエムを\x01",
            "聞いてくれないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "ちくしょう、１人くらい\x01",
            "感動してくれても\x01",
            "いいじゃないかっ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9075")

    label("loc_8F66")


    #C0441
    ChrTalk(
        0xFE,
        (
            "君、よかったら\x01",
            "僕の作ったポエムを\x01",
            "聞いていかないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "旅はかきすて世は情け……\x01",
            "諸行無常の響きあり……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xFE,
        "……どうだい？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0444
    ChrTalk(
        0x101,
        "#0003F（……ポエムか、これ？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_9075")

    Jump("loc_92A9")

    label("loc_907A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_922C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_9111")

    #C0445
    ChrTalk(
        0xFE,
        (
            "自分を変えるためには、\x01",
            "自分から動かなきゃダメなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "……それは分かってるんだけど、\x01",
            "どうすればいいかは分からないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9227")

    label("loc_9111")


    #C0447
    ChrTalk(
        0xFE,
        (
            "クロスベルに来て、\x01",
            "もう３日が経とうとしてる。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "こんなにも賑やかな場所なのに、\x01",
            "僕のぼんやり過ごす日々は\x01",
            "いまだ変わる気配を見せないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "ひさかたの、光のどけきダメな日々……\x01",
            "頑張れアントンここにあり……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "……やっぱりポエムはいいな。\x01",
            "少しだけ元気が出てきたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_9227")

    Jump("loc_92A9")

    label("loc_922C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_92A6")

    #C0451
    ChrTalk(
        0xFE,
        (
            "仕事も無い、彼女もいない。\x01",
            "ぼんやりした僕の人生……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "このクロスベルの旅で\x01",
            "何かが起こればいいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92A9")

    label("loc_92A6")

    Call(0, 49)

    label("loc_92A9")

    TalkEnd(0xFE)
    Return()

    # Function_47_8C5F end

    def Function_48_92AD(): pass

    label("Function_48_92AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9337")
    OP_93(0x20, 0xB4, 0x0)

    #C0453
    ChrTalk(
        0xFE,
        (
            "アントン、悲観的に\x01",
            "なりすぎるのは悪い癖だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "落し物なんて、忘れた頃に\x01",
            "意外なところから出てくるものさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_9337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_94C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_93F1")
    OP_93(0x20, 0x87, 0x0)

    #C0455
    ChrTalk(
        0xFE,
        (
            "おっ、見ろよアントン。\x01",
            "ステージが面白いことになってるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        (
            "飛び入り参加して、\x01",
            "思いっきり歌ってきらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        "淀んだ気分が晴れるかもしれないぞ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_94C3")

    label("loc_93F1")


    #C0458
    ChrTalk(
        0xFE,
        (
            "アントンは、朝からここに立って\x01",
            "道行く人にポエムを贈っていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "結果は見ての通りだよ。\x01",
            "すっかり打ちひしがれてしまったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        (
            "……さて、そろそろ腹も減ったし\x01",
            "今から出店でも回るとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)

    label("loc_94C3")

    Jump("loc_97A2")

    label("loc_94C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9592")

    #C0461
    ChrTalk(
        0xFE,
        (
            "今朝、突然アントンが\x01",
            "路上ポエマーなんてものを\x01",
            "やりたいって言い出したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "ま、アントンのことだから\x01",
            "すぐに飽きると思うけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        (
            "俺はただ、いつもどおり\x01",
            "生暖かく見守るだけさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_9592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_96F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_9616")
    OP_93(0x20, 0xB4, 0x0)

    #C0464
    ChrTalk(
        0xFE,
        (
            "アントン、やりたいことが\x01",
            "決まったら呼んでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "それまで向こうのベンチで\x01",
            "昼寝してるからさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96EF")

    label("loc_9616")


    #C0466
    ChrTalk(
        0xFE,
        (
            "アントンは少し前に失恋してから\x01",
            "ポエマーを目指すことにしたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "それが、飽き性のわりに\x01",
            "意外と続いているみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xFE,
        (
            "上手いかどうかはさておき、\x01",
            "それで生活しようと考えないのは\x01",
            "実にアントンらしいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)

    label("loc_96EF")

    Jump("loc_97A2")

    label("loc_96F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_978E")

    #C0469
    ChrTalk(
        0xFE,
        (
            "アントンの自分探しに付き合って、\x01",
            "はるばるリベールから訪れたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        (
            "ここでは何をするんだろうな。\x01",
            "アントンといると本当に飽きないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_978E")

    Call(0, 49)
    TurnDirection(0x20, 0x0, 0)
    OP_93(0x20, 0xB4, 0x0)
    SetScenarioFlags(0x2, 2)

    label("loc_97A2")

    TalkEnd(0xFE)
    Return()

    # Function_48_92AD end

    def Function_49_97A6(): pass

    label("Function_49_97A6")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0x20, 0xB4, 0x0)

    #C0471
    ChrTalk(
        0x1F,
        (
            "自分を探すため、\x01",
            "ついにこんな所にまで\x01",
            "足を伸ばしてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x1F,
        (
            "にぎやかでいい所だなぁ、\x01",
            "クロスベルは……\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x1F,
        (
            "……なあリックス。\x01",
            "ここならきっと、僕の求めるものが\x01",
            "あると思わないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x20,
        "さぁ、俺にはなんとも言えないな。\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x20,
        (
            "逸る気持ちは分かるけど\x01",
            "落ち着けよ、アントン。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetScenarioFlags(0x2, 1)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_49_97A6 end

    def Function_50_98E1(): pass

    label("Function_50_98E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9AD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_9949")

    #C0476
    ChrTalk(
        0x2E,
        (
            "#1601Fチッ、気をつけとけ。\x01",
            "うっかり蹴っ飛ばしちまう\x01",
            "所だったじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD2")

    label("loc_9949")

    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)

    #C0477
    ChrTalk(
        0x2E,
        (
            "#1601Fオイガキ、\x01",
            "ぶつかってんじゃねえぞ……\x02\x03",

            "#1607Fそれと財布落としたぞ。\x01",
            "どこまで抜けてんだ、アア？\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x22,
        "あ、ボクのおさいふだー。\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x22,
        "わーい、ありがと！\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x21,
        "はわわわ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0481
    ChrTalk(
        0x101,
        "#0005F（な、何をやってるんだ……？）\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x104,
        (
            "#0306F（まあ、絡んでるわけじゃ\x01",
            "  なさそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    OP_4C(0x21, 0xFF)
    OP_4C(0x22, 0xFF)

    label("loc_9AD2")

    Jump("loc_9B71")

    label("loc_9AD7")


    #C0483
    ChrTalk(
        0x2E,
        (
            "#1600Fオウ、お前らは仕事か？\x02\x03",

            "#1602Fクク……サツも大変だな。\x01",
            "お疲れさんなこった。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        (
            "#0006Fはぁ、同情するんだったら\x01",
            "騒ぎは起こさないでくれよ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B71")

    TalkEnd(0xFE)
    Return()

    # Function_50_98E1 end

    def Function_51_9B75(): pass

    label("Function_51_9B75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9C20")

    #C0485
    ChrTalk(
        0x2F,
        (
            "イ～ヤッホウッッ！\x01",
            "オレに歌わせな～～ッ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x2F,
        (
            "飛び入り、参加、誰でも、ＯＫ！\x01",
            "飛び入り、参加、誰でも、ＯＫッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x2F,
        "……イィィ～～ヤッホウッッ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C70")

    label("loc_9C20")


    #C0488
    ChrTalk(
        0x2F,
        "ひゃひゃひゃ～っ！\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x2F,
        (
            "見ろよ～、\x01",
            "あんなちっちぇえ子が\x01",
            "出店やってンぞ～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C70")

    TalkEnd(0xFE)
    Return()

    # Function_51_9B75 end

    def Function_52_9C74(): pass

    label("Function_52_9C74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_9CDC")
    OP_4B(0x14, 0xFF)

    #C0490
    ChrTalk(
        0x30,
        "ルガノフが歌うと言ってやがるんだ。\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x30,
        "黙って聴いてろやボケが。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_9CDF")

    label("loc_9CDC")

    Call(0, 53)

    label("loc_9CDF")

    Jump("loc_9D24")

    label("loc_9CE4")


    #C0492
    ChrTalk(
        0x30,
        "サツが妙にウロウロしてやがるな。\x02",
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x30,
        "今日は何かあるのか？\x02",
    )

    CloseMessageWindow()

    label("loc_9D24")

    TalkEnd(0xFE)
    Return()

    # Function_52_9C74 end

    def Function_53_9D28(): pass

    label("Function_53_9D28")

    OP_4B(0x30, 0xFF)
    OP_4B(0x14, 0xFF)

    #C0494
    ChrTalk(
        0x14,
        (
            "うおお、また何をやってるんだ\x01",
            "あんた達はーっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x14,
        (
            "すぐにステージから降りろっ！\x01",
            "降りてくれ～っ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x30,
        "うっせえ、黙ってろやボケが。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0x14, 0x30, 500)
    Sleep(300)

    #C0497
    ChrTalk(
        0x14,
        "ひいい、何をするんだ～っ！？\x02",
    )

    CloseMessageWindow()
    OP_64(0x14)
    OP_93(0x14, 0x0, 0x0)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x30, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_53_9D28 end

    def Function_54_9E16(): pass

    label("Function_54_9E16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9E69")

    #C0498
    ChrTalk(
        0x31,
        "下がれっつってんだよコラァ！\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x31,
        "邪魔するとぶっ飛ばすぞォ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F3E")

    label("loc_9E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_9EA4")

    #C0500
    ChrTalk(
        0x31,
        (
            "ヴァルドさん、\x01",
            "今日はどっちに行きます？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F3E")

    label("loc_9EA4")


    #C0501
    ChrTalk(
        0x31,
        (
            "おうおう、今日は一段と\x01",
            "盛り上がってんじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x31,
        (
            "……ヴァルドさん、\x01",
            "今日はどっちに行きます？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x31,
        (
            "坂の方が見晴らしが\x01",
            "いいかもしれませんぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)

    label("loc_9F3E")

    TalkEnd(0xFE)
    Return()

    # Function_54_9E16 end

    def Function_55_9F42(): pass

    label("Function_55_9F42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9FAC")

    #C0504
    ChrTalk(
        0x32,
        (
            "このガキ、ヴァルドさんに\x01",
            "ぶつかって来やがってよォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x32,
        "ハァ、鉄砲玉のつもりかァ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A010")

    label("loc_9FAC")


    #C0506
    ChrTalk(
        0x32,
        (
            "……おお！？\x01",
            "出店のねーちゃん、美人じゃねえ？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x32,
        (
            "よォよォねーちゃん、\x01",
            "後で俺と回んねえ～っ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A010")

    TalkEnd(0xFE)
    Return()

    # Function_55_9F42 end

    def Function_56_A014(): pass

    label("Function_56_A014")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0508
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(63790, 0, 7940, 1500)
    MoveCamera(45, 23, 0, 1500)
    OP_6E(280, 1500)
    SetCameraDistance(29000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0509
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E3")
    OP_E0(0x2)
    MiniGame(0x6, 0x1, 0x10BE4, 0xFFFFF63C, 0x4074, 0xB4, 0x109C8, 0xFFFFF254, 0x2E2C)

    label("loc_A0E3")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_56_A014 end

    def Function_57_A0E8(): pass

    label("Function_57_A0E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A722")
    EventBegin(0x0)
    Fade(1000)
    OP_68(34650, -1200, -280, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14510, 0)
    SetChrPos(0x101, 35000, -2500, 0, 90)
    SetChrPos(0x102, 33600, -2500, -800, 90)
    SetChrPos(0x103, 34000, -2500, 800, 90)
    SetChrPos(0x104, 32600, -2500, 0, 90)
    OP_0D()

    #C0510
    ChrTalk(
        0x102,
        (
            "#0100F#6Pどうする、ロイド？\x02\x03",

            "もう、水上バスに乗って\x01",
            "ミシュラムへ行ってしまう？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0511
    ChrTalk(
        0x101,
        "#0003F#11Pそうだな……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ用事がある】\x01",                    # 0
            "【水上バスでミシュラムに向かう】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A255"),
        (1, "loc_A467"),
        (SWITCH_DEFAULT, "loc_A71D"),
    )


    label("loc_A255")


    #C0512
    ChrTalk(
        0x101,
        (
            "#0000F#11P一度、ミシュラムに渡ったら\x01",
            "他の仕事は出来なくなりそうだ。\x02\x03",

            "頻繁に出ているみたいだし、\x01",
            "一通り用事を済ませてから乗ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x102,
        "#0100F#6Pそうね……\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x103,
        (
            "#0202F#1P買い物や工房での調整も\x01",
            "済ませた方が良さそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x104,
        (
            "#0300F#6Pそんじゃま、用事が済んだら\x01",
            "またここに来るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0516
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水上バスに乗る場合、\x01",
            "すぐ近くの時刻表を調べてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0517
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なお、一度ミシュラムに向かうと\x01",
            "記念祭中の支援要請は全て\x01",
            "終了してしまうので注意が必要です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 34000, -2500, 0, 270)
    EventEnd(0x5)
    Jump("loc_A71D")

    label("loc_A467")


    #C0518
    ChrTalk(
        0x101,
        (
            "#0000F#11Pよし……\x01",
            "それじゃあ水上バスを待とう。\x02\x03",

            "#0006F……今更ながら\x01",
            "浮いた格好な気がしてきたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x102,
        (
            "#0106F#6Pそれもそうね……\x02\x03",

            "#0108Fフォーマルな格好で\x01",
            "行った方がよかったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x104,
        (
            "#0303F#6Pま、パーティに乗り込めると\x01",
            "決まったわけじゃねえしな。\x02\x03",

            "#0300Fテーマパーク目当ての観光客に\x01",
            "紛れていいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0521
    ChrTalk(
        0x103,
        (
            "#0203F#5P……それでもわたしは\x01",
            "やや浮いているかと思いますが。\x02\x03",

            "#0202Fいっそ《みっしぃ》のパジャマでも\x01",
            "着て行けばよかったでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A63B():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A63B)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0522
    ChrTalk(
        0x101,
        (
            "#0012F#11Pいや……\x01",
            "さすがに目立ちすぎだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x102,
        (
            "#0109F#12Pいくらテーマパークの\x01",
            "マスコットキャラでもね……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_65(0x0, 0x1)
    Call(0, 59)
    Jump("loc_A71D")

    label("loc_A71D")

    Jump("loc_A7DA")

    label("loc_A722")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0524
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《ミシュラム》行き水上バス・時刻表\x01\x01",
            "※ミシュラムが誇るテーマパーク\x01",
            "  『ワンダーランド』開園中！\x01",
            "  楽しいひと時をお楽しみ下さい！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_A7DA")

    Return()

    # Function_57_A0E8 end

    def Function_58_A7DB(): pass

    label("Function_58_A7DB")

    EventBegin(0x0)
    Fade(1000)
    OP_68(34650, -1200, -280, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14510, 0)
    SetChrPos(0x101, 35000, -2500, 0, 90)
    SetChrPos(0x102, 33600, -2500, -800, 90)
    SetChrPos(0x103, 34000, -2500, 800, 90)
    SetChrPos(0x104, 32600, -2500, 0, 90)
    OP_0D()

    #C0525
    ChrTalk(
        0x101,
        (
            "#0008F#5P水上バスの乗り場……\x02\x03",

            "#0001Fここから《ミシュラム》に\x01",
            "行くことができるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x102,
        (
            "#0100F#6Pええ、３０分に１本は\x01",
            "運航していると思ったけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)

    def lambda_A8FF():

        label("loc_A8FF")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_A8FF")

    QueueWorkItem2(0x101, 1, lambda_A8FF)

    def lambda_A911():

        label("loc_A911")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_A911")

    QueueWorkItem2(0x102, 1, lambda_A911)

    def lambda_A923():

        label("loc_A923")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_A923")

    QueueWorkItem2(0x104, 1, lambda_A923)

    def lambda_A935():
        OP_95(0xFE, 34000, -2500, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A935)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0527
    ChrTalk(
        0x103,
        (
            "#0200F#5P記念祭の間は、２０分に\x01",
            "１本出ているみたいですね。\x02\x03",

            "最終は夜の１２時半みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x101,
        "#0005F#12Pそんな遅くまで出ているのか……\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_A9EB():
        OP_95(0xFE, 34000, -2500, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A9EB)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_AA15():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA15)

    def lambda_AA22():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA22)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    #C0529
    ChrTalk(
        0x104,
        (
            "#0304F#6Pまあ、テーマパークで遊んでから\x01",
            "レストランでディナーと洒落込んだら\x01",
            "どうしても遅くなっちまうしな。\x02\x03",

            "#0300Fミシュラムにあるホテルなんざ\x01",
            "普通は高くて泊まれないだろうし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0530
    ChrTalk(
        0x102,
        (
            "#0106F#6Pそれでも今の時期は\x01",
            "満室の可能性が高いでしょうね。\x02\x03",

            "#0100F──どうする、ロイド？\x02\x03",

            "もう、水上バスに乗って\x01",
            "ミシュラムへ行ってしまう？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0531
    ChrTalk(
        0x101,
        "#0003F#11Pそうだな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xA3, 4)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ用事がある】\x01",                    # 0
            "【水上バスでミシュラムに向かう】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AC12"),
        (1, "loc_AE2D"),
        (SWITCH_DEFAULT, "loc_B0DF"),
    )


    label("loc_AC12")


    #C0532
    ChrTalk(
        0x101,
        (
            "#0000F#11P一度、ミシュラムに渡ったら\x01",
            "他の仕事は出来なくなりそうだ。\x02\x03",

            "頻繁に出ているみたいだし、\x01",
            "一通り用事を済ませてから乗ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x102,
        "#0100F#6Pそうね……\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x103,
        (
            "#0202F#1P買い物や工房での調整も\x01",
            "済ませた方が良さそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x104,
        (
            "#0300F#6Pそんじゃま、用事が済んだら\x01",
            "またここに来るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0536
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水上バスに乗る場合、\x01",
            "すぐ近くの時刻表を調べてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0537
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なお、一度ミシュラムに向かうと\x01",
            "記念祭中の支援要請は全て\x01",
            "終了してしまうので注意が必要です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 34000, -2500, 0, 270)
    ModifyEventFlags(0, 0, 0x80)
    OP_66(0x0, 0x1)
    EventEnd(0x5)
    Jump("loc_B0DF")

    label("loc_AE2D")


    #C0538
    ChrTalk(
        0x101,
        (
            "#0000F#11Pよし……\x01",
            "それじゃあ水上バスを待とう。\x02\x03",

            "#0006F……今更ながら\x01",
            "浮いた格好な気がしてきたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x102,
        (
            "#0106F#6Pそれもそうね……\x02\x03",

            "#0108Fフォーマルな格好で\x01",
            "行った方がよかったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x104,
        (
            "#0303F#6Pま、パーティに乗り込めると\x01",
            "決まったわけじゃねえしな。\x02\x03",

            "#0300Fテーマパーク目当ての観光客に\x01",
            "紛れていいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0541
    ChrTalk(
        0x103,
        (
            "#0203F#5P……それでもわたしは\x01",
            "やや浮いているかと思いますが。\x02\x03",

            "#0202Fいっそ《みっしぃ》のパジャマでも\x01",
            "着て行けばよかったでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B001():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B001)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0542
    ChrTalk(
        0x101,
        (
            "#0012F#11Pいや……\x01",
            "さすがに目立ちすぎだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x102,
        (
            "#0109F#12Pいくらテーマパークの\x01",
            "マスコットキャラでもね……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 59)
    Jump("loc_B0DF")

    label("loc_B0DF")

    Return()

    # Function_58_A7DB end

    def Function_59_B0E0(): pass

    label("Function_59_B0E0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x32)
    LoadChrToIndex("chr/ch07300.itc", 0x33)
    SoundLoad(479)
    OP_93(0xF, 0x87, 0x0)
    OP_4B(0xF, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)
    OP_4B(0x28, 0xFF)
    OP_4B(0x29, 0xFF)
    SetChrPos(0x21, 41400, -2500, -3400, 0)
    SetChrPos(0x22, 40300, -2500, -3400, 0)
    SetChrPos(0x28, 41400, -2500, -4700, 0)
    SetChrPos(0x29, 40300, -2500, -4700, 0)
    SetChrPos(0x101, 40300, -2500, -6000, 0)
    SetChrPos(0x102, 41400, -2500, -6000, 0)
    SetChrPos(0x103, 40300, -2500, -7300, 0)
    SetChrPos(0x104, 41400, -2500, -7300, 0)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrChipByIndex(0x44, 0xE)
    SetChrChipByIndex(0x45, 0xF)
    SetChrChipByIndex(0x46, 0x10)
    SetChrChipByIndex(0x47, 0x11)
    SetChrChipByIndex(0x48, 0x12)
    SetChrChipByIndex(0x49, 0x13)
    SetChrChipByIndex(0x4A, 0x14)
    SetChrChipByIndex(0x4B, 0x15)
    SetChrChipByIndex(0x4C, 0x16)
    SetChrChipByIndex(0x4D, 0x17)
    SetChrSubChip(0x44, 0x0)
    SetChrSubChip(0x45, 0x0)
    SetChrSubChip(0x46, 0x0)
    SetChrSubChip(0x47, 0x0)
    SetChrSubChip(0x48, 0x0)
    SetChrSubChip(0x49, 0x0)
    SetChrSubChip(0x4A, 0x0)
    SetChrSubChip(0x4B, 0x0)
    SetChrSubChip(0x4C, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x44, 0x4)
    ClearChrFlags(0x45, 0x4)
    ClearChrFlags(0x46, 0x4)
    ClearChrFlags(0x47, 0x4)
    ClearChrFlags(0x48, 0x4)
    ClearChrFlags(0x49, 0x4)
    ClearChrFlags(0x4A, 0x4)
    ClearChrFlags(0x4B, 0x4)
    ClearChrFlags(0x4C, 0x4)
    ClearChrFlags(0x4D, 0x4)
    SetChrPos(0x44, 48000, -2500, -1250, 270)
    SetChrPos(0x45, 48000, -2500, -2250, 270)
    SetChrPos(0x46, 48000, -2500, -1250, 270)
    SetChrPos(0x47, 48000, -2500, -2250, 270)
    SetChrPos(0x48, 48000, -2500, -1250, 270)
    SetChrPos(0x49, 48000, -2500, -2250, 270)
    SetChrPos(0x4A, 48000, -2500, -1250, 270)
    SetChrPos(0x4B, 48000, -2500, -2250, 270)
    SetChrPos(0x4C, 48000, -2500, -1250, 270)
    SetChrPos(0x4D, 48000, -2500, -2250, 270)
    OP_A7(0x44, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x45, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x46, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x47, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x48, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x49, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0x46, 0x80)
    ClearChrBattleFlags(0x46, 0x8000)
    ClearChrFlags(0x47, 0x80)
    ClearChrBattleFlags(0x47, 0x8000)
    ClearChrFlags(0x48, 0x80)
    ClearChrBattleFlags(0x48, 0x8000)
    ClearChrFlags(0x49, 0x80)
    ClearChrBattleFlags(0x49, 0x8000)
    ClearChrFlags(0x4A, 0x80)
    ClearChrBattleFlags(0x4A, 0x8000)
    ClearChrFlags(0x4B, 0x80)
    ClearChrBattleFlags(0x4B, 0x8000)
    ClearChrFlags(0x4C, 0x80)
    ClearChrBattleFlags(0x4C, 0x8000)
    ClearChrFlags(0x4D, 0x80)
    ClearChrBattleFlags(0x4D, 0x8000)
    SetChrChipByIndex(0x34, 0x32)
    SetChrSubChip(0x34, 0x0)
    SetChrPos(0x34, 33000, -2500, -1500, 90)
    SetChrFlags(0x34, 0x8000)
    ClearChrFlags(0x34, 0x80)
    ClearChrBattleFlags(0x34, 0x8000)
    SetChrChipByIndex(0x33, 0x33)
    SetChrSubChip(0x33, 0x0)
    SetChrPos(0x33, 33000, -2500, -1500, 90)
    SetChrFlags(0x33, 0x8000)
    ClearChrFlags(0x35, 0x80)
    OP_78(0x9, 0x35)
    OP_49()
    OP_D3(0x35, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    SetChrPos(0x35, 51800, -3850, -4000, 0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x9, 0x4)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03500.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    OP_68(35100, 1000, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7518", 0)
    FadeToBright(1000, 0)
    OP_68(35100, 0, -7650, 3000)
    OP_6F(0x1)
    OP_0D()

    #N0544
    NpcTalk(
        0x34,
        "軽そうな声",
        (
            "ん～……？\x01",
            "こっちでいいのかねェ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B578():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B578)

    def lambda_B585():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B585)
    Sleep(100)

    def lambda_B595():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B595)

    def lambda_B5A2():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B5A2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    OP_68(37000, -1300, -5750, 0)
    OP_68(38150, -1300, -5750, 2000)
    MoveCamera(360, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15600, 0)
    OP_93(0x101, 0x13B, 0x0)
    OP_93(0x102, 0x13B, 0x0)
    OP_93(0x103, 0x13B, 0x0)
    OP_93(0x104, 0x13B, 0x0)

    def lambda_B61F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_B61F)
    WaitChrThread(0x34, 1)
    OP_6F(0x79)
    OP_0D()

    #C0545
    ChrTalk(
        0x101,
        "#0005F#6P（観光客……？）\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        (
            "#0100F#12P（ええ、いかにも\x01",
            "  そんな感じの人みたいね……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x34, 0x2D, 0x1F4)
    Sleep(200)
    TurnDirection(0x34, 0x101, 500)
    Sleep(200)
    OP_68(39450, -1300, -5400, 2000)

    def lambda_B6BE():
        OP_95(0xFE, 39030, -2500, -4320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_B6BE)
    WaitChrThread(0x34, 1)
    OP_6F(0x79)
    Sleep(200)

    #N0547
    NpcTalk(
        0x34,
        "軽そうな青年",
        (
            "#3500F#5Pよー、彼氏たち。\x02\x03",

            "ちょいと訊ねたいんだけど\x01",
            "構わないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        (
            "#0000F#12Pええ、いいですよ。\x02\x03",

            "観光客の方みたいですけど\x01",
            "道に迷いましたか？\x02",
        )
    )

    CloseMessageWindow()

    #N0549
    NpcTalk(
        0x34,
        "軽そうな青年",
        (
            "#3506F#5Pああ、この街\x01",
            "ちょっと広すぎるんだよな～。\x02\x03",

            "#3500Fそんでさ、ミシュラムって場所に\x01",
            "行きたいんだが、こっちでいいのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0550
    ChrTalk(
        0x101,
        (
            "#0005F#12Pああ、こっちでいいですよ。\x02\x03",

            "#0000F俺たちも丁度、\x01",
            "ミシュラムに行く水上バスを\x01",
            "待っているところなんで。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #N0551
    NpcTalk(
        0x34,
        "軽そうな青年",
        (
            "#3502F#5Pお、ビンゴだったか。\x02\x03",

            "#3504Fそんじゃあオレも\x01",
            "並ばせてもらおうかねぇ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0552
    NpcTalk(
        0x34,
        "軽そうな青年",
        "#3505F#5Pおっと、名乗り忘れてたな。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("軽そうな青年")

    #A0553
    AnonymousTalk(
        0xFF,
        (
            "オレの名前はレクター。\x01",
            "レクター・アランドールだ。\x02\x03",

            "エレボニアの帝都から\x01",
            "さっき鉄道で着いたばかりだぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0554
    ChrTalk(
        0x101,
        "#0005F#12Pエレボニアの帝都……\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x102,
        "#0100F#12P帝国の方だったんですか……\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x104,
        (
            "#0300F#12Pへえ、それにしちゃあ\x01",
            "なかなかイカした格好してんな。\x02\x03",

            "サングラスなんざかけて\x01",
            "もろにバカンス仕様じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x34,
        (
            "#3509F#5Pおう、クロスベルっていやぁ\x01",
            "最近リゾートでも有名だからな！\x02\x03",

            "郷に入れば郷に従え。\x01",
            "これでも気合入れて来たんだぜ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x103,
        (
            "#0206F#6P気合いを入れる方向が\x01",
            "間違っている気もしますが……\x02\x03",

            "#0202Fやっぱりテーマパーク目当てで\x01",
            "いらっしゃったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0559
    ChrTalk(
        0x34,
        (
            "#3505F#5Pテーマパーク？\x02\x03",

            "#3501F……なんだそりゃ。\x01",
            "そんな面白いモンが\x01",
            "ミシュラムにはあんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x101,
        (
            "#0012F#12Pええ、まあ……\x01",
            "俺も行ったことないですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x102,
        (
            "#0109F#12P元々、保養地でしたけれど\x01",
            "最近ではそちらの方が有名ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x34,
        (
            "#3500F#5Pへ～、なるほどねェ。\x02\x03",

            "#3506Fまあ今回は、ただの代理として\x01",
            "出席しに来ただけだからな。\x02\x03",

            "もうちょい色々と調べてから\x01",
            "来りゃあよかったかもなァ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0563
    ChrTalk(
        0x101,
        "#0001F#12P代理として出席……？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(475, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x34, 0x5A, 0x1F4)

    #C0564
    ChrTalk(
        0x34,
        "#3502F#6Pお、来たみたいだなァ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_93(0xF, 0xB4, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    SetChrPos(0x35, 126220, -3850, -50690, 315)
    OP_D3(0x35, 0x0, 0x4CE78, 0x0, 0x0)
    BeginChrThread(0x53, 1, 0, 64)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x0, 0x1)
    OP_68(59280, 17600, -8870, 0)
    MoveCamera(90, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(51010, 0)
    OP_68(59280, 8000, -8870, 10000)

    def lambda_BF84():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_BF84)
    OP_0D()
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x1, 0x1)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_93(0x101, 0x2D, 0x0)
    OP_93(0x102, 0x2D, 0x0)
    OP_93(0x103, 0x2D, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x34, 0x2D, 0x0)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    OP_D3(0x35, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x35, 54800, -3850, -4000, 0)
    Sound(476, 0, 100, 0)
    Sound(477, 0, 100, 0)

    def lambda_C058():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_C058)
    WaitChrThread(0x35, 1)
    OP_82(0x32, 0x0, 0xBB8, 0x1F4)
    Sound(478, 0, 100, 0)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x12D, 0x168, 0x0, 0x20)
    OP_71(0x9, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x9)
    OP_71(0x9, 0xF1, 0x12C, 0x0, 0x20)
    Sleep(500)
    BeginChrThread(0x44, 3, 0, 60)
    Sleep(280)
    BeginChrThread(0x45, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x46, 3, 0, 60)
    Sleep(150)
    BeginChrThread(0x47, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x48, 3, 0, 60)
    Sleep(150)
    BeginChrThread(0x49, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x4A, 3, 0, 60)
    Sleep(50)
    BeginChrThread(0x4B, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x4C, 3, 0, 60)
    Sleep(180)
    BeginChrThread(0x4D, 3, 0, 60)
    Sleep(5000)
    BeginChrThread(0x21, 3, 0, 61)
    Sleep(150)
    BeginChrThread(0x22, 3, 0, 62)
    Sleep(800)
    BeginChrThread(0x28, 3, 0, 61)
    Sleep(200)
    BeginChrThread(0x29, 3, 0, 62)
    Sleep(2000)
    EndChrThread(0x44, 0x3)
    EndChrThread(0x45, 0x3)
    EndChrThread(0x46, 0x3)
    EndChrThread(0x47, 0x3)
    EndChrThread(0x48, 0x3)
    EndChrThread(0x49, 0x3)
    EndChrThread(0x4A, 0x3)
    EndChrThread(0x4B, 0x3)
    EndChrThread(0x4C, 0x3)
    EndChrThread(0x4D, 0x3)
    SetChrFlags(0x44, 0x80)
    SetChrBattleFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x80)
    SetChrBattleFlags(0x45, 0x8000)
    SetChrFlags(0x46, 0x80)
    SetChrBattleFlags(0x46, 0x8000)
    SetChrFlags(0x47, 0x80)
    SetChrBattleFlags(0x47, 0x8000)
    SetChrFlags(0x48, 0x80)
    SetChrBattleFlags(0x48, 0x8000)
    SetChrFlags(0x49, 0x80)
    SetChrBattleFlags(0x49, 0x8000)
    SetChrFlags(0x4A, 0x80)
    SetChrBattleFlags(0x4A, 0x8000)
    SetChrFlags(0x4B, 0x80)
    SetChrBattleFlags(0x4B, 0x8000)
    SetChrFlags(0x4C, 0x80)
    SetChrBattleFlags(0x4C, 0x8000)
    SetChrFlags(0x4D, 0x80)
    SetChrBattleFlags(0x4D, 0x8000)
    EndChrThread(0x53, 0x1)
    OP_0D()
    Fade(500)
    OP_68(35100, 0, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    OP_0D()

    #C0565
    ChrTalk(
        0x34,
        (
            "#3504F#6Pうむ、なかなか\x01",
            "イカス船ではないか。\x02\x03",

            "#3500F早速、オレ様は甲板席の\x01",
            "最前列をゲットさせてもらおう。\x02\x03",

            "#3509Fそんじゃ、お先になー♪\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x34, 3, 0, 63)
    Sleep(500)

    def lambda_C2A5():

        label("loc_C2A5")

        TurnDirection(0x101, 0x34, 300)
        Yield()
        Jump("loc_C2A5")

    QueueWorkItem2(0x101, 1, lambda_C2A5)

    def lambda_C2B7():

        label("loc_C2B7")

        TurnDirection(0x102, 0x34, 300)
        Yield()
        Jump("loc_C2B7")

    QueueWorkItem2(0x102, 1, lambda_C2B7)

    def lambda_C2C9():

        label("loc_C2C9")

        TurnDirection(0x103, 0x34, 300)
        Yield()
        Jump("loc_C2C9")

    QueueWorkItem2(0x103, 1, lambda_C2C9)

    def lambda_C2DB():

        label("loc_C2DB")

        TurnDirection(0x104, 0x34, 300)
        Yield()
        Jump("loc_C2DB")

    QueueWorkItem2(0x104, 1, lambda_C2DB)
    WaitChrThread(0x34, 3)
    SetChrFlags(0x34, 0x80)
    SetChrBattleFlags(0x34, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    WaitChrThread(0x21, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x28, 3)
    WaitChrThread(0x29, 3)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(39290, 0, -7600, 0)
    MoveCamera(60, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11230, 0)
    OP_0D()

    #C0566
    ChrTalk(
        0x102,
        (
            "#0106F#5P何だかランディを\x01",
            "さらにチャランポランに\x01",
            "したような人だったわね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0567
    ChrTalk(
        0x104,
        (
            "#0303F#2Pどういう意味だっつーの。\x02\x03",

            "#0301F俺はあそこまで\x01",
            "遊び人って感じじゃねえだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x103,
        (
            "#0211F#6P……十分、\x01",
            "遊び人風かと思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        (
            "#0012F#6Pまあ、同じ遊び人でも\x01",
            "ぜんぜん違うタイプかもな。\x02\x03",

            "#0000Fランディみたいに\x01",
            "夜遊びとナンパが趣味っていうより\x01",
            "妙にフリーダムな感じと言うか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0570
    ChrTalk(
        0x104,
        (
            "#0309F#11Pおお、分かってんじゃねーか。\x02\x03",

            "#0300F俺と同じくらいの歳みてぇだが\x01",
            "一人で何しに来てんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x33, 0x80)
    ClearChrBattleFlags(0x33, 0x8000)

    #N0571
    NpcTalk(
        0x33,
        "女性の声",
        "あら──奇遇ね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C63E():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C63E)

    def lambda_C64B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C64B)
    Sleep(100)

    def lambda_C65B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C65B)

    def lambda_C668():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C668)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    OP_68(37000, -1300, -5750, 0)
    OP_68(38150, -1300, -5750, 2000)
    MoveCamera(360, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15600, 0)
    OP_93(0x101, 0x13B, 0x0)
    OP_93(0x102, 0x13B, 0x0)
    OP_93(0x103, 0x13B, 0x0)
    OP_93(0x104, 0x13B, 0x0)

    def lambda_C6E5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_C6E5)
    WaitChrThread(0x33, 1)
    TurnDirection(0x33, 0x101, 500)
    OP_6F(0x79)
    OP_0D()

    #C0572
    ChrTalk(
        0x101,
        "#0005F#12Pあなたは……\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x104,
        (
            "#0305F#12Pおおっ……！？\x01",
            "キリカさんじゃないっスか！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(39450, -1300, -5400, 2000)

    def lambda_C76E():
        OP_95(0xFE, 39030, -2500, -4320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_C76E)
    WaitChrThread(0x33, 1)
    OP_6F(0x79)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0574
    AnonymousTalk(
        0x33,
        (
            "フフ、一昨日はどうも。\x02\x03",

            "ここにいるという事は\x01",
            "あなた達もミシュラムへ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0575
    ChrTalk(
        0x102,
        (
            "#0100F#12Pええ……\x01",
            "キリカさんもですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x33,
        (
            "#3404F#5P仕事半分、観光半分ね。\x02\x03",

            "#3400Fそれより……\x01",
            "今の派手な格好をした子は？\x02\x03",

            "あなた達のお友達かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x101,
        (
            "#0004F#12Pいえ……\x01",
            "先ほど知り合ったばかりです。\x02\x03",

            "#0000F何でもエレボニアの帝都から\x01",
            "観光に来たみたいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x33,
        (
            "#3405F#5P帝都から……\x02\x03",

            "#3404F……ふふ、成程ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x101,
        "#0005F#12P？？？\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x103,
        (
            "#0205F#6Pひょっとして\x01",
            "お知り合いですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x33,
        (
            "#3404F#5Pいえ、ユニークそうな\x01",
            "オーラをまとっていたから\x01",
            "職業柄気になっただけよ。\x02\x03",

            "#3400Fそれではお先に……\x01",
            "あなた達も早く乗りなさい。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(35100, 0, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)

    def lambda_CA7D():

        label("loc_CA7D")

        TurnDirection(0x101, 0x33, 300)
        Yield()
        Jump("loc_CA7D")

    QueueWorkItem2(0x101, 1, lambda_CA7D)

    def lambda_CA8F():

        label("loc_CA8F")

        TurnDirection(0x102, 0x33, 300)
        Yield()
        Jump("loc_CA8F")

    QueueWorkItem2(0x102, 1, lambda_CA8F)

    def lambda_CAA1():

        label("loc_CAA1")

        TurnDirection(0x103, 0x33, 300)
        Yield()
        Jump("loc_CAA1")

    QueueWorkItem2(0x103, 1, lambda_CAA1)

    def lambda_CAB3():

        label("loc_CAB3")

        TurnDirection(0x104, 0x33, 300)
        Yield()
        Jump("loc_CAB3")

    QueueWorkItem2(0x104, 1, lambda_CAB3)
    OP_93(0x33, 0x41, 0x1F4)

    def lambda_CACC():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_CACC)
    WaitChrThread(0x33, 1)
    OP_93(0x33, 0x5A, 0x0)

    def lambda_CAEC():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_CAEC)
    Sleep(2000)

    def lambda_CB04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_CB04)
    WaitChrThread(0x33, 1)
    WaitChrThread(0x33, 2)
    SetChrFlags(0x33, 0x80)
    SetChrBattleFlags(0x33, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_63(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0582
    ChrTalk(
        0x104,
        (
            "#0309F#12Pいや～……\x01",
            "相変わらずクールで素敵だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x101,
        (
            "#0000F#6P仕事半分って言ってたけど……\x01",
            "やっぱりテーマパークが目当てかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x102,
        (
            "#0100F#5P芸能関係の仕事なら\x01",
            "その可能性が高そうね……\x02",
        )
    )

    CloseMessageWindow()
    Sound(475, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0585
    ChrTalk(
        0x103,
        "#0205F#12P出航するみたいですね。\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x101,
        "#0000F#6Pああ、俺たちも乗ろう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(9210, 2000)
    OP_6F(0x10)
    OP_0D()
    OP_4C(0xF, 0xFF)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_71(0x9, 0x1F, 0x5A, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(478, 0, 100, 0)
    OP_79(0x9)
    Sound(477, 0, 100, 0)
    Sleep(200)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_CD85():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_CD85)
    WaitChrThread(0x35, 1)

    def lambda_CDA3():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_CDA3)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x35, 1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearScenarioFlags(0x5A, 2)
    OP_24(0x1DF)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_59_B0E0 end

    def Function_60_CDE3(): pass

    label("Function_60_CDE3")


    def lambda_CDE8():
        OP_9B(0x0, 0xFE, 0x0, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CDE8)

    def lambda_CDFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CDFD)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_60_CDE3 end

    def Function_61_CE12(): pass

    label("Function_61_CE12")


    def lambda_CE17():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CE17)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_CE37():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CE37)
    Sleep(3000)

    def lambda_CE4F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CE4F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_61_CE12 end

    def Function_62_CE64(): pass

    label("Function_62_CE64")


    def lambda_CE69():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CE69)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_CE89():
        OP_9B(0x0, 0xFE, 0x0, 0x1FA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CE89)
    Sleep(3500)

    def lambda_CEA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CEA1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_62_CE64 end

    def Function_63_CEB6(): pass

    label("Function_63_CEB6")

    OP_95(0xFE, 42770, -2500, -2020, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)

    def lambda_CED6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CED6)
    Sleep(1700)

    def lambda_CEEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CEEE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_63_CEB6 end

    def Function_64_CF03(): pass

    label("Function_64_CF03")

    Sound(479, 2, 0, 0)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Sleep(8000)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_24(0x1DF)
    Return()

    # Function_64_CF03 end

    def Function_65_CF95(): pass

    label("Function_65_CF95")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-13700, 3000, 22500, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -13700, 2000, 21800, 135)
    SetChrPos(0x102, -13700, 2000, 23100, 135)
    SetChrPos(0x103, -15100, 2000, 21800, 135)
    SetChrPos(0x104, -15100, 2000, 23100, 135)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0587
    ChrTalk(
        0x101,
        "#0013F#5Pあれは……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 72)
    Return()

    # Function_65_CF95 end

    def Function_66_D0A9(): pass

    label("Function_66_D0A9")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-19100, 1500, -13300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -18400, 0, -13300, 45)
    SetChrPos(0x102, -19700, 0, -13300, 45)
    SetChrPos(0x103, -19700, 0, -14600, 45)
    SetChrPos(0x104, -18400, 0, -14600, 45)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0588
    ChrTalk(
        0x101,
        "#0013F#5Pあれは……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 72)
    Return()

    # Function_66_D0A9 end

    def Function_67_D1BD(): pass

    label("Function_67_D1BD")

    OP_95(0xFE, 250, 0, 14720, 4000, 0x0)
    OP_95(0xFE, 1930, 0, 14500, 4000, 0x0)
    OP_95(0xFE, 3230, 500, 17000, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_67_D1BD end

    def Function_68_D201(): pass

    label("Function_68_D201")

    OP_95(0xFE, 800, 0, 12080, 4000, 0x0)
    OP_95(0xFE, 4400, 70, 16149, 4000, 0x0)
    TurnDirection(0xFE, 0x37, 500)
    Return()

    # Function_68_D201 end

    def Function_69_D231(): pass

    label("Function_69_D231")

    OP_95(0xFE, 250, 0, 14720, 4000, 0x0)
    OP_95(0xFE, 1230, 0, 14880, 4000, 0x0)
    OP_95(0xFE, 2230, 200, 16400, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_69_D231 end

    def Function_70_D275(): pass

    label("Function_70_D275")

    OP_95(0xFE, 800, 0, 12080, 4000, 0x0)
    OP_95(0xFE, 3400, 0, 15350, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_70_D275 end

    def Function_71_D2A5(): pass

    label("Function_71_D2A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D4BF")

    def lambda_D2B5():
        OP_9D(0xFE, 0xF14, 0x0, 0x2F58, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_D2B5)
    Sound(814, 0, 100, 0)
    Sound(541, 0, 100, 0)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrSubChip(0x3A, 0x0)

    def lambda_D2E6():
        OP_9D(0xFE, 0x17DE, 0x0, 0x2D64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_D2E6)
    OP_A0(0x3A, 2000, 0x0, 0x5)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)
    SetChrChipByIndex(0x3F, 0x2C)
    SetChrSubChip(0x3F, 0x0)

    def lambda_D31A():
        OP_9D(0xFE, 0x1234, 0x0, 0x2E72, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_D31A)
    Sound(814, 0, 100, 0)
    Sound(541, 0, 100, 0)
    OP_A0(0x3F, 2000, 0x0, 0x3)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_D387():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x32, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_D387)
    OP_A0(0x3F, 2000, 0x4, 0x5)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrChipByIndex(0x3F, 0x2C)

    def lambda_D3B3():
        OP_A0(0x3A, 4000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_D3B3)

    def lambda_D3C0():
        OP_A0(0x3F, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_D3C0)
    OP_9D(0x3A, 0xC8A, 0x0, 0x2F58, 0x32, 0x7D0)
    SetChrSubChip(0x3A, 0x5)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_D425():

        label("loc_D425")

        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        Yield()
        Jump("loc_D425")

    QueueWorkItem2(0x3A, 2, lambda_D425)

    def lambda_D443():

        label("loc_D443")

        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        Yield()
        Jump("loc_D443")

    QueueWorkItem2(0x3F, 2, lambda_D443)
    Sleep(1500)
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)

    def lambda_D47C():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_D47C)

    def lambda_D499():
        OP_9D(0xFE, 0x1388, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_D499)
    Sound(804, 0, 100, 0)
    Sleep(1000)
    Jump("Function_71_D2A5")

    label("loc_D4BF")

    Return()

    # Function_71_D2A5 end

    def Function_72_D4C0(): pass

    label("Function_72_D4C0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch02150.itc", 0x20)
    LoadChrToIndex("chr/ch02152.itc", 0x21)
    LoadChrToIndex("chr/ch02151.itc", 0x22)
    LoadChrToIndex("chr/ch30800.itc", 0x23)
    LoadChrToIndex("chr/ch31700.itc", 0x24)
    LoadChrToIndex("chr/ch30900.itc", 0x25)
    LoadChrToIndex("chr/ch31800.itc", 0x26)
    LoadChrToIndex("chr/ch00400.itc", 0x27)
    LoadChrToIndex("chr/ch02100.itc", 0x28)
    LoadChrToIndex("chr/ch06700.itc", 0x29)
    LoadChrToIndex("chr/ch30850.itc", 0x2A)
    LoadChrToIndex("chr/ch30950.itc", 0x2B)
    LoadChrToIndex("chr/ch30852.itc", 0x2C)
    LoadChrToIndex("chr/ch30952.itc", 0x2D)
    LoadChrToIndex("apl/ch50307.itc", 0x2E)
    LoadChrToIndex("apl/ch50309.itc", 0x2F)
    LoadChrToIndex("apl/ch50390.itc", 0x30)
    LoadChrToIndex("chr/ch00601.itc", 0x31)
    LoadChrToIndex("chr/ch00701.itc", 0x32)
    LoadEffect(0x0, "event\\eva01_00.eff")
    LoadEffect(0x1, "event\\eva04_00.eff")
    LoadEffect(0x2, "battle\\cr313100.eff")
    OP_68(3210, 1480, 11840, 0)
    MoveCamera(36, 18, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x38, 0x27)
    SetChrSubChip(0x38, 0x0)
    OP_90(0x38, 3200, 600, 17150, 180)
    SetChrFlags(0x38, 0x8000)
    ClearChrFlags(0x38, 0x4)
    ClearChrFlags(0x38, 0x80)
    ClearChrBattleFlags(0x38, 0x8000)
    OP_4B(0x2E, 0xFF)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    OP_90(0x2E, 5900, 800, 17600, 180)
    SetChrFlags(0x2E, 0x8000)
    ClearChrFlags(0x2E, 0x4)
    SetChrFlags(0x2E, 0x40)
    ClearChrFlags(0x2E, 0x80)
    ClearChrBattleFlags(0x2E, 0x8000)
    SetChrChipByIndex(0x39, 0x29)
    SetChrSubChip(0x39, 0x0)
    OP_90(0x39, 2100, 900, 17800, 180)
    SetChrFlags(0x39, 0x8000)
    ClearChrFlags(0x39, 0x80)
    ClearChrBattleFlags(0x39, 0x8000)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)
    SetChrPos(0x3A, 2000, 0, 12000, 90)
    SetChrFlags(0x3A, 0x8000)
    ClearChrFlags(0x3A, 0x80)
    ClearChrBattleFlags(0x3A, 0x8000)
    SetChrChipByIndex(0x3B, 0x26)
    SetChrSubChip(0x3B, 0x0)
    SetChrPos(0x3B, 0, 0, 13500, 135)
    SetChrFlags(0x3B, 0x8000)
    ClearChrFlags(0x3B, 0x80)
    ClearChrBattleFlags(0x3B, 0x8000)
    SetChrChipByIndex(0x3C, 0x25)
    SetChrSubChip(0x3C, 0x0)
    SetChrPos(0x3C, -800, 0, 10600, 90)
    SetChrFlags(0x3C, 0x8000)
    ClearChrFlags(0x3C, 0x80)
    ClearChrBattleFlags(0x3C, 0x8000)
    SetChrChipByIndex(0x3D, 0x25)
    SetChrSubChip(0x3D, 0x0)
    SetChrPos(0x3D, 500, 0, 9290, 45)
    SetChrFlags(0x3D, 0x8000)
    ClearChrFlags(0x3D, 0x80)
    ClearChrBattleFlags(0x3D, 0x8000)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrPos(0x3F, 5000, 0, 12000, 270)
    SetChrFlags(0x3F, 0x8000)
    ClearChrFlags(0x3F, 0x80)
    ClearChrBattleFlags(0x3F, 0x8000)
    SetChrChipByIndex(0x40, 0x24)
    SetChrSubChip(0x40, 0x0)
    SetChrPos(0x40, 8400, 0, 13500, 250)
    SetChrFlags(0x40, 0x8000)
    ClearChrFlags(0x40, 0x80)
    ClearChrBattleFlags(0x40, 0x8000)
    SetChrChipByIndex(0x41, 0x23)
    SetChrSubChip(0x41, 0x0)
    SetChrPos(0x41, 9100, 0, 11600, 270)
    SetChrFlags(0x41, 0x8000)
    ClearChrFlags(0x41, 0x80)
    ClearChrBattleFlags(0x41, 0x8000)
    SetChrChipByIndex(0x42, 0x24)
    SetChrSubChip(0x42, 0x0)
    SetChrPos(0x42, 7900, 0, 9700, 315)
    SetChrFlags(0x42, 0x8000)
    ClearChrFlags(0x42, 0x80)
    ClearChrBattleFlags(0x42, 0x8000)
    SetChrChipByIndex(0x43, 0x23)
    SetChrSubChip(0x43, 0x0)
    SetChrPos(0x43, 5100, 0, 9000, 0)
    SetChrFlags(0x43, 0x8000)
    ClearChrFlags(0x43, 0x80)
    ClearChrBattleFlags(0x43, 0x8000)
    SetChrChipByIndex(0x36, 0x31)
    SetChrSubChip(0x36, 0x0)
    SetChrPos(0x36, -3800, 2000, 20900, 90)
    ClearChrFlags(0x36, 0x4)
    SetChrFlags(0x36, 0x8000)
    SetChrChipByIndex(0x37, 0x32)
    SetChrSubChip(0x37, 0x0)
    SetChrPos(0x37, -4900, 2000, 22200, 90)
    ClearChrFlags(0x37, 0x4)
    SetChrFlags(0x37, 0x8000)
    OP_52(0x36, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x37, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x38, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Sleep(10)
    PlayBGM("ed7517", 0)
    SetCameraDistance(20500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0589
    ChrTalk(
        0x3F,
        (
            "#11Pおら、青坊主！\x01",
            "気合い入れてかかってこいや！\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x3A,
        "言うまでもないさ！\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x3A,
        "行くぞッ！\x02",
    )

    CloseMessageWindow()
    OP_52(0x3A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x3B, 2, 0, 71)
    Sleep(3500)
    Fade(500)
    OP_68(-3180, 1310, 11540, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, -9000, 0, 11410, 90)
    SetChrPos(0x104, -9300, 0, 10010, 90)
    SetChrPos(0x102, -10000, 0, 11410, 90)
    SetChrPos(0x103, -10300, 0, 10010, 90)
    OP_0D()

    #C0592
    ChrTalk(
        0x102,
        (
            "#0105Fあれは……\x01",
            "何をしているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x103,
        (
            "#0200Fそれほど険悪な雰囲気では\x01",
            "無さそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        (
            "#0305Fただのタイマンってわけじゃ\x01",
            "無さそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x101,
        (
            "#0006Fとにかく事情を聞こう。\x02\x03",

            "#0001F幸い、ワジもヴァルドも\x01",
            "来ているみたいだし──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 20, -1, -1)
    SetChrName("娘の声")

    #A0596
    AnonymousTalk(
        0xFF,
        (
            "ちょっとちょっと！\x01",
            "あなたたち、何してるのよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(5160, 940, 14220, 0)
    MoveCamera(62, 13, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    OP_68(4760, 1660, 17450, 2000)
    MoveCamera(50, 13, 0, 2000)
    OP_6E(420, 2000)
    SetCameraDistance(23500, 2000)
    EndChrThread(0x3B, 0xFF)
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrChipByIndex(0x3F, 0x2C)

    def lambda_DB70():
        OP_A0(0x3A, 5000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_DB70)

    def lambda_DB7D():
        OP_A0(0x3F, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_DB7D)
    SetChrPos(0x3F, 3790, 0, 11880, 270)
    SetChrPos(0x3A, 2340, 0, 12120, 90)
    SetChrSubChip(0x3A, 0x5)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_DBED():

        label("loc_DBED")

        OP_A6(0xFE, 0x0, 0x19, 0x96, 0x5DC)
        Yield()
        Jump("loc_DBED")

    QueueWorkItem2(0x3A, 2, lambda_DBED)

    def lambda_DC0B():

        label("loc_DC0B")

        OP_A6(0xFE, 0x0, 0x19, 0x96, 0x5DC)
        Yield()
        Jump("loc_DC0B")

    QueueWorkItem2(0x3F, 2, lambda_DC0B)
    ClearChrFlags(0x36, 0x80)
    ClearChrBattleFlags(0x36, 0x8000)
    ClearChrFlags(0x37, 0x80)
    ClearChrBattleFlags(0x37, 0x8000)

    def lambda_DC3D():
        OP_95(0xFE, 4200, 2000, 20900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_DC3D)
    Sleep(50)

    def lambda_DC5A():
        OP_95(0xFE, 3400, 2000, 22200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_DC5A)
    WaitChrThread(0x36, 1)
    SetChrChipByIndex(0x36, 0x1E)
    SetChrSubChip(0x36, 0x0)

    def lambda_DC80():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x36, 2, lambda_DC80)
    WaitChrThread(0x37, 1)
    SetChrChipByIndex(0x37, 0x1F)
    SetChrSubChip(0x37, 0x0)

    def lambda_DC99():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x37, 2, lambda_DC99)

    def lambda_DCA6():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_DCA6)
    Sleep(50)

    def lambda_DCB6():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_DCB6)
    Sleep(50)
    TurnDirection(0x39, 0x36, 500)
    OP_0D()

    #C0597
    ChrTalk(
        0x2E,
        "#1605F#12Pあん……？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x38,
        "#0405F#12P……へえ………\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x36,
        (
            "#0806Fまったく、連絡を受けて\x01",
            "見に来てみればゾロゾロと……\x02\x03",

            "#0801Fあなたたち、旧市街の\x01",
            "テスタメンツとサーベルバイパーね？\x02\x03",

            "喧嘩は終わり！\x01",
            "とっとと解散しなさいよね！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)

    def lambda_DDC7():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_DDC7)

    def lambda_DDE4():
        OP_9D(0xFE, 0x1388, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_DDE4)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x3A, 0)
    WaitChrThread(0x3F, 0)

    def lambda_DE0F():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_DE0F)

    def lambda_DE1C():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x40, 0, lambda_DE1C)

    def lambda_DE29():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x41, 0, lambda_DE29)

    def lambda_DE36():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x42, 0, lambda_DE36)

    def lambda_DE43():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x43, 0, lambda_DE43)

    def lambda_DE50():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_DE50)

    def lambda_DE5D():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3B, 0, lambda_DE5D)

    def lambda_DE6A():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3C, 0, lambda_DE6A)

    def lambda_DE77():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3D, 0, lambda_DE77)

    #C0600
    ChrTalk(
        0x2E,
        "#1601F#12Pなんだぁ、てめぇらは……\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x37,
        (
            "#0903F遊撃士協会に所属する者です。\x02\x03",

            "#0901Fあなた達が喧嘩をしていると\x01",
            "連絡を受けて、仲裁に来ました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x3F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x41, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x3B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x40, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x3C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_68(4440, 2550, 18850, 2000)
    MoveCamera(37, 13, 0, 2000)
    OP_6E(480, 2000)
    SetCameraDistance(23630, 2000)
    Sleep(2000)

    #C0602
    ChrTalk(
        0x2E,
        "#1605F#12P遊撃士だとぉ……！？\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x38,
        (
            "#0404F#6P#Nエステル・ブライトに\x01",
            "ヨシュア・ブライト……\x02\x03",

            "#0400Fフフ、雑誌で\x01",
            "何度か見かけた事があるね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0604
    ChrTalk(
        0x36,
        (
            "#0806F#5Pそりゃどうも。\x02\x03",

            "#0800Fえっと、あなた達が\x01",
            "両チームのリーダーってところ？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x38,
        (
            "#0404F#6P#N一応ね。\x02\x03",

            "#0400F僕はテスタメンツのワジ。\x01",
            "こっちはバイパーのヴァルドさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0606
    ChrTalk(
        0x37,
        (
            "#0903F#5P情報通りだね。\x02\x03",

            "#0900F見たところ、喧嘩をしている\x01",
            "訳じゃなさそうだけど……？\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x38,
        (
            "#0404F#6P#Nフフ、単なるお遊びさ。\x02\x03",

            "せっかくの記念祭だからね。\x01",
            "どうせだったら普段と違うことを\x01",
            "しようと思ってさ。\x02\x03",

            "#0402Fそれで勝ち抜きタイマンバトルを\x01",
            "しようって事になったわけさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0608
    ChrTalk(
        0x36,
        "#0805F#5Pか、勝ち抜きタイマンバトル～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x39, 0x36, 500)

    #C0609
    ChrTalk(
        0x39,
        (
            "#6P……両チームから５人ずつ出して\x01",
            "１対１の勝負で勝ち抜き戦をさせる。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x39,
        "#6P大将はワジと、そちらのヴァルド。\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x39,
        (
            "#6P最終的に負けた側が、勝った側の\x01",
            "記念祭での飲食費を払う取り決めだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x36,
        (
            "#0805F#5Pなるほど、試合みたいなもんね。\x02\x03",

            "#0809Fそれなら別に構わないか──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0613
    ChrTalk(
        0x36,
        (
            "#0806F#5Pって、違う違う！\x02\x03",

            "#0801F試合をするのはともかく、\x01",
            "こんな所でしちゃダメでしょ！？\x02\x03",

            "ここは人通りも多いんだし、\x01",
            "別の場所でやればいいじゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x2E,
        (
            "#1603F#12Pハッ、そんなのは俺らの勝手だ。\x02\x03",

            "#1601Fしかしてめえ……\x01",
            "遊撃士だか何だか知らねぇが\x01",
            "随分と偉そうなクチを叩きやがるな。\x02\x03",

            "調子に乗ってんじゃねえのか、アア？\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x36,
        (
            "#0803F#5Pあのね……\x01",
            "調子に乗ってるのはあなた達でしょ。\x02\x03",

            "#0801Fあたしは常識的なことを\x01",
            "言ってるだけじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x2E,
        "#1600F#12Pこのアマ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x0, 0x1F4)
    OP_68(5860, 2550, 20980, 2000)

    def lambda_E56E():

        label("loc_E56E")

        TurnDirection(0xFE, 0x2E, 500)
        Yield()
        Jump("loc_E56E")

    QueueWorkItem2(0x36, 2, lambda_E56E)

    def lambda_E580():

        label("loc_E580")

        TurnDirection(0xFE, 0x2E, 500)
        Yield()
        Jump("loc_E580")

    QueueWorkItem2(0x37, 2, lambda_E580)
    OP_95(0x2E, 6200, 2000, 20800, 2000, 0x0)
    TurnDirection(0x2E, 0x36, 500)
    EndChrThread(0x36, 0x2)
    EndChrThread(0x37, 0x2)

    #C0617
    ChrTalk(
        0x2E,
        (
            "#1604F#11Pどうやら少しばかり\x01",
            "痛い目に遭いたいらしいな？\x02\x03",

            "#1602Fそこの黒髪の野郎と一緒に\x01",
            "可愛がってやってもいいんだぜ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x36,
        (
            "#0806F#6Pう、うーん……\x02\x03",

            "#0808Fヨシュア、どうしよう？\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x37,
        (
            "#0903F#5Pまあ、周りの目もあるし……\x02\x03",

            "#0900Fあまり大人気ない事は\x01",
            "しない方がいいと思うけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x36,
        "#0802F#6Pやっぱり？\x02",
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0621
    ChrTalk(
        0x2E,
        (
            "#1607F#11Pてめえら……\x01",
            "何ブツクサ言ってやがる！\x02\x03",

            "この“鬼砕き”の\x01",
            "ヴァルド・ヴァレス様が恐くねえのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6010, 2550, 21180, 800)
    SetCameraDistance(23800, 800)
    OP_95(0x38, 3500, 1100, 18200, 1800, 0x0)
    TurnDirection(0x38, 0x2E, 500)
    OP_6F(0x1)

    #C0622
    ChrTalk(
        0x38,
        (
            "#0406F#6P#N──やめときなよ、ヴァルド。\x02\x03",

            "#0400Fそのお姉さん、武術込みだったら\x01",
            "たぶん君より強いよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x2E, 0x38, 500)

    #C0623
    ChrTalk(
        0x2E,
        "#1605F#11Pなにぃ……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x36, 0x38, 500)
    Sleep(150)

    #C0624
    ChrTalk(
        0x36,
        "#0800F#5Pへえ、分かるんだ？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x38, 0x36, 500)
    Sleep(150)

    #C0625
    ChrTalk(
        0x38,
        (
            "#0404F#12P#N何となく、だけどね。\x02\x03",

            "#0402Fそちらのお兄さんは\x01",
            "実力的には更に上なのかな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x37, 0x38, 500)
    Sleep(150)

    #C0626
    ChrTalk(
        0x37,
        (
            "#0902F#5Pはは……\x01",
            "まだまだ修行中の身だけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x36,
        (
            "#0806F#5Pむー……\x01",
            "ヨシュアの方が上っていうのは\x01",
            "確かにそうなんだけど……\x02\x03",

            "#0801F決め付けられると、それはそれで\x01",
            "ちょっと納得行かないわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x37,
        (
            "#0904F#5Pまあまあ、遊撃士の仕事は\x01",
            "何も戦闘だけじゃなんだし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    TurnDirection(0x2E, 0x36, 500)
    Sleep(1000)
    #Sound(1807, 255, 100, 0)    #voice#Wald
    Sleep(500)

    #C0629
    ChrTalk(
        0x2E,
        (
            "#1602F#11Pククク……\x01",
            "こんな小娘が俺より上だと？\x02\x03",

            "#1607Fハッ……\x01",
            "だったら証明してみせろや！！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(5680, 2550, 20990, 1000)
    SetCameraDistance(21320, 1000)

    def lambda_EAAB():

        label("loc_EAAB")

        TurnDirection(0xFE, 0x2E, 600)
        Yield()
        Jump("loc_EAAB")

    QueueWorkItem2(0x36, 0, lambda_EAAB)
    OP_99(0x2E, 0x36, 0x3E8, 0xBB8, 0x0)
    Fade(250)
    SetChrChipByIndex(0x2E, 0x2E)
    SetChrSubChip(0x2E, 0x0)
    SetChrFlags(0x2E, 0x20)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0630
    ChrTalk(
        0x37,
        "#0901F#5Pエステル……\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x36,
        "#0804F#6P大丈夫、任せて。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(4190, 2920, 19620, 0)
    MoveCamera(359, 8, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(25000, 1000)
    SetChrChipByIndex(0x3F, 0x23)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x25)
    SetChrSubChip(0x3A, 0x0)
    OP_93(0x36, 0x5A, 0x0)

    def lambda_EB81():

        label("loc_EB81")

        TurnDirection(0xFE, 0x2E, 300)
        Yield()
        Jump("loc_EB81")

    QueueWorkItem2(0x37, 0, lambda_EB81)
    SetChrChipByIndex(0x2E, 0x30)
    SetChrSubChip(0x2E, 0x0)
    SetChrPos(0x2E, 5300, 2300, 20900, 270)
    Sound(804, 0, 100, 0)
    OP_D3(0x2E, 0x0, 0x0, 0x15F90, 0x0)
    Sound(1648, 255, 100, 0)    #voice#Estelle
    Sound(534, 0, 100, 0)
    ClearChrFlags(0x2E, 0x1)
    ClearChrFlags(0x2E, 0x100)

    def lambda_EBDB():
        OP_9D(0xFE, 0x9C4, 0x7D0, 0x526C, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_EBDB)
    OP_D3(0x2E, 0x0, 0x0, 0x57E40, 0x384)
    SetChrChipByIndex(0x2E, 0x2F)
    SetChrSubChip(0x2E, 0x0)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    Sound(819, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_9D(0x2E, 0x7D0, 0x7D0, 0x5334, 0x190, 0x7D0)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x64, 0x5DC, 0x96)
    Sound(819, 0, 100, 0)
    CancelBlur(0)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x2E, 0x1)
    Sleep(500)
    EndChrThread(0x37, 0x0)

    #C0632
    ChrTalk(
        0x2E,
        "#1605F#11Pあ゛……？\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x38,
        "#0406F#6Pほら、言わんこっちゃない。\x02",
    )

    CloseMessageWindow()
    OP_68(4320, 2270, 18840, 3000)
    MoveCamera(359, 7, 0, 3000)
    OP_6E(380, 3000)
    SetCameraDistance(25000, 3000)
    OP_63(0x3F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x40, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x41, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x3F)
    OP_64(0x40)
    OP_64(0x41)
    OP_64(0x3A)
    OP_64(0x3B)
    OP_64(0x3C)

    #C0634
    ChrTalk(
        0x40,
        "#11Pヴァ、ヴァルドさんが！？\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x3F,
        "#5Pな、なんだあの娘……！？\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x3B,
        "#5Pすごい……！\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x3A,
        "#5Pあれが遊撃士……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(2720, 2400, 21470, 0)
    MoveCamera(336, 12, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_63(0x2E, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2E)

    #C0638
    ChrTalk(
        0x36,
        "#0805F#12Pえっと、大丈夫？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x2E, 0x2)

    def lambda_EEBD():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_EEBD)
    WaitChrThread(0x2E, 2)
    #Sound(1808, 255, 100, 0)    #voice#Wald

    #C0639
    ChrTalk(
        0x2E,
        "#1604F#11Pククク……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_EEFD():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_EEFD)
    SetChrSubChip(0x2E, 0x1)
    #Sound(1809, 255, 100, 0)    #voice#Wald
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0640
    ChrTalk(
        0x2E,
        "#1609F#4S#11P#Nハハハハハハハハッ！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(2450, 2500, 22450, 800)
    SetCameraDistance(26180, 800)
    Sound(804, 0, 100, 0)
    Sound(534, 0, 100, 0)
    SetChrFlags(0x2E, 0x100)
    SetChrChipByIndex(0x2E, 0x20)
    SetChrSubChip(0x2E, 0x0)

    def lambda_EF95():
        TurnDirection(0xFE, 0x36, 800)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_EF95)
    OP_9C(0x2E, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrFlags(0x2E, 0x1)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0641
    ChrTalk(
        0x2E,
        (
            "#1604F#5P──悪かった。\x01",
            "侮ってたみてえだったな。\x02\x03",

            "#1601Fだがよ……\x01",
            "さすがにナメすぎなんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x36,
        "#0801F#12P……！\x02",
    )

    CloseMessageWindow()
    OP_68(3100, 2500, 22470, 800)
    SetCameraDistance(24870, 800)
    BeginChrThread(0x36, 3, 0, 73)
    SetChrChipByIndex(0x2E, 0x21)
    SetChrSubChip(0x2E, 0x0)
    Sleep(90)
    SetChrSubChip(0x2E, 0x1)
    Sleep(90)
    SetChrSubChip(0x2E, 0x2)
    Sleep(90)

    def lambda_F080():

        label("loc_F080")

        TurnDirection(0xFE, 0x36, 100)
        Yield()
        Jump("loc_F080")

    QueueWorkItem2(0x37, 2, lambda_F080)
    SetChrFlags(0x2E, 0x20)
    Sound(1789, 255, 100, 0)    #voice#Wald
    Sound(532, 0, 100, 0)

    def lambda_F0A3():
        OP_96(0xFE, 0xAF0, 0x7D0, 0x529E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_F0A3)
    SetChrSubChip(0x2E, 0x3)
    Sleep(70)
    SetChrSubChip(0x2E, 0x4)
    WaitChrThread(0x2E, 1)
    SetChrSubChip(0x2E, 0x5)
    ClearChrFlags(0x2E, 0x20)
    PlayEffect(0x2, 0xFF, 0x2E, 0x140, 0, 100, 1300, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    Sound(895, 0, 100, 0)
    Sound(834, 0, 100, 0)
    Sleep(800)
    WaitChrThread(0x36, 3)

    #C0643
    ChrTalk(
        0x36,
        "#0807F#12Pあ、危な……！\x02",
    )

    CloseMessageWindow()
    #Sound(1780, 255, 100, 0)    #voice#Joshua

    #C0644
    ChrTalk(
        0x37,
        "#0901F#5Pエステル……！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x37, 0x2)
    SetChrChipByIndex(0x37, 0x32)
    SetChrSubChip(0x37, 0x3)

    def lambda_F17D():
        OP_9D(0xFE, 0x157C, 0x7D0, 0x5078, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_F17D)
    Sound(814, 0, 100, 0)

    def lambda_F1A0():

        label("loc_F1A0")

        TurnDirection(0xFE, 0x2E, 1000)
        Yield()
        Jump("loc_F1A0")

    QueueWorkItem2(0x37, 2, lambda_F1A0)
    WaitChrThread(0x37, 0)
    PlayEffect(0x1, 0xFF, 0x37, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x37, 0x1F)
    SetChrSubChip(0x37, 0x0)
    Sleep(100)
    OP_95(0x38, 3150, 1600, 19150, 2000, 0x0)
    TurnDirection(0x38, 0x37, 500)
    EndChrThread(0x37, 0x2)

    #C0645
    ChrTalk(
        0x38,
        (
            "#0404F#6Pやれやれ……\x02\x03",

            "#0400F──君たちもちょっと\x01",
            "調子に乗りすぎじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x37,
        (
            "#0903F#11Pああ、そうみたいだね。\x02\x03",

            "#0901Fだからと言って謝るのも\x01",
            "スジが違うとは思うけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2E, 0x6)
    Sleep(90)
    SetChrSubChip(0x2E, 0x7)
    Sleep(90)
    Fade(250)
    SetChrChipByIndex(0x2E, 0x20)
    SetChrSubChip(0x2E, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0647
    ChrTalk(
        0x2E,
        (
            "#1602F#5Pクク……\x01",
            "目の色が変わりやがったな。\x02\x03",

            "#1604F分かるぜ──てめぇは相当強い。\x02\x03",

            "#1601Fそういったヤツを叩きのめすのが\x01",
            "俺は何よりも楽しみでなぁ！\x02\x03",

            "とっとと抜けや、アア！？\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x37,
        "#0901F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x36,
        (
            "#0801F#12Pちょ、ちょっとヨシュア！\x02\x03",

            "あたしは大丈夫だから\x01",
            "あんまり本気にならないでよ！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    #Sound(1086, 255, 100, 0)    #voice#Lloyd

    #N0650
    NpcTalk(
        0x101,
        "ロイドの声",
        "──待った！\x02",
    )

    CloseMessageWindow()
    OP_63(0x37, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x38, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x36, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(20, 1750, 13750, 0)
    MoveCamera(314, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -2450, 0, 13210, 90)
    SetChrPos(0x104, -2720, 0, 11440, 90)
    SetChrPos(0x102, -4470, 0, 12520, 90)
    SetChrPos(0x103, -4720, 0, 10900, 90)
    BeginChrThread(0x101, 0, 0, 67)
    BeginChrThread(0x104, 0, 0, 68)
    BeginChrThread(0x102, 0, 0, 69)
    BeginChrThread(0x103, 0, 0, 70)

    def lambda_F545():

        label("loc_F545")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_F545")

    QueueWorkItem2(0x36, 0, lambda_F545)

    def lambda_F557():

        label("loc_F557")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F557")

    QueueWorkItem2(0x37, 0, lambda_F557)

    def lambda_F569():

        label("loc_F569")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F569")

    QueueWorkItem2(0x38, 0, lambda_F569)

    def lambda_F57B():

        label("loc_F57B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F57B")

    QueueWorkItem2(0x2E, 0, lambda_F57B)

    def lambda_F58D():

        label("loc_F58D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F58D")

    QueueWorkItem2(0x39, 0, lambda_F58D)

    def lambda_F59F():

        label("loc_F59F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F59F")

    QueueWorkItem2(0x3F, 0, lambda_F59F)

    def lambda_F5B1():

        label("loc_F5B1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F5B1")

    QueueWorkItem2(0x40, 0, lambda_F5B1)

    def lambda_F5C3():

        label("loc_F5C3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F5C3")

    QueueWorkItem2(0x41, 0, lambda_F5C3)

    def lambda_F5D5():

        label("loc_F5D5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F5D5")

    QueueWorkItem2(0x42, 0, lambda_F5D5)

    def lambda_F5E7():

        label("loc_F5E7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F5E7")

    QueueWorkItem2(0x43, 0, lambda_F5E7)

    def lambda_F5F9():

        label("loc_F5F9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F5F9")

    QueueWorkItem2(0x3A, 0, lambda_F5F9)

    def lambda_F60B():

        label("loc_F60B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F60B")

    QueueWorkItem2(0x3B, 0, lambda_F60B)

    def lambda_F61D():

        label("loc_F61D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_F61D")

    QueueWorkItem2(0x3C, 0, lambda_F61D)
    OP_68(4220, 2200, 18860, 4000)
    MoveCamera(328, 17, 0, 4000)
    OP_6E(380, 4000)
    SetCameraDistance(26000, 4000)
    WaitChrThread(0x101, 0)
    EndChrThread(0x36, 0x0)
    EndChrThread(0x37, 0x0)
    EndChrThread(0x38, 0x0)
    EndChrThread(0x2E, 0x0)
    EndChrThread(0x39, 0x0)

    #C0651
    ChrTalk(
        0x38,
        "#0405F#11Pあれ……\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x36,
        "#0805F#11Pロイド君たち……？\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x101,
        (
            "#0003F#6P話は聞かせてもらったよ。\x02\x03",

            "#0001F双方とも……\x01",
            "まずは落ち着いてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x2E,
        (
            "#1601F#5P#Nハッ、落ちついてられるかよ！\x02\x03",

            "#1604F遊撃士！　いいじゃねえか！\x02\x03",

            "#1607F噂には聞いてたが、まさかここまで\x01",
            "ゾクゾクさせてくれるとはなぁッ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0655
    ChrTalk(
        0x101,
        (
            "#0006F#6Pだから落ち着いてくれって\x01",
            "言ってるだろう……\x02\x03",

            "#0001Fそもそも、ここは公共の場所だ。\x02\x03",

            "タイマン勝負にしても\x01",
            "スジを通すにしても\x01",
            "他の場所でやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x38,
        (
            "#0406F#11Pんー、そうは言ってもねぇ。\x02\x03",

            "#0402Fここまで盛り上がった以上、\x01",
            "ハイ解散ってのもアレじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x101,
        "#0011F#6Pワジ……！？\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x38,
        (
            "#0402F#11Pヴァルドは頭に血が上ってるし\x01",
            "お姉さんたちもお仕事で来ている。\x02\x03",

            "#0409Fお互い勝負するくらいしか\x01",
            "スジは通せないんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0x36, 500)
    Sleep(300)

    #C0659
    ChrTalk(
        0x2E,
        "#1602F#6Pクク、その通りだぜ……！\x02",
    )

    CloseMessageWindow()

    def lambda_F97F():
        TurnDirection(0xFE, 0x2E, 400)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_F97F)
    Sleep(50)

    def lambda_F98F():
        TurnDirection(0xFE, 0x2E, 400)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_F98F)
    Sleep(300)

    #C0660
    ChrTalk(
        0x36,
        (
            "#0803F#12P……あたしも何だか\x01",
            "ちょっと腹が立ってきたわね。\x02\x03",

            "#0801Fそっちがその気なら\x01",
            "決着を付けてもいいんですけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x2E,
        "#1607F#6P上等だ……！\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x101,
        (
            "#0006F#6Pああもう……！\x02\x03",

            "#0013Fヨシュア！\x01",
            "君も何とか言ってくれよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x37,
        (
            "#0908F#12P……ごめん。\x01",
            "僕もちょっと退けないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x101,
        "#0011F#6Pうっ……\x02",
    )

    CloseMessageWindow()

    def lambda_FAC8():

        label("loc_FAC8")

        TurnDirection(0xFE, 0x37, 400)
        Yield()
        Jump("loc_FAC8")

    QueueWorkItem2(0x38, 0, lambda_FAC8)
    Sleep(300)

    #C0665
    ChrTalk(
        0x38,
        (
            "#0404F#6Pフフ、それじゃあ僕は\x01",
            "ヴァルドに加勢しようかな。\x02\x03",

            "#0402Fさすがの君も、その２人を\x01",
            "相手にするのは厳しいだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x2E,
        "#1603F#5P#Nケッ……勝手にしろや。\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#0007F#6Pだあああ～っ！\x01",
            "だから何でそうなるんだって！\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x102,
        "#0106F#5P（こ、困ったわね……）\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x103,
        (
            "#0211F#5P（このままだと凄い乱闘騒ぎに\x01",
            "  なってしまいそうですね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x104,
        (
            "#0303F#6P#N──あのよぉ。\x02\x03",

            "#0300Fそんなにやり合いたいんなら\x01",
            "別の方法でやればいいんじゃね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x37, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x38, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(4180, 1700, 17780, 1500)

    def lambda_FD25():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FD25)
    Sleep(50)

    def lambda_FD35():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_FD35)

    def lambda_FD42():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_FD42)
    Sleep(50)

    def lambda_FD52():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FD52)

    def lambda_FD5F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FD5F)
    Sleep(50)

    def lambda_FD6F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x38, 0, lambda_FD6F)

    def lambda_FD7C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_FD7C)
    Sleep(50)

    def lambda_FD8C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_FD8C)
    OP_6F(0x1)

    #C0671
    ChrTalk(
        0x101,
        "#0005F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x38,
        "#0405F#5P#Nふぅん……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0673
    ChrTalk(
        0x104,
        (
            "#0306F#6Pせっかくの祭だ。\x01",
            "遺恨を残してもつまらねぇだろ。\x02\x03",

            "#0302Fだったらスカッとする方法で\x01",
            "決着を付けるっつーのはどうだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x2E,
        "#1601F#5P#Nスカッとする方法だぁ……？\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x36,
        (
            "#0805F#11P#Nえっと……\x01",
            "ランディさん、どういうこと？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0676
    ChrTalk(
        0x104,
        "#0304F#6Pああ、そいつはな──\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(29500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_72_D4C0 end

    def Function_73_FF02(): pass

    label("Function_73_FF02")

    Sleep(350)
    SetChrChip(0x0, 0x36, 0x1E, 0x12C)
    SetChrChipByIndex(0x36, 0x31)
    SetChrSubChip(0x36, 0x3)

    def lambda_FF1A():
        OP_9D(0xFE, 0x189C, 0x7D0, 0x5078, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_FF1A)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x36, 0)
    PlayEffect(0x1, 0xFF, 0x36, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x36, 0x1E)
    SetChrSubChip(0x36, 0x0)
    Sleep(150)
    SetChrChip(0x1, 0x36, 0x0, 0x0)
    Return()

    # Function_73_FF02 end

    def Function_74_FF87(): pass

    label("Function_74_FF87")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x7, "event\\ev308_00.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -11990, -3000, -9930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 2340, -3000, -8610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 19600, -3000, -4370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(885)
    LoadChrToIndex("chr/ch20000.itc", 0x28)
    LoadChrToIndex("chr/ch20100.itc", 0x29)
    LoadChrToIndex("chr/ch20200.itc", 0x2A)
    LoadChrToIndex("chr/ch20300.itc", 0x2B)
    LoadChrToIndex("chr/ch20800.itc", 0x2C)
    LoadChrToIndex("chr/ch20900.itc", 0x2D)
    LoadChrToIndex("chr/ch21200.itc", 0x2E)
    LoadChrToIndex("chr/ch21300.itc", 0x2F)
    LoadChrToIndex("chr/ch21800.itc", 0x30)
    LoadChrToIndex("chr/ch21900.itc", 0x31)
    SetChrChipByIndex(0x44, 0x28)
    SetChrChipByIndex(0x45, 0x29)
    SetChrChipByIndex(0x46, 0x2A)
    SetChrChipByIndex(0x47, 0x2B)
    SetChrChipByIndex(0x48, 0x2C)
    SetChrChipByIndex(0x49, 0x2D)
    SetChrChipByIndex(0x4A, 0x2E)
    SetChrChipByIndex(0x4B, 0x2F)
    SetChrChipByIndex(0x4C, 0x30)
    SetChrChipByIndex(0x4D, 0x31)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0x46, 0x80)
    ClearChrBattleFlags(0x46, 0x8000)
    ClearChrFlags(0x47, 0x80)
    ClearChrBattleFlags(0x47, 0x8000)
    ClearChrFlags(0x48, 0x80)
    ClearChrBattleFlags(0x48, 0x8000)
    ClearChrFlags(0x49, 0x80)
    ClearChrBattleFlags(0x49, 0x8000)
    ClearChrFlags(0x4A, 0x80)
    ClearChrBattleFlags(0x4A, 0x8000)
    ClearChrFlags(0x4B, 0x80)
    ClearChrBattleFlags(0x4B, 0x8000)
    ClearChrFlags(0x4C, 0x80)
    ClearChrBattleFlags(0x4C, 0x8000)
    ClearChrFlags(0x4D, 0x80)
    ClearChrBattleFlags(0x4D, 0x8000)
    SetChrFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x8000)
    SetChrFlags(0x46, 0x8000)
    SetChrFlags(0x47, 0x8000)
    SetChrFlags(0x48, 0x8000)
    SetChrFlags(0x49, 0x8000)
    SetChrFlags(0x4A, 0x8000)
    SetChrFlags(0x4B, 0x8000)
    SetChrFlags(0x4C, 0x8000)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x44, 43420, -2500, 1510, 181)
    SetChrPos(0x45, 43370, -2500, -2450, 1)
    SetChrPos(0x46, 42230, -2500, 320, 91)
    SetChrPos(0x47, 41700, -2500, -920, 91)
    SetChrPos(0x48, 39850, -2500, 200, 91)
    SetChrPos(0x49, 39820, -2500, -930, 1)
    SetChrPos(0x4A, 37910, -2500, 70, 91)
    SetChrPos(0x4B, 35970, -2500, -690, 91)
    SetChrPos(0x4C, 34150, -2500, 300, 91)
    SetChrPos(0x4D, 32689, -2500, -390, 91)
    SetChrPos(0x0, 14720, -1000, -920, 135)
    SetChrPos(0x1, 14720, -1000, -920, 135)
    SetChrPos(0x2, 14720, -1000, -920, 135)
    SetChrPos(0x3, 14720, -1000, -920, 135)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x1)
    OP_71(0x9, 0xF1, 0x12C, 0x0, 0x20)
    SetMapObjFrame(0x9, "wave00", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_68(8160, 2600, -2060, 0)
    MoveCamera(21, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(39180, 3000, -8560, 10000)
    MoveCamera(71, 11, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(26500, 10000)
    Sound(885, 2, 90, 0)
    FadeToBright(1000, 0)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 0)
    NewScene("c047C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_74_FF87 end

    def Function_75_1031E(): pass

    label("Function_75_1031E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 315)
    SetChrPos(0x15, -16920, 0, -9360, 135)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0677
    ChrTalk(
        0x101,
        (
            "#12P#0000Fすみません、\x01",
            "クロスベル警察の者ですが……\x02\x03",

            "支援要請の件で伺いました。\x01",
            "商工会のテントというのは\x01",
            "こちらでいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x1A, 0xC6, 0x1F4)
    OP_93(0x15, 0xC6, 0x1F4)
    Sleep(300)

    #C0678
    ChrTalk(
        0x1A,
        "#11Pおお、来てくれたか。\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x1A,
        (
            "#11Pそれに……\x01",
            "引き受けてくれたのが\x01",
            "君だったとはのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x101,
        (
            "#12P#0000Fはは、支援課にも\x01",
            "情報が回ってきたみたいだから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_END)), "loc_10711")

    #C0681
    ChrTalk(
        0x102,
        (
            "#12P#0100Fご協力をよろしくお願いしますね、\x01",
            "会長さん。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x1A, 500)
    Sleep(300)

    #C0682
    ChrTalk(
        0x15,
        (
            "#5Pあれ、会長の\x01",
            "お知り合いなんですか……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x15, 500)
    Sleep(300)

    #C0683
    ChrTalk(
        0x1A,
        (
            "#11Pウム、この青年とは\x01",
            "鉄道で隣の席になった事があってのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x101,
        (
            "#12P#0000F俺が警察に\x01",
            "着任する直前でしたよね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10640():
        OP_93(0xFE, 0xC6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_10640)

    def lambda_1064D():
        OP_93(0xFE, 0xC6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1064D)
    Sleep(300)

    #C0685
    ChrTalk(
        0x1A,
        (
            "#11Pふふ、そうじゃった。\x01",
            "それ以来、彼らとは\x01",
            "少し付き合いがあるのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x1A,
        (
            "#11P……少々困った事になっておってな。\x01",
            "すまんが特務支援課の諸君、\x01",
            "今回は世話にならせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108B5")

    label("loc_10711")

    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0687
    ChrTalk(
        0x103,
        (
            "#6P#0205Fあれ、ロイドさんの\x01",
            "知り合いなんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0688
    ChrTalk(
        0x101,
        (
            "#12P#0000Fああ、警察に着任する直前\x01",
            "クロスベルに戻る鉄道の中で\x01",
            "偶然隣の席になってね。\x02\x03",

            "あとで話を聞いたら\x01",
            "商工会の会長さんだったんだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_107EB():
        OP_93(0xFE, 0xF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_107EB)

    def lambda_107F8():
        OP_93(0xFE, 0xF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_107F8)
    Sleep(300)

    #C0689
    ChrTalk(
        0x1A,
        (
            "#11Pふふ、あの時の青年が\x01",
            "警察官だったとは\x01",
            "ワシも知らなんだのだがのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x1A,
        (
            "#11P……少々困った事になっておってな。\x01",
            "すまんが特務支援課の諸君、\x01",
            "今回は世話にならせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108B5")


    #C0691
    ChrTalk(
        0x101,
        (
            "#12P#0004Fええ、お任せください。\x02\x03",

            "#0001Fええと……確かご依頼では\x01",
            "窃盗事件ということでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x104,
        "#12P#0301F連続窃盗犯、だったスか？\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x15,
        "#5Pそ、そうなんですよ。\x02",
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x15,
        (
            "#5P昨日から今日に掛けて\x01",
            "立て続けに４件も……\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x15,
        "#5Pどの店も売り上げがパーなんですよ！\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x1A,
        (
            "#11P記念祭の出店は\x01",
            "商工会が取りまとめておってな。\x01",
            "情報は逐一入ってくるんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x1A,
        (
            "#11P総合するに、どうも出店ばかりを狙う\x01",
            "連続窃盗犯と思われる。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x1A,
        (
            "#11Pしかし特に手がかりも無くてな、\x01",
            "注意を呼びかけるしかできんのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x102,
        (
            "#12P#0101Fそうですか……\x01",
            "それは辛いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそれにこのままでは\x01",
            "被害が拡大する恐れもある、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x1A,
        (
            "#11Pウム、それで君たちを\x01",
            "呼んだというわけじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x1A,
        (
            "#11P商工会としても\x01",
            "これ以上放っては置けん……\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x1A,
        (
            "#11P何より、このままでは\x01",
            "祭りを楽しみに来た客にも\x01",
            "迷惑が掛かってしまうじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x1A,
        (
            "#11P君たちで犯人を\x01",
            "捕まえてはくれんかね。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【断る】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C63")
    OP_29(0x20, 0x1, 0x1)
    Call(0, 76)
    Return()

    label("loc_10C63")


    #C0705
    ChrTalk(
        0x101,
        (
            "#12P#0006Fすみません、今は仕事が\x01",
            "立て込んでまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x1A,
        "#11Pそうか、なら仕方がないな。\x02",
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x1A,
        (
            "#11P手が空いたらまた来てくれんか。\x01",
            "次の被害が出る前に\x01",
            "何としても解決したいんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_29(0x20, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_75_1031E end

    def Function_76_10D7D(): pass

    label("Function_76_10D7D")


    #C0708
    ChrTalk(
        0x101,
        (
            "#12P#0001F判りました。\x01",
            "事情も深刻ですし、すぐに\x01",
            "お引き受けしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x15,
        (
            "#5Pよかった……\x01",
            "これで一安心ですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x1A,
        "#11Pウム、頼りにしておるぞ！\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x104,
        (
            "#12P#0304Fま、大船に乗った気で\x01",
            "居てくださいッス。\x02\x03",

            "#0301F……それでロイド、\x01",
            "捜査方法はどうする？\x01",
            "手がかりなしって話だったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそうだな……\x01",
            "情報が少なすぎて\x01",
            "推理のしようがない気がする。\x02\x03",

            "#0001Fすみません、被害のあった出店を\x01",
            "教えてもらえますか？\x02\x03",

            "聞き込みをして\x01",
            "情報を集めたいんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x1A,
        (
            "#11Pなるほど、それなら\x01",
            "こちらで記録をつけているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x1A,
        (
            "#11P被害に遭ったのは……\x01",
            "……読み上げるが、いいかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x102,
        "#12P#0100Fええ、大丈夫です。\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x1A,
        (
            "#11P中央広場の『ナードルバーガー』、\x01",
            "行政区の『クロマのジュース屋』……\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x1A,
        (
            "#11P歓楽街の『バレット・ピザ』、\x01",
            "そしてこの港湾公園の\x01",
            "『ミスラズ・ジェラート』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x102,
        (
            "#12P#0103F（サラサラ……）\x01",
            "……全部で４店舗、\x01",
            "街区はバラバラみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x103,
        (
            "#6P#0200Fまあ４店舗もあれば\x01",
            "手がかりの一つくらいは\x01",
            "見つかるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x101,
        "#12P#0001Fああ、ともかく回ってみよう。\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x101,
        (
            "#12P#0000F皆さんはここで\x01",
            "待機していていただけますか？\x01",
            "一回りしたら戻ってきますので。\x02\x03",

            "#0005F……そうだ、自分の連絡先を\x01",
            "伝えておくので\x01",
            "何かあればお連絡下さい。\x02\x03",

            "#0001F次の犯行がいつ起こるか\x01",
            "分かりませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x1A,
        "#11Pわかった、待機していよう。\x02",
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x15,
        (
            "#5P皆さん、どうか\x01",
            "よろしくお願いします！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0724
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【窃盗事件の捜査依頼】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_65(0x4, 0x1)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_29(0x20, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_76_10D7D end

    def Function_77_1135C(): pass

    label("Function_77_1135C")

    EventBegin(0x0)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 194)
    SetChrPos(0x15, -16920, 0, -9360, 194)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0725
    ChrTalk(
        0x1A,
        (
            "#11Pおお戻ったか……\x01",
            "聞き込みはどうだったかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、色々と\x01",
            "見えてきたと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x102,
        (
            "#12P#0100F一度情報を\x01",
            "整理してみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x103,
        "#6P#0200Fそうですね。\x02",
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x104,
        "#12P#0300Fロイド、いつものやつを頼むぜ。\x02",
    )

    CloseMessageWindow()

    def lambda_1150A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1150A)

    def lambda_11517():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11517)

    def lambda_11524():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11524)

    def lambda_11531():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11531)
    Sleep(300)

    #C0730
    ChrTalk(
        0x101,
        (
            "#11P#0001F分かった、\x01",
            "それじゃあ始めようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    OP_68(-18800, 2400, -13110, 0)
    MoveCamera(39, 34, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21870, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    SetChrPos(0x101, -15680, 0, -12000, 280)
    SetChrPos(0x102, -19550, 0, -12530, 100)
    SetChrPos(0x103, -19450, 0, -11230, 100)
    SetChrPos(0x104, -18070, 0, -13540, 55)
    SetChrPos(0x1A, -16760, 0, -10660, 145)
    SetChrPos(0x15, -18000, 0, -10000, 145)
    FadeToBright(500, 0)
    OP_0D()

    #C0731
    ChrTalk(
        0x101,
        (
            "#11P#0003Fコホン……まずは\x01",
            "聞き込みで集めた情報を整理しよう。\x02\x03",

            "#0001F店の人の話によると、\x01",
            "４つの出店からミラを奪った\x01",
            "犯行の手口は……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【武器で脅して奪った】\x01",      # 0
            "【客を装って奪った】\x01",        # 1
            "【客の応対中に奪った】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1181C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0732
    ChrTalk(
        0x104,
        (
            "#12P#0301Fどこの店も\x01",
            "客の応対中にやられたって\x01",
            "話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x103,
        (
            "#6P#0203F店の人の隙をついた犯行……\x02\x03",

            "#0200Fこれでは\x01",
            "気をつけようがありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x101,
        (
            "#11P#0001Fああ、いくら注意を呼びかけても\x01",
            "効果は薄いだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11939")

    label("loc_1181C")


    #C0735
    ChrTalk(
        0x104,
        (
            "#12P#0305Fいや、そうじゃ\x01",
            "ないんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x103,
        (
            "#6P#0200Fどこの店も\x01",
            "客の応対中に盗まれたという\x01",
            "話でしたが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0737
    ChrTalk(
        0x101,
        (
            "#11P#0005Fおっと……そうだったな。\x02\x03",

            "#0003F店の人の隙を付いて\x01",
            "背後から盗み取る犯行。\x02\x03",

            "#0001Fこれではいくら注意を呼びかけても\x01",
            "効果は薄いだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11939")


    #C0738
    ChrTalk(
        0x1A,
        (
            "#5Pうむぅ、話は聞いておったが\x01",
            "卑劣な奴じゃな……\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x104,
        (
            "#12P#0303Fおまけに立て続けに\x01",
            "４軒もやられてるしな。\x02\x03",

            "#0301F犯人は今ごろ\x01",
            "ほくそ笑んでんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x101,
        (
            "#11P#0001Fそうだな……こういった犯罪には\x01",
            "いくつかパターンが\x01",
            "あると思うけど……\x02\x03",

            "今回の犯行にも\x01",
            "一定の傾向がありそうだ。\x02\x03",

            "#0003Fそうだな、動機として\x01",
            "考えられるのは……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【嫌がらせ】\x01",          # 0
            "【ミラに困って】\x01",      # 1
            "【遊び半分】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BAD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0741
    ChrTalk(
        0x102,
        (
            "#6P#0101F遊び半分……\x01",
            "確かにそんな感じだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        (
            "#6P#0200F短期間での連続犯行、\x01",
            "ミラに困ってる風じゃなさそうです。\x02\x03",

            "むしろ窃盗のスリルを\x01",
            "楽しんでいるという所でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E21")

    label("loc_11BAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D0A")

    #C0743
    ChrTalk(
        0x102,
        (
            "#6P#0105F嫌がらせ……というか\x01",
            "愉快犯的な感じだったけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x103,
        (
            "#6P#0200Fそうですね、嫌がらせなら\x01",
            "特定の店舗を繰り返し狙うはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        (
            "#11P#0006Fそ、そうだな……\x01",
            "あまり明確な目的は伺えなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x104,
        (
            "#12P#0303F短期間での連続犯行、\x01",
            "ミラに困ってる風でもなさそうだよな。\x02\x03",

            "#0301Fむしろ窃盗のスリルを\x01",
            "楽しんでるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E21")

    label("loc_11D0A")


    #C0747
    ChrTalk(
        0x102,
        (
            "#6P#0105Fミラに困って……\x01",
            "という感じではなかったけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x104,
        (
            "#12P#0301Fだな。\x01",
            "短期間での連続犯行、\x01",
            "むしろ愉快犯的なカンジだぜ。\x02\x03",

            "#0303F大金が必要なら\x01",
            "そもそも出店なんざ\x01",
            "狙わねえだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#11P#0005Fそ、そうだな……\x02\x03",

            "#0003Fむしろ窃盗のスリルを\x01",
            "楽しんでるって感じか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E21")


    #C0750
    ChrTalk(
        0x15,
        (
            "#5Pそ、そんな理由で\x01",
            "犯行を繰り返すなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x15,
        "#5P犯人は一体……！？\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそうですね、犯人像も\x01",
            "見えてきた気がします。\x02\x03",

            "#0001F犯人は……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ベテランのスリ】\x01",      # 0
            "【青年２人組み】\x01",        # 1
            "【大窃盗団】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1225F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11F47")
    OP_2C(0x20, 0x2)

    label("loc_11F47")


    #C0753
    ChrTalk(
        0x101,
        "#11P#0001F青年の２人組みじゃないかと思う。\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0754
    ChrTalk(
        0x104,
        (
            "#12P#0305F目撃した人間も\x01",
            "いなかったと思うが……\x01",
            "どうして判るんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x101,
        (
            "#11P#0000Fよく思い出してくれ。\x01",
            "どの出店でも接客中だったけど……\x02\x03",

            "その接客をしていた相手は\x01",
            "似た様な相手じゃなかったか？\x02\x03",

            "#0003F行政区と港湾公園に現れたのは\x01",
            "軽い感じの青年……\x02\x03",

            "中央広場と歓楽街に現れたのは\x01",
            "喋り好きの青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x103,
        (
            "#6P#0203F２種類の客の\x01",
            "相手をしているときだけ\x01",
            "犯行が起こる……\x02\x03",

            "#0200F偶然にしては\x01",
            "出来すぎていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x101,
        (
            "#11P#0001Fああ、だからこれは\x01",
            "２人組みの犯行じゃないかと思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x102,
        (
            "#6P#0105Fということは……\x02\x03",

            "片方が客として気を引きつけている隙に\x01",
            "もう片方が売り上げを掠め取る……？\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x104,
        (
            "#12P#0303F成る程な、それを２人が\x01",
            "交互にやってやがるわけだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1261F")

    label("loc_1225F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122CC")

    #C0760
    ChrTalk(
        0x101,
        (
            "#11P#0001Fベテランのスリ……かもしれない。\x02\x03",

            "手口が鮮やかだし、\x01",
            "素人とは考えにくい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1231F")

    label("loc_122CC")


    #C0761
    ChrTalk(
        0x101,
        (
            "#11P#0001F大窃盗団……かもしれない。\x02\x03",

            "手口が鮮やかだし、\x01",
            "素人とは考えにくい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1231F")


    #C0762
    ChrTalk(
        0x102,
        (
            "#6P#0103Fそうね、でも……\x02\x03",

            "#0100F接客中の隙をつく、\x01",
            "という事を考え付けば\x01",
            "素人でもできるかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x101,
        "#11P#0005Fそ、それもそうか。\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x103,
        (
            "#6P#0203F…………………………\x01",
            "気になっていたのですが……\x02\x03",

            "#0200Fどの出店も接客中に\x01",
            "狙われていましたよね？\x02\x03",

            "その接客をしていた相手……\x01",
            "似た様な人物では\x01",
            "ありませんでしたか？\x02\x03",

            "#0203F行政区と港湾公園に現れたのは\x01",
            "軽い感じの青年……\x02\x03",

            "中央広場と歓楽街に現れたのは\x01",
            "喋り好きの青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#12P#0305F言われてみりゃあ、確かに……\x02\x03",

            "#0301Fどこもその２人の客しか\x01",
            "聞かなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x101,
        (
            "#11P#0001F２種類の客の相手を\x01",
            "しているときだけ犯行が起こる……\x01",
            "偶然にしては出来すぎているな。\x02\x03",

            "#0003Fもしかして２人組みの犯行……？\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x102,
        (
            "#6P#0105Fということは……\x02\x03",

            "#0101F例えば、片方が客として\x01",
            "気を引きつけている隙に\x01",
            "もう片方が売り上げを掠め取るとか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1261F")


    #C0768
    ChrTalk(
        0x1A,
        (
            "#5Pむむむ……\x01",
            "それが本当だとすれば\x01",
            "とても見過ごせんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x15,
        "#5Pええ、まったくです……！\x02",
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x15,
        (
            "#5Pはあ、でも青年２人組みといっても\x01",
            "市内に沢山いるでしょうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x15,
        (
            "#5Pまいったなぁ……\x01",
            "出店の皆さんに気をつけてもらうしか\x01",
            "ないんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x101,
        (
            "#11P#0003Fいえ、ここまで分かれば\x01",
            "もっといい方法が採れると思います。\x02\x03",

            "#0001Fなあみんな、\x01",
            "次はどこが狙われると思う？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    #C0773
    ChrTalk(
        0x102,
        (
            "#6P#0101Fそうね……一度狙われた店は\x01",
            "除外していいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x104,
        (
            "#12P#0300Fま、いくらなんでも\x01",
            "バレるだろうしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x103,
        (
            "#6P#0200Fとなると可能性があるのは\x01",
            "まだ被害にあっていない\x01",
            "店舗ですが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1294D")
    OP_2C(0x20, 0x1)

    #C0776
    ChrTalk(
        0x101,
        (
            "#11P#0003F（被害に遭っていない店にも\x01",
            "  聞き込んでおいてよかった。）\x02\x03",

            "#0001F（たしか、狙われそうだったのは……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129C9")

    label("loc_1294D")


    #C0777
    ChrTalk(
        0x101,
        (
            "#11P#0003F（被害に遭っていない店も\x01",
            "  回っておけばよかったかな……）\x02\x03",

            "#0001F（まあ見た所、\x01",
            "  一番狙われそうなのは……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_129C9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【中央広場のスイーツ屋】\x01",      # 0
            "【行政区のオムライス屋】\x01",      # 1
            "【歓楽街のアイス屋】\x01",          # 2
            "【港湾公園のタンメン屋】\x01",      # 3
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12A77"),
        (1, "loc_12E9A"),
        (2, "loc_130B5"),
        (3, "loc_132A1"),
        (SWITCH_DEFAULT, "loc_13432"),
    )


    label("loc_12A77")

    OP_2C(0x20, 0x2)

    #C0778
    ChrTalk(
        0x1A,
        "#5P中央広場のスイーツ屋かね？\x02",
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x101,
        (
            "#11P#0001Fええ、これには理由があります。\x02\x03",

            "#0003F今日はパレードがあるので\x01",
            "行政区の辺りは警官で一杯ですし……\x02\x03",

            "歓楽街の広場や港湾公園は\x01",
            "比較的見通しが良さそうでした。\x02\x03",

            "#0001Fそれに……犯行後の\x01",
            "“逃走のしやすさ”を考えると\x01",
            "やはり狙われ易いのは中央広場かと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(15)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(12)
    OP_63(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0780
    ChrTalk(
        0x104,
        "#12P#0305F逃走のしやすさ……？\x02",
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x101,
        (
            "#11P#0001F出店が何件も被害に遭って\x01",
            "店主も警戒している状況だ。\x02\x03",

            "#0003Fいくら巧妙な手口でも\x01",
            "見咎められる可能性は\x01",
            "高くなっているはず……\x02\x03",

            "#0000Fとなれば、たとえ見つかっても\x01",
            "逃げやすい店舗を狙うと思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x102,
        (
            "#6P#0105Fそういえば……\x02\x03",

            "#0100F被害に遭ったばかりっていう\x01",
            "バーガー屋も、街区の交差点に\x01",
            "店を出していたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x103,
        (
            "#6P#0200F中央広場のスイーツ屋は\x01",
            "裏通りや行政区にもほど近い位置です。\x02\x03",

            "逃走のしやすさという観点からすれば、\x01",
            "一番狙われやすいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x104,
        (
            "#12P#0303Fああ、可能性は高そうだな……\x02\x03",

            "#0300F……よし、ここは一つ\x01",
            "そいつに賭けてみようぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0xE)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 4)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_13432")

    label("loc_12E9A")


    #C0785
    ChrTalk(
        0x1A,
        "#5P行政区のオムライス屋かね？\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x101,
        (
            "#11P#0003Fええ、何となくですが……\x02\x03",

            "今日はパレードがあるため\x01",
            "行政区の辺りは\x01",
            "かなり賑わっています。\x02\x03",

            "#0001Fその人出に乗じて\x01",
            "犯行を行う可能性があるかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x102,
        (
            "#6P#0101Fでもパレードの警備のために\x01",
            "警官が集まっていなかったかしら。\x02\x03",

            "#0103Fいくら注意を引きつけても\x01",
            "あの中で盗みをするのは\x01",
            "相当危険だと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x101,
        (
            "#11P#0006Fうっ……\x01",
            "ちょっと苦しかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x104,
        (
            "#12P#0303Fま、この人ごみの中を\x01",
            "探し回るよりは確実なんじゃねえか？\x02\x03",

            "#0300Fそれに賭けてみようぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x11)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 1)
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_13432")

    label("loc_130B5")


    #C0790
    ChrTalk(
        0x1A,
        "#5P歓楽街のアイス屋かね？\x02",
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x101,
        (
            "#11P#0003Fええ、何となくですが……\x02\x03",

            "歓楽街のアイス屋は\x01",
            "アルカンシェルのすぐ前にあります。\x02\x03",

            "#0001F劇団の公演前後の\x01",
            "人ごみに紛れれば、犯行も可能かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x103,
        (
            "#6P#0205Fですが、それはどちらかと言うと\x01",
            "単独犯の手口なのでは……？\x02\x03",

            "#0200F今までのケースとは方向性が違う気が。\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x101,
        (
            "#11P#0006Fうっ……\x01",
            "ちょっと苦しかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x104,
        (
            "#12P#0303Fま、この人ごみの中を\x01",
            "探し回るよりは確実なんじゃねえか？\x02\x03",

            "#0300Fそれに賭けてみようぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x12)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Jump("loc_13432")

    label("loc_132A1")


    #C0795
    ChrTalk(
        0x1A,
        "#5P港湾公園のタンメン屋かね？\x02",
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x101,
        (
            "#11P#0003Fええ、何となくですが……\x02\x03",

            "#0001F商工会のテントからは\x01",
            "一番近い店ですが……\x01",
            "裏をかかれる可能性もあるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x102,
        (
            "#6P#0103Fよほどスリルの好きな\x01",
            "犯人ということになりそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x101,
        (
            "#11P#0006Fうっ……\x01",
            "ちょっと苦しかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x104,
        (
            "#12P#0303Fま、この人ごみの中を\x01",
            "探し回るよりは確実なんじゃねえか？\x02\x03",

            "#0300Fそれに賭けてみようぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x13)
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 83)
    Jump("loc_13432")

    label("loc_13432")

    Return()

    # Function_77_1135C end

    def Function_78_13433(): pass

    label("Function_78_13433")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32300.itc", 0x28)
    LoadChrToIndex("chr/ch23600.itc", 0x29)
    LoadChrToIndex("chr/ch30000.itc", 0x2A)
    LoadChrToIndex("chr/ch02708.itc", 0x2B)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-20590, 2500, -12420, 0)
    MoveCamera(64, 28, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -19640, 0, -10290, 90)
    SetChrPos(0x102, -18810, 0, -12750, 20)
    SetChrPos(0x103, -19720, 0, -11730, 65)
    SetChrPos(0x104, -17130, 0, -12710, 335)
    SetChrPos(0x1A, -15910, 0, -10370, 245)
    SetChrPos(0x15, -16920, 0, -9360, 200)
    SetChrPos(0x4E, -17790, 0, -11400, 20)
    SetChrPos(0x4F, -18560, 0, -10890, 20)
    SetChrPos(0x50, -19300, 0, -3440, 20)
    SetChrPos(0x51, -20380, 0, -3260, 20)
    SetChrPos(0x52, -15180, 0, -11440, 300)
    SetChrChipByIndex(0x4E, 0x28)
    SetChrSubChip(0x4E, 0x0)
    SetChrChipByIndex(0x4F, 0x29)
    SetChrSubChip(0x4F, 0x0)
    SetChrChipByIndex(0x50, 0x2A)
    SetChrSubChip(0x50, 0x0)
    SetChrChipByIndex(0x51, 0x2A)
    SetChrSubChip(0x51, 0x0)
    SetChrChipByIndex(0x52, 0x2B)
    SetChrSubChip(0x52, 0x0)
    ClearChrFlags(0x4E, 0x80)
    ClearChrBattleFlags(0x4E, 0x8000)
    ClearChrFlags(0x4F, 0x80)
    ClearChrBattleFlags(0x4F, 0x8000)
    ClearChrFlags(0x50, 0x80)
    ClearChrBattleFlags(0x50, 0x8000)
    ClearChrFlags(0x51, 0x80)
    ClearChrBattleFlags(0x51, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135B0")
    ClearChrFlags(0x52, 0x80)
    ClearChrBattleFlags(0x52, 0x8000)

    label("loc_135B0")

    BeginChrThread(0x4E, 0, 0, 79)
    BeginChrThread(0x4F, 0, 0, 79)
    OP_52(0x4E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0800
    ChrTalk(
        0x4E,
        (
            "#11P腰抜け警察のくせに\x01",
            "やってくれんじゃねーかよう！\x02",
        )
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x4F,
        (
            "#5P俺たち《ブラックエンペラー》を\x01",
            "舐めんなよォ！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13726")

    #C0802
    ChrTalk(
        0x52,
        "#11P#1207Fガウ、ガルルルッ……！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x4E, 0x0)
    EndChrThread(0x4F, 0x0)

    def lambda_136B6():
        TurnDirection(0xFE, 0x52, 500)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_136B6)

    def lambda_136C3():
        TurnDirection(0xFE, 0x52, 500)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_136C3)
    Sleep(200)
    OP_63(0x4E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x4F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0803
    ChrTalk(
        0x4E,
        (
            "#11Pひえええ、\x01",
            "す、すんませんでした～っ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13726")


    #C0804
    ChrTalk(
        0x15,
        (
            "#5P売上金は取り返しましたが……\x01",
            "なんだか粋がった連中ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x104,
        (
            "#12P#0306Fだなぁ。\x02\x03",

            "#0300F旧市街の不良どもに掛かりゃあ\x01",
            "一発でビビらされそうだが。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x4E, 0x0)
    EndChrThread(0x4F, 0x0)
    OP_63(0x4E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x4F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_137FE():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_137FE)

    def lambda_1381B():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_1381B)
    Sleep(1200)
    OP_63(0x4E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x4F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)

    #C0806
    ChrTalk(
        0x101,
        "#6P#0005Fあれ、急に大人しくなったな。\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x102,
        (
            "#12P#0105Fもしかして……\x01",
            "本当に不良たちに\x01",
            "脅されてしまったとか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_138D3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_138D3)

    def lambda_138E0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_138E0)
    Sleep(200)

    #C0808
    ChrTalk(
        0x4E,
        (
            "#11Pだ、だ、誰が\x01",
            "あんな連中にビビるか！！\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x4F,
        (
            "#5Pな、舐めた事\x01",
            "抜かしてんじゃねーよォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x103,
        (
            "#6P#0200F直球で図星のようですね。\x02\x03",

            "……なるほど、それで\x01",
            "ムシャクシャしていたから\x01",
            "気晴らしに犯行を重ねたと。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x1A,
        "#11P……そうだったか。\x02",
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x1A,
        (
            "#11Pそれで大勢の人たちに\x01",
            "迷惑をのう……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13A07():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_13A07)

    def lambda_13A14():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_13A14)
    Sleep(300)
    SetCameraDistance(19210, 1600)
    OP_95(0x1A, -16880, 0, -10300, 1000, 0x0)

    def lambda_13A41():
        OP_93(0xFE, 0xF5, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_13A41)
    OP_93(0x1A, 0xF5, 0x190)
    Sleep(300)

    #C0813
    ChrTalk(
        0x1A,
        (
            "#11Pその罪……\x01",
            "償ってもらわんとのう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x4E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x4F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1200)

    #C0814
    ChrTalk(
        0x4E,
        (
            "#12Pううっ……\x01",
            "（なんだこの爺さん……）\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x4F,
        (
            "#6Pゴクリ……\x01",
            "（眼光が怖え……）\x02",
        )
    )

    CloseMessageWindow()

    #N0816
    NpcTalk(
        0x50,
        "声",
        (
            "#4P……いたいた。\x01",
            "君らが特務支援課か。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-19920, 2500, -11390, 2500)
    MoveCamera(53, 31, 0, 2500)
    OP_6E(420, 2500)
    SetCameraDistance(20320, 2500)

    def lambda_13B5B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13B5B)

    def lambda_13B68():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13B68)

    def lambda_13B75():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_13B75)

    def lambda_13B82():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13B82)

    def lambda_13B8F():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_13B8F)

    def lambda_13B9C():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_13B9C)

    def lambda_13BA9():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_13BA9)

    def lambda_13BB6():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_13BB6)

    def lambda_13BC3():
        OP_95(0xFE, -19300, 0, -7440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_13BC3)

    def lambda_13BDD():
        OP_95(0xFE, -20380, 0, -7260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_13BDD)
    Sleep(2500)

    #C0817
    ChrTalk(
        0x50,
        "#11Pすまないな、遅れてしまって。\x02",
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x51,
        (
            "#5P窃盗犯とやらを\x01",
            "引き取りに来てやったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x101,
        (
            "#12P#0001Fすみません、お忙しい所を\x01",
            "呼びたててしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x50,
        "#11Pいやあ構わんさ。\x02",
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x50,
        "#11P……そっちの２人組みでいいのか？\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x101,
        (
            "#12P#0001Fええ、本部までの連行を\x01",
            "お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x51,
        "#5Pよしきた、任せろ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x4E, -19770, 0, -6410, 341)
    SetChrPos(0x4F, -20770, 0, -6710, 0)
    SetChrPos(0x1A, -18220, 0, -9760, 315)
    SetChrPos(0x15, -18050, 0, -8480, 315)
    SetChrPos(0x50, -19220, 0, -7200, 341)
    SetChrPos(0x51, -21370, 0, -7320, 26)
    FadeToBright(1000, 0)
    OP_0D()

    #C0824
    ChrTalk(
        0x50,
        "#11Pほら、キリキリ歩け！\x02",
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x4E,
        "#11Pうおっ、押すなよう！？\x02",
    )

    CloseMessageWindow()

    def lambda_13DDA():

        label("loc_13DDA")

        TurnDirection(0xFE, 0x51, 400)
        Yield()
        Jump("loc_13DDA")

    QueueWorkItem2(0x1A, 1, lambda_13DDA)

    def lambda_13DEC():

        label("loc_13DEC")

        TurnDirection(0xFE, 0x50, 400)
        Yield()
        Jump("loc_13DEC")

    QueueWorkItem2(0x15, 1, lambda_13DEC)

    def lambda_13DFE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_13DFE)

    def lambda_13E0B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_13E0B)

    def lambda_13E18():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_13E18)

    def lambda_13E25():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_13E25)
    Sleep(100)

    def lambda_13E35():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_13E35)

    def lambda_13E4A():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_13E4A)

    def lambda_13E5F():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_13E5F)

    def lambda_13E74():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_13E74)
    Sleep(6000)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x15, 0x1)
    OP_68(-20430, 2500, -11880, 2000)
    MoveCamera(69, 29, 0, 2000)
    OP_6E(420, 2000)
    SetCameraDistance(20320, 2000)

    def lambda_13EC2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13EC2)

    def lambda_13ECF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13ECF)

    def lambda_13EDC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13EDC)

    def lambda_13EE9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13EE9)
    BeginChrThread(0x1A, 1, 0, 80)
    Sleep(100)
    BeginChrThread(0x15, 1, 0, 81)
    Sleep(300)
    SetChrFlags(0x4E, 0x80)
    SetChrBattleFlags(0x4E, 0x8000)
    SetChrFlags(0x4F, 0x80)
    SetChrBattleFlags(0x4F, 0x8000)
    SetChrFlags(0x50, 0x80)
    SetChrBattleFlags(0x50, 0x8000)
    SetChrFlags(0x51, 0x80)
    SetChrBattleFlags(0x51, 0x8000)

    #C0826
    ChrTalk(
        0x15,
        (
            "#5Pふう……ともかく\x01",
            "一件落着ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0x102,
        (
            "#12P#0100F外国人のようなので……\x01",
            "留置所に３日入れておく程度には\x01",
            "なりそうですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x104,
        (
            "#12P#0306Fクロスベルはその辺りが\x01",
            "甘いんだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x1A,
        (
            "#11Pふふ、せっかくの記念祭を\x01",
            "留置所の壁を見詰めて過ごすんじゃ。\x01",
            "それで十分じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x1A,
        (
            "#11Pそれに……ちょっぴり\x01",
            "脅しておいたからのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x103,
        (
            "#6P#0205Fそういえば会長さん、\x01",
            "結構凄みがありましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x1A,
        (
            "#11Pふふ、これでも元は\x01",
            "百戦錬磨の商人じゃ。\x01",
            "ああいう手合いは慣れておるわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x101,
        "#6P#0000Fはは、そうだったんだ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_14304")

    #C0834
    ChrTalk(
        0x1A,
        (
            "#11Pいやはや、しかしわしから見ても\x01",
            "見事な手際じゃったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0x1A,
        "#11P今回の一件、感謝するわい。\x02",
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x15,
        (
            "#5Pそうですね、\x01",
            "本当にお世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x15,
        (
            "#5P商工会として\x01",
            "お礼を言わせて頂きますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあ、いえいえ。\x01",
            "こちらとしても無事\x01",
            "解決できて何よりでした。\x02\x03",

            "はは……また何かあれば\x01",
            "相談してもらえると嬉しいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x1A,
        (
            "#11Pああ、頼りにさせてもらおう。\x01",
            "その時はよろしくのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x102,
        (
            "#12P#0100Fええ、喜んで。\x01",
            "こちらこそよろしく\x01",
            "お願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xF)
    OP_29(0x20, 0x1, 0x10)
    Jump("loc_1466B")

    label("loc_14304")


    #C0841
    ChrTalk(
        0x101,
        (
            "#6P#0006Fすみません、\x01",
            "今回は推理を外してしまいまして。\x02\x03",

            "危うく取り逃す所でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x102,
        (
            "#12P#0106F申し訳ありません、\x01",
            "信頼して頂いていたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0843
    ChrTalk(
        0x1A,
        (
            "#11Pいやいや、無事解決したんじゃ。\x01",
            "よしとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x87, 0x190)

    #C0844
    ChrTalk(
        0x1A,
        (
            "#11Pそれに君達の優秀な警察犬……\x01",
            "ツァイト君だったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x1A,
        (
            "#11P万が一を考えて\x01",
            "出動させておくとは、\x01",
            "やはり君達の手柄じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x101,
        (
            "#6P#0012Fは、ははは……\x01",
            "それは、その……\x02",
        )
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x52,
        "#11P#1203Fグルルルル……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x52, 400)
    Sleep(300)

    #C0848
    ChrTalk(
        0x103,
        "#6P#0203Fまだまだだな、だそうです。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0849
    ChrTalk(
        0x104,
        "#12P#0306Fマジでスミマセンでした。\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0xE1, 0x190)
    OP_63(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(300)

    #C0850
    ChrTalk(
        0x15,
        (
            "#5Pともあれ、今回はお世話になりました。\x01",
            "商工会としてお礼を言わせて頂きますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0x1A,
        (
            "#11Pうむ、また何かあれば\x01",
            "頼むかもしれん。\x01",
            "その時はよろしくのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0x102,
        (
            "#12P#0100Fはい、こちらこそ\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x14)
    OP_29(0x20, 0x1, 0x15)

    label("loc_1466B")

    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0853
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【窃盗事件の捜査依頼】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    SetChrFlags(0x52, 0x80)
    SetChrBattleFlags(0x52, 0x8000)
    OP_49()
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_29(0x20, 0x4, 0x10)
    SetScenarioFlags(0x2, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_78_13433 end

    def Function_79_14777(): pass

    label("Function_79_14777")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_147B7"),
        (1, "loc_147C3"),
        (2, "loc_147CF"),
        (3, "loc_147DB"),
        (4, "loc_147E7"),
        (5, "loc_147F3"),
        (6, "loc_147FF"),
        (SWITCH_DEFAULT, "loc_1480B"),
    )


    label("loc_147B7")

    OP_A0(0xFE, 2450, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_147C3")

    OP_A0(0xFE, 2550, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_147CF")

    OP_A0(0xFE, 2600, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_147DB")

    OP_A0(0xFE, 2400, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_147E7")

    OP_A0(0xFE, 2650, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_147F3")

    OP_A0(0xFE, 2350, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_147FF")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_1480B")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_14817")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1487A")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1484A"),
        (1, "loc_14856"),
        (2, "loc_14862"),
        (SWITCH_DEFAULT, "loc_1486E"),
    )


    label("loc_1484A")

    OP_93(0xFE, 0x2D, 0x1F4)
    Jump("loc_1486E")

    label("loc_14856")

    OP_93(0xFE, 0x10E, 0x1F4)
    Jump("loc_1486E")

    label("loc_14862")

    OP_93(0xFE, 0x87, 0x1F4)
    Jump("loc_1486E")

    label("loc_1486E")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_14817")

    label("loc_1487A")

    Return()

    # Function_79_14777 end

    def Function_80_1487B(): pass

    label("Function_80_1487B")

    OP_95(0xFE, -16940, 0, -10040, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_80_1487B end

    def Function_81_14897(): pass

    label("Function_81_14897")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, -17600, 0, -9230, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_81_14897 end

    def Function_82_148BA(): pass

    label("Function_82_148BA")

    EventBegin(0x0)
    OP_4B(0x10, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(12800, 2510, 10130, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14520, 0)
    SetChrPos(0x101, 14260, 10, 10900, 0)
    SetChrPos(0x102, 15680, 10, 9480, 0)
    SetChrPos(0x103, 15680, 10, 10900, 0)
    SetChrPos(0x104, 14260, 10, 9480, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0854
    ChrTalk(
        0x104,
        (
            "#12P#0309F『ミスラズ・ジェラート』……\x01",
            "ヒュー、美人な姉さんじゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x101,
        (
            "#6P#0006Fランディ、落ち着いてくれ。\x01",
            "ここは被害にあった店のはず……\x02\x03",

            "#0001Fいまは聞き込みが先だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x102,
        (
            "#0100Fすみません、\x01",
            "クロスベル警察の者ですが……\x01",
            "お話を伺ってよろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0857
    ChrTalk(
        0x10,
        "#5Pああ……窃盗事件の話ね？\x02",
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x10,
        (
            "#5Pそうなのよ、やられちゃったわ。\x01",
            "客の相手をしてる間にね。\x02",
        )
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0x103,
        "#12P#0200F接客中の犯行、ですか。\x02",
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0x10,
        (
            "#5Pええ、その時の客って言うのが\x01",
            "外国人風の軽い男でね。\x01",
            "私を口説こうとしてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x10,
        (
            "#5Pあんまりしつこいから\x01",
            "足を踏んづけてやろうとした時に、\x01",
            "背後から誰かの気配を感じたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x10,
        (
            "#5Pでも、少し遅かったわね。\x01",
            "私が振り向いたときには\x01",
            "もうレジは空になっていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x101,
        (
            "#6P#0001Fそれでは詳しい事は\x01",
            "分かりませんね……\x02",
        )
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0x10,
        (
            "#5Pそうなのよ。\x01",
            "私とした事がとんだ失態ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E19")
    OP_68(13510, 2510, 9070, 1200)
    MoveCamera(45, 24, 0, 1200)

    def lambda_14C98():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14C98)

    def lambda_14CA5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14CA5)

    def lambda_14CB2():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14CB2)

    def lambda_14CBF():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14CBF)
    Sleep(1200)

    #C0865
    ChrTalk(
        0x101,
        "#6P#0003F聞き込みはこんな所かな……\x02",
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x104,
        (
            "#12P#0300Fだな、そろそろ戻って\x01",
            "整理してみようぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14E13")

    #C0867
    ChrTalk(
        0x102,
        (
            "#0100F商工会から連絡もないし、\x01",
            "まだ次の犯行は\x01",
            "行われてないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0x103,
        (
            "#11P#0203Fですね。\x02\x03",

            "#0200F……念のため、\x01",
            "出店を見て回りながら戻った方が\x01",
            "いいかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E13")

    OP_29(0x20, 0x1, 0xD)

    label("loc_14E19")

    OP_5A()
    SetChrPos(0x0, 14780, 10, 10480, 0)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_82_148BA end

    def Function_83_14E3C(): pass

    label("Function_83_14E3C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    SoundLoad(806)
    OP_68(-12140, 2500, 10400, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(31380, 0)
    SetChrPos(0x101, -2510, -700, 2200, 315)
    SetChrPos(0x102, -3310, -700, 3000, 315)
    SetChrPos(0x103, -3710, -700, 1390, 315)
    SetChrPos(0x104, -4520, -700, 2180, 315)
    SetChrPos(0x44, -10280, 0, 11510, 0)
    SetChrPos(0x45, 1440, 0, 10420, 45)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x45, 0x4)
    SetChrChipByIndex(0x44, 0x18)
    SetChrSubChip(0x44, 0x0)
    SetChrChipByIndex(0x45, 0x9)
    SetChrSubChip(0x45, 0x0)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrName("")

    #A0869
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達は目星をつけた街区へ向かい\x01",
            "張り込みを行う事にした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-12140, 1500, 10400, 2800)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    BeginChrThread(0x9, 1, 0, 84)
    Sleep(150)
    BeginChrThread(0x44, 1, 0, 84)
    OP_0D()
    OP_6F(0x1)

    #A0870
    AnonymousTalk(
        0x101,
        (
            "#0001F………………………………\x02\x03",

            "この客じゃなさそうだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x44, 0x1)
    OP_64(0x9)
    OP_64(0x44)
    Sleep(200)
    OP_95(0x44, 1370, 0, 11710, 1500, 0x0)
    Sleep(1800)
    OP_95(0x45, -10170, 0, 10420, 1500, 0x0)
    OP_95(0x45, -10170, 0, 11550, 1500, 0x0)
    BeginChrThread(0x9, 1, 0, 84)
    Sleep(150)
    BeginChrThread(0x45, 1, 0, 84)
    Sleep(2500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x45, 0x1)
    OP_64(0x9)
    OP_64(0x45)
    Sleep(200)
    OP_95(0x45, -14300, 0, 13120, 1500, 0x0)
    OP_95(0x45, -14300, 2000, 23040, 1500, 0x0)
    SetChrFlags(0x44, 0x80)
    SetChrBattleFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x80)
    SetChrBattleFlags(0x45, 0x8000)

    #A0871
    AnonymousTalk(
        0x104,
        "#0306F来ねえな……\x02",
    )

    CloseMessageWindow()

    #A0872
    AnonymousTalk(
        0x103,
        (
            "#0200Fもう１時間以上\x01",
            "張り込んでいますが……\x02",
        )
    )

    CloseMessageWindow()

    #A0873
    AnonymousTalk(
        0x101,
        (
            "#0001Fおかしいな、もう来ても\x01",
            "いいはずなんだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(800)
    Fade(300)
    OP_68(-4170, 1840, 1020, 0)
    MoveCamera(3, 17, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13040, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0x87, 0x190)
    Sleep(50)

    def lambda_15175():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15175)

    def lambda_15182():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15182)

    def lambda_1518F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1518F)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0874
    ChrTalk(
        0x101,
        (
            "#11P#0003Fはい、ロイド・バニングス──\x02\x03",

            "#0005Fえっ、窃盗犯が現れた……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0875
    ChrTalk(
        0x101,
        (
            "#11P#0001Fはい、はい、中央広場ですね。\x02\x03",

            "判りました、すぐに急行します！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)
    Sleep(200)

    #C0876
    ChrTalk(
        0x101,
        (
            "#11P#0006F……みんなゴメン。\x01",
            "読みが外れたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0877
    ChrTalk(
        0x102,
        "#5P#0101Fいいから急ぎましょう、ロイド！\x02",
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x101,
        (
            "#11P#0001Fそ、そうだな。\x01",
            "今は現場に急ごう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1537C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1537C)

    def lambda_15389():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_15389)

    def lambda_15396():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_15396)

    def lambda_153A3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_153A3)
    Sleep(300)

    def lambda_153B3():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_153B3)

    def lambda_153C8():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_153C8)

    def lambda_153DD():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_153DD)

    def lambda_153F2():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_153F2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_14E3C end

    def Function_84_1541F(): pass

    label("Function_84_1541F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15444")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_84_1541F")

    label("loc_15444")

    Return()

    # Function_84_1541F end

    def Function_85_15445(): pass

    label("Function_85_15445")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0879
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　《ルピナス川・第一灯台》\x01\x01",
            "関係者以外の立ち入りを禁ずる。\x01",
            "　　　　　　～クロスベル市～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_85_15445 end

    def Function_86_154D5(): pass

    label("Function_86_154D5")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0880
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっており、\x01",
            "メッセージプレートが付いている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0881
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《黒月貿易公司・クロスベル支社》\x01",
            "※ご用命の方はノックしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_86_154D5 end

    SaveToFile()

Try(main)
