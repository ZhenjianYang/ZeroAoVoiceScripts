from ZeroScenarioHelper import *

def main():
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
        "库妮娅",                 # 1
        "奥赛尔",                 # 2
        "毕肖普",                 # 3
        "奎因老人",               # 4
        "亚米萨",                 # 5
        "格蕾丝",                 # 6
        "雷因兹",                 # 7
        "水上巴士向导",           # 8
        "米斯拉",                 # 9
        "也基",                   # 10
        "米萨",                   # 11
        "工商协会干部",           # 12
        "主持人",                 # 13
        "工商协会服务员",         # 14
        "洛依",                   # 15
        "洛依",                   # 16
        "梅琳",                   # 17
        "梅琳",                   # 18
        "摩尔斯会长",             # 19
        "帕拉夫人",               # 20
        "小桃",                   # 21
        "爱尔莎",                 # 22
        "艾玛搜查官",             # 23
        "安敦",                   # 24
        "利库斯",                 # 25
        "游客",                   # 26
        "男孩",                   # 27
        "游客",                   # 28
        "游客",                   # 29
        "游客",                   # 30
        "游客",                   # 31
        "女孩",                   # 32
        "游客",                   # 33
        "游客",                   # 34
        "阿蕾莎",                 # 35
        "史蒂芬",                 # 36
        "街头艺人",               # 37
        "歌手",                   # 38
        "瓦鲁多",                 # 39
        "诺加诺夫",               # 40
        "杰德",                   # 41
        "修伊",                   # 42
        "斯拉修",                 # 43
        "雾香",                   # 44
        "雷克特",                 # 45
        "水上巴士",               # 46
        "艾丝蒂尔",               # 47
        "约修亚",                 # 48
        "瓦吉",                   # 49
        "阿巴斯",                 # 50
        "圣书会的青年",           # 51
        "圣书会的青年",           # 52
        "圣书会的青年",           # 53
        "圣书会的青年",           # 54
        "圣书会的青年",           # 55
        "剑蛇帮的青年",           # 56
        "剑蛇帮的青年",           # 57
        "剑蛇帮的青年",           # 58
        "剑蛇帮的青年",           # 59
        "剑蛇帮的青年",           # 60
        "客人",                   # 61
        "客人",                   # 62
        "客人",                   # 63
        "客人",                   # 64
        "客人",                   # 65
        "客人",                   # 66
        "客人",                   # 67
        "客人",                   # 68
        "客人",                   # 69
        "客人",                   # 70
        "青年",                   # 71
        "青年",                   # 72
        "警官",                   # 73
        "警官",                   # 74
        "蔡特",                   # 75
        "SE控制",                 # 76
        "中央广场",               # 77
        "西街",                   # 78
        "行政区",                 # 79
        "住宅街",                 # 80
        "欢乐街",                 # 81
        "东街",                   # 82
        "旧城区",                 # 83
        "港湾区",                 # 84
        "ＩＢＣ",                 # 85
        "站前街道",               # 86
        "后巷",                   # 87
        "乌尔斯拉间道",           # 88
        "东克洛斯贝尔街道",       # 89
        "西克洛斯贝尔街道",       # 90
        "玛因兹山道",             # 91
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

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "中央广场")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "西街")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "住宅街")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "欢乐街")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "东街")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "旧城区")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "站前街道")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "后巷")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "玛因兹山道")
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
        "Function_13_2290",        # 0D, 13
        "Function_14_28AB",        # 0E, 14
        "Function_15_2B4F",        # 0F, 15
        "Function_16_2D96",        # 10, 16
        "Function_17_2FAC",        # 11, 17
        "Function_18_2FFC",        # 12, 18
        "Function_19_32CC",        # 13, 19
        "Function_20_34AF",        # 14, 20
        "Function_21_3C09",        # 15, 21
        "Function_22_41F9",        # 16, 22
        "Function_23_4705",        # 17, 23
        "Function_24_4BE9",        # 18, 24
        "Function_25_5058",        # 19, 25
        "Function_26_506D",        # 1A, 26
        "Function_27_57B3",        # 1B, 27
        "Function_28_584F",        # 1C, 28
        "Function_29_58D1",        # 1D, 29
        "Function_30_5BB0",        # 1E, 30
        "Function_31_6030",        # 1F, 31
        "Function_32_605B",        # 20, 32
        "Function_33_63FA",        # 21, 33
        "Function_34_6E8D",        # 22, 34
        "Function_35_6F01",        # 23, 35
        "Function_36_709E",        # 24, 36
        "Function_37_719E",        # 25, 37
        "Function_38_7354",        # 26, 38
        "Function_39_752C",        # 27, 39
        "Function_40_764B",        # 28, 40
        "Function_41_77B8",        # 29, 41
        "Function_42_7911",        # 2A, 42
        "Function_43_7979",        # 2B, 43
        "Function_44_79EC",        # 2C, 44
        "Function_45_7AE5",        # 2D, 45
        "Function_46_7C7E",        # 2E, 46
        "Function_47_8175",        # 2F, 47
        "Function_48_86D7",        # 30, 48
        "Function_49_8B4C",        # 31, 49
        "Function_50_8C69",        # 32, 50
        "Function_51_8EA9",        # 33, 51
        "Function_52_8FA0",        # 34, 52
        "Function_53_9042",        # 35, 53
        "Function_54_910C",        # 36, 54
        "Function_55_920C",        # 37, 55
        "Function_56_92B8",        # 38, 56
        "Function_57_9380",        # 39, 57
        "Function_58_99F9",        # 3A, 58
        "Function_59_A258",        # 3B, 59
        "Function_60_BDD1",        # 3C, 60
        "Function_61_BE00",        # 3D, 61
        "Function_62_BE52",        # 3E, 62
        "Function_63_BEA4",        # 3F, 63
        "Function_64_BEF1",        # 40, 64
        "Function_65_BF83",        # 41, 65
        "Function_66_C095",        # 42, 66
        "Function_67_C1A7",        # 43, 67
        "Function_68_C1EB",        # 44, 68
        "Function_69_C21B",        # 45, 69
        "Function_70_C25F",        # 46, 70
        "Function_71_C28F",        # 47, 71
        "Function_72_C4AA",        # 48, 72
        "Function_73_EC04",        # 49, 73
        "Function_74_EC89",        # 4A, 74
        "Function_75_F020",        # 4B, 75
        "Function_76_F9BB",        # 4C, 76
        "Function_77_FF0E",        # 4D, 77
        "Function_78_11E61",       # 4E, 78
        "Function_79_130D9",       # 4F, 79
        "Function_80_131DD",       # 50, 80
        "Function_81_131F9",       # 51, 81
        "Function_82_1321C",       # 52, 82
        "Function_83_13730",       # 53, 83
        "Function_84_13CE7",       # 54, 84
        "Function_85_13D0D",       # 55, 85
        "Function_86_13D8D",       # 56, 86
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20A9")

    #C0001
    ChrTalk(
        0xFE,
        "……嘿，听说了吗？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "今天的活动最后会有\x01",
            "抢零食大赛呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0003
    ChrTalk(
        0xFE,
        (
            "真是期待啊～\x01",
            "一定要参加才行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_20A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2108")

    #C0004
    ChrTalk(
        0xFE,
        "啊呀，又有不良少年出现了……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "那些孩子，莫非只是想吸引\x01",
            "别人的注意力吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_2108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2163")

    #C0006
    ChrTalk(
        0xFE,
        (
            "今天的舞台是可以\x01",
            "随时上场参加的。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "呵呵，我是不是也该去挑战一下呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_2163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21AE")

    #C0008
    ChrTalk(
        0xFE,
        (
            "难得可以做些\x01",
            "有趣的事，\x01",
            "必须要先占个好地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F4")

    label("loc_21AE")


    #C0009
    ChrTalk(
        0xFE,
        (
            "嗯～这么多人，\x01",
            "都看不清楚舞台呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "哪里有好点的位置啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_21F4")

    Jump("loc_228C")

    label("loc_21F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_222E")

    #C0011
    ChrTalk(
        0xFE,
        (
            "今天也会有什么活动吧，\x01",
            "真期待啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228C")

    label("loc_222E")


    #C0012
    ChrTalk(
        0xFE,
        (
            "昨天，那里的舞台\x01",
            "有场演唱会呢，\x01",
            "气氛相当热闹的。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "呵呵，我对这种活动\x01",
            "最感兴趣了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_228C")

    TalkEnd(0xFE)
    Return()

    # Function_12_2021 end

    def Function_13_2290(): pass

    label("Function_13_2290")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_229D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22ED")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_22ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230D")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28A2")

    label("loc_230D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2321")
    Jump("loc_28A2")

    label("loc_2321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2382")

    #C0014
    ChrTalk(
        0xFE,
        (
            "你们也来尝尝吧，\x01",
            "纪念庆典中最后的机会了哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2404")

    label("loc_2382")


    #C0015
    ChrTalk(
        0xFE,
        (
            "在纪念庆典的最终日，\x01",
            "每年都会有很多游客去米修拉姆游玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "港湾公园也比往常热闹很多。\x01",
            "……呵呵，面条也因此\x01",
            "卖得很好呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2404")

    Jump("loc_28A2")

    label("loc_2409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2442")

    #C0017
    ChrTalk(
        0xFE,
        (
            "好难听的歌……\x01",
            "这简直就是妨碍营业啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A2")

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2783")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_24C3")

    #C0018
    ChrTalk(
        0xFE,
        (
            "听说盗窃案的犯人\x01",
            "被抓到了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "哼，这就是恶有恶报，\x01",
            "干坏事必遭报应。\x01",
            "可恶的犯人，好好反省吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_277E")

    label("loc_24C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2712")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267A")

    #C0020
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，能不能\x01",
            "稍微向您打听一些情况？\x02\x03",

            "我们正在对盗窃案\x01",
            "进行调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "嗯嗯，那个我也听说了。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "如果犯人敢来我的店，\x01",
            "我马上就把他按倒在地！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003F那个，我并不是想说这个。\x01",
            "请问您有没有什么关于犯人的线索呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "嗯嗯，线索吗……\x02",
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
            "完全没有呢，\x01",
            "毕竟人这么多。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#0101F说得也是啊……\x01",
            "那个，谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xB)
    Jump("loc_270D")

    label("loc_267A")


    #C0028
    ChrTalk(
        0xFE,
        (
            "趁着庆典而不断作案，\x01",
            "犯人肯定是个相当恶劣的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "如果敢来我的店，\x01",
            "马上就把他按倒在地！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0000F（这家店看起来\x01",
            "  好像没有遭窃呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270D")

    Jump("loc_277E")

    label("loc_2712")


    #C0031
    ChrTalk(
        0xFE,
        (
            "似乎从昨天开始，就不断出现\x01",
            "以露天店为目标的盗窃案。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "唔唔唔……岂有此理。\x01",
            "我真想亲手把犯人抓住……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_277E")

    Jump("loc_28A2")

    label("loc_2783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2810")

    #C0033
    ChrTalk(
        0xFE,
        (
            "这种跟不上潮流的露天店，\x01",
            "果然还是竞争不过那些\x01",
            "冰激凌店和爆米花店。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "……但我才不在乎。\x01",
            "我可是抱着坚定的信念来开店的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A2")

    label("loc_2810")


    #C0035
    ChrTalk(
        0xFE,
        (
            "其实你们根本就没吃过正宗的汤面，\x01",
            "不信的话，可以来尝尝我这里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "哼……你们听清了吧？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "和那些随处可见的普通面条\x01",
            "可是完全不一样的哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A2")

    Jump("loc_229D")

    label("loc_28A7")

    TalkEnd(0xFE)
    Return()

    # Function_13_2290 end

    def Function_14_28AB(): pass

    label("Function_14_28AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_28FD")

    #C0038
    ChrTalk(
        0xFE,
        "今天全家出行的人很多啊。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "果然是想要去\x01",
            "米修拉姆游玩吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B4B")

    label("loc_28FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_29C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2952")

    #C0040
    ChrTalk(
        0xFE,
        "徒步也有徒步的好处。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "……虽然，走着去确实会很累啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29BB")

    label("loc_2952")


    #C0042
    ChrTalk(
        0xFE,
        (
            "在这种拥挤的时候，步行的送货员就\x01",
            "可以走小路、抄近道。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "绝对不会输给那些\x01",
            "使用导力车的运送员！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_29BB")

    Jump("loc_2B4B")

    label("loc_29C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_29FA")

    #C0044
    ChrTalk(
        0xFE,
        (
            "呼……要趁现在\x01",
            "赶快配送完啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A69")

    label("loc_29FA")


    #C0045
    ChrTalk(
        0xFE,
        (
            "……游行时期的交通管制\x01",
            "可能会对配送的准时度造成影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "所以，在游行开始之前，\x01",
            "要尽全力多送一点啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2A69")

    Jump("loc_2B4B")

    label("loc_2A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2ABC")

    #C0047
    ChrTalk(
        0xFE,
        (
            "他们要是如此精力过剩的话，\x01",
            "不如来帮我做点工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B06")

    label("loc_2ABC")


    #C0048
    ChrTalk(
        0xFE,
        (
            "听说公园的正中地带\x01",
            "昨天发生了骚乱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "是不良团伙干的好事吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2B06")

    Jump("loc_2B4B")

    label("loc_2B0B")


    #C0050
    ChrTalk(
        0xFE,
        "在纪念庆典期间也没有休假。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "……最痛苦的事莫过于此啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2B4B")

    TalkEnd(0xFE)
    Return()

    # Function_14_28AB end

    def Function_15_2B4F(): pass

    label("Function_15_2B4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2BC7")

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
            "虽然这么说有些对不起孙女，\x01",
            "但我很讨厌那些\x01",
            "时髦新奇的游戏。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2BC7")


    #C0054
    ChrTalk(
        0xFE,
        (
            "可恶的ＩＢＣ……\x01",
            "竟然把我的钓鱼点给……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "我才不管什么米修拉姆，\x01",
            "总之他们是一群让人生气的家伙……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2C34")

    Jump("loc_2D92")

    label("loc_2C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2C68")

    #C0056
    ChrTalk(
        0xFE,
        (
            "真是吵闹啊……\x01",
            "让人头疼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D92")

    label("loc_2C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CA1")

    #C0057
    ChrTalk(
        0xFE,
        (
            "……不要，\x01",
            "我对游行之类的东西没兴趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D92")

    label("loc_2CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2CD4")

    #C0058
    ChrTalk(
        0xFE,
        (
            "我已经决定要像这样\x01",
            "度过余生了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D92")

    label("loc_2CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2D2D")

    #C0059
    ChrTalk(
        0xFE,
        (
            "运营那个水上巴士的\x01",
            "好像是ＩＢＣ吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "……我决定了，我讨厌ＩＢＣ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D92")

    label("loc_2D2D")


    #C0061
    ChrTalk(
        0xFE,
        "哇啊啊……！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "真是的～～……\x01",
            "好吵闹的一群家伙！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "我正在享受垂钓呢，\x01",
            "难道没看出来吗！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2D92")

    TalkEnd(0xFE)
    Return()

    # Function_15_2B4F end

    def Function_16_2D96(): pass

    label("Function_16_2D96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E06")

    #C0064
    ChrTalk(
        0xFE,
        (
            "米修拉姆吗……\x01",
            "我也想去看看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "嘿嘿，不过，\x01",
            "看爷爷这种态度，\x01",
            "就算求他也是没用的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FA8")

    label("loc_2E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2E59")

    #C0066
    ChrTalk(
        0xFE,
        "哎？总觉得很吵闹呢……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "舞台那边好像\x01",
            "正在举办什么活动吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FA8")

    label("loc_2E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2EAE")

    #C0068
    ChrTalk(
        0xFE,
        (
            "听说啊，今年的游行队伍\x01",
            "将会超级华丽呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "那个，一起去看看吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FA8")

    label("loc_2EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2F11")

    #C0070
    ChrTalk(
        0xFE,
        (
            "本来想和爷爷一起\x01",
            "去玩的……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "但照现在的情况看，\x01",
            "根本就叫不动他嘛。\x01",
            "呼～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FA8")

    label("loc_2F11")

    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0072
    ChrTalk(
        0xFE,
        "爷爷也一起去转转啦！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xB,
        "……不要。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "我有想去的地方呢。\x01",
            "爷爷，带我去啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        "……不要。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "真是的～实在太顽固了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x10)

    label("loc_2FA8")

    TalkEnd(0xFE)
    Return()

    # Function_16_2D96 end

    def Function_17_2FAC(): pass

    label("Function_17_2FAC")

    TalkBegin(0xFE)

    #C0077
    ChrTalk(
        0xFE,
        "（咔嚓，咔嚓）……！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "嗯，这张照片好像\x01",
            "可以用在文化报道方面吧¤\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2FAC end

    def Function_18_2FFC(): pass

    label("Function_18_2FFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_END)), "loc_3142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_309D")

    #C0079
    ChrTalk(
        0xD,
        (
            "#2100F啊，对了对了，\x01",
            "关于那个拍照的委托，如果照片数量够了，\x01",
            "就拿到通讯社的接待处去吧。\x02\x03",

            "#2109F拜托你们了哦～¤\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    Jump("loc_313D")

    label("loc_309D")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0080
    ChrTalk(
        0xD,
        (
            "#2100F那么～继续昨天的工作，\x01",
            "去捕捉纪念庆典中各种热闹的\x01",
            "的场面吧～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 300)

    #C0081
    ChrTalk(
        0xD,
        "#2109F雷因兹，跟上我啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)

    #C0082
    ChrTalk(
        0xE,
        "了、了解！\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 6)

    label("loc_313D")

    Jump("loc_32C8")

    label("loc_3142")


    #C0083
    ChrTalk(
        0xD,
        (
            "#2100FＨｅｌｌｏ～昨天辛苦啦！\x02\x03",

            "#2109F我会尽快将昨天的竞赛\x01",
            "写成一篇有趣的报道哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0006F格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0306F果然要将那个\x01",
            "写成报道吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xD,
        (
            "#2104F对对，应该会登在纪念庆典最终日\x01",
            "发行的临时特别刊上。\x02\x03",

            "#2100F到时一定会把你们的活跃展示给大家，\x01",
            "请尽情期待吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0006F（她的文章，表面上像是在赞扬我们，\x01",
            "  其实绝对是想让我们难堪吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        "#0200F（算了，反正一向如此。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 0)

    label("loc_32C8")

    TalkEnd(0xFE)
    Return()

    # Function_18_2FFC end

    def Function_19_32CC(): pass

    label("Function_19_32CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3335")

    #C0089
    ChrTalk(
        0xFE,
        (
            "前往米修拉姆的水上巴士\x01",
            "马上就要靠岸了～\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "请需要乘坐的客人们\x01",
            "再耐心稍等一下～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AB")

    label("loc_3335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3397")

    #C0091
    ChrTalk(
        0xFE,
        (
            "呼，我也想和家人\x01",
            "一起去玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "……等纪念庆典结束之后，\x01",
            "就去申请个休假好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AB")

    label("loc_3397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_33F2")

    #C0093
    ChrTalk(
        0xFE,
        (
            "前往米修拉姆的水上巴士\x01",
            "即将出航～！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "请需要乘坐的客人们抓紧时间～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AB")

    label("loc_33F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_344F")

    #C0095
    ChrTalk(
        0xFE,
        (
            "距离前往米修拉姆的水上巴士靠岸，\x01",
            "还剩下最后五分种。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "请您再稍等片刻～\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AB")

    label("loc_344F")


    #C0097
    ChrTalk(
        0xFE,
        (
            "若要乘坐前往米修拉姆的水上巴士，\x01",
            "请来这边的站台～！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "需要乘坐的客人\x01",
            "请抓紧时间～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34AB")

    TalkEnd(0xFE)
    Return()

    # Function_19_32CC end

    def Function_20_34AF(): pass

    label("Function_20_34AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34D9")
    Call(0, 82)
    Return()

    label("loc_34D9")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_34E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C05")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3536")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3536")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3556")
    OP_AF(0x7D)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C00")

    label("loc_3556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_356A")
    Jump("loc_3C00")

    label("loc_356A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C00")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_365E")

    #C0099
    ChrTalk(
        0xFE,
        (
            "你们几个将盗窃犯\x01",
            "给抓住了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "呵呵，很能干嘛。\x01",
            "谢谢啦。\x02",
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
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('冰凉甜点『七彩』', 1)

    #C0102
    ChrTalk(
        0xFE,
        (
            "请收下吧，\x01",
            "这是谢礼。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        "#0100F谢谢您。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 1)
    Jump("loc_3C00")

    label("loc_365E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370F")

    #C0104
    ChrTalk(
        0xFE,
        (
            "呵呵，欢迎欢迎，\x01",
            "欢迎光临米斯拉的雪糕车。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "我的手制冰激凌堪称一流哦，\x01",
            "在雷米菲利亚公国可是\x01",
            "被称为『皇室御用』的品牌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "有兴趣的话，欢迎品尝哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 4)
    Jump("loc_3C00")

    label("loc_370F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3871")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F3")

    #C0107
    ChrTalk(
        0xFE,
        "今天就是纪念庆典的最终日了啊。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "呵呵，机会难得，\x01",
            "就把我们店手制冰激凌\x01",
            "的做法教给你吧。\x02",
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
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x13)
    Jump("loc_386C")

    label("loc_37F3")


    #C0111
    ChrTalk(
        0xFE,
        "今天就是纪念庆典的最终日了……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "四处漂泊的雪糕店『米斯拉』\x01",
            "过了今天也就要消失啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "想买的客人请抓紧机会哦。\x02",
    )

    CloseMessageWindow()

    label("loc_386C")

    Jump("loc_3C00")

    label("loc_3871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_38DD")

    #C0114
    ChrTalk(
        0xFE,
        (
            "虽然听说过会有游行，\x01",
            "但没想到能有这种规模呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的人\x01",
            "好像很喜欢大场面呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C00")

    label("loc_38DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3AF7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3955")

    #C0116
    ChrTalk(
        0xFE,
        (
            "那么，游行活动好像差不多\x01",
            "就要开始了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "呵呵，客人似乎也会增加不少。\x01",
            "我也很期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF2")

    label("loc_3955")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39BE")

    #C0118
    ChrTalk(
        0xFE,
        (
            "……没想到盗窃犯会趁我\x01",
            "接待客人时下手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        "我真是太不小心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF2")

    label("loc_39BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3A34")

    #C0120
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔真是个\x01",
            "充满刺激的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "呵呵，一想到庆典即将结束，\x01",
            "都感觉有些哀伤了，真舍不得啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF2")

    label("loc_3A34")


    #C0122
    ChrTalk(
        0xFE,
        (
            "全世界的人都\x01",
            "汇聚到了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "在享受一场梦幻般的庆典后，\x01",
            "然后各自回到自己的国家……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "呵呵，这里真是个有意思的地方呢。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "在我至今为止去过的场所中，\x01",
            "这里最令人兴奋了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_3AF2")

    Jump("loc_3C00")

    label("loc_3AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3B48")

    #C0126
    ChrTalk(
        0xFE,
        (
            "呵呵，昨天\x01",
            "真是不得了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "传言都流到\x01",
            "这边了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B8B")

    label("loc_3B48")


    #C0128
    ChrTalk(
        0xFE,
        "哎呀，你们不是昨天的英雄吗？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "怎么样，算你们便宜点吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_3B8B")

    Jump("loc_3C00")

    label("loc_3B90")


    #C0130
    ChrTalk(
        0xFE,
        (
            "我的手制冰激凌堪称一流哦，\x01",
            "在雷米菲利亚公国可是\x01",
            "被称为『皇室御用』的品牌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        "有兴趣的话，欢迎品尝哦。\x02",
    )

    CloseMessageWindow()

    label("loc_3C00")

    Jump("loc_34E6")

    label("loc_3C05")

    TalkEnd(0xFE)
    Return()

    # Function_20_34AF end

    def Function_21_3C09(): pass

    label("Function_21_3C09")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C66")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3C66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C86")
    OP_AF(0x7C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41F0")

    label("loc_3C86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C9A")
    Jump("loc_41F0")

    label("loc_3C9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3D0A")

    #C0132
    ChrTalk(
        0xFE,
        "……来份牛排怎么样？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "在庆典的最后，要尽情享受一下哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D6E")

    label("loc_3D0A")


    #C0134
    ChrTalk(
        0xFE,
        "今天是庆典的最后一天了。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "我们也觉得很失落呢。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "这种心情应该就是\x01",
            "所谓的恋恋不舍吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_3D6E")

    Jump("loc_41F0")

    label("loc_3D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3DA4")

    #C0137
    ChrTalk(
        0xFE,
        (
            "哎呀……\x01",
            "舞台那边好像很乱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F0")

    label("loc_3DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4169")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3E12")

    #C0138
    ChrTalk(
        0xFE,
        (
            "您好，欢迎光临。\x01",
            "要不要来份串烧牛排呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "我们这里有美味无比的\x01",
            "串烧牛排哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4164")

    label("loc_3E12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_410F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A2")

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，能稍微\x01",
            "问您几句话吗？\x02\x03",

            "我们正在对盗窃案\x01",
            "进行调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "那、那件事啊。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "我觉得我们店应该比较安全，\x01",
            "因为我和妹妹两个人一起看店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "如果只有一个人，\x01",
            "再怎么警惕也都会给人以可乘之机吧。\x01",
            "所以，如果有两个人的话，就万无一失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        (
            "#0101F请问您有没有在这附近看到过\x01",
            "奇怪的可疑人物呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "那、那个嘛……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "从刚才开始，就有群穿着\x01",
            "红色衣服的青年一直在那边转悠。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "我已经注意很久了，\x01",
            "他们究竟是什么人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        "#0300F那些家伙吗，应该和这件事无关。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        (
            "#0203F他们应该不会做出盗窃这种\x01",
            "卑鄙的行为。\x02\x03",

            "#0200F不过，如果他们惹出什么事，\x01",
            "就请作为别起案件来通报吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "了、了解。\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xC)
    Jump("loc_410A")

    label("loc_40A2")


    #C0151
    ChrTalk(
        0xFE,
        (
            "纪念庆典中，客人实在太多了，\x01",
            "要说可疑人物的话，真是想不出。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "……我就祈祷盗窃犯\x01",
            "别来我这里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410A")

    Jump("loc_4164")

    label("loc_410F")


    #C0153
    ChrTalk(
        0xFE,
        (
            "我们为了克洛斯贝尔\x01",
            "的庆典，特意从\x01",
            "东方赶来。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "果然如我所想，\x01",
            "生意非常红火。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4164")

    Jump("loc_41F0")

    label("loc_4169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_41A5")

    #C0155
    ChrTalk(
        0xFE,
        "妹妹很擅长招揽客人。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "帮了我大忙呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41F0")

    label("loc_41A5")


    #C0157
    ChrTalk(
        0xFE,
        "呀，要不要来份串烧牛排呢？\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "香嫩美味、入口即化，\x01",
            "是最棒的牛排哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F0")

    Jump("loc_3C16")

    label("loc_41F5")

    TalkEnd(0xFE)
    Return()

    # Function_21_3C09 end

    def Function_22_41F9(): pass

    label("Function_22_41F9")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4701")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4256")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4276")
    OP_AF(0x7C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46FC")

    label("loc_4276")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_428A")
    Jump("loc_46FC")

    label("loc_428A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4311")

    #C0159
    ChrTalk(
        0xFE,
        (
            "哎～莫非那位就是\x01",
            "舞台活动的主办人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "看起来就是个很普通的老爷爷嘛。\x01",
            "稍微有些吃惊呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46FC")

    label("loc_4311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_438E")

    #C0161
    ChrTalk(
        0xFE,
        (
            "嘿，今天供应\x01",
            "多种饮料套餐哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "各位口渴的客人们\x01",
            "不来喝点吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "饮料套餐，\x01",
            "便宜划算，快来买吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46FC")

    label("loc_438E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4532")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_444E")

    #C0164
    ChrTalk(
        0xFE,
        (
            "那个连环盗窃犯\x01",
            "好像已经被抓到了？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "哎呀呀，这下就能稍微\x01",
            "安下心来做生意了～\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "不过，反正克洛斯贝尔\x01",
            "一向都有很多麻烦事。\x01",
            "特别是在纪念庆典，更不能掉以轻心～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452D")

    label("loc_444E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44FA")

    #C0167
    ChrTalk(
        0xFE,
        (
            "工商协会的人过来\x01",
            "提醒我们多小心\x01",
            "盗窃犯。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的治安\x01",
            "果然不怎么样～\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "要是被盗，努力可就付诸东流了。\x01",
            "必须要保持警惕啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_452D")

    label("loc_44FA")


    #C0170
    ChrTalk(
        0xFE,
        (
            "今天来了很多\x01",
            "警察呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "发生什么事了吗～？\x02",
    )

    CloseMessageWindow()

    label("loc_452D")

    Jump("loc_46FC")

    label("loc_4532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4595")

    #C0172
    ChrTalk(
        0xFE,
        (
            "好啦，想买东西的话\x01",
            "就快点买吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "再磨磨蹭蹭的，\x01",
            "太阳就要下山了啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4604")

    label("loc_4595")


    #C0174
    ChrTalk(
        0xFE,
        (
            "嘿，小兄弟，\x01",
            "有没有觉得肚子饿啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "这种时候，\x01",
            "就来份串烧牛排吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "边吃边逛才能尽情享受庆典啦！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_4604")

    Jump("loc_46FC")

    label("loc_4609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_467A")

    #C0177
    ChrTalk(
        0xFE,
        "参加庆典怎么可以不吃串烧呢！\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "手里拿着串烧，边走边吃，\x01",
            "逛庆典的乐趣自然会加倍啊，小兄弟！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46FC")

    label("loc_467A")


    #C0179
    ChrTalk(
        0xFE,
        (
            "哎呀，庆典快乐，庆典快乐。\x01",
            "今天可是快乐的庆典日啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "参加庆典，当然不能不吃串烧牛排啦！\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "来，小兄弟你也买一份吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_46FC")

    Jump("loc_4206")

    label("loc_4701")

    TalkEnd(0xFE)
    Return()

    # Function_22_41F9 end

    def Function_23_4705(): pass

    label("Function_23_4705")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_476E")

    #C0182
    ChrTalk(
        0xFE,
        (
            "听说犯人被顺利\x01",
            "逮捕了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "哇哈哈，太好了。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "这样我们也能\x01",
            "安心享受庆典了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE5")

    label("loc_476E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_47D2")

    #C0185
    ChrTalk(
        0xFE,
        (
            "摩尔斯那家伙\x01",
            "最擅长演讲致辞的。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "哇哈哈，在开始之前还\x01",
            "发牢骚，说什么很紧张！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE5")

    label("loc_47D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_488C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4820")

    #C0187
    ChrTalk(
        0xFE,
        "噢噢？怎么了……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        "舞台那边吵吵闹闹的啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4887")

    label("loc_4820")


    #C0189
    ChrTalk(
        0xFE,
        (
            "啊呀，不愧是游击士。\x01",
            "完成工作的速度就是快啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "这样一来，市民们\x01",
            "也能尽情享受庆典了。\x01",
            "哇哈哈！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4887")

    Jump("loc_4BE5")

    label("loc_488C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4B2D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4936")
    OP_93(0xFE, 0x87, 0x0)

    #C0191
    ChrTalk(
        0xFE,
        (
            "怎么样，稍微工作一下之后，\x01",
            "心情很舒畅吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "如何，今天我请客喝酒吧。\x01",
            "哇哈哈，酒可真是好东西！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x17,
        (
            "呜呜，不用了！\x01",
            "我还没成年呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B28")

    label("loc_4936")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_49AA")

    #C0194
    ChrTalk(
        0xFE,
        "这附近没有异常哦。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "嗯……话虽如此，\x01",
            "但是找不到犯人的踪迹。\x01",
            "也只能这么漫无目的地巡视了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B28")

    label("loc_49AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_4AAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1E")

    #C0196
    ChrTalk(
        0xFE,
        (
            "还是去提醒一下各位店主，\x01",
            "让他们自己也多加小心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "我们也再去巡视一圈好了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_4AA5")

    label("loc_4A1E")


    #C0198
    ChrTalk(
        0xFE,
        (
            "我当年开露天店的时候，\x01",
            "也经常和盗贼战斗呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "不过……这次的盗贼可是\x01",
            "破坏庆典的无耻之辈啊。\x01",
            "对他们没必要留情，直接逮捕就是了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA5")

    Jump("loc_4B28")

    label("loc_4AAA")


    #C0200
    ChrTalk(
        0xFE,
        (
            "盗窃犯也来了港湾公园，\x01",
            "米斯拉的店好像\x01",
            "就遭到了毒手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "哎呀呀，明明正值\x01",
            "难得的庆典期间，\x01",
            "竟有做出如此败兴行为的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B28")

    Jump("loc_4BE5")

    label("loc_4B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4B83")

    #C0202
    ChrTalk(
        0xFE,
        (
            "说起来，这家伙\x01",
            "还有个可爱的小孙女呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "呵呵～\x01",
            "我去陪她玩玩吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE5")

    label("loc_4B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B95")
    Call(0, 33)
    Jump("loc_4BE5")

    label("loc_4B95")


    #C0204
    ChrTalk(
        0xFE,
        (
            "帕拉从以前开始\x01",
            "就是我们的偶像啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "哇哈哈，摩尔斯那家伙\x01",
            "真是让人羡慕！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE5")

    TalkEnd(0xFE)
    Return()

    # Function_23_4705 end

    def Function_24_4BE9(): pass

    label("Function_24_4BE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4C58")

    #C0206
    ChrTalk(
        0xFE,
        (
            "今晨，首先请我们工商协会的\x01",
            "会长先生发表致辞！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A, 500)

    #C0207
    ChrTalk(
        0xFE,
        "──有请会长！\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x0)
    Jump("loc_4DAD")

    label("loc_4C58")


    #C0208
    ChrTalk(
        0xFE,
        "嗯，在此有个遗憾的消息要通知大家。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "欢乐的纪念庆典，\x01",
            "到今天就要接近尾声啦！\x02",
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
            "那么，为了纪念\x01",
            "这最后的一天～……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "特别邀请我们克洛斯贝尔工商协会\x01",
            "的会长先生发表致辞！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A, 500)

    #C0212
    ChrTalk(
        0xFE,
        "──有请会长！\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x0)
    SetScenarioFlags(0x1, 2)

    label("loc_4DAD")

    Jump("loc_5054")

    label("loc_4DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_4E17")

    #C0213
    ChrTalk(
        0xFE,
        (
            "噢噢，又在干什么呢，\x01",
            "你们几个～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "赶快从舞台上下来！\x01",
            "快下来～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E1A")

    label("loc_4E17")

    Call(0, 53)

    label("loc_4E1A")

    Jump("loc_5054")

    label("loc_4E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4EA7")

    #C0215
    ChrTalk(
        0xFE,
        (
            "好，刷新最高分数记录\x01",
            "的究竟会是谁呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "今日欢迎各位随时上台挑战！\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "拥有自信的朋友，\x01",
            "就请您上台一展身手～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5054")

    label("loc_4EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4F9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4F24")

    #C0218
    ChrTalk(
        0xFE,
        (
            "虽然昨天是个灾难，\x01",
            "但今天的活动进行得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "作为昨天的补偿，\x01",
            "今天必须要让大家尽情享受啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F9A")

    label("loc_4F24")


    #C0220
    ChrTalk(
        0xFE,
        (
            "ＹＥＡＨ～接下来是杂技——\x01",
            "千钧一发的逃脱表演～！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "那么，还要从各位之中，\x01",
            "选出一位朋友上台帮忙……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x14, 0x10)

    label("loc_4F9A")

    Jump("loc_5054")

    label("loc_4F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4FFB")

    #C0222
    ChrTalk(
        0xFE,
        (
            "问答比赛的准备工作\x01",
            "还剩少许……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "小兄弟们，请不要着急，\x01",
            "再等一下吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5054")

    label("loc_4FFB")


    #C0224
    ChrTalk(
        0xFE,
        (
            "ＹＥＡＨ～小兄弟们，\x01",
            "请再等一下吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "现在正在进行开心问答比赛\x01",
            "的准备工作呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_5054")

    TalkEnd(0xFE)
    Return()

    # Function_24_4BE9 end

    def Function_25_5058(): pass

    label("Function_25_5058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5069")
    Call(0, 30)
    Jump("loc_506C")

    label("loc_5069")

    Call(0, 26)

    label("loc_506C")

    Return()

    # Function_25_5058 end

    def Function_26_506D(): pass

    label("Function_26_506D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50BB")
    Call(0, 77)
    Return()

    label("loc_50BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50E4")
    Call(0, 75)
    Return()

    label("loc_50E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5144")
    TalkBegin(0x15)

    #C0226
    ChrTalk(
        0x15,
        (
            "洛依和梅琳都来帮忙，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x15,
        (
            "就算嘴上抱怨，洛依\x01",
            "也很努力呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Jump("loc_57B2")

    label("loc_5144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5358")
    TalkBegin(0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_51D3")

    #C0228
    ChrTalk(
        0xFE,
        "各位，非常感谢你们的帮助！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "话说回来……还真是给露天市场的各位\x01",
            "添麻烦了呢。\x01",
            "最好能想办法补偿一下他们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5350")

    label("loc_51D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5274")

    #C0230
    ChrTalk(
        0xFE,
        (
            "虽然在每年的纪念庆典中\x01",
            "都会出现很多骚乱……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "……但没想到会发生连环盗窃案，\x01",
            "我们实在是束手无策啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "不好意思，各位，\x01",
            "万事拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5350")

    label("loc_5274")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_5308")

    #C0233
    ChrTalk(
        0xFE,
        (
            "再这么下去，\x01",
            "有些店铺或许都会\x01",
            "因此停业呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "难得的纪念庆典，\x01",
            "真不希望出现那种情况啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "总之，一切就\x01",
            "拜托各位了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5350")

    label("loc_5308")


    #C0236
    ChrTalk(
        0xFE,
        (
            "呼，虽然提醒过\x01",
            "大家要小心……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "但果然还是有必要\x01",
            "寻求帮助呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5350")

    TalkEnd(0x15)
    Jump("loc_57B2")

    label("loc_5358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5521")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x15)
    ClearChrFlags(0x15, 0x10)
    TurnDirection(0x15, 0x0, 0)
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_53F5")
    Jump("loc_543F")

    label("loc_53F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5415")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_543F")

    label("loc_5415")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5435")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_543F")

    label("loc_5435")

    OP_52(0x15, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_543F")

    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_54BA")

    #C0238
    ChrTalk(
        0x15,
        (
            "呼，话说回来，\x01",
            "还真是混乱啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x15,
        (
            "只有我一个，\x01",
            "实在是忙不过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5515")

    label("loc_54BA")


    #C0240
    ChrTalk(
        0x15,
        (
            "会长的儿子很能干，\x01",
            "经营着一家大企业哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x15,
        (
            "但是他的孙子洛依\x01",
            "好像却对此很排斥呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_5515")

    SetChrSubChip(0x15, 0x0)
    TalkEnd(0x15)
    Jump("loc_57B2")

    label("loc_5521")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x15)
    ClearChrFlags(0x15, 0x10)
    TurnDirection(0x15, 0x0, 0)
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55B5")
    Jump("loc_55FF")

    label("loc_55B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55D5")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55FF")

    label("loc_55D5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55F5")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55FF")

    label("loc_55F5")

    OP_52(0x15, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55FF")

    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56B5")

    #C0242
    ChrTalk(
        0x15,
        (
            "哎呀，欢迎，这里是\x01",
            "克洛斯贝尔工商协会的招待棚。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x15,
        (
            "欢迎各位市民\x01",
            "前来参加。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x15,
        (
            "我们正在举办抽奖以及\x01",
            "交换奖品的活动哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 5)
    Jump("loc_57AB")

    label("loc_56B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_571B")

    #C0245
    ChrTalk(
        0x15,
        (
            "会长他们以前也是\x01",
            "独立经营露天店的。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x15,
        (
            "不知为什么，当时的景象\x01",
            "总会浮现在我眼前。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57AB")

    label("loc_571B")


    #C0247
    ChrTalk(
        0x15,
        (
            "会长他们以前也在市场上\x01",
            "经营露天店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x15,
        (
            "既是竞争对手，又是商业伙伴……\x01",
            "大家就是那种关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x15,
        (
            "呵呵，当时的景象\x01",
            "总是浮现在我眼前呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_57AB")

    SetChrSubChip(0x15, 0x0)
    TalkEnd(0x15)

    label("loc_57B2")

    Return()

    # Function_26_506D end

    def Function_27_57B3(): pass

    label("Function_27_57B3")

    TalkBegin(0xFE)

    #C0250
    ChrTalk(
        0xFE,
        "嗯～景色真棒。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "一直在逛露天市场，也很累了，\x01",
            "所以在这里稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "稍微远离喧嚣的场所后，\x01",
            "发现克洛斯贝尔\x01",
            "也是个安宁闲适的好地方嘛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_57B3 end

    def Function_28_584F(): pass

    label("Function_28_584F")

    TalkBegin(0xFE)

    #C0253
    ChrTalk(
        0xFE,
        (
            "这个城市也好，阿尔摩利卡村也好，\x01",
            "都有各自的优缺点呢，\x01",
            "是这样吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "……不然就买点特产带回去，\x01",
            "送给村里的孩子吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_584F end

    def Function_29_58D1(): pass

    label("Function_29_58D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_59EA")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595B")

    #C0255
    ChrTalk(
        0xFE,
        "啊，犯人已经被逮捕了吗？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "……什、什么啊。\x01",
            "还真是意外地迅速呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "呵……这、这就太好啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_59DE")

    label("loc_595B")


    #C0258
    ChrTalk(
        0xFE,
        (
            "听说那些店遭窃之后，\x01",
            "我可是担心得不得了呢……\x01",
            "破案的速度真比想象中要快呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "真是太好了，\x01",
            "……我也得赶快去看着接待帐篷了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59DE")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_5BAC")

    label("loc_59EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_5A6F")

    #C0260
    ChrTalk(
        0xFE,
        (
            "那个，接下来……\x01",
            "要不要再去一次\x01",
            "米斯拉那里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "虽然已经遭窃的店应该不会再被盯上了，\x01",
            "……但还是很担心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BAC")

    label("loc_5A6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5B2C")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AE7")

    #C0262
    ChrTalk(
        0xFE,
        (
            "我稍微在这附近\x01",
            "巡视一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "连环作案的盗窃犯吗……\x01",
            "真担心那些开店的人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_5B20")

    label("loc_5AE7")


    #C0264
    ChrTalk(
        0xFE,
        (
            "区区巡视的话，我也可以做到呢。\x01",
            "……我稍微去转转吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B20")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_5BAC")

    label("loc_5B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5BAC")

    #C0265
    ChrTalk(
        0xFE,
        (
            "梅琳刚才过来找我，\x01",
            "说她想去逛逛露天市场。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "我对工商协会什么的\x01",
            "完全没兴趣～\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "……爷爷，要对我\x01",
            "老爸保密啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BAC")

    TalkEnd(0xFE)
    Return()

    # Function_29_58D1 end

    def Function_30_5BB0(): pass

    label("Function_30_5BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5D68")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C4D")
    Jump("loc_5C97")

    label("loc_5C4D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C6D")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C97")

    label("loc_5C6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C8D")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C97")

    label("loc_5C8D")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C97")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFE")

    #C0268
    ChrTalk(
        0x17,
        "欢迎～\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x17,
        "抽奖和奖品兑换就到今天为止哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_5D5C")

    label("loc_5CFE")


    #C0270
    ChrTalk(
        0x17,
        (
            "……因为人手不足，\x01",
            "所以接待员这个差事就落在我头上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x17,
        (
            "呵呵，我还真是\x01",
            "容易被指使啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D5C")

    SetChrSubChip(0x17, 0x0)
    TalkEnd(0x17)
    Jump("loc_602F")

    label("loc_5D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5F57")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E05")
    Jump("loc_5E4F")

    label("loc_5E05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E25")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E4F")

    label("loc_5E25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E45")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E4F")

    label("loc_5E45")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E4F")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5ECC")

    #C0272
    ChrTalk(
        0x17,
        "噢～这人数还真是壮观……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x17,
        (
            "我是不是也该去\x01",
            "帮忙进行一下疏导啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F4B")

    label("loc_5ECC")


    #C0274
    ChrTalk(
        0x17,
        (
            "游击士还是那么\x01",
            "厉害啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x17,
        "话说，这人数真是相当惊人啊……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x17,
        (
            "都是来看游行的吗？\x01",
            "我是不是也该去\x01",
            "帮忙进行一下疏导呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F4B")

    SetChrSubChip(0x17, 0x0)
    TalkEnd(0x17)
    Jump("loc_602F")

    label("loc_5F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_602F")
    TalkBegin(0x17)
    SetChrSubChip(0x17, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5FD8")

    #C0277
    ChrTalk(
        0x17,
        (
            "可恶～仔细想想的话，\x01",
            "我为什么非要去帮忙不可呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x17,
        (
            "明明说过对商业活动\x01",
            "没有兴趣的啊～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6028")

    label("loc_5FD8")


    #C0279
    ChrTalk(
        0x17,
        (
            "似乎连续发生了\x01",
            "什么事件啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x17,
        (
            "真、真没办法啊，\x01",
            "我来帮忙做接待工作好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6028")

    SetChrSubChip(0x17, 0x2)
    TalkEnd(0x17)

    label("loc_602F")

    Return()

    # Function_30_5BB0 end

    def Function_31_6030(): pass

    label("Function_31_6030")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6057")

    #C0281
    ChrTalk(
        0xFE,
        (
            "哇～！\x01",
            "有好多店呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6057")

    TalkEnd(0xFE)
    Return()

    # Function_31_6030 end

    def Function_32_605B(): pass

    label("Function_32_605B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x19)
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x0, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60EF")
    Jump("loc_6139")

    label("loc_60EF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_610F")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6139")

    label("loc_610F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_612F")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6139")

    label("loc_612F")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6139")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_61A5")

    #C0282
    ChrTalk(
        0x19,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x19,
        (
            "这里是接待处，\x01",
            "可以兑换奖品哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F2")

    label("loc_61A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6244")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_61F8")

    #C0284
    ChrTalk(
        0x19,
        "那就是游行吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    #C0285
    ChrTalk(
        0x19,
        "真棒呀～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_623F")

    label("loc_61F8")


    #C0286
    ChrTalk(
        0x19,
        "游击士真厉害呀～！\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x19,
        (
            "啪啪啪啪，只用了几招\x01",
            "就把犯人给抓住了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_623F")

    Jump("loc_63F2")

    label("loc_6244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_63F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6369")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_62CE")

    #C0288
    ChrTalk(
        0x19,
        "哥哥们真是太帅了～\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x19,
        (
            "然后还向穿制服的人\x01",
            "严肃地打了招呼，\x01",
            "真是好帅啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    Jump("loc_6364")

    label("loc_62CE")


    #C0290
    ChrTalk(
        0x19,
        "哥哥们真是太帅了～\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x19,
        (
            "不过还是狗狗\x01",
            "更帅啊～\x02",
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

    label("loc_6364")

    Jump("loc_63F2")

    label("loc_6369")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_63C2")

    #C0292
    ChrTalk(
        0x19,
        "有梅琳在这里看着呢，\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x19,
        (
            "大哥哥，你们需要去别处调查\x01",
            "也没问题的～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F2")

    label("loc_63C2")


    #C0294
    ChrTalk(
        0x19,
        "我和哥哥都在这里看着呢。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x19,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    label("loc_63F2")

    SetChrSubChip(0x19, 0x0)
    TalkEnd(0x19)
    Return()

    # Function_32_605B end

    def Function_33_63FA(): pass

    label("Function_33_63FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6448")
    Call(0, 77)
    Return()

    label("loc_6448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6471")
    Call(0, 75)
    Return()

    label("loc_6471")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_64FF")

    #C0296
    ChrTalk(
        0xFE,
        "哎呀呀，终于到了最终日吗……\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "我很不擅长说寒暄语啊。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x14, 0xFF)
    TurnDirection(0x14, 0xFE, 500)

    #C0298
    ChrTalk(
        0x14,
        (
            "好啦，请您开始\x01",
            "最后的致词吧，会长！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_93(0x14, 0x10E, 0x0)
    Jump("loc_6E89")

    label("loc_64FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_66B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6550")

    #C0299
    ChrTalk(
        0xFE,
        (
            "噢噢，又是你们吗……！\x01",
            "别再做出粗暴的事了啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66AB")

    label("loc_6550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_657B")

    #C0300
    ChrTalk(
        0xFE,
        "哎呀，是你们啊。\x02",
    )

    CloseMessageWindow()

    label("loc_657B")


    #C0301
    ChrTalk(
        0xFE,
        (
            "其实，游击士已经帮我们\x01",
            "把盗窃犯给抓到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "哈哈哈，太好了，太好了。\x01",
            "这下终于可以愉快地享受庆典了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_663E")

    #C0303
    ChrTalk(
        0x101,
        (
            "#0005F（啊……那个事件\x01",
            "  已经被解决了吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6671")

    label("loc_663E")


    #C0304
    ChrTalk(
        0x101,
        (
            "#0005F（事件……？\x01",
            "  是指那起盗窃事件吗……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6671")


    #C0305
    ChrTalk(
        0x104,
        (
            "#0306F（坏了……竟然还是\x01",
            "  被游击士抢先一步……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A8")

    SetScenarioFlags(0x1, 4)

    label("loc_66AB")

    Jump("loc_6E89")

    label("loc_66B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6C15")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_674F")

    #C0306
    ChrTalk(
        0xFE,
        (
            "哎呀呀，真是麻烦你们啦。\x01",
            "这样一来，终于可以愉快地享受庆典了。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "哈哈哈，太好了，太好了。\x01",
            "我还真是认识了一群\x01",
            "优秀的年轻人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C10")

    label("loc_674F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6949")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68B4")

    #C0308
    ChrTalk(
        0xFE,
        (
            "遭窃的店铺，\x01",
            "在中央广场、行政区、\x01",
            "欢乐街和港湾公园各有一家。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "……不过，最好也去没有\x01",
            "遭窃的店铺问一问，\x01",
            "或许能得到一些可供参考的线索。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#0005F原来如此……说得也是呢，\x01",
            "那我们就全部都去问一遍吧。\x02\x03",

            "#0001F结束之后，我们会回来报告的，\x01",
            "请您在这里等我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "嗯，知道了。\x01",
            "如果我们这边有了什么消息，\x01",
            "也会立刻通知你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_6944")

    label("loc_68B4")


    #C0312
    ChrTalk(
        0xFE,
        (
            "遭窃的店铺，\x01",
            "在中央广场、行政区、\x01",
            "欢乐街和港湾公园各有一家。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "……不过，最好也去没有\x01",
            "遭窃的店铺问一问，\x01",
            "或许能得到一些可供参考的线索。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6944")

    Jump("loc_6C10")

    label("loc_6949")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_6BD7")

    #C0314
    ChrTalk(
        0x1A,
        (
            "以露天店为目标的连环盗窃犯……\x01",
            "站在工商协会的立场来说，\x01",
            "也无法再继续坐视不理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x1A,
        (
            "毕竟，如果再这么下去，\x01",
            "恐怕也会给前来享受庆典\x01",
            "的客人们带来麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x1A,
        (
            "你们愿意帮忙\x01",
            "抓捕犯人吗。\x02",
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
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B22")
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

    label("loc_6B22")


    #C0317
    ChrTalk(
        0x101,
        (
            "#0006F实在抱歉，我们现在\x01",
            "还有其它工作，脱不开身……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x1A,
        "是吗，那就没办法了啊。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x1A,
        (
            "等你们有空了再来吧。\x01",
            "希望能在下一个受害者出现之前，\x01",
            "赶快将事件解决啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x1A, 0x13B, 0x0)
    OP_93(0x15, 0x87, 0x0)
    Jump("loc_6C10")

    label("loc_6BD7")


    #C0320
    ChrTalk(
        0xFE,
        "真头疼啊……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "这样一来，都不能\x01",
            "安心享受庆典了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C10")

    Jump("loc_6E89")

    label("loc_6C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6CDB")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0322
    ChrTalk(
        0xFE,
        (
            "哦，这不是洛依吗，\x01",
            "你来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x16,
        (
            "因为梅琳说\x01",
            "想来玩的……\x01",
            "不要对老爸说哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "哈哈哈，什么嘛，\x01",
            "那家伙在庆典期间\x01",
            "也不会对你多说什么的。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "今天就\x01",
            "放心去玩吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_6E89")

    label("loc_6CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6E89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E38")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0326
    ChrTalk(
        0x13,
        (
            "噢噢，帕拉，\x01",
            "好久不见啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x13,
        (
            "不过……摩尔斯那家伙\x01",
            "还真是有本事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x13,
        (
            "居然娶到了我们大家\x01",
            "的偶像帕拉……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x1B,
        "啊呀呀，你这么说可就太夸张了。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x1A,
        (
            "如果不赶快把\x01",
            "清洁布和酒摆好，\x01",
            "我可就要揍人啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x13,
        (
            "哇哈哈，真可怕，真可怕。\x01",
            "会长他们还是和从前一样，\x01",
            "是一对鸳鸯般的恩爱夫妇呢。\x02",
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
    Jump("loc_6E89")

    label("loc_6E38")


    #C0332
    ChrTalk(
        0xFE,
        (
            "哎呀呀，我的朋友\x01",
            "全都是这种容易得意忘形的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        "有时真想揍他们一顿。\x02",
    )

    CloseMessageWindow()

    label("loc_6E89")

    TalkEnd(0xFE)
    Return()

    # Function_33_63FA end

    def Function_34_6E8D(): pass

    label("Function_34_6E8D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EAB")
    Call(0, 33)
    Jump("loc_6EFD")

    label("loc_6EAB")


    #C0334
    ChrTalk(
        0xFE,
        (
            "工商协会的各位\x01",
            "我也早就认识。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "呵呵，虽然过了这么多年，\x01",
            "但大家都没变啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EFD")

    TalkEnd(0xFE)
    Return()

    # Function_34_6E8D end

    def Function_35_6F01(): pass

    label("Function_35_6F01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6F6C")

    #C0336
    ChrTalk(
        0xFE,
        (
            "咳咳，既然是我儿子的请求，\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "今天就去主题公园痛痛快快\x01",
            "地玩个够吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709A")

    label("loc_6F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6FD8")

    #C0338
    ChrTalk(
        0xFE,
        "哈哈，这么可怕的人……\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "儿、儿子啊，\x01",
            "如果已经道完谢的话，\x01",
            "就赶快和爸爸一起去别处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709A")

    label("loc_6FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7025")

    #C0340
    ChrTalk(
        0xFE,
        "游行马上就要开始了啊！\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "我从小时候开始\x01",
            "就很喜欢游行！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709A")

    label("loc_7025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7075")

    #C0342
    ChrTalk(
        0xFE,
        (
            "唔唔唔……这家店的小姐……\x01",
            "是个比我老婆还要\x01",
            "漂亮的美人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709A")

    label("loc_7075")


    #C0343
    ChrTalk(
        0xFE,
        (
            "好，今天就去\x01",
            "逛逛露天店吧～！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_709A")

    TalkEnd(0xFE)
    Return()

    # Function_35_6F01 end

    def Function_36_709E(): pass

    label("Function_36_709E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_70E6")

    #C0344
    ChrTalk(
        0xFE,
        (
            "我要坐上大船，\x01",
            "到米修拉姆去玩～\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "……哇～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_719A")

    label("loc_70E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_7111")

    #C0346
    ChrTalk(
        0x22,
        "哇～谢谢哥哥！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7114")

    label("loc_7111")

    Call(0, 50)

    label("loc_7114")

    Jump("loc_719A")

    label("loc_7119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7160")

    #C0347
    ChrTalk(
        0xFE,
        "庆典、庆典～！\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "说到庆典，\x01",
            "自然少不了游行啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_719A")

    label("loc_7160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7186")

    #C0349
    ChrTalk(
        0xFE,
        "爸爸，你怎么了～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_719A")

    label("loc_7186")


    #C0350
    ChrTalk(
        0xFE,
        "哇～是庆典～！\x02",
    )

    CloseMessageWindow()

    label("loc_719A")

    TalkEnd(0xFE)
    Return()

    # Function_36_709E end

    def Function_37_719E(): pass

    label("Function_37_719E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_71ED")

    #C0351
    ChrTalk(
        0xFE,
        (
            "今天好像有很多人\x01",
            "去米修拉姆呢。\x01",
            "我也凑个热闹，一起去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7350")

    label("loc_71ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_729C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7265")

    #C0352
    ChrTalk(
        0xFE,
        (
            "听说盗窃犯在中央广场那边\x01",
            "被抓住了？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "在难得的庆典期间，竟然\x01",
            "还有那种干坏事的家伙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7297")

    label("loc_7265")


    #C0354
    ChrTalk(
        0xFE,
        (
            "开店的人看上去\x01",
            "都很困扰呢，\x01",
            "发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7297")

    Jump("loc_7350")

    label("loc_729C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7305")

    #C0355
    ChrTalk(
        0xFE,
        (
            "冰激凌、果汁、\x01",
            "爆米花还有串烧……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "庆典真好啊……\x01",
            "简直都想和路上的\x01",
            "行人们干一杯！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7350")

    label("loc_7305")


    #C0357
    ChrTalk(
        0xFE,
        "庆典，庆典啊～！\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "这种时候怎么可以不好好享受。\x01",
            "你们也来干一杯吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7350")

    TalkEnd(0xFE)
    Return()

    # Function_37_719E end

    def Function_38_7354(): pass

    label("Function_38_7354")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_73A7")

    #C0359
    ChrTalk(
        0xFE,
        (
            "工商协会的会长先生\x01",
            "好像是个很能干的人呢，\x01",
            "真期待他的致辞啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7528")

    label("loc_73A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_73DA")

    #C0360
    ChrTalk(
        0xFE,
        (
            "哇哇哇～！？\x01",
            "他们要干什么～！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7528")

    label("loc_73DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_744E")

    #C0361
    ChrTalk(
        0xFE,
        (
            "刚才那个组合的表演相当精彩，\x01",
            "但这个歌手也很棒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "到底要给谁评高分呢，\x01",
            "真是拿不定主意啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7528")

    label("loc_744E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_749E")

    #C0363
    ChrTalk(
        0xFE,
        (
            "噢噢～好精彩的\x01",
            "表演啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "这个的得分\x01",
            "应该很值得期待吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7528")

    label("loc_749E")


    #C0365
    ChrTalk(
        0xFE,
        (
            "接下来将是工商协会主办的\x01",
            "快乐问答比赛哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "奖品是米修拉姆的豪华住宿套票！\x01",
            "另外还有工商协会的商品券。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        "呵呵，一定不能错过呢。\x02",
    )

    CloseMessageWindow()

    label("loc_7528")

    TalkEnd(0xFE)
    Return()

    # Function_38_7354 end

    def Function_39_752C(): pass

    label("Function_39_752C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7569")

    #C0368
    ChrTalk(
        0xFE,
        "呀呀，是会长先生！\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        "请加油啊～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7647")

    label("loc_7569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_75BF")

    #C0370
    ChrTalk(
        0xFE,
        (
            "哎哎，那些不是之前的\x01",
            "不良青年吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "为什么会跑到\x01",
            "舞台上啊！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7647")

    label("loc_75BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7607")

    #C0372
    ChrTalk(
        0xFE,
        "听说今天可以随时上台挑战！\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        "我也上去试试好啦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7647")

    label("loc_7607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_762F")

    #C0374
    ChrTalk(
        0xFE,
        "呀呀，请加油啊～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7647")

    label("loc_762F")


    #C0375
    ChrTalk(
        0xFE,
        "我一定会抽中的～！\x02",
    )

    CloseMessageWindow()

    label("loc_7647")

    TalkEnd(0xFE)
    Return()

    # Function_39_752C end

    def Function_40_764B(): pass

    label("Function_40_764B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_767C")

    #C0376
    ChrTalk(
        0xFE,
        "庆典到今天就要结束了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_77B4")

    label("loc_767C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_76A9")

    #C0377
    ChrTalk(
        0xFE,
        (
            "等、等一下！？\x01",
            "怎么了！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77B4")

    label("loc_76A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_76F0")

    #C0378
    ChrTalk(
        0xFE,
        (
            "虽然歌唱得也很好……\x01",
            "但最让人羡慕的还是那份美貌啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77B4")

    label("loc_76F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_776F")

    #C0379
    ChrTalk(
        0xFE,
        (
            "这个舞台活动好像是\x01",
            "克洛斯贝尔工商协会主办的。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "参加者还能得到可以在\x01",
            "露天店使用的打折券呢！\x01",
            "不能错过啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77B4")

    label("loc_776F")


    #C0381
    ChrTalk(
        0xFE,
        "啊啊，真是豪华的奖品啊！\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "这样的话，不参加可就\x01",
            "太吃亏了啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77B4")

    TalkEnd(0xFE)
    Return()

    # Function_40_764B end

    def Function_41_77B8(): pass

    label("Function_41_77B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_780C")

    #C0383
    ChrTalk(
        0xFE,
        (
            "虽然是个老爷爷，\x01",
            "但还挺帅的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        "那个人就是会长先生啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_790D")

    label("loc_780C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_786C")

    #C0385
    ChrTalk(
        0xFE,
        (
            "在游行之后，\x01",
            "那群人就蜂拥而来！\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "难道是被游行的热闹气氛\x01",
            "冲昏头脑了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790D")

    label("loc_786C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_78A3")

    #C0387
    ChrTalk(
        0xFE,
        (
            "距离游行还有些时间，\x01",
            "再稍微转转吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790D")

    label("loc_78A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_78CF")

    #C0388
    ChrTalk(
        0xFE,
        "妈妈，你好像有些贪吃啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_790D")

    label("loc_78CF")


    #C0389
    ChrTalk(
        0xFE,
        (
            "昨天的演唱会很精彩，\x01",
            "今天好像也有什么活动呢。\x01",
            "真期待啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790D")

    TalkEnd(0xFE)
    Return()

    # Function_41_77B8 end

    def Function_42_7911(): pass

    label("Function_42_7911")

    TalkBegin(0xFE)

    #C0390
    ChrTalk(
        0xFE,
        "终于要去期待已久的米修拉姆了⊥\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "虽然等待水上巴士的时间只有十分钟，\x01",
            "却感觉如此漫长啊～⊥\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_7911 end

    def Function_43_7979(): pass

    label("Function_43_7979")

    TalkBegin(0xFE)

    #C0392
    ChrTalk(
        0xFE,
        (
            "（心跳）……\x01",
            "我要和女朋友一起去米修拉姆哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "最终日就要去米修拉姆！\x01",
            "这可是近两三年来的固定选择哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_7979 end

    def Function_44_79EC(): pass

    label("Function_44_79EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7A43")

    #C0394
    ChrTalk(
        0xFE,
        (
            "嗯～果然还是\x01",
            "想吃冰激凌啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "可是爸爸好像\x01",
            "比较喜欢汤面……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE1")

    label("loc_7A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7A8E")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0396
    ChrTalk(
        0xFE,
        "那、那个……\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        "游行真是精彩啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AE1")

    label("loc_7A8E")


    #C0398
    ChrTalk(
        0xFE,
        "今天是和妈妈一起出门的。\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……都已经很久\x01",
            "没有和妈妈一起出来玩了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AE1")

    TalkEnd(0xFE)
    Return()

    # Function_44_79EC end

    def Function_45_7AE5(): pass

    label("Function_45_7AE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7B31")

    #C0400
    ChrTalk(
        0xFE,
        (
            "必须要给老公\x01",
            "买点什么礼物带回去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        "买什么好呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C7A")

    label("loc_7B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7BA8")

    #C0402
    ChrTalk(
        0xFE,
        (
            "没能看成彩虹剧团的表演，\x01",
            "虽然有些遗憾，\x01",
            "但观赏游行也很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "呵呵，明年也叫上\x01",
            "老公一起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C7A")

    label("loc_7BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_7BEE")

    #C0404
    ChrTalk(
        0xFE,
        "小桃，接下来要去哪里？\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        "要不要去那家店看看啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C7A")

    label("loc_7BEE")

    TurnDirection(0xFE, 0x0, 0)

    #C0406
    ChrTalk(
        0xFE,
        (
            "呵呵，我把店交给老公，\x01",
            "自己带着女儿出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "本来难得有个全家出游\x01",
            "的机会呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "可惜那个人受不了\x01",
            "吵闹的气氛。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xB4, 0x0)
    SetScenarioFlags(0x1, 7)

    label("loc_7C7A")

    TalkEnd(0xFE)
    Return()

    # Function_45_7AE5 end

    def Function_46_7C7E(): pass

    label("Function_46_7C7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7D11")

    #C0409
    ChrTalk(
        0xFE,
        (
            "呼，我也只有继续\x01",
            "港湾公园的警备工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "虽然有些不甘心……\x01",
            "但在米修拉姆发生的事情，\x01",
            "连一科这边都是默认不管的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DB9")

    label("loc_7D11")


    #C0411
    ChrTalk(
        0xFE,
        (
            "今天去米修拉姆的客人\x01",
            "真是很多呢。\x02",
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
            "#0001F（果然掌握到了\x01",
            "  『黑之竞拍会』\x01",
            "  的情况呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        "#0101F（嗯，毕竟是搜查一科啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_7DB9")

    Jump("loc_8171")

    label("loc_7DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 6)), scpexpr(EXPR_END)), "loc_7F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7E24")

    #C0415
    ChrTalk(
        0xFE,
        (
            "我正在进行警备工作这件事\x01",
            "是要对一般市民保密的。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        "请不要总来和我说话。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EFD")

    label("loc_7E24")


    #C0417
    ChrTalk(
        0xFE,
        (
            "我正在进行警备工作这件事\x01",
            "是要对一般市民保密的。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "请不要总来和我说话。\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        (
            "#0003F（说起来……\x01",
            "  昨天来看演唱会时\x01",
            "  也没注意到她呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x104,
        (
            "#0300F（隐藏气息来进行监视和跟踪，\x01",
            "  正是搜查一科的拿手好戏吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_7EFD")

    Jump("loc_8171")

    label("loc_7F02")


    #C0421
    ChrTalk(
        0xFE,
        (
            "特别任务支援科……\x01",
            "又来这边转悠了啊。\x02",
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
            "#0005F啊，您好像是\x01",
            "一科的搜查官……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        "#0300F在这种地方进行纪念庆典的警备工作吗？\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "……在创立纪念庆典期间，\x01",
            "到处都会有毫无防备的人群。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "再加上，其中还包括很多来自\x01",
            "国内外的有势者与资产家……\x01",
            "不能排除发生恐怖袭击的可能性啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x102,
        (
            "#0100F所以才来这里进行警备工作啊……\x01",
            "一科也真是很辛苦呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "嗯，那是当然。\x01",
            "和你们不一样，\x01",
            "我们可是任务繁重啊。\x02",
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
        "#0200F（这人说话稍微有些令人生厌呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 6)

    label("loc_8171")

    TalkEnd(0xFE)
    Return()

    # Function_46_7C7E end

    def Function_47_8175(): pass

    label("Function_47_8175")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8265")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_81E2")

    #C0429
    ChrTalk(
        0xFE,
        (
            "不仅被迫认识到了自己缺乏才能，\x01",
            "连钱包都弄丢了……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        "……我究竟在做什么啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8260")

    label("loc_81E2")


    #C0431
    ChrTalk(
        0xFE,
        (
            "虽然本来是想今天就\x01",
            "回利贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        (
            "但没想到把\x01",
            "钱包给丢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "……我究竟在做什么啊。\x01",
            "难道连空之女神都讨厌我吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_8260")

    Jump("loc_86D3")

    label("loc_8265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_82D2")

    #C0434
    ChrTalk(
        0xFE,
        (
            "……我决定放弃\x01",
            "成为诗人的梦想了。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "虽然早了一点……\x01",
            "但也只能回利贝尔了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8350")

    label("loc_82D2")


    #C0436
    ChrTalk(
        0xFE,
        (
            "大家听了我创作的诗歌之后，\x01",
            "纷纷摇头而去。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "难道我真的没有\x01",
            "创作的才能吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "……我决定放弃\x01",
            "成为诗人的梦想了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_8350")

    Jump("loc_86D3")

    label("loc_8355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_84F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_83D2")

    #C0439
    ChrTalk(
        0xFE,
        (
            "……从刚才开始，\x01",
            "就没有任何人愿意\x01",
            "听我的诗。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "可恶啊，哪怕只是\x01",
            "能将一个人给感动\x01",
            "也好啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84ED")

    label("loc_83D2")


    #C0441
    ChrTalk(
        0xFE,
        (
            "你们几个，如果愿意的话，\x01",
            "要不要来听听我创作\x01",
            "的诗歌呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "旅途不惧羞耻，在外要靠朋友……\x01",
            "圣堂钟声彻响，诉说万事无常……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xFE,
        "……怎么样啊？\x02",
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
        "#0003F（……这个，是诗吗？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_84ED")

    Jump("loc_86D3")

    label("loc_84F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8658")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_856D")

    #C0445
    ChrTalk(
        0xFE,
        (
            "为了改变自己，\x01",
            "就必须要从自身开始努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "……我虽然明白了这一点，\x01",
            "但却不知究竟该从何做起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8653")

    label("loc_856D")


    #C0447
    ChrTalk(
        0xFE,
        (
            "来到克洛斯贝尔之后，\x01",
            "已经都过去三天了。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "在如此热闹繁华的场所，\x01",
            "我却仍在糊涂度日，\x01",
            "找不到任何改变的感觉与先兆。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "继续着这种没有光芒与希望的生活……\x01",
            "努力的安敦在此……\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "……果然还是诗歌好。\x01",
            "让我稍微有了些精神。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_8653")

    Jump("loc_86D3")

    label("loc_8658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_86D0")

    #C0451
    ChrTalk(
        0xFE,
        (
            "没工作、没女朋友，\x01",
            "我的人生就是如此不堪……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "在此次克洛斯贝尔之旅中，\x01",
            "要是能发生什么好事就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86D3")

    label("loc_86D0")

    Call(0, 49)

    label("loc_86D3")

    TalkEnd(0xFE)
    Return()

    # Function_47_8175 end

    def Function_48_86D7(): pass

    label("Function_48_86D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8755")
    OP_93(0x20, 0xB4, 0x0)

    #C0453
    ChrTalk(
        0xFE,
        (
            "安敦，过于悲观\x01",
            "可是个坏习惯啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "所谓遗失物，经常会在你忘记它\x01",
            "的时候，从意外的地方冒出来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B48")

    label("loc_8755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_88AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_87FB")
    OP_93(0x20, 0x87, 0x0)

    #C0455
    ChrTalk(
        0xFE,
        (
            "噢，看啊，安敦。\x01",
            "舞台那边在举办很有趣的活动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        (
            "上台参加，然后\x01",
            "尽情高歌一曲如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        "长期压抑的感觉，或许会瞬间一扫而空哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_88A7")

    label("loc_87FB")


    #C0458
    ChrTalk(
        0xFE,
        (
            "安敦从早上开始就一直站在这里，\x01",
            "给路过的行人们赠诗。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "结果就如你们所见，\x01",
            "残酷的现实似乎把他完全打垮了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        (
            "……那么，肚子也有点饿了，\x01",
            "去露天市场那边看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)

    label("loc_88A7")

    Jump("loc_8B48")

    label("loc_88AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8958")

    #C0461
    ChrTalk(
        0xFE,
        (
            "今天早上，安敦突然\x01",
            "说想成为\x01",
            "流浪诗人。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "呼，因为安敦一向三分钟热度，\x01",
            "所以我早就料到他会很快放弃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        (
            "我只要一如既往地，\x01",
            "怀着温暖的心守护他就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B48")

    label("loc_8958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_89DA")
    OP_93(0x20, 0xB4, 0x0)

    #C0464
    ChrTalk(
        0xFE,
        (
            "安敦，如果决定了自己\x01",
            "想做的事情，就告诉我一声吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "在那之前，我先去对面\x01",
            "的长椅上午睡一会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AA7")

    label("loc_89DA")


    #C0466
    ChrTalk(
        0xFE,
        (
            "安敦在不久之前刚刚失恋，\x01",
            "随即便决定要成为诗人。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "虽然他一直都很没毅力，\x01",
            "但这次坚持的时间真是意外地长呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xFE,
        (
            "暂且不说他能不能写出好诗，\x01",
            "像这样完全不考虑现实生活，还真是\x01",
            "符合安敦一贯的作风呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)

    label("loc_8AA7")

    Jump("loc_8B48")

    label("loc_8AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_8B34")

    #C0469
    ChrTalk(
        0xFE,
        (
            "我为了陪安敦寻找自我，\x01",
            "从遥远的利贝尔来到了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        (
            "他在这里又准备做什么呢，\x01",
            "和安敦在一起真是永远不会感到无聊啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B48")

    label("loc_8B34")

    Call(0, 49)
    TurnDirection(0x20, 0x0, 0)
    OP_93(0x20, 0xB4, 0x0)
    SetScenarioFlags(0x2, 2)

    label("loc_8B48")

    TalkEnd(0xFE)
    Return()

    # Function_48_86D7 end

    def Function_49_8B4C(): pass

    label("Function_49_8B4C")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0x20, 0xB4, 0x0)

    #C0471
    ChrTalk(
        0x1F,
        (
            "为了寻找自我，\x01",
            "竟然一直来到了\x01",
            "如此遥远的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x1F,
        (
            "克洛斯贝尔还真是个热闹的\x01",
            "好地方啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x1F,
        (
            "……我说，利库斯。\x01",
            "你不觉得，我在这里一定能\x01",
            "找到自己一直在追求的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x20,
        "哈，不要问我啊。\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x20,
        (
            "虽然我了解你振奋的心情，\x01",
            "但还是冷静些吧，安敦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetScenarioFlags(0x2, 1)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_49_8B4C end

    def Function_50_8C69(): pass

    label("Function_50_8C69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_8CBB")

    #C0476
    ChrTalk(
        0x2E,
        (
            "#1601F嘁，小心一点。\x01",
            "我刚才差点就\x01",
            "把你一脚踢飞了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E1A")

    label("loc_8CBB")

    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)

    #C0477
    ChrTalk(
        0x2E,
        (
            "#1601F喂，小鬼，\x01",
            "不要乱撞……\x02\x03",

            "#1607F而且钱包还掉了。\x01",
            "你到底在看哪里啊，嗯？\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x22,
        "啊，是我的钱包～\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x22,
        "哇～谢谢你！\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x21,
        "哈哈哈哈……\x02",
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
        "#0005F（在、在做什么呢……？）\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x104,
        (
            "#0306F（算啦，看起来好像\x01",
            "  并不是在找别人的麻烦。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    OP_4C(0x21, 0xFF)
    OP_4C(0x22, 0xFF)

    label("loc_8E1A")

    Jump("loc_8EA5")

    label("loc_8E1F")


    #C0483
    ChrTalk(
        0x2E,
        (
            "#1600F噢，你们在工作吗？\x02\x03",

            "#1602F呵呵……警察好像也很忙啊，\x01",
            "辛苦啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        (
            "#0006F呼，如果真的同情我们，\x01",
            "就请别再惹出什么乱子了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EA5")

    TalkEnd(0xFE)
    Return()

    # Function_50_8C69 end

    def Function_51_8EA9(): pass

    label("Function_51_8EA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8F50")

    #C0485
    ChrTalk(
        0x2F,
        (
            "噢～呀呵！\x01",
            "让我来唱一曲吧～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x2F,
        (
            "随时可以～上台参加，任何人都～ＯＫ哦！\x01",
            "随时可以～上台参加，任何人都～ＯＫ啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x2F,
        "……呀呀呀～～呀呵！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F9C")

    label("loc_8F50")


    #C0488
    ChrTalk(
        0x2F,
        "哈哈哈哈～！\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x2F,
        (
            "看啊～\x01",
            "在工商协会的帐篷负责接待的\x01",
            "竟然是那种小毛孩～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F9C")

    TalkEnd(0xFE)
    Return()

    # Function_51_8EA9 end

    def Function_52_8FA0(): pass

    label("Function_52_8FA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9000")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_8FF8")
    OP_4B(0x14, 0xFF)

    #C0490
    ChrTalk(
        0x30,
        "诺加诺夫说了要唱歌的。\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x30,
        "闭上嘴给我好好听着。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_8FFB")

    label("loc_8FF8")

    Call(0, 53)

    label("loc_8FFB")

    Jump("loc_903E")

    label("loc_9000")


    #C0492
    ChrTalk(
        0x30,
        "奇怪，好像到处都有警察徘徊啊。\x02",
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x30,
        "今天发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_903E")

    TalkEnd(0xFE)
    Return()

    # Function_52_8FA0 end

    def Function_53_9042(): pass

    label("Function_53_9042")

    OP_4B(0x30, 0xFF)
    OP_4B(0x14, 0xFF)

    #C0494
    ChrTalk(
        0x14,
        (
            "喔喔喔，又要干什么啊！\x01",
            "你们几个～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x14,
        (
            "马上从舞台上下来！\x01",
            "给我下来～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x30,
        "吵死人了，给我闭嘴。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0x14, 0x30, 500)
    Sleep(300)

    #C0497
    ChrTalk(
        0x14,
        "哇呀呀，你要干什么～！？\x02",
    )

    CloseMessageWindow()
    OP_64(0x14)
    OP_93(0x14, 0x0, 0x0)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x30, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_53_9042 end

    def Function_54_910C(): pass

    label("Function_54_910C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_915F")

    #C0498
    ChrTalk(
        0x31,
        "你小子让谁下来啊！？混蛋！\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x31,
        "敢捣乱的话，就把你给打飞哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9208")

    label("loc_915F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_9190")

    #C0500
    ChrTalk(
        0x31,
        (
            "瓦鲁多大哥，\x01",
            "今天要去哪里啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9208")

    label("loc_9190")


    #C0501
    ChrTalk(
        0x31,
        (
            "噢噢，今天就玩得\x01",
            "再痛快一点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x31,
        (
            "……瓦鲁多大哥，\x01",
            "今天要去哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x31,
        (
            "去斜坡那边看看景色\x01",
            "好像也很不错啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)

    label("loc_9208")

    TalkEnd(0xFE)
    Return()

    # Function_54_910C end

    def Function_55_920C(): pass

    label("Function_55_920C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9258")

    #C0504
    ChrTalk(
        0x32,
        (
            "这小子，竟敢撞到\x01",
            "瓦鲁多大哥！\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x32,
        "哈，难道想找死吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_92B4")

    label("loc_9258")


    #C0506
    ChrTalk(
        0x32,
        (
            "……噢噢！？\x01",
            "看店的那位姐姐是个美人啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x32,
        (
            "哟，姐姐，稍后\x01",
            "要不要跟我一起去转转啊～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92B4")

    TalkEnd(0xFE)
    Return()

    # Function_55_920C end

    def Function_56_92B8(): pass

    label("Function_56_92B8")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0508
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
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
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937B")
    OP_E0(0x2)
    MiniGame(0x6, 0x1, 0x10BE4, 0xFFFFF63C, 0x4074, 0xB4, 0x109C8, 0xFFFFF254, 0x2E2C)

    label("loc_937B")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_56_92B8 end

    def Function_57_9380(): pass

    label("Function_57_9380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9946")
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
            "#0100F#6P怎么办，罗伊德？\x02\x03",

            "现在要乘水上巴士\x01",
            "去米修拉姆吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0511
    ChrTalk(
        0x101,
        "#0003F#11P这个嘛……\x02",
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
            "【还有别的事要做】\x01",              # 0
            "【乘水上巴士前往米修拉姆】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_94D1"),
        (1, "loc_96B5"),
        (SWITCH_DEFAULT, "loc_9941"),
    )


    label("loc_94D1")


    #C0512
    ChrTalk(
        0x101,
        (
            "#0000F#11P前往米修拉姆之后，\x01",
            "应该就无法处理其它工作了。\x02\x03",

            "水上巴士的班次非常频繁，\x01",
            "可以先把其它事情解决后再来乘坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x102,
        "#0100F#6P是啊……\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x103,
        (
            "#0202F#1P如果要买东西，或是去工房调整装备，\x01",
            "最好也趁现在先去办完呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x104,
        (
            "#0300F#6P那么，就先把要办的事都办完，\x01",
            "然后再来这里吧。\x02",
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
            "想乘坐水上巴士时，\x01",
            "请调查旁边的时刻表。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0517
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，一旦前往米修拉姆，\x01",
            "纪念庆典期间的支援请求就会\x01",
            "强制终止，需要多加注意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 34000, -2500, 0, 270)
    EventEnd(0x5)
    Jump("loc_9941")

    label("loc_96B5")


    #C0518
    ChrTalk(
        0x101,
        (
            "#0000F#11P好……\x01",
            "那我们就在这里等待水上巴士吧。\x02\x03",

            "#0006F……那个，虽然现在说也迟了，\x01",
            "但我们穿的衣服似乎有些不太合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x102,
        (
            "#0106F#6P说得也是啊……\x02\x03",

            "#0108F还是应该穿得正式一点\x01",
            "再去比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x104,
        (
            "#0303F#6P算啦，反正我们到时\x01",
            "也不一定就能成功潜入那个宴会嘛。\x02\x03",

            "#0300F先装成去主题公园\x01",
            "游玩的游客也可以吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0521
    ChrTalk(
        0x103,
        (
            "#0203F#5P……就算如此，我也觉得\x01",
            "现在的衣服还是有些突兀了。\x02\x03",

            "#0202F不然干脆就换上『咪西』\x01",
            "的全身套装再过去怎么样？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9869():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9869)
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
            "#0012F#11P不……\x01",
            "不管怎么说，那都显眼过头了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x102,
        (
            "#0109F#12P就算那是主题公园的\x01",
            "吉祥物，也太……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_65(0x0, 0x1)
    Call(0, 59)
    Jump("loc_9941")

    label("loc_9941")

    Jump("loc_99F8")

    label("loc_9946")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0524
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前往『米修拉姆』的水上巴士·时刻表\x01\x01",
            "※米修拉姆引以为傲的主题公园\x01",
            "  『奇幻乐园』正在营业！\x01",
            "  请尽情享受一段美妙的快乐时光！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_99F8")

    Return()

    # Function_57_9380 end

    def Function_58_99F9(): pass

    label("Function_58_99F9")

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
            "#0008F#5P水上巴士的搭乘处……\x02\x03",

            "#0001F在这里就可以乘坐水上巴士\x01",
            "前往『米修拉姆』了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x102,
        (
            "#0100F#6P嗯，按照时刻表，应该是\x01",
            "每三十分钟来一班……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)

    def lambda_9B13():

        label("loc_9B13")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_9B13")

    QueueWorkItem2(0x101, 1, lambda_9B13)

    def lambda_9B25():

        label("loc_9B25")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_9B25")

    QueueWorkItem2(0x102, 1, lambda_9B25)

    def lambda_9B37():

        label("loc_9B37")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_9B37")

    QueueWorkItem2(0x104, 1, lambda_9B37)

    def lambda_9B49():
        OP_95(0xFE, 34000, -2500, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B49)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0527
    ChrTalk(
        0x103,
        (
            "#0200F#5P在纪念庆典期间，好像临时改成\x01",
            "二十分钟一班了呢。\x02\x03",

            "最后一班应该在夜里十二点半。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x101,
        "#0005F#12P一直航行到那么晚吗……\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_9BF3():
        OP_95(0xFE, 34000, -2500, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9BF3)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_9C1D():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C1D)

    def lambda_9C2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C2A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    #C0529
    ChrTalk(
        0x104,
        (
            "#0304F#6P呵，又要去主题公园游玩，\x01",
            "又要到西餐厅用餐，然后再闲聊一阵，\x01",
            "肯定会耗到很晚嘛。\x02\x03",

            "#0300F米修拉姆的酒店住宿价格\x01",
            "非常昂贵，普通人大概负担不起吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0530
    ChrTalk(
        0x102,
        (
            "#0106F#6P即使如此，现在也很有可能\x01",
            "已经全部住满了呢。\x02\x03",

            "#0100F──怎么办，罗伊德？\x02\x03",

            "现在要乘水上巴士\x01",
            "前往米修拉姆吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0531
    ChrTalk(
        0x101,
        "#0003F#11P这个嘛……\x02",
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
            "【还有别的事要做】\x01",              # 0
            "【乘水上巴士前往米修拉姆】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9DE2"),
        (1, "loc_9FCF"),
        (SWITCH_DEFAULT, "loc_A257"),
    )


    label("loc_9DE2")


    #C0532
    ChrTalk(
        0x101,
        (
            "#0000F#11P前往米修拉姆之后，\x01",
            "应该就无法处理其它工作了。\x02\x03",

            "水上巴士的班次非常频繁，\x01",
            "可以先把其它事情解决后再来乘坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x102,
        "#0100F#6P是啊……\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x103,
        (
            "#0202F#1P如果要买东西，或是去工房调整装备，\x01",
            "最好也趁现在先去办完呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x104,
        (
            "#0300F#6P那么，就先把要办的事都办完，\x01",
            "然后再来这里吧。\x02",
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
            "想乘坐水上巴士时，\x01",
            "请调查旁边的时刻表。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0537
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，一旦前往米修拉姆，\x01",
            "纪念庆典期间的支援请求就会\x01",
            "强制终止，需要多加注意。\x07\x00\x02",
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
    Jump("loc_A257")

    label("loc_9FCF")


    #C0538
    ChrTalk(
        0x101,
        (
            "#0000F#11P好……\x01",
            "那我们就在这里等待水上巴士吧。\x02\x03",

            "#0006F……那个，虽然现在说也迟了，\x01",
            "但我们穿的衣服似乎有些不太合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x102,
        (
            "#0106F#6P说得也是啊……\x02\x03",

            "#0108F还是应该穿得正式一点\x01",
            "再去比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x104,
        (
            "#0303F#6P算啦，反正我们到时\x01",
            "也不一定就能成功潜入那个宴会嘛。\x02\x03",

            "#0300F先装成去主题公园\x01",
            "游玩的游客也可以吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0541
    ChrTalk(
        0x103,
        (
            "#0203F#5P……就算如此，我也觉得\x01",
            "现在的衣服还是有些突兀了。\x02\x03",

            "#0202F不然干脆就换上『咪西』\x01",
            "的全身套装再过去怎么样？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A183():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A183)
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
            "#0012F#11P不……\x01",
            "不管怎么说，那都显眼过头了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x102,
        (
            "#0109F#12P就算那是主题公园的\x01",
            "吉祥物，也太……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 59)
    Jump("loc_A257")

    label("loc_A257")

    Return()

    # Function_58_99F9 end

    def Function_59_A258(): pass

    label("Function_59_A258")

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
        "轻浮的声音",
        (
            "嗯～……？\x01",
            "好像就是这里吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A6EA():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A6EA)

    def lambda_A6F7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6F7)
    Sleep(100)

    def lambda_A707():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A707)

    def lambda_A714():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A714)
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

    def lambda_A791():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_A791)
    WaitChrThread(0x34, 1)
    OP_6F(0x79)
    OP_0D()

    #C0545
    ChrTalk(
        0x101,
        "#0005F#6P（是游客吗……？）\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        (
            "#0100F#12P（嗯，看起来\x01",
            "  应该是呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x34, 0x2D, 0x1F4)
    Sleep(200)
    TurnDirection(0x34, 0x101, 500)
    Sleep(200)
    OP_68(39450, -1300, -5400, 2000)

    def lambda_A820():
        OP_95(0xFE, 39030, -2500, -4320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_A820)
    WaitChrThread(0x34, 1)
    OP_6F(0x79)
    Sleep(200)

    #N0547
    NpcTalk(
        0x34,
        "轻浮的青年",
        (
            "#3500F#5P哟～几位朋友。\x02\x03",

            "能不能稍微问你们\x01",
            "几句话呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        (
            "#0000F#12P嗯，可以啊。\x02\x03",

            "你看上去似乎是游客呢，\x01",
            "莫非是迷路了吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0549
    NpcTalk(
        0x34,
        "轻浮的青年",
        (
            "#3506F#5P嗯，这个地方实在是\x01",
            "太大了呢～\x02\x03",

            "#3500F那个，要去米修拉姆的话，\x01",
            "在这里等水上巴士就可以了吧？\x02",
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
            "#0005F#12P是啊，就是在这里。\x02\x03",

            "#0000F我们正好也在等待\x01",
            "开往米修拉姆的\x01",
            "水上巴士呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #N0551
    NpcTalk(
        0x34,
        "轻浮的青年",
        (
            "#3502F#5P噢，看来我找对了嘛。\x02\x03",

            "#3504F那么，我也来\x01",
            "一起排队吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0552
    NpcTalk(
        0x34,
        "轻浮的青年",
        "#3505F#5P噢，对了，忘了报上名字了。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("轻浮的青年")

    #A0553
    AnonymousTalk(
        0xFF,
        (
            "我的名字是雷克特，\x01",
            "雷克特·亚兰德尔。\x02\x03",

            "从埃雷波尼亚的帝都乘列车过来，\x01",
            "刚到了没多久呢。\x02",
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
        "#0005F#12P埃雷波尼亚的帝都……\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x102,
        "#0100F#12P原来是帝国人吗……\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x104,
        (
            "#0300F#12P嘿，但你这身个性十足的打扮，\x01",
            "倒是不太像帝国人的风格啊。\x02\x03",

            "还戴着太阳镜，\x01",
            "难不成是来度假的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x34,
        (
            "#3509F#5P是啊，克洛斯贝尔\x01",
            "最近在度假胜地中也是很有名气的啊！\x02\x03",

            "正所谓入乡随俗，从这方面也能\x01",
            "看出我来这里游玩的干劲有多高吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x103,
        (
            "#0206F#6P但这干劲好像\x01",
            "没用对地方呢……\x02\x03",

            "#0202F想必你也是为了\x01",
            "主题公园而来的吧？\x02",
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
            "#3505F#5P主题公园？\x02\x03",

            "#3501F……那是什么啊，\x01",
            "米修拉姆还有那么\x01",
            "有意思的东西啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x101,
        (
            "#0012F#12P嗯，是啊……\x01",
            "虽然我也没有去过。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x102,
        (
            "#0109F#12P其实米修拉姆原来是个疗养地，\x01",
            "但最近却是乐园变得更有名气了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x34,
        (
            "#3500F#5P嘿～原来如此啊。\x02\x03",

            "#3506F唉，因为我这次只是以代理人的身份\x01",
            "前来出席的，所以准备不足啊。\x02\x03",

            "看样子，在过来之前，\x01",
            "真应该多做些事前调查啊。\x02",
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
        "#0001F#12P以代理人的身份出席……？\x02",
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
        "#3502F#6P噢，好像来了呢。\x02",
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

    def lambda_B014():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_B014)
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

    def lambda_B0E8():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_B0E8)
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
            "#3504F#6P嗯，相当\x01",
            "不错的船嘛。\x02\x03",

            "#3500F好，本少爷就先去抢占\x01",
            "甲板席最前排的座位啦。\x02\x03",

            "#3509F那么，先走一步喽～¤\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x34, 3, 0, 63)
    Sleep(500)

    def lambda_B31B():

        label("loc_B31B")

        TurnDirection(0x101, 0x34, 300)
        Yield()
        Jump("loc_B31B")

    QueueWorkItem2(0x101, 1, lambda_B31B)

    def lambda_B32D():

        label("loc_B32D")

        TurnDirection(0x102, 0x34, 300)
        Yield()
        Jump("loc_B32D")

    QueueWorkItem2(0x102, 1, lambda_B32D)

    def lambda_B33F():

        label("loc_B33F")

        TurnDirection(0x103, 0x34, 300)
        Yield()
        Jump("loc_B33F")

    QueueWorkItem2(0x103, 1, lambda_B33F)

    def lambda_B351():

        label("loc_B351")

        TurnDirection(0x104, 0x34, 300)
        Yield()
        Jump("loc_B351")

    QueueWorkItem2(0x104, 1, lambda_B351)
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
            "#0106F#5P好像是个比兰迪\x01",
            "还要不正经的\x01",
            "人呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0567
    ChrTalk(
        0x104,
        (
            "#0303F#2P这叫什么话～\x02\x03",

            "#0301F我可不像他那样游手好闲、\x01",
            "轻浮胡闹吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x103,
        (
            "#0211F#6P……可我觉得你已经\x01",
            "十分轻浮和胡闹了。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        (
            "#0012F#6P哈，就算同样是轻浮胡闹的人，\x01",
            "也包括多种不同的类型呢。\x02\x03",

            "#0000F比起像兰迪这样\x01",
            "将夜游和搭讪当成兴趣爱好的人，\x01",
            "他更多了一种莫名的洒脱感呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0570
    ChrTalk(
        0x104,
        (
            "#0309F#11P噢噢，你很清楚嘛～\x02\x03",

            "#0300F看他的年龄大概和我差不多，\x01",
            "一个人来这里要做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x33, 0x80)
    ClearChrBattleFlags(0x33, 0x8000)

    #N0571
    NpcTalk(
        0x33,
        "女性的声音",
        "啊呀──很巧呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B676():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B676)

    def lambda_B683():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B683)
    Sleep(100)

    def lambda_B693():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B693)

    def lambda_B6A0():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B6A0)
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

    def lambda_B71D():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_B71D)
    WaitChrThread(0x33, 1)
    TurnDirection(0x33, 0x101, 500)
    OP_6F(0x79)
    OP_0D()

    #C0572
    ChrTalk(
        0x101,
        "#0005F#12P您是……\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x104,
        (
            "#0305F#12P噢噢……！？\x01",
            "这不是雾香小姐吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(39450, -1300, -5400, 2000)

    def lambda_B798():
        OP_95(0xFE, 39030, -2500, -4320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_B798)
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
            "呵呵，前天承蒙关照了。\x02\x03",

            "既然会在这里相遇，也就是说，\x01",
            "你们也要去米修拉姆吗？\x02",
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
            "#0100F#12P是啊……\x01",
            "雾香小姐也是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x33,
        (
            "#3404F#5P嗯，一半为工作，一半为观光吧。\x02\x03",

            "#3400F说起来……\x01",
            "刚才那位打扮奇特的男孩子是谁呢？\x02\x03",

            "是你们的朋友吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x101,
        (
            "#0004F#12P不……\x01",
            "是刚刚才认识的。\x02\x03",

            "#0000F听说是从埃雷波尼亚\x01",
            "的帝都前来观光的。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x33,
        (
            "#3405F#5P从帝都……\x02\x03",

            "#3404F……呵呵，原来如此啊。\x02",
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
            "#0205F#6P莫非雾香小姐\x01",
            "和他认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x33,
        (
            "#3404F#5P不，只是他身上散发\x01",
            "出来的那种独特气息让我\x01",
            "犯了职业病。\x02\x03",

            "#3400F那么，我就先走一步……\x01",
            "你们也快点上去吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(35100, 0, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)

    def lambda_BA77():

        label("loc_BA77")

        TurnDirection(0x101, 0x33, 300)
        Yield()
        Jump("loc_BA77")

    QueueWorkItem2(0x101, 1, lambda_BA77)

    def lambda_BA89():

        label("loc_BA89")

        TurnDirection(0x102, 0x33, 300)
        Yield()
        Jump("loc_BA89")

    QueueWorkItem2(0x102, 1, lambda_BA89)

    def lambda_BA9B():

        label("loc_BA9B")

        TurnDirection(0x103, 0x33, 300)
        Yield()
        Jump("loc_BA9B")

    QueueWorkItem2(0x103, 1, lambda_BA9B)

    def lambda_BAAD():

        label("loc_BAAD")

        TurnDirection(0x104, 0x33, 300)
        Yield()
        Jump("loc_BAAD")

    QueueWorkItem2(0x104, 1, lambda_BAAD)
    OP_93(0x33, 0x41, 0x1F4)

    def lambda_BAC6():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_BAC6)
    WaitChrThread(0x33, 1)
    OP_93(0x33, 0x5A, 0x0)

    def lambda_BAE6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_BAE6)
    Sleep(2000)

    def lambda_BAFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_BAFE)
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
            "#0309F#12P呀～……\x01",
            "还是一如既往的冰冷又美丽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x101,
        (
            "#0000F#6P说是一半为了工作……\x01",
            "那应该是要去主题公园吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x102,
        (
            "#0100F#5P既然是从事演艺方面的工作，\x01",
            "那种可能性应该很高……\x02",
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
        "#0205F#12P巴士好像快要出航了呢。\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x101,
        "#0000F#6P是啊，我们也赶快上去吧。\x02",
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

    def lambda_BD73():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_BD73)
    WaitChrThread(0x35, 1)

    def lambda_BD91():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_BD91)
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

    # Function_59_A258 end

    def Function_60_BDD1(): pass

    label("Function_60_BDD1")


    def lambda_BDD6():
        OP_9B(0x0, 0xFE, 0x0, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BDD6)

    def lambda_BDEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BDEB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_60_BDD1 end

    def Function_61_BE00(): pass

    label("Function_61_BE00")


    def lambda_BE05():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE05)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_BE25():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE25)
    Sleep(3000)

    def lambda_BE3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BE3D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_61_BE00 end

    def Function_62_BE52(): pass

    label("Function_62_BE52")


    def lambda_BE57():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE57)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_BE77():
        OP_9B(0x0, 0xFE, 0x0, 0x1FA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE77)
    Sleep(3500)

    def lambda_BE8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BE8F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_62_BE52 end

    def Function_63_BEA4(): pass

    label("Function_63_BEA4")

    OP_95(0xFE, 42770, -2500, -2020, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)

    def lambda_BEC4():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BEC4)
    Sleep(1700)

    def lambda_BEDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BEDC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_63_BEA4 end

    def Function_64_BEF1(): pass

    label("Function_64_BEF1")

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

    # Function_64_BEF1 end

    def Function_65_BF83(): pass

    label("Function_65_BF83")

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
        "#0013F#5P那是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 72)
    Return()

    # Function_65_BF83 end

    def Function_66_C095(): pass

    label("Function_66_C095")

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
        "#0013F#5P那是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 72)
    Return()

    # Function_66_C095 end

    def Function_67_C1A7(): pass

    label("Function_67_C1A7")

    OP_95(0xFE, 250, 0, 14720, 4000, 0x0)
    OP_95(0xFE, 1930, 0, 14500, 4000, 0x0)
    OP_95(0xFE, 3230, 500, 17000, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_67_C1A7 end

    def Function_68_C1EB(): pass

    label("Function_68_C1EB")

    OP_95(0xFE, 800, 0, 12080, 4000, 0x0)
    OP_95(0xFE, 4400, 70, 16149, 4000, 0x0)
    TurnDirection(0xFE, 0x37, 500)
    Return()

    # Function_68_C1EB end

    def Function_69_C21B(): pass

    label("Function_69_C21B")

    OP_95(0xFE, 250, 0, 14720, 4000, 0x0)
    OP_95(0xFE, 1230, 0, 14880, 4000, 0x0)
    OP_95(0xFE, 2230, 200, 16400, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_69_C21B end

    def Function_70_C25F(): pass

    label("Function_70_C25F")

    OP_95(0xFE, 800, 0, 12080, 4000, 0x0)
    OP_95(0xFE, 3400, 0, 15350, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_70_C25F end

    def Function_71_C28F(): pass

    label("Function_71_C28F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C4A9")

    def lambda_C29F():
        OP_9D(0xFE, 0xF14, 0x0, 0x2F58, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_C29F)
    Sound(814, 0, 100, 0)
    Sound(541, 0, 100, 0)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrSubChip(0x3A, 0x0)

    def lambda_C2D0():
        OP_9D(0xFE, 0x17DE, 0x0, 0x2D64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_C2D0)
    OP_A0(0x3A, 2000, 0x0, 0x5)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)
    SetChrChipByIndex(0x3F, 0x2C)
    SetChrSubChip(0x3F, 0x0)

    def lambda_C304():
        OP_9D(0xFE, 0x1234, 0x0, 0x2E72, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_C304)
    Sound(814, 0, 100, 0)
    Sound(541, 0, 100, 0)
    OP_A0(0x3F, 2000, 0x0, 0x3)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_C371():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x32, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_C371)
    OP_A0(0x3F, 2000, 0x4, 0x5)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrChipByIndex(0x3F, 0x2C)

    def lambda_C39D():
        OP_A0(0x3A, 4000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_C39D)

    def lambda_C3AA():
        OP_A0(0x3F, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_C3AA)
    OP_9D(0x3A, 0xC8A, 0x0, 0x2F58, 0x32, 0x7D0)
    SetChrSubChip(0x3A, 0x5)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_C40F():

        label("loc_C40F")

        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        Yield()
        Jump("loc_C40F")

    QueueWorkItem2(0x3A, 2, lambda_C40F)

    def lambda_C42D():

        label("loc_C42D")

        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        Yield()
        Jump("loc_C42D")

    QueueWorkItem2(0x3F, 2, lambda_C42D)
    Sleep(1500)
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)

    def lambda_C466():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_C466)

    def lambda_C483():
        OP_9D(0xFE, 0x1388, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_C483)
    Sound(804, 0, 100, 0)
    Sleep(1000)
    Jump("Function_71_C28F")

    label("loc_C4A9")

    Return()

    # Function_71_C28F end

    def Function_72_C4AA(): pass

    label("Function_72_C4AA")

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
            "#11P嘿，蓝衣服小子！\x01",
            "尽管放马过来吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x3A,
        "用不着你说！\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x3A,
        "我来了！\x02",
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
            "#0105F那是……\x01",
            "他们在干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x103,
        (
            "#0200F虽然情况看上去好像并\x01",
            "没有多险恶……\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        (
            "#0305F但看起来似乎\x01",
            "也不像是一般的单挑……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x101,
        (
            "#0006F总之，过去问问情况吧。\x02\x03",

            "#0001F幸好瓦吉和瓦鲁多\x01",
            "两个人也都在──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 20, -1, -1)
    SetChrName("女孩的声音")

    #A0596
    AnonymousTalk(
        0xFF,
        (
            "等一下，等一下！\x01",
            "你们在干什么呢？\x02",
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

    def lambda_CB1A():
        OP_A0(0x3A, 5000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_CB1A)

    def lambda_CB27():
        OP_A0(0x3F, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_CB27)
    SetChrPos(0x3F, 3790, 0, 11880, 270)
    SetChrPos(0x3A, 2340, 0, 12120, 90)
    SetChrSubChip(0x3A, 0x5)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_CB97():

        label("loc_CB97")

        OP_A6(0xFE, 0x0, 0x19, 0x96, 0x5DC)
        Yield()
        Jump("loc_CB97")

    QueueWorkItem2(0x3A, 2, lambda_CB97)

    def lambda_CBB5():

        label("loc_CBB5")

        OP_A6(0xFE, 0x0, 0x19, 0x96, 0x5DC)
        Yield()
        Jump("loc_CBB5")

    QueueWorkItem2(0x3F, 2, lambda_CBB5)
    ClearChrFlags(0x36, 0x80)
    ClearChrBattleFlags(0x36, 0x8000)
    ClearChrFlags(0x37, 0x80)
    ClearChrBattleFlags(0x37, 0x8000)

    def lambda_CBE7():
        OP_95(0xFE, 4200, 2000, 20900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_CBE7)
    Sleep(50)

    def lambda_CC04():
        OP_95(0xFE, 3400, 2000, 22200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_CC04)
    WaitChrThread(0x36, 1)
    SetChrChipByIndex(0x36, 0x1E)
    SetChrSubChip(0x36, 0x0)

    def lambda_CC2A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x36, 2, lambda_CC2A)
    WaitChrThread(0x37, 1)
    SetChrChipByIndex(0x37, 0x1F)
    SetChrSubChip(0x37, 0x0)

    def lambda_CC43():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x37, 2, lambda_CC43)

    def lambda_CC50():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_CC50)
    Sleep(50)

    def lambda_CC60():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_CC60)
    Sleep(50)
    TurnDirection(0x39, 0x36, 500)
    OP_0D()

    #C0597
    ChrTalk(
        0x2E,
        "#1605F#12P嗯……？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x38,
        "#0405F#12P……咦………\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x36,
        (
            "#0806F真是的，接到联络之后\x01",
            "马上就赶过来看，人还真不少嘛……\x02\x03",

            "#0801F你们就是旧城区的\x01",
            "圣书会和剑蛇帮吧？\x02\x03",

            "请你们停止斗殴！\x01",
            "马上解散！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)

    def lambda_CD4D():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_CD4D)

    def lambda_CD6A():
        OP_9D(0xFE, 0x1388, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_CD6A)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x3A, 0)
    WaitChrThread(0x3F, 0)

    def lambda_CD95():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_CD95)

    def lambda_CDA2():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x40, 0, lambda_CDA2)

    def lambda_CDAF():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x41, 0, lambda_CDAF)

    def lambda_CDBC():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x42, 0, lambda_CDBC)

    def lambda_CDC9():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x43, 0, lambda_CDC9)

    def lambda_CDD6():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_CDD6)

    def lambda_CDE3():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3B, 0, lambda_CDE3)

    def lambda_CDF0():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3C, 0, lambda_CDF0)

    def lambda_CDFD():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3D, 0, lambda_CDFD)

    #C0600
    ChrTalk(
        0x2E,
        "#1601F#12P什么啊，你们……\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x37,
        (
            "#0903F我们是游击士协会的人。\x02\x03",

            "#0901F刚才接到联络，听说你们在此斗殴，\x01",
            "所以前来进行仲裁。\x02",
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
        "#1605F#12P游击士……！？\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x38,
        (
            "#0404F#6P#N艾丝蒂尔·布莱特和\x01",
            "约修亚·布莱特……\x02\x03",

            "#0400F呵呵，在杂志上见过\x01",
            "你们很多次呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0604
    ChrTalk(
        0x36,
        (
            "#0806F#5P那可多谢啦。\x02\x03",

            "#0800F那个，你们应该就是\x01",
            "两边的头领吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x38,
        (
            "#0404F#6P#N算是吧。\x02\x03",

            "#0400F我是圣书会的瓦吉，\x01",
            "他是剑蛇帮的瓦鲁多。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0606
    ChrTalk(
        0x37,
        (
            "#0903F#5P与情报一致呢。\x02\x03",

            "#0900F看起来，你们好像\x01",
            "并不是在斗殴吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x38,
        (
            "#0404F#6P#N呵呵，只是个单纯的游戏而已。\x02\x03",

            "毕竟是难得的纪念庆典嘛，\x01",
            "所以总想做些和平时\x01",
            "不同的事情。\x02\x03",

            "#0402F然后，就发展成这种\x01",
            "单挑淘汰战啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0608
    ChrTalk(
        0x36,
        "#0805F#5P单、单挑淘汰战～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x39, 0x36, 500)

    #C0609
    ChrTalk(
        0x39,
        (
            "#6P……两边各派出五个人，\x01",
            "以一对一的方式来分出胜负。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x39,
        "#6P我们的大将是瓦吉，那边的大将是瓦鲁多。\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x39,
        (
            "#6P而最终战败的一方，将要\x01",
            "在纪念庆典期间内，担负获胜一方的全部饮食费。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x36,
        (
            "#0805F#5P原来如此，看起来只是比赛而已呢。\x02\x03",

            "#0809F那样的话就无所谓──\x02",
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
            "#0806F#5P啊！不对不对！\x02\x03",

            "#0801F就算只是比赛，\x01",
            "也不能在这种地方进行吧！？\x02\x03",

            "这里有这么多来来往往的人，\x01",
            "你们就不能去别的地方吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x2E,
        (
            "#1603F#12P哈，去哪里是我们的自由。\x02\x03",

            "#1601F话说回来，你听好……\x01",
            "我可不管你们是游击士还是什么，\x01",
            "但态度未免也太嚣张了吧。\x02\x03",

            "可不要得意忘形啊，嗯？\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x36,
        (
            "#0803F#5P那个……\x01",
            "得意忘形的明明是你们吧。\x02\x03",

            "#0801F我只是说了些常识性\x01",
            "的事情而已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x2E,
        "#1600F#12P这小丫头……\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x0, 0x1F4)
    OP_68(5860, 2550, 20980, 2000)

    def lambda_D41A():

        label("loc_D41A")

        TurnDirection(0xFE, 0x2E, 500)
        Yield()
        Jump("loc_D41A")

    QueueWorkItem2(0x36, 2, lambda_D41A)

    def lambda_D42C():

        label("loc_D42C")

        TurnDirection(0xFE, 0x2E, 500)
        Yield()
        Jump("loc_D42C")

    QueueWorkItem2(0x37, 2, lambda_D42C)
    OP_95(0x2E, 6200, 2000, 20800, 2000, 0x0)
    TurnDirection(0x2E, 0x36, 500)
    EndChrThread(0x36, 0x2)
    EndChrThread(0x37, 0x2)

    #C0617
    ChrTalk(
        0x2E,
        (
            "#1604F#11P看来，是非得让你\x01",
            "受点教训才行了啊？\x02\x03",

            "#1602F顺便也疼爱一下那边的\x01",
            "那个黑头发小子，如何呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x36,
        (
            "#0806F#6P嗯、嗯～……\x02\x03",

            "#0808F约修亚，要怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x37,
        (
            "#0903F#5P算了，四周都有人在看……\x02\x03",

            "#0900F我想还是不要做出\x01",
            "太过孩子气的行为吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x36,
        "#0802F#6P果然是这样吗？\x02",
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
            "#1607F#11P你们两个……\x01",
            "在那里窃窃私语个什么！\x02\x03",

            "难道就不怕我『碎鬼』——\x01",
            "瓦鲁多·瓦雷斯大爷吗！？\x02",
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
            "#0406F#6P#N──住手吧，瓦鲁多。\x02\x03",

            "#0400F这位小姐的武术造诣，\x01",
            "也许在你之上哦。\x02",
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
        "#1605F#11P你说什么……！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x36, 0x38, 500)
    Sleep(150)

    #C0624
    ChrTalk(
        0x36,
        "#0800F#5P嘿，你看出来了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x38, 0x36, 500)
    Sleep(150)

    #C0625
    ChrTalk(
        0x38,
        (
            "#0404F#12P#N大概吧，不过呢。\x02\x03",

            "#0402F那边的小兄弟，\x01",
            "实力似乎更在你之上吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x37, 0x38, 500)
    Sleep(150)

    #C0626
    ChrTalk(
        0x37,
        (
            "#0902F#5P哈哈……\x01",
            "我也尚需修行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x36,
        (
            "#0806F#5P嗯～……\x01",
            "约修亚比我厉害，这确实\x01",
            "是事实啦，不过呢……\x02\x03",

            "#0801F被你这么一断言，\x01",
            "还是稍微有些难以接受呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x37,
        (
            "#0904F#5P算了算了，游击士的工作\x01",
            "又不是只有战斗。\x02",
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
            "#1602F#11P哼哼哼……\x01",
            "这种小丫头的实力在我之上？\x02\x03",

            "#1607F哈……\x01",
            "那就证明给我看看吧！！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(5680, 2550, 20990, 1000)
    SetCameraDistance(21320, 1000)

    def lambda_D8D1():

        label("loc_D8D1")

        TurnDirection(0xFE, 0x2E, 600)
        Yield()
        Jump("loc_D8D1")

    QueueWorkItem2(0x36, 0, lambda_D8D1)
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
        "#0901F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x36,
        "#0804F#6P没问题，交给我吧。\x02",
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

    def lambda_D9A9():

        label("loc_D9A9")

        TurnDirection(0xFE, 0x2E, 300)
        Yield()
        Jump("loc_D9A9")

    QueueWorkItem2(0x37, 0, lambda_D9A9)
    SetChrChipByIndex(0x2E, 0x30)
    SetChrSubChip(0x2E, 0x0)
    SetChrPos(0x2E, 5300, 2300, 20900, 270)
    Sound(804, 0, 100, 0)
    OP_D3(0x2E, 0x0, 0x0, 0x15F90, 0x0)
    Sound(1648, 255, 100, 0)    #voice#Estelle
    Sound(534, 0, 100, 0)
    ClearChrFlags(0x2E, 0x1)
    ClearChrFlags(0x2E, 0x100)

    def lambda_DA03():
        OP_9D(0xFE, 0x9C4, 0x7D0, 0x526C, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_DA03)
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
        "#1605F#11P啊……？\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x38,
        "#0406F#6P看吧，我早就说过的。\x02",
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
        "#11P瓦、瓦鲁多大哥竟然！？\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x3F,
        "#5P那、那小丫头到底是……！？\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x3B,
        "#5P好厉害……！\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x3A,
        "#5P那就是游击士……！\x02",
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
        "#0805F#12P那个，你没事吧？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x2E, 0x2)

    def lambda_DCDD():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_DCDD)
    WaitChrThread(0x2E, 2)
    #Sound(1808, 255, 100, 0)    #voice#Wald

    #C0639
    ChrTalk(
        0x2E,
        "#1604F#11P呵呵……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_DD1B():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_DD1B)
    SetChrSubChip(0x2E, 0x1)
    #Sound(1809, 255, 100, 0)    #voice#Wald
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0640
    ChrTalk(
        0x2E,
        "#1609F#4S#11P#N哈哈哈哈哈哈哈哈哈哈！！\x02",
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

    def lambda_DDB5():
        TurnDirection(0xFE, 0x36, 800)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_DDB5)
    OP_9C(0x2E, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrFlags(0x2E, 0x1)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0641
    ChrTalk(
        0x2E,
        (
            "#1604F#5P──真抱歉，\x01",
            "看来我确实是小看你了。\x02\x03",

            "#1601F可是啊……\x01",
            "你也未免太看不起我了吧！？\x02",
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

    def lambda_DE96():

        label("loc_DE96")

        TurnDirection(0xFE, 0x36, 100)
        Yield()
        Jump("loc_DE96")

    QueueWorkItem2(0x37, 2, lambda_DE96)
    SetChrFlags(0x2E, 0x20)
    Sound(1789, 255, 100, 0)    #voice#Wald
    Sound(532, 0, 100, 0)

    def lambda_DEB9():
        OP_96(0xFE, 0xAF0, 0x7D0, 0x529E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_DEB9)
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
        "#0807F#12P真、真危险……！\x02",
    )

    CloseMessageWindow()
    #Sound(1780, 255, 100, 0)    #voice#Joshua

    #C0644
    ChrTalk(
        0x37,
        "#0901F#5P艾丝蒂尔……！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x37, 0x2)
    SetChrChipByIndex(0x37, 0x32)
    SetChrSubChip(0x37, 0x3)

    def lambda_DF95():
        OP_9D(0xFE, 0x157C, 0x7D0, 0x5078, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_DF95)
    Sound(814, 0, 100, 0)

    def lambda_DFB8():

        label("loc_DFB8")

        TurnDirection(0xFE, 0x2E, 1000)
        Yield()
        Jump("loc_DFB8")

    QueueWorkItem2(0x37, 2, lambda_DFB8)
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
            "#0404F#6P哎呀呀……\x02\x03",

            "#0400F──你们是不是也\x01",
            "太得意忘形了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x37,
        (
            "#0903F#11P嗯，似乎是有点呢。\x02\x03",

            "#0901F但即使如此，我想我们\x01",
            "也并没有道歉的理由呢……\x02",
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
            "#1602F#5P呵呵……\x01",
            "你的眼神变了呢。\x02\x03",

            "#1604F我明白了──你相当厉害呢。\x02\x03",

            "#1601F把你这种厉害的家伙打得落花流水，\x01",
            "对我来说就是最大的乐趣啊！\x02\x03",

            "赶快动手吧，啊啊！？\x02",
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
            "#0801F#12P等、等一下啊，约修亚！\x02\x03",

            "我没有关系的，\x01",
            "你可不要和他们认真啊！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    #Sound(1086, 255, 100, 0)    #voice#Lloyd

    #N0650
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "──等一下！\x02",
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

    def lambda_E32B():

        label("loc_E32B")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_E32B")

    QueueWorkItem2(0x36, 0, lambda_E32B)

    def lambda_E33D():

        label("loc_E33D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E33D")

    QueueWorkItem2(0x37, 0, lambda_E33D)

    def lambda_E34F():

        label("loc_E34F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E34F")

    QueueWorkItem2(0x38, 0, lambda_E34F)

    def lambda_E361():

        label("loc_E361")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E361")

    QueueWorkItem2(0x2E, 0, lambda_E361)

    def lambda_E373():

        label("loc_E373")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E373")

    QueueWorkItem2(0x39, 0, lambda_E373)

    def lambda_E385():

        label("loc_E385")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E385")

    QueueWorkItem2(0x3F, 0, lambda_E385)

    def lambda_E397():

        label("loc_E397")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E397")

    QueueWorkItem2(0x40, 0, lambda_E397)

    def lambda_E3A9():

        label("loc_E3A9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E3A9")

    QueueWorkItem2(0x41, 0, lambda_E3A9)

    def lambda_E3BB():

        label("loc_E3BB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E3BB")

    QueueWorkItem2(0x42, 0, lambda_E3BB)

    def lambda_E3CD():

        label("loc_E3CD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E3CD")

    QueueWorkItem2(0x43, 0, lambda_E3CD)

    def lambda_E3DF():

        label("loc_E3DF")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E3DF")

    QueueWorkItem2(0x3A, 0, lambda_E3DF)

    def lambda_E3F1():

        label("loc_E3F1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E3F1")

    QueueWorkItem2(0x3B, 0, lambda_E3F1)

    def lambda_E403():

        label("loc_E403")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E403")

    QueueWorkItem2(0x3C, 0, lambda_E403)
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
        "#0405F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x36,
        "#0805F#11P是罗伊德他们……？\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x101,
        (
            "#0003F#6P大致情况我已经了解了。\x02\x03",

            "#0001F双方都先……\x01",
            "稍微冷静一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x2E,
        (
            "#1601F#5P#N哈？我能冷静得下来吗！\x02\x03",

            "#1604F游击士！很有一套嘛！\x02\x03",

            "#1607F虽然早就听过传闻，但真没想到\x01",
            "竟然能让本大爷兴奋到如此程度啊！！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0655
    ChrTalk(
        0x101,
        (
            "#0006F#6P所以才要你们稍微\x01",
            "冷静一下啊……\x02\x03",

            "#0001F再怎么说，这里也是公共场所。\x02\x03",

            "不管是单挑比赛也好，\x01",
            "讲道理也好，\x01",
            "都请换个地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x38,
        (
            "#0406F#11P嗯～话虽如此。\x02\x03",

            "#0402F但大家都已经闹到这个地步了，难道\x01",
            "还能说一句『好，解散』，然后就此收场吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x101,
        "#0011F#6P瓦吉……！？\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x38,
        (
            "#0402F#11P瓦鲁多已经热血沸腾了，\x01",
            "这位小姐也是为工作而来。\x02\x03",

            "#0409F如果不让他们分出个胜负，\x01",
            "未免也太没道理了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0x36, 500)
    Sleep(300)

    #C0659
    ChrTalk(
        0x2E,
        "#1602F#6P呵呵，正是如此……！\x02",
    )

    CloseMessageWindow()

    def lambda_E719():
        TurnDirection(0xFE, 0x2E, 400)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_E719)
    Sleep(50)

    def lambda_E729():
        TurnDirection(0xFE, 0x2E, 400)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_E729)
    Sleep(300)

    #C0660
    ChrTalk(
        0x36,
        (
            "#0803F#12P……我也稍微有点\x01",
            "生气了哦。\x02\x03",

            "#0801F既然你有此意，\x01",
            "我也不介意来场决斗。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x2E,
        "#1607F#6P好，够胆量……！\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x101,
        (
            "#0006F#6P啊啊，真是……！\x02\x03",

            "#0013F约修亚！\x01",
            "你也说点什么吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x37,
        (
            "#0908F#12P……抱歉，\x01",
            "我也不打算退让呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x101,
        "#0011F#6P唔……\x02",
    )

    CloseMessageWindow()

    def lambda_E830():

        label("loc_E830")

        TurnDirection(0xFE, 0x37, 400)
        Yield()
        Jump("loc_E830")

    QueueWorkItem2(0x38, 0, lambda_E830)
    Sleep(300)

    #C0665
    ChrTalk(
        0x38,
        (
            "#0404F#6P呵呵，那么，\x01",
            "我就来帮瓦鲁多吧。\x02\x03",

            "#0402F即使是你，想独自对抗\x01",
            "那两个人，恐怕也相当勉强吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x2E,
        "#1603F#5P#N哼……随你高兴吧。\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#0007F#6P啊啊啊～！\x01",
            "为什么会变成这样啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x102,
        "#0106F#5P（真、真令人头疼啊……）\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x103,
        (
            "#0211F#5P（再这样下去，肯定会\x01",
            "  演变成一场激烈的乱斗事件……）\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x104,
        (
            "#0303F#6P#N──那个。\x02\x03",

            "#0300F既然你们那么想比试，\x01",
            "换个方法应该也可以吧？\x02",
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

    def lambda_EA51():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EA51)
    Sleep(50)

    def lambda_EA61():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_EA61)

    def lambda_EA6E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_EA6E)
    Sleep(50)

    def lambda_EA7E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EA7E)

    def lambda_EA8B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EA8B)
    Sleep(50)

    def lambda_EA9B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x38, 0, lambda_EA9B)

    def lambda_EAA8():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_EAA8)
    Sleep(50)

    def lambda_EAB8():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_EAB8)
    OP_6F(0x1)

    #C0671
    ChrTalk(
        0x101,
        "#0005F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x38,
        "#0405F#5P#N嗯……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0673
    ChrTalk(
        0x104,
        (
            "#0306F#6P难得的纪念庆典，\x01",
            "如果彼此结怨可就太扫兴了吧。\x02\x03",

            "#0302F所以啦，不妨换个爽快\x01",
            "一点的决斗方法，如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x2E,
        "#1601F#5P#N爽快的方法……？\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x36,
        (
            "#0805F#11P#N那个……\x01",
            "兰迪先生，那是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0676
    ChrTalk(
        0x104,
        "#0304F#6P啊，那就是──\x02",
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

    # Function_72_C4AA end

    def Function_73_EC04(): pass

    label("Function_73_EC04")

    Sleep(350)
    SetChrChip(0x0, 0x36, 0x1E, 0x12C)
    SetChrChipByIndex(0x36, 0x31)
    SetChrSubChip(0x36, 0x3)

    def lambda_EC1C():
        OP_9D(0xFE, 0x189C, 0x7D0, 0x5078, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_EC1C)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x36, 0)
    PlayEffect(0x1, 0xFF, 0x36, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x36, 0x1E)
    SetChrSubChip(0x36, 0x0)
    Sleep(150)
    SetChrChip(0x1, 0x36, 0x0, 0x0)
    Return()

    # Function_73_EC04 end

    def Function_74_EC89(): pass

    label("Function_74_EC89")

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

    # Function_74_EC89 end

    def Function_75_F020(): pass

    label("Function_75_F020")

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
            "#12P#0000F不好意思，\x01",
            "我们是克洛斯贝尔警察局的人……\x02\x03",

            "接到支援请求而来。\x01",
            "请问工商协会的接待帐篷\x01",
            "就是这里吧？\x02",
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
        "#11P噢噢，你们来了啊。\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x1A,
        (
            "#11P而且……\x01",
            "没想到受理委托的人\x01",
            "竟然是你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x101,
        (
            "#12P#0000F哈哈，因为不止协会，支援科\x01",
            "也接到了这个委托的相关情报呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_END)), "loc_F3BF")

    #C0681
    ChrTalk(
        0x102,
        (
            "#12P#0100F总之，还要麻烦您多加协助哦，\x01",
            "会长先生。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x1A, 500)
    Sleep(300)

    #C0682
    ChrTalk(
        0x15,
        (
            "#5P哎，会长，\x01",
            "你们认识吗……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x15, 500)
    Sleep(300)

    #C0683
    ChrTalk(
        0x1A,
        (
            "#11P嗯，我乘坐导力列车回来时，\x01",
            "这位青年就坐在我对面。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x101,
        (
            "#12P#0000F那还是我担任\x01",
            "警察工作之前的事呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F310():
        OP_93(0xFE, 0xC6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_F310)

    def lambda_F31D():
        OP_93(0xFE, 0xC6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F31D)
    Sleep(300)

    #C0685
    ChrTalk(
        0x1A,
        (
            "#11P呵呵，是啊。\x01",
            "自那之后，我们也稍微\x01",
            "有过几次接触呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x1A,
        (
            "#11P……事情稍微有些棘手。\x01",
            "不好意思，特别任务支援科的各位，\x01",
            "这次就要麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F53D")

    label("loc_F3BF")

    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0687
    ChrTalk(
        0x103,
        (
            "#6P#0205F哎，是罗伊德前辈\x01",
            "认识的人吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0688
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，在我去警察局报到之前认识的。\x01",
            "在回克洛斯贝尔的列车上，\x01",
            "我们偶然坐在相对的座位呢。\x02\x03",

            "在之后的闲谈中，\x01",
            "得知他就是工商协会的会长先生。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F499():
        OP_93(0xFE, 0xF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F499)

    def lambda_F4A6():
        OP_93(0xFE, 0xF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F4A6)
    Sleep(300)

    #C0689
    ChrTalk(
        0x1A,
        (
            "#11P呵呵，我也不知道\x01",
            "当时那个青年\x01",
            "竟然会是警官。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x1A,
        (
            "#11P……事情稍微有些棘手。\x01",
            "不好意思，特别任务支援科的各位，\x01",
            "这次就要麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F53D")


    #C0691
    ChrTalk(
        0x101,
        (
            "#12P#0004F嗯，请交给我们吧。\x02\x03",

            "#0001F那个……委托内容\x01",
            "好像是解决盗窃案吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x104,
        "#12P#0301F是连环盗窃犯吗？\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x15,
        "#5P正、正是啊。\x02",
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x15,
        (
            "#5P从昨天到今天，\x01",
            "已经连续出现了四起……\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x15,
        "#5P所有店铺的销售额都受了影响呢！\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x1A,
        (
            "#11P纪念庆典的露天店\x01",
            "都是由工商协会负责统一管理的。\x01",
            "虽然情报是从各处收集而来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x1A,
        (
            "#11P但将它们综合到一起来看，作案者似乎是\x01",
            "以露天店铺为目标的连环盗窃犯。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x1A,
        (
            "#11P但由于并没有什么关于犯人的具体线索，\x01",
            "我们现在能做的也只有让大家自己注意了。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x102,
        (
            "#12P#0101F是吗……\x01",
            "那真是很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x103,
        (
            "#6P#0203F而且，这样下去，\x01",
            "受害店铺也许还会继续增加呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x1A,
        (
            "#11P嗯，这也正是把你们\x01",
            "叫来的原因啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x1A,
        (
            "#11P站在工商协会的立场来说，\x01",
            "也无法再继续坐视不理了……\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x1A,
        (
            "#11P毕竟，再这么下去，\x01",
            "甚至可能会给前来享受庆典\x01",
            "的客人们也带来麻烦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x1A,
        (
            "#11P希望你们能帮忙\x01",
            "将犯人逮捕。\x02",
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
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8AB")
    OP_29(0x20, 0x1, 0x1)
    Call(0, 76)
    Return()

    label("loc_F8AB")


    #C0705
    ChrTalk(
        0x101,
        (
            "#12P#0006F实在抱歉，我们现在\x01",
            "还有其它工作，脱不开身……\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x1A,
        "#11P是吗，那就没办法了啊。\x02",
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x1A,
        (
            "#11P等你们有空了再来吧。\x01",
            "希望能在下一个受害者出现之前，\x01",
            "赶快将事件解决啊。\x02",
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

    # Function_75_F020 end

    def Function_76_F9BB(): pass

    label("Function_76_F9BB")


    #C0708
    ChrTalk(
        0x101,
        (
            "#12P#0001F明白了。\x01",
            "事态也很严重，我们\x01",
            "立刻接受任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x15,
        (
            "#5P太好了……\x01",
            "这样一来，就能安心了！\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x1A,
        "#11P嗯，拜托你们了啊！\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x104,
        (
            "#12P#0304F哈，一切都交给我们，\x01",
            "尽管放心好啦。\x02\x03",

            "#0301F……那么，罗伊德，\x01",
            "有什么调查方法吗？\x01",
            "现在可是没有任何线索啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x101,
        (
            "#12P#0003F是啊……\x01",
            "情报实在太少了，\x01",
            "也没办法进行推理。\x02\x03",

            "#0001F不好意思，可以给我们\x01",
            "遭窃店铺的名单吗？\x02\x03",

            "我们想去进行一下查访，\x01",
            "借此收集情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x1A,
        (
            "#11P原来如此，店名\x01",
            "都已经记录在这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x1A,
        (
            "#11P遭窃的店铺有……\x01",
            "……我要开始读了，可以吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x102,
        "#12P#0100F嗯，当然可以。\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x1A,
        (
            "#11P中央广场的『纳德尔汉堡』、\x01",
            "行政区的『库罗玛果汁店』……\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x1A,
        (
            "#11P欢乐街的『帕雷特比萨』，\x01",
            "以及这个港湾公园中的\x01",
            "『米斯拉雪糕』。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x102,
        (
            "#12P#0103F（认真记录……）\x01",
            "……一共有四家店铺，\x01",
            "而且好像分散在不同街区呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x103,
        (
            "#6P#0200F既然有四家店铺，\x01",
            "依次问一遍，至少也能发现\x01",
            "一条线索吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x101,
        "#12P#0001F嗯，总之，现在就去查访一遍吧。\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x101,
        (
            "#12P#0000F各位就请暂时留在\x01",
            "这里等待好吗？\x01",
            "全部问完之后，我们会回来报告的。\x02\x03",

            "#0005F……对了，我把自己的\x01",
            "联络方式留下，\x01",
            "如果发生什么情况还请联络我。\x02\x03",

            "#0001F毕竟不知道下一起案件\x01",
            "将会在什么时候发生。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x1A,
        "#11P明白了，我们就在这里等待。\x02",
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x15,
        (
            "#5P各位，一切都\x01",
            "拜托你们啦！\x02",
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
            "任务【调查盗窃事件的委托】\x07\x00",
            "开始！\x02",
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

    # Function_76_F9BB end

    def Function_77_FF0E(): pass

    label("Function_77_FF0E")

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
            "#11P噢噢，回来了吗……\x01",
            "询问得怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯，我想应该\x01",
            "是发现了不少线索呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x102,
        (
            "#12P#0100F先来整理\x01",
            "一下情报吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x103,
        "#6P#0200F是啊。\x02",
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x104,
        "#12P#0300F罗伊德，还是老规矩，接下来的推理就拜托你啦。\x02",
    )

    CloseMessageWindow()

    def lambda_100AE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_100AE)

    def lambda_100BB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_100BB)

    def lambda_100C8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_100C8)

    def lambda_100D5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_100D5)
    Sleep(300)

    #C0730
    ChrTalk(
        0x101,
        (
            "#11P#0001F明白，\x01",
            "那么，开始吧。\x02",
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
            "#11P#0003F咳……首先，我们来整理\x01",
            "一下在查访中收集到的情报吧。\x02\x03",

            "#0001F根据店员们的说法，\x01",
            "在四家店铺作案时，\x01",
            "犯人所用的手法是……\x02",
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
            "【用武器威胁，直接强抢】\x01",          # 0
            "【扮装成客人进行盗窃】\x01",            # 1
            "【在店员接待客人时趁机盗窃】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103C2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0732
    ChrTalk(
        0x104,
        (
            "#12P#0301F每家店都是在店员专心\x01",
            "接待客人的时候被\x01",
            "犯人得手了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x103,
        (
            "#6P#0203F趁店员无法分神警戒时作案……\x02\x03",

            "#0200F这样一来，确实是不会\x01",
            "被注意到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x101,
        (
            "#11P#0001F嗯，不管再怎么提醒他们小心注意，\x01",
            "也都不会有什么效果吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104F3")

    label("loc_103C2")


    #C0735
    ChrTalk(
        0x104,
        (
            "#12P#0305F不对，好像\x01",
            "不是那样的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x103,
        (
            "#6P#0200F根据查访得来的情报，\x01",
            "所有店铺应该都是在店员\x01",
            "接待客人时遭到盗窃的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0737
    ChrTalk(
        0x101,
        (
            "#11P#0005F啊……对了，是那样的啊。\x02\x03",

            "#0003F趁店员无法分神警戒时，\x01",
            "趁机在其身后实施盗窃。\x02\x03",

            "#0001F这样一来，不管再怎么提醒他们小心注意，\x01",
            "也都不会有什么效果吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104F3")


    #C0738
    ChrTalk(
        0x1A,
        (
            "#5P嗯，从这些情况来看，\x01",
            "真是个卑劣的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x104,
        (
            "#12P#0303F而且他都已经连续\x01",
            "得手了四次啊。\x02\x03",

            "#0301F犯人眼下恐怕正躲在什么地方\x01",
            "嘲笑着我们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x101,
        (
            "#11P#0001F是啊……像这类犯罪行为\x01",
            "包括多种类型，\x01",
            "不过……\x02\x03",

            "这次的案件好像有\x01",
            "一定的倾向性呢。\x02\x03",

            "#0003F是啊，以动机来\x01",
            "考虑的话……\x02",
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
            "【整人报复】\x01",      # 0
            "【急需米拉】\x01",      # 1
            "【半是好玩】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10717")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0741
    ChrTalk(
        0x102,
        (
            "#6P#0101F有一半是为了好玩……\x01",
            "确实有那种感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        (
            "#6P#0200F在短时间内连续作案，\x01",
            "看起来并不像是因为缺钱而盗窃。\x02\x03",

            "而是为了享受盗窃\x01",
            "所带来的刺激吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10987")

    label("loc_10717")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10870")

    #C0743
    ChrTalk(
        0x102,
        (
            "#6P#0105F整人报复……吗，\x01",
            "不过我感觉犯人是为了乐趣而作案呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x103,
        (
            "#6P#0200F但是，如果是为了整人报复，\x01",
            "应该会选择特定的店铺，反复下手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        (
            "#11P#0006F也、也是啊……\x01",
            "但犯人好像并没有很明确的目标呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x104,
        (
            "#12P#0303F在短时间内连续作案，\x01",
            "看起来也并不像是因为缺钱而盗窃啊。\x02\x03",

            "#0301F恐怕他作案是为了享受盗窃\x01",
            "所带来的刺激吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10987")

    label("loc_10870")


    #C0747
    ChrTalk(
        0x102,
        (
            "#6P#0105F急需米拉……\x01",
            "好像并没有这样的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x104,
        (
            "#12P#0301F是啊。\x01",
            "在短时间内连续作案，\x01",
            "看起来倒像是为了乐趣而进行盗窃。\x02\x03",

            "#0303F如果真需要很多钱，\x01",
            "恐怕也就不会以\x01",
            "这些露天店为目标了。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#11P#0005F也、也是啊……\x02\x03",

            "#0003F不如说他作案的目的，是为了享受\x01",
            "盗窃所带来的刺激吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10987")


    #C0750
    ChrTalk(
        0x15,
        (
            "#5P竟、竟然因为那种理由\x01",
            "而不断作案……！\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x15,
        "#5P犯人究竟是……！？\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x101,
        (
            "#11P#0003F这个嘛，关于犯人的特征，\x01",
            "也有了一些基本印象了。\x02\x03",

            "#0001F犯人是……\x02",
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
            "【惯偷】\x01",                # 0
            "【两个青年的组合】\x01",      # 1
            "【大型盗窃团伙】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D71")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10AA7")
    OP_2C(0x20, 0x2)

    label("loc_10AA7")


    #C0753
    ChrTalk(
        0x101,
        "#11P#0001F我想应该是两个青年的组合吧。\x02",
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
            "#12P#0305F犯人并没有被\x01",
            "目击到啊……\x01",
            "你是怎么知道的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x101,
        (
            "#11P#0000F仔细回想一下。\x01",
            "每家店都是店员在接待客人时被得手的……\x02\x03",

            "而他们所接待的客人\x01",
            "是不是都很相似？\x02\x03",

            "#0003F出现在行政区和港湾公园\x01",
            "的是感觉轻浮的青年……\x02\x03",

            "出现在中央广场和欢乐街\x01",
            "的是喜欢唠叨的青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x103,
        (
            "#6P#0203F只有在店员接待这两种\x01",
            "客人时，\x01",
            "案件才会发生……\x02\x03",

            "#0200F如果说是偶然，\x01",
            "未免也太巧了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x101,
        (
            "#11P#0001F嗯，所以我认为这很有可能\x01",
            "是两人联手进行作案。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x102,
        (
            "#6P#0105F也就是说……\x02\x03",

            "其中一个人假扮客人，吸引店主的注意力，\x01",
            "另一个人趁机出手盗窃……？\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x104,
        (
            "#12P#0303F原来如此，两个人\x01",
            "也会相互交换角色呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110EF")

    label("loc_10D71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DCA")

    #C0760
    ChrTalk(
        0x101,
        (
            "#11P#0001F大概是……惯偷吧。\x02\x03",

            "手段这么利落，\x01",
            "恐怕不是外行所为。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E17")

    label("loc_10DCA")


    #C0761
    ChrTalk(
        0x101,
        (
            "#11P#0001F或许是……大型盗窃团伙吧。\x02\x03",

            "手段这么利落，\x01",
            "恐怕不是外行所为。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E17")


    #C0762
    ChrTalk(
        0x102,
        (
            "#6P#0103F也有道理，不过……\x02\x03",

            "#0100F换个角度考虑的话，\x01",
            "如果是在店员接待客人时趁机盗窃，\x01",
            "即使是业余人士恐怕也很容易得手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x101,
        "#11P#0005F说、说得也是啊。\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x103,
        (
            "#6P#0203F…………………………\x01",
            "有件事我很在意……\x02\x03",

            "#0200F好像每家店都是在\x01",
            "店主接待客人时遭窃的吧？\x02\x03",

            "而且，他们所接待的客人……\x01",
            "不觉得都是\x01",
            "很相似的人物吗？\x02\x03",

            "#0203F出现在行政区和港湾公园\x01",
            "的是感觉轻浮的青年……\x02\x03",

            "出现在中央广场和欢乐街\x01",
            "的是喜欢唠叨的青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#12P#0305F这么一说，确实如此呢……\x02\x03",

            "#0301F每家店的店主好像都\x01",
            "只提到了这两种客人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x101,
        (
            "#11P#0001F只有在店主接待这两类客人时，\x01",
            "案件才会发生……\x01",
            "如果说是偶然，那未免也太巧了。\x02\x03",

            "#0003F莫非是两人联手作案吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x102,
        (
            "#6P#0105F也就是说……\x02\x03",

            "#0101F其中一个人假扮客人，\x01",
            "吸引店主的注意力，\x01",
            "另一个人趁机出手盗窃？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110EF")


    #C0768
    ChrTalk(
        0x1A,
        (
            "#5P嗯嗯嗯……\x01",
            "如果真是那样，\x01",
            "就绝对不能再对他们放任下去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x15,
        "#5P是啊，完全赞同……！\x02",
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x15,
        (
            "#5P呼，可是，说到两个青年的组合，\x01",
            "市内实在是太多了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x15,
        (
            "#5P真是没办法啊……\x01",
            "也只能提醒一下开店的各位，\x01",
            "让他们自己小心了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x101,
        (
            "#11P#0003F不，既然都已经知道这些了，\x01",
            "我想，可以采取更好的办法。\x02\x03",

            "#0001F那么，各位，你们觉得\x01",
            "他们的下一个目标将会是哪里？\x02",
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
            "#6P#0101F这个嘛……已经遭窃的店\x01",
            "应该可以排除在外了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x104,
        (
            "#12P#0300F是啊，再怎么说，\x01",
            "连偷两次肯定也会暴露的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x103,
        (
            "#6P#0200F也就是说，有可能会成为\x01",
            "下一个目标的，只有那些尚未\x01",
            "遭窃的店铺了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1140F")
    OP_2C(0x20, 0x1)

    #C0776
    ChrTalk(
        0x101,
        (
            "#11P#0003F（幸好我们也去那些\x01",
            "  没有遭窃的店铺查访了一下。）\x02\x03",

            "#0001F（有可能会成为下一个目标的店应该就是……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11499")

    label("loc_1140F")


    #C0777
    ChrTalk(
        0x101,
        (
            "#11P#0003F（要是我们也去那些没有\x01",
            "  受害的店铺进行查访就好了……）\x02\x03",

            "#0001F（算了，按照现状分析，\x01",
            "  最有可能成为下一个目标的店是……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11499")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【中央广场的甜品店】\x01",      # 0
            "【行政区的蛋包饭店】\x01",      # 1
            "【欢乐街的冰激凌车】\x01",      # 2
            "【港湾公园的汤面摊】\x01",      # 3
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1153B"),
        (1, "loc_1191E"),
        (2, "loc_11B19"),
        (3, "loc_11CE3"),
        (SWITCH_DEFAULT, "loc_11E60"),
    )


    label("loc_1153B")

    OP_2C(0x20, 0x2)

    #C0778
    ChrTalk(
        0x1A,
        "#5P中央广场的甜品店吗？\x02",
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x101,
        (
            "#11P#0001F嗯，这是有理由的。\x02\x03",

            "#0003F因为今天有游行活动，\x01",
            "所以行政区一带会有很多警官……\x02\x03",

            "相比之下，对犯人来说，欢乐街、\x01",
            "中央广场和港湾公园恐怕是更好的选择。\x02\x03",

            "#0001F而且……考虑到作案之后\x01",
            "『逃脱的难易度』，\x01",
            "最容易被盯上的地方果然还是中央广场。\x02",
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
        "#12P#0305F逃脱的难易度……？\x02",
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x101,
        (
            "#11P#0001F如今已有好几家店受害，\x01",
            "店主们的警戒应该都会大有提高。\x02\x03",

            "#0003F不管盗窃技术再怎么高明，\x01",
            "被当场发现的可能性\x01",
            "恐怕都不小……\x02\x03",

            "#0000F这样一来，我想犯人肯定会选择\x01",
            "那种即使被发现，也能顺利脱身的店铺下手。\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x102,
        (
            "#6P#0105F这么说的话……\x02\x03",

            "#0100F刚刚遭到盗窃的\x01",
            "汉堡店似乎也位于\x01",
            "街区的路口呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x103,
        (
            "#6P#0200F中央广场的甜品店处在\x01",
            "离后巷和行政区都很近的位置。\x02\x03",

            "从逃跑的难易程度来分析，那里确实是\x01",
            "最有可能成为目标的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x104,
        (
            "#12P#0303F是啊，可能性好像很高呢……\x02\x03",

            "#0300F……好，那我们\x01",
            "就去那里赌一次看看吧！\x02",
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
    Jump("loc_11E60")

    label("loc_1191E")


    #C0785
    ChrTalk(
        0x1A,
        "#5P行政区的蛋包饭店吗？\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x101,
        (
            "#11P#0003F嗯，我想应该是吧……\x02\x03",

            "因为今天有游行活动，\x01",
            "所以行政区那边是\x01",
            "相当热闹的。\x02\x03",

            "#0001F在这种人山人海的环境下，\x01",
            "犯人也许会趁乱作案……\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x102,
        (
            "#6P#0101F不过，由于要对游行进行警备，\x01",
            "那里应该会聚集很多警官吧。\x02\x03",

            "#0103F再怎么吸引店主的注意力，\x01",
            "在这种环境下进行盗窃，\x01",
            "我想也是相当危险的……\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x101,
        (
            "#11P#0006F唔……\x01",
            "脑子好像有点乱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x104,
        (
            "#12P#0303F算啦，与其在人群中漫无目的地寻找，\x01",
            "还不如选定那里赌一把呢，对吧？\x02\x03",

            "#0300F好，就赌赌看吧！\x02",
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
    Jump("loc_11E60")

    label("loc_11B19")


    #C0790
    ChrTalk(
        0x1A,
        "#5P欢乐街的冰激凌车？\x02",
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x101,
        (
            "#11P#0003F嗯，我想应该是吧……\x02\x03",

            "欢乐街的冰激凌车\x01",
            "就在彩虹剧团的门口。\x02\x03",

            "#0001F剧团公演前后，人流量都相当可观，\x01",
            "犯人可能会趁机作案。\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x103,
        (
            "#6P#0205F可是，一般会采取这种手法的，\x01",
            "不都是单独行窃的犯人吗……？\x02\x03",

            "#0200F这就和本次的案情不太相符了。\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x101,
        (
            "#11P#0006F唔……\x01",
            "脑子好像有点乱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x104,
        (
            "#12P#0303F算啦，与其在人群中漫无目的地寻找，\x01",
            "还不如选定那里赌一把呢，对吧？\x02\x03",

            "#0300F好，就赌赌看吧！\x02",
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
    Jump("loc_11E60")

    label("loc_11CE3")


    #C0795
    ChrTalk(
        0x1A,
        "#5P港湾公园的汤面摊？\x02",
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x101,
        (
            "#11P#0003F嗯，我想应该是吧……\x02\x03",

            "#0001F虽然那是距离工商协会\x01",
            "接待帐篷最近的店……\x01",
            "但犯人有可能出其不意对那里下手。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x102,
        (
            "#6P#0103F那样的话，犯人还真\x01",
            "不是一般地喜欢刺激呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x101,
        (
            "#11P#0006F呜……\x01",
            "脑子好像有点乱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x104,
        (
            "#12P#0303F算啦，与其在人群中漫无目的地寻找，\x01",
            "还不如选定那里赌一把呢，对吧？\x02\x03",

            "#0300F好，就赌赌看吧！\x02",
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
    Jump("loc_11E60")

    label("loc_11E60")

    Return()

    # Function_77_FF0E end

    def Function_78_11E61(): pass

    label("Function_78_11E61")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FDE")
    ClearChrFlags(0x52, 0x80)
    ClearChrBattleFlags(0x52, 0x8000)

    label("loc_11FDE")

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
            "#11P不过只是无能的警察而已，\x01",
            "居然还想对我们指手划脚！\x02",
        )
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x4F,
        (
            "#5P竟敢看不起我们\x01",
            "『暗黑帝王』吗！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12136")

    #C0802
    ChrTalk(
        0x52,
        "#11P#1207F嗷噜噜噜……！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x4E, 0x0)
    EndChrThread(0x4F, 0x0)

    def lambda_120D0():
        TurnDirection(0xFE, 0x52, 500)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_120D0)

    def lambda_120DD():
        TurnDirection(0xFE, 0x52, 500)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_120DD)
    Sleep(200)
    OP_63(0x4E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x4F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0803
    ChrTalk(
        0x4E,
        (
            "#11P哇哇哇哇！\x01",
            "十、十分抱歉～！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12136")


    #C0804
    ChrTalk(
        0x15,
        (
            "#5P赃款已经顺利追回了……\x01",
            "但总觉得这两个家伙十分虚张声势呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x104,
        (
            "#12P#0306F是啊。\x02\x03",

            "#0300F要是他们和旧城区那些不良少年们碰上了，\x01",
            "估计只要一拳就会被吓得腿软吧。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x4E, 0x0)
    EndChrThread(0x4F, 0x0)
    OP_63(0x4E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x4F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1221A():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_1221A)

    def lambda_12237():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_12237)
    Sleep(1200)
    OP_63(0x4E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x4F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)

    #C0806
    ChrTalk(
        0x101,
        "#6P#0005F哎，怎么突然就一言不发了。\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x102,
        (
            "#12P#0105F莫非……\x01",
            "你们真的被那些不良少年\x01",
            "教训过吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_122E1():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_122E1)

    def lambda_122EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_122EE)
    Sleep(200)

    #C0808
    ChrTalk(
        0x4E,
        (
            "#11P谁、谁、谁、\x01",
            "谁会害怕那种家伙啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x4F,
        (
            "#5P不、不要再\x01",
            "小看我们了啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x103,
        (
            "#6P#0200F好像戳到痛处了呢。\x02\x03",

            "……原来如此，\x01",
            "因为被教训了，所以满怀愤懑，\x01",
            "为了发泄情绪才不断作案。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x1A,
        "#11P……是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x1A,
        (
            "#11P所以你们才给那么多的人\x01",
            "添了那么大的麻烦……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12403():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_12403)

    def lambda_12410():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_12410)
    Sleep(300)
    SetCameraDistance(19210, 1600)
    OP_95(0x1A, -16880, 0, -10300, 1000, 0x0)

    def lambda_1243D():
        OP_93(0xFE, 0xF5, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1243D)
    OP_93(0x1A, 0xF5, 0x190)
    Sleep(300)

    #C0813
    ChrTalk(
        0x1A,
        (
            "#11P如此罪过……\x01",
            "你们要怎么偿还呢？\x02",
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
            "#12P呜呜……\x01",
            "（怎么回事，这个老爷爷……）\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x4F,
        (
            "#6P（咽口水）……\x01",
            "（眼神好可怕啊……）\x02",
        )
    )

    CloseMessageWindow()

    #N0816
    NpcTalk(
        0x50,
        "声音",
        (
            "#4P……找到了、找到了，\x01",
            "你们就是特别任务支援科吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-19920, 2500, -11390, 2500)
    MoveCamera(53, 31, 0, 2500)
    OP_6E(420, 2500)
    SetCameraDistance(20320, 2500)

    def lambda_1256B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1256B)

    def lambda_12578():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_12578)

    def lambda_12585():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_12585)

    def lambda_12592():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12592)

    def lambda_1259F():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1259F)

    def lambda_125AC():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_125AC)

    def lambda_125B9():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_125B9)

    def lambda_125C6():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_125C6)

    def lambda_125D3():
        OP_95(0xFE, -19300, 0, -7440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_125D3)

    def lambda_125ED():
        OP_95(0xFE, -20380, 0, -7260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_125ED)
    Sleep(2500)

    #C0817
    ChrTalk(
        0x50,
        "#11P抱歉，来晚了。\x02",
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x51,
        (
            "#5P我们是来接手\x01",
            "这些盗窃犯的。\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x101,
        (
            "#12P#0001F抱歉啊，在这么忙的时候\x01",
            "还把你们叫出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x50,
        "#11P啊，没关系的。\x02",
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x50,
        "#11P……就是那边的两个人吗？\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x101,
        (
            "#12P#0001F嗯，请把他们带回\x01",
            "总部吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x51,
        "#5P好的，交给我们吧。\x02",
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
        "#11P好啦，赶快走！\x02",
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x4E,
        "#11P哇，别推我啊！\x02",
    )

    CloseMessageWindow()

    def lambda_127A6():

        label("loc_127A6")

        TurnDirection(0xFE, 0x51, 400)
        Yield()
        Jump("loc_127A6")

    QueueWorkItem2(0x1A, 1, lambda_127A6)

    def lambda_127B8():

        label("loc_127B8")

        TurnDirection(0xFE, 0x50, 400)
        Yield()
        Jump("loc_127B8")

    QueueWorkItem2(0x15, 1, lambda_127B8)

    def lambda_127CA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_127CA)

    def lambda_127D7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_127D7)

    def lambda_127E4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_127E4)

    def lambda_127F1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_127F1)
    Sleep(100)

    def lambda_12801():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_12801)

    def lambda_12816():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_12816)

    def lambda_1282B():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_1282B)

    def lambda_12840():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_12840)
    Sleep(6000)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x15, 0x1)
    OP_68(-20430, 2500, -11880, 2000)
    MoveCamera(69, 29, 0, 2000)
    OP_6E(420, 2000)
    SetCameraDistance(20320, 2000)

    def lambda_1288E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1288E)

    def lambda_1289B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1289B)

    def lambda_128A8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_128A8)

    def lambda_128B5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_128B5)
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
            "#5P呼……总之，\x01",
            "一块石头落了地啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0x102,
        (
            "#12P#0100F他们好像是外国人……\x01",
            "所以在拘留所里关个三天后\x01",
            "就不会再受到更多追究了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x104,
        (
            "#12P#0306F克洛斯贝尔对于这方面的规定\x01",
            "实在是太宽松了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x1A,
        (
            "#11P呵呵，难得的纪念庆典，\x01",
            "他们却只能对着拘留所的墙壁度过了。\x01",
            "这就已经足够啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x1A,
        (
            "#11P而且……我也成功\x01",
            "把他们给吓到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x103,
        (
            "#6P#0205F说起来，会长先生，\x01",
            "您那时的威压感真的很强烈呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x1A,
        (
            "#11P呵呵，毕竟我以前也\x01",
            "是个经历过百般磨练的商人啊。\x01",
            "对付那样的货色，还不是手到擒来。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x101,
        "#6P#0000F哈哈，是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_12CAC")

    #C0834
    ChrTalk(
        0x1A,
        (
            "#11P不过，说老实话，即使在我看来，\x01",
            "他们的作案手段也真是很高明呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0x1A,
        "#11P这次的事件，实在是多谢你们了。\x02",
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x15,
        (
            "#5P是呀，\x01",
            "真是多亏你们帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x15,
        (
            "#5P我代表工商协会，\x01",
            "衷心向你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x101,
        (
            "#6P#0000F啊，不不，这没什么。\x01",
            "能将事情顺利解决\x01",
            "就是最好不过了。\x02\x03",

            "哈哈……如果以后还有什么困难，\x01",
            "也请与我们商量。\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x1A,
        (
            "#11P嗯，一定会去拜托你们的，\x01",
            "到时还请多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x102,
        (
            "#12P#0100F嗯，乐意效劳，\x01",
            "今后也要请您\x01",
            "多多关照呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xF)
    OP_29(0x20, 0x1, 0x10)
    Jump("loc_12FD7")

    label("loc_12CAC")


    #C0841
    ChrTalk(
        0x101,
        (
            "#6P#0006F对不起，\x01",
            "这次的推理失败了，\x02\x03",

            "差一点就让他们逃脱。\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x102,
        (
            "#12P#0106F真是很抱歉，\x01",
            "辜负了您的信赖。\x02",
        )
    )

    CloseMessageWindow()

    #C0843
    ChrTalk(
        0x1A,
        (
            "#11P哪里哪里，事情不是也得到顺利解决了嘛。\x01",
            "这样就很好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x87, 0x190)

    #C0844
    ChrTalk(
        0x1A,
        (
            "#11P另外，你们那条优秀的警犬……\x01",
            "是叫蔡特吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x1A,
        (
            "#11P事先考虑到了意外情况，\x01",
            "以防万一而派它出动，\x01",
            "这也是你们的功劳啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x101,
        (
            "#6P#0012F哈、哈哈哈……\x01",
            "那、那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x52,
        "#11P#1203F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x52, 400)
    Sleep(300)

    #C0848
    ChrTalk(
        0x103,
        "#6P#0203F它说，你们还差得远呢。\x02",
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
        "#12P#0306F实在是很抱歉。\x02",
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
            "#5P哪里的话，这次全靠你们的帮忙。\x01",
            "我代表工商协会，衷心向你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0x1A,
        (
            "#11P嗯，如果以后又发生什么事情，\x01",
            "说不定还要请你们帮忙呢。\x01",
            "到时就请多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0x102,
        (
            "#12P#0100F是，今后也请您\x01",
            "多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x14)
    OP_29(0x20, 0x1, 0x15)

    label("loc_12FD7")

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
            "任务【调查盗窃事件的委托】\x07\x00",
            "完成！\x02",
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

    # Function_78_11E61 end

    def Function_79_130D9(): pass

    label("Function_79_130D9")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_13119"),
        (1, "loc_13125"),
        (2, "loc_13131"),
        (3, "loc_1313D"),
        (4, "loc_13149"),
        (5, "loc_13155"),
        (6, "loc_13161"),
        (SWITCH_DEFAULT, "loc_1316D"),
    )


    label("loc_13119")

    OP_A0(0xFE, 2450, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_13125")

    OP_A0(0xFE, 2550, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_13131")

    OP_A0(0xFE, 2600, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_1313D")

    OP_A0(0xFE, 2400, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_13149")

    OP_A0(0xFE, 2650, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_13155")

    OP_A0(0xFE, 2350, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_13161")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_1316D")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_13179")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_131DC")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_131AC"),
        (1, "loc_131B8"),
        (2, "loc_131C4"),
        (SWITCH_DEFAULT, "loc_131D0"),
    )


    label("loc_131AC")

    OP_93(0xFE, 0x2D, 0x1F4)
    Jump("loc_131D0")

    label("loc_131B8")

    OP_93(0xFE, 0x10E, 0x1F4)
    Jump("loc_131D0")

    label("loc_131C4")

    OP_93(0xFE, 0x87, 0x1F4)
    Jump("loc_131D0")

    label("loc_131D0")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_13179")

    label("loc_131DC")

    Return()

    # Function_79_130D9 end

    def Function_80_131DD(): pass

    label("Function_80_131DD")

    OP_95(0xFE, -16940, 0, -10040, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_80_131DD end

    def Function_81_131F9(): pass

    label("Function_81_131F9")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, -17600, 0, -9230, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_81_131F9 end

    def Function_82_1321C(): pass

    label("Function_82_1321C")

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
            "#12P#0309F『米斯拉的雪糕车』……\x01",
            "哇～店主真是位美人姐姐啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x101,
        (
            "#6P#0006F兰迪，冷静一点。\x01",
            "这里应该是遭受过盗窃的店……\x02\x03",

            "#0001F现在要以询问案情为重。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x102,
        (
            "#0100F不好意思，\x01",
            "我们是克洛斯贝尔警察局的人……\x01",
            "能问您几句话吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0857
    ChrTalk(
        0x10,
        "#5P啊……是关于盗窃案的吧？\x02",
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x10,
        (
            "#5P没错，我的店也遭窃了呢，\x01",
            "就在我接待客人的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0x103,
        "#12P#0200F接待客人时遭到盗窃的吗……\x02",
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0x10,
        (
            "#5P那时的客人是个轻浮的男子，\x01",
            "看起来好像是外国人，\x01",
            "当时正在和我搭讪。\x02",
        )
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x10,
        (
            "#5P他一直纠缠不休，\x01",
            "就在我烦得准备踩他一脚的时候，\x01",
            "感觉到后面好像有人。\x02",
        )
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x10,
        (
            "#5P不过，那时已经晚了。\x01",
            "当我回过头的时候，\x01",
            "放钱的盒子已经空了。\x02",
        )
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x101,
        (
            "#6P#0001F更详细的情况，\x01",
            "您好像也不清楚了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0x10,
        (
            "#5P是啊，\x01",
            "我也真是太大意了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1370D")
    OP_68(13510, 2510, 9070, 1200)
    MoveCamera(45, 24, 0, 1200)

    def lambda_13596():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13596)

    def lambda_135A3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_135A3)

    def lambda_135B0():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_135B0)

    def lambda_135BD():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_135BD)
    Sleep(1200)

    #C0865
    ChrTalk(
        0x101,
        "#6P#0003F询问工作就到此为止吧……\x02",
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x104,
        (
            "#12P#0300F是啊，差不多也该回去\x01",
            "整理一下情报了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13707")

    #C0867
    ChrTalk(
        0x102,
        (
            "#0100F工商协会那边也没有和我们联络，\x01",
            "看样子，似乎还没有\x01",
            "出现新的案情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0x103,
        (
            "#11P#0203F是啊。\x02\x03",

            "#0200F……谨慎起见，\x01",
            "在回去的路上，顺便再留意\x01",
            "一下别的露天店铺吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13707")

    OP_29(0x20, 0x1, 0xD)

    label("loc_1370D")

    OP_5A()
    SetChrPos(0x0, 14780, 10, 10480, 0)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_82_1321C end

    def Function_83_13730(): pass

    label("Function_83_13730")

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
            "罗伊德等人前往目标街区，\x01",
            "随后埋伏了下来。\x07\x00\x02",
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

            "看来不是这位客人呢……\x02",
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
        "#0306F还不来啊……\x02",
    )

    CloseMessageWindow()

    #A0872
    AnonymousTalk(
        0x103,
        (
            "#0200F都已经在这里\x01",
            "埋伏了一个多小时了……\x02",
        )
    )

    CloseMessageWindow()

    #A0873
    AnonymousTalk(
        0x101,
        (
            "#0001F真奇怪啊，都这么久了，\x01",
            "也该来了吧……\x02",
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

    def lambda_13A4B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13A4B)

    def lambda_13A58():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13A58)

    def lambda_13A65():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13A65)
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
            "#11P#0003F您好，我是罗伊德·班宁斯──\x02\x03",

            "#0005F哎，盗窃犯出现了……！？\x02",
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
            "#11P#0001F好、好，是中央广场对吧。\x02\x03",

            "明白了，我们马上就过去！\x02",
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
            "#11P#0006F……抱歉了，大家。\x01",
            "看来是我计算错误了。\x02",
        )
    )

    CloseMessageWindow()

    #C0877
    ChrTalk(
        0x102,
        "#5P#0101F别说这些了，赶快出发吧，罗伊德！\x02",
    )

    CloseMessageWindow()

    #C0878
    ChrTalk(
        0x101,
        (
            "#11P#0001F也、也是啊。\x01",
            "当务之急是赶往现场！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13C44():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13C44)

    def lambda_13C51():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13C51)

    def lambda_13C5E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_13C5E)

    def lambda_13C6B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13C6B)
    Sleep(300)

    def lambda_13C7B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13C7B)

    def lambda_13C90():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13C90)

    def lambda_13CA5():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_13CA5)

    def lambda_13CBA():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13CBA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_13730 end

    def Function_84_13CE7(): pass

    label("Function_84_13CE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D0C")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_84_13CE7")

    label("loc_13D0C")

    Return()

    # Function_84_13CE7 end

    def Function_85_13D0D(): pass

    label("Function_85_13D0D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0879
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　『羽扇河·第一灯塔』\x01\x01",
            "无关人员禁止入内。\x01",
            "　　　　　　～克洛斯贝尔市～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_85_13D0D end

    def Function_86_13D8D(): pass

    label("Function_86_13D8D")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0880
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁，\x01",
            "并挂着一块牌子。\x07\x00\x02",
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
            "『黑月贸易公司·克洛斯贝尔分公司』\x01",
            "※若有要事，敬请敲门。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_86_13D8D end

    SaveToFile()

Try(main)
