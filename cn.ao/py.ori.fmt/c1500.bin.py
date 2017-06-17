from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1500.bin",                # FileName
        "c1500",                    # MapName
        "c1500",                    # Location
        0x00AA,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\n',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 170, 0, 11, 0, 12],
    )

    BuildStringList((
        "c1500",                  # 0
        "坎宁巡警",               # 1
        "马丁巡警",               # 2
        "塔基库",                 # 3
        "警官",                   # 4
        "警官",                   # 5
        "警官",                   # 6
        "警官",                   # 7
        "市政府职员",             # 8
        "市政府职员",             # 9
        "米蕾优三尉",             # 10
        "市民",                   # 11
        "女孩",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "游客",                   # 17
        "游客",                   # 18
        "金德尔",                 # 19
        "隆",                     # 20
        "亨利",                   # 21
        "小桃",                   # 22
        "秦",                     # 23
        "记者诺蒂亚",             # 24
        "尼尔森",                 # 25
        "道格拉斯副司令",         # 26
        "麦克道尔议长",           # 27
        "赛尔盖科长",             # 28
        "支援科损坏车辆",         # 29
        "新型装甲车",             # 30
        "新型装甲车",             # 31
        "奥斯本宰相",             # 32
        "雷克特书记官",           # 33
        "奥利维特皇子",           # 34
        "穆拉少校",               # 35
        "科洛蒂娅公主",           # 36
        "尤莉亚准校",             # 37
        "阿尔伯特大公",           # 38
        "洛克史密斯总统",         # 39
        "雾香辅佐官",             # 40
        "迪塔市长",               # 41
        "玛丽亚贝尔",             # 42
        "游击士斯克特",           # 43
        "游击士温蔡尔",           # 44
        "游击士林",               # 45
        "游击士艾欧莉娅",         # 46
        "亚里欧斯国防长官",       # 47
        "达德利搜查官",           # 48
        "雷蒙德搜查官",           # 49
        "艾玛搜查官",             # 50
        "乔里基科长",             # 51
        "凯特巡警",               # 52
        "弗兰茨巡警",             # 53
        "罗伊德等人的声音",       # 54
        "事件用魔兽",             # 55
        "事件用魔兽",             # 56
        "事件用魔兽",             # 57
        "事件用魔兽",             # 58
        "事件用魔兽",             # 59
        "事件用魔兽",             # 60
        "事件用魔兽",             # 61
        "事件用魔兽",             # 62
        "事件用魔兽",             # 63
        "索妮亚司令",             # 64
        "警官",                   # 65
        "警官",                   # 66
        "警官",                   # 67
        "警官",                   # 68
        "警官",                   # 69
        "警官",                   # 70
        "警官",                   # 71
        "警官",                   # 72
        "警官",                   # 73
        "警官",                   # 74
        "警备队员",               # 75
        "警备队员",               # 76
        "警备队员",               # 77
        "警备队员",               # 78
        "警备队员",               # 79
        "警备队员",               # 80
        "警备队员",               # 81
        "警备队员",               # 82
        "秘书",                   # 83
        "总管",                   # 84
        "帝国军士官",             # 85
        "帝国军士官",             # 86
        "共和国军士官",           # 87
        "共和国军士官",           # 88
        "亲卫队",                 # 89
        "亲卫队",                 # 90
        "士兵卡塔",               # 91
        "国防军士兵·男",         # 92
        "国防军士兵·男",         # 93
        "国防军士兵·男",         # 94
        "国防军士兵·男",         # 95
        "国防军士兵·女",         # 96
        "国防军士兵·女",         # 97
        "国防军士兵·女",         # 98
        "国防军士官",             # 99
        "格蕾丝",                 # 100
        "雷因兹",                 # 101
        "记者",                   # 102
        "记者",                   # 103
        "记者",                   # 104
        "记者",                   # 105
        "车辆",                   # 106
        "车辆",                   # 107
        "车辆",                   # 108
        "车辆",                   # 109
        "新型装甲车（Ａ）",       # 110
        "新型装甲车（Ｂ）",       # 111
        "偃月轮",                 # 112
        "偃月轮",                 # 113
        "SE控制",                 # 114
        "中央广场",               # 115
        "西街",                   # 116
        "行政区",                 # 117
        "住宅街",                 # 118
        "欢乐街",                 # 119
        "东街",                   # 120
        "旧城区",                 # 121
        "港湾区",                 # 122
        "ＩＢＣ",                 # 123
        "站前街道",               # 124
        "后巷",                   # 125
        "乌尔斯拉间道",           # 126
        "东克洛斯贝尔街道",       # 127
        "西克洛斯贝尔街道",       # 128
        "玛因兹山道",             # 129
        "兰花塔",                 # 130
    ))

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch27700.itc",                   # 02
        "chr/ch27800.itc",                   # 03
        "chr/ch32600.itc",                   # 04
        "chr/ch20302.itc",                   # 05
        "chr/ch22300.itc",                   # 06
        "chr/ch24400.itc",                   # 07
        "chr/ch44200.itc",                   # 08
        "chr/ch34300.itc",                   # 09
        "chr/ch44200.itc",                   # 0A
        "chr/ch20600.itc",                   # 0B
        "chr/ch22200.itc",                   # 0C
        "chr/ch20700.itc",                   # 0D
        "chr/ch45000.itc",                   # 0E
        "chr/ch47900.itc",                   # 0F
        "chr/ch45102.itc",                   # 10
        "chr/ch49200.itc",                   # 11
        "chr/ch49000.itc",                   # 12
        "chr/ch05800.itc",                   # 13
        "chr/ch02500.itc",                   # 14
        "chr/ch44700.itc",                   # 15
        "chr/ch21800.itc",                   # 16
    ))

    DeclNpc(2759,    0,       26000,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-2759,   0,       26000,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2859,    0,       -3779,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(2759,    0,       -19020,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-2980,   0,       -19010,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(10069,   300,     -12420,  0,    385,  0x0, 0,   0,   0,   0,   1,   0,   24,  255,  0)
    DeclNpc(-10829,  0,       5320,    180,  385,  0x0, 0,   0,   0,   0,   2,   0,   25,  255,  0)
    DeclNpc(-5480,   250,     7909,    270,  385,  0x0, 0,   2,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-7480,   250,     7909,    90,   385,  0x0, 0,   3,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(7230,    250,     7760,    225,  385,  0x0, 0,   4,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(13539,   449,     -13340,  315,  389,  0x0, 0,   5,   0,   0,   0,   0,   34,  255,  0)
    DeclNpc(13539,   300,     -11000,  0,    385,  0x0, 0,   6,   0,   0,   3,   0,   35,  255,  0)
    DeclNpc(-10600,  289,     -14420,  0,    385,  0x0, 0,   7,   0,   0,   0,   0,   36,  255,  0)
    DeclNpc(-9750,   289,     -14699,  0,    385,  0x0, 0,   8,   0,   0,   0,   0,   37,  255,  0)
    DeclNpc(-17700,  0,       7489,    0,    385,  0x0, 0,   9,   0,   0,   0,   0,   38,  255,  0)
    DeclNpc(-18700,  0,       7489,    0,    385,  0x0, 0,   10,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-600,    100,     6090,    0,    385,  0x0, 0,   17,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(600,     100,     6090,    0,    385,  0x0, 0,   18,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(-10630,  0,       11239,   45,   385,  0x0, 0,   22,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-899,    100,     7260,    135,  389,  0x0, 0,   11,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(2220,    100,     5559,    270,  389,  0x0, 0,   12,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-2029,   100,     5559,    90,   389,  0x0, 0,   13,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(1620,    100,     7010,    225,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6829,    250,     5150,    0,    389,  0x0, 0,   15,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(-22889,  400,     -6019,   90,   389,  0x0, 0,   16,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   21,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   19,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   20,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-10170,  0,       19069,   0,    132,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(3430,    100,     8590,    0,    132,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(10510,   0,       6289,    0,    132,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 59,  0.0,                   29.0,                  -0.75,                 225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -9.666666984558105,    0.15000000596046448,   1.0])
    DeclEvent(0x0000, 0, 57,  0.0,                   29.0,                  -0.75,                 225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -9.666666984558105,    0.15000000596046448,   1.0])

    DeclActor(-10170,  0,       18070,   2500,    -10170,  2500,    18070,   0x007C, 0,  33, 0x0000)

    PlaceName(-20.690000534057617, 0.0, -334.95001220703125, 0x0000, 0x0000, "中央广场")
    PlaceName(-176.4499969482422, 0.0, -343.79998779296875, 0x0000, 0x0000, "西街")
    PlaceName(21.639999389648438, 0.0, -191.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-276.45001220703125, 0.0, -223.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-142.5, 0.0, -222.60000610351562, 0x0000, 0x0000, "欢乐街")
    PlaceName(113.25, 0.0, -400.5, 0x0000, 0x0000, "东街")
    PlaceName(183.5800018310547, 0.0, -513.25, 0x0000, 0x0000, "旧城区")
    PlaceName(154.9499969482422, 0.0, -274.3999938964844, 0x0000, 0x0000, "港湾区")
    PlaceName(126.94999694824219, 0.0, -96.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-17.75, 0.0, -493.6000061035156, 0x0000, 0x0000, "站前街道")
    PlaceName(-101.80000305175781, 0.0, -283.20001220703125, 0x0000, 0x0000, "后巷")
    PlaceName(-21.200000762939453, 0.0, -548.0499877929688, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(234.85000610351562, 0.0, -384.6000061035156, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-264.95001220703125, 0.0, -340.3999938964844, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-254.0500030517578, 0.0, -165.39999389648438, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(0.0, 0.0, 55.5, 0x0000, 0x0000, "兰花塔")
    PlaceName(-75.98999786376953, 0.0, -390.8500061035156, 0x0000, 0x0051, "")
    PlaceName(26.18000030517578, 0.0, -340.75, 0x0000, 0x0054, "")
    PlaceName(-30.809999465942383, 0.0, -400.6499938964844, 0x0000, 0x0057, "")
    PlaceName(-76.8499984741211, 0.0, -336.20001220703125, 0x0000, 0x0053, "")
    PlaceName(-33.279998779296875, 0.0, -289.79998779296875, 0x0000, 0x0053, "")
    PlaceName(-155.63999938964844, 0.0, -302.45001220703125, 0x0000, 0x0053, "")
    PlaceName(-99.7300033569336, 0.0, -266.6000061035156, 0x0000, 0x0053, "")
    PlaceName(-110.25, 0.0, -240.39999389648438, 0x0000, 0x0052, "")
    PlaceName(128.3000030517578, 0.0, -543.5800170898438, 0x0000, 0x0053, "")
    PlaceName(-85.7300033569336, 0.0, -280.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-26.950000762939453, 0.0, -144.3300018310547, 0x0000, 0x0051, "")
    PlaceName(181.85000610351562, 0.0, -410.5, 0x0000, 0x0052, "")
    PlaceName(128.3000030517578, 0.0, -543.5800170898438, 0x0000, 0x0053, "")
    PlaceName(158.64999389648438, 0.0, -582.2999877929688, 0x0000, 0x0053, "")

    ChipFrameInfo(4864, 0)                                       # 0

    ScpFunction((
        "Function_0_1300",         # 00, 0
        "Function_1_13B0",         # 01, 1
        "Function_2_1445",         # 02, 2
        "Function_3_14DA",         # 03, 3
        "Function_4_1505",         # 04, 4
        "Function_5_159A",         # 05, 5
        "Function_6_15ED",         # 06, 6
        "Function_7_1640",         # 07, 7
        "Function_8_1733",         # 08, 8
        "Function_9_1752",         # 09, 9
        "Function_10_176F",        # 0A, 10
        "Function_11_1832",        # 0B, 11
        "Function_12_1D3D",        # 0C, 12
        "Function_13_204C",        # 0D, 13
        "Function_14_27D4",        # 0E, 14
        "Function_15_3006",        # 0F, 15
        "Function_16_37C0",        # 10, 16
        "Function_17_38DE",        # 11, 17
        "Function_18_393B",        # 12, 18
        "Function_19_39B6",        # 13, 19
        "Function_20_3A17",        # 14, 20
        "Function_21_3A8D",        # 15, 21
        "Function_22_4013",        # 16, 22
        "Function_23_40DB",        # 17, 23
        "Function_24_418F",        # 18, 24
        "Function_25_41BB",        # 19, 25
        "Function_26_4212",        # 1A, 26
        "Function_27_4289",        # 1B, 27
        "Function_28_42C6",        # 1C, 28
        "Function_29_46A3",        # 1D, 29
        "Function_30_4A43",        # 1E, 30
        "Function_31_4DD9",        # 1F, 31
        "Function_32_5227",        # 20, 32
        "Function_33_562E",        # 21, 33
        "Function_34_5842",        # 22, 34
        "Function_35_5B15",        # 23, 35
        "Function_36_5CDC",        # 24, 36
        "Function_37_5D38",        # 25, 37
        "Function_38_5D82",        # 26, 38
        "Function_39_5EFB",        # 27, 39
        "Function_40_6046",        # 28, 40
        "Function_41_6074",        # 29, 41
        "Function_42_60BA",        # 2A, 42
        "Function_43_6137",        # 2B, 43
        "Function_44_61D0",        # 2C, 44
        "Function_45_6FEC",        # 2D, 45
        "Function_46_74F9",        # 2E, 46
        "Function_47_7A32",        # 2F, 47
        "Function_48_7A7F",        # 30, 48
        "Function_49_7ACC",        # 31, 49
        "Function_50_7B19",        # 32, 50
        "Function_51_7B66",        # 33, 51
        "Function_52_94F1",        # 34, 52
        "Function_53_95AA",        # 35, 53
        "Function_54_9728",        # 36, 54
        "Function_55_974E",        # 37, 55
        "Function_56_97A9",        # 38, 56
        "Function_57_9B72",        # 39, 57
        "Function_58_9BD0",        # 3A, 58
        "Function_59_A3B9",        # 3B, 59
        "Function_60_A7CC",        # 3C, 60
        "Function_61_AA32",        # 3D, 61
        "Function_62_B68D",        # 3E, 62
        "Function_63_B74C",        # 3F, 63
        "Function_64_B86D",        # 40, 64
        "Function_65_BF86",        # 41, 65
        "Function_66_C03F",        # 42, 66
        "Function_67_CAF5",        # 43, 67
        "Function_68_CB11",        # 44, 68
        "Function_69_CB3A",        # 45, 69
        "Function_70_CC48",        # 46, 70
        "Function_71_E57B",        # 47, 71
        "Function_72_E5E4",        # 48, 72
        "Function_73_E647",        # 49, 73
        "Function_74_E6AA",        # 4A, 74
        "Function_75_E70D",        # 4B, 75
        "Function_76_E778",        # 4C, 76
        "Function_77_E7E1",        # 4D, 77
        "Function_78_E836",        # 4E, 78
        "Function_79_E8A2",        # 4F, 79
        "Function_80_E913",        # 50, 80
        "Function_81_EABA",        # 51, 81
        "Function_82_EC64",        # 52, 82
        "Function_83_EE0B",        # 53, 83
        "Function_84_EE56",        # 54, 84
        "Function_85_EEA5",        # 55, 85
        "Function_86_EF08",        # 56, 86
        "Function_87_EF6B",        # 57, 87
        "Function_88_EFCE",        # 58, 88
        "Function_89_F02C",        # 59, 89
        "Function_90_F0B9",        # 5A, 90
        "Function_91_F28F",        # 5B, 91
        "Function_92_F312",        # 5C, 92
        "Function_93_F395",        # 5D, 93
        "Function_94_F418",        # 5E, 94
        "Function_95_F75C",        # 5F, 95
        "Function_96_F7B2",        # 60, 96
        "Function_97_F8D1",        # 61, 97
        "Function_98_F919",        # 62, 98
        "Function_99_FC11",        # 63, 99
        "Function_100_FC9F",       # 64, 100
        "Function_101_FDAD",       # 65, 101
        "Function_102_FDDC",       # 66, 102
        "Function_103_FE95",       # 67, 103
        "Function_104_FFA2",       # 68, 104
        "Function_105_10117",      # 69, 105
        "Function_106_10150",      # 6A, 106
        "Function_107_1078A",      # 6B, 107
        "Function_108_10796",      # 6C, 108
        "Function_109_107B9",      # 6D, 109
        "Function_110_10A04",      # 6E, 110
        "Function_111_10A9E",      # 6F, 111
        "Function_112_10B01",      # 70, 112
        "Function_113_10CA0",      # 71, 113
        "Function_114_10CEB",      # 72, 114
        "Function_115_10D85",      # 73, 115
        "Function_116_10DEB",      # 74, 116
        "Function_117_10E77",      # 75, 117
        "Function_118_10E96",      # 76, 118
        "Function_119_10F78",      # 77, 119
        "Function_120_1104B",      # 78, 120
        "Function_121_11180",      # 79, 121
        "Function_122_111A8",      # 7A, 122
        "Function_123_11249",      # 7B, 123
        "Function_124_1129F",      # 7C, 124
        "Function_125_11372",      # 7D, 125
        "Function_126_11391",      # 7E, 126
        "Function_127_1143B",      # 7F, 127
        "Function_128_11455",      # 80, 128
        "Function_129_1146F",      # 81, 129
        "Function_130_11489",      # 82, 130
        "Function_131_114D0",      # 83, 131
        "Function_132_11517",      # 84, 132
        "Function_133_11534",      # 85, 133
        "Function_134_1155F",      # 86, 134
        "Function_135_115AE",      # 87, 135
        "Function_136_115E7",      # 88, 136
        "Function_137_11619",      # 89, 137
        "Function_138_1164B",      # 8A, 138
        "Function_139_116A1",      # 8B, 139
        "Function_140_116F7",      # 8C, 140
        "Function_141_1174D",      # 8D, 141
        "Function_142_117A3",      # 8E, 142
        "Function_143_11EBE",      # 8F, 143
        "Function_144_11F2D",      # 90, 144
        "Function_145_11F93",      # 91, 145
        "Function_146_11FF9",      # 92, 146
        "Function_147_1205F",      # 93, 147
        "Function_148_120C5",      # 94, 148
        "Function_149_1212B",      # 95, 149
        "Function_150_123EC",      # 96, 150
    ))


    def Function_0_1300(): pass

    label("Function_0_1300")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1338"),
        (1, "loc_1344"),
        (2, "loc_1350"),
        (3, "loc_135C"),
        (4, "loc_1368"),
        (5, "loc_1374"),
        (6, "loc_1380"),
        (SWITCH_DEFAULT, "loc_138C"),
    )


    label("loc_1338")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1344")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1350")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_135C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1368")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1374")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1380")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_138C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_1398")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1398")

    label("loc_13AF")

    Return()

    # Function_0_1300 end

    def Function_1_13B0(): pass

    label("Function_1_13B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1444")
    OP_95(0xFE, 10070, 0, 6000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 21680, 300, 6000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 21680, 300, -6750, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 10070, 300, -12420, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    Jump("Function_1_13B0")

    label("loc_1444")

    Return()

    # Function_1_13B0 end

    def Function_2_1445(): pass

    label("Function_2_1445")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14D9")
    OP_95(0xFE, -10830, 300, -12520, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -21560, 300, -6130, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -21560, 300, 5320, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -10830, 0, 5320, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_2_1445")

    label("loc_14D9")

    Return()

    # Function_2_1445 end

    def Function_3_14DA(): pass

    label("Function_3_14DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1504")
    OP_94(0xFE, 0x2AEE, 0xFFFFD800, 0x3E30, 0xFFFFD382, 0x3E8)
    Sleep(300)
    Jump("Function_3_14DA")

    label("loc_1504")

    Return()

    # Function_3_14DA end

    def Function_4_1505(): pass

    label("Function_4_1505")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1599")
    OP_95(0xFE, -5600, 250, 3020, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -10570, 0, 3180, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -5330, 0, -3700, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -10720, 0, -3700, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    Jump("Function_4_1505")

    label("loc_1599")

    Return()

    # Function_4_1505 end

    def Function_5_159A(): pass

    label("Function_5_159A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15EC")
    OP_95(0xFE, -21660, 300, 20300, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -21660, 300, -7500, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    Jump("Function_5_159A")

    label("loc_15EC")

    Return()

    # Function_5_159A end

    def Function_6_15ED(): pass

    label("Function_6_15ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_163F")
    OP_95(0xFE, 21300, 300, -9300, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 21300, 300, 21000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_6_15ED")

    label("loc_163F")

    Return()

    # Function_6_15ED end

    def Function_7_1640(): pass

    label("Function_7_1640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1732")
    OP_95(0xFE, 14560, 0, 5730, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, 8390, 250, 4070, 2000, 0x0)
    OP_95(0xFE, 6130, 250, 4070, 2000, 0x0)
    OP_95(0xFE, 140, 100, 4000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 6130, 250, 4070, 2000, 0x0)
    OP_95(0xFE, 8390, 250, 4070, 2000, 0x0)
    Jump("Function_7_1640")

    label("loc_1732")

    Return()

    # Function_7_1640 end

    def Function_8_1733(): pass

    label("Function_8_1733")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1751")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_1733")

    label("loc_1751")

    Return()

    # Function_8_1733 end

    def Function_9_1752(): pass

    label("Function_9_1752")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_176E")
    OP_A1(0xFE, 0x2BC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_9_1752")

    label("loc_176E")

    Return()

    # Function_9_1752 end

    def Function_10_176F(): pass

    label("Function_10_176F")

    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17CA")
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_17CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_180D")
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1822")
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1831")
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_1831")

    Return()

    # Function_10_176F end

    def Function_11_1832(): pass

    label("Function_11_1832")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190F")
    SetChrPos(0x0, 0, -4930, -40200, 0)
    SetChrPos(0x1, 0, -4930, -40200, 0)
    SetChrPos(0x2, 0, -4930, -40200, 0)
    SetChrPos(0x3, 0, -4930, -40200, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B9")
    SetChrPos(0x4, 0, -4930, -40200, 0)
    SetChrPos(0x5, 0, -4930, -40200, 0)
    Jump("loc_18D8")

    label("loc_18B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D8")
    SetChrPos(0x4, 0, -4930, -40200, 0)

    label("loc_18D8")

    OP_68(0, -2430, -40200, 0)
    MoveCamera(0, 2, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(19000, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_190F")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 12310, 300, -14690, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x40)
    ClearChrFlags(0x23, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1973")
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x21, 0x10)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x23, 0x10)

    label("loc_1973")

    BeginChrThread(0x22, 0, 0, 0)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrPos(0x11, 4840, 250, 3840, 45)
    SetChrPos(0x21, 5390, 250, 6320, 135)
    SetChrPos(0x22, 7580, 250, 5850, 225)
    SetChrPos(0x23, 8310, 250, 4150, 315)
    Jump("loc_1C02")

    label("loc_19C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19E0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_1C02")

    label("loc_19E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19F8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_1C02")

    label("loc_19F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A3C")
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0x10)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jump("loc_1C02")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A87")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_93(0x16, 0x5A, 0x0)
    OP_93(0x17, 0x5A, 0x0)
    Jump("loc_1C02")

    label("loc_1A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A9F")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_1C02")

    label("loc_1A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1AD7")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1C02")

    label("loc_1AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B0F")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1C02")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B47")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_1C02")

    label("loc_1B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B82")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_1C02")

    label("loc_1B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BDD")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_1C02")

    label("loc_1BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BEB")
    Jump("loc_1C02")

    label("loc_1BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1BF9")
    Jump("loc_1C02")

    label("loc_1BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C02")

    label("loc_1C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1C19")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 7)
    Event(0, 46)
    Jump("loc_1CE2")

    label("loc_1C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1C2D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 51)
    Jump("loc_1CE2")

    label("loc_1C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1C44")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 7)
    Event(0, 60)
    Jump("loc_1CE2")

    label("loc_1C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1C58")
    ClearScenarioFlags(0x22, 3)
    Event(0, 61)
    Jump("loc_1CE2")

    label("loc_1C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1C6F")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x0, 7)
    Event(0, 64)
    Jump("loc_1CE2")

    label("loc_1C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1C83")
    ClearScenarioFlags(0x22, 5)
    Event(0, 66)
    Jump("loc_1CE2")

    label("loc_1C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1C97")
    ClearScenarioFlags(0x22, 6)
    Event(0, 69)
    Jump("loc_1CE2")

    label("loc_1C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_1CAB")
    ClearScenarioFlags(0x22, 7)
    Event(0, 70)
    Jump("loc_1CE2")

    label("loc_1CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_1CBF")
    ClearScenarioFlags(0x23, 0)
    Event(0, 142)
    Jump("loc_1CE2")

    label("loc_1CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1CD3")
    ClearScenarioFlags(0x23, 1)
    Event(0, 149)
    Jump("loc_1CE2")

    label("loc_1CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1CE2")
    ClearScenarioFlags(0x23, 2)
    Event(0, 150)

    label("loc_1CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D06")
    SetMapFlags(0x10000000)
    Event(0, 44)
    Jump("loc_1D3C")

    label("loc_1D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D21")
    SetMapFlags(0x10000000)
    Event(0, 58)
    Jump("loc_1D3C")

    label("loc_1D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3C")
    SetMapFlags(0x10000000)
    Event(0, 56)

    label("loc_1D3C")

    Return()

    # Function_11_1832 end

    def Function_12_1D3D(): pass

    label("Function_12_1D3D")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x1C2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1D5F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)

    label("loc_1D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D78")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_1D7E")

    label("loc_1D78")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_1D7E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D96")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1D96")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2_add", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1ECC")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x1F4, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F4E")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0x276, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_1F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_1F5D")
    SetMapObjFlags(0x9, 0x4)

    label("loc_1F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F85")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    SetMapObjFrame(0xC, "mark01", 0x0, 0x1)

    label("loc_1F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2022")
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x25, 0x4)
    OP_78(0xC, 0x25)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    OP_D5(0x25, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFrame(0xC, "mark00", 0x0, 0x1)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x4)
    OP_78(0xE, 0x26)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_D5(0x26, 0x0, 0x27100, 0x0, 0x0)
    SetMapObjFrame(0xE, "mark00", 0x0, 0x1)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x2)

    label("loc_2022")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2033")
    OP_66(0x0, 0x1)

    label("loc_2033")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_204B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_204B")

    Return()

    # Function_12_1D3D end

    def Function_13_204C(): pass

    label("Function_13_204C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20C3")

    #C0001
    ChrTalk(
        0xFE,
        (
            "国防军士兵撤退之后，\x01",
            "我们警备科被重新\x01",
            "分配到了守备位置。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "目前的状况很严峻，我们一起努力吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27D0")

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20D1")
    Jump("loc_27D0")

    label("loc_20D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_20DF")
    Jump("loc_27D0")

    label("loc_20DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C1")

    #C0003
    ChrTalk(
        0xFE,
        (
            "兰花塔前的攻防战……\x01",
            "真是惨烈到了极点。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "老实说，如果没有亚里欧斯先生，\x01",
            "这里恐怕也会和ＩＢＣ一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……唔，\x01",
            "说出口之后，\x01",
            "突然觉得很后怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "总之，这里平安无事。\x01",
            "想太多也是没用的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_226E")

    label("loc_21C1")


    #C0007
    ChrTalk(
        0xFE,
        (
            "话说回来，达德利警官真是厉害……\x01",
            "而亚里欧斯先生的实力就更不用说了，\x01",
            "和我们简直不在一个层次。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "剑术与身法简直可以说是神乎其技……\x01",
            "『风之剑圣』这个称号真是太贴切了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_226E")

    Jump("loc_27D0")

    label("loc_2273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_22F1")

    #C0009
    ChrTalk(
        0xFE,
        (
            "玛因兹遭受占领吗……\x01",
            "啧，又发生了\x01",
            "不得了的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "据说现在的情况相当严峻，\x01",
            "希望警备队尽力\x01",
            "撑过去啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D0")

    label("loc_22F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2355")

    #C0011
    ChrTalk(
        0xFE,
        (
            "一到下雨天，\x01",
            "连这个广场都没人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "这里如此宽阔，\x01",
            "更是平添了一丝忧愁的气息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D0")

    label("loc_2355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_23DE")

    #C0013
    ChrTalk(
        0xFE,
        (
            "刚才听前台的人说，\x01",
            "发生了列车脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "搜查二科和警备队都\x01",
            "已经派人去调查了……\x01",
            "不知受损程度如何，真让人担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D0")

    label("loc_23DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2469")

    #C0015
    ChrTalk(
        0xFE,
        (
            "兰花塔前的这片广场\x01",
            "已经成为广受市民们欢迎的\x01",
            "休息场所了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "看着和睦的一家人\x01",
            "来这里玩，\x01",
            "心里感到很温暖。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24AD")

    label("loc_2469")


    #C0017
    ChrTalk(
        0xFE,
        (
            "明媚的阳光\x01",
            "与和睦的家庭……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "嗯～没有比这更\x01",
            "温馨的景象了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AD")

    Jump("loc_27D0")

    label("loc_24B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_25FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2597")

    #C0019
    ChrTalk(
        0xFE,
        (
            "自通商会议结束，\x01",
            "已经过了一个多月了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "恐怖分子们的袭击\x01",
            "自然是件大事，\x01",
            "紧接着，市长又呼吁独立……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "呼，今年真是\x01",
            "接连不断地\x01",
            "发生重大事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "简直让人眼花缭乱，\x01",
            "日子好像一眨眼就过去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25F6")

    label("loc_2597")


    #C0023
    ChrTalk(
        0xFE,
        (
            "呼，今年真是\x01",
            "接连不断地\x01",
            "发生重大事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "简直让人眼花缭乱，\x01",
            "日子好像一眨眼就过去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F6")

    Jump("loc_27D0")

    label("loc_25FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2683")

    #C0025
    ChrTalk(
        0xFE,
        "哟，这不是特别任务支援科吗。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "听说你们参加了\x01",
            "通商会议的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "如果有需要，随时都可以进去。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26CE")

    label("loc_2683")


    #C0028
    ChrTalk(
        0xFE,
        (
            "听说你们参加了\x01",
            "通商会议的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "如果有需要，随时都可以进去。\x02",
    )

    CloseMessageWindow()

    label("loc_26CE")

    Jump("loc_27D0")

    label("loc_26D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2770")

    #C0030
    ChrTalk(
        0xFE,
        "哦，你们是特别任务支援科吧？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "兰花塔的警备工作\x01",
            "是由我们警备科负责的。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "大家都是警察，如果遇到\x01",
            "什么问题就互相帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27D0")

    label("loc_2770")


    #C0033
    ChrTalk(
        0xFE,
        (
            "兰花塔的警备工作\x01",
            "是由我们警备科负责的。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "大家都是警察，如果遇到\x01",
            "什么问题就互相帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D0")

    TalkEnd(0xFE)
    Return()

    # Function_13_204C end

    def Function_14_27D4(): pass

    label("Function_14_27D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2842")

    #C0035
    ChrTalk(
        0xFE,
        (
            "迪塔总统被拘禁\x01",
            "在三十六层。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "竟然拘捕了\x01",
            "自己国家的最高领导。\x01",
            "……心情真是很复杂啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3002")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2850")
    Jump("loc_3002")

    label("loc_2850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_285E")
    Jump("loc_3002")

    label("loc_285E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291A")

    #C0037
    ChrTalk(
        0xFE,
        (
            "『赤色星座』……\x01",
            "……真是一群可怕的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "单体战斗技术自不必说，\x01",
            "装备的差距也相当明显……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "假如克洛斯贝尔有自己的军队，\x01",
            "情况应该就会有所不同了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_298C")

    label("loc_291A")


    #C0040
    ChrTalk(
        0xFE,
        (
            "『赤色星座』……\x01",
            "……真是一群可怕的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "但是，假如克洛斯贝尔有自己的军队，\x01",
            "情况应该就会有所不同了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298C")

    Jump("loc_3002")

    label("loc_2991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6E")

    #C0042
    ChrTalk(
        0xFE,
        (
            "在这种特殊时期，\x01",
            "我们警察就更要拿出勇气，\x01",
            "为广大市民保卫这座城市。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "和警备队一样，\x01",
            "我们平时也是为此\x01",
            "才不断训练的。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "『永远担当市民的表率』，\x01",
            "让我们重新回味这番话，\x01",
            "一同鼓起干劲吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AFC")

    label("loc_2A6E")


    #C0045
    ChrTalk(
        0xFE,
        (
            "在这种特殊时期，\x01",
            "我们警察就更要拿出勇气，\x01",
            "为广大市民保卫这座城市。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "『永远担当市民的表率』，\x01",
            "让我们重新回味这番话，\x01",
            "一同鼓起干劲吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFC")

    Jump("loc_3002")

    label("loc_2B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2BA7")

    #C0047
    ChrTalk(
        0xFE,
        (
            "多亏了警备队的努力，\x01",
            "铁路总算在昨天\x01",
            "恢复通车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "假如在抢修结束前下了这场雨，\x01",
            "情况肯定会很麻烦吧……\x01",
            "警备队的应对如此迅速，真是令人心生敬意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3002")

    label("loc_2BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2C20")

    #C0049
    ChrTalk(
        0xFE,
        (
            "西克洛斯贝尔街道那边的\x01",
            "导力列车脱轨了……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "这种事故在克洛斯贝尔\x01",
            "可十分罕见，\x01",
            "到底发生了什么情况？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3002")

    label("loc_2C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2CBB")

    #C0051
    ChrTalk(
        0xFE,
        (
            "等兰花塔进一步\x01",
            "投入使用之后，\x01",
            "肯定会有更多人出入这个广场。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "到时候，工作应该会变得更加繁忙，\x01",
            "但身为一名克洛斯贝尔人，实在是很高兴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3002")

    label("loc_2CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DED")

    #C0053
    ChrTalk(
        0xFE,
        (
            "这话题已经讨论过多次了，\x01",
            "在通商会议的恐怖袭击中，\x01",
            "我们实在是很失败。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "警队完全陷入被动，\x01",
            "最后全靠两大国事先预备的\x01",
            "战斗部队，才将事态平息……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "不仅如此，还被两大国以安保问题\x01",
            "为由反将一军……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "今后不但需要更加完善的危机管理措施，\x01",
            "我们自己也需进一步\x01",
            "提高危机意识。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E85")

    label("loc_2DED")


    #C0057
    ChrTalk(
        0xFE,
        (
            "本以为我们布置了两三重防线，\x01",
            "足以确保万无一失，\x01",
            "没想到那么简单就被……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "今后不但需要更加完善的危机管理措施，\x01",
            "我们自己也需进一步\x01",
            "提高危机意识。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E85")

    Jump("loc_3002")

    label("loc_2E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2EE1")

    #C0059
    ChrTalk(
        0xFE,
        "各位，今天也辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "为了让通商会议平安结束，\x01",
            "我们一起努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3002")

    label("loc_2EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F74")

    #C0061
    ChrTalk(
        0xFE,
        (
            "我和坎宁巡警\x01",
            "这次被分配来做\x01",
            "兰花塔的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "在通商会议期间自不必说，\x01",
            "今后应该也会一直守在这里，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3002")

    label("loc_2F74")


    #C0063
    ChrTalk(
        0xFE,
        (
            "能在这被整个大陆关注的\x01",
            "兰花塔工作，\x01",
            "我感到十分光荣。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "虽然这座建筑拥有最尖端的安全系统，\x01",
            "但我绝不会因此而松懈，\x01",
            "一定会用心履行职责。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3002")

    TalkEnd(0xFE)
    Return()

    # Function_14_27D4 end

    def Function_15_3006(): pass

    label("Function_15_3006")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3070")

    #C0065
    ChrTalk(
        0xFE,
        (
            "总统竟然被捕了……\x01",
            "克洛斯贝尔今后\x01",
            "将何去何从呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "……算了，\x01",
            "船到桥头自然直。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BC")

    label("loc_3070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_307E")
    Jump("loc_37BC")

    label("loc_307E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_308C")
    Jump("loc_37BC")

    label("loc_308C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3176")

    #C0067
    ChrTalk(
        0xFE,
        (
            "遭到袭击的时候，我正在财务科的楼层，\x01",
            "当时要去地下避难……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "但导力梯显然不能\x01",
            "供所有人乘坐，\x01",
            "所以年轻男子就要走楼梯。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "顺便一说，\x01",
            "财务科在三十一层。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "……我当时跑得上气不接下气，\x01",
            "简直快死了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31DA")

    label("loc_3176")


    #C0071
    ChrTalk(
        0xFE,
        (
            "真是没想到，在这种高层建筑中，\x01",
            "竟然还要从楼梯跑下去……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "呼，看来平时的锻炼\x01",
            "也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31DA")

    Jump("loc_37BC")

    label("loc_31DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_32FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3293")

    #C0073
    ChrTalk(
        0xFE,
        "听说猎兵团和警备队正在交战……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "无谓的支出又要增加了吧……\x01",
            "不对，现在可不是\x01",
            "说这种话的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "总之，还是向女神祈祷，\x01",
            "希望事态能尽早平息吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32F9")

    label("loc_3293")


    #C0076
    ChrTalk(
        0xFE,
        (
            "真是的，最近的大事接连不断，\x01",
            "让人无可奈何啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "总之，还是向女神祈祷，\x01",
            "希望事态能尽早平息吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F9")

    Jump("loc_37BC")

    label("loc_32FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_330C")
    Jump("loc_37BC")

    label("loc_330C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3421")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33BA")

    #C0078
    ChrTalk(
        0xFE,
        (
            "虽然不知道发生了什么，\x01",
            "但列车好像停运了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "大陆经济的大动脉停止运作……\x01",
            "这可不是闹着玩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "要是不快点恢复通车，\x01",
            "会造成严重问题的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_341C")

    label("loc_33BA")


    #C0081
    ChrTalk(
        0xFE,
        (
            "大陆经济的大动脉停止运作……\x01",
            "这可不是闹着玩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "要是不快点恢复通车，\x01",
            "会造成严重问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_341C")

    Jump("loc_37BC")

    label("loc_3421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34B5")

    #C0083
    ChrTalk(
        0xFE,
        (
            "迪塔市长从来不用\x01",
            "公款来支付交际费用或旅费，\x01",
            "全部都是自掏腰包。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "不愧是ＩＢＣ总裁……\x01",
            "光用豪爽大方等词汇\x01",
            "完全不足以形容他啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BC")

    label("loc_34B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_367E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35EF")

    #C0085
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立吗……\x01",
            "库罗伊斯市长\x01",
            "竟然如此大胆。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "我也是财务科的一员，\x01",
            "自然明白税收纳贡制度\x01",
            "是个令人头痛的问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "就算在谈话时，我们都不能提及\x01",
            "任何与宗主国问题相关的话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "两大国自然已经\x01",
            "发出了不承认独立的声明……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "不知他们今后会有什么行动，\x01",
            "我真是担心得不得了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3679")

    label("loc_35EF")


    #C0090
    ChrTalk(
        0xFE,
        (
            "虽然居民投票活动\x01",
            "只是为了调查居民们\x01",
            "对独立一事的意向……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "但即使如此，两大国\x01",
            "肯定也不会给我们好脸色看。\x01",
            "真担心他们今后的行动啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3679")

    Jump("loc_37BC")

    label("loc_367E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_368C")
    Jump("loc_37BC")

    label("loc_368C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3742")

    #C0092
    ChrTalk(
        0xFE,
        (
            "呼，兰花塔竟然\x01",
            "真的竣工了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "不惜花费ＩＢＣ的资本\x01",
            "投资公共事业，\x01",
            "这就是迪塔市长的气魄……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "相比那些只知道\x01",
            "中饱私囊的议员，\x01",
            "差别实在是太大了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37BC")

    label("loc_3742")


    #C0095
    ChrTalk(
        0xFE,
        (
            "不惜花费ＩＢＣ的资本\x01",
            "投资公共事业，\x01",
            "这就是迪塔市长的气魄……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "相比那些只知道\x01",
            "中饱私囊的议员，\x01",
            "差别实在是太大了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BC")

    TalkEnd(0xFE)
    Return()

    # Function_15_3006 end

    def Function_16_37C0(): pass

    label("Function_16_37C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_38D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_386E")

    #C0097
    ChrTalk(
        0xFE,
        (
            "『兰花塔』终于\x01",
            "展现在了市民的面前……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "这直耸入云的威容\x01",
            "和以蓝白为基调的外观\x01",
            "实在是漂亮极了……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "接下设计它的工作，\x01",
            "真是太好了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_38CC")

    label("loc_386E")


    #C0100
    ChrTalk(
        0xFE,
        (
            "说起来，设计这座高达\x01",
            "四十层的建筑，还真是极其困难……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "……唔……\x01",
            "眼眶都开始发热了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CC")

    Jump("loc_38DA")

    label("loc_38D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38DA")

    label("loc_38DA")

    TalkEnd(0xFE)
    Return()

    # Function_16_37C0 end

    def Function_17_38DE(): pass

    label("Function_17_38DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F3")
    Call(0, 21)
    Jump("loc_3937")

    label("loc_38F3")


    #C0102
    ChrTalk(
        0xFE,
        (
            "说起来，琪雅\x01",
            "没事吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "她在百货店楼顶的\x01",
            "样子有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3937")

    TalkEnd(0xFE)
    Return()

    # Function_17_38DE end

    def Function_18_393B(): pass

    label("Function_18_393B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3950")
    Call(0, 21)
    Jump("loc_39B2")

    label("loc_3950")


    #C0104
    ChrTalk(
        0xFE,
        (
            "秦虽然说话没什么礼貌，\x01",
            "但本质上是个好孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "听说他明天就要回去了，\x01",
            "那就趁现在玩个够吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B2")

    TalkEnd(0xFE)
    Return()

    # Function_18_393B end

    def Function_19_39B6(): pass

    label("Function_19_39B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CB")
    Call(0, 21)
    Jump("loc_3A13")

    label("loc_39CB")


    #C0106
    ChrTalk(
        0xFE,
        (
            "兰花塔……\x01",
            "这栋建筑比想象中还要\x01",
            "帅气得多呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "真想进去看看啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3A13")

    TalkEnd(0xFE)
    Return()

    # Function_19_39B6 end

    def Function_20_3A17(): pass

    label("Function_20_3A17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2C")
    Call(0, 21)
    Jump("loc_3A89")

    label("loc_3A2C")


    #C0108
    ChrTalk(
        0xFE,
        (
            "哼、哼……\x01",
            "俗人就是这样，真麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "总之……\x01",
            "为了我光辉的未来，\x01",
            "一定要认真参观这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A89")

    TalkEnd(0xFE)
    Return()

    # Function_20_3A17 end

    def Function_21_3A8D(): pass

    label("Function_21_3A8D")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3BCF")

    #C0110
    ChrTalk(
        0x101,
        "#00005F咦，这不是秦吗。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    #C0111
    ChrTalk(
        0x1E,
        (
            "啊……\x01",
            "你们是昨天的……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)

    #C0112
    ChrTalk(
        0x1E,
        "大姐姐，你好！！\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，你好，\x01",
            "在和隆他们一起玩吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x1E,
        (
            "嗯，是呀。\x01",
            "他们非要和我一起玩，\x01",
            "真是没办法……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1E, 500)

    #C0115
    ChrTalk(
        0x1B,
        "谁说非要和你玩了～？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x1B,
        (
            "琪雅和滴都回去了，\x01",
            "我们看你一副寂寞的样子，\x01",
            "才邀请你的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EE3")

    label("loc_3BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DAF")

    #C0117
    ChrTalk(
        0x101,
        "#00005F咦，你好像是……秦？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    #C0118
    ChrTalk(
        0x1E,
        (
            "啊……\x01",
            "你们是昨天的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1E,
        (
            "不给我做导游，\x01",
            "干什么去了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        (
            "#00106F抱歉，秦。\x01",
            "我们实在是\x01",
            "脱不开身……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)

    #C0121
    ChrTalk(
        0x1E,
        (
            "唔……那、那个……\x01",
            "我并不是想对大姐姐发脾气……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1E,
        (
            "……哼，算了。\x01",
            "虽然让部下们带我游览很无聊，\x01",
            "但至少也参观过市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#00300F话说回来，你今天在和\x01",
            "这两个小鬼一起玩啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x104, 500)

    #C0124
    ChrTalk(
        0x1B,
        (
            "嗯，我们在百货店的楼顶\x01",
            "一起看了揭幕式，\x01",
            "然后就继续在一起玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x1B,
        (
            "因为他就一个人，\x01",
            "好像很寂寞的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EE3")

    label("loc_3DAF")


    #C0126
    ChrTalk(
        0x101,
        (
            "#00002F呀，这不是隆和亨利吗。\x02\x03",

            "#00005F……咦，还有个\x01",
            "没见过的孩子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x0, 500)

    #C0127
    ChrTalk(
        0x1E,
        (
            "你们是谁啊？\x01",
            "隆，你们认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x1E,
        "听好，本少爷是黑——\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x0, 500)

    #C0129
    ChrTalk(
        0x1B,
        (
            "这个，虽然不太懂……\x01",
            "但他好像是来自共和国的旅客。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x1B,
        (
            "我们在百货店的楼顶\x01",
            "一起看了揭幕式，\x01",
            "然后就继续在一起玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1B,
        (
            "因为他就一个人，\x01",
            "好像很寂寞的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE3")

    TurnDirection(0x1E, 0x1B, 500)

    #C0132
    ChrTalk(
        0x1E,
        (
            "谁、谁寂寞了……\x01",
            "不许胡说！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x1B,
        (
            "才不是胡说呢！\x01",
            "小桃，你说对不对？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)

    #C0134
    ChrTalk(
        0x1D,
        "啊……嗯，那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    #C0135
    ChrTalk(
        0x1C,
        (
            "好、好啦，隆，\x01",
            "别再戏弄人家了～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3FBC")

    #C0136
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈，相处得\x01",
            "  好像不错呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE3")

    label("loc_3FBC")


    #C0137
    ChrTalk(
        0x101,
        "#00002F（哈哈，相处得很融洽啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_3FE3")

    OP_93(0x1E, 0xE1, 0x0)
    OP_93(0x1B, 0x87, 0x0)
    OP_93(0x1C, 0x10E, 0x0)
    OP_93(0x1D, 0x5A, 0x0)
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    OP_4C(0x1D, 0xFF)
    SetScenarioFlags(0x159, 2)
    Return()

    # Function_21_3A8D end

    def Function_22_4013(): pass

    label("Function_22_4013")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4086")

    #C0138
    ChrTalk(
        0xFE,
        (
            "暂时没有发现\x01",
            "恐怖分子的迹象。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "再怎么说，他们也不会从正面来吧……\x01",
            "总之，我会继续警戒的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D7")

    label("loc_4086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_40D7")

    #C0140
    ChrTalk(
        0xFE,
        (
            "呀，你们好。\x01",
            "这个广场不错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "一定会成为克洛斯贝尔的\x01",
            "新景点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D7")

    TalkEnd(0xFE)
    Return()

    # Function_22_4013 end

    def Function_23_40DB(): pass

    label("Function_23_40DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4139")

    #C0142
    ChrTalk(
        0xFE,
        (
            "兰花塔今天全天\x01",
            "禁止无关人士\x01",
            "入内。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "各位是特别任务支援科吧？\x01",
            "请进。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_418B")

    label("loc_4139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_418B")

    #C0144
    ChrTalk(
        0xFE,
        "欢迎来到兰花塔。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "各位可以自由出入广场，\x01",
            "有需要时，请随意通行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_418B")

    TalkEnd(0xFE)
    Return()

    # Function_23_40DB end

    def Function_24_418F(): pass

    label("Function_24_418F")

    TalkBegin(0xFE)

    #C0146
    ChrTalk(
        0xFE,
        (
            "大家辛苦了，\x01",
            "广场一带没有异常。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_418F end

    def Function_25_41BB(): pass

    label("Function_25_41BB")

    TalkBegin(0xFE)

    #C0147
    ChrTalk(
        0xFE,
        (
            "呼，会议终于要\x01",
            "正式召开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "我开始有点紧张了……\x01",
            "必须要放松下来才行。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_41BB end

    def Function_26_4212(): pass

    label("Function_26_4212")

    TalkBegin(0xFE)

    #C0149
    ChrTalk(
        0xFE,
        (
            "听、听好，在迎接各国首脑的时候，\x01",
            "一定要面带笑容，\x01",
            "不准失礼。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "万一失了礼节，\x01",
            "我们的脑袋\x01",
            "可就保不住了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_4212 end

    def Function_27_4289(): pass

    label("Function_27_4289")

    TalkBegin(0xFE)

    #C0151
    ChrTalk(
        0xFE,
        (
            "部、部长～\x01",
            "我们都知道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "请别再\x01",
            "吓唬人啦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_4289 end

    def Function_28_42C6(): pass

    label("Function_28_42C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E4")
    Call(0, 30)
    Jump("loc_4623")

    label("loc_42E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A5")

    #C0153
    ChrTalk(
        0x11,
        "#07902F各位……还有兰迪。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#00302F哟，米蕾优，\x01",
            "你平安返回部队了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x11,
        (
            "#07904F嗯，托各位的福。\x02\x03",

            "#07902F司令爽快地接纳了\x01",
            "我们这群违规脱队的人归队。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4410")

    #C0156
    ChrTalk(
        0x109,
        (
            "#10100F呵呵，以索妮亚司令的作风来说，\x01",
            "这也是预料之中的。\x02\x03",

            "毕竟部队现在很需要\x01",
            "米蕾优三尉这样的优秀队员……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447A")

    label("loc_4410")


    #C0157
    ChrTalk(
        0x103,
        (
            "#00204F不愧是索妮亚司令，\x01",
            "处理方式真灵活。\x02\x03",

            "#00202F部队现在肯定很需要\x01",
            "米蕾优三尉这样的优秀队员吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_447A")


    #C0158
    ChrTalk(
        0x11,
        (
            "#07904F呵呵，是否优秀\x01",
            "倒不敢说……\x02\x03",

            "#07902F但既然已经归队，\x01",
            "我就要竭尽全力。\x02\x03",

            "这不仅是为了完成国防军成员\x01",
            "或警备队员的职责，\x01",
            "更是为了履行守护克洛斯贝尔的使命。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#00300F加油啊，米蕾优。\x02\x03",

            "#00309F但也别因为太有干劲，\x01",
            "四处瞎忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x11,
        (
            "#07906F不、不用你说我也知道！\x01",
            "……真是的，蠢兰迪！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 2)
    Jump("loc_4623")

    label("loc_45A5")


    #C0161
    ChrTalk(
        0x11,
        (
            "#07902F既然已经归队，\x01",
            "我就要竭尽全力。\x02\x03",

            "这不仅是为了完成国防军成员\x01",
            "或警备队员的职责，\x01",
            "更是为了履行守护克洛斯贝尔的使命。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4623")

    Jump("loc_469F")

    label("loc_4628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_469F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4643")
    Call(0, 45)
    Jump("loc_469F")

    label("loc_4643")


    #C0162
    ChrTalk(
        0x11,
        (
            "#07903F等我们整编好部队之后，\x01",
            "一定会随后赶上。\x02\x03",

            "#07901F各位……\x01",
            "那个笨蛋就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_469F")

    TalkEnd(0xFE)
    Return()

    # Function_28_42C6 end

    def Function_29_46A3(): pass

    label("Function_29_46A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B8")
    Call(0, 30)
    Jump("loc_4A3F")

    label("loc_46B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4904")

    #C0163
    ChrTalk(
        0x22,
        (
            "#02501F迪塔被拘捕所产生的影响\x01",
            "已经扩散到了自治州内外。\x02\x03",

            "即使事态能顺利平息，\x01",
            "今后也一定会有无数苦难\x01",
            "等待着克洛斯贝尔。\x02\x03",

            "#02503F……现在想想，对迪塔而言，\x01",
            "『克洛斯贝尔的未来』这份担子\x01",
            "或许太过沉重了。\x02\x03",

            "身为自治州代表之一，在事态发展到\x01",
            "如今这个地步之前，什么都没做……\x01",
            "这真是令我深切感受到了自己的无能。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        "#00108F外公……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        (
            "#00003F……这次的事情，\x01",
            "是整个克洛斯贝尔的\x01",
            "问题。\x02\x03",

            "#00000F今后到底该怎么做……\x01",
            "才是最重要的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x22,
        (
            "#02503F……嗯，你说的没错。\x02\x03",

            "#02500F总之，如今就先一一解决\x01",
            "眼前的问题吧。\x02\x03",

            "虽然你们这些年轻人\x01",
            "将会非常辛苦……\x01",
            "但请暂时助我一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 3)
    Jump("loc_4A3F")

    label("loc_4904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C8")

    #C0167
    ChrTalk(
        0x22,
        (
            "#02503F总之，如今就先一一解决\x01",
            "眼前的问题吧。\x02\x03",

            "#02500F身为克洛斯贝尔自治州的代表，\x01",
            "无论如何也要将此次事态平息。\x02\x03",

            "虽然你们这些年轻人\x01",
            "将会非常辛苦……\x01",
            "但请暂时助我一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A3F")

    label("loc_49C8")


    #C0168
    ChrTalk(
        0x22,
        (
            "#02503F总之，如今就先一一解决\x01",
            "眼前的问题吧。\x02\x03",

            "#02500F虽然你们这些年轻人\x01",
            "将会非常辛苦……\x01",
            "但请暂时助我一臂之力吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A3F")

    TalkEnd(0xFE)
    Return()

    # Function_29_46A3 end

    def Function_30_4A43(): pass

    label("Function_30_4A43")

    OP_4B(0x22, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x23, 0xFF)

    #C0169
    ChrTalk(
        0x22,
        (
            "#02503F总统被拘捕的消息\x01",
            "已经传遍各处了。\x02\x03",

            "#02500F对两大国的警戒\x01",
            "自然不可懈怠……\x01",
            "……不知各地现在的状况如何了。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x21,
        (
            "那棵『大树』的出现\x01",
            "在各地引起了混乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x21,
        (
            "另外，由于结界已经消失，\x01",
            "有很多市民希望前往\x01",
            "乌尔斯拉医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x21,
        (
            "关于这些问题，米蕾优三尉\x01",
            "已经做出了指示。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x11,
        (
            "#07903F关于出入市区的问题，\x01",
            "我们已经在郊外各条大道增派了小队，\x01",
            "用以护卫往来的车辆。\x02\x03",

            "#07900F相比受总统管制的时期，\x01",
            "如今可以运送数倍于当时的市民。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x22,
        (
            "#02503F唔，感谢你们的迅速应对。\x02\x03",

            "#02500F我身为自治州议会的议长，\x01",
            "有必要公开解释\x01",
            "拘捕总统一事。\x02\x03",

            "现在已经安排市民会馆\x01",
            "去做召开见面会的准备……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x23,
        (
            "#01002F关于此事，可以使用\x01",
            "总统当时准备的直播车辆。\x02\x03",

            "我这就委托市内的警察\x01",
            "帮忙准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x22,
        (
            "#02503F不好意思，麻烦你们了。\x02\x03",

            "#02501F对两大国的警戒不可懈怠……\x01",
            "诸位请多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#00001F（麦克道尔议长他们\x01",
            "  似乎正在忙着处理\x01",
            "  各方面的问题。）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        (
            "#00100F（这里的事情就交给\x01",
            "  外公他们吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x22, 0xFF)
    OP_4C(0x21, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x23, 0xFF)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x21, 0x10)
    ClearChrFlags(0x22, 0x10)
    ClearChrFlags(0x23, 0x10)
    SetScenarioFlags(0x1AE, 1)
    Return()

    # Function_30_4A43 end

    def Function_31_4DD9(): pass

    label("Function_31_4DD9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DEE")
    Call(0, 30)
    Jump("loc_5223")

    label("loc_4DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50BC")

    #C0179
    ChrTalk(
        0x23,
        (
            "#01002F是你们啊……\x01",
            "怎么？发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00000F不，只是有点在意\x01",
            "这边的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x23,
        (
            "#01003F哦，如你所见，\x01",
            "正在与各方人士探讨今后的对策。\x02\x03",

            "#01001F我是作为警察的联络员\x01",
            "被派到这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EFD")

    #C0182
    ChrTalk(
        0x10A,
        (
            "#00604F嗯……\x01",
            "赛尔盖长官很适合这项任务呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2A")

    label("loc_4EFD")


    #C0183
    ChrTalk(
        0x103,
        "#00204F原来如此，科长很适合这项任务呢。\x02",
    )

    CloseMessageWindow()

    label("loc_4F2A")


    #C0184
    ChrTalk(
        0x104,
        (
            "#00300F这么一来……\x01",
            "支援科那边就没人了吧，\x01",
            "不会接到什么委托吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x23,
        (
            "#01002F虽然接到了来自各地的\x01",
            "不少委托，\x01",
            "但已经全部交给游击士协会了。\x02\x03",

            "#01004F你们不必担心\x01",
            "委托的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x103,
        "#00205F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00104F既然交给了游击士协会，\x01",
            "我们也就可以放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x23,
        (
            "#01004F总之，你们就放手去干吧，\x01",
            "直到自己满意为止。\x02\x03",

            "#01002F这不仅是为了『特别任务支援科』……\x01",
            "更是为了你们自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        "#00002F是……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 4)
    Jump("loc_5223")

    label("loc_50BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51AB")

    #C0190
    ChrTalk(
        0x23,
        (
            "#01003F……哦，对了，总统\x01",
            "被拘禁在了兰花塔三十六层的\x01",
            "某个房间里。\x02\x03",

            "由于现状，他的押送被推迟了。\x01",
            "总统并没有抵抗的意图，\x01",
            "所以只安排了最低限度的守卫人员。\x02\x03",

            "#01002F要是想去看看他，可以直接上去，\x01",
            "你们应该有不少话想问吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5223")

    label("loc_51AB")


    #C0191
    ChrTalk(
        0x23,
        (
            "#01003F总统被拘禁在了兰花塔\x01",
            "三十六层的某个房间里。\x02\x03",

            "#01002F要是想去看看他，可以直接上去，\x01",
            "你们应该有不少话想问吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5223")

    TalkEnd(0xFE)
    Return()

    # Function_31_4DD9 end

    def Function_32_5227(): pass

    label("Function_32_5227")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523C")
    Call(0, 30)
    Jump("loc_562A")

    label("loc_523C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E8")

    #C0192
    ChrTalk(
        0x104,
        (
            "#00300F道格拉斯老兄，\x01",
            "你到这里来了啊？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52A1")

    #C0193
    ChrTalk(
        0x109,
        "#10100F您辛苦了，副司令！\x02",
    )

    CloseMessageWindow()

    label("loc_52A1")


    #C0194
    ChrTalk(
        0xFE,
        (
            "是你们啊。\x01",
            "哈哈，好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "我是应索妮亚司令的要求，\x01",
            "以国防军代表的身份\x01",
            "而来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#00005F原来如此。\x02\x03",

            "#00000F话说回来……\x01",
            "好像还是第一次看您身穿国防军的制服呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "哈哈，相比警备队的制服，\x01",
            "感觉稍微有些死板……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "不过，在事态平息到一定程度之前，\x01",
            "应该会一直穿着它行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00103F……看来目前的情况\x01",
            "不太妙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "是啊……笼罩着市区的结界\x01",
            "和那几架『神机』都消失了，\x01",
            "如今更要加强对两大国的警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "……不过，他们也不至于\x01",
            "立刻就发动侵略，\x01",
            "这些事就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "你们只要做好只有你们\x01",
            "才能做到的事情就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "那警戒的事就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 5)
    Jump("loc_562A")

    label("loc_54E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55BD")

    #C0204
    ChrTalk(
        0xFE,
        (
            "自从接到总统被拘捕的报告之后，\x01",
            "司令就时常露出一副\x01",
            "若有所思的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "……她是个责任感很强的人。\x01",
            "连同自己今后的去留问题在内，\x01",
            "她肯定思考了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "我身为副司令，现在必须要\x01",
            "好好支持她。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_562A")

    label("loc_55BD")


    #C0207
    ChrTalk(
        0xFE,
        (
            "两大国也不至于\x01",
            "立刻就发动侵略，\x01",
            "这些事就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "你们只要做好只有你们\x01",
            "才能做到的事情就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562A")

    TalkEnd(0xFE)
    Return()

    # Function_32_5227 end

    def Function_33_562E(): pass

    label("Function_33_562E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5781")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_568F")

    #C0209
    ChrTalk(
        0x109,
        "#10105F啊……\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#00005F支援科的车……\x01",
            "被挪到这里了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56C3")

    label("loc_568F")


    #C0211
    ChrTalk(
        0x101,
        (
            "#00005F啊……\x02\x03",

            "支援科的车……\x01",
            "被挪到这里了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56C3")


    #C0212
    ChrTalk(
        0x102,
        (
            "#00106F虽然很可怜……\x01",
            "但暂时似乎也只能\x01",
            "把它放在这里了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x104,
        (
            "#00306F嗯，在这种状况下，\x01",
            "也只能这样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x103,
        (
            "#00202F等事情告一段落之后，\x01",
            "一定要把它修好。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#00000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 6)
    Jump("loc_583E")

    label("loc_5781")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57ED")

    #C0216
    ChrTalk(
        0x109,
        (
            "#10100F等事件结束之后，\x01",
            "一定要修好它。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        "#00004F嗯……辛苦了，暂时休息一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_583E")

    label("loc_57ED")


    #C0218
    ChrTalk(
        0x101,
        (
            "#00000F等事件结束之后，\x01",
            "一定要修好它。\x02\x03",

            "#00004F……辛苦了，暂时休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_583E")

    TalkEnd(0xFF)
    Return()

    # Function_33_562E end

    def Function_34_5842(): pass

    label("Function_34_5842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5853")
    Jump("loc_5B11")

    label("loc_5853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5901")

    #C0219
    ChrTalk(
        0xFE,
        (
            "在遭到袭击的时候，\x01",
            "我和女儿就在这个广场……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "听到去大楼避难的指示时，\x01",
            "我真的以为自己死定了。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "真不知该如何感谢\x01",
            "死守这里的亚里欧斯先生\x01",
            "和那些警员。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B11")

    label("loc_5901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_596B")

    #C0222
    ChrTalk(
        0xFE,
        (
            "今天的天气这么好，却发生了\x01",
            "占领事件，真是令人悲伤啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "到底为什么\x01",
            "会发生这种事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B11")

    label("loc_596B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5979")
    Jump("loc_5B11")

    label("loc_5979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_59BE")

    #C0224
    ChrTalk(
        0xFE,
        "嗯，马上就到中午了。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "吃一些带来的\x01",
            "三明治吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B11")

    label("loc_59BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A17")

    #C0226
    ChrTalk(
        0xFE,
        "呵呵，今天的天气也不错。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "在晴朗天空的映照下，\x01",
            "兰花塔显得更美了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B11")

    label("loc_5A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5A81")

    #C0228
    ChrTalk(
        0xFE,
        (
            "呵呵，这个广场\x01",
            "真是个很棒的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "虽然离繁华市区有些远，\x01",
            "但不知不觉就走到这里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B11")

    label("loc_5A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5A8F")
    Jump("loc_5B11")

    label("loc_5A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B11")

    #C0230
    ChrTalk(
        0xFE,
        (
            "呵呵，真让人难以想象\x01",
            "这里刚刚才举行过揭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "这么棒的地方，竟然从第一天\x01",
            "就开始向民众开放，\x01",
            "迪塔市长真是大方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B11")

    TalkEnd(0xFE)
    Return()

    # Function_34_5842 end

    def Function_35_5B15(): pass

    label("Function_35_5B15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5B26")
    Jump("loc_5CD8")

    label("loc_5B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B7C")

    #C0232
    ChrTalk(
        0xFE,
        (
            "听说一个叫亚里欧斯的人\x01",
            "和众多警察\x01",
            "保护了我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "真是非常感谢¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CD8")

    label("loc_5B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5BBC")

    #C0234
    ChrTalk(
        0xFE,
        (
            "妈妈今天好像\x01",
            "心事重重的。\x01",
            "希望她打起精神……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD8")

    label("loc_5BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5BCA")
    Jump("loc_5CD8")

    label("loc_5BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5BF2")

    #C0235
    ChrTalk(
        0xFE,
        "吃饭，吃饭，吃午饭¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CD8")

    label("loc_5BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5C2F")

    #C0236
    ChrTalk(
        0xFE,
        (
            "天气，天气，好天气¤\x01",
            "下雨，下雨，别下雨¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD8")

    label("loc_5C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C71")

    #C0237
    ChrTalk(
        0xFE,
        (
            "嘿嘿，今天又和妈妈\x01",
            "一起来这里散步了。\x01",
            "啦啦啦¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD8")

    label("loc_5C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C7F")
    Jump("loc_5CD8")

    label("loc_5C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5CD8")

    #C0238
    ChrTalk(
        0xFE,
        (
            "抬头看了看\x01",
            "兰花塔的塔顶，\x01",
            "脖子好痛好痛。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        "好痛好痛，好痛好痛，痛痛痛¤\x02",
    )

    CloseMessageWindow()

    label("loc_5CD8")

    TalkEnd(0xFE)
    Return()

    # Function_35_5B15 end

    def Function_36_5CDC(): pass

    label("Function_36_5CDC")

    TalkBegin(0xFE)

    #C0240
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "呼～～～～～～～～～\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        "……美得简直让人说不出话来。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_5CDC end

    def Function_37_5D38(): pass

    label("Function_37_5D38")

    TalkBegin(0xFE)

    #C0242
    ChrTalk(
        0xFE,
        (
            "嗯～确实无法\x01",
            "用语言来形容。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        "让人震撼得都陷入忘我状态了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_5D38 end

    def Function_38_5D82(): pass

    label("Function_38_5D82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5DFA")

    #C0244
    ChrTalk(
        0xFE,
        (
            "玛因兹那边好像\x01",
            "出了什么大事。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "虽然还不清楚是怎么回事……\x01",
            "但趁着没被卷进去，\x01",
            "还是赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF7")

    label("loc_5DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5E08")
    Jump("loc_5EF7")

    label("loc_5E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5E3D")

    #C0246
    ChrTalk(
        0xFE,
        (
            "好，差不多也该\x01",
            "回市区吃个午饭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF7")

    label("loc_5E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5E95")

    #C0247
    ChrTalk(
        0xFE,
        (
            "听说兰花塔的塔顶\x01",
            "还没向一般民众开放。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "唔，真遗憾。\x01",
            "下次再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF7")

    label("loc_5E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5EF7")

    #C0249
    ChrTalk(
        0xFE,
        (
            "我是来看传说中的\x01",
            "兰花塔的……\x01",
            "比想象中还要壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔\x01",
            "到底有多富有啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EF7")

    TalkEnd(0xFE)
    Return()

    # Function_38_5D82 end

    def Function_39_5EFB(): pass

    label("Function_39_5EFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5F5D")

    #C0251
    ChrTalk(
        0xFE,
        "那个女孩是克洛斯贝尔警备队的人吧？\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "真漂亮啊……\x01",
            "她也要拿着武器作战吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6042")

    label("loc_5F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5F6B")
    Jump("loc_6042")

    label("loc_5F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5FC8")

    #C0253
    ChrTalk(
        0xFE,
        "这么一说，肚子还真是饿了啊。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "呵呵，待在这里，\x01",
            "不知不觉就会忘记时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6042")

    label("loc_5FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6004")

    #C0255
    ChrTalk(
        0xFE,
        "啊啊～把塔顶的景色藏起来，不让人看吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6042")

    label("loc_6004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6042")

    #C0256
    ChrTalk(
        0xFE,
        (
            "哇～离近一看，感觉果然和\x01",
            "在远处眺望时完全不同。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6042")

    TalkEnd(0xFE)
    Return()

    # Function_39_5EFB end

    def Function_40_6046(): pass

    label("Function_40_6046")

    TalkBegin(0xFE)

    #C0257
    ChrTalk(
        0xFE,
        (
            "唔，雨下得这么大，\x01",
            "看不清塔顶呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_6046 end

    def Function_41_6074(): pass

    label("Function_41_6074")

    TalkBegin(0xFE)

    #C0258
    ChrTalk(
        0xFE,
        (
            "特意来看，结果却是这样，真扫兴。\x01",
            "真是的，为什么要下雨啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_6074 end

    def Function_42_60BA(): pass

    label("Function_42_60BA")

    TalkBegin(0xFE)

    #C0259
    ChrTalk(
        0xFE,
        (
            "呵呵，不管看多少次，\x01",
            "都觉得这座建筑很了不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "虽然并不是同一类型，\x01",
            "但『四轮之塔』恐怕都无法和它一较高下吧？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_60BA end

    def Function_43_6137(): pass

    label("Function_43_6137")

    TalkBegin(0xFE)

    #C0261
    ChrTalk(
        0xFE,
        (
            "兰花塔的存在感真是惊人，\x01",
            "就算无法看到，都能\x01",
            "感受到它的存在。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "被破坏的ＩＢＣ\x01",
            "和被守住了的城市新象征……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "唔，这真的只是\x01",
            "偶然吗……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_6137 end

    def Function_44_61D0(): pass

    label("Function_44_61D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, 650, 0, -19420, 0)
    SetChrPos(0x104, -650, 0, -19720, 0)
    SetChrPos(0x102, -1790, 0, -20140, 0)
    SetChrPos(0x103, 1630, 0, -20020, 0)
    OP_68(-1230, 2770, -21620, 0)
    MoveCamera(29, 31, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10240, 0)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch41800.itc", 0x20)
    SetChrChipByIndex(0x62, 0x1E)
    SetChrChipByIndex(0x63, 0x1F)
    SetChrChipByIndex(0x64, 0x1F)
    SetChrChipByIndex(0x65, 0x1E)
    SetChrChipByIndex(0x66, 0x20)
    SetChrChipByIndex(0x67, 0x1E)
    SetChrChipByIndex(0x68, 0x1F)
    SetChrChipByIndex(0x69, 0x1E)
    SetChrChipByIndex(0x6A, 0x1F)
    SetChrPos(0x62, -3160, 0, -12800, 180)
    SetChrPos(0x63, 3160, 0, -12800, 180)
    SetChrPos(0x64, -3140, 0, 25000, 180)
    SetChrPos(0x65, 2740, 0, 25240, 180)
    SetChrPos(0x66, -10520, 0, 3070, 180)
    SetChrPos(0x67, 5320, 250, 6840, 180)
    SetChrPos(0x68, -21660, 300, -7560, 180)
    SetChrPos(0x69, 21300, 300, 21000, 180)
    SetChrPos(0x6A, 14560, 0, 5730, 180)
    ClearChrFlags(0x62, 0x80)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x66, 0x4)
    ClearChrFlags(0x68, 0x4)
    ClearChrFlags(0x69, 0x4)
    ClearChrFlags(0x6A, 0x4)
    SetChrFlags(0x62, 0x8000)
    SetChrFlags(0x63, 0x8000)
    SetChrFlags(0x64, 0x8000)
    SetChrFlags(0x65, 0x8000)
    SetChrFlags(0x66, 0x8000)
    SetChrFlags(0x67, 0x8000)
    SetChrFlags(0x68, 0x8000)
    SetChrFlags(0x69, 0x8000)
    SetChrFlags(0x6A, 0x8000)
    BeginChrThread(0x62, 1, 0, 0)
    BeginChrThread(0x63, 1, 0, 0)
    BeginChrThread(0x64, 1, 0, 0)
    BeginChrThread(0x65, 1, 0, 0)
    BeginChrThread(0x66, 1, 0, 4)
    BeginChrThread(0x67, 1, 0, 0)
    BeginChrThread(0x68, 1, 0, 5)
    BeginChrThread(0x69, 1, 0, 6)
    BeginChrThread(0x6A, 1, 0, 7)
    ClearChrFlags(0x75, 0x80)
    ClearChrFlags(0x75, 0x4)
    OP_78(0xC, 0x75)
    SetChrPos(0x75, 7330, 250, 8180, 225)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_D5(0x75, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFrame(0xC, "mark00", 0x0, 0x1)
    ClearChrFlags(0x76, 0x80)
    ClearChrFlags(0x76, 0x4)
    OP_78(0xE, 0x76)
    SetChrPos(0x76, -7220, 250, 8270, 135)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    OP_D5(0x76, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFrame(0xE, "mark00", 0x0, 0x1)
    FadeToBright(2000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0264
    ChrTalk(
        0x101,
        "#12P#00005F这是……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(0, 3400, 30670, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(19000, 0)
    Fade(1000)
    OP_68(0, 3400, 1770, 8000)
    MoveCamera(0, 9, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(19000, 8000)
    Sleep(8000)
    OP_68(-3770, 2500, 3480, 0)
    MoveCamera(60, 30, 0, 0)
    OP_6E(990, 0)
    SetCameraDistance(19000, 0)
    Fade(1000)
    OP_68(3510, 2500, 3790, 6000)
    MoveCamera(300, 30, 0, 6000)
    OP_6E(990, 6000)
    SetCameraDistance(19000, 6000)
    Sleep(6000)
    OP_68(0, 3400, -6240, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(19000, 0)
    Fade(1000)
    OP_68(-1230, 2770, -21620, 4000)
    MoveCamera(29, 31, 0, 4000)
    OP_6E(750, 4000)
    SetCameraDistance(10240, 4000)
    Sleep(4500)

    #C0265
    ChrTalk(
        0x104,
        (
            "#12P#00301F『国防军』的人\x01",
            "正在兰花塔的\x01",
            "前方严密戒备……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x102,
        (
            "#6P#00108F毕竟是迪塔叔叔发表独立宣言的地方，\x01",
            "这种程度的警备也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x62, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_4B(0x62, 0x1)

    #C0267
    ChrTalk(
        0x62,
        (
            "咦，你……\x01",
            "你不是兰迪吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_95(0x62, -1340, 0, -17100, 2000, 0x0)
    OP_93(0x101, 0x13B, 0x1F4)
    OP_93(0x103, 0x13B, 0x1F4)

    #C0268
    ChrTalk(
        0x104,
        (
            "#00305F#12P这不是卡塔吗！\x02\x03",

            "#00302F哈哈，穿着这身白军服，\x01",
            "我都认不出来了。\x02\x03",

            "你不是被分到\x01",
            "贝尔加德门了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x62,
        (
            "哦，因为总统要发表演说，\x01",
            "从边境大门调来很多人\x01",
            "做警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x62,
        (
            "罗金斯也在那边\x01",
            "巡逻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x104,
        "#00302F#12P哈哈，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        "#00000F#12P（这个人是……）\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        (
            "#00100F#6P（兰迪在警备队时的\x01",
            "  同僚吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x62,
        (
            "哎呀，话说回来，\x01",
            "事情还真是惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x62,
        (
            "我们突然领到\x01",
            "这种军服时，\x01",
            "实在是吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        (
            "#00306F#12P嗯，太过突然了，\x01",
            "让人完全搞不懂……\x02\x03",

            "#00300F仔细想想，竟然连军服这种东西都准备好了，\x01",
            "这未免也太过周全了。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x62,
        (
            "总统肯定从很久之前\x01",
            "就开始做准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x62,
        (
            "国防军的装备\x01",
            "也有希望得到强化，\x01",
            "我们一定要打起精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#00305F#12P嗯……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x103,
        (
            "#00201F#12P（……国防军的士兵们\x01",
            "  似乎很高兴地\x01",
            "  接受了这次的重编呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        (
            "#00106F#6P（相比其它国家的正规军，\x01",
            "  他们一直都很不得志，\x01",
            "  这种心情也不难理解……）\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x62,
        (
            "顺便一提，由于改组为国防军，\x01",
            "我们的军阶也换成了\x01",
            "一般军队中所用的通用名称。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x62,
        (
            "一尉、二尉、三尉变成了\x01",
            "大尉、中尉、少尉。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x62,
        (
            "在称呼士官的时候，要是叫错了军阶，\x01",
            "可是非常失礼的行为，一定要注意。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#00300F#12P嗯，多谢忠告。\x02\x03",

            "#00303F也就是说，米蕾优那家伙\x01",
            "以前是『三尉』……\x01",
            "但以后就要改叫她『少尉』了。\x02\x03",

            "#00309F哈哈，又多了一个可以用来戏弄她的话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        "#00006F#12P喂喂……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x62,
        (
            "呃～那个……\x01",
            "算了，没什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0288
    ChrTalk(
        0x104,
        (
            "#00305F#12P什么嘛，\x01",
            "怎么欲言又止的……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#00105F#12P应该没有\x01",
            "叫错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x62,
        "不，并不是这个问题啦……\x02",
    )

    CloseMessageWindow()
    OP_63(0x62, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x62)

    #C0291
    ChrTalk(
        0x62,
        (
            "那个，兰迪，\x01",
            "其实……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x6A, 0x1)
    TurnDirection(0x6A, 0x62, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("国防军士官的声音")

    #C0292
    ChrTalk(
        0x6A,
        (
            "#4S……卡塔！！\x01",
            "值班时不要闲聊！！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x62, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_93(0x62, 0x2D, 0x1F4)

    #C0293
    ChrTalk(
        0x62,
        "……是、是！！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x6A, 0x1)
    TurnDirection(0x62, 0x104, 300)

    #C0294
    ChrTalk(
        0x62,
        (
            "……抱歉，兰迪，\x01",
            "下次再跟你细说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        (
            "#00300F#12P不太明白你的意思……但这次都怪我主动\x01",
            "过来搭话，才害你挨骂，真是抱歉啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x62,
        "哈哈，别在意。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x62,
        (
            "对了，你们警察\x01",
            "也被编进国防军了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x62,
        (
            "咱们今后又是同事了，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x62, -3160, 0, -12800, 2000, 0x0)
    OP_93(0x62, 0xB4, 0x12C)
    OP_4C(0x62, 0x1)

    #C0299
    ChrTalk(
        0x104,
        (
            "#00306F#12P哎呀呀……\x01",
            "净说些让人在意的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        (
            "#00201F#12P我们暂且\x01",
            "回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#00001F#12P嗯，走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_68(0, 2770, -13870, 5000)
    MoveCamera(0, 7, 0, 5000)
    OP_6E(750, 5000)
    SetCameraDistance(19000, 5000)

    def lambda_6F4B():

        label("loc_6F4B")

        TurnDirection(0x62, 0x104, 500)
        Yield()
        Jump("loc_6F4B")

    QueueWorkItem2(0x62, 2, lambda_6F4B)
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_6F64():

        label("loc_6F64")

        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_6F64")

    QueueWorkItem2(0x101, 1, lambda_6F64)
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_6F85():

        label("loc_6F85")

        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_6F85")

    QueueWorkItem2(0x104, 1, lambda_6F85)
    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_6FA6():

        label("loc_6FA6")

        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_6FA6")

    QueueWorkItem2(0x103, 1, lambda_6FA6)
    OP_93(0x102, 0xB4, 0x1F4)

    def lambda_6FC7():

        label("loc_6FC7")

        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_6FC7")

    QueueWorkItem2(0x102, 1, lambda_6FC7)
    OP_0D()
    SetScenarioFlags(0x191, 4)
    EventEnd(0x6)
    NewScene("c1100", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_44_61D0 end

    def Function_45_6FEC(): pass

    label("Function_45_6FEC")

    EventBegin(0x0)
    OP_4B(0x11, 0xFF)
    Fade(500)
    OP_68(6100, 2500, 4460, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(8570, 0)
    OP_93(0x11, 0xE1, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x101, 5260, 250, 6290, 43)
    SetChrPos(0x102, 4290, 130, 6800, 45)
    SetChrPos(0x103, 5340, 250, 4840, 43)
    SetChrPos(0x109, 3390, 100, 5970, 43)
    SetChrPos(0x105, 4400, 190, 5200, 43)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0302
    ChrTalk(
        0x101,
        (
            "#6P#00001F米蕾优三尉……\x01",
            "你来市内了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x11,
        (
            "#07903F嗯，刚刚才到。\x02\x03",

            "#07900F司令和副司令还在开会，\x01",
            "我正在这里等他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        (
            "#6P#00103F就是科长从昨晚\x01",
            "一直开到现在的会吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#6P#00201F连警备队的司令\x01",
            "都留下了……\x01",
            "看来在制定对策时遇到了难题呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x11)

    #C0306
    ChrTalk(
        0x11,
        (
            "#07901F……各位，\x01",
            "你们科长今天早上\x01",
            "来问过我……\x02\x03",

            "听说兰迪\x01",
            "出走了？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        (
            "#6P#00003F……是的。\x02\x03",

            "#00001F他恐怕……\x01",
            "去了玛因兹\x01",
            "山道。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x11,
        "#07908F……是吗……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    #C0309
    ChrTalk(
        0x105,
        "#6P#10300F……没事吧？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x11,
        (
            "#07903F……嗯，我没事。\x01",
            "话说回来……\x02\x03",

            "#07901F兰迪会不辞而别，\x01",
            "应该和他的过去\x01",
            "有关吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        "#6P#00008F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x11,
        (
            "#07908F……虽然很不甘心，\x01",
            "但我并不太清楚\x01",
            "兰迪的过去。\x02\x03",

            "他一直不愿在实战训练中\x01",
            "使用来复枪的理由，\x01",
            "我也一直不了解。\x02\x03",

            "#07901F但是……我知道\x01",
            "他这次的愚蠢行为\x01",
            "害大家多么担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x109,
        "#6P#10108F米蕾优三尉……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#6P#00203F……确实，他真是傻瓜中的大傻瓜。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x11,
        (
            "#07903F……警备队遭受了重大损失。\x01",
            "接下来，司令他们将会\x01",
            "重新编组救援部队。\x02\x03",

            "在那之前，我们无法擅自行动……\x01",
            "不能为了兰迪一人\x01",
            "提早出动。\x02\x03",

            "#07900F所以……\x01",
            "那个笨蛋就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#6P#00000F……交给我们吧。\x01",
            "我们一定会找回兰迪的……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x11, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x16F, 4)
    EventEnd(0x5)
    Return()

    # Function_45_6FEC end

    def Function_46_74F9(): pass

    label("Function_46_74F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31200.itc", 0x1E)
    LoadChrToIndex("chr/ch31300.itc", 0x1F)
    LoadChrToIndex("chr/ch44900.itc", 0x20)
    SetChrChipByIndex(0x48, 0x0)
    SetChrSubChip(0x48, 0x0)
    ClearChrFlags(0x48, 0x80)
    SetChrFlags(0x48, 0x8000)
    SetChrPos(0x48, -2500, 0, 22800, 180)
    BeginChrThread(0x48, 0, 0, 0)
    SetChrChipByIndex(0x49, 0x0)
    SetChrSubChip(0x49, 0x0)
    ClearChrFlags(0x49, 0x80)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, 2500, 0, 22800, 180)
    BeginChrThread(0x49, 0, 0, 0)
    SetChrChipByIndex(0x4A, 0x0)
    SetChrSubChip(0x4A, 0x0)
    ClearChrFlags(0x4A, 0x80)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, 2000, 0, -19500, 180)
    BeginChrThread(0x4A, 0, 0, 0)
    SetChrChipByIndex(0x4B, 0x0)
    SetChrSubChip(0x4B, 0x0)
    ClearChrFlags(0x4B, 0x80)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, -2000, 0, -19500, 180)
    BeginChrThread(0x4B, 0, 0, 0)
    SetChrChipByIndex(0x4C, 0x0)
    SetChrSubChip(0x4C, 0x0)
    ClearChrFlags(0x4C, 0x80)
    SetChrFlags(0x4C, 0x8000)
    SetChrPos(0x4C, 21700, 300, 19000, 180)
    BeginChrThread(0x4C, 0, 0, 47)
    SetChrChipByIndex(0x4D, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x4D, 0x80)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x4D, -21700, 300, -6000, 0)
    BeginChrThread(0x4D, 0, 0, 48)
    SetChrChipByIndex(0x4E, 0x0)
    SetChrSubChip(0x4E, 0x0)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4E, 0x4)
    SetChrFlags(0x4E, 0x8000)
    SetChrPos(0x4E, -19000, 0, 5500, 90)
    BeginChrThread(0x4E, 0, 0, 49)
    SetChrChipByIndex(0x4F, 0x0)
    SetChrSubChip(0x4F, 0x0)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x4F, 0x4)
    SetChrFlags(0x4F, 0x8000)
    SetChrPos(0x4F, 19000, 0, 5500, 270)
    BeginChrThread(0x4F, 0, 0, 50)
    SetChrChipByIndex(0x47, 0x20)
    SetChrSubChip(0x47, 0x0)
    ClearChrFlags(0x47, 0x80)
    SetChrFlags(0x47, 0x8000)
    SetChrPos(0x47, 0, 240, -800, 180)
    SetChrChipByIndex(0x52, 0x1E)
    SetChrSubChip(0x52, 0x0)
    ClearChrFlags(0x52, 0x80)
    SetChrFlags(0x52, 0x8000)
    SetChrPos(0x52, -2100, 0, -3500, 0)
    SetChrChipByIndex(0x53, 0x1F)
    SetChrSubChip(0x53, 0x0)
    ClearChrFlags(0x53, 0x80)
    SetChrFlags(0x53, 0x8000)
    SetChrPos(0x53, -700, 0, -3500, 0)
    SetChrChipByIndex(0x54, 0x1E)
    SetChrSubChip(0x54, 0x0)
    ClearChrFlags(0x54, 0x80)
    SetChrFlags(0x54, 0x8000)
    SetChrPos(0x54, 700, 0, -3500, 0)
    SetChrChipByIndex(0x55, 0x1F)
    SetChrSubChip(0x55, 0x0)
    ClearChrFlags(0x55, 0x80)
    SetChrFlags(0x55, 0x8000)
    SetChrPos(0x55, 2100, 0, -3500, 0)
    SetChrChipByIndex(0x56, 0x1F)
    SetChrSubChip(0x56, 0x0)
    ClearChrFlags(0x56, 0x80)
    SetChrFlags(0x56, 0x8000)
    SetChrPos(0x56, -2100, 0, -4900, 0)
    SetChrChipByIndex(0x57, 0x1E)
    SetChrSubChip(0x57, 0x0)
    ClearChrFlags(0x57, 0x80)
    SetChrFlags(0x57, 0x8000)
    SetChrPos(0x57, -700, 0, -4900, 0)
    SetChrChipByIndex(0x58, 0x1F)
    SetChrSubChip(0x58, 0x0)
    ClearChrFlags(0x58, 0x80)
    SetChrFlags(0x58, 0x8000)
    SetChrPos(0x58, 700, 0, -4900, 0)
    SetChrChipByIndex(0x59, 0x1E)
    SetChrSubChip(0x59, 0x0)
    ClearChrFlags(0x59, 0x80)
    SetChrFlags(0x59, 0x8000)
    SetChrPos(0x59, 2100, 0, -4900, 0)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0317
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "『西塞姆里亚通商会议』──\x02\x03",

            "这场邀请了各国首脑的国际会议\x01",
            "即将在新市长迪塔·库罗伊斯的\x01",
            "提议之下正式召开。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7111", 0)
    OP_68(0, 1000, -20000, 0)
    MoveCamera(40, 30, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(15000, 0)
    OP_68(0, 1000, 0, 9000)
    MoveCamera(0, 30, 0, 9000)
    SetCameraDistance(30000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 5500, 25000, 0)
    MoveCamera(0, -5, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(38000, 0)
    OP_68(0, 20500, 25000, 15000)
    MoveCamera(0, -20, 0, 15000)
    SetCameraDistance(48000, 15000)
    OP_0D()
    Sleep(3000)
    FadeToDark(300, 0, 100)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0318
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "另外，刚刚竣工的新市政厅大楼\x01",
            "也将同时举行揭幕式。\x02\x03",

            "──通称『兰花塔』。\x02\x03",

            "高达二百五十亚矩，共计四十层，\x01",
            "是大陆有史以来第一座超高层建筑，\x01",
            "如今在大陆之中广受瞩目。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_74F9 end

    def Function_47_7A32(): pass

    label("Function_47_7A32")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A7E")
    OP_95(0xFE, 21700, 300, -6000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 21700, 300, 19000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Jump("Function_47_7A32")

    label("loc_7A7E")

    Return()

    # Function_47_7A32 end

    def Function_48_7A7F(): pass

    label("Function_48_7A7F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7ACB")
    OP_95(0xFE, -21700, 300, 19000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, -21700, 300, -6000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    Jump("Function_48_7A7F")

    label("loc_7ACB")

    Return()

    # Function_48_7A7F end

    def Function_49_7ACC(): pass

    label("Function_49_7ACC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B18")
    OP_95(0xFE, -7000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -19000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Jump("Function_49_7ACC")

    label("loc_7B18")

    Return()

    # Function_49_7ACC end

    def Function_50_7B19(): pass

    label("Function_50_7B19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B65")
    OP_95(0xFE, 7000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Jump("Function_50_7B19")

    label("loc_7B65")

    Return()

    # Function_50_7B19 end

    def Function_51_7B66(): pass

    label("Function_51_7B66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10900.itc", 0x1E)
    LoadChrToIndex("chr/ch12400.itc", 0x1F)
    LoadChrToIndex("chr/ch11100.itc", 0x20)
    LoadChrToIndex("chr/ch11300.itc", 0x21)
    LoadChrToIndex("chr/ch11000.itc", 0x22)
    LoadChrToIndex("chr/ch11200.itc", 0x23)
    LoadChrToIndex("chr/ch11800.itc", 0x24)
    LoadChrToIndex("chr/ch11700.itc", 0x25)
    LoadChrToIndex("chr/ch13300.itc", 0x26)
    LoadChrToIndex("chr/ch05600.itc", 0x27)
    LoadChrToIndex("chr/ch05500.itc", 0x28)
    LoadChrToIndex("chr/ch05800.itc", 0x29)
    LoadChrToIndex("chr/ch25800.itc", 0x2A)
    LoadChrToIndex("chr/ch27800.itc", 0x2B)
    LoadChrToIndex("chr/ch41000.itc", 0x2C)
    LoadChrToIndex("chr/ch41200.itc", 0x2D)
    LoadChrToIndex("chr/ch41600.itc", 0x2E)
    SoundLoad(468)
    SoundLoad(924)
    SoundLoad(835)
    SoundLoad(851)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    CreatePortrait(2, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis520.itp")
    CreatePortrait(3, 16, 200, 528, 264, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis521.itp")
    LoadEffect(0x1, "event\\ev12031.eff")
    LoadEffect(0x2, "event\\ev12030.eff")
    SetChrPos(0x101, 18200, 0, 5400, 270)
    SetChrPos(0x102, 18200, 0, 6600, 270)
    SetChrPos(0x104, 19300, 0, 7100, 270)
    SetChrPos(0x109, 19300, 0, 4900, 270)
    SetChrPos(0x105, 19700, 0, 6000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x5C, 0x2C)
    SetChrSubChip(0x5C, 0x0)
    ClearChrFlags(0x5C, 0x80)
    SetChrFlags(0x5C, 0x8000)
    SetChrPos(0x5C, 3600, 250, 500, 0)
    SetChrChipByIndex(0x5D, 0x2C)
    SetChrSubChip(0x5D, 0x0)
    ClearChrFlags(0x5D, 0x80)
    SetChrFlags(0x5D, 0x8000)
    SetChrPos(0x5D, 2500, 250, 500, 0)
    SetChrChipByIndex(0x5E, 0x2D)
    SetChrSubChip(0x5E, 0x0)
    ClearChrFlags(0x5E, 0x80)
    SetChrFlags(0x5E, 0x8000)
    SetChrPos(0x5E, 550, 250, 500, 0)
    SetChrChipByIndex(0x5F, 0x2D)
    SetChrSubChip(0x5F, 0x0)
    ClearChrFlags(0x5F, 0x80)
    SetChrFlags(0x5F, 0x8000)
    SetChrPos(0x5F, -550, 250, 500, 0)
    SetChrChipByIndex(0x60, 0x2E)
    SetChrSubChip(0x60, 0x0)
    ClearChrFlags(0x60, 0x80)
    SetChrFlags(0x60, 0x8000)
    SetChrPos(0x60, -2500, 250, 500, 0)
    SetChrChipByIndex(0x61, 0x2E)
    SetChrSubChip(0x61, 0x0)
    ClearChrFlags(0x61, 0x80)
    SetChrFlags(0x61, 0x8000)
    SetChrPos(0x61, -3600, 250, 500, 0)
    SetChrChipByIndex(0x27, 0x1E)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 1200, 100, 4400, 0)
    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 600, 100, 3100, 0)
    SetChrChipByIndex(0x29, 0x20)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 2500, 100, 4100, 325)
    SetChrChipByIndex(0x2A, 0x21)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 3500, 100, 4700, 330)
    SetChrChipByIndex(0x2B, 0x22)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, -2800, 100, 4900, 70)
    SetChrChipByIndex(0x2C, 0x23)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -3500, 100, 5500, 75)
    SetChrChipByIndex(0x2D, 0x24)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 3300, 100, 6700, 270)
    SetChrChipByIndex(0x2E, 0x25)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, -700, 100, 4300, 0)
    SetChrChipByIndex(0x2F, 0x26)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, -1650, 100, 3700, 15)
    SetChrChipByIndex(0x30, 0x27)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, -1000, 100, 7200, 180)
    SetChrChipByIndex(0x31, 0x28)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, -1600, 100, 8200, 180)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 1300, 100, 6500, 160)
    SetChrChipByIndex(0x5B, 0x2A)
    SetChrSubChip(0x5B, 0x0)
    ClearChrFlags(0x5B, 0x80)
    SetChrFlags(0x5B, 0x8000)
    SetChrPos(0x5B, 600, 100, 7100, 160)
    SetChrChipByIndex(0x5A, 0x2B)
    SetChrSubChip(0x5A, 0x0)
    ClearChrFlags(0x5A, 0x80)
    SetChrFlags(0x5A, 0x8000)
    SetChrPos(0x5A, 4300, 100, 6400, 270)
    SetChrChipByIndex(0x48, 0x0)
    SetChrSubChip(0x48, 0x0)
    ClearChrFlags(0x48, 0x80)
    SetChrFlags(0x48, 0x8000)
    SetChrPos(0x48, 14000, 0, 8000, 270)
    SetChrChipByIndex(0x49, 0x0)
    SetChrSubChip(0x49, 0x0)
    ClearChrFlags(0x49, 0x80)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, 14000, 0, 4000, 270)
    SetChrChipByIndex(0x4A, 0x0)
    SetChrSubChip(0x4A, 0x0)
    ClearChrFlags(0x4A, 0x80)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, 14000, 0, 21000, 180)
    SetChrChipByIndex(0x4B, 0x0)
    SetChrSubChip(0x4B, 0x0)
    ClearChrFlags(0x4B, 0x80)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, 14000, 0, -6000, 315)
    SetChrChipByIndex(0x4C, 0x0)
    SetChrSubChip(0x4C, 0x0)
    ClearChrFlags(0x4C, 0x80)
    SetChrFlags(0x4C, 0x8000)
    SetChrPos(0x4C, -14000, 0, 8000, 90)
    SetChrChipByIndex(0x4D, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x4D, 0x80)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x4D, -14000, 0, 4000, 90)
    SetChrChipByIndex(0x4E, 0x0)
    SetChrSubChip(0x4E, 0x0)
    ClearChrFlags(0x4E, 0x80)
    SetChrFlags(0x4E, 0x8000)
    SetChrPos(0x4E, -14000, 0, 21000, 180)
    SetChrChipByIndex(0x4F, 0x0)
    SetChrSubChip(0x4F, 0x0)
    ClearChrFlags(0x4F, 0x80)
    SetChrFlags(0x4F, 0x8000)
    SetChrPos(0x4F, -14000, 0, -6000, 45)
    SetChrChipByIndex(0x50, 0x0)
    SetChrSubChip(0x50, 0x0)
    ClearChrFlags(0x50, 0x80)
    SetChrFlags(0x50, 0x8000)
    SetChrPos(0x50, -2500, 0, -12000, 180)
    SetChrChipByIndex(0x51, 0x0)
    SetChrSubChip(0x51, 0x0)
    ClearChrFlags(0x51, 0x80)
    SetChrFlags(0x51, 0x8000)
    SetChrPos(0x51, 2500, 0, -12000, 180)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x71, 0x4)
    OP_78(0xA, 0x71)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x71, 0, -15500, -83500, 0)
    OP_D5(0x71, 0xFFFFC568, 0x0, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x72, 0x4)
    SetMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x72)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x72, 0, -15500, -83500, 0)
    OP_D5(0x72, 0xFFFFC568, 0x0, 0x0, 0x0)
    SetMapObjFlags(0xB, 0x1000)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_68(0, -8500, -55000, 0)
    MoveCamera(20, -8, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, -500, -30000, 10000)
    MoveCamera(0, -8, 0, 10000)
    SetCameraDistance(24000, 10000)

    def lambda_824F():
        OP_98(0xFE, 0x0, 0x0, 0xEA60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x71, 1, lambda_824F)
    BeginChrThread(0x79, 1, 0, 55)
    FadeToBright(2000, 0)
    Sleep(3000)
    ClearMapObjFlags(0xB, 0x4)

    def lambda_8281():
        OP_98(0xFE, 0x0, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x72, 1, lambda_8281)
    Sleep(1000)
    Sound(494, 0, 80, 0)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xA, 0x4)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    StopSound(468, 1000, 100)
    StopSound(924, 1000, 20)
    Sleep(1000)
    OP_68(0, 900, 5700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(24000, 0)
    Sound(835, 2, 50, 0)
    Sound(851, 2, 50, 0)
    MoveCamera(30, 23, 0, 7000)
    SetCameraDistance(14000, 7000)
    FadeToBright(2000, 0)
    BeginChrThread(0x27, 3, 0, 54)
    Sleep(300)
    BeginChrThread(0x22, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x29, 3, 0, 54)
    Sleep(300)
    BeginChrThread(0x30, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x2E, 3, 0, 54)
    Sleep(300)
    BeginChrThread(0x2B, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x2D, 3, 0, 54)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 52)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(1300, 1000, 6500, 0)
    MoveCamera(27, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)

    def lambda_83AA():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_83AA)
    SetCameraDistance(12500, 2000)
    OP_0D()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(2500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CC(0x0, 0x2, 0x3)

    def lambda_845C():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_845C)
    OP_68(-1000, 1000, 6200, 2500)
    MoveCamera(9, 27, 0, 2500)
    SetCameraDistance(13500, 2500)
    OP_6F(0x79)
    Sleep(500)

    def lambda_8493():
        TurnDirection(0xFE, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_8493)
    SetCameraDistance(12500, 2000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(2500)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)

    def lambda_8544():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_8544)
    Fade(500)
    OP_68(19650, 900, 6530, 0)
    MoveCamera(53, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16340, 0)
    SetCameraDistance(15340, 1500)
    OP_4B(0x101, 0x3)
    OP_0D()
    OP_6F(0x79)

    #C0319
    ChrTalk(
        0x101,
        "#11P#00011F（……好、好惊人………）\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x102,
        (
            "#00104F#5P（嗯……全都是治理着整个国家的人，\x01",
            "  果然不同凡响啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#00301F#5P（话说回来，他就是『铁血宰相』啊……\x01",
            "  实在是器宇不凡。）\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x105,
        (
            "#11P#10302F（呵呵，共和国的总统就像个\x01",
            "  难以捉摸的老狐狸。）\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x109,
        (
            "#11P#10102F（利贝尔的科洛蒂娅王太女\x01",
            "  真是美丽端庄……）\x02\x03",

            "#10109F（……而且，竟然能在这里见到\x01",
            "  尤莉亚准校……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(500)
    EndChrThread(0x27, 0xFF)
    OP_64(0x27)
    EndChrThread(0x22, 0xFF)
    OP_64(0x22)
    EndChrThread(0x29, 0xFF)
    OP_64(0x29)
    EndChrThread(0x30, 0xFF)
    OP_64(0x30)
    EndChrThread(0x2E, 0xFF)
    OP_64(0x2E)
    EndChrThread(0x2B, 0xFF)
    OP_64(0x2B)
    EndChrThread(0x2D, 0xFF)
    OP_64(0x2D)
    SetChrPos(0x30, 0, 100, 6800, 180)
    SetChrPos(0x31, -900, 100, 8000, 180)
    SetChrPos(0x22, 1500, 100, 8200, 180)
    SetChrPos(0x5B, 2500, 100, 8200, 180)

    def lambda_8789():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_8789)

    def lambda_8796():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_8796)

    def lambda_87A3():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_87A3)

    def lambda_87B0():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_87B0)

    def lambda_87BD():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_87BD)

    def lambda_87CA():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_87CA)

    def lambda_87D7():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_87D7)

    def lambda_87E4():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_87E4)
    OP_68(70, 1000, 7670, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15500, 0)
    OP_4C(0x101, 0x3)
    SetCameraDistance(14000, 2000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0324
    ChrTalk(
        0x30,
        (
            "#02804F#5P──各位首脑。\x02\x03",

            "#02800F感谢大家长途跋涉莅临\x01",
            "克洛斯贝尔，我在此表示衷心欢迎。\x02\x03",

            "我是克洛斯贝尔市的市长——\x01",
            "迪塔·库罗伊斯。\x02",
        )
    )

    CloseMessageWindow()
    Sound(968, 0, 70, 0)
    Sleep(2500)

    #C0325
    ChrTalk(
        0x30,
        (
            "#02804F#5P承蒙诸位前来参加『西塞姆里亚通商会议』，\x01",
            "实在是万分感谢。\x02\x03",

            "按照惯例，我本该在致欢迎辞的同时\x01",
            "宣布大会开幕。\x02\x03",

            "#02800F但在这个值得纪念的日子，\x01",
            "请允许我占用各位的一点时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0x3)
    OP_68(-1330, 4700, 14630, 3000)
    MoveCamera(28, 2, 0, 3000)
    OP_6E(750, 3000)
    SetCameraDistance(15500, 3000)
    OP_93(0x30, 0x0, 0x1F4)
    Sleep(500)

    def lambda_89B8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_89B8)

    def lambda_89C5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_89C5)
    Sleep(50)

    def lambda_89D5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_89D5)

    def lambda_89E2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_89E2)
    Sleep(50)

    def lambda_89F2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_89F2)

    def lambda_89FF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_89FF)
    Sleep(50)

    def lambda_8A0F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_8A0F)

    def lambda_8A1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_8A1C)
    Sleep(50)

    def lambda_8A2C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_8A2C)

    def lambda_8A39():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5A, 2, lambda_8A39)
    Sleep(50)

    def lambda_8A49():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_8A49)

    def lambda_8A56():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_8A56)

    def lambda_8A63():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5B, 2, lambda_8A63)
    WaitChrThread(0x31, 2)
    OP_6F(0x79)
    Sleep(500)

    #C0326
    ChrTalk(
        0x30,
        (
            "#02803F#N#11P接下来，我要向大家介绍——\x02\x03",

            "克洛斯贝尔市的新市政厅。\x02\x03",

            "它将是贸易金融都市\x01",
            "克洛斯贝尔市的全新象征。\x02\x03",

            "#02800F更是为整个大陆的和平与繁荣\x01",
            "做出贡献的国际交流中心。\x02\x03",

            "接下来，大陆有史以来\x01",
            "第一座超高层建筑——\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0327
    ChrTalk(
        0x30,
        "#02809F#N#4S#11P『兰花塔』正式揭幕！\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7550", 0)
    OP_68(0, 12300, 8000, 5000)
    MoveCamera(0, -27, 0, 5000)
    SetCameraDistance(21500, 5000)
    Sleep(3000)
    StopSound(835, 1000, 50)
    StopSound(851, 1000, 50)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_02.pmf", 0x226, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    SetMapObjFlags(0x9, 0x4)
    OP_93(0x101, 0x14A, 0x0)
    OP_93(0x102, 0x14A, 0x0)
    OP_93(0x104, 0x14A, 0x0)
    OP_93(0x109, 0x14A, 0x0)
    OP_93(0x105, 0x14A, 0x0)
    OP_4C(0x101, 0x3)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 0, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, 3000, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -3000, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0xFF, 0x0, 5000, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x5, 0xFF, 0x0, -5000, 0, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(0, 2300, 8000, 5000)
    MoveCamera(0, 11, 0, 5000)
    SetCameraDistance(15500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Sound(967, 0, 100, 0)
    Fade(500)
    OP_68(19080, 11500, 6140, 0)
    MoveCamera(331, -63, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(19080, 11300, 6140, 3000)
    MoveCamera(330, -70, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15000, 3000)
    OP_6F(0x79)

    #C0328
    ChrTalk(
        0x101,
        (
            "#00011F#N这、这就是……\x01",
            "『兰花塔』……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0329
    ChrTalk(
        0x102,
        (
            "#00102F#N虽然之前就已经了解了基本信息，\x01",
            "但没想到会如此壮丽……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0330
    ChrTalk(
        0x109,
        (
            "#6P#10111F#N光、光是看着它，\x01",
            "就要震撼到窒息了……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0331
    ChrTalk(
        0x104,
        (
            "#00306F#N难以置信……\x01",
            "到底花了多少钱啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0332
    ChrTalk(
        0x105,
        (
            "#12P#10302F#N呵呵，一定投入了\x01",
            "天文数字的米拉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x101, 0x3)
    Fade(500)
    OP_68(3720, 1100, 4019, 0)
    MoveCamera(141, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 0, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, 3000, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -3000, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0xFF, 0x0, 5000, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x5, 0xFF, 0x0, -5000, -10000, 15000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)

    #C0333
    ChrTalk(
        0x29,
        (
            "#07205F#11P（哎呀呀……\x01",
            "  真是令人惊叹。）\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x2A,
        (
            "#07303F#5P（……技术的进步\x01",
            "  确实值得赞叹啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-3710, 1100, 5280, 2500)
    MoveCamera(216, 31, 0, 2500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0335
    ChrTalk(
        0x2B,
        (
            "#07000F#5P（……让我不由得\x01",
            "  想起了利贝尔·方舟呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x2C,
        (
            "#07104F#5P（嗯……虽然还及不上\x01",
            "  中枢塔的高度……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1460, 1100, 3570, 1500)
    MoveCamera(180, 27, 0, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0337
    ChrTalk(
        0x2E,
        (
            "#07511F#5P（哈哈哈，\x01",
            "  真是相当豪气啊！）\x02\x03",

            "#07510F（之前就看过你发给我的报告了，\x01",
            "  但没想到会如此壮观！）\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x2F,
        (
            "#12004F#11P（嗯，我也没想到\x01",
            "  实物会如此雄伟。）\x02\x03",

            "#12000F（真不愧是资产雄厚的\x01",
            "  ＩＢＣ啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1170, 1100, 3330, 1500)
    MoveCamera(136, 26, 0, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0339
    ChrTalk(
        0x27,
        (
            "#07404F#11P（呵呵，实在是了不起。）\x02\x03",

            "#07400F（竟在这因缘之地\x01",
            "  建起了如此庞然大物。）\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x28,
        (
            "#11509F#11P（唔，真想登上塔顶\x01",
            "  看看啊。）\x02\x03",

            "#11502F（去求求市长的话，\x01",
            "  他会让咱们上去吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(70, 1000, 7670, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    OP_93(0x30, 0xB4, 0x1F4)
    Sleep(300)

    def lambda_9388():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_9388)

    def lambda_9395():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_9395)

    def lambda_93A2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5B, 2, lambda_93A2)
    Sleep(50)

    def lambda_93B2():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_93B2)

    def lambda_93BF():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_93BF)
    Sleep(50)

    def lambda_93CF():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_93CF)

    def lambda_93DC():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_93DC)
    Sleep(50)

    def lambda_93EC():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_93EC)

    def lambda_93F9():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_93F9)
    Sleep(50)

    def lambda_9409():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_9409)

    def lambda_9416():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_9416)
    Sleep(50)

    def lambda_9426():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_9426)

    def lambda_9433():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x5A, 2, lambda_9433)
    OP_6F(0x79)
    Sleep(500)

    #C0341
    ChrTalk(
        0x30,
        (
            "#02804F那么……\x02\x03",

            "我再次向在场的各位首脑和\x01",
            "各位来宾宣布──\x02\x03",

            "#02800F『西塞姆里亚通商会议』\x01",
            "正式开始！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 53)
    Sound(820, 0, 100, 0)
    Sound(968, 0, 100, 0)
    SetCameraDistance(17500, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_7B66 end

    def Function_52_94F1(): pass

    label("Function_52_94F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95A9")
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_955C")
    Sleep(500)
    Jump("loc_95A4")

    label("loc_955C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9573")
    Sleep(1000)
    Jump("loc_95A4")

    label("loc_9573")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_958A")
    Sleep(150)
    Jump("loc_95A4")

    label("loc_958A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_95A1")
    Sleep(2000)
    Jump("loc_95A4")

    label("loc_95A1")

    Sleep(2500)

    label("loc_95A4")

    Jump("Function_52_94F1")

    label("loc_95A9")

    Return()

    # Function_52_94F1 end

    def Function_53_95AA(): pass

    label("Function_53_95AA")

    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_53_95AA end

    def Function_54_9728(): pass

    label("Function_54_9728")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_974D")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(4000)
    Jump("Function_54_9728")

    label("loc_974D")

    Return()

    # Function_54_9728 end

    def Function_55_974E(): pass

    label("Function_55_974E")

    Sound(457, 0, 80, 0)
    Sound(468, 2, 20, 0)
    Sound(924, 2, 0, 0)
    Sleep(100)
    OP_25(0x1D4, 0x1E)
    Sleep(100)
    OP_25(0x1D4, 0x28)
    OP_25(0x39C, 0x5)
    Sleep(100)
    OP_25(0x1D4, 0x32)
    Sleep(100)
    OP_25(0x1D4, 0x3C)
    OP_25(0x39C, 0xA)
    Sleep(100)
    OP_25(0x1D4, 0x46)
    Sleep(100)
    OP_25(0x1D4, 0x50)
    OP_25(0x39C, 0xF)
    Sleep(100)
    OP_25(0x1D4, 0x5A)
    Sleep(100)
    OP_25(0x1D4, 0x64)
    OP_25(0x39C, 0x14)
    Return()

    # Function_55_974E end

    def Function_56_97A9(): pass

    label("Function_56_97A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 950, 0, -16620, 0)
    SetChrPos(0x102, -750, 0, -16720, 0)
    SetChrPos(0x104, -1690, 0, -17640, 0)
    SetChrPos(0x105, 280, 0, -17860, 0)
    SetChrPos(0x109, 1930, 0, -17220, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_68(0, 20000, -14480, 0)
    MoveCamera(0, -59, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(2000, 0)
    OP_68(0, 5300, -14480, 8000)
    MoveCamera(0, 2, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(19000, 8000)
    Sleep(8500)
    OP_68(-2230, 2500, 14840, 0)
    MoveCamera(43, 37, 0, 0)
    OP_6E(870, 0)
    SetCameraDistance(22500, 0)
    Fade(500)
    OP_68(-2029, 2500, -13510, 8000)
    MoveCamera(43, 37, 0, 8000)
    OP_6E(870, 8000)
    SetCameraDistance(22500, 8000)
    Sleep(8500)
    Fade(500)
    OP_68(-990, 2500, -18610, 0)
    MoveCamera(33, 33, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10170, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    OP_0D()
    Sleep(1500)

    #C0342
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，真热闹。\x02\x03",

            "隆和亨利他们\x01",
            "好像也来玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        (
            "#00100F揭幕式结束，各国首脑\x01",
            "离开之后，这个广场立刻就\x01",
            "对市民们开放了。\x02\x03",

            "#00104F呵呵，这就是迪塔叔叔的\x01",
            "体贴之处吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x109,
        (
            "#10109F哈哈，真符合迪塔市长的作风。\x02\x03",

            "#10100F话说回来，这里的警察还真多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x105,
        (
            "#10304F#4P嗯，全市居民现在\x01",
            "都处于兴奋状态。\x02\x03",

            "#10300F在这种情况下，很容易产生纠纷，\x01",
            "所以才会加强警备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#00003F嗯，塔内似乎还\x01",
            "禁止入内。\x02\x03",

            "#00000F我们现在\x01",
            "也不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15E, 6)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, 0, 0, -17130, 0)
    EventEnd(0x5)
    Return()

    # Function_56_97A9 end

    def Function_57_9B72(): pass

    label("Function_57_9B72")

    EventBegin(0x1)

    #C0347
    ChrTalk(
        0x101,
        (
            "#00000F今天好像禁止\x01",
            "一般市民进入塔内。\x02\x03",

            "我们现在\x01",
            "也不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 0, 25470, 180)
    EventEnd(0x4)
    Return()

    # Function_57_9B72 end

    def Function_58_9BD0(): pass

    label("Function_58_9BD0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, -1500, -25000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(20500, 0)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_90(0x101, 500, 0, -31700, 0)
    OP_90(0x102, -500, 0, -31700, 0)
    OP_90(0x103, 1200, 0, -33400, 0)
    OP_90(0x104, -1200, 0, -33400, 0)
    OP_90(0x109, -700, 0, -34700, 0)
    OP_90(0x105, 700, 0, -34700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x10000000)

    def lambda_9C98():
        OP_97(0x105, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9C98)
    Sleep(100)

    def lambda_9CB5():
        OP_97(0x109, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9CB5)
    Sleep(100)

    def lambda_9CD2():
        OP_97(0x103, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9CD2)
    Sleep(100)

    def lambda_9CEF():
        OP_97(0x104, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9CEF)
    Sleep(100)

    def lambda_9D0C():
        OP_97(0x101, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9D0C)
    Sleep(100)

    def lambda_9D29():
        OP_97(0x102, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9D29)
    OP_68(0, -500, -25000, 7000)
    SetCameraDistance(15500, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x102, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 20000, -9000, 0)
    MoveCamera(0, -55, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(12000, 0)
    OP_68(0, 3000, -18000, 7000)
    MoveCamera(0, 0, 0, 7000)
    OP_6F(0x79)
    Sleep(300)

    #C0348
    ChrTalk(
        0x103,
        (
            "#00206F#11P昨晚在空港降落前，\x01",
            "我就看到了这座建筑\x01",
            "灯光闪烁的样子……\x02\x03",

            "#00202F但还是在离近仰望之后，\x01",
            "才深刻感受到了它的巨大。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#00004F#11P哈哈……我理解你的心情。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x109,
        (
            "#10102F#5P不愧是克洛斯贝尔的\x01",
            "新标志性建筑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x104,
        (
            "#00306F#5P不过，这么高的建筑，\x01",
            "到底要做什么用啊？\x02\x03",

            "#00301F比起之前的市政厅，\x01",
            "未免也太高了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x102,
        (
            "#00104F#5P这座建筑内具有\x01",
            "各种各样的功能。\x02\x03",

            "#00100F除了本市和自治州的行政场所之外，\x01",
            "还包含了国际贸易中心\x01",
            "与文化交流专用的楼层。\x02\x03",

            "甚至可以说，建造它的目的\x01",
            "便是使其成为大陆西部的中心。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x104,
        (
            "#00305F#5P呼……\x01",
            "听起来真宏大。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x109,
        (
            "#10100F#5P听你这样一说，\x01",
            "也就不难理解这次的通商会议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x105,
        (
            "#10304F#11P这座建筑竣工之后，\x01",
            "资本和信息向克洛斯贝尔汇集的速度\x01",
            "恐怕会进一步提升。\x02\x03",

            "#10300F在这场会议中，恐怕也会\x01",
            "基于这样的前景\x01",
            "而展开讨论吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x102,
        (
            "#00104F#5P嗯，我听说是这样的。\x02\x03",

            "#00108F不过，会议的论题恐怕\x01",
            "并不会局限于经济方面……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 900, -17650, 0)
    MoveCamera(6, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17100, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0357
    ChrTalk(
        0x101,
        (
            "#00003F#11P那么，接下来怎么办？\x02\x03",

            "#00001F我们和达德利警官有约，\x01",
            "中午要在一层的\x01",
            "入口大厅会合。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A1AF():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A1AF)
    Sleep(50)

    def lambda_A1BF():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A1BF)
    Sleep(50)

    def lambda_A1CF():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A1CF)
    Sleep(50)

    def lambda_A1DF():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A1DF)
    Sleep(50)

    def lambda_A1EF():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A1EF)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A25B")

    #C0358
    ChrTalk(
        0x102,
        (
            "#00108F#5P是啊……\x01",
            "不过还有时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A286")

    label("loc_A25B")


    #C0359
    ChrTalk(
        0x102,
        (
            "#00105F#5P是啊……\x01",
            "不过还有不少时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A286")


    #C0360
    ChrTalk(
        0x104,
        (
            "#6P#00304F好啦，那就先把要办的事情办完，\x01",
            "做好充分准备吧。\x02\x03",

            "#00300F万一遇到什么特殊情况，也能从容应对。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x109,
        (
            "#6P#10106F说的对……\x01",
            "会议开始之后，\x01",
            "应该就不能出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x103,
        (
            "#12P#00202F那么，把要办的事情办完，\x01",
            "并做好准备工作之后再进去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, -19000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetScenarioFlags(0x141, 6)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_58_9BD0 end

    def Function_59_A3B9(): pass

    label("Function_59_A3B9")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1500, 26500, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 0, 0, 26000, 0)
    SetChrPos(0x102, -1000, 0, 25300, 0)
    SetChrPos(0x103, 1000, 0, 25300, 0)
    SetChrPos(0x104, 1100, 0, 23400, 0)
    SetChrPos(0x109, -1100, 0, 23400, 0)
    SetChrPos(0x105, 0, 0, 22700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A50D")

    #C0363
    ChrTalk(
        0x101,
        (
            "#00003F#5P（我们和达德利警官有约，\x01",
            "  中午要在一层的\x01",
            "  入口大厅会合……）\x02\x03",

            "#00001F（现在还有一些时间，\x01",
            "  要立刻进去吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A58F")

    label("loc_A50D")


    #C0364
    ChrTalk(
        0x101,
        (
            "#00003F#5P（我们和达德利警官有约，\x01",
            "  中午要在一层的\x01",
            "  入口大厅会合……）\x02\x03",

            "#00001F（现在还有不少时间，\x01",
            "  要提前进去等着吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A58F")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进入塔内之后，\x01",
            "就无法去商店调整装备、道具，\x01",
            "以及导力器了。\x02\x03",

            "另外，未完成的任务也将\x01",
            "全部终止，还请注意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它事情要办】\x01",      # 0
            "【进入兰花塔】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_A67D"),
        (0, "loc_A79F"),
        (SWITCH_DEFAULT, "loc_A7C9"),
    )


    label("loc_A67D")

    OP_68(0, 1500, 30500, 4000)
    MoveCamera(0, 7, 0, 4000)

    def lambda_A69E():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A69E)
    Sleep(50)

    def lambda_A6BB():
        OP_97(0x103, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A6BB)
    Sleep(50)

    def lambda_A6D8():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A6D8)
    Sleep(50)

    def lambda_A6F5():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A6F5)
    Sleep(50)

    def lambda_A712():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A712)
    Sleep(50)

    def lambda_A72F():
        OP_97(0x105, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A72F)
    Sleep(700)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("c1510", 0, 0, 0)
    IdleLoop()
    Jump("loc_A7C9")

    label("loc_A79F")

    SetChrPos(0x0, 0, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_A7C9")

    label("loc_A7C9")

    EventEnd(0x5)
    Return()

    # Function_59_A3B9 end

    def Function_60_A7CC(): pass

    label("Function_60_A7CC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "调查居民对迪塔市长提出的\x01",
            "『克洛斯贝尔独立』提案\x01",
            "意向的居民投票活动日渐临近。\x02\x03",

            "虽然帝国、共和国政府一直在\x01",
            "不断施加强大的压力，\x01",
            "但市民们仍然对此抱有高度关注……\x02\x03",

            "同时，恰逢彩虹剧团的\x01",
            "新版舞剧公演，\x01",
            "市内的热烈气氛更加高涨。\x02\x03",

            "就在此时，又有新的问题\x01",
            "发生在了荒无人烟的郊外。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7151", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 25000, 40000, 0)
    MoveCamera(335, -20, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(70000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    OP_68(0, 65000, 45000, 10000)
    MoveCamera(20, -35, 0, 10000)
    SetCameraDistance(120000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 170000, 45000, 0)
    MoveCamera(30, -45, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    OP_68(0, 175000, 45000, 5000)
    SetCameraDistance(60000, 5000)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_F0(0x0, 0xA)
    SetScenarioFlags(0x22, 4)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_A7CC end

    def Function_61_AA32(): pass

    label("Function_61_AA32")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27200.itc", 0x1E)
    LoadChrToIndex("chr/ch27300.itc", 0x1F)
    LoadChrToIndex("chr/ch32000.itc", 0x20)
    LoadChrToIndex("chr/ch32100.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis251.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis408.itp")
    SetChrChipByIndex(0x32, 0x1E)
    SetChrSubChip(0x32, 0x0)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x32, 0x4)
    SetChrFlags(0x32, 0x8000)
    SetChrPos(0x32, 550, 200, 32700, 0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x33, 0x1F)
    SetChrSubChip(0x33, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x33, 0x4)
    SetChrFlags(0x33, 0x8000)
    SetChrPos(0x33, 1200, 200, 33700, 0)
    OP_A7(0x33, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x34, 0x20)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x34, 0x4)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, -550, 200, 32700, 0)
    OP_A7(0x34, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x35, 0x21)
    SetChrSubChip(0x35, 0x0)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x35, 0x4)
    SetChrFlags(0x35, 0x8000)
    SetChrPos(0x35, -1200, 200, 33700, 0)
    OP_A7(0x35, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 900, 31000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -550, 0, 32400, 180)
    SetChrPos(0x102, 550, 0, 32400, 180)
    SetChrPos(0x103, -1200, 0, 33400, 180)
    SetChrPos(0x104, 1200, 0, 33400, 180)
    SetChrPos(0x109, -700, 0, 34400, 180)
    SetChrPos(0x105, 700, 0, 34400, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(24000, 8500)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0x32, 3, 0, 62)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 63)
    Sleep(3000)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x32, 0)
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    EndChrThread(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    EndChrThread(0x34, 0xFF)
    SetChrSubChip(0x34, 0x0)
    EndChrThread(0x33, 0xFF)
    SetChrSubChip(0x33, 0x0)
    EndChrThread(0x35, 0xFF)
    SetChrSubChip(0x35, 0x0)
    Fade(500)
    OP_68(-280, 1500, 19760, 0)
    MoveCamera(127, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17530, 0)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetCameraDistance(16530, 1500)
    SetChrPos(0x101, -600, 0, 20400, 180)
    SetChrPos(0x102, 600, 0, 20400, 180)
    SetChrPos(0x103, -1000, 0, 21400, 180)
    SetChrPos(0x104, 1000, 0, 21400, 180)
    SetChrPos(0x109, -600, 0, 22400, 180)
    SetChrPos(0x105, 600, 0, 22400, 180)
    SetChrPos(0x32, 600, 0, 17700, 0)
    SetChrPos(0x33, 1100, 0, 16700, 0)
    SetChrPos(0x34, -600, 0, 17700, 0)
    SetChrPos(0x35, -1100, 0, 16700, 0)
    OP_0D()
    OP_6F(0x79)

    #C0367
    ChrTalk(
        0x34,
        (
            "#11P话说回来，真没想到\x01",
            "会以这种形式与你们联手。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x33,
        (
            "#11P呵……在最开始的时候，\x01",
            "真是无法想象啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#6P#00012F哈哈……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#00304F毕竟我们也有了\x01",
            "少许成长。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x32,
        "#11P哪里，应该说是很惊人的成长。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x32,
        (
            "#11P如果你们以后被警察局开除，\x01",
            "协会随时欢迎你们哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x35,
        "#11P是啊是啊！\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x35,
        (
            "#11P特别是小缇欧，应该很适合\x01",
            "在协会工作呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x35, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0375
    ChrTalk(
        0x103,
        "#6P#00211F就算你这么说……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        (
            "#00109F呵呵……\x01",
            "我们心领了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x109,
        (
            "#6P#10101F话说回来……\x01",
            "『幻兽』还真是很让人在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x32,
        (
            "#11P嗯，我们先来\x01",
            "分工吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x32,
        (
            "#11P来自警备队的委托\x01",
            "共有五件……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x32,
        (
            "#11P我希望你们\x01",
            "负责其中的两件。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0381
    ChrTalk(
        0x105,
        (
            "#10302F嘿，还真是\x01",
            "照顾我们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#6P#00005F这样好吗？\x01",
            "分给你们的是不是有些多……\x02\x03",

            "#00001F而且你们现在无法\x01",
            "调用亚里欧斯先生……\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x34,
        "#11P正因如此，才这样分配。\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x34,
        (
            "#11P由于他无法行动，\x01",
            "你们那边的委托肯定也会增多。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x35,
        (
            "#11P驱除魔兽本是我们\x01",
            "游击士擅长的工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x35,
        (
            "#11P大家都还有别的工作在身，\x01",
            "分配任务时应该注重效率。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#00104F……那就不客气了。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x109,
        (
            "#6P#10108F总、总觉得有点\x01",
            "不好意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x32,
        "#11P哪里，这是互相帮忙啦。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x32,
        (
            "#11P而且你们还要处理\x01",
            "『结社』的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        "#6P#00006F……是的。\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#00306F真是的……\x01",
            "那也是个大问题啊。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(120, 210, -1, -1)

    #A0393
    AnonymousTalk(
        0x103,
        (
            "#00203F结社『噬身之蛇』……\x02\x03",

            "#00201F他们似乎和游击士协会\x01",
            "也颇有因缘……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 200, -1, -1)

    #A0394
    AnonymousTalk(
        0x35,
        (
            "嗯，在利贝尔异变时，\x01",
            "结社曾和以艾丝蒂尔小姐\x01",
            "为代表的游击士们交过手……\x02\x03",

            "另外，在各地的事件中\x01",
            "也与我们有过不少次冲突。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 140, -1, -1)

    #A0395
    AnonymousTalk(
        0x33,
        (
            "……据说帝国协会遭到破坏，\x01",
            "一时陷入瘫痪的事情\x01",
            "也是他们所为。\x02\x03",

            "当然，帝国协会之后的衰退则是\x01",
            "由于军方施加的压力。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 190, -1, -1)

    #A0396
    AnonymousTalk(
        0x101,
        "#00001F是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(100, 210, -1, -1)

    #A0397
    AnonymousTalk(
        0x104,
        (
            "#00301F越听越觉得是一群\x01",
            "难以捉摸的对手了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    #C0398
    ChrTalk(
        0x32,
        (
            "#11P不管怎么说，『结社』可是连\x01",
            "游击士协会都未能调查清楚的组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x32,
        (
            "#11P目前还不知他们有何目的，\x01",
            "你们一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x34,
        (
            "#11P如果遇到什么困难，\x01",
            "请不要客气，随时联系我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x34,
        (
            "#11P既然牵扯到了『结社』，\x01",
            "对我们来说，也不是毫无关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        "#6P#00002F……我明白了。\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x102,
        (
            "#00104F要是有什么事情，\x01",
            "一定会拜托你们帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17030, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xA)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_61_AA32 end

    def Function_62_B68D(): pass

    label("Function_62_B68D")


    def lambda_B692():
        OP_97(0x32, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 0, lambda_B692)
    Sleep(50)

    def lambda_B6AF():
        OP_97(0x34, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 0, lambda_B6AF)
    Sleep(50)

    def lambda_B6CC():
        OP_97(0x33, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 0, lambda_B6CC)
    Sleep(50)

    def lambda_B6E9():
        OP_97(0x35, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 0, lambda_B6E9)

    def lambda_B703():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_B703)
    Sleep(100)

    def lambda_B717():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 2, lambda_B717)
    Sleep(400)

    def lambda_B72B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_B72B)
    Sleep(100)

    def lambda_B73F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_B73F)
    Return()

    # Function_62_B68D end

    def Function_63_B74C(): pass

    label("Function_63_B74C")


    def lambda_B751():
        OP_97(0x101, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B751)
    Sleep(50)

    def lambda_B76E():
        OP_97(0x102, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B76E)
    Sleep(50)

    def lambda_B78B():
        OP_97(0x103, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B78B)
    Sleep(50)

    def lambda_B7A8():
        OP_97(0x104, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B7A8)
    Sleep(50)

    def lambda_B7C5():
        OP_97(0x109, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B7C5)
    Sleep(50)

    def lambda_B7E2():
        OP_97(0x105, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B7E2)

    def lambda_B7FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B7FC)
    Sleep(100)

    def lambda_B810():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B810)
    Sleep(400)

    def lambda_B824():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B824)
    Sleep(100)

    def lambda_B838():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B838)
    Sleep(400)

    def lambda_B84C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B84C)
    Sleep(100)

    def lambda_B860():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B860)
    Return()

    # Function_63_B74C end

    def Function_64_B86D(): pass

    label("Function_64_B86D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("apl/ch51524.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch12200.itc", 0x21)
    LoadChrToIndex("chr/ch41400.itc", 0x22)
    LoadChrToIndex("chr/ch41500.itc", 0x23)
    LoadChrToIndex("chr/ch41800.itc", 0x24)
    LoadChrToIndex("chr/ch06000.itc", 0x25)
    LoadChrToIndex("chr/ch47900.itc", 0x26)
    LoadChrToIndex("apl/ch50314.itc", 0x27)
    LoadChrToIndex("chr/ch27400.itc", 0x28)
    LoadChrToIndex("chr/ch27800.itc", 0x29)
    LoadChrToIndex("chr/ch27900.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(851)
    SoundLoad(835)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11300.itp")
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x30, 0x1E)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 0, 10500, 35000, 180)
    OP_8E(0x30, "迪塔总统")
    SetChrChipByIndex(0x36, 0x20)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, -1400, 10380, 36500, 180)
    OP_52(0x36, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x36, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x36, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x47, 0x21)
    SetChrSubChip(0x47, 0x0)
    ClearChrFlags(0x47, 0x80)
    SetChrFlags(0x47, 0x8000)
    SetChrPos(0x47, -2500, 10380, 36500, 180)
    SetChrChipByIndex(0x63, 0x22)
    SetChrSubChip(0x63, 0x0)
    ClearChrFlags(0x63, 0x80)
    SetChrFlags(0x63, 0x8000)
    SetChrPos(0x63, -5500, 10380, 37000, 180)
    SetChrChipByIndex(0x64, 0x23)
    SetChrSubChip(0x64, 0x0)
    ClearChrFlags(0x64, 0x80)
    SetChrFlags(0x64, 0x8000)
    SetChrPos(0x64, 5500, 10380, 37000, 180)
    SetChrChipByIndex(0x65, 0x23)
    SetChrSubChip(0x65, 0x0)
    ClearChrFlags(0x65, 0x80)
    SetChrFlags(0x65, 0x8000)
    SetChrPos(0x65, -900, 0, 15500, 180)
    SetChrChipByIndex(0x66, 0x23)
    SetChrSubChip(0x66, 0x0)
    ClearChrFlags(0x66, 0x80)
    SetChrFlags(0x66, 0x8000)
    SetChrPos(0x66, -2300, 0, 15500, 180)
    SetChrChipByIndex(0x67, 0x24)
    SetChrSubChip(0x67, 0x0)
    ClearChrFlags(0x67, 0x80)
    SetChrFlags(0x67, 0x8000)
    SetChrPos(0x67, 900, 0, 15500, 180)
    SetChrChipByIndex(0x68, 0x24)
    SetChrSubChip(0x68, 0x0)
    ClearChrFlags(0x68, 0x80)
    SetChrFlags(0x68, 0x8000)
    SetChrPos(0x68, 2300, 0, 15500, 180)
    SetChrChipByIndex(0x69, 0x22)
    SetChrSubChip(0x69, 0x0)
    ClearChrFlags(0x69, 0x80)
    SetChrFlags(0x69, 0x8000)
    SetChrPos(0x69, -9800, 0, 14500, 135)
    SetChrChipByIndex(0x6A, 0x22)
    SetChrSubChip(0x6A, 0x0)
    ClearChrFlags(0x6A, 0x80)
    SetChrFlags(0x6A, 0x8000)
    SetChrPos(0x6A, 9800, 0, 14500, 225)
    SetChrChipByIndex(0x6B, 0x25)
    SetChrSubChip(0x6B, 0x0)
    ClearChrFlags(0x6B, 0x80)
    SetChrFlags(0x6B, 0x8000)
    SetChrPos(0x6B, 600, 250, 12600, 0)
    OP_4B(0x1F, 0xFF)
    SetChrChipByIndex(0x1F, 0x26)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -2000, 250, 12600, 0)
    SetChrChipByIndex(0x6C, 0x27)
    SetChrSubChip(0x6C, 0x0)
    ClearChrFlags(0x6C, 0x80)
    SetChrFlags(0x6C, 0x8000)
    SetChrPos(0x6C, 1700, 250, 12200, 0)
    SetChrChipByIndex(0x6D, 0x28)
    SetChrSubChip(0x6D, 0x0)
    ClearChrFlags(0x6D, 0x80)
    SetChrFlags(0x6D, 0x8000)
    SetChrPos(0x6D, -1700, 250, 10900, 0)
    SetChrChipByIndex(0x6E, 0x29)
    SetChrSubChip(0x6E, 0x0)
    ClearChrFlags(0x6E, 0x80)
    SetChrFlags(0x6E, 0x8000)
    SetChrPos(0x6E, 0, 250, 11300, 0)
    SetChrChipByIndex(0x6F, 0x2A)
    SetChrSubChip(0x6F, 0x0)
    ClearChrFlags(0x6F, 0x80)
    SetChrFlags(0x6F, 0x8000)
    SetChrPos(0x6F, -1000, 250, 12100, 0)
    SetChrChipByIndex(0x70, 0x2B)
    SetChrSubChip(0x70, 0x0)
    ClearChrFlags(0x70, 0x80)
    SetChrFlags(0x70, 0x8000)
    SetChrPos(0x70, 1200, 250, 10700, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 800, 100, 8300, 0)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2000, 100, 7300, 0)
    OP_4B(0x14, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 3100, 100, 8600, 0)
    OP_4B(0x15, 0xFF)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -800, 100, 8300, 0)
    OP_4B(0x16, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -2000, 100, 7300, 0)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -3100, 100, 8600, 0)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x10, 0x71)
    OP_49()
    SetChrPos(0x71, -8500, 0, 17000, 180)
    OP_D5(0x71, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    OP_74(0x10, 0x1E)
    OP_70(0x10, 0x0)
    ClearChrFlags(0x72, 0x80)
    OP_78(0x11, 0x72)
    OP_49()
    SetChrPos(0x72, 6500, 0, 17000, 180)
    OP_D5(0x72, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    OP_74(0x11, 0x1E)
    OP_70(0x11, 0x0)
    SetMapObjFlags(0x19, 0x1000)
    ClearMapObjFlags(0x19, 0x4)
    OP_68(0, 1500, 13000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15500, 0)
    Sound(851, 2, 50, 0)
    Sound(835, 2, 80, 0)
    BeginChrThread(0x6C, 0, 0, 65)
    SetCameraDistance(17500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1500, 13000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    OP_68(0, 11600, 34750, 6000)
    MoveCamera(30, 27, 0, 6000)
    SetCameraDistance(14000, 6000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 11500, 34750, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(13000, 0)
    SetChrChipByIndex(0x30, 0x1F)
    SetChrSubChip(0x30, 0x0)
    SetChrFlags(0x30, 0x10)
    SetChrFlags(0x30, 0x2)
    SetCameraDistance(12000, 3000)
    OP_6F(0x79)
    ClearChrFlags(0x30, 0x10)
    ClearChrFlags(0x30, 0x2)
    SetChrChipByIndex(0x30, 0x1E)
    SetChrSubChip(0x30, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0404
    AnonymousTalk(
        0x30,
        (
            "各位，你们好。\x02\x03",

            "我是刚刚就任为『克洛斯贝尔独立国』\x01",
            "第一任总统的\x01",
            "迪塔·库罗伊斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    PlayBGM("ed7566", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopSound(851, 1000, 50)
    StopSound(835, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c110D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_64_B86D end

    def Function_65_BF86(): pass

    label("Function_65_BF86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C03E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFB4")
    Sleep(500)
    Jump("loc_BFFC")

    label("loc_BFB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFCB")
    Sleep(1000)
    Jump("loc_BFFC")

    label("loc_BFCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFE2")
    Sleep(1500)
    Jump("loc_BFFC")

    label("loc_BFE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFF9")
    Sleep(2000)
    Jump("loc_BFFC")

    label("loc_BFF9")

    Sleep(2500)

    label("loc_BFFC")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 70, 0)
    Jump("Function_65_BF86")

    label("loc_C03E")

    Return()

    # Function_65_BF86 end

    def Function_66_C03F(): pass

    label("Function_66_C03F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("apl/ch51525.itc", 0x1F)
    LoadChrToIndex("chr/ch03800.itc", 0x20)
    LoadChrToIndex("chr/ch12200.itc", 0x21)
    LoadChrToIndex("chr/ch41400.itc", 0x22)
    LoadChrToIndex("chr/ch41500.itc", 0x23)
    LoadChrToIndex("chr/ch41800.itc", 0x24)
    LoadChrToIndex("chr/ch06000.itc", 0x25)
    LoadChrToIndex("chr/ch47900.itc", 0x26)
    LoadChrToIndex("apl/ch50314.itc", 0x27)
    LoadChrToIndex("chr/ch27400.itc", 0x28)
    LoadChrToIndex("chr/ch27800.itc", 0x29)
    LoadChrToIndex("chr/ch27900.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(821)
    SoundLoad(835)
    SoundLoad(4084)
    SoundLoad(4085)
    SoundLoad(4086)
    SoundLoad(4087)
    SoundLoad(4088)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10501.itp")
    CreatePortrait(1, 224, 0, 480, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10500.itp")
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x30, 0x1F)
    SetChrSubChip(0x30, 0x0)
    SetChrFlags(0x30, 0x10)
    SetChrFlags(0x30, 0x2)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 0, 10500, 35000, 180)
    OP_8E(0x30, "迪塔总统")
    SetChrChipByIndex(0x36, 0x20)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, -1400, 10380, 36500, 180)
    OP_52(0x36, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x36, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x36, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x47, 0x21)
    SetChrSubChip(0x47, 0x0)
    ClearChrFlags(0x47, 0x80)
    SetChrFlags(0x47, 0x8000)
    SetChrPos(0x47, -2500, 10380, 36500, 180)
    SetChrChipByIndex(0x63, 0x22)
    SetChrSubChip(0x63, 0x0)
    ClearChrFlags(0x63, 0x80)
    SetChrFlags(0x63, 0x8000)
    SetChrPos(0x63, -5500, 10380, 37000, 180)
    SetChrChipByIndex(0x64, 0x23)
    SetChrSubChip(0x64, 0x0)
    ClearChrFlags(0x64, 0x80)
    SetChrFlags(0x64, 0x8000)
    SetChrPos(0x64, 5500, 10380, 37000, 180)
    SetChrChipByIndex(0x65, 0x23)
    SetChrSubChip(0x65, 0x0)
    ClearChrFlags(0x65, 0x80)
    SetChrFlags(0x65, 0x8000)
    SetChrPos(0x65, -900, 0, 15500, 180)
    SetChrChipByIndex(0x66, 0x23)
    SetChrSubChip(0x66, 0x0)
    ClearChrFlags(0x66, 0x80)
    SetChrFlags(0x66, 0x8000)
    SetChrPos(0x66, -2300, 0, 15500, 180)
    SetChrChipByIndex(0x67, 0x24)
    SetChrSubChip(0x67, 0x0)
    ClearChrFlags(0x67, 0x80)
    SetChrFlags(0x67, 0x8000)
    SetChrPos(0x67, 900, 0, 15500, 180)
    SetChrChipByIndex(0x68, 0x24)
    SetChrSubChip(0x68, 0x0)
    ClearChrFlags(0x68, 0x80)
    SetChrFlags(0x68, 0x8000)
    SetChrPos(0x68, 2300, 0, 15500, 180)
    SetChrChipByIndex(0x69, 0x22)
    SetChrSubChip(0x69, 0x0)
    ClearChrFlags(0x69, 0x80)
    SetChrFlags(0x69, 0x8000)
    SetChrPos(0x69, -9800, 0, 14500, 135)
    SetChrChipByIndex(0x6A, 0x22)
    SetChrSubChip(0x6A, 0x0)
    ClearChrFlags(0x6A, 0x80)
    SetChrFlags(0x6A, 0x8000)
    SetChrPos(0x6A, 9800, 0, 14500, 225)
    SetChrChipByIndex(0x6B, 0x25)
    SetChrSubChip(0x6B, 0x0)
    ClearChrFlags(0x6B, 0x80)
    SetChrFlags(0x6B, 0x8000)
    SetChrPos(0x6B, 600, 250, 12600, 0)
    OP_4B(0x1F, 0xFF)
    SetChrChipByIndex(0x1F, 0x26)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -2000, 250, 12600, 0)
    SetChrChipByIndex(0x6C, 0x27)
    SetChrSubChip(0x6C, 0x0)
    ClearChrFlags(0x6C, 0x80)
    SetChrFlags(0x6C, 0x8000)
    SetChrPos(0x6C, 1700, 250, 12200, 0)
    SetChrChipByIndex(0x6D, 0x28)
    SetChrSubChip(0x6D, 0x0)
    ClearChrFlags(0x6D, 0x80)
    SetChrFlags(0x6D, 0x8000)
    SetChrPos(0x6D, -1700, 250, 10900, 0)
    SetChrChipByIndex(0x6E, 0x29)
    SetChrSubChip(0x6E, 0x0)
    ClearChrFlags(0x6E, 0x80)
    SetChrFlags(0x6E, 0x8000)
    SetChrPos(0x6E, 0, 250, 11300, 0)
    SetChrChipByIndex(0x6F, 0x2A)
    SetChrSubChip(0x6F, 0x0)
    ClearChrFlags(0x6F, 0x80)
    SetChrFlags(0x6F, 0x8000)
    SetChrPos(0x6F, -1000, 250, 12100, 0)
    SetChrChipByIndex(0x70, 0x2B)
    SetChrSubChip(0x70, 0x0)
    ClearChrFlags(0x70, 0x80)
    SetChrFlags(0x70, 0x8000)
    SetChrPos(0x70, 1200, 250, 10700, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x12, 0x2)
    SetChrSubChip(0x12, 0x0)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 800, 100, 8300, 0)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2000, 100, 7300, 0)
    OP_4B(0x14, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 3100, 100, 8600, 0)
    OP_4B(0x15, 0xFF)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -800, 100, 8300, 0)
    OP_4B(0x16, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -2000, 100, 7300, 0)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -3100, 100, 8600, 0)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x10, 0x71)
    OP_49()
    SetChrPos(0x71, -8500, 0, 17000, 180)
    OP_D5(0x71, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    OP_74(0x10, 0x1E)
    OP_70(0x10, 0x1)
    ClearChrFlags(0x72, 0x80)
    OP_78(0x11, 0x72)
    OP_49()
    SetChrPos(0x72, 6500, 0, 17000, 180)
    OP_D5(0x72, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    OP_74(0x11, 0x1E)
    OP_70(0x11, 0x1)
    SetMapObjFlags(0x19, 0x1000)
    ClearMapObjFlags(0x19, 0x4)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    BeginChrThread(0x6C, 0, 0, 65)
    OP_68(0, 5000, 19500, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(25000, 0)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    OP_68(0, 4000, 19500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    #C0405
    ChrTalk(
        0x30,
        (
            "#11303F#6P为此，\x01",
            "我今天才会\x01",
            "担任总统一职。\x02\x03",

            "#11300F当然，这只是为了\x01",
            "处理即将到来的危机\x01",
            "而采取的一时之策。\x02\x03",

            "#11304F我在此宣誓，一旦恢复和平，\x01",
            "我将立刻以选举的形式\x01",
            "倾听民意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 11400, 34500, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(13500, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x30, 0x1E)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x10)
    ClearChrFlags(0x30, 0x2)
    OP_0D()
    Sleep(300)
    TurnDirection(0x30, 0x36, 500)
    Sleep(150)

    #C0406
    ChrTalk(
        0x30,
        (
            "#11303F#11P接下来……\x02\x03",

            "#11300F还有一位大家所熟知的人，\x01",
            "将为新生的『克洛斯贝尔独立国』\x01",
            "贡献自己的力量。\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(27, 20, 0, 1500)
    SetCameraDistance(13000, 1500)
    BeginChrThread(0x30, 1, 0, 67)
    Sleep(300)
    BeginChrThread(0x36, 1, 0, 68)
    WaitChrThread(0x30, 1)
    WaitChrThread(0x36, 1)
    OP_93(0x30, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sleep(300)

    #C0407
    ChrTalk(
        0x30,
        (
            "#11304F#5P让我来介绍──\x02\x03",

            "在之前的克洛斯贝尔市\x01",
            "受袭事件中，奋勇守住了\x01",
            "兰花塔的人物……\x02\x03",

            "#11300F拥有『风之剑圣』之称，\x01",
            "曾经从属于游击士协会·克洛斯贝尔分部的\x01",
            "Ａ级游击士……\x02\x03",

            "#11309F『克洛斯贝尔国防军』司令长官，\x01",
            "亚里欧斯·马克莱因先生！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x50, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(1000)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x15E, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0408
    AnonymousTalk(
        0x36,
        (
            "#4084V承蒙总统介绍，\x01",
            "我是亚里欧斯·马克莱因。\x02\x03",

            "#4085V我资历尚浅，\x01",
            "恐怕会招致\x01",
            "各位的不安。\x02\x03",

            "#4086V但是，我在此与大家约定，\x01",
            "我将尽到比游击士时期更大的努力，\x01",
            "排除一切威胁到我国的势力。\x02\x03",

            "#4087V我会化为守护克洛斯贝尔的坚盾……\x02\x03",

            "#4088V以及打倒一切威胁正义与和平\x01",
            "之敌的利剑……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xFF8)
    VolumeBGM(0x64, 0x3E8)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    StopSound(851, 1000, 70)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 6)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_C03F end

    def Function_67_CAF5(): pass

    label("Function_67_CAF5")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_96(0xFE, 0x3E8, 0x2904, 0x88B8, 0x3E8, 0x0)
    Return()

    # Function_67_CAF5 end

    def Function_68_CB11(): pass

    label("Function_68_CB11")

    OP_95(0xFE, 0, 10380, 35600, 1500, 0x0)
    OP_95(0xFE, 0, 10500, 35000, 1500, 0x0)
    Return()

    # Function_68_CB11 end

    def Function_69_CB3A(): pass

    label("Function_69_CB3A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 25000, 40000, 0)
    MoveCamera(335, -20, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(70000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    OP_68(0, 65000, 45000, 8000)
    MoveCamera(20, -35, 0, 8000)
    SetCameraDistance(120000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 80000, 45000, 0)
    MoveCamera(35, -15, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    SetCameraDistance(60000, 4000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_F0(0x0, 0xA)
    SetScenarioFlags(0x22, 0)
    NewScene("c1560", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_69_CB3A end

    def Function_70_CC48(): pass

    label("Function_70_CC48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51719.itc", 0x0)
    LoadChrToIndex("apl/ch51718.itc", 0x1)
    LoadChrToIndex("chr/ch32050.itc", 0x2)
    LoadChrToIndex("chr/ch32051.itc", 0x3)
    LoadChrToIndex("chr/ch32052.itc", 0x4)
    LoadChrToIndex("chr/ch32056.itc", 0x5)
    LoadChrToIndex("chr/ch32150.itc", 0x6)
    LoadChrToIndex("chr/ch32151.itc", 0x7)
    LoadChrToIndex("chr/ch32152.itc", 0x8)
    LoadChrToIndex("monster/ch85150.itc", 0x9)
    LoadChrToIndex("monster/ch85151.itc", 0xA)
    LoadChrToIndex("monster/ch85153.itc", 0xB)
    LoadChrToIndex("monster/ch85152.itc", 0xC)
    LoadChrToIndex("apl/ch50509.itc", 0xD)
    LoadChrToIndex("apl/ch50506.itc", 0xE)
    LoadChrToIndex("chr/ch30200.itc", 0xF)
    LoadChrToIndex("apl/ch51720.itc", 0x10)
    LoadChrToIndex("chr/ch30500.itc", 0x11)
    LoadChrToIndex("chr/ch30100.itc", 0x12)
    LoadChrToIndex("chr/ch30000.itc", 0x13)
    LoadChrToIndex("apl/ch51236.itc", 0x14)
    LoadChrToIndex("apl/ch50006.itc", 0x15)
    LoadChrToIndex("apl/ch51721.itc", 0x16)
    LoadChrToIndex("apl/ch51760.itc", 0x17)
    LoadChrToIndex("apl/ch51762.itc", 0x18)
    LoadChrToIndex("apl/ch51722.itc", 0x19)
    LoadChrToIndex("apl/ch51764.itc", 0x1A)
    LoadChrToIndex("apl/ch51765.itc", 0x1B)
    LoadChrToIndex("apl/ch50372.itc", 0x1C)
    LoadChrToIndex("apl/ch51766.itc", 0x1D)
    LoadChrToIndex("apl/ch51763.itc", 0x1E)
    LoadChrToIndex("chr/ch30600.itc", 0x1F)
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    LoadEffect(0x0, "event/ev17060.eff")
    LoadEffect(0x1, "event/ev17062.eff")
    LoadEffect(0x2, "battle/btgun00.eff")
    LoadEffect(0x3, "event/ev606_00.eff")
    LoadEffect(0x4, "battle\\ms00001.eff")
    LoadEffect(0x5, "event/eva01_01.eff")
    LoadEffect(0x6, "battle\\cr320000.eff")
    LoadEffect(0x7, "event/ev17046.eff")
    LoadEffect(0x8, "event\\ev310_00.eff")
    SoundLoad(861)
    SoundLoad(863)
    SoundLoad(926)
    OP_8E(0x2F, "雾香")
    OP_8E(0x28, "雷克特")
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x32, 0x0)
    SetChrSubChip(0x32, 0x0)
    SetChrFlags(0x32, 0x8000)
    ClearChrFlags(0x32, 0x4)
    SetChrPos(0x32, 800, 0, -17400, 0)
    SetChrChipByIndex(0x33, 0x1)
    SetChrSubChip(0x33, 0x0)
    SetChrFlags(0x33, 0x8000)
    ClearChrFlags(0x33, 0x4)
    SetChrPos(0x33, 600, 0, -15600, 0)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    SetChrFlags(0x34, 0x8000)
    ClearChrFlags(0x34, 0x4)
    SetChrPos(0x34, -600, 0, -15600, 0)
    SetChrChipByIndex(0x35, 0x6)
    SetChrSubChip(0x35, 0x0)
    SetChrFlags(0x35, 0x8000)
    ClearChrFlags(0x35, 0x4)
    SetChrPos(0x35, -800, 0, -17400, 0)
    SetChrChipByIndex(0x38, 0xF)
    SetChrSubChip(0x38, 0x0)
    SetChrFlags(0x38, 0x8000)
    ClearChrFlags(0x38, 0x4)
    SetChrPos(0x38, 5200, 250, 300, 135)
    OP_A7(0x38, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x48, 0x13)
    SetChrSubChip(0x48, 0x0)
    SetChrFlags(0x48, 0x8000)
    ClearChrFlags(0x48, 0x4)
    SetChrPos(0x48, 5200, 250, 300, 135)
    OP_A7(0x48, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x3C, 0x13)
    SetChrSubChip(0x3C, 0x0)
    SetChrFlags(0x3C, 0x8000)
    ClearChrFlags(0x3C, 0x4)
    SetChrPos(0x3C, 5200, 250, 300, 135)
    OP_A7(0x3C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x49, 0x13)
    SetChrSubChip(0x49, 0x0)
    SetChrFlags(0x49, 0x8000)
    ClearChrFlags(0x49, 0x4)
    SetChrPos(0x49, -5200, 250, 300, 225)
    OP_A7(0x49, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x39, 0x11)
    SetChrSubChip(0x39, 0x0)
    SetChrFlags(0x39, 0x8000)
    ClearChrFlags(0x39, 0x4)
    SetChrPos(0x39, -5200, 250, 300, 225)
    OP_A7(0x39, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x4A, 0x13)
    SetChrSubChip(0x4A, 0x0)
    SetChrFlags(0x4A, 0x8000)
    ClearChrFlags(0x4A, 0x4)
    SetChrPos(0x4A, -5200, 250, 300, 225)
    OP_A7(0x4A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x3B, 0x1F)
    SetChrSubChip(0x3B, 0x0)
    SetChrFlags(0x3B, 0x8000)
    ClearChrFlags(0x3B, 0x4)
    SetChrPos(0x3B, -5200, 250, 300, 225)
    OP_A7(0x3B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x3A, 0x12)
    SetChrSubChip(0x3A, 0x0)
    SetChrFlags(0x3A, 0x8000)
    ClearChrFlags(0x3A, 0x4)
    SetChrPos(0x3A, 5200, 250, 300, 135)
    OP_A7(0x3A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x23, 0xD)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrPos(0x23, -5200, 250, 300, 225)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x19)
    SetChrSubChip(0x2F, 0x0)
    SetChrFlags(0x2F, 0x8000)
    ClearChrFlags(0x2F, 0x4)
    SetChrPos(0x2F, -11000, 250, -4500, 0)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x4)
    SetChrPos(0x28, 2500, 0, -10000, 0)
    SetChrChipByIndex(0x3E, 0x9)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    OP_52(0x3E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3E, -2000, 250, 9500, 180)
    BeginChrThread(0x3E, 0, 0, 8)
    SetChrChipByIndex(0x3F, 0x9)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    OP_52(0x3F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3F, 2000, 250, 9500, 180)
    BeginChrThread(0x3F, 0, 0, 8)
    SetChrChipByIndex(0x40, 0x9)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    OP_52(0x40, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x40, -6000, 0, 12500, 180)
    BeginChrThread(0x40, 0, 0, 8)
    SetChrChipByIndex(0x41, 0x9)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    OP_52(0x41, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x41, 6000, 0, 12500, 180)
    BeginChrThread(0x41, 0, 0, 8)
    SetChrChipByIndex(0x42, 0x9)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    OP_52(0x42, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x42, 4000, 0, 16500, 180)
    BeginChrThread(0x42, 0, 0, 8)
    SetChrChipByIndex(0x43, 0x9)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    OP_52(0x43, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x43, -4000, 0, 16500, 180)
    BeginChrThread(0x43, 0, 0, 8)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x71, 0x4)
    OP_78(0x12, 0x71)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x71, 0, -8500, -54800, 0)
    OP_D5(0x71, 0xFFFFCD38, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x0, 0x20)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x72, 0x4)
    OP_78(0x13, 0x72)
    SetMapObjFrame(0x13, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x72, 0, -10500, -61800, 0)
    OP_D5(0x72, 0xFFFFCD38, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0xB5, 0xF0, 0x0, 0x20)
    ClearChrFlags(0x73, 0x80)
    ClearChrFlags(0x73, 0x4)
    OP_78(0x14, 0x73)
    SetMapObjFrame(0x14, "light", 0x0, 0x1)
    OP_49()
    OP_90(0x73, 0, -13500, -75800, 0)
    OP_D5(0x73, 0xFFFFCD38, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x0)
    OP_71(0x14, 0xB5, 0xF0, 0x0, 0x20)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    OP_74(0x17, 0x1E)
    OP_70(0x17, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearChrFlags(0x75, 0x80)
    OP_78(0x15, 0x75)
    OP_49()
    SetChrPos(0x75, 0, 0, -20000, 0)
    OP_D5(0x75, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    ClearChrFlags(0x76, 0x80)
    OP_78(0x16, 0x76)
    OP_49()
    SetChrPos(0x76, 0, 0, 0, 0)
    OP_D5(0x76, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    SetChrChipByIndex(0x77, 0x1C)
    SetChrSubChip(0x77, 0x0)
    SetChrChipByIndex(0x78, 0x1C)
    SetChrSubChip(0x78, 0x0)
    SetChrFlags(0x77, 0x8000)
    SetChrFlags(0x78, 0x8000)
    SetChrFlags(0x77, 0x20)
    SetChrFlags(0x78, 0x20)
    SetChrFlags(0x77, 0x2)
    SetChrFlags(0x78, 0x2)
    SetChrFlags(0x77, 0x10)
    SetChrFlags(0x78, 0x10)
    BeginChrThread(0x77, 0, 0, 125)
    BeginChrThread(0x78, 0, 0, 125)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearScenarioFlags(0x1, 1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    OP_68(0, 3000, 15000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(20500, 0)
    OP_68(0, 1000, 15000, 5000)
    MoveCamera(0, 15, 5, 5000)
    SetCameraDistance(17500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(0, -3050, -40000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(850, 0)
    SetCameraDistance(17500, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x42, 3000, 0, 16500, 180)
    SetChrPos(0x43, -3000, 0, 16500, 180)
    BeginChrThread(0x71, 3, 0, 118)
    BeginChrThread(0x72, 3, 0, 119)
    BeginChrThread(0x79, 1, 0, 133)
    OP_68(0, 1350, 3300, 7000)
    MoveCamera(27, 17, 0, 7000)
    OP_6E(750, 7000)
    SetCameraDistance(19500, 7000)
    Sleep(6000)

    def lambda_D622():
        OP_93(0xFE, 0xC8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x40, 2, lambda_D622)
    Sleep(500)

    def lambda_D632():
        OP_93(0xFE, 0xC8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_D632)
    WaitChrThread(0x71, 3)
    Sound(861, 2, 30, 0)
    Sound(863, 2, 50, 0)
    BeginChrThread(0x71, 3, 0, 80)
    WaitChrThread(0x72, 3)
    BeginChrThread(0x72, 3, 0, 81)
    BeginChrThread(0x3E, 2, 0, 83)
    BeginChrThread(0x3E, 1, 0, 138)
    Sleep(300)
    BeginChrThread(0x3F, 2, 0, 83)
    BeginChrThread(0x3F, 1, 0, 139)
    Sleep(300)
    BeginChrThread(0x40, 2, 0, 83)
    BeginChrThread(0x40, 1, 0, 140)
    Sleep(300)
    BeginChrThread(0x41, 2, 0, 83)
    BeginChrThread(0x41, 1, 0, 141)
    WaitChrThread(0x39, 3)
    WaitChrThread(0x3A, 3)
    Sleep(500)
    OP_6F(0x79)
    OP_F0(0x0, 0xA)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x32, 0x80)
    OP_68(0, 1350, 5300, 3000)
    SetCameraDistance(14500, 3000)
    BeginChrThread(0x34, 3, 0, 98)
    Sleep(600)
    BeginChrThread(0x3E, 3, 0, 86)
    BeginChrThread(0x33, 3, 0, 96)
    Sleep(600)
    BeginChrThread(0x32, 3, 0, 94)
    Sleep(300)
    BeginChrThread(0x35, 3, 0, 102)
    Sleep(300)
    BeginChrThread(0x3F, 3, 0, 87)
    Sleep(1300)
    OP_68(-200, 1350, 4800, 1000)
    MoveCamera(25, 25, -10, 1000)
    SetCameraDistance(12000, 1000)
    WaitChrThread(0x34, 3)
    WaitChrThread(0x33, 3)
    WaitChrThread(0x35, 3)
    WaitChrThread(0x32, 3)
    WaitChrThread(0x3E, 3)
    WaitChrThread(0x3F, 3)
    OP_6F(0x79)
    OP_68(-300, 1350, 7310, 1500)
    MoveCamera(23, 20, -10, 1500)
    SetCameraDistance(14500, 1500)
    BeginChrThread(0x23, 2, 0, 126)
    Sleep(800)
    Fade(500)
    EndChrThread(0x40, 0x1)
    EndChrThread(0x41, 0x1)
    ClearChrFlags(0x40, 0x20)
    ClearChrFlags(0x41, 0x20)
    BeginChrThread(0x40, 0, 0, 135)
    BeginChrThread(0x41, 0, 0, 135)
    SetChrPos(0x40, -6000, 0, 12500, 180)
    SetChrPos(0x41, 6000, 0, 12500, 180)
    SetChrPos(0x43, -4000, 0, 16500, 180)
    OP_68(5600, 1350, 1000, 0)
    MoveCamera(87, 29, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(14500, 0)
    MoveCamera(97, 29, 0, 3000)
    SetCameraDistance(13000, 3000)
    SetChrPos(0x38, 2300, 250, -800, 0)
    SetChrFlags(0x33, 0x8)
    SetChrFlags(0x32, 0x8)
    SetChrFlags(0x34, 0x8)
    SetChrFlags(0x35, 0x8)
    OP_0D()
    BeginChrThread(0x3E, 3, 0, 90)
    Sleep(3500)
    EndChrThread(0x72, 0x3)
    EndChrThread(0x79, 0x2)
    EndChrThread(0x79, 0x1)
    EndChrThread(0x3C, 0x1)
    SetChrChipByIndex(0x3C, 0x13)
    SetChrSubChip(0x3C, 0x0)
    OP_63(0x3C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_D868():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x3C, 2, lambda_D868)

    def lambda_D875():
        OP_96(0xFE, 0x1CE8, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_D875)
    Sleep(50)
    EndChrThread(0x48, 0x1)
    SetChrChipByIndex(0x48, 0x13)
    SetChrSubChip(0x48, 0x0)
    OP_63(0x48, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_D8B0():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_D8B0)

    def lambda_D8BD():
        OP_96(0xFE, 0x17D4, 0x32, 0xFFFFF95C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_D8BD)
    Sleep(50)
    EndChrThread(0x38, 0x1)
    EndChrThread(0x79, 0x0)
    SetChrChipByIndex(0x38, 0xF)
    SetChrSubChip(0x38, 0x0)
    OP_63(0x38, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_D8FC():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_D8FC)
    Sleep(50)
    OP_63(0x3A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_D91E():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_D91E)
    Sleep(50)

    #C0409
    ChrTalk(
        0x3C,
        "哦哦哦！？\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x38,
        "哎哎哎！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x3E, 3)
    BeginChrThread(0x79, 0, 0, 129)
    BeginChrThread(0x79, 2, 0, 131)
    OP_68(5600, 1150, 1000, 1500)
    MoveCamera(122, 29, 0, 1500)
    SetCameraDistance(15000, 1500)
    Sleep(500)
    ClearChrFlags(0x77, 0x80)
    SetChrPos(0x77, -2000, 1000, -3000, 0)
    BeginChrThread(0x77, 3, 0, 110)
    Sound(926, 2, 80, 0)
    Sleep(800)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1500, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x3E, 0x0)
    SetChrChipByIndex(0x3E, 0xB)
    SetChrSubChip(0x3E, 0x0)
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x3E, 0x20)

    def lambda_DA5D():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_DA5D)

    def lambda_DA76():
        OP_9B(0x1, 0xFE, 0xB4, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_DA76)
    StopSound(926, 2000, 70)
    SetChrFlags(0x28, 0x800)
    ClearChrFlags(0x28, 0x80)
    BeginChrThread(0x28, 3, 0, 106)
    OP_68(6150, 2350, 3200, 2000)
    MoveCamera(155, 30, 5, 2000)
    SetCameraDistance(10000, 2000)
    WaitChrThread(0x28, 3)
    OP_64(0x3C)
    OP_64(0x48)
    OP_64(0x38)
    OP_64(0x3A)
    WaitChrThread(0x3E, 3)
    SetChrChip(0x1, 0x28, 0x0, 0x0)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x0)
    TurnDirection(0x28, 0x2F, 500)
    ClearChrFlags(0x28, 0x800)
    ClearChrFlags(0x2F, 0x80)
    LoadEffect(0x6, "battle\\cr004101.eff")
    LoadEffect(0x7, "battle\\ms00101.eff")

    #C0411
    ChrTalk(
        0x28,
        "#11507F#5P下面该轮到你啦～\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x2F,
        "#03404F嗯。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-5600, 1150, 2000, 0)
    MoveCamera(105, 23, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(14500, 0)
    SetChrChipByIndex(0x3C, 0x14)
    SetChrSubChip(0x3C, 0x0)
    SetChrPos(0x3C, 7400, 0, -500, 0)
    SetChrChipByIndex(0x48, 0x14)
    SetChrSubChip(0x48, 0x0)
    SetChrPos(0x48, 6100, 50, -700, 0)
    SetChrChipByIndex(0x38, 0x10)
    SetChrSubChip(0x38, 0x0)
    SetChrPos(0x38, 2300, 250, -800, 0)
    SetChrPos(0x3A, 4400, 0, -2200, 0)
    BeginChrThread(0x3A, 3, 0, 117)
    BeginChrThread(0x3F, 3, 0, 91)
    Sleep(1000)
    OP_68(-8500, 1350, 4400, 2000)
    MoveCamera(135, 15, -5, 2000)
    SetCameraDistance(11000, 2000)
    ClearChrFlags(0x78, 0x80)
    SetChrPos(0x78, 1000, 3000, -4000, 0)
    BeginChrThread(0x78, 3, 0, 114)
    Sound(926, 2, 80, 0)
    Sleep(1000)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x5, 0, 1500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x5, 0, 1500, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x3F, 0x0)
    StopSound(926, 1000, 70)
    SetChrChipByIndex(0x3F, 0xB)
    SetChrSubChip(0x3F, 0x0)
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x3F, 0x20)

    def lambda_DCFA():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_DCFA)

    def lambda_DD13():
        OP_9B(0x1, 0xFE, 0xB4, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_DD13)
    BeginChrThread(0x2F, 3, 0, 104)
    WaitChrThread(0x2F, 3)
    EndChrThread(0x4A, 0x1)
    SetChrChipByIndex(0x4A, 0x13)
    SetChrSubChip(0x4A, 0x0)
    OP_93(0x4A, 0x0, 0x1F4)

    #C0413
    ChrTalk(
        0x3B,
        "好、好厉害……！\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x23,
        "#5P#N#01005F真不愧是泰斗流……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x3F, 3)
    Fade(500)
    OP_68(-6950, 1350, 6300, 0)
    MoveCamera(350, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12500, 0)
    SetCameraDistance(8750, 2000)
    SetChrPos(0x2F, -7400, 250, 5800, 0)
    SetChrPos(0x34, -3500, 250, 9200, 225)
    ClearChrFlags(0x34, 0x8)
    SetChrPos(0x77, -7900, 1000, -2200, 0)
    OP_A7(0x77, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x78, 1100, 1000, 5800, 0)
    OP_A7(0x78, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x43, -1500, 250, 10500, 225)
    BeginChrThread(0x43, 2, 0, 83)
    OP_93(0x4A, 0x2D, 0x1F4)
    SetChrChipByIndex(0x4A, 0x14)
    SetChrSubChip(0x4A, 0x0)
    BeginChrThread(0x4A, 1, 0, 123)
    Sound(926, 2, 80, 0)
    BeginChrThread(0x34, 3, 0, 101)
    BeginChrThread(0x77, 3, 0, 111)
    BeginChrThread(0x78, 3, 0, 115)
    WaitChrThread(0x77, 3)
    WaitChrThread(0x78, 3)
    StopSound(926, 300, 70)
    Sound(308, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x2F, 0x19)
    SetChrSubChip(0x2F, 0x0)
    OP_0D()
    WaitChrThread(0x34, 3)
    OP_6F(0x79)

    #C0415
    ChrTalk(
        0x34,
        (
            "#11P雾香前辈！\x01",
            "我来帮你！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2F, 0x34, 500)
    BeginChrThread(0x3E, 3, 0, 92)

    #C0416
    ChrTalk(
        0x2F,
        (
            "#6P#03402F嗯，就让它们好好见识一下\x01",
            "泰斗流的真髓吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x34,
        "#11P是！\x02",
    )

    CloseMessageWindow()

    def lambda_DF00():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_DF00)
    OP_93(0x34, 0x2D, 0x1F4)
    WaitChrThread(0x3E, 3)
    WaitChrThread(0x3F, 3)
    OP_68(-6950, 2150, 6300, 5500)
    MoveCamera(5, 25, -15, 5500)
    SetCameraDistance(13000, 5500)
    BeginChrThread(0x2F, 3, 0, 105)
    BeginChrThread(0x34, 3, 0, 99)
    OP_6F(0x79)
    StopSound(926, 1000, 40)
    Fade(500)
    OP_68(7000, 1350, 5200, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(13000, 0)
    OP_68(9400, 1350, 4200, 1500)
    MoveCamera(30, 25, 0, 1500)
    SetCameraDistance(10000, 1500)
    SetChrPos(0x28, 9400, 0, 4200, 315)
    SetChrPos(0x33, 6500, 250, 9400, 0)
    SetChrPos(0x32, 4700, 250, 5800, 0)
    SetChrPos(0x35, 3700, 100, 6900, 0)
    SetChrChipByIndex(0x35, 0x8)
    SetChrSubChip(0x35, 0x1)
    ClearChrFlags(0x33, 0x8)
    ClearChrFlags(0x32, 0x8)
    ClearChrFlags(0x35, 0x8)
    OP_A7(0x43, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x72, 3, 0, 82)
    BeginChrThread(0x42, 2, 0, 83)
    BeginChrThread(0x41, 3, 0, 88)
    EndChrThread(0x2F, 0xFF)
    EndChrThread(0x34, 0xFF)
    EndChrThread(0x77, 0xFF)
    EndChrThread(0x78, 0xFF)
    OP_0D()
    LoadEffect(0x6, "battle/mgaria0.eff")
    LoadEffect(0x7, "battle/mgaria1.eff")
    LoadEffect(0x8, "battle/mg063_00.eff")
    LoadEffect(0xA, "battle/mg063_01.eff")
    BeginChrThread(0x3F, 3, 0, 93)
    BeginChrThread(0x79, 0, 0, 132)
    BeginChrThread(0x32, 3, 0, 95)
    BeginChrThread(0x33, 3, 0, 97)
    OP_6F(0x79)

    #C0418
    ChrTalk(
        0x28,
        (
            "#11P#11509F哎呀呀，\x01",
            "这也太招摇了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)
    Sleep(300)

    #C0419
    ChrTalk(
        0x28,
        (
            "#11P#11502F也好，这样一来，\x01",
            "我这边就比较轻松了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x33, 3)
    WaitChrThread(0x3F, 3)
    WaitChrThread(0x41, 3)
    BeginChrThread(0x28, 3, 0, 109)
    WaitChrThread(0x28, 3)
    EndChrThread(0x79, 0x0)
    Fade(500)
    OP_68(-4400, 1150, -2700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12500, 0)
    SetChrChipByIndex(0x2F, 0x19)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x2F, -6400, 250, 5800, 270)
    ClearChrFlags(0x34, 0x20)
    ClearChrFlags(0x34, 0x10)
    ClearChrFlags(0x34, 0x2)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    SetChrPos(0x34, -4400, 250, 7800, 0)
    ClearScenarioFlags(0x1, 0)
    BeginChrThread(0x35, 3, 0, 103)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x79, 0x2)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -4400, 0, -2700, 0)
    SetChrChipByIndex(0x3F, 0x9)
    SetChrSubChip(0x3F, 0x0)
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x3F, 0, 0, 8)
    SetChrChipByIndex(0x41, 0x9)
    SetChrSubChip(0x41, 0x0)
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x41, 0, 0, 8)
    SetChrChipByIndex(0x42, 0x9)
    SetChrSubChip(0x42, 0x0)
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x42, 0, 0, 8)
    SetChrChipByIndex(0x3E, 0x9)
    SetChrSubChip(0x3E, 0x0)
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x3E, 0, 0, 8)
    SetChrPos(0x3E, -11500, 0, 8300, 90)
    SetCameraDistance(12000, 1000)
    OP_6F(0x79)
    LoadEffect(0x8, "battle/mg043_00.eff")
    LoadEffect(0xA, "event\\eva03_01.eff")

    #C0420
    ChrTalk(
        0x23,
        "#01003F#11P是时候了……\x02",
    )

    CloseMessageWindow()
    OP_93(0x23, 0x10E, 0x1F4)
    Fade(250)
    SetChrFlags(0x23, 0x20)
    SetChrFlags(0x23, 0x10)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 0x15)
    SetChrSubChip(0x23, 0x2)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x23, 0x3)
    Sound(804, 0, 100, 0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0421
    ChrTalk(
        0x23,
        (
            "#01007F#4S#11P特别任务支援科，突击！\x02\x03",

            "『道路』已经拓开！\x01",
            "接下来就交给你们了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x3D, -4400, 0, -2400, 0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0422
    ChrTalk(
        0x3D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S明白！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -4150, -40000, 0)
    MoveCamera(139, 31, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(19500, 0)
    OP_F0(0x0, 0x1)
    OP_68(0, 1150, -20000, 3300)
    MoveCamera(149, 31, 0, 3300)
    SetCameraDistance(12500, 3300)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    ClearMapObjFlags(0x14, 0x4)
    BeginChrThread(0x73, 3, 0, 120)
    BeginChrThread(0x79, 1, 0, 134)
    SetChrChipByIndex(0x23, 0xD)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x20)
    ClearChrFlags(0x23, 0x10)
    ClearChrFlags(0x23, 0x2)
    OP_93(0x23, 0x0, 0x0)
    OP_6F(0x79)
    PlayEffect(0xA, 0x4, 0x73, 0x1, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA, 0x5, 0x73, 0x1, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA, 0x6, 0x73, 0x1, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(0, 650, 12000, 4000)
    MoveCamera(153, 19, -13, 4000)
    SetCameraDistance(14500, 4000)
    SetScenarioFlags(0x1, 0)
    OP_6F(0x79)
    Fade(100)
    OP_68(0, 1050, 22000, 0)
    MoveCamera(25, 17, 5, 0)
    OP_6E(750, 0)
    SetCameraDistance(19000, 0)
    OP_F0(0x0, 0xA)
    SetMapObjFlags(0x18, 0x4)
    OP_68(0, 1050, 29000, 2500)
    MoveCamera(25, 17, 13, 2500)
    SetCameraDistance(16000, 2500)
    Sleep(1500)
    StopSound(861, 2000, 30)
    StopSound(863, 2000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x73, 3)
    StopBGM(0x1770)
    WaitBGM()
    ReplaceBGM(-1, -1)
    OP_24(0x35D)
    OP_24(0x35F)
    OP_24(0x39E)
    SetScenarioFlags(0x23, 4)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_CC48 end

    def Function_71_E57B(): pass

    label("Function_71_E57B")


    def lambda_E580():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E580)

    def lambda_E59A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E59A)
    WaitChrThread(0xFE, 1)

    def lambda_E5AF():
        OP_95(0xFE, 3100, 250, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E5AF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x38, 1, 0, 123)
    BeginChrThread(0x79, 0, 0, 127)
    Return()

    # Function_71_E57B end

    def Function_72_E5E4(): pass

    label("Function_72_E5E4")


    def lambda_E5E9():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E5E9)

    def lambda_E603():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E603)
    WaitChrThread(0xFE, 1)

    def lambda_E618():
        OP_95(0xFE, 6100, 50, -700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E618)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x48, 1, 0, 123)
    Return()

    # Function_72_E5E4 end

    def Function_73_E647(): pass

    label("Function_73_E647")


    def lambda_E64C():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E64C)

    def lambda_E666():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E666)
    WaitChrThread(0xFE, 1)

    def lambda_E67B():
        OP_95(0xFE, 7400, 0, -500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E67B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x3C, 1, 0, 123)
    Return()

    # Function_73_E647 end

    def Function_74_E6AA(): pass

    label("Function_74_E6AA")


    def lambda_E6AF():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6AF)

    def lambda_E6C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E6C9)
    WaitChrThread(0xFE, 1)

    def lambda_E6DE():
        OP_95(0xFE, -3100, 250, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6DE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x49, 1, 0, 123)
    Return()

    # Function_74_E6AA end

    def Function_75_E70D(): pass

    label("Function_75_E70D")


    def lambda_E712():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E712)

    def lambda_E72C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E72C)
    WaitChrThread(0xFE, 1)

    def lambda_E741():
        OP_95(0xFE, -6100, 50, -700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E741)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)

    #C0423
    ChrTalk(
        0x39,
        "#5P开始迎击！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_75_E70D end

    def Function_76_E778(): pass

    label("Function_76_E778")


    def lambda_E77D():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E77D)

    def lambda_E797():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E797)
    WaitChrThread(0xFE, 1)

    def lambda_E7AC():
        OP_95(0xFE, -7400, 0, -500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7AC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x4A, 1, 0, 123)
    BeginChrThread(0x79, 1, 0, 128)
    Return()

    # Function_76_E778 end

    def Function_77_E7E1(): pass

    label("Function_77_E7E1")


    def lambda_E7E6():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7E6)

    def lambda_E800():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E800)
    WaitChrThread(0xFE, 1)

    def lambda_E815():
        OP_95(0xFE, -6400, 0, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E815)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_77_E7E1 end

    def Function_78_E836(): pass

    label("Function_78_E836")


    def lambda_E83B():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E83B)

    def lambda_E855():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E855)
    WaitChrThread(0xFE, 1)

    def lambda_E86A():
        OP_95(0xFE, 4400, 0, -2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E86A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x9)

    #C0424
    ChrTalk(
        0x3A,
        "用车辆作掩护！\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_78_E836 end

    def Function_79_E8A2(): pass

    label("Function_79_E8A2")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E8AF():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E8AF)

    def lambda_E8C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E8C9)
    WaitChrThread(0xFE, 1)

    def lambda_E8DE():
        OP_95(0xFE, -2000, 250, -1600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E8DE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x23, 1, 0, 124)
    BeginChrThread(0x79, 2, 0, 130)
    Return()

    # Function_79_E8A2 end

    def Function_80_E913(): pass

    label("Function_80_E913")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAB9")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -2600, 100, 6500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -3700, 250, 11100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -5500, 250, 8800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -1300, 100, 8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -3300, 150, 9000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -6800, 250, 9100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -5500, 250, 6700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_80_E913")

    label("loc_EAB9")

    Return()

    # Function_80_E913 end

    def Function_81_EABA(): pass

    label("Function_81_EABA")

    Sleep(300)

    label("loc_EABD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC63")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 2600, 100, 6500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3700, 250, 11100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 5500, 250, 8800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1300, 100, 8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3300, 150, 9000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 6800, 250, 9100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 5500, 250, 6700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("loc_EABD")

    label("loc_EC63")

    Return()

    # Function_81_EABA end

    def Function_82_EC64(): pass

    label("Function_82_EC64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE0A")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 2600, 250, 9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3700, 0, 14100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 5500, 250, 11800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1300, 250, 11000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 3300, 250, 12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 6800, 250, 12100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 5500, 250, 9700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_82_EC64")

    label("loc_EE0A")

    Return()

    # Function_82_EC64 end

    def Function_83_EE0B(): pass

    label("Function_83_EE0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE55")
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 1600, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("Function_83_EE0B")

    label("loc_EE55")

    Return()

    # Function_83_EE0B end

    def Function_84_EE56(): pass

    label("Function_84_EE56")

    Sleep(6500)
    BeginChrThread(0x3E, 3, 0, 85)
    Sleep(50)
    BeginChrThread(0x43, 3, 0, 85)
    Sleep(500)
    BeginChrThread(0x3F, 3, 0, 85)
    Sleep(50)
    BeginChrThread(0x41, 3, 0, 85)
    Sleep(500)
    BeginChrThread(0x40, 3, 0, 85)
    Sleep(50)
    BeginChrThread(0x42, 3, 0, 85)
    WaitChrThread(0x3E, 3)
    WaitChrThread(0x3F, 3)
    WaitChrThread(0x40, 3)
    WaitChrThread(0x41, 3)
    WaitChrThread(0x42, 3)
    WaitChrThread(0x43, 3)
    Return()

    # Function_84_EE56 end

    def Function_85_EEA5(): pass

    label("Function_85_EEA5")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_EECC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EECC)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_85_EEA5 end

    def Function_86_EF08(): pass

    label("Function_86_EF08")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_EF2F():
        OP_95(0xFE, -2200, 100, 5300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF2F)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_86_EF08 end

    def Function_87_EF6B(): pass

    label("Function_87_EF6B")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_EF92():
        OP_95(0xFE, 2000, 100, 5800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF92)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_87_EF6B end

    def Function_88_EFCE(): pass

    label("Function_88_EFCE")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(630)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_EFF4():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EFF4)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_88_EFCE end

    def Function_89_F02C(): pass

    label("Function_89_F02C")

    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_F04C():
        OP_A6(0xFE, 0x0, 0x64, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_F04C)
    Sleep(1000)
    Sound(985, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_F0A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F0A8)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_89_F02C end

    def Function_90_F0B9(): pass

    label("Function_90_F0B9")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, 7300, 250, 4300, 225)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_F122():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F122)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Sleep(130)
    SetChrSubChip(0x3E, 0x1)
    Sleep(130)

    def lambda_F144():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_F144)
    Sleep(1000)
    Sound(951, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)

    def lambda_F16F():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F16F)
    Sleep(50)
    Sound(893, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x0, 0x3E8, 0xBB8, 0x3E8)
    Sound(876, 0, 100, 0)
    Sound(880, 0, 100, 0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4500, 1700, 1000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 4500, 1800, 1000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    OP_52(0x76, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x72, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x76, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x72, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x76, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x72, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D5(0x76, 0x0, 0x11170, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    WaitChrThread(0xFE, 1)
    CancelBlur(700)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_90_F0B9 end

    def Function_91_F28F(): pass

    label("Function_91_F28F")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, -7300, 250, 4300, 135)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_F2FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F2FE)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_91_F28F end

    def Function_92_F312(): pass

    label("Function_92_F312")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, -12800, 0, 8300, 135)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_F381():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F381)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_92_F312 end

    def Function_93_F395(): pass

    label("Function_93_F395")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, 8300, 0, 15000, 180)
    Sound(985, 0, 70, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_F404():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F404)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_93_F395 end

    def Function_94_F418(): pass

    label("Function_94_F418")


    def lambda_F41D():
        OP_95(0xFE, 800, 100, 600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F41D)
    WaitChrThread(0xFE, 1)

    def lambda_F43B():
        OP_96(0xFE, 0x44C, 0x64, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F43B)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sound(567, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_82(0x64, 0x64, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)

    def lambda_F4C6():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_F4C6)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x0, 0, 2350, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x0, 0, 2350, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    SetChrSubChip(0xFE, 0x6)
    Sound(567, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_82(0x64, 0x64, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)

    def lambda_F5C4():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_F5C4)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x0, 300, 2350, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x0, 300, 2350, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    SetChrSubChip(0xFE, 0x6)
    Sound(567, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_82(0x64, 0x64, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)

    def lambda_F6C2():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_F6C2)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x0, -300, 2350, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x0, -300, 2350, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    BeginChrThread(0x3F, 3, 0, 89)
    Return()

    # Function_94_F418 end

    def Function_95_F75C(): pass

    label("Function_95_F75C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F7B1")
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Jump("Function_95_F75C")

    label("loc_F7B1")

    Return()

    # Function_95_F75C end

    def Function_96_F7B2(): pass

    label("Function_96_F7B2")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_F7C2():
        OP_95(0xFE, 600, 250, 400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F7C2)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 100, 0)

    def lambda_F7EA():
        OP_9D(0xFE, 0x6A4, 0x64, 0x1130, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F7EA)
    Sleep(500)
    SetChrSubChip(0xFE, 0x7)
    Sound(538, 0, 100, 0)
    OP_82(0x190, 0x190, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 0, 1500, 1300, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x3F, 0x0)
    SetChrChipByIndex(0x3F, 0xB)
    SetChrSubChip(0x3F, 0x0)
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x3F, 0x20)

    def lambda_F889():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_F889)
    OP_52(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_F8AD():
        OP_9D(0xFE, 0x7D0, 0x64, 0x1E78, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_F8AD)
    WaitChrThread(0xFE, 1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_96_F7B2 end

    def Function_97_F8D1(): pass

    label("Function_97_F8D1")

    SetChrSubChip(0xFE, 0x7)
    Sleep(1200)
    SetChrSubChip(0xFE, 0x3)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x1964, 0xFA, 0x170C, 0x1F4, 0x3E8)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    OP_96(0xFE, 0x1964, 0xFA, 0x1CE8, 0xFA0, 0x0)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_97_F8D1 end

    def Function_98_F919(): pass

    label("Function_98_F919")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)

    def lambda_F931():
        OP_95(0xFE, -600, 250, 400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F931)
    WaitChrThread(0xFE, 1)

    def lambda_F94F():
        OP_95(0xFE, -1300, 100, 4400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F94F)
    Sleep(100)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x4)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x3E, 0x0)
    SetChrChipByIndex(0x3E, 0xB)
    SetChrSubChip(0x3E, 0x0)
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x3E, 0x20)

    def lambda_FA11():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_FA11)

    def lambda_FA2A():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_FA2A)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)

    def lambda_FA64():
        OP_95(0xFE, -1400, 100, 5400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA64)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)

    def lambda_FAEC():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_FAEC)

    def lambda_FB05():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_FB05)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)

    def lambda_FB3F():
        OP_95(0xFE, -1500, 100, 6400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB3F)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)

    def lambda_FBC7():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_FBC7)

    def lambda_FBE0():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_FBE0)
    WaitChrThread(0xFE, 1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_98_F919 end

    def Function_99_FC11(): pass

    label("Function_99_FC11")

    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FC1E():
        OP_95(0xFE, -3900, 250, 8800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC1E)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x5)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 100, 0)

    def lambda_FC61():
        OP_9C(0xFE, 0x0, 0x2BC, 0x0, 0x2EE, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC61)
    SetChrSubChip(0xFE, 0x14)
    Sleep(50)
    BeginChrThread(0xFE, 2, 0, 100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    Return()

    # Function_99_FC11 end

    def Function_100_FC9F(): pass

    label("Function_100_FC9F")

    EndChrThread(0x43, 0x0)
    EndChrThread(0x43, 0x2)
    SetChrChipByIndex(0x43, 0xB)
    SetChrSubChip(0x43, 0x0)
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FCBA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FDAC")
    Sound(815, 0, 100, 0)
    Sound(635, 0, 50, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x4, 0xFF, 0x43, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_FD1E():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_FD1E)
    Sound(253, 0, 40, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(50)
    SetChrSubChip(0xFE, 0x19)
    Sleep(50)
    SetChrSubChip(0xFE, 0x18)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(50)
    Jump("loc_FCBA")

    label("loc_FDAC")

    Return()

    # Function_100_FC9F end

    def Function_101_FDAD(): pass

    label("Function_101_FDAD")

    SetChrChipByIndex(0x34, 0x3)
    SetChrSubChip(0x34, 0x0)

    def lambda_FDBA():
        OP_95(0xFE, -6500, 250, 6800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_FDBA)
    WaitChrThread(0x34, 1)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    Return()

    # Function_101_FDAD end

    def Function_102_FDDC(): pass

    label("Function_102_FDDC")

    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FDE9():
        OP_95(0xFE, -800, 100, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FDE9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sound(253, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, -200, 1100, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(256, 0, 100, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    BeginChrThread(0x3E, 3, 0, 89)
    Sleep(1500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_102_FDDC end

    def Function_103_FE95(): pass

    label("Function_103_FE95")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x6, 0x3, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_AD(0x8)
    StopEffect(0x3, 0x2)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    EndChrThread(0x42, 0x2)
    PlayEffect(0x8, 0xFF, 0x42, 0x1, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BeginChrThread(0x42, 3, 0, 89)
    Sleep(4000)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x6, 0x3, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_103_FE95 end

    def Function_104_FFA2(): pass

    label("Function_104_FFA2")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FFC2():
        OP_95(0xFE, -8500, 150, 3500, 9000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFC2)
    WaitChrThread(0xFE, 1)
    Sound(621, 0, 100, 0)
    Sound(534, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    CancelBlur(500)
    SetCameraDistance(8000, 500)
    MoveCamera(145, 20, -10, 500)
    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)

    #C0425
    ChrTalk(
        0x2F,
        "#03401F#9A喝……！\x02",
    )
    #Auto

    Sleep(700)

    def lambda_10033():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10033)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x14)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x1F4)
    Sound(833, 0, 80, 0)
    Sound(635, 0, 100, 0)
    OP_68(-8500, 1350, 4900, 500)
    MoveCamera(135, 15, -5, 500)
    SetCameraDistance(11500, 500)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 1100, -1300, 180, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x3F, 3, 0, 89)

    def lambda_100DA():
        OP_9D(0xFE, 0xFFFFDF94, 0xFA, 0x2454, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_100DA)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    CancelBlur(700)
    Sleep(500)
    Sound(880, 0, 100, 0)
    Sleep(1500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_104_FFA2 end

    def Function_105_10117(): pass

    label("Function_105_10117")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sound(250, 0, 100, 0)
    Sleep(250)
    SetChrSubChip(0xFE, 0x2)
    Sound(926, 2, 50, 0)
    BeginChrThread(0x77, 3, 0, 112)
    BeginChrThread(0x78, 3, 0, 116)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_105_10117 end

    def Function_106_10150(): pass

    label("Function_106_10150")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_10170():
        OP_95(0xFE, 2500, 100, -2600, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10170)
    WaitChrThread(0xFE, 1)

    #C0426
    ChrTalk(
        0x28,
        "#12P#11507F#9A看招！\x02",
    )
    #Auto

    TurnDirection(0xFE, 0x3E, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrSubChip(0xFE, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_101BD():
        OP_9D(0xFE, 0x1194, 0x5DC, 0x258, 0x76C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101BD)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 100, 0)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(844, 0, 100, 0)

    def lambda_101FE():
        OP_9D(0xFE, 0x1A90, 0xFA, 0xABE, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101FE)
    Sleep(400)
    Sound(540, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    OP_68(6800, 850, 2750, 300)
    MoveCamera(150, 25, 5, 300)
    SetCameraDistance(10000, 300)
    OP_82(0x12C, 0x12C, 0xBB8, 0x12C)
    CancelBlur(0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(246, 0, 100, 0)
    Sound(288, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_102F5():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_102F5)

    def lambda_1030E():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_1030E)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x4)
    Sleep(1000)
    BeginChrThread(0xFE, 0, 0, 108)
    TurnDirection(0xFE, 0x3E, 1000)
    OP_6F(0x79)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0xC8, 0x0, 0x0, 0xFA, 0x1388)
    Sleep(50)
    OP_9C(0xFE, 0xFFFFFF38, 0x0, 0x0, 0xFA, 0x1388)
    Sleep(200)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)

    def lambda_1039E():
        OP_A6(0xFE, 0x0, 0x64, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_1039E)
    OP_82(0x12C, 0x12C, 0xBB8, 0x9C4)
    OP_68(7300, 850, 4300, 300)
    MoveCamera(145, 30, 5, 300)
    SetChrFlags(0xFE, 0x20)
    SetChrChip(0x0, 0xFE, 0x5, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_9A(0xFE, 0x3E, 0x0, 0x4E20, 0x0)
    Sound(287, 0, 100, 0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    SetChrPos(0xFE, 5170, 250, 2670, 45)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x4E20, 0x0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    SetChrPos(0xFE, 9280, 0, 1780, 315)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x4E20, 0x0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    SetChrPos(0xFE, 4640, 250, 3970, 90)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x4E20, 0x0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    OP_68(8100, 850, 5270, 300)
    MoveCamera(135, 25, 10, 300)
    SetCameraDistance(11000, 300)
    SetChrPos(0xFE, 6730, 850, 1510, 0)
    BeginChrThread(0xFE, 0, 0, 107)
    OP_96(0xFE, 0x2134, 0xFA, 0x16A8, 0x4E20, 0x0)
    Sound(264, 0, 100, 0)
    Sound(681, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x5, 0, 1900, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    WaitChrThread(0xFE, 0)
    CancelBlur(500)
    ClearChrFlags(0xFE, 0x20)
    Sleep(500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_68(7300, 1350, 3300, 2000)
    MoveCamera(155, 25, 5, 2000)
    SetCameraDistance(13500, 2000)
    BeginChrThread(0x3E, 3, 0, 89)
    Return()

    # Function_106_10150 end

    def Function_107_1078A(): pass

    label("Function_107_1078A")

    SetChrChipByIndex(0xFE, 0x18)
    OP_A0(0xFE, 1500, 0x0, 0x3)
    Return()

    # Function_107_1078A end

    def Function_108_10796(): pass

    label("Function_108_10796")

    SetChrChipByIndex(0xFE, 0x16)

    label("loc_1079A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_107B8")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    OP_A0(0xFE, 1500, 0x3, 0x1)
    Jump("loc_1079A")

    label("loc_107B8")

    Return()

    # Function_108_10796 end

    def Function_109_107B9(): pass

    label("Function_109_107B9")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_68(9400, 850, 4200, 2000)
    MoveCamera(30, 30, 5, 2000)
    SetCameraDistance(9500, 2000)
    Sound(357, 0, 70, 0)
    PlayEffect(0x6, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    Sound(280, 0, 80, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(300)
    OP_68(5600, 1550, 14500, 1500)
    MoveCamera(40, 27, 0, 1500)
    SetCameraDistance(14500, 1500)
    OP_6F(0x79)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 5600, 250, 14500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 5600, 250, 14500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    MoveCamera(50, 27, 0, 3500)
    SetCameraDistance(16500, 3500)
    EndChrThread(0x3F, 0x0)
    EndChrThread(0x3F, 0x2)
    SetChrChipByIndex(0x3F, 0xB)
    SetChrSubChip(0x3F, 0x0)
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10965():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_10965)
    Sleep(50)
    EndChrThread(0x41, 0x0)
    EndChrThread(0x41, 0x2)
    SetChrChipByIndex(0x41, 0xB)
    SetChrSubChip(0x41, 0x0)
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1099C():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x41, 2, lambda_1099C)
    Sleep(50)
    EndChrThread(0x42, 0x0)
    EndChrThread(0x42, 0x2)
    SetChrChipByIndex(0x42, 0xB)
    SetChrSubChip(0x42, 0x0)
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_109D3():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x42, 2, lambda_109D3)
    Sleep(2500)
    CancelBlur(0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sleep(1000)
    Return()

    # Function_109_107B9 end

    def Function_110_10A04(): pass

    label("Function_110_10A04")

    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_10A48():
        OP_9E(0xFE, 0xFA0, 0xFFFFF448, 0x36EE8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10A48)

    label("loc_10A5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10A86")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_10A5E")

    label("loc_10A86")

    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_110_10A04 end

    def Function_111_10A9E(): pass

    label("Function_111_10A9E")

    SetChrChip(0x0, 0x77, 0x32, 0x12C)

    def lambda_10AAB():
        OP_9E(0xFE, 0xFFFFE124, 0x708, 0x2BF20, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x77, 1, lambda_10AAB)

    label("loc_10AC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10AE9")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_10AC1")

    label("loc_10AE9")

    WaitChrThread(0x77, 1)
    SetChrChip(0x1, 0x77, 0x0, 0x0)
    OP_A7(0x77, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_111_10A9E end

    def Function_112_10B01(): pass

    label("Function_112_10B01")

    SetChrPos(0xFE, -7400, 250, 5400, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0xFE, 2, 0, 113)

    def lambda_10B30():
        OP_9E(0xFE, 0xFFFFD9B8, 0x1C84, 0x2BF20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B30)
    WaitChrThread(0xFE, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 40, 0)
    Sound(308, 0, 100, 0)
    EndChrThread(0x3E, 0x0)
    SetChrChipByIndex(0x3E, 0xB)
    SetChrSubChip(0x3E, 0x0)
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x4, 0xFF, 0x3E, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_10BCB():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_10BCB)

    label("loc_10BDF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10C8C")

    def lambda_10BEF():
        OP_9E(0xFE, 0xFFFFD3DC, 0x2CEC, 0x57E40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10BEF)
    WaitChrThread(0xFE, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 40, 0)
    Sound(308, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_10C73():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_10C73)
    Jump("loc_10BDF")

    label("loc_10C8C")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_112_10B01 end

    def Function_113_10CA0(): pass

    label("Function_113_10CA0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10CEA")
    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1900)
    Jump("Function_113_10CA0")

    label("loc_10CEA")

    Return()

    # Function_113_10CA0 end

    def Function_114_10CEB(): pass

    label("Function_114_10CEB")

    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_10D2F():
        OP_9E(0xFE, 0xFFFFE4A8, 0xFFFFF060, 0xFFFD40E0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D2F)

    label("loc_10D45")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10D6D")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_10D45")

    label("loc_10D6D")

    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_114_10CEB end

    def Function_115_10D85(): pass

    label("Function_115_10D85")

    Sleep(150)
    SetChrChip(0x0, 0x78, 0x32, 0x12C)

    def lambda_10D95():
        OP_9E(0xFE, 0xFFFFF4AC, 0x16A8, 0x2BF20, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x78, 1, lambda_10D95)

    label("loc_10DAB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10DD3")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_10DAB")

    label("loc_10DD3")

    WaitChrThread(0x78, 1)
    SetChrChip(0x1, 0x78, 0x0, 0x0)
    OP_A7(0x78, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_115_10D85 end

    def Function_116_10DEB(): pass

    label("Function_116_10DEB")

    SetChrPos(0xFE, -7400, 250, 6200, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0xFE, 2, 0, 113)

    def lambda_10E1A():
        OP_9E(0xFE, 0xFFFFD9B8, 0x1C84, 0xFFFD5468, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E1A)
    WaitChrThread(0xFE, 1)

    label("loc_10E34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10E63")

    def lambda_10E44():
        OP_9E(0xFE, 0xFFFFCE00, 0x17D4, 0xFFFA81C0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E44)
    WaitChrThread(0xFE, 1)
    Jump("loc_10E34")

    label("loc_10E63")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_116_10DEB end

    def Function_117_10E77(): pass

    label("Function_117_10E77")

    BeginChrThread(0x3C, 1, 0, 123)
    Sleep(300)
    BeginChrThread(0x38, 1, 0, 123)
    Sleep(300)
    BeginChrThread(0x48, 1, 0, 123)
    BeginChrThread(0x72, 3, 0, 81)
    Return()

    # Function_117_10E77 end

    def Function_118_10E96(): pass

    label("Function_118_10E96")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x2710, 0x0)

    def lambda_10EAF():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10EAF)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x2710, 0x0)

    def lambda_10EDC():
        OP_D5(0xFE, 0x0, 0xFFFEEE90, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10EDC)
    OP_9E(0xFE, 0xFFFFDCD8, 0xFFFFE4A8, 0xFFFF15A0, 0x1F40, 0x0)
    Sound(487, 0, 100, 0)
    OP_71(0x12, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x12)
    Sound(462, 0, 100, 0)
    OP_71(0x12, 0x12D, 0x14A, 0x0, 0x0)
    OP_79(0x12)
    BeginChrThread(0x4A, 3, 0, 76)
    Sleep(400)
    BeginChrThread(0x39, 3, 0, 75)
    Sleep(400)
    BeginChrThread(0x23, 3, 0, 79)
    Sleep(400)
    BeginChrThread(0x49, 3, 0, 74)
    Sleep(400)
    BeginChrThread(0x3B, 3, 0, 77)
    Sleep(400)
    Sound(461, 0, 100, 0)
    OP_71(0x12, 0x14B, 0x168, 0x0, 0x0)
    OP_79(0x12)
    Sound(485, 0, 100, 0)
    Return()

    # Function_118_10E96 end

    def Function_119_10F78(): pass

    label("Function_119_10F78")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x2710, 0x0)

    def lambda_10F91():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10F91)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x2710, 0x0)

    def lambda_10FBE():
        OP_D5(0xFE, 0x0, 0x11170, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10FBE)
    OP_9E(0xFE, 0x2328, 0xFFFFE4A8, 0xEA60, 0x1F40, 0x0)
    Sound(492, 0, 100, 0)
    OP_71(0x13, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x13)
    Sound(462, 0, 100, 0)
    OP_71(0x13, 0xF1, 0x10E, 0x0, 0x0)
    OP_79(0x13)
    BeginChrThread(0x3C, 3, 0, 73)
    Sleep(400)
    BeginChrThread(0x48, 3, 0, 72)
    Sleep(400)
    BeginChrThread(0x38, 3, 0, 71)
    Sleep(400)
    BeginChrThread(0x3A, 3, 0, 78)
    Sleep(800)
    Sound(461, 0, 100, 0)
    OP_71(0x13, 0x10F, 0x12C, 0x0, 0x0)
    OP_79(0x13)
    Return()

    # Function_119_10F78 end

    def Function_120_1104B(): pass

    label("Function_120_1104B")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3A98, 0x0)

    def lambda_11064():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11064)
    SetMapObjFrame(0x14, "kage", 0x0, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    BeginChrThread(0x75, 3, 0, 121)
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x514, 0x514)

    def lambda_110AC():
        OP_D5(0xFE, 0x0, 0x1B58, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_110AC)
    OP_82(0x0, 0xC8, 0xBB8, 0xC8)
    Sound(833, 0, 100, 0)
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x12C, 0x44C)
    EndChrThread(0xFE, 0x2)

    def lambda_110F7():
        OP_D5(0xFE, 0x0, 0xFFFFE4A8, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_110F7)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    Sound(833, 0, 100, 0)
    Sound(487, 0, 100, 0)
    SetMapObjFrame(0x14, "kage", 0x1, 0x1)
    SetMapObjFlags(0x15, 0x4)
    EndChrThread(0x75, 0x3)
    BeginChrThread(0x74, 3, 0, 122)

    def lambda_11149():
        OP_96(0xFE, 0x0, 0xC8, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11149)
    WaitChrThread(0xFE, 2)

    def lambda_11167():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11167)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_120_1104B end

    def Function_121_11180(): pass

    label("Function_121_11180")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_111A7")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x73, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x73, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_121_11180")

    label("loc_111A7")

    Return()

    # Function_121_11180 end

    def Function_122_111A8(): pass

    label("Function_122_111A8")

    Sleep(3100)
    Sound(880, 0, 100, 0)
    Sound(991, 0, 100, 0)
    Sound(200, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -900, 1200, 31000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 900, 1200, 31000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x1F4)
    OP_71(0x17, 0x0, 0xA, 0x0, 0x0)
    Return()

    # Function_122_111A8 end

    def Function_123_11249(): pass

    label("Function_123_11249")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1129E")
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_123_11249")

    label("loc_1129E")

    Return()

    # Function_123_11249 end

    def Function_124_1129F(): pass

    label("Function_124_1129F")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    label("loc_112D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11371")
    SetChrSubChip(0x23, 0x5)
    Sleep(150)
    SetChrSubChip(0x23, 0x6)
    Sleep(100)
    SetChrSubChip(0x23, 0x7)
    Sleep(100)
    SetChrSubChip(0x23, 0x4)
    Sleep(100)
    SetChrSubChip(0x23, 0x3)
    Sleep(70)
    SetChrSubChip(0x23, 0x2)
    Sleep(70)
    SetChrSubChip(0x23, 0x1)
    Sleep(70)
    SetChrSubChip(0x23, 0x0)
    Sleep(70)
    SetChrSubChip(0x23, 0x1)
    Sleep(70)
    SetChrSubChip(0x23, 0x2)
    Sleep(70)
    SetChrSubChip(0x23, 0x3)
    Sleep(70)
    SetChrSubChip(0x23, 0x4)
    Sleep(600)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Jump("loc_112D6")

    label("loc_11371")

    Return()

    # Function_124_1129F end

    def Function_125_11372(): pass

    label("Function_125_11372")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11390")
    OP_A1(0xFE, 0xFA0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_125_11372")

    label("loc_11390")

    Return()

    # Function_125_11372 end

    def Function_126_11391(): pass

    label("Function_126_11391")


    def lambda_11396():
        OP_96(0xFE, 0xA8C, 0xFA, 0x283C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_11396)
    Sleep(50)

    def lambda_113B3():
        OP_96(0xFE, 0x44C, 0x64, 0x206C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_113B3)
    Sleep(100)
    SetChrChipByIndex(0x34, 0x3)
    SetChrSubChip(0x34, 0x0)

    def lambda_113D8():
        OP_96(0xFE, 0xFFFFF18C, 0xFA, 0x2454, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_113D8)
    Sleep(50)
    SetChrChipByIndex(0x35, 0x7)
    SetChrSubChip(0x35, 0x0)

    def lambda_113FD():
        OP_96(0xFE, 0xFFFFF2B8, 0x64, 0x1BBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_113FD)
    WaitChrThread(0x33, 1)
    SetChrSubChip(0x33, 0x5)
    WaitChrThread(0x32, 1)
    SetChrSubChip(0x32, 0x5)
    WaitChrThread(0x34, 1)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    WaitChrThread(0x35, 1)
    SetChrChipByIndex(0x35, 0x6)
    SetChrSubChip(0x35, 0x0)
    Return()

    # Function_126_11391 end

    def Function_127_1143B(): pass

    label("Function_127_1143B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11454")
    Sound(567, 0, 100, 0)
    Sleep(1200)
    Jump("Function_127_1143B")

    label("loc_11454")

    Return()

    # Function_127_1143B end

    def Function_128_11455(): pass

    label("Function_128_11455")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1146E")
    Sound(530, 0, 70, 0)
    Sleep(1200)
    Jump("Function_128_11455")

    label("loc_1146E")

    Return()

    # Function_128_11455 end

    def Function_129_1146F(): pass

    label("Function_129_1146F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11488")
    Sound(530, 0, 50, 0)
    Sleep(1200)
    Jump("Function_129_1146F")

    label("loc_11488")

    Return()

    # Function_129_1146F end

    def Function_130_11489(): pass

    label("Function_130_11489")

    Sound(987, 0, 100, 0)

    label("loc_1148F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_114CF")
    Sleep(150)
    Sleep(100)
    Sleep(100)
    Sound(531, 0, 50, 0)
    Sleep(100)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(600)
    Sound(987, 0, 70, 0)
    Jump("loc_1148F")

    label("loc_114CF")

    Return()

    # Function_130_11489 end

    def Function_131_114D0(): pass

    label("Function_131_114D0")

    Sound(987, 0, 50, 0)

    label("loc_114D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11516")
    Sleep(150)
    Sleep(100)
    Sleep(100)
    Sound(531, 0, 30, 0)
    Sleep(100)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(70)
    Sleep(600)
    Sound(987, 0, 40, 0)
    Jump("loc_114D6")

    label("loc_11516")

    Return()

    # Function_131_114D0 end

    def Function_132_11517(): pass

    label("Function_132_11517")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11533")
    Sound(567, 0, 40, 0)
    Sleep(500)
    Sleep(500)
    Jump("Function_132_11517")

    label("loc_11533")

    Return()

    # Function_132_11517 end

    def Function_133_11534(): pass

    label("Function_133_11534")

    Sound(457, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(2000)
    Sound(458, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Return()

    # Function_133_11534 end

    def Function_134_1155F(): pass

    label("Function_134_1155F")

    Sound(457, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sleep(1000)
    Sound(458, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sleep(1500)
    Sound(486, 0, 100, 0)
    Sound(457, 0, 100, 0)
    Sleep(500)
    Sound(493, 0, 100, 0)
    Sleep(1000)
    Sound(494, 0, 100, 0)
    Sleep(1000)
    Sound(486, 0, 100, 0)
    Return()

    # Function_134_1155F end

    def Function_135_115AE(): pass

    label("Function_135_115AE")

    SetChrChipByIndex(0xFE, 0x9)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_115C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_115E6")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_115C8")

    label("loc_115E6")

    Return()

    # Function_135_115AE end

    def Function_136_115E7(): pass

    label("Function_136_115E7")

    SetChrChipByIndex(0xFE, 0xA)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11601")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11618")
    OP_A0(0xFE, 700, 0x0, 0x5)
    Jump("loc_11601")

    label("loc_11618")

    Return()

    # Function_136_115E7 end

    def Function_137_11619(): pass

    label("Function_137_11619")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
    Return()

    # Function_137_11619 end

    def Function_138_1164B(): pass

    label("Function_138_1164B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_116A0")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 136)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x1F4, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 137)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1388, 0x0)
    WaitChrThread(0xFE, 0)
    ClearChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 135)
    Sleep(1500)
    Jump("Function_138_1164B")

    label("loc_116A0")

    Return()

    # Function_138_1164B end

    def Function_139_116A1(): pass

    label("Function_139_116A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_116F6")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 136)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x1F4, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 137)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1388, 0x0)
    WaitChrThread(0xFE, 0)
    ClearChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 135)
    Sleep(1000)
    Jump("Function_139_116A1")

    label("loc_116F6")

    Return()

    # Function_139_116A1 end

    def Function_140_116F7(): pass

    label("Function_140_116F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1174C")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 136)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x2BC, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 137)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x1388, 0x0)
    WaitChrThread(0xFE, 0)
    ClearChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 135)
    Sleep(2000)
    Jump("Function_140_116F7")

    label("loc_1174C")

    Return()

    # Function_140_116F7 end

    def Function_141_1174D(): pass

    label("Function_141_1174D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_117A2")
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 136)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x384, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 137)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x1388, 0x0)
    WaitChrThread(0xFE, 0)
    ClearChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 135)
    Sleep(2500)
    Jump("Function_141_1174D")

    label("loc_117A2")

    Return()

    # Function_141_1174D end

    def Function_142_117A3(): pass

    label("Function_142_117A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51719.itc", 0x0)
    LoadChrToIndex("apl/ch51718.itc", 0x1)
    LoadChrToIndex("chr/ch32050.itc", 0x2)
    LoadChrToIndex("chr/ch32056.itc", 0x5)
    LoadChrToIndex("chr/ch32152.itc", 0x8)
    LoadChrToIndex("monster/ch85150.itc", 0x9)
    LoadChrToIndex("monster/ch85151.itc", 0xA)
    LoadChrToIndex("monster/ch85153.itc", 0xB)
    LoadChrToIndex("apl/ch50509.itc", 0xD)
    LoadChrToIndex("chr/ch30200.itc", 0xF)
    LoadChrToIndex("apl/ch51720.itc", 0x10)
    LoadChrToIndex("chr/ch30500.itc", 0x11)
    LoadChrToIndex("chr/ch30100.itc", 0x12)
    LoadChrToIndex("chr/ch30000.itc", 0x13)
    LoadChrToIndex("apl/ch51236.itc", 0x14)
    LoadChrToIndex("apl/ch51721.itc", 0x16)
    LoadChrToIndex("apl/ch51722.itc", 0x19)
    LoadChrToIndex("chr/ch30600.itc", 0x1F)
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    LoadEffect(0x1, "event/ev17061.eff")
    OP_8E(0x2F, "雾香")
    OP_8E(0x28, "雷克特")
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x32, 0x0)
    SetChrSubChip(0x32, 0x5)
    SetChrFlags(0x32, 0x8000)
    ClearChrFlags(0x32, 0x80)
    SetChrPos(0x32, 1900, 100, 4200, 45)
    SetChrChipByIndex(0x33, 0x1)
    SetChrSubChip(0x33, 0x5)
    SetChrFlags(0x33, 0x8000)
    ClearChrFlags(0x33, 0x80)
    SetChrPos(0x33, 2500, 100, 6500, 45)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    SetChrFlags(0x34, 0x8000)
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, -1500, 100, 6300, 0)
    SetChrChipByIndex(0x35, 0x8)
    SetChrSubChip(0x35, 0x1)
    SetChrFlags(0x35, 0x8000)
    ClearChrFlags(0x35, 0x80)
    SetChrPos(0x35, 500, 100, 4800, 0)
    SetChrChipByIndex(0x38, 0xF)
    SetChrSubChip(0x38, 0x0)
    SetChrFlags(0x38, 0x8000)
    ClearChrFlags(0x38, 0x80)
    SetChrPos(0x38, 3100, 250, -1700, 0)
    SetChrChipByIndex(0x48, 0x13)
    SetChrSubChip(0x48, 0x0)
    SetChrFlags(0x48, 0x8000)
    ClearChrFlags(0x48, 0x80)
    SetChrPos(0x48, 6100, 50, -700, 315)
    SetChrChipByIndex(0x3C, 0x13)
    SetChrSubChip(0x3C, 0x0)
    SetChrFlags(0x3C, 0x8000)
    ClearChrFlags(0x3C, 0x80)
    SetChrPos(0x3C, 7400, 0, -500, 315)
    SetChrChipByIndex(0x49, 0x13)
    SetChrSubChip(0x49, 0x0)
    SetChrFlags(0x49, 0x8000)
    ClearChrFlags(0x49, 0x80)
    SetChrPos(0x49, -3100, 250, -1700, 0)
    SetChrChipByIndex(0x39, 0x11)
    SetChrSubChip(0x39, 0x0)
    SetChrFlags(0x39, 0x8000)
    ClearChrFlags(0x39, 0x80)
    SetChrPos(0x39, -6100, 50, -700, 45)
    SetChrChipByIndex(0x4A, 0x13)
    SetChrSubChip(0x4A, 0x0)
    SetChrFlags(0x4A, 0x8000)
    ClearChrFlags(0x4A, 0x80)
    SetChrPos(0x4A, -7400, 0, -500, 45)
    SetChrChipByIndex(0x3B, 0x1F)
    SetChrSubChip(0x3B, 0x0)
    SetChrFlags(0x3B, 0x8000)
    ClearChrFlags(0x3B, 0x80)
    SetChrPos(0x3B, -6400, 0, -3000, 0)
    SetChrChipByIndex(0x3A, 0x12)
    SetChrSubChip(0x3A, 0x0)
    SetChrFlags(0x3A, 0x8000)
    ClearChrFlags(0x3A, 0x80)
    SetChrPos(0x3A, 4400, 0, -2200, 0)
    SetChrChipByIndex(0x23, 0xD)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -2000, 250, -1600, 0)
    SetChrChipByIndex(0x2F, 0x19)
    SetChrSubChip(0x2F, 0x0)
    SetChrFlags(0x2F, 0x8000)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x2F, -3000, 100, 6600, 315)
    SetChrChipByIndex(0x28, 0x16)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 4100, 100, 4800, 45)
    SetChrChipByIndex(0x3E, 0x9)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    OP_52(0x3E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3E, -8500, 0, 9500, 135)
    SetChrChipByIndex(0x3F, 0x9)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    OP_52(0x3F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3F, 8500, 0, 9500, 225)
    SetChrChipByIndex(0x40, 0x9)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    OP_52(0x40, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x40, -5500, 250, 10500, 135)
    SetChrChipByIndex(0x41, 0x9)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    OP_52(0x41, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x41, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x41, 5500, 250, 10500, 225)
    SetChrChipByIndex(0x42, 0x9)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    OP_52(0x42, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x42, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x42, 3000, 100, 15000, 180)
    SetChrChipByIndex(0x43, 0x9)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    OP_52(0x43, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x43, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x43, -3000, 100, 15000, 180)
    BeginChrThread(0x3E, 3, 0, 143)
    BeginChrThread(0x3F, 3, 0, 144)
    BeginChrThread(0x40, 3, 0, 145)
    BeginChrThread(0x41, 3, 0, 146)
    BeginChrThread(0x42, 3, 0, 147)
    BeginChrThread(0x43, 3, 0, 148)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x12, 0x71)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x71, -4500, 250, 800, 0)
    OP_D5(0x71, 0x0, 0xFFFEEE90, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x0)
    ClearChrFlags(0x72, 0x80)
    OP_78(0x16, 0x72)
    OP_49()
    SetChrPos(0x72, 4500, 250, 800, 0)
    OP_D5(0x72, 0x0, 0x11170, 0x0, 0x0)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_70(0x16, 0x0)
    OP_68(0, 1350, 9300, 0)
    MoveCamera(37, 17, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(2000, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1770)
    OP_11(0x8E, 0xC7, 0xFF, 0x1E, 0x26C, 0x1770)
    OP_68(0, 1250, 2300, 6000)
    MoveCamera(27, 17, 0, 6000)
    SetCameraDistance(16500, 6000)
    Sleep(2000)
    StopEffect(0x7, 0x2)
    OP_6F(0x79)

    #C0427
    ChrTalk(
        0x32,
        "#5P哦哦……！\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x38,
        "#12P消、消失了……！？\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x2F,
        (
            "#03400F……似乎是灵力的供给\x01",
            "断掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x28,
        (
            "#11P#11506F哎呀呀……\x01",
            "真是累死了～\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x23,
        (
            "#01002F哼……\x01",
            "干得不错嘛。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_142_117A3 end

    def Function_143_11EBE(): pass

    label("Function_143_11EBE")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x0, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(985, 0, 100, 0)
    Sleep(1800)

    def lambda_11F19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11F19)
    WaitChrThread(0xFE, 2)
    StopEffect(0x0, 0x2)
    Return()

    # Function_143_11EBE end

    def Function_144_11F2D(): pass

    label("Function_144_11F2D")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2400)

    def lambda_11F7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11F7F)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_144_11F2D end

    def Function_145_11F93(): pass

    label("Function_145_11F93")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2800)

    def lambda_11FE5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11FE5)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_145_11F93 end

    def Function_146_11FF9(): pass

    label("Function_146_11FF9")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2600)

    def lambda_1204B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1204B)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_146_11FF9 end

    def Function_147_1205F(): pass

    label("Function_147_1205F")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)

    def lambda_120B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_120B1)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_147_1205F end

    def Function_148_120C5(): pass

    label("Function_148_120C5")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2200)

    def lambda_12117():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12117)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_148_120C5 end

    def Function_149_1212B(): pass

    label("Function_149_1212B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0x9, 0x4)
    LoadChrToIndex("chr/ch31300.itc", 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    SetChrChipByIndex(0x48, 0x0)
    SetChrSubChip(0x48, 0x0)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x48, 0x4)
    SetChrFlags(0x48, 0x8000)
    SetChrPos(0x48, -2100, 0, -20500, 180)
    SetChrChipByIndex(0x49, 0x0)
    SetChrSubChip(0x49, 0x0)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x49, 0x4)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, 2100, 0, -20500, 180)
    SetChrChipByIndex(0x4A, 0x0)
    SetChrSubChip(0x4A, 0x0)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x49, 0x4)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, -900, 0, -15300, 90)
    SetChrChipByIndex(0x4B, 0x1)
    SetChrSubChip(0x4B, 0x0)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4B, 0x4)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, 200, 0, -15300, 270)
    SetChrChipByIndex(0x4C, 0x0)
    SetChrSubChip(0x4C, 0x0)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4C, 0x4)
    SetChrFlags(0x4C, 0x8000)
    SetChrPos(0x4C, 900, 0, -11600, 30)
    SetChrChipByIndex(0x4D, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4D, 0x4)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x4D, -2200, 0, -8900, 345)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x13, 0x71)
    SetMapObjFrame(0x13, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x71, -2500, 0, -16000, 0)
    OP_D5(0x71, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x0)
    ClearChrFlags(0x72, 0x80)
    OP_78(0xC, 0x72)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x72, 2500, 0, -16000, 0)
    OP_D5(0x72, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    OP_74(0xC, 0x1E)
    OP_70(0xC, 0x0)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x12, 0x73)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x73, 2300, 0, -9700, 300)
    OP_D5(0x73, 0x0, 0x493E0, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x0)
    ClearChrFlags(0x74, 0x80)
    OP_78(0xB, 0x74)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x74, -2300, 0, -5400, 70)
    OP_D5(0x74, 0x0, 0x11170, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    OP_74(0xB, 0x1E)
    OP_70(0xB, 0x0)
    OP_68(-1000, 1700, -17500, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_149_1212B end

    def Function_150_123EC(): pass

    label("Function_150_123EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0x9, 0x4)
    LoadChrToIndex("chr/ch05620.itc", 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    ClearChrFlags(0x71, 0x80)
    OP_78(0x13, 0x71)
    SetMapObjFrame(0x13, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x71, 0, 0, -8500, 270)
    OP_D5(0x71, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x186)
    SetChrChipByIndex(0x48, 0x0)
    SetChrSubChip(0x48, 0x0)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x48, 0x4)
    SetChrFlags(0x48, 0x8000)
    SetChrPos(0x48, -800, 0, -4900, 180)
    SetChrChipByIndex(0x49, 0x0)
    SetChrSubChip(0x49, 0x0)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x49, 0x4)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, 800, 0, -4900, 180)
    SetChrChipByIndex(0x4A, 0x0)
    SetChrSubChip(0x4A, 0x0)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4A, 0x4)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, -2500, 0, -6800, 45)
    SetChrChipByIndex(0x30, 0x1)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x30, 0x4)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 0, 0, -5000, 180)
    OP_68(0, 900, -7000, 0)
    MoveCamera(137, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_150_123EC end

    SaveToFile()

Try(main)
