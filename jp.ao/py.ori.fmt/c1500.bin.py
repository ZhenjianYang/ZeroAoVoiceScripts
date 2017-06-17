from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "カニング巡査",           # 1
        "マルティン巡査",         # 2
        "タジク",                 # 3
        "警官",                   # 4
        "警官",                   # 5
        "警官",                   # 6
        "警官",                   # 7
        "市役所職員",             # 8
        "市役所職員",             # 9
        "ミレイユ三尉",           # 10
        "市民",                   # 11
        "女の子",                 # 12
        "観光客",                 # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "観光客",                 # 17
        "観光客",                 # 18
        "キンドール",             # 19
        "リュウ",                 # 20
        "アンリ",                 # 21
        "モモ",                   # 22
        "シン",                   # 23
        "記者ノティシア",         # 24
        "ニールセン",             # 25
        "ダグラス副司令",         # 26
        "マクダエル議長",         # 27
        "セルゲイ課長",           # 28
        "壊れた支援課車",         # 29
        "新型装甲車",             # 30
        "新型装甲車",             # 31
        "オズボーン宰相",         # 32
        "レクター書記官",         # 33
        "オリヴァルト皇子",       # 34
        "ミュラー少佐",           # 35
        "クローディア姫",         # 36
        "ユリア准佐",             # 37
        "アルバート大公",         # 38
        "ロックスミス大統領",     # 39
        "キリカ補佐官",           # 40
        "ディーター市長",         # 41
        "マリアベル",             # 42
        "遊撃士スコット",         # 43
        "遊撃士ヴェンツェル",     # 44
        "遊撃士リン",             # 45
        "遊撃士エオリア",         # 46
        "アリオス国防長官",       # 47
        "ダドリー捜査官",         # 48
        "レイモンド捜査官",       # 49
        "エマ捜査官",             # 50
        "ジョーリッジ課長",       # 51
        "ケイト巡査長",           # 52
        "フランツ巡査",           # 53
        "ロイドたちの声",         # 54
        "イベント用モンスター",   # 55
        "イベント用モンスター",   # 56
        "イベント用モンスター",   # 57
        "イベント用モンスター",   # 58
        "イベント用モンスター",   # 59
        "イベント用モンスター",   # 60
        "イベント用モンスター",   # 61
        "イベント用モンスター",   # 62
        "イベント用モンスター",   # 63
        "ソーニャ司令",           # 64
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
        "警備隊",                 # 75
        "警備隊",                 # 76
        "警備隊",                 # 77
        "警備隊",                 # 78
        "警備隊",                 # 79
        "警備隊",                 # 80
        "警備隊",                 # 81
        "警備隊",                 # 82
        "秘書",                   # 83
        "執事",                   # 84
        "帝国軍士官",             # 85
        "帝国軍士官",             # 86
        "共和国軍士官",           # 87
        "共和国軍士官",           # 88
        "親衛隊",                 # 89
        "親衛隊",                 # 90
        "兵士カーター",           # 91
        "国防軍兵士・男",         # 92
        "国防軍兵士・男",         # 93
        "国防軍兵士・男",         # 94
        "国防軍兵士・男",         # 95
        "国防軍兵士・女",         # 96
        "国防軍兵士・女",         # 97
        "国防軍兵士・女",         # 98
        "国防軍仕官",             # 99
        "グレイス",               # 100
        "レインズ",               # 101
        "記者",                   # 102
        "記者",                   # 103
        "記者",                   # 104
        "記者",                   # 105
        "車",                     # 106
        "車",                     # 107
        "車",                     # 108
        "車",                     # 109
        "新型装甲車（Ａ）",       # 110
        "新型装甲車（Ｂ）",       # 111
        "偃月輪",                 # 112
        "偃月輪",                 # 113
        "SE制御",                 # 114
        "中央広場",               # 115
        "西通り",                 # 116
        "行政区",                 # 117
        "住宅街",                 # 118
        "歓楽街",                 # 119
        "東通り",                 # 120
        "旧市街",                 # 121
        "港湾区",                 # 122
        "ＩＢＣ",                 # 123
        "駅前通り",               # 124
        "裏通り",                 # 125
        "ウルスラ間道",           # 126
        "東クロスベル街道",       # 127
        "西クロスベル街道",       # 128
        "マインツ山道",           # 129
        "オルキスタワー",         # 130
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

    PlaceName(-20.690000534057617, 0.0, -334.95001220703125, 0x0000, 0x0000, "中央広場")
    PlaceName(-176.4499969482422, 0.0, -343.79998779296875, 0x0000, 0x0000, "西通り")
    PlaceName(21.639999389648438, 0.0, -191.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-276.45001220703125, 0.0, -223.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-142.5, 0.0, -222.60000610351562, 0x0000, 0x0000, "歓楽街")
    PlaceName(113.25, 0.0, -400.5, 0x0000, 0x0000, "東通り")
    PlaceName(183.5800018310547, 0.0, -513.25, 0x0000, 0x0000, "旧市街")
    PlaceName(154.9499969482422, 0.0, -274.3999938964844, 0x0000, 0x0000, "港湾区")
    PlaceName(126.94999694824219, 0.0, -96.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-17.75, 0.0, -493.6000061035156, 0x0000, 0x0000, "駅前通り")
    PlaceName(-101.80000305175781, 0.0, -283.20001220703125, 0x0000, 0x0000, "裏通り")
    PlaceName(-21.200000762939453, 0.0, -548.0499877929688, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(234.85000610351562, 0.0, -384.6000061035156, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-264.95001220703125, 0.0, -340.3999938964844, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-254.0500030517578, 0.0, -165.39999389648438, 0x0000, 0x0000, "マインツ山道")
    PlaceName(0.0, 0.0, 55.5, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_14_299C",        # 0E, 14
        "Function_15_335A",        # 0F, 15
        "Function_16_3CD4",        # 10, 16
        "Function_17_3E1A",        # 11, 17
        "Function_18_3E9D",        # 12, 18
        "Function_19_3F3C",        # 13, 19
        "Function_20_3FCD",        # 14, 20
        "Function_21_4067",        # 15, 21
        "Function_22_475B",        # 16, 22
        "Function_23_4873",        # 17, 23
        "Function_24_4973",        # 18, 24
        "Function_25_49AF",        # 19, 25
        "Function_26_4A16",        # 1A, 26
        "Function_27_4ABD",        # 1B, 27
        "Function_28_4B26",        # 1C, 28
        "Function_29_4FBF",        # 1D, 29
        "Function_30_5471",        # 1E, 30
        "Function_31_591D",        # 1F, 31
        "Function_32_5E43",        # 20, 32
        "Function_33_6330",        # 21, 33
        "Function_34_659E",        # 22, 34
        "Function_35_6911",        # 23, 35
        "Function_36_6B78",        # 24, 36
        "Function_37_6BD8",        # 25, 37
        "Function_38_6C30",        # 26, 38
        "Function_39_6E33",        # 27, 39
        "Function_40_6FB4",        # 28, 40
        "Function_41_6FF8",        # 29, 41
        "Function_42_7046",        # 2A, 42
        "Function_43_70BD",        # 2B, 43
        "Function_44_7180",        # 2C, 44
        "Function_45_8186",        # 2D, 45
        "Function_46_87F9",        # 2E, 46
        "Function_47_8D68",        # 2F, 47
        "Function_48_8DB5",        # 30, 48
        "Function_49_8E02",        # 31, 49
        "Function_50_8E4F",        # 32, 50
        "Function_51_8E9C",        # 33, 51
        "Function_52_AA19",        # 34, 52
        "Function_53_AAD2",        # 35, 53
        "Function_54_AC50",        # 36, 54
        "Function_55_AC76",        # 37, 55
        "Function_56_ACD1",        # 38, 56
        "Function_57_B12A",        # 39, 57
        "Function_58_B1C8",        # 3A, 58
        "Function_59_BA8D",        # 3B, 59
        "Function_60_BF06",        # 3C, 60
        "Function_61_C1A8",        # 3D, 61
        "Function_62_CF44",        # 3E, 62
        "Function_63_D003",        # 3F, 63
        "Function_64_D124",        # 40, 64
        "Function_65_D865",        # 41, 65
        "Function_66_D91E",        # 42, 66
        "Function_67_E4A6",        # 43, 67
        "Function_68_E4C2",        # 44, 68
        "Function_69_E4EB",        # 45, 69
        "Function_70_E5F9",        # 46, 70
        "Function_71_FF58",        # 47, 71
        "Function_72_FFC1",        # 48, 72
        "Function_73_10024",       # 49, 73
        "Function_74_10087",       # 4A, 74
        "Function_75_100EA",       # 4B, 75
        "Function_76_1015D",       # 4C, 76
        "Function_77_101C6",       # 4D, 77
        "Function_78_1021B",       # 4E, 78
        "Function_79_1028B",       # 4F, 79
        "Function_80_102FC",       # 50, 80
        "Function_81_104A3",       # 51, 81
        "Function_82_1064D",       # 52, 82
        "Function_83_107F4",       # 53, 83
        "Function_84_1083F",       # 54, 84
        "Function_85_1088E",       # 55, 85
        "Function_86_108F1",       # 56, 86
        "Function_87_10954",       # 57, 87
        "Function_88_109B7",       # 58, 88
        "Function_89_10A15",       # 59, 89
        "Function_90_10AA2",       # 5A, 90
        "Function_91_10C78",       # 5B, 91
        "Function_92_10CFB",       # 5C, 92
        "Function_93_10D7E",       # 5D, 93
        "Function_94_10E01",       # 5E, 94
        "Function_95_11145",       # 5F, 95
        "Function_96_1119B",       # 60, 96
        "Function_97_112BA",       # 61, 97
        "Function_98_11302",       # 62, 98
        "Function_99_115FA",       # 63, 99
        "Function_100_11688",      # 64, 100
        "Function_101_11796",      # 65, 101
        "Function_102_117C5",      # 66, 102
        "Function_103_1187E",      # 67, 103
        "Function_104_1198B",      # 68, 104
        "Function_105_11B02",      # 69, 105
        "Function_106_11B3B",      # 6A, 106
        "Function_107_1217B",      # 6B, 107
        "Function_108_12187",      # 6C, 108
        "Function_109_121AA",      # 6D, 109
        "Function_110_123F5",      # 6E, 110
        "Function_111_1248F",      # 6F, 111
        "Function_112_124F2",      # 70, 112
        "Function_113_12691",      # 71, 113
        "Function_114_126DC",      # 72, 114
        "Function_115_12776",      # 73, 115
        "Function_116_127DC",      # 74, 116
        "Function_117_12868",      # 75, 117
        "Function_118_12887",      # 76, 118
        "Function_119_12969",      # 77, 119
        "Function_120_12A3C",      # 78, 120
        "Function_121_12B71",      # 79, 121
        "Function_122_12B99",      # 7A, 122
        "Function_123_12C3A",      # 7B, 123
        "Function_124_12C90",      # 7C, 124
        "Function_125_12D63",      # 7D, 125
        "Function_126_12D82",      # 7E, 126
        "Function_127_12E2C",      # 7F, 127
        "Function_128_12E46",      # 80, 128
        "Function_129_12E60",      # 81, 129
        "Function_130_12E7A",      # 82, 130
        "Function_131_12EC1",      # 83, 131
        "Function_132_12F08",      # 84, 132
        "Function_133_12F25",      # 85, 133
        "Function_134_12F50",      # 86, 134
        "Function_135_12F9F",      # 87, 135
        "Function_136_12FD8",      # 88, 136
        "Function_137_1300A",      # 89, 137
        "Function_138_1303C",      # 8A, 138
        "Function_139_13092",      # 8B, 139
        "Function_140_130E8",      # 8C, 140
        "Function_141_1313E",      # 8D, 141
        "Function_142_13194",      # 8E, 142
        "Function_143_138C9",      # 8F, 143
        "Function_144_13938",      # 90, 144
        "Function_145_1399E",      # 91, 145
        "Function_146_13A04",      # 92, 146
        "Function_147_13A6A",      # 93, 147
        "Function_148_13AD0",      # 94, 148
        "Function_149_13B36",      # 95, 149
        "Function_150_13DF7",      # 96, 150
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20DF")

    #C0001
    ChrTalk(
        0xFE,
        (
            "国防軍兵士も一通り撤退したから、\x01",
            "俺たち警備課が改めて\x01",
            "配備されることになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "大変な状況だが、お互いがんばろうぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2998")

    label("loc_20DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20ED")
    Jump("loc_2998")

    label("loc_20ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_20FB")
    Jump("loc_2998")

    label("loc_20FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2219")

    #C0003
    ChrTalk(
        0xFE,
        (
            "オルキスタワー前の攻防は……\x01",
            "まさに熾烈を極めた戦いだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "正直アリオスさんがいなければ、\x01",
            "ここもＩＢＣのように……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……って、やれやれ。\x01",
            "自分で言ってて\x01",
            "何か恐ろしくなって来たぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "とにかく、ここは無事だった。\x01",
            "それ以上は考えても仕方ないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22CE")

    label("loc_2219")


    #C0007
    ChrTalk(
        0xFE,
        (
            "しかし、ダドリーさんも凄腕だが……\x01",
            "アリオスさんに至っては俺たちとは\x01",
            "まるで次元が違う強さだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "神業とも言える剣速に身のこなし……\x01",
            "《風の剣聖》とはよく言ったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CE")

    Jump("loc_2998")

    label("loc_22D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2381")

    #C0009
    ChrTalk(
        0xFE,
        (
            "マインツで占拠事件、か……\x01",
            "くっ、またとんでもない事が\x01",
            "起こったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "かなり状況はキツイらしいが、\x01",
            "警備隊には何としても\x01",
            "踏ん張ってもらわないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2998")

    label("loc_2381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_240B")

    #C0011
    ChrTalk(
        0xFE,
        (
            "雨の日は流石に、\x01",
            "この広場にも人気#4Rひとけ#がなくなるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "これだけ広い場所だと、\x01",
            "何つうか物悲しさもひとしおだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2998")

    label("loc_240B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24AE")

    #C0013
    ChrTalk(
        0xFE,
        (
            "さっき受付で聞いたんだが、\x01",
            "何でも列車が脱線したらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "既に捜査二課と警備隊が\x01",
            "調査に出向いたらしいが……\x01",
            "どの程度の被害かが気になるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2998")

    label("loc_24AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2561")

    #C0015
    ChrTalk(
        0xFE,
        (
            "このタワー前の広場も\x01",
            "市民の憩いの場として、\x01",
            "定着してきたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "仲良さそうに遊んでいる\x01",
            "家族連れなんかを見ていると、\x01",
            "ほのぼのして来るぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25C3")

    label("loc_2561")


    #C0017
    ChrTalk(
        0xFE,
        (
            "うららかな日差しと、\x01",
            "仲むつましい家族連れ……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "う～ん、こんなに\x01",
            "ほのぼのする画はないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C3")

    Jump("loc_2998")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26FB")

    #C0019
    ChrTalk(
        0xFE,
        (
            "通商会議が終わってから、\x01",
            "もう１ヶ月以上経つんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "テロリストたちの襲撃も\x01",
            "もちろん大きな事件だったが、\x01",
            "直後に独立の提唱が行われて……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "とかく、今年はホントに\x01",
            "大きな事件や出来事が立て続けに\x01",
            "起こるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "何つうか、目まぐるしくて\x01",
            "月日があっという間に感じるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2780")

    label("loc_26FB")


    #C0023
    ChrTalk(
        0xFE,
        (
            "とかく、今年はホントに\x01",
            "大きな事件や出来事が立て続けに\x01",
            "起こるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "何つうか、目まぐるしくて\x01",
            "月日があっという間に感じるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2780")

    Jump("loc_2998")

    label("loc_2785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281F")

    #C0025
    ChrTalk(
        0xFE,
        "よう、特務支援課じゃないか。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "君たちが通商会議の警備に\x01",
            "参加することは聞いてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "まあ、いつでも中に入ってくれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_287C")

    label("loc_281F")


    #C0028
    ChrTalk(
        0xFE,
        (
            "君たちが通商会議の警備に\x01",
            "参加することは聞いてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "まあ、いつでも中に入ってくれ。\x02",
    )

    CloseMessageWindow()

    label("loc_287C")

    Jump("loc_2998")

    label("loc_2881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292C")

    #C0030
    ChrTalk(
        0xFE,
        "おや、君たちは特務支援課だな。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの\x01",
            "警戒は俺たち警護課の担当だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ま、お互い警察同士、\x01",
            "何かあった時はよろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2998")

    label("loc_292C")


    #C0033
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの\x01",
            "警戒は俺たち警護課の担当だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ま、お互い警察同士、\x01",
            "何かあった時はよろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2998")

    TalkEnd(0xFE)
    Return()

    # Function_13_204C end

    def Function_14_299C(): pass

    label("Function_14_299C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A3C")

    #C0035
    ChrTalk(
        0xFE,
        (
            "ディーター大統領も、\x01",
            "３６Ｆで拘束されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "まさか、自分達の住む国の\x01",
            "トップを拘束する事になるなんて。\x01",
            "……いい気分はしませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A4A")
    Jump("loc_3356")

    label("loc_2A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A58")
    Jump("loc_3356")

    label("loc_2A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B22")

    #C0037
    ChrTalk(
        0xFE,
        (
            "《赤い星座》……\x01",
            "……本当に恐ろしい連中でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "個々の戦闘技術はもちろん、\x01",
            "武装の差も歴然で……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "もしもクロスベルに軍隊があれば、\x01",
            "状況は違っていたはずですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B88")

    label("loc_2B22")


    #C0040
    ChrTalk(
        0xFE,
        (
            "《赤い星座》……\x01",
            "……本当に恐ろしい連中でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "ですが、もしも\x01",
            "クロスベルに軍隊があれば……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B88")

    Jump("loc_3356")

    label("loc_2B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA0")

    #C0042
    ChrTalk(
        0xFE,
        (
            "こういう状況時だからこそ\x01",
            "我々警察は市民のために堂々と\x01",
            "構えていないといけません。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "警備隊同様、我々は日頃から\x01",
            "そのための訓練を積んでいる\x01",
            "わけですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "『常に市民の模範たれ』、\x01",
            "この言葉を改めて噛み締めて\x01",
            "お互い気合いを入れましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D4C")

    label("loc_2CA0")


    #C0045
    ChrTalk(
        0xFE,
        (
            "こういう状況時だからこそ\x01",
            "我々警察は市民のために堂々と\x01",
            "構えていないといけません。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "『常に市民の模範たれ』、\x01",
            "この言葉を改めて噛み締めて\x01",
            "お互い気合いを入れましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4C")

    Jump("loc_3356")

    label("loc_2D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E11")

    #C0047
    ChrTalk(
        0xFE,
        (
            "大陸横断鉄道は警備隊の活躍で\x01",
            "何とか昨日の内に\x01",
            "復旧できたとのことですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "もしこの雨に降られていたら、\x01",
            "色々と面倒もあったと思いますが……\x01",
            "迅速なる対応に敬意を覚えます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_2E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EA4")

    #C0049
    ChrTalk(
        0xFE,
        (
            "西クロスベル街道方面で\x01",
            "導力列車が脱線ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "このクロスベルでは\x01",
            "滅多に聞かない事故ですが、\x01",
            "一体何があったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_2EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F69")

    #C0051
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの運用がもっと\x01",
            "本格化すれば、この広場の人の出入りも\x01",
            "さらに活発になるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "そうなれば、仕事は忙しくなったとしても\x01",
            "一クロスベル人として喜ばしい限りです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_2F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C3")

    #C0053
    ChrTalk(
        0xFE,
        (
            "蒸し返すようですが、\x01",
            "通商会議のテロ事件には\x01",
            "本当に不覚を取らされましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "我々警官隊は防戦一方で、\x01",
            "最終的には２大国がそれぞれ\x01",
            "備えていた武力に頼る結果に……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "それに、今回はセキュリティも\x01",
            "逆手に取られたという話ですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "更なる危機管理は当然として、\x01",
            "自分たちも、もっと意識を高める\x01",
            "必要がありますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3161")

    label("loc_30C3")


    #C0057
    ChrTalk(
        0xFE,
        (
            "２重３重にも張られ、\x01",
            "信頼を置いていたはずの防衛線が\x01",
            "ああも簡単に……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "更なる危機管理は当然として、\x01",
            "自分たちも、もっと意識を高める\x01",
            "必要がありますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3161")

    Jump("loc_3356")

    label("loc_3166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31D7")

    #C0059
    ChrTalk(
        0xFE,
        "今日もお疲れ様です、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "通商会議が無事に終わるよう、\x01",
            "お互いに全力を尽くしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3356")

    label("loc_31D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A6")

    #C0061
    ChrTalk(
        0xFE,
        (
            "自分とカニング巡査はこの度、\x01",
            "オルキスタワーの警備要員として\x01",
            "配属されることになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "通商会議はもちろん、\x01",
            "以降もこの場に詰める予定ですので\x01",
            "どうぞ宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3356")

    label("loc_32A6")


    #C0063
    ChrTalk(
        0xFE,
        (
            "大陸中の注目を集める、\x01",
            "このオルキスタワーで働けることを\x01",
            "大変光栄に思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "当ビルに備えられた最新鋭の\x01",
            "セキュリティに甘んじることなく、\x01",
            "立派に務めを果たす所存です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3356")

    TalkEnd(0xFE)
    Return()

    # Function_14_299C end

    def Function_15_335A(): pass

    label("Function_15_335A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33EE")

    #C0065
    ChrTalk(
        0xFE,
        (
            "大統領があんな事になっちまって、\x01",
            "クロスベルはこれから\x01",
            "どうなっちまうのかねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "……まあ、なるようにしか\x01",
            "ならねえわな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD0")

    label("loc_33EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33FC")
    Jump("loc_3CD0")

    label("loc_33FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_340A")
    Jump("loc_3CD0")

    label("loc_340A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_35A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351E")

    #C0067
    ChrTalk(
        0xFE,
        (
            "襲撃の時、俺は財務課のフロアにいて\x01",
            "地下に避難することになったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "全員が全員エレベーターを\x01",
            "使うわけにも行かず、\x01",
            "若い男連中は階段を使ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "ちなみに、\x01",
            "財務課は３１Ｆにあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "……あの時は\x01",
            "息切れで死にそうになったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_359C")

    label("loc_351E")


    #C0071
    ChrTalk(
        0xFE,
        (
            "まさか、この高層ビルを階段で\x01",
            "駆け下りるとは思わなかったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "なんつーか、日頃からの\x01",
            "体力作りってヤツは大事だよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_359C")

    Jump("loc_3CD0")

    label("loc_35A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_36E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3669")

    #C0073
    ChrTalk(
        0xFE,
        "猟兵団と警備隊が交戦中、か。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "また余計な出費がかさみそうだが……\x01",
            "なんて、んなこと\x01",
            "言ってる場合じゃねえよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "とにかく一刻も早い\x01",
            "事態の収束を女神に祈ってるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36DF")

    label("loc_3669")


    #C0076
    ChrTalk(
        0xFE,
        (
            "ったく、最近はでかい事件が続いて\x01",
            "ほとほと参っちまうよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "とにかく一刻も早い\x01",
            "事態の収束を女神に祈ってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DF")

    Jump("loc_3CD0")

    label("loc_36E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36F2")
    Jump("loc_3CD0")

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_385F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D4")

    #C0078
    ChrTalk(
        0xFE,
        (
            "何かよく分からねえけど、\x01",
            "列車が停まっちまってるんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "大陸経済の大動脈が機能停止……\x01",
            "なんてマジで笑えねえ冗談だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "早いとこ復旧してもらわねえと、\x01",
            "たちまち大問題になっちまうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_385A")

    label("loc_37D4")


    #C0081
    ChrTalk(
        0xFE,
        (
            "大陸経済の大動脈が機能停止……\x01",
            "なんてマジで笑えねえ冗談だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "早いとこ復旧してもらわねえと、\x01",
            "たちまち大問題になっちまうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385A")

    Jump("loc_3CD0")

    label("loc_385F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3917")

    #C0083
    ChrTalk(
        0xFE,
        (
            "ディーター市長は、自分の\x01",
            "交際費や旅費に公費を充てずに\x01",
            "全て自腹で払ってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "流石はＩＢＣ総裁っつうか……\x01",
            "あの人の場合は、太っ腹の域を\x01",
            "優に超えちまってるよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD0")

    label("loc_3917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A93")

    #C0085
    ChrTalk(
        0xFE,
        (
            "クロスベルを国家に、か……\x01",
            "まさかクロイス市長が\x01",
            "ここまで大胆な方だったとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "俺も財務課にいるから\x01",
            "税収の譲渡制度が頭の痛い\x01",
            "問題なのは分かってるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "従属国関連の問題ってのはとにかく\x01",
            "口に出すことすらタブーだったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "２大国は既に当然\x01",
            "否定的な声明を出しているし……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "今後両国がどう動くか、\x01",
            "俺にはそれが心配でたまらねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B37")

    label("loc_3A93")


    #C0090
    ChrTalk(
        0xFE,
        (
            "住民投票はあくまでも\x01",
            "独立に対する市民の意志を\x01",
            "問うものだという話だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "いずれにせよ２大国が\x01",
            "いい顔をするわけがないからな。\x01",
            "今後の両国の動静が心配だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B37")

    Jump("loc_3CD0")

    label("loc_3B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B4A")
    Jump("loc_3CD0")

    label("loc_3B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C38")

    #C0092
    ChrTalk(
        0xFE,
        (
            "はー、まさかオルキスタワーが\x01",
            "本当に完成するとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "ＩＢＣの資本を惜しげもなく\x01",
            "公共事業に投入する\x01",
            "ディーター市長の心意気……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "私腹を肥やすことだけに\x01",
            "熱心などこぞの議員先生方とは\x01",
            "役者が違うよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CD0")

    label("loc_3C38")


    #C0095
    ChrTalk(
        0xFE,
        (
            "ＩＢＣの資本を惜しげもなく\x01",
            "公共事業に投入する\x01",
            "ディーター市長の心意気……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "私腹を肥やすことだけに\x01",
            "熱心などこぞの議員先生方とは\x01",
            "役者が違うよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD0")

    TalkEnd(0xFE)
    Return()

    # Function_15_335A end

    def Function_16_3CD4(): pass

    label("Function_16_3CD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA6")

    #C0097
    ChrTalk(
        0xFE,
        (
            "ついに『オルキスタワー』が\x01",
            "その姿を市民たちに……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "空にも届くこの威容、\x01",
            "そして蒼と白を基調とした\x01",
            "外観は実に美しい……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "やはり、デザインを引き受けて\x01",
            "本当によかった……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3E08")

    label("loc_3DA6")


    #C0100
    ChrTalk(
        0xFE,
        (
            "地上４０階のビルのデザインは\x01",
            "困難を極めたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "……ウム……\x01",
            "目頭が熱くなってしまうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E08")

    Jump("loc_3E16")

    label("loc_3E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E16")

    label("loc_3E16")

    TalkEnd(0xFE)
    Return()

    # Function_16_3CD4 end

    def Function_17_3E1A(): pass

    label("Function_17_3E1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2F")
    Call(0, 21)
    Jump("loc_3E99")

    label("loc_3E2F")


    #C0102
    ChrTalk(
        0xFE,
        (
            "そういえばキーアちゃん、\x01",
            "だいじょうぶかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "百貨店の屋上で、\x01",
            "なんだか様子がヘンだったけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E99")

    TalkEnd(0xFE)
    Return()

    # Function_17_3E1A end

    def Function_18_3E9D(): pass

    label("Function_18_3E9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB2")
    Call(0, 21)
    Jump("loc_3F38")

    label("loc_3EB2")


    #C0104
    ChrTalk(
        0xFE,
        (
            "シン、言葉づかいはエラソーだけど\x01",
            "根はいいやつっぽいんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "明日には帰っちゃうそうだし、\x01",
            "今のうちに一杯遊んどかなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F38")

    TalkEnd(0xFE)
    Return()

    # Function_18_3E9D end

    def Function_19_3F3C(): pass

    label("Function_19_3F3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F51")
    Call(0, 21)
    Jump("loc_3FC9")

    label("loc_3F51")


    #C0106
    ChrTalk(
        0xFE,
        (
            "それにしてもオルキスタワー……\x01",
            "想像したよりもず～っと\x01",
            "かっこいい建物でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "できたら中に入ってみたいです。\x02",
    )

    CloseMessageWindow()

    label("loc_3FC9")

    TalkEnd(0xFE)
    Return()

    # Function_19_3F3C end

    def Function_20_3FCD(): pass

    label("Function_20_3FCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE2")
    Call(0, 21)
    Jump("loc_4063")

    label("loc_3FE2")


    #C0108
    ChrTalk(
        0xFE,
        (
            "フ、フン……\x01",
            "ボンゾクはこれだから困るんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "とにかく……\x01",
            "ボクの輝かしい未来のためにも、\x01",
            "しっかり見物しておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4063")

    TalkEnd(0xFE)
    Return()

    # Function_20_3FCD end

    def Function_21_4067(): pass

    label("Function_21_4067")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41FB")

    #C0110
    ChrTalk(
        0x101,
        "#00005Fあれ、シンじゃないか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    #C0111
    ChrTalk(
        0x1E,
        (
            "あっ……\x01",
            "お前たちは昨日の！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)

    #C0112
    ChrTalk(
        0x1E,
        "お姉さん、こんにちは！！\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、こんにちは、\x01",
            "リュウ君たちと一緒にいたのね？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x1E,
        (
            "ええ、そうなんです。\x01",
            "こいつらがどうしてもって\x01",
            "言うから仕方なく……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1E, 500)

    #C0115
    ChrTalk(
        0x1B,
        "んなこと言ってないだろ～？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x1B,
        (
            "キーアとシズクが帰っちゃって\x01",
            "寂しそうにしてたから、\x01",
            "仲間に入れてやったってわけ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CF")

    label("loc_41FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4447")

    #C0117
    ChrTalk(
        0x101,
        "#00005Fあれ、君は確か……シン？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    #C0118
    ChrTalk(
        0x1E,
        (
            "あっ……\x01",
            "お前たちは昨日の！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1E,
        (
            "ボクの案内を引き受けずに、\x01",
            "何をしてたんだっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        (
            "#00106Fごめんなさい、シン君。\x01",
            "私たちもどうしても\x01",
            "手が離せなくて……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x102, 500)

    #C0121
    ChrTalk(
        0x1E,
        (
            "うっ……い、いやその。\x01",
            "お姉さんを攻めたわけじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1E,
        (
            "……フン、まあいい。\x01",
            "部下の案内は面白くなかったけど、\x01",
            "一通り街の見物はできたしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#00300Fにしても、今日は\x01",
            "坊主たちと一緒にいたんだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x104, 500)

    #C0124
    ChrTalk(
        0x1B,
        (
            "ああ、デパートの屋上で\x01",
            "除幕式を一緒に見てて、\x01",
            "そのまま遊んでるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x1B,
        (
            "なんだか１人で寂しそうだったから\x01",
            "仲間に入れてやったってわけ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CF")

    label("loc_4447")


    #C0126
    ChrTalk(
        0x101,
        (
            "#00002Fやあ、リュウ達じゃないか。\x02\x03",

            "#00005F……あれ、なんだか\x01",
            "見慣れない子がいるな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x0, 500)

    #C0127
    ChrTalk(
        0x1E,
        (
            "なんだ、おまえたちは。\x01",
            "リュウたちの知り合いか？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x1E,
        "いいか、このボクは黒──\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x0, 500)

    #C0129
    ChrTalk(
        0x1B,
        (
            "まあ、よく分かんないんだけど\x01",
            "共和国からの旅行者みたいでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x1B,
        (
            "デパートの屋上で\x01",
            "除幕式を一緒に見てたから、\x01",
            "そのまま遊んでるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1B,
        (
            "なんだか１人で寂しそうだったから\x01",
            "仲間に入れてやったってわけ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CF")

    TurnDirection(0x1E, 0x1B, 500)

    #C0132
    ChrTalk(
        0x1E,
        (
            "だ、誰が寂しくしていた……\x01",
            "言いがかりは止めてもらおう！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x1B,
        (
            "いーや、してたね！\x01",
            "なあモモ、してたよなー？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)

    #C0134
    ChrTalk(
        0x1D,
        "え、えと、その……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)

    #C0135
    ChrTalk(
        0x1C,
        (
            "ちょ、ちょっとリュウってば、\x01",
            "からかうのはやめてあげなよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46FA")

    #C0136
    ChrTalk(
        0x101,
        (
            "#00002F（はは、なんだかんだで\x01",
            "  馴染んでるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472B")

    label("loc_46FA")


    #C0137
    ChrTalk(
        0x101,
        "#00002F（はは、仲良く遊んでるみたいだな。）\x02",
    )

    CloseMessageWindow()

    label("loc_472B")

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

    # Function_21_4067 end

    def Function_22_475B(): pass

    label("Function_22_475B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47F4")

    #C0138
    ChrTalk(
        0xFE,
        (
            "今の所、テロリストの気配は\x01",
            "こちらでは感じてはいないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "流石に正面から来るとは思えないが……\x01",
            "とにかく引き続き警戒を続けるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_486F")

    label("loc_47F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_486F")

    #C0140
    ChrTalk(
        0xFE,
        (
            "やあ、こんにちは。\x01",
            "この広場はとてもいい場所だろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "クロスベルの新たな名所に\x01",
            "なること間違いなしだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486F")

    TalkEnd(0xFE)
    Return()

    # Function_22_475B end

    def Function_23_4873(): pass

    label("Function_23_4873")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4903")

    #C0142
    ChrTalk(
        0xFE,
        (
            "オルキスタワーは本日一杯、\x01",
            "関係者以外の立ち入りを\x01",
            "制限しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "皆さんは特務支援課ですね。\x01",
            "どうぞお通りください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_496F")

    label("loc_4903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_496F")

    #C0144
    ChrTalk(
        0xFE,
        "オルキスタワーへようこそ。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "広場への出入りはご自由ですので\x01",
            "よければ是非お立ち寄り下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496F")

    TalkEnd(0xFE)
    Return()

    # Function_23_4873 end

    def Function_24_4973(): pass

    label("Function_24_4973")

    TalkBegin(0xFE)

    #C0146
    ChrTalk(
        0xFE,
        (
            "お疲れ様です皆さん。\x01",
            "広場の方、異常ありません。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4973 end

    def Function_25_49AF(): pass

    label("Function_25_49AF")

    TalkBegin(0xFE)

    #C0147
    ChrTalk(
        0xFE,
        (
            "ふう、とうとう\x01",
            "本会議が開かれるんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "少し緊張して来たが……\x01",
            "リラックスしないとな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_49AF end

    def Function_26_4A16(): pass

    label("Function_26_4A16")

    TalkBegin(0xFE)

    #C0149
    ChrTalk(
        0xFE,
        (
            "い、いいかい、首脳たちを\x01",
            "出迎える時は笑顔でくれぐれも\x01",
            "失礼のないように。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "もし万が一、粗相でも\x01",
            "働こうものなら僕らの首なんて\x01",
            "一瞬で吹き飛ぶんだからね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_4A16 end

    def Function_27_4ABD(): pass

    label("Function_27_4ABD")

    TalkBegin(0xFE)

    #C0151
    ChrTalk(
        0xFE,
        (
            "ぶ、部長ぉ～、\x01",
            "そんなの分かってますってば。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "下手にプレッシャーを\x01",
            "かけないで下さいよぉ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_4ABD end

    def Function_28_4B26(): pass

    label("Function_28_4B26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B44")
    Call(0, 30)
    Jump("loc_4F23")

    label("loc_4B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E93")

    #C0153
    ChrTalk(
        0x11,
        "#07902F皆さん……それにランディ。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#00302Fよう、ミレイユ。\x01",
            "部隊には無事復帰できたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x11,
        (
            "#07904Fええ、おかげさまでね。\x02\x03",

            "#07902F規律に背いて隊を離れた私たちを、\x01",
            "司令は快く迎え入れてくれたわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CB2")

    #C0156
    ChrTalk(
        0x109,
        (
            "#10100Fふふ、ソーニャ司令なら\x01",
            "当然の対応だと思います。\x02\x03",

            "ミレイユ三尉のような優秀な方は\x01",
            "１人でも欲しい状況でしょうし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D30")

    label("loc_4CB2")


    #C0157
    ChrTalk(
        0x103,
        (
            "#00204Fソーニャ司令ならではの\x01",
            "柔軟な対応ですね。\x02\x03",

            "#00202Fミレイユ三尉のような優秀な方は\x01",
            "１人でも欲しい状況でしょうし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D30")


    #C0158
    ChrTalk(
        0x11,
        (
            "#07904Fふふ、優秀かどうかは\x01",
            "分からないけど……\x02\x03",

            "#07902Fこうして戻ってきた以上、\x01",
            "力を尽くさせてもらうつもりよ。\x02\x03",

            "国防軍や警備隊である前に、\x01",
            "クロスベルを守る使命を持つ\x01",
            "１人の人間としてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#00300F頑張れよ、ミレイユ。\x02\x03",

            "#00309Fま、張り切りすぎて\x01",
            "空回りしないようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x11,
        (
            "#07906Fい、言われなくても分かってるわよ！\x01",
            "……もう、馬鹿ランディ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 2)
    Jump("loc_4F23")

    label("loc_4E93")


    #C0161
    ChrTalk(
        0x11,
        (
            "#07902Fこうして戻ってきた以上、\x01",
            "力を尽くさせてもらうつもりよ。\x02\x03",

            "国防軍や警備隊である前に、\x01",
            "クロスベルを守る使命を持つ\x01",
            "１人の人間としてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F23")

    Jump("loc_4FBB")

    label("loc_4F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F43")
    Call(0, 45)
    Jump("loc_4FBB")

    label("loc_4F43")


    #C0162
    ChrTalk(
        0x11,
        (
            "#07903F私たちも、部隊を編成して\x01",
            "きっと後から駆けつける。\x02\x03",

            "#07901Fだから皆さん……\x01",
            "あの馬鹿のこと、どうかお願いね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FBB")

    TalkEnd(0xFE)
    Return()

    # Function_28_4B26 end

    def Function_29_4FBF(): pass

    label("Function_29_4FBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD4")
    Call(0, 30)
    Jump("loc_546D")

    label("loc_4FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52CE")

    #C0163
    ChrTalk(
        0x22,
        (
            "#02501Fディーター君が拘束された影響は、\x01",
            "じきに国内外に広がっていくはずだ。\x02\x03",

            "例えこの事態を収拾したとしても、\x01",
            "これから先、クロスベルには\x01",
            "数々の苦難が待っていることだろう。\x02\x03",

            "#02503F……思えば、ディーター君には\x01",
            "クロスベルの未来という重荷を\x01",
            "背負わせすぎていたのかもしれん。\x02\x03",

            "自治州代表の１人として、\x01",
            "こうなる前に何とか出来なかったものか……\x01",
            "己が無力さを痛感してしまうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        "#00108Fおじいさま……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        (
            "#00003F……今回の件に関しては、\x01",
            "それこそクロスベル全体の\x01",
            "問題だったと思います。\x02\x03",

            "#00000Fこれからどうしていくか……\x01",
            "それが大切なんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x22,
        (
            "#02503F……うむ、その通りだな。\x02\x03",

            "#02500Fとにかく、今は目の前にある問題を\x01",
            "一つ一つ解決していくとしよう。\x02\x03",

            "若い君たちには\x01",
            "大変な苦労をかけてしまうが……\x01",
            "今しばらく力を貸してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 3)
    Jump("loc_546D")

    label("loc_52CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53CA")

    #C0167
    ChrTalk(
        0x22,
        (
            "#02503Fとにかく、今は目の前にある問題を\x01",
            "一つ一つ解決していくとしよう。\x02\x03",

            "#02500Fクロスベル自治州の代表として、\x01",
            "何としてもこの事態を収拾しなければな。\x02\x03",

            "若い君たちには\x01",
            "大変な苦労をかけてしまうが……\x01",
            "今しばらく力を貸してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_546D")

    label("loc_53CA")


    #C0168
    ChrTalk(
        0x22,
        (
            "#02503Fとにかく、今は目の前にある問題を\x01",
            "一つ一つ解決していくとしよう。\x02\x03",

            "#02500F若い君たちには\x01",
            "大変な苦労をかけてしまうが……\x01",
            "今しばらく力を貸してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_546D")

    TalkEnd(0xFE)
    Return()

    # Function_29_4FBF end

    def Function_30_5471(): pass

    label("Function_30_5471")

    OP_4B(0x22, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x23, 0xFF)

    #C0169
    ChrTalk(
        0x22,
        (
            "#02503F大統領が拘束された噂は\x01",
            "すでに内外に広まっているようだ。\x02\x03",

            "#02500F２大国への警戒も\x01",
            "怠ることはできん状況だが……\x01",
            "……各地の状況はどうなっているかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x21,
        (
            "やはり、あの《大樹》の出現に\x01",
            "各方面で混乱が出ています。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x21,
        (
            "それと、結界が消えた影響で\x01",
            "ウルスラ病院行きを希望する市民が\x01",
            "多数出ているようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x21,
        (
            "それに関しては、ミレイユ三尉に\x01",
            "先んじて対応を指示しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x11,
        (
            "#07903F市外との行き来に関しては\x01",
            "各街道に小隊を投入して\x01",
            "移動車両の護衛を増員しています。\x02\x03",

            "#07900F現在、大統領の制限下における\x01",
            "数倍の市民の輸送が可能です。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x22,
        (
            "#02503Fふむ、迅速な対応に感謝する。\x02\x03",

            "#02500F私の方は自治州議会の議長として\x01",
            "公の場で、大統領の拘束について\x01",
            "説明をする必要があるだろう。\x02\x03",

            "すでに市民会館の方に\x01",
            "会見の準備を手配しておいたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x23,
        (
            "#01002Fそれに関しては、大統領の用意した\x01",
            "スクリーン車も利用できるでしょう。\x02\x03",

            "そっちは市内にいる警察で分担して\x01",
            "準備するとしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x22,
        (
            "#02503Fすまぬ、よろしく頼むとしよう。\x02\x03",

            "#02501F２大国への警戒も怠ることはできん……\x01",
            "諸君も十分に注意してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#00001F（マクダエル議長たちは\x01",
            "  各方面の対応に\x01",
            "  追われてるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        (
            "#00100F（ここはおじいさまたちに\x01",
            "  お任せして大丈夫でしょう。）\x02",
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

    # Function_30_5471 end

    def Function_31_591D(): pass

    label("Function_31_591D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5932")
    Call(0, 30)
    Jump("loc_5E3F")

    label("loc_5932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9C")

    #C0179
    ChrTalk(
        0x23,
        (
            "#01002Fお前たちか……\x01",
            "どうした、何かあったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、こちらの状況は\x01",
            "どうなっているかと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x23,
        (
            "#01003Fまあ、見ての通り\x01",
            "今後の対応を各方面で協議中だ。\x02\x03",

            "#01001F俺も警察の連絡役として\x01",
            "こっちに出向かせてもらってる所でな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A7B")

    #C0182
    ChrTalk(
        0x10A,
        (
            "#00604Fふむ……\x01",
            "セルゲイさんなら適任でしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAA")

    label("loc_5A7B")


    #C0183
    ChrTalk(
        0x103,
        "#00204Fなるほど、課長なら適任そうですね。\x02",
    )

    CloseMessageWindow()

    label("loc_5AAA")


    #C0184
    ChrTalk(
        0x104,
        (
            "#00300Fそうすっと……\x01",
            "支援課はガラガラになってるわけか。\x01",
            "依頼とかは入ってないんッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x23,
        (
            "#01002F各地からこまごまとした依頼が\x01",
            "多数入ってはいるが、それらは\x01",
            "ギルドに一任することにした。\x02\x03",

            "#01004Fお前たちが依頼のことを\x01",
            "心配する必要は無いだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x103,
        "#00205Fそうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00104Fギルドに任せられるなら\x01",
            "私たちも安心です。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x23,
        (
            "#01004Fとにかく、お前たちはお前たちで\x01",
            "納得できるまでやって来い。\x02\x03",

            "#01002F『特務支援課』として……\x01",
            "何よりもお前たち自身としてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        "#00002Fはい……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 4)
    Jump("loc_5E3F")

    label("loc_5C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DAB")

    #C0190
    ChrTalk(
        0x23,
        (
            "#01003F……ちなみに大統領は、\x01",
            "タワー３６Ｆの一室に\x01",
            "身柄を拘束している状態だ。\x02\x03",

            "現状、護送も後回しだからな。\x01",
            "抵抗する意思もないようだし、\x01",
            "最低限の見張りだけをつけている。\x02\x03",

            "#01002Fまあ、気が向いたら面会するといい。\x01",
            "改めて聞ける話もあるだろうからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E3F")

    label("loc_5DAB")


    #C0191
    ChrTalk(
        0x23,
        (
            "#01003F大統領は、タワー３６Ｆの一室に\x01",
            "身柄を拘束している状態だ。\x02\x03",

            "#01002Fまあ、気が向いたら面会するといい。\x01",
            "改めて聞ける話もあるだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E3F")

    TalkEnd(0xFE)
    Return()

    # Function_31_591D end

    def Function_32_5E43(): pass

    label("Function_32_5E43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E58")
    Call(0, 30)
    Jump("loc_632C")

    label("loc_5E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6198")

    #C0192
    ChrTalk(
        0x104,
        (
            "#00300Fダグラスのオッサン、\x01",
            "こっちに来てたんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ECD")

    #C0193
    ChrTalk(
        0x109,
        "#10100Fお疲れ様です、副司令！\x02",
    )

    CloseMessageWindow()

    label("loc_5ECD")


    #C0194
    ChrTalk(
        0xFE,
        (
            "お前さんたちか。\x01",
            "はは、久しぶりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "ソーニャ司令に頼まれて、\x01",
            "国防軍側の代表として\x01",
            "来ているところでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#00005Fそうだったんですか。\x02\x03",

            "#00000Fそれにしても、その制服……\x01",
            "国防軍としての姿は初めてですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "ハハ、警備隊の頃に比べると\x01",
            "少々窮屈に見えるだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "ある程度の収拾がつくまでは\x01",
            "このまま活動することになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00103F……やはり、状況は芳しく\x01",
            "ないみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "ああ……市内を包んでいた結界や\x01",
            "あの《神機》までもが失われた今、\x01",
            "２大国への警戒は厳にすべきだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "……まあ、すぐに侵攻が\x01",
            "始まるわけでもないだろうし、\x01",
            "こちらは俺たちに任せておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "お前さんたちはお前さんたちにしか\x01",
            "できないことをすればいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#00000Fええ……\x01",
            "そちらはよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 5)
    Jump("loc_632C")

    label("loc_6198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6297")

    #C0204
    ChrTalk(
        0xFE,
        (
            "大統領の拘束の報せが届いてから、\x01",
            "司令は時折考えるような仕草を\x01",
            "見せていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "……彼女は責任感が強いお人だ。\x01",
            "おそらく自分の進退も含めて、\x01",
            "様々な思いを巡らせているのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "副司令として、今はしっかりと\x01",
            "支えていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_632C")

    label("loc_6297")


    #C0207
    ChrTalk(
        0xFE,
        (
            "すぐに２大国の侵攻が\x01",
            "始まるわけでもないだろうし、\x01",
            "こちらは俺たちに任せておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "お前さんたちはお前さんたちにしか\x01",
            "できないことをすればいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_632C")

    TalkEnd(0xFE)
    Return()

    # Function_32_5E43 end

    def Function_33_6330(): pass

    label("Function_33_6330")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C7")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63A1")

    #C0209
    ChrTalk(
        0x109,
        "#10105Fあっ……\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#00005F支援課で使ってる車……\x01",
            "ここに移動されたのか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E3")

    label("loc_63A1")


    #C0211
    ChrTalk(
        0x101,
        (
            "#00005Fあ……\x02\x03",

            "支援課で使ってる車……\x01",
            "ここに移動されたのか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E3")


    #C0212
    ChrTalk(
        0x102,
        (
            "#00106F可哀想だけど……\x01",
            "しばらくはこの状態のまま\x01",
            "置いておくしかなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x104,
        (
            "#00306Fまあ、こんな状況だし\x01",
            "しゃあねえだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x103,
        (
            "#00202F一通り片付いたら、\x01",
            "きっと修理してあげましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#00000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 6)
    Jump("loc_659A")

    label("loc_64C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6541")

    #C0216
    ChrTalk(
        0x109,
        (
            "#10100F事件が終わったら、\x01",
            "きっと修理してあげましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        "#00004Fああ……ひとまず、お疲れ様。\x02",
    )

    CloseMessageWindow()
    Jump("loc_659A")

    label("loc_6541")


    #C0218
    ChrTalk(
        0x101,
        (
            "#00000F事件が終わったら、\x01",
            "きっと修理してあげよう。\x02\x03",

            "#00004F……ひとまず、お疲れ様。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_659A")

    TalkEnd(0xFF)
    Return()

    # Function_33_6330 end

    def Function_34_659E(): pass

    label("Function_34_659E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_65AF")
    Jump("loc_690D")

    label("loc_65AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_669B")

    #C0219
    ChrTalk(
        0xFE,
        (
            "私と娘は、あの襲撃の際も\x01",
            "この広場にいたのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "ビルへの避難を指示された時は\x01",
            "本当に生きた心地がしなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "ここを死守してくれたっていう\x01",
            "アリオスさんや他の皆さん方には\x01",
            "ほんと感謝してもしきれないわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_669B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6723")

    #C0222
    ChrTalk(
        0xFE,
        (
            "今日もこんなに良い天気なのに、\x01",
            "占拠事件だなんて悲しいわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "一体なぜ、こんなことが\x01",
            "起こってしまうのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_6723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6731")
    Jump("loc_690D")

    label("loc_6731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6790")

    #C0224
    ChrTalk(
        0xFE,
        "さてと、そろそろお昼時ね。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "持ってきたサンドイッチでも\x01",
            "食べようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_6790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67EB")

    #C0226
    ChrTalk(
        0xFE,
        "ふふ、今日も良い天気ね。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "晴天の空にオルキスタワーが\x01",
            "よく映えるわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_67EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6865")

    #C0228
    ChrTalk(
        0xFE,
        (
            "ふふ、やっぱり\x01",
            "この広場は素敵な場所ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "繁華街からはちょっと遠いけど、\x01",
            "ついつい足を運んじゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_690D")

    label("loc_6865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6873")
    Jump("loc_690D")

    label("loc_6873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_690D")

    #C0230
    ChrTalk(
        0xFE,
        (
            "ふふ、何だかここで除幕式が\x01",
            "あったばかりなんて思えないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "こんな素敵な場所を\x01",
            "初日から開放してくれるなんて\x01",
            "ディーター市長も太っ腹ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_690D")

    TalkEnd(0xFE)
    Return()

    # Function_34_659E end

    def Function_35_6911(): pass

    label("Function_35_6911")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6922")
    Jump("loc_6B74")

    label("loc_6922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_69A6")

    #C0232
    ChrTalk(
        0xFE,
        (
            "アリオスさんって人と\x01",
            "ケーサツの人たちがわたしたちを\x01",
            "守ってくれたんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "たくさんたくさん、カンシャなの♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_69A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6A04")

    #C0234
    ChrTalk(
        0xFE,
        (
            "今日はママ、なんだか\x01",
            "むずかしいお顔をしているの。\x01",
            "ゲンキだしてほしいな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_6A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6A12")
    Jump("loc_6B74")

    label("loc_6A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6A46")

    #C0235
    ChrTalk(
        0xFE,
        "ゴハン、ゴハン、おひるゴハーン♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_6A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A97")

    #C0236
    ChrTalk(
        0xFE,
        (
            "テンキ、テンキ、イイテンキー♪\x01",
            "アメアメふるな、アメふるなー♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_6A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6AEB")

    #C0237
    ChrTalk(
        0xFE,
        (
            "えへへー、今日もママと\x01",
            "おさんぽしてここまで来たの。\x01",
            "るんるるん♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B74")

    label("loc_6AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6AF9")
    Jump("loc_6B74")

    label("loc_6AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B74")

    #C0238
    ChrTalk(
        0xFE,
        (
            "おるきすたわーの\x01",
            "ちょーじょーを見ようとすると\x01",
            "クビがイタタタなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        "イタタタ、タタタ、タッタッター♪\x02",
    )

    CloseMessageWindow()

    label("loc_6B74")

    TalkEnd(0xFE)
    Return()

    # Function_35_6911 end

    def Function_36_6B78(): pass

    label("Function_36_6B78")

    TalkBegin(0xFE)

    #C0240
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "はぁ～～～～～～～～～。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        "………溜息しか出てこないよ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_6B78 end

    def Function_37_6BD8(): pass

    label("Function_37_6BD8")

    TalkBegin(0xFE)

    #C0242
    ChrTalk(
        0xFE,
        (
            "う～ん、確かに\x01",
            "表現のしようがないかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        "ただただ、茫然としちゃうわね。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_6BD8 end

    def Function_38_6C30(): pass

    label("Function_38_6C30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6CD8")

    #C0244
    ChrTalk(
        0xFE,
        (
            "なんか、マインツって所が\x01",
            "大変なことになってるんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "よく分からないけど……\x01",
            "巻き込まれない内にさっさと\x01",
            "帰った方がいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2F")

    label("loc_6CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6CE6")
    Jump("loc_6E2F")

    label("loc_6CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6D35")

    #C0246
    ChrTalk(
        0xFE,
        (
            "さてと、お昼ご飯でも食べに\x01",
            "そろそろ街の方に戻ろうかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2F")

    label("loc_6D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6DAF")

    #C0247
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの屋上は\x01",
            "まだ一般開放されてないんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "うーん、残念。\x01",
            "また改めて来なくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2F")

    label("loc_6DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6E2F")

    #C0249
    ChrTalk(
        0xFE,
        (
            "噂のオルキスタワーを\x01",
            "見に来たんだけど……\x01",
            "想像以上にすごいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "クロスベルって、\x01",
            "一体どれだけお金持ちなの？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E2F")

    TalkEnd(0xFE)
    Return()

    # Function_38_6C30 end

    def Function_39_6E33(): pass

    label("Function_39_6E33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6EB1")

    #C0251
    ChrTalk(
        0xFE,
        "あれって、クロスベル警備隊の人よね。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "ずいぶん綺麗な方だけど……\x01",
            "あの人も武器を持って戦うのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FB0")

    label("loc_6EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6EBF")
    Jump("loc_6FB0")

    label("loc_6EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6F30")

    #C0253
    ChrTalk(
        0xFE,
        "そういえば、おなか空いたなぁ。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "ふふ、何かこの場所にいると\x01",
            "ついつい時間を忘れちゃうわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FB0")

    label("loc_6F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F68")

    #C0255
    ChrTalk(
        0xFE,
        "あ～あ、屋上からの景色はお預けかぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FB0")

    label("loc_6F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6FB0")

    #C0256
    ChrTalk(
        0xFE,
        (
            "ふわ～、やっぱり遠くから\x01",
            "眺めるのとは迫力が全然違うわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FB0")

    TalkEnd(0xFE)
    Return()

    # Function_39_6E33 end

    def Function_40_6FB4(): pass

    label("Function_40_6FB4")

    TalkBegin(0xFE)

    #C0257
    ChrTalk(
        0xFE,
        (
            "うーん、この雨じゃ\x01",
            "テッペンの方がはっきり見えないなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_6FB4 end

    def Function_41_6FF8(): pass

    label("Function_41_6FF8")

    TalkBegin(0xFE)

    #C0258
    ChrTalk(
        0xFE,
        (
            "せっかく来たのにつまんなーい。\x01",
            "もう、どうして雨なんか降るのよぉ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_6FF8 end

    def Function_42_7046(): pass

    label("Function_42_7046")

    TalkBegin(0xFE)

    #C0259
    ChrTalk(
        0xFE,
        (
            "ふふ、改めて見ても\x01",
            "本当にとんでもないビルね。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "比べるものじゃないけど、\x01",
            "《四輪の塔》の比じゃないわね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_7046 end

    def Function_43_70BD(): pass

    label("Function_43_70BD")

    TalkBegin(0xFE)

    #C0261
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの存在感は\x01",
            "目で見なくとも感じられるほど\x01",
            "圧倒的ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "破壊されたⅠＢＣと、\x01",
            "守られた街の新たな象徴……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "ふむ、果たしてこの結果は\x01",
            "偶然の産物なのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_70BD end

    def Function_44_7180(): pass

    label("Function_44_7180")

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
        "#12P#00005Fこれは……\x02",
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
            "#12P#00301Fオルキスタワー前は\x01",
            "『国防軍』の奴らが\x01",
            "ガッチリ固めてやがるな……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x102,
        (
            "#6P#00108Fおじさまの独立宣言が行われた場所だし、\x01",
            "このくらいの警戒は当然でしょうね。\x02",
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
            "あれ、お前……\x01",
            "ランディじゃないか？\x02",
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
            "#00305F#12Pもしかして、カーターか？\x02\x03",

            "#00302Fはは、そんな白い軍服だから\x01",
            "気づかなかったぜ。\x02\x03",

            "お前、ベルガード門に\x01",
            "配備されてたんじゃなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x62,
        (
            "ああ、大統領の演説にあわせて\x01",
            "国境門からも何人か\x01",
            "警備に呼ばれてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x62,
        (
            "ロギンスもあっちの方で\x01",
            "巡回してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x104,
        "#00302F#12Pはは、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        "#00000F#12P（この人は……）\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        (
            "#00100F#6P（ランディの警備隊時代の\x01",
            "  同僚みたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x62,
        (
            "いや、しかし\x01",
            "大変なことになったよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x62,
        (
            "俺たちも突然\x01",
            "こんな軍服を渡されて、\x01",
            "最初は驚いたもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        (
            "#00306F#12Pああ、いきなりすぎて\x01",
            "訳がわかんねえっつうか……\x02\x03",

            "#00300F考えてみりゃ、軍服といい\x01",
            "随分用意が良すぎる気もするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x62,
        (
            "きっと大統領が、前々から\x01",
            "準備を進めてたんだろうなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x62,
        (
            "国防軍の装備も強化される\x01",
            "見込みがあるみたいだし\x01",
            "気を引き締めてかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#00305F#12Pあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x103,
        (
            "#00201F#12P（……国防軍の兵士さんたちは、\x01",
            "  今回の再編成をかなり好意的に\x01",
            "  受け取ってるみたいですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        (
            "#00106F#6P（他国の正規軍に比べて\x01",
            "  不遇なのは間違いなかったから、\x01",
            "  気持ちは分かる気がするけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x62,
        (
            "ちなみに、国防軍になるにあたって\x01",
            "俺たちにも通常の軍隊のような\x01",
            "階級名が使われることになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x62,
        (
            "一尉、二尉、三尉って呼ばれてたのが\x01",
            "大尉、中尉、少尉って具合にな。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x62,
        (
            "士官を呼ぶときに間違えたりすると、\x01",
            "相当失礼だから気をつけろよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#00300F#12Pああ、ご忠告あんがとよ。\x02\x03",

            "#00303Fつーことは、ミレイユのヤツは\x01",
            "『三尉』だったから……\x01",
            "今度からは『少尉』になるわけか。\x02\x03",

            "#00309Fはは、からかうネタが一つ増えたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        "#00006F#12Pおいおい……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x62,
        (
            "え、え～っと……\x01",
            "まあ、そうなるかな。\x02",
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
            "#00305F#12Pなんだよその、\x01",
            "煮えきらねえ返事は……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#00105F#12P呼び方としては\x01",
            "間違いじゃないはずですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x62,
        "いや、そういう話じゃないんだが……\x02",
    )

    CloseMessageWindow()
    OP_63(0x62, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x62)

    #C0291
    ChrTalk(
        0x62,
        (
            "えっとな、ランディ。\x01",
            "実は……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x6A, 0x1)
    TurnDirection(0x6A, 0x62, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("国防軍士官の声")

    #C0292
    ChrTalk(
        0x6A,
        (
            "#4S……カーター！！\x01",
            "警備中の私語は慎みたまえっ！！#3S\x02",
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
        "……は、はッ！！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x6A, 0x1)
    TurnDirection(0x62, 0x104, 300)

    #C0294
    ChrTalk(
        0x62,
        (
            "……悪い、ランディ。\x01",
            "詳しくは今度話させてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        (
            "#00300F#12Pよく分からねえが……\x01",
            "こっちこそ話し込んで悪かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x62,
        "ハハ、気にしないでくれ。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x62,
        (
            "そうそう、お前たち警察も\x01",
            "国防軍に組み込まれるんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x62,
        (
            "これからはまた同僚ってわけだ。\x01",
            "よろしく頼むぜ。\x02",
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
            "#00306F#12Pやれやれ……\x01",
            "気になることだけ言いやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        (
            "#00201F#12Pひとまずここは引き返したほうが\x01",
            "いいんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#00001F#12Pああ、行くとしよう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_68(0, 2770, -13870, 5000)
    MoveCamera(0, 7, 0, 5000)
    OP_6E(750, 5000)
    SetCameraDistance(19000, 5000)

    def lambda_80E5():

        label("loc_80E5")

        TurnDirection(0x62, 0x104, 500)
        Yield()
        Jump("loc_80E5")

    QueueWorkItem2(0x62, 2, lambda_80E5)
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_80FE():

        label("loc_80FE")

        OP_9B(0x0, 0x101, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_80FE")

    QueueWorkItem2(0x101, 1, lambda_80FE)
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_811F():

        label("loc_811F")

        OP_9B(0x0, 0x104, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_811F")

    QueueWorkItem2(0x104, 1, lambda_811F)
    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_8140():

        label("loc_8140")

        OP_9B(0x0, 0x103, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_8140")

    QueueWorkItem2(0x103, 1, lambda_8140)
    OP_93(0x102, 0xB4, 0x1F4)

    def lambda_8161():

        label("loc_8161")

        OP_9B(0x0, 0x102, 0x0, 0x2710, 0x7D0, 0x0)
        Yield()
        Jump("loc_8161")

    QueueWorkItem2(0x102, 1, lambda_8161)
    OP_0D()
    SetScenarioFlags(0x191, 4)
    EventEnd(0x6)
    NewScene("c1100", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_44_7180 end

    def Function_45_8186(): pass

    label("Function_45_8186")

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
            "#6P#00001Fミレイユ三尉……\x01",
            "街に来てたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x11,
        (
            "#07903Fええ、ついさっきね。\x02\x03",

            "#07900Fまだこちらで会議を続けている\x01",
            "司令と副司令をお待ちしているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        (
            "#6P#00103F課長も昨夜から\x01",
            "参加していた会議ね……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#6P#00201F警備隊の司令たちが残っている\x01",
            "ということは……やっぱり\x01",
            "対策も難航しているんでしょうか。\x02",
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
            "#07901F……あなたたち。\x01",
            "今朝、その課長さんから\x01",
            "問い合わせがあった件だけど……\x02\x03",

            "ランディが行方を\x01",
            "くらませたんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        (
            "#6P#00003F……はい。\x02\x03",

            "#00001Fおそらく……\x01",
            "マインツ山道に向かっている\x01",
            "状況だと思われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x11,
        "#07908F……そう……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    #C0309
    ChrTalk(
        0x105,
        "#6P#10300F……大丈夫かい？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x11,
        (
            "#07903F……ええ、私は平気よ。\x01",
            "それよりも……\x02\x03",

            "#07901Fランディが姿を消したのは、\x01",
            "あいつの過去が関係してる……\x01",
            "そうなんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        "#6P#00008Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x11,
        (
            "#07908F……くやしいけど、\x01",
            "私はランディの過去を、\x01",
            "あまり詳しくは知らないわ。\x02\x03",

            "今まで実戦訓練で\x01",
            "ライフルを使えなかった理由も、\x01",
            "私には分からない。\x02\x03",

            "#07901Fだけど……今回のこれが、\x01",
            "皆に多大な心配をかける\x01",
            "本当に馬鹿な行為なのは分かる。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x109,
        "#6P#10108Fミレイユ三尉……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#6P#00203F……確かに、馬鹿を超えた大馬鹿です。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x11,
        (
            "#07903F……警備隊も甚大な被害を受けたわ。\x01",
            "これから司令たちによって、もう一度\x01",
            "救援部隊を編成することになると思う。\x02\x03",

            "私たちはそれまで動く事はできないし……\x01",
            "ランディ１人のために出動を\x01",
            "早めるわけにもいかない。\x02\x03",

            "#07900Fだから皆さん……\x01",
            "あの馬鹿のこと、どうかお願いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#6P#00000F……任せてください。\x01",
            "ランディは俺たちが、必ず……！\x02",
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

    # Function_45_8186 end

    def Function_46_87F9(): pass

    label("Function_46_87F9")

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
            "『西ゼムリア通商会議』──\x02\x03",

            "各国首脳を招いた国際会議が\x01",
            "ディーター・クロイス新市長の提唱で\x01",
            "開催されようとしていた。\x07\x00\x02",
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
            "同時にそれは、完成したばかりの\x01",
            "新市庁ビルのお披露目を兼ねていた。\x02\x03",

            "──通称『オルキスタワー』。\x02\x03",

            "地上４０階、高さ２５０アージュとなる、\x01",
            "大陸史上初の超高層ビルディングは\x01",
            "今や大陸中の人々の関心を呼んでいた。\x07\x00\x02",
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

    # Function_46_87F9 end

    def Function_47_8D68(): pass

    label("Function_47_8D68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DB4")
    OP_95(0xFE, 21700, 300, -6000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 21700, 300, 19000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Jump("Function_47_8D68")

    label("loc_8DB4")

    Return()

    # Function_47_8D68 end

    def Function_48_8DB5(): pass

    label("Function_48_8DB5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E01")
    OP_95(0xFE, -21700, 300, 19000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, -21700, 300, -6000, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x0, 0x1F4)
    Jump("Function_48_8DB5")

    label("loc_8E01")

    Return()

    # Function_48_8DB5 end

    def Function_49_8E02(): pass

    label("Function_49_8E02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E4E")
    OP_95(0xFE, -7000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -19000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Jump("Function_49_8E02")

    label("loc_8E4E")

    Return()

    # Function_49_8E02 end

    def Function_50_8E4F(): pass

    label("Function_50_8E4F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E9B")
    OP_95(0xFE, 7000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19000, 0, 5500, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Jump("Function_50_8E4F")

    label("loc_8E9B")

    Return()

    # Function_50_8E4F end

    def Function_51_8E9C(): pass

    label("Function_51_8E9C")

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

    def lambda_9585():
        OP_98(0xFE, 0x0, 0x0, 0xEA60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x71, 1, lambda_9585)
    BeginChrThread(0x79, 1, 0, 55)
    FadeToBright(2000, 0)
    Sleep(3000)
    ClearMapObjFlags(0xB, 0x4)

    def lambda_95B7():
        OP_98(0xFE, 0x0, 0x0, 0xD6D8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x72, 1, lambda_95B7)
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

    def lambda_96E0():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_96E0)
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

    def lambda_9792():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_9792)
    OP_68(-1000, 1000, 6200, 2500)
    MoveCamera(9, 27, 0, 2500)
    SetCameraDistance(13500, 2500)
    OP_6F(0x79)
    Sleep(500)

    def lambda_97C9():
        TurnDirection(0xFE, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_97C9)
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

    def lambda_987A():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_987A)
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
        "#11P#00011F（……す、凄いな………）\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x102,
        (
            "#00104F#5P（ええ……さすが一国を\x01",
            "  まとめ上げる人たちばかりね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#00301F#5P（しかし《鉄血宰相》か……\x01",
            "  かなりガタイがいいじゃねぇか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x105,
        (
            "#11P#10302F（フフ、共和国の大統領の方は\x01",
            "  飄々#4Rひょうひょう#としたタヌキって感じだね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x109,
        (
            "#11P#10102F（リベールのクローディア王太女も\x01",
            "  素敵ですね……）\x02\x03",

            "#10109F（……それにあのユリア准佐を\x01",
            "  こんな所で見られるなんて……！）\x02",
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

    def lambda_9AF5():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_9AF5)

    def lambda_9B02():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_9B02)

    def lambda_9B0F():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_9B0F)

    def lambda_9B1C():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_9B1C)

    def lambda_9B29():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_9B29)

    def lambda_9B36():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_9B36)

    def lambda_9B43():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_9B43)

    def lambda_9B50():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_9B50)
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
            "#02804F#5P──各国首脳の皆様。\x02\x03",

            "#02800Fようこそ、遠路はるばる\x01",
            "クロスベルへいらっしゃいました。\x02\x03",

            "クロスベル市の市長、\x01",
            "ディーター・クロイスであります。\x02",
        )
    )

    CloseMessageWindow()
    Sound(968, 0, 70, 0)
    Sleep(2500)

    #C0325
    ChrTalk(
        0x30,
        (
            "#02804F#5Pこの度は『西ゼムリア通商会議』に\x01",
            "参加して頂き、誠に有難うございます。\x02\x03",

            "通例ならば、この場で歓迎の意と共に\x01",
            "開会宣言をさせて頂くところですが……\x02\x03",

            "#02800Fその前に、この記念すべき日にことよせて\x01",
            "皆様のお時間を頂きたいと思います。\x02",
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

    def lambda_9D6E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_9D6E)

    def lambda_9D7B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_9D7B)
    Sleep(50)

    def lambda_9D8B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_9D8B)

    def lambda_9D98():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_9D98)
    Sleep(50)

    def lambda_9DA8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_9DA8)

    def lambda_9DB5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_9DB5)
    Sleep(50)

    def lambda_9DC5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_9DC5)

    def lambda_9DD2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_9DD2)
    Sleep(50)

    def lambda_9DE2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_9DE2)

    def lambda_9DEF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5A, 2, lambda_9DEF)
    Sleep(50)

    def lambda_9DFF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_9DFF)

    def lambda_9E0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_9E0C)

    def lambda_9E19():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5B, 2, lambda_9E19)
    WaitChrThread(0x31, 2)
    OP_6F(0x79)
    Sleep(500)

    #C0326
    ChrTalk(
        0x30,
        (
            "#02803F#N#11P──ご紹介申し上げます。\x02\x03",

            "クロスベル市の新市庁舎として。\x02\x03",

            "貿易・金融都市クロスベルを象徴する\x01",
            "新たなるランドマークとして。\x02\x03",

            "#02800F何よりも、大陸全土の平和と発展に\x01",
            "貢献する国際交流センターとして。\x02\x03",

            "皆様にお披露目させていただだく、\x01",
            "大陸史上初の超高層ビルディング──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0327
    ChrTalk(
        0x30,
        "#02809F#N#4S#11P《オルキスタワー》であります！\x02",
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
            "#00011F#Nこ、これが……\x01",
            "《オルキスタワー》……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0329
    ChrTalk(
        0x102,
        (
            "#00102F#N概要は知っていたけど\x01",
            "ここまで壮麗だったなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0330
    ChrTalk(
        0x109,
        (
            "#6P#10111F#Nな、なんだか見てるだけで\x01",
            "圧倒されそうですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0331
    ChrTalk(
        0x104,
        (
            "#00306F#Nあり得ねぇだろ……\x01",
            "どんだけミラがかかってんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0332
    ChrTalk(
        0x105,
        (
            "#12P#10302F#Nフフ、気の遠くなるような\x01",
            "ミラが投入されたんだろうねぇ。\x02",
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
            "#07205F#11P（いやはや……\x01",
            "  さすがに度肝を抜かれたねぇ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x2A,
        (
            "#07303F#5P（……技術の進歩というのは\x01",
            "  凄まじいものだな……）\x02",
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
            "#07000F#5P（……まるでリベル＝アークを\x01",
            "  思い出してしまいますね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x2C,
        (
            "#07104F#5P（ええ……さすがに中枢塔#6Rアクシスピラー#ほどの\x01",
            "  高さではありませんが……）\x02",
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
            "#07511F#5P（はっはっはっ、\x01",
            "  何とも豪気じゃないか！）\x02\x03",

            "#07510F（キミの報告は受けていたが\x01",
            "  まさかここまでとはなぁ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x2F,
        (
            "#12004F#11P（ええ、私も実物が\x01",
            "  ここまでとは思いませんでした。）\x02\x03",

            "#12000F（さすがはＩＢＣの資本力と\x01",
            "  言ったところでしょうか。）\x02",
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
            "#07404F#11P（フフ、実際大したものだ。）\x02\x03",

            "#07400F（この因縁の地に\x01",
            "  これほどの大伽藍#6Rだい が らん#を築くとはな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x28,
        (
            "#11509F#11P（んー、とりあえず一度、\x01",
            "  屋上に登ってみたいねぇ。）\x02\x03",

            "#11502F（市長さんに頼んでみたら\x01",
            "  登らせてくれっかなァ？）\x02",
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

    def lambda_A878():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_A878)

    def lambda_A885():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_A885)

    def lambda_A892():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5B, 2, lambda_A892)
    Sleep(50)

    def lambda_A8A2():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_A8A2)

    def lambda_A8AF():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_A8AF)
    Sleep(50)

    def lambda_A8BF():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_A8BF)

    def lambda_A8CC():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A8CC)
    Sleep(50)

    def lambda_A8DC():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A8DC)

    def lambda_A8E9():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_A8E9)
    Sleep(50)

    def lambda_A8F9():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_A8F9)

    def lambda_A906():
        TurnDirection(0xFE, 0x30, 500)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_A906)
    Sleep(50)

    def lambda_A916():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_A916)

    def lambda_A923():
        TurnDirection(0xFE, 0x30, 0)
        ExitThread()

    QueueWorkItem(0x5A, 2, lambda_A923)
    OP_6F(0x79)
    Sleep(500)

    #C0341
    ChrTalk(
        0x30,
        (
            "#02804F──それでは改めまして。\x02\x03",

            "首脳の方々、およびこの場にいる\x01",
            "全ての関係者の立会いの下──\x02\x03",

            "#02800F『西ゼムリア通商会議』の\x01",
            "開催を宣言させていただきます！\x02",
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

    # Function_51_8E9C end

    def Function_52_AA19(): pass

    label("Function_52_AA19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAD1")
    Sound(810, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA84")
    Sleep(500)
    Jump("loc_AACC")

    label("loc_AA84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA9B")
    Sleep(1000)
    Jump("loc_AACC")

    label("loc_AA9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AAB2")
    Sleep(150)
    Jump("loc_AACC")

    label("loc_AAB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AAC9")
    Sleep(2000)
    Jump("loc_AACC")

    label("loc_AAC9")

    Sleep(2500)

    label("loc_AACC")

    Jump("Function_52_AA19")

    label("loc_AAD1")

    Return()

    # Function_52_AA19 end

    def Function_53_AAD2(): pass

    label("Function_53_AAD2")

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

    # Function_53_AAD2 end

    def Function_54_AC50(): pass

    label("Function_54_AC50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC75")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(4000)
    Jump("Function_54_AC50")

    label("loc_AC75")

    Return()

    # Function_54_AC50 end

    def Function_55_AC76(): pass

    label("Function_55_AC76")

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

    # Function_55_AC76 end

    def Function_56_ACD1(): pass

    label("Function_56_ACD1")

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
            "#00000Fはは、賑わってるな。\x02\x03",

            "リュウやアンリたちも\x01",
            "遊びに来ているみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        (
            "#00100Fこの広場は除幕式の後、\x01",
            "首脳たちが去って間もなくして\x01",
            "市民に開放されたのよね。\x02\x03",

            "#00104Fふふ、おじさまの\x01",
            "粋なはからいと言った所かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x109,
        (
            "#10109Fあはは、ディーター市長らしいです。\x02\x03",

            "#10100Fでも、さすがに警官の方も多いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x105,
        (
            "#10304F#4Pまあ、今は街全体が\x01",
            "浮き立っている状態だしね。\x02\x03",

            "#10300Fトラブルも起きやすいだろうし\x01",
            "警戒は厳にしてるんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#00003Fああ、流石にタワー内部までは\x01",
            "立ち入れないようにしてるみたいだ。\x02\x03",

            "#00000F俺たちも今の時点では、\x01",
            "中に入るのは止めておこう。\x02",
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

    # Function_56_ACD1 end

    def Function_57_B12A(): pass

    label("Function_57_B12A")

    EventBegin(0x1)

    #C0347
    ChrTalk(
        0x101,
        (
            "#00000F今日は、市民たちもタワー内部までは\x01",
            "立ち入れないようにしてるみたいだ。\x02\x03",

            "俺たちも今の時点では、\x01",
            "中に入るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 0, 25470, 180)
    EventEnd(0x4)
    Return()

    # Function_57_B12A end

    def Function_58_B1C8(): pass

    label("Function_58_B1C8")

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

    def lambda_B290():
        OP_97(0x105, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B290)
    Sleep(100)

    def lambda_B2AD():
        OP_97(0x109, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B2AD)
    Sleep(100)

    def lambda_B2CA():
        OP_97(0x103, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B2CA)
    Sleep(100)

    def lambda_B2E7():
        OP_97(0x104, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B2E7)
    Sleep(100)

    def lambda_B304():
        OP_97(0x101, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B304)
    Sleep(100)

    def lambda_B321():
        OP_97(0x102, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B321)
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
            "#00206F#11P昨夜、空港に到着する前に\x01",
            "ライティングされたこのビルを\x01",
            "見かけましたが……\x02\x03",

            "#00202Fこうして実際に見上げると\x01",
            "とんでもない大きさですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#00004F#11Pはは……気持ちは分かるよ。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x109,
        (
            "#10102F#5Pまさにクロスベルの新しい\x01",
            "ランドマークって感じですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x104,
        (
            "#00306F#5Pしかしこんなでかいビル、\x01",
            "いったい何に使うってんだ？\x02\x03",

            "#00301F前の市庁舎に比べて\x01",
            "デカすぎるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x102,
        (
            "#00104F#5Pまあ、色々な機能が\x01",
            "盛り込まれているビルだから。\x02\x03",

            "#00100F市や自治州の行政区画以外にも\x01",
            "国際貿易センターや\x01",
            "文化交流に関するフロアもあるの。\x02\x03",

            "まさに大陸西部の中心となるべく、\x01",
            "建造されたと言えるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x104,
        (
            "#00305F#5Pは～……\x01",
            "スケールのデカイ話だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x109,
        (
            "#10100F#5Pでも、そんな風に言われると\x01",
            "今回の通商会議も納得ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x105,
        (
            "#10304F#11P実際、このビルの完成で\x01",
            "クロスベルへの資本・情報集中は\x01",
            "今まで以上に加速するだろうね。\x02\x03",

            "#10300Fそうした展望を踏まえての\x01",
            "今後の取り決めなんかが\x01",
            "話し合われるってところかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x102,
        (
            "#00104F#5Pええ、そう聞いているわ。\x02\x03",

            "#00108Fもっとも経済的な話だけには\x01",
            "留まらないでしょうけど……\x02",
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
            "#00003F#11P──さてと、どうする？\x02\x03",

            "#00001Fダドリーさんとは\x01",
            "正午に１Ｆの玄関フロアで\x01",
            "待ち合わせているけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B85B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B85B)
    Sleep(50)

    def lambda_B86B():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B86B)
    Sleep(50)

    def lambda_B87B():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B87B)
    Sleep(50)

    def lambda_B88B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B88B)
    Sleep(50)

    def lambda_B89B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B89B)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B90F")

    #C0358
    ChrTalk(
        0x102,
        (
            "#00108F#5Pそうね……\x01",
            "まだ時間はあるけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B942")

    label("loc_B90F")


    #C0359
    ChrTalk(
        0x102,
        (
            "#00105F#5Pそうね……\x01",
            "まだ大分時間はあるけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B942")


    #C0360
    ChrTalk(
        0x104,
        (
            "#6P#00304Fまあ、とにかく用事やら\x01",
            "準備なんかは済ませとこうぜ。\x02\x03",

            "#00300F何が起きても問題ねぇようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x109,
        (
            "#6P#10106Fそうですね……\x01",
            "さすがに会議が始まったら\x01",
            "外に出るわけにもいきませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x103,
        (
            "#12P#00202Fでは、用事と準備を済ませたら\x01",
            "ビルに入るとしましょう。\x02",
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

    # Function_58_B1C8 end

    def Function_59_BA8D(): pass

    label("Function_59_BA8D")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBF3")

    #C0363
    ChrTalk(
        0x101,
        (
            "#00003F#5P（ダドリーさんとは\x01",
            "  正午に１Ｆの玄関フロアで\x01",
            "  待ち合わせしている……）\x02\x03",

            "#00001F（まだ時間はあるけど\x01",
            "  そろそろ中に入ろうか？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC8D")

    label("loc_BBF3")


    #C0364
    ChrTalk(
        0x101,
        (
            "#00003F#5P（ダドリーさんとは\x01",
            "  正午に１Ｆの玄関フロアで\x01",
            "  待ち合わせしている……）\x02\x03",

            "#00001F（まだ大分時間はあるけど\x01",
            "  早めに入って待っておこうか？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC8D")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一度、タワーに入ったら\x01",
            "装備やアイテム、オーブメントを\x01",
            "整えることができなくなります。\x02\x03",

            "また、残ったクエストなども\x01",
            "全て終了するので注意してください。\x07\x00\x02",
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
            "【まだ他に用事がある】\x01",            # 0
            "【オルキスタワーの中に入る】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BDB7"),
        (0, "loc_BED9"),
        (SWITCH_DEFAULT, "loc_BF03"),
    )


    label("loc_BDB7")

    OP_68(0, 1500, 30500, 4000)
    MoveCamera(0, 7, 0, 4000)

    def lambda_BDD8():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BDD8)
    Sleep(50)

    def lambda_BDF5():
        OP_97(0x103, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BDF5)
    Sleep(50)

    def lambda_BE12():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BE12)
    Sleep(50)

    def lambda_BE2F():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BE2F)
    Sleep(50)

    def lambda_BE4C():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BE4C)
    Sleep(50)

    def lambda_BE69():
        OP_97(0x105, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BE69)
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
    Jump("loc_BF03")

    label("loc_BED9")

    SetChrPos(0x0, 0, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_BF03")

    label("loc_BF03")

    EventEnd(0x5)
    Return()

    # Function_59_BA8D end

    def Function_60_BF06(): pass

    label("Function_60_BF06")

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
            "ディーター市長の提唱した\x01",
            "『クロスベルの国家独立』の是非を問う\x01",
            "住民投票の日が迫りつつあった。\x02\x03",

            "帝国、共和国政府による圧力も\x01",
            "日増しに露骨になり始めていたが\x01",
            "市民たちの関心は非常に高く……\x02\x03",

            "アルカンシェルによる\x01",
            "リニューアル舞台の公開と相まって\x01",
            "市内の熱気は更に高まっていた。\x02\x03",

            "──そんな中、新たな問題が\x01",
            "人知れず郊外で起きつつあった。\x07\x00\x02",
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

    # Function_60_BF06 end

    def Function_61_C1A8(): pass

    label("Function_61_C1A8")

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
            "#11Pしっかし、アンタたちと\x01",
            "こんな形で共闘するとはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x33,
        (
            "#11Pフ……最初の頃からすると\x01",
            "想像も付かんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#6P#00012Fはは……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#00304Fま、こっちもそれなりに\x01",
            "成長してるってことだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x32,
        "#11Pいや、実際大したもんだよ。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x32,
        (
            "#11Pもし警察をクビになったら\x01",
            "いつでも歓迎させてもらうぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x35,
        "#11Pそうそう！\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x35,
        (
            "#11P特にティオちゃんなんか\x01",
            "ギルド向きだと思うのよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x35, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0375
    ChrTalk(
        0x103,
        "#6P#00211Fそう言われましても。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        (
            "#00109Fふふっ……\x01",
            "お言葉だけ頂いておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x109,
        (
            "#6P#10101Fでも《幻獣》ですか……\x01",
            "確かに気になりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x32,
        (
            "#11Pああ、とりあえず\x01",
            "手分けすることにしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x32,
        (
            "#11P警備隊から回ってきたのは\x01",
            "全部で５件……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x32,
        (
            "#11P君たちにはそのうち、\x01",
            "２件を受け持ってもらいたい。\x02",
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
            "#10302Fへえ、ずいぶんと\x01",
            "気前がいいじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        (
            "#6P#00005Fいいんですか？\x01",
            "そちらの分担が多くても……\x02\x03",

            "#00001Fただでさえ、アリオスさんが\x01",
            "今は動けない状況なのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x34,
        "#11P──だからこそ、さ。\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x34,
        (
            "#11P彼が動けない分、あんた達にも\x01",
            "必ずシワ寄せが来るはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x35,
        (
            "#11P元より、魔獣退治は\x01",
            "遊撃士#6Rわたしたち#の十八番……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x35,
        (
            "#11Pお互い、他の仕事もあるし\x01",
            "効率的に分担すべきでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#00104F……助かります。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x109,
        (
            "#6P#10108Fな、何だか\x01",
            "申しわけないですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x32,
        "#11Pなに、お互い様さ。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x32,
        (
            "#11Pそれに君たちの方には\x01",
            "《結社》の問題もあるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        "#6P#00006F……はい。\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#00306Fったく……\x01",
            "その問題もあるんだよな。\x02",
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
            "#00203F結社《身喰らう蛇#10Rウ ロ ボ ロ ス#》……\x02\x03",

            "#00201F何でも、遊撃士協会とは\x01",
            "色々と因縁があるとか……？\x02",
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
            "ええ、リベールの異変でも\x01",
            "エステルちゃんたちを始めとする\x01",
            "遊撃士がやり合ったし……\x02\x03",

            "それ以外にも各地の事件で\x01",
            "幾度となくぶつかっているわね。\x02",
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
            "……帝国のギルドが\x01",
            "一時壊滅状態に陥ったのも\x01",
            "奴らの仕業だと言われている。\x02\x03",

            "もっとも、その後の衰退の原因は\x01",
            "帝国軍の圧力によるものだがな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 190, -1, -1)

    #A0396
    AnonymousTalk(
        0x101,
        "#00001Fそうなんですか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(100, 210, -1, -1)

    #A0397
    AnonymousTalk(
        0x104,
        (
            "#00301Fしかし、聞けば聞くほど\x01",
            "捉えどころのねぇ連中だぜ。\x02",
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
            "#11Pいずれにせよ、ギルドの方でも\x01",
            "未だ実態が掴めていない連中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x32,
        (
            "#11P何が目的か分からないが\x01",
            "くれぐれも気を付けるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x34,
        (
            "#11P困ったことがあったら\x01",
            "遠慮なく連絡してきなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x34,
        (
            "#11P正直、連中に関しては\x01",
            "こっちも他人事じゃないんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        "#6P#00002F……分かりました。\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x102,
        (
            "#00104F何かあれば遠慮なく\x01",
            "頼らせていただきます。\x02",
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

    # Function_61_C1A8 end

    def Function_62_CF44(): pass

    label("Function_62_CF44")


    def lambda_CF49():
        OP_97(0x32, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 0, lambda_CF49)
    Sleep(50)

    def lambda_CF66():
        OP_97(0x34, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 0, lambda_CF66)
    Sleep(50)

    def lambda_CF83():
        OP_97(0x33, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 0, lambda_CF83)
    Sleep(50)

    def lambda_CFA0():
        OP_97(0x35, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 0, lambda_CFA0)

    def lambda_CFBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_CFBA)
    Sleep(100)

    def lambda_CFCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 2, lambda_CFCE)
    Sleep(400)

    def lambda_CFE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_CFE2)
    Sleep(100)

    def lambda_CFF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_CFF6)
    Return()

    # Function_62_CF44 end

    def Function_63_D003(): pass

    label("Function_63_D003")


    def lambda_D008():
        OP_97(0x101, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D008)
    Sleep(50)

    def lambda_D025():
        OP_97(0x102, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D025)
    Sleep(50)

    def lambda_D042():
        OP_97(0x103, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D042)
    Sleep(50)

    def lambda_D05F():
        OP_97(0x104, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D05F)
    Sleep(50)

    def lambda_D07C():
        OP_97(0x109, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D07C)
    Sleep(50)

    def lambda_D099():
        OP_97(0x105, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D099)

    def lambda_D0B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D0B3)
    Sleep(100)

    def lambda_D0C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D0C7)
    Sleep(400)

    def lambda_D0DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D0DB)
    Sleep(100)

    def lambda_D0EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D0EF)
    Sleep(400)

    def lambda_D103():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D103)
    Sleep(100)

    def lambda_D117():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D117)
    Return()

    # Function_63_D003 end

    def Function_64_D124(): pass

    label("Function_64_D124")

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
    OP_8E(0x30, "ディーター大統領")
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
            "──皆さん、ごきげんよう。\x02\x03",

            "この度、『クロスベル独立国』の\x01",
            "初代大統領に就任した\x01",
            "ディーター・クロイスであります。\x02",
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

    # Function_64_D124 end

    def Function_65_D865(): pass

    label("Function_65_D865")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D91D")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D893")
    Sleep(500)
    Jump("loc_D8DB")

    label("loc_D893")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8AA")
    Sleep(1000)
    Jump("loc_D8DB")

    label("loc_D8AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8C1")
    Sleep(1500)
    Jump("loc_D8DB")

    label("loc_D8C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8D8")
    Sleep(2000)
    Jump("loc_D8DB")

    label("loc_D8D8")

    Sleep(2500)

    label("loc_D8DB")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 70, 0)
    Jump("Function_65_D865")

    label("loc_D91D")

    Return()

    # Function_65_D865 end

    def Function_66_D91E(): pass

    label("Function_66_D91E")

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
    OP_8E(0x30, "ディーター大統領")
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
            "#11303F#6P──そのために私は今日、\x01",
            "大統領という立場に\x01",
            "就かせていただく事となった。\x02\x03",

            "#11300F無論、これはあくまで\x01",
            "迫り来る危機に対処するための\x01",
            "暫定的な処置にすぎない。\x02\x03",

            "#11304Fいずれ平和を取り戻した暁には\x01",
            "選挙という形で民意に問うことを\x01",
            "この場でお約束させていただく。\x02",
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
            "#11303F#11Pそしてもう一人……\x02\x03",

            "#11300F諸君も良く知るこの人物が、\x01",
            "新生『クロスベル独立国』に\x01",
            "協力してくれることとなった。\x02",
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
            "#11304F#5Pご紹介しよう──\x02\x03",

            "先のクロスベル市襲撃において\x01",
            "獅子奮迅の働きでオルキスタワーを\x01",
            "死守してくれた人物……\x02\x03",

            "#11300F《風の剣聖》の名で知られる、\x01",
            "遊撃士協会・クロスベル支部に\x01",
            "所属していた元Ａ級遊撃士……\x02\x03",

            "#11309F『クロスベル国防軍』司令長官、\x01",
            "アリオス・マクレイン君だ！\x02",
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
            "#4084V──ご紹介にあずかった、\x01",
            "アリオス・マクレインです。\x02\x03",

            "#4085Vいまだ若輩者ゆえ、\x01",
            "不安に感じられる方々も\x01",
            "いらっしゃるかもしれません。\x02\x03",

            "#4086Vですが、遊撃士の時以上の働きで\x01",
            "いかなる脅威も退けることを\x01",
            "お約束しましょう。\x02\x03",

            "#4087Vクロスベルを守りぬく盾として……\x02\x03",

            "#4088Vそして、正義と平和を脅かす\x01",
            "全ての敵を撃ち破る剣として……！\x02",
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

    # Function_66_D91E end

    def Function_67_E4A6(): pass

    label("Function_67_E4A6")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_96(0xFE, 0x3E8, 0x2904, 0x88B8, 0x3E8, 0x0)
    Return()

    # Function_67_E4A6 end

    def Function_68_E4C2(): pass

    label("Function_68_E4C2")

    OP_95(0xFE, 0, 10380, 35600, 1500, 0x0)
    OP_95(0xFE, 0, 10500, 35000, 1500, 0x0)
    Return()

    # Function_68_E4C2 end

    def Function_69_E4EB(): pass

    label("Function_69_E4EB")

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

    # Function_69_E4EB end

    def Function_70_E5F9(): pass

    label("Function_70_E5F9")

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
    OP_8E(0x2F, "キリカ")
    OP_8E(0x28, "レクター")
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

    def lambda_EFD7():
        OP_93(0xFE, 0xC8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x40, 2, lambda_EFD7)
    Sleep(500)

    def lambda_EFE7():
        OP_93(0xFE, 0xC8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_EFE7)
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

    def lambda_F21D():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x3C, 2, lambda_F21D)

    def lambda_F22A():
        OP_96(0xFE, 0x1CE8, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_F22A)
    Sleep(50)
    EndChrThread(0x48, 0x1)
    SetChrChipByIndex(0x48, 0x13)
    SetChrSubChip(0x48, 0x0)
    OP_63(0x48, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_F265():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x48, 2, lambda_F265)

    def lambda_F272():
        OP_96(0xFE, 0x17D4, 0x32, 0xFFFFF95C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_F272)
    Sleep(50)
    EndChrThread(0x38, 0x1)
    EndChrThread(0x79, 0x0)
    SetChrChipByIndex(0x38, 0xF)
    SetChrSubChip(0x38, 0x0)
    OP_63(0x38, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_F2B1():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_F2B1)
    Sleep(50)
    OP_63(0x3A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_F2D3():
        TurnDirection(0xFE, 0x3E, 500)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_F2D3)
    Sleep(50)

    #C0409
    ChrTalk(
        0x3C,
        "うおおおっ！？\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x38,
        "ひえええっ！？\x02",
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

    def lambda_F41A():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_F41A)

    def lambda_F433():
        OP_9B(0x1, 0xFE, 0xB4, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_F433)
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
        "#11507F#5Pお次は任せたぜ～。\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x2F,
        "#03404F──ええ。\x02",
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

    def lambda_F6BF():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_F6BF)

    def lambda_F6D8():
        OP_9B(0x1, 0xFE, 0xB4, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_F6D8)
    BeginChrThread(0x2F, 3, 0, 104)
    WaitChrThread(0x2F, 3)
    EndChrThread(0x4A, 0x1)
    SetChrChipByIndex(0x4A, 0x13)
    SetChrSubChip(0x4A, 0x0)
    OP_93(0x4A, 0x0, 0x1F4)

    #C0413
    ChrTalk(
        0x3B,
        "す、凄い……！\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x23,
        "#5P#N#01005Fさすが泰斗流だな……\x02",
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
            "#11Pキリカさん！\x01",
            "お手伝いします！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2F, 0x34, 500)
    BeginChrThread(0x3E, 3, 0, 92)

    #C0416
    ChrTalk(
        0x2F,
        (
            "#6P#03402Fええ、泰斗の真髄、\x01",
            "見せてあげましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x34,
        "#11Pはいっ！\x02",
    )

    CloseMessageWindow()

    def lambda_F8CF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_F8CF)
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
            "#11P#11509Fやれやれ。\x01",
            "目立ちまくってんなァ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)
    Sleep(300)

    #C0419
    ChrTalk(
        0x28,
        (
            "#11P#11502Fま、こっちは少し、\x01",
            "ラクをさせてもらうかね。\x02",
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
        "#01003F#11P頃合いか……\x02",
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
            "#01007F#4S#11P──特務支援課、突入！\x02\x03",

            "“道”は拓いた！\x01",
            "後はお前たちに任せる！\x02",
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
            "#4S了解！\x07\x00\x02",
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

    # Function_70_E5F9 end

    def Function_71_FF58(): pass

    label("Function_71_FF58")


    def lambda_FF5D():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF5D)

    def lambda_FF77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FF77)
    WaitChrThread(0xFE, 1)

    def lambda_FF8C():
        OP_95(0xFE, 3100, 250, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF8C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x38, 1, 0, 123)
    BeginChrThread(0x79, 0, 0, 127)
    Return()

    # Function_71_FF58 end

    def Function_72_FFC1(): pass

    label("Function_72_FFC1")


    def lambda_FFC6():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFC6)

    def lambda_FFE0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FFE0)
    WaitChrThread(0xFE, 1)

    def lambda_FFF5():
        OP_95(0xFE, 6100, 50, -700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FFF5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x48, 1, 0, 123)
    Return()

    # Function_72_FFC1 end

    def Function_73_10024(): pass

    label("Function_73_10024")


    def lambda_10029():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10029)

    def lambda_10043():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10043)
    WaitChrThread(0xFE, 1)

    def lambda_10058():
        OP_95(0xFE, 7400, 0, -500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10058)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x3C, 1, 0, 123)
    Return()

    # Function_73_10024 end

    def Function_74_10087(): pass

    label("Function_74_10087")


    def lambda_1008C():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1008C)

    def lambda_100A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_100A6)
    WaitChrThread(0xFE, 1)

    def lambda_100BB():
        OP_95(0xFE, -3100, 250, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_100BB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x49, 1, 0, 123)
    Return()

    # Function_74_10087 end

    def Function_75_100EA(): pass

    label("Function_75_100EA")


    def lambda_100EF():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_100EF)

    def lambda_10109():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10109)
    WaitChrThread(0xFE, 1)

    def lambda_1011E():
        OP_95(0xFE, -6100, 50, -700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1011E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)

    #C0423
    ChrTalk(
        0x39,
        "#5P迎撃を開始します！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_75_100EA end

    def Function_76_1015D(): pass

    label("Function_76_1015D")


    def lambda_10162():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10162)

    def lambda_1017C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1017C)
    WaitChrThread(0xFE, 1)

    def lambda_10191():
        OP_95(0xFE, -7400, 0, -500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10191)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x4A, 1, 0, 123)
    BeginChrThread(0x79, 1, 0, 128)
    Return()

    # Function_76_1015D end

    def Function_77_101C6(): pass

    label("Function_77_101C6")


    def lambda_101CB():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101CB)

    def lambda_101E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_101E5)
    WaitChrThread(0xFE, 1)

    def lambda_101FA():
        OP_95(0xFE, -6400, 0, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101FA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_77_101C6 end

    def Function_78_1021B(): pass

    label("Function_78_1021B")


    def lambda_10220():
        OP_95(0xFE, 5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10220)

    def lambda_1023A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1023A)
    WaitChrThread(0xFE, 1)

    def lambda_1024F():
        OP_95(0xFE, 4400, 0, -2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1024F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x9)

    #C0424
    ChrTalk(
        0x3A,
        "車輌を盾にしろー！\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_78_1021B end

    def Function_79_1028B(): pass

    label("Function_79_1028B")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_10298():
        OP_95(0xFE, -5400, 100, -1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10298)

    def lambda_102B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_102B2)
    WaitChrThread(0xFE, 1)

    def lambda_102C7():
        OP_95(0xFE, -2000, 250, -1600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_102C7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0x23, 1, 0, 124)
    BeginChrThread(0x79, 2, 0, 130)
    Return()

    # Function_79_1028B end

    def Function_80_102FC(): pass

    label("Function_80_102FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_104A2")
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
    Jump("Function_80_102FC")

    label("loc_104A2")

    Return()

    # Function_80_102FC end

    def Function_81_104A3(): pass

    label("Function_81_104A3")

    Sleep(300)

    label("loc_104A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1064C")
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
    Jump("loc_104A6")

    label("loc_1064C")

    Return()

    # Function_81_104A3 end

    def Function_82_1064D(): pass

    label("Function_82_1064D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_107F3")
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
    Jump("Function_82_1064D")

    label("loc_107F3")

    Return()

    # Function_82_1064D end

    def Function_83_107F4(): pass

    label("Function_83_107F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1083E")
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 1600, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("Function_83_107F4")

    label("loc_1083E")

    Return()

    # Function_83_107F4 end

    def Function_84_1083F(): pass

    label("Function_84_1083F")

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

    # Function_84_1083F end

    def Function_85_1088E(): pass

    label("Function_85_1088E")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_108B5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_108B5)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_85_1088E end

    def Function_86_108F1(): pass

    label("Function_86_108F1")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_10918():
        OP_95(0xFE, -2200, 100, 5300, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10918)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_86_108F1 end

    def Function_87_10954(): pass

    label("Function_87_10954")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 9)

    def lambda_1097B():
        OP_95(0xFE, 2000, 100, 5800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1097B)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_87_10954 end

    def Function_88_109B7(): pass

    label("Function_88_109B7")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(630)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)

    def lambda_109DD():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_109DD)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_88_109B7 end

    def Function_89_10A15(): pass

    label("Function_89_10A15")

    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10A35():
        OP_A6(0xFE, 0x0, 0x64, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_10A35)
    Sleep(1000)
    Sound(985, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10A91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10A91)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_89_10A15 end

    def Function_90_10AA2(): pass

    label("Function_90_10AA2")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xFE, 7300, 250, 4300, 225)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10B0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10B0B)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Sleep(130)
    SetChrSubChip(0x3E, 0x1)
    Sleep(130)

    def lambda_10B2D():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_10B2D)
    Sleep(1000)
    Sound(951, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)

    def lambda_10B58():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B58)
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

    # Function_90_10AA2 end

    def Function_91_10C78(): pass

    label("Function_91_10C78")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, -7300, 250, 4300, 135)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10CE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10CE7)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_91_10C78 end

    def Function_92_10CFB(): pass

    label("Function_92_10CFB")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, -12800, 0, 8300, 135)
    Sound(985, 0, 100, 0)
    PlayEffect(0x0, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_10D6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10D6A)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_92_10CFB end

    def Function_93_10D7E(): pass

    label("Function_93_10D7E")

    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    SetChrPos(0xFE, 8300, 0, 15000, 180)
    Sound(985, 0, 70, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10DED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10DED)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_93_10D7E end

    def Function_94_10E01(): pass

    label("Function_94_10E01")


    def lambda_10E06():
        OP_95(0xFE, 800, 100, 600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E06)
    WaitChrThread(0xFE, 1)

    def lambda_10E24():
        OP_96(0xFE, 0x44C, 0x64, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E24)
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

    def lambda_10EAF():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_10EAF)
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

    def lambda_10FAD():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_10FAD)
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

    def lambda_110AB():
        OP_98(0xFE, 0x0, 0x0, 0xC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_110AB)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3F, 0x0, -300, 2350, 200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x3F, 0x0, -300, 2350, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sleep(300)
    BeginChrThread(0x3F, 3, 0, 89)
    Return()

    # Function_94_10E01 end

    def Function_95_11145(): pass

    label("Function_95_11145")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1119A")
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Jump("Function_95_11145")

    label("loc_1119A")

    Return()

    # Function_95_11145 end

    def Function_96_1119B(): pass

    label("Function_96_1119B")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_111AB():
        OP_95(0xFE, 600, 250, 400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_111AB)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x6)
    Sound(809, 0, 100, 0)

    def lambda_111D3():
        OP_9D(0xFE, 0x6A4, 0x64, 0x1130, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_111D3)
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

    def lambda_11272():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_11272)
    OP_52(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_11296():
        OP_9D(0xFE, 0x7D0, 0x64, 0x1E78, 0x12C, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_11296)
    WaitChrThread(0xFE, 1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_96_1119B end

    def Function_97_112BA(): pass

    label("Function_97_112BA")

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

    # Function_97_112BA end

    def Function_98_11302(): pass

    label("Function_98_11302")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1131A():
        OP_95(0xFE, -600, 250, 400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1131A)
    WaitChrThread(0xFE, 1)

    def lambda_11338():
        OP_95(0xFE, -1300, 100, 4400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11338)
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

    def lambda_113FA():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_113FA)

    def lambda_11413():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_11413)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)

    def lambda_1144D():
        OP_95(0xFE, -1400, 100, 5400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1144D)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)

    def lambda_114D5():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_114D5)

    def lambda_114EE():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_114EE)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)

    def lambda_11528():
        OP_95(0xFE, -1500, 100, 6400, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11528)
    Sound(533, 0, 60, 0)
    Sleep(100)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(815, 0, 100, 0)
    Sound(635, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x3, 0, 1100, 0, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)

    def lambda_115B0():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_115B0)

    def lambda_115C9():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_115C9)
    WaitChrThread(0xFE, 1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_98_11302 end

    def Function_99_115FA(): pass

    label("Function_99_115FA")

    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)

    def lambda_11607():
        OP_95(0xFE, -3900, 250, 8800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11607)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x5)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    Sound(844, 0, 100, 0)

    def lambda_1164A():
        OP_9C(0xFE, 0x0, 0x2BC, 0x0, 0x2EE, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1164A)
    SetChrSubChip(0xFE, 0x14)
    Sleep(50)
    BeginChrThread(0xFE, 2, 0, 100)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    Return()

    # Function_99_115FA end

    def Function_100_11688(): pass

    label("Function_100_11688")

    EndChrThread(0x43, 0x0)
    EndChrThread(0x43, 0x2)
    SetChrChipByIndex(0x43, 0xB)
    SetChrSubChip(0x43, 0x0)
    OP_52(0x43, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_116A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11795")
    Sound(815, 0, 100, 0)
    Sound(635, 0, 50, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x4, 0xFF, 0x43, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_11707():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_11707)
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
    Jump("loc_116A3")

    label("loc_11795")

    Return()

    # Function_100_11688 end

    def Function_101_11796(): pass

    label("Function_101_11796")

    SetChrChipByIndex(0x34, 0x3)
    SetChrSubChip(0x34, 0x0)

    def lambda_117A3():
        OP_95(0xFE, -6500, 250, 6800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_117A3)
    WaitChrThread(0x34, 1)
    SetChrChipByIndex(0x34, 0x2)
    SetChrSubChip(0x34, 0x0)
    Return()

    # Function_101_11796 end

    def Function_102_117C5(): pass

    label("Function_102_117C5")

    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)

    def lambda_117D2():
        OP_95(0xFE, -800, 100, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_117D2)
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

    # Function_102_117C5 end

    def Function_103_1187E(): pass

    label("Function_103_1187E")

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

    # Function_103_1187E end

    def Function_104_1198B(): pass

    label("Function_104_1198B")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_119AB():
        OP_95(0xFE, -8500, 150, 3500, 9000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_119AB)
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
        "#03401F#9Aハッ……！\x02",
    )
    #Auto

    Sleep(700)

    def lambda_11A1E():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11A1E)
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

    def lambda_11AC5():
        OP_9D(0xFE, 0xFFFFDF94, 0xFA, 0x2454, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_11AC5)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    CancelBlur(700)
    Sleep(500)
    Sound(880, 0, 100, 0)
    Sleep(1500)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_104_1198B end

    def Function_105_11B02(): pass

    label("Function_105_11B02")

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

    # Function_105_11B02 end

    def Function_106_11B3B(): pass

    label("Function_106_11B3B")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_11B5B():
        OP_95(0xFE, 2500, 100, -2600, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11B5B)
    WaitChrThread(0xFE, 1)

    #C0426
    ChrTalk(
        0x28,
        "#12P#11507F#9Aそーらよっ！\x02",
    )
    #Auto

    TurnDirection(0xFE, 0x3E, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrSubChip(0xFE, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_11BAE():
        OP_9D(0xFE, 0x1194, 0x5DC, 0x258, 0x76C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11BAE)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 100, 0)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Sound(844, 0, 100, 0)

    def lambda_11BEF():
        OP_9D(0xFE, 0x1A90, 0xFA, 0xABE, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11BEF)
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

    def lambda_11CE6():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_11CE6)

    def lambda_11CFF():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_11CFF)
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

    def lambda_11D8F():
        OP_A6(0xFE, 0x0, 0x64, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_11D8F)
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

    # Function_106_11B3B end

    def Function_107_1217B(): pass

    label("Function_107_1217B")

    SetChrChipByIndex(0xFE, 0x18)
    OP_A0(0xFE, 1500, 0x0, 0x3)
    Return()

    # Function_107_1217B end

    def Function_108_12187(): pass

    label("Function_108_12187")

    SetChrChipByIndex(0xFE, 0x16)

    label("loc_1218B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_121A9")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    OP_A0(0xFE, 1500, 0x3, 0x1)
    Jump("loc_1218B")

    label("loc_121A9")

    Return()

    # Function_108_12187 end

    def Function_109_121AA(): pass

    label("Function_109_121AA")

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

    def lambda_12356():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 2, lambda_12356)
    Sleep(50)
    EndChrThread(0x41, 0x0)
    EndChrThread(0x41, 0x2)
    SetChrChipByIndex(0x41, 0xB)
    SetChrSubChip(0x41, 0x0)
    OP_52(0x41, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1238D():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x41, 2, lambda_1238D)
    Sleep(50)
    EndChrThread(0x42, 0x0)
    EndChrThread(0x42, 0x2)
    SetChrChipByIndex(0x42, 0xB)
    SetChrSubChip(0x42, 0x0)
    OP_52(0x42, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_123C4():
        OP_A6(0xFE, 0x0, 0x64, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x42, 2, lambda_123C4)
    Sleep(2500)
    CancelBlur(0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sleep(1000)
    Return()

    # Function_109_121AA end

    def Function_110_123F5(): pass

    label("Function_110_123F5")

    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_12439():
        OP_9E(0xFE, 0xFA0, 0xFFFFF448, 0x36EE8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12439)

    label("loc_1244F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12477")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_1244F")

    label("loc_12477")

    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_110_123F5 end

    def Function_111_1248F(): pass

    label("Function_111_1248F")

    SetChrChip(0x0, 0x77, 0x32, 0x12C)

    def lambda_1249C():
        OP_9E(0xFE, 0xFFFFE124, 0x708, 0x2BF20, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x77, 1, lambda_1249C)

    label("loc_124B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_124DA")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_124B2")

    label("loc_124DA")

    WaitChrThread(0x77, 1)
    SetChrChip(0x1, 0x77, 0x0, 0x0)
    OP_A7(0x77, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_111_1248F end

    def Function_112_124F2(): pass

    label("Function_112_124F2")

    SetChrPos(0xFE, -7400, 250, 5400, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0xFE, 2, 0, 113)

    def lambda_12521():
        OP_9E(0xFE, 0xFFFFD9B8, 0x1C84, 0x2BF20, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12521)
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

    def lambda_125BC():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_125BC)

    label("loc_125D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1267D")

    def lambda_125E0():
        OP_9E(0xFE, 0xFFFFD3DC, 0x2CEC, 0x57E40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_125E0)
    WaitChrThread(0xFE, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    Sound(501, 0, 40, 0)
    Sound(308, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x3E, 0x1, 0, 1200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_12664():
        OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_12664)
    Jump("loc_125D0")

    label("loc_1267D")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_112_124F2 end

    def Function_113_12691(): pass

    label("Function_113_12691")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_126DB")
    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1900)
    Jump("Function_113_12691")

    label("loc_126DB")

    Return()

    # Function_113_12691 end

    def Function_114_126DC(): pass

    label("Function_114_126DC")

    PlayEffect(0x8, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)

    def lambda_12720():
        OP_9E(0xFE, 0xFFFFE4A8, 0xFFFFF060, 0xFFFD40E0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12720)

    label("loc_12736")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1275E")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_12736")

    label("loc_1275E")

    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_114_126DC end

    def Function_115_12776(): pass

    label("Function_115_12776")

    Sleep(150)
    SetChrChip(0x0, 0x78, 0x32, 0x12C)

    def lambda_12786():
        OP_9E(0xFE, 0xFFFFF4AC, 0x16A8, 0x2BF20, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x78, 1, lambda_12786)

    label("loc_1279C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_127C4")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    Jump("loc_1279C")

    label("loc_127C4")

    WaitChrThread(0x78, 1)
    SetChrChip(0x1, 0x78, 0x0, 0x0)
    OP_A7(0x78, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_115_12776 end

    def Function_116_127DC(): pass

    label("Function_116_127DC")

    SetChrPos(0xFE, -7400, 250, 6200, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0xFE, 2, 0, 113)

    def lambda_1280B():
        OP_9E(0xFE, 0xFFFFD9B8, 0x1C84, 0xFFFD5468, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1280B)
    WaitChrThread(0xFE, 1)

    label("loc_12825")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12854")

    def lambda_12835():
        OP_9E(0xFE, 0xFFFFCE00, 0x17D4, 0xFFFA81C0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12835)
    WaitChrThread(0xFE, 1)
    Jump("loc_12825")

    label("loc_12854")

    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_116_127DC end

    def Function_117_12868(): pass

    label("Function_117_12868")

    BeginChrThread(0x3C, 1, 0, 123)
    Sleep(300)
    BeginChrThread(0x38, 1, 0, 123)
    Sleep(300)
    BeginChrThread(0x48, 1, 0, 123)
    BeginChrThread(0x72, 3, 0, 81)
    Return()

    # Function_117_12868 end

    def Function_118_12887(): pass

    label("Function_118_12887")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x2710, 0x0)

    def lambda_128A0():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_128A0)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x2710, 0x0)

    def lambda_128CD():
        OP_D5(0xFE, 0x0, 0xFFFEEE90, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_128CD)
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

    # Function_118_12887 end

    def Function_119_12969(): pass

    label("Function_119_12969")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x2710, 0x0)

    def lambda_12982():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12982)
    OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x2710, 0x0)

    def lambda_129AF():
        OP_D5(0xFE, 0x0, 0x11170, 0x0, 0x4B0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_129AF)
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

    # Function_119_12969 end

    def Function_120_12A3C(): pass

    label("Function_120_12A3C")

    OP_96(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3A98, 0x0)

    def lambda_12A55():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12A55)
    SetMapObjFrame(0x14, "kage", 0x0, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    BeginChrThread(0x75, 3, 0, 121)
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x514, 0x514)

    def lambda_12A9D():
        OP_D5(0xFE, 0x0, 0x1B58, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12A9D)
    OP_82(0x0, 0xC8, 0xBB8, 0xC8)
    Sound(833, 0, 100, 0)
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x12C, 0x44C)
    EndChrThread(0xFE, 0x2)

    def lambda_12AE8():
        OP_D5(0xFE, 0x0, 0xFFFFE4A8, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12AE8)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    Sound(833, 0, 100, 0)
    Sound(487, 0, 100, 0)
    SetMapObjFrame(0x14, "kage", 0x1, 0x1)
    SetMapObjFlags(0x15, 0x4)
    EndChrThread(0x75, 0x3)
    BeginChrThread(0x74, 3, 0, 122)

    def lambda_12B3A():
        OP_96(0xFE, 0x0, 0xC8, 0x9C40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12B3A)
    WaitChrThread(0xFE, 2)

    def lambda_12B58():
        OP_D5(0xFE, 0x0, 0x0, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12B58)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_120_12A3C end

    def Function_121_12B71(): pass

    label("Function_121_12B71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12B98")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x73, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x73, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_121_12B71")

    label("loc_12B98")

    Return()

    # Function_121_12B71 end

    def Function_122_12B99(): pass

    label("Function_122_12B99")

    Sleep(3100)
    Sound(880, 0, 100, 0)
    Sound(991, 0, 100, 0)
    Sound(200, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -900, 1200, 31000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 900, 1200, 31000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x1F4)
    OP_71(0x17, 0x0, 0xA, 0x0, 0x0)
    Return()

    # Function_122_12B99 end

    def Function_123_12C3A(): pass

    label("Function_123_12C3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12C8F")
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_123_12C3A")

    label("loc_12C8F")

    Return()

    # Function_123_12C3A end

    def Function_124_12C90(): pass

    label("Function_124_12C90")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 0, 1100, 1100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    label("loc_12CC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12D62")
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
    Jump("loc_12CC7")

    label("loc_12D62")

    Return()

    # Function_124_12C90 end

    def Function_125_12D63(): pass

    label("Function_125_12D63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12D81")
    OP_A1(0xFE, 0xFA0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_125_12D63")

    label("loc_12D81")

    Return()

    # Function_125_12D63 end

    def Function_126_12D82(): pass

    label("Function_126_12D82")


    def lambda_12D87():
        OP_96(0xFE, 0xA8C, 0xFA, 0x283C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_12D87)
    Sleep(50)

    def lambda_12DA4():
        OP_96(0xFE, 0x44C, 0x64, 0x206C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_12DA4)
    Sleep(100)
    SetChrChipByIndex(0x34, 0x3)
    SetChrSubChip(0x34, 0x0)

    def lambda_12DC9():
        OP_96(0xFE, 0xFFFFF18C, 0xFA, 0x2454, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_12DC9)
    Sleep(50)
    SetChrChipByIndex(0x35, 0x7)
    SetChrSubChip(0x35, 0x0)

    def lambda_12DEE():
        OP_96(0xFE, 0xFFFFF2B8, 0x64, 0x1BBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_12DEE)
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

    # Function_126_12D82 end

    def Function_127_12E2C(): pass

    label("Function_127_12E2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E45")
    Sound(567, 0, 100, 0)
    Sleep(1200)
    Jump("Function_127_12E2C")

    label("loc_12E45")

    Return()

    # Function_127_12E2C end

    def Function_128_12E46(): pass

    label("Function_128_12E46")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E5F")
    Sound(530, 0, 70, 0)
    Sleep(1200)
    Jump("Function_128_12E46")

    label("loc_12E5F")

    Return()

    # Function_128_12E46 end

    def Function_129_12E60(): pass

    label("Function_129_12E60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12E79")
    Sound(530, 0, 50, 0)
    Sleep(1200)
    Jump("Function_129_12E60")

    label("loc_12E79")

    Return()

    # Function_129_12E60 end

    def Function_130_12E7A(): pass

    label("Function_130_12E7A")

    Sound(987, 0, 100, 0)

    label("loc_12E80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12EC0")
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
    Jump("loc_12E80")

    label("loc_12EC0")

    Return()

    # Function_130_12E7A end

    def Function_131_12EC1(): pass

    label("Function_131_12EC1")

    Sound(987, 0, 50, 0)

    label("loc_12EC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12F07")
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
    Jump("loc_12EC7")

    label("loc_12F07")

    Return()

    # Function_131_12EC1 end

    def Function_132_12F08(): pass

    label("Function_132_12F08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12F24")
    Sound(567, 0, 40, 0)
    Sleep(500)
    Sleep(500)
    Jump("Function_132_12F08")

    label("loc_12F24")

    Return()

    # Function_132_12F08 end

    def Function_133_12F25(): pass

    label("Function_133_12F25")

    Sound(457, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(2000)
    Sound(458, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Return()

    # Function_133_12F25 end

    def Function_134_12F50(): pass

    label("Function_134_12F50")

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

    # Function_134_12F50 end

    def Function_135_12F9F(): pass

    label("Function_135_12F9F")

    SetChrChipByIndex(0xFE, 0x9)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12FB9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FD7")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_12FB9")

    label("loc_12FD7")

    Return()

    # Function_135_12F9F end

    def Function_136_12FD8(): pass

    label("Function_136_12FD8")

    SetChrChipByIndex(0xFE, 0xA)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12FF2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13009")
    OP_A0(0xFE, 700, 0x0, 0x5)
    Jump("loc_12FF2")

    label("loc_13009")

    Return()

    # Function_136_12FD8 end

    def Function_137_1300A(): pass

    label("Function_137_1300A")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A6(0xFE, 0x0, 0x64, 0x12C, 0xBB8)
    Return()

    # Function_137_1300A end

    def Function_138_1303C(): pass

    label("Function_138_1303C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13091")
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
    Jump("Function_138_1303C")

    label("loc_13091")

    Return()

    # Function_138_1303C end

    def Function_139_13092(): pass

    label("Function_139_13092")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130E7")
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
    Jump("Function_139_13092")

    label("loc_130E7")

    Return()

    # Function_139_13092 end

    def Function_140_130E8(): pass

    label("Function_140_130E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1313D")
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
    Jump("Function_140_130E8")

    label("loc_1313D")

    Return()

    # Function_140_130E8 end

    def Function_141_1313E(): pass

    label("Function_141_1313E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13193")
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
    Jump("Function_141_1313E")

    label("loc_13193")

    Return()

    # Function_141_1313E end

    def Function_142_13194(): pass

    label("Function_142_13194")

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
    OP_8E(0x2F, "キリカ")
    OP_8E(0x28, "レクター")
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
        "#5Pおお……！\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x38,
        "#12Pき、消えた……！？\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x2F,
        (
            "#03400F……霊力の供給が\x01",
            "途絶えたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x28,
        (
            "#11P#11506Fやれやれ……\x01",
            "マジで疲れたぜぇ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x23,
        (
            "#01002Fフッ……\x01",
            "やりやがったな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_142_13194 end

    def Function_143_138C9(): pass

    label("Function_143_138C9")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x0, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(985, 0, 100, 0)
    Sleep(1800)

    def lambda_13924():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13924)
    WaitChrThread(0xFE, 2)
    StopEffect(0x0, 0x2)
    Return()

    # Function_143_138C9 end

    def Function_144_13938(): pass

    label("Function_144_13938")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2400)

    def lambda_1398A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1398A)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_144_13938 end

    def Function_145_1399E(): pass

    label("Function_145_1399E")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2800)

    def lambda_139F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_139F0)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_145_1399E end

    def Function_146_13A04(): pass

    label("Function_146_13A04")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x3, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2600)

    def lambda_13A56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13A56)
    WaitChrThread(0xFE, 2)
    StopEffect(0x3, 0x2)
    Return()

    # Function_146_13A04 end

    def Function_147_13A6A(): pass

    label("Function_147_13A6A")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x4, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)

    def lambda_13ABC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13ABC)
    WaitChrThread(0xFE, 2)
    StopEffect(0x4, 0x2)
    Return()

    # Function_147_13A6A end

    def Function_148_13AD0(): pass

    label("Function_148_13AD0")

    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0x5, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2200)

    def lambda_13B22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13B22)
    WaitChrThread(0xFE, 2)
    StopEffect(0x5, 0x2)
    Return()

    # Function_148_13AD0 end

    def Function_149_13B36(): pass

    label("Function_149_13B36")

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

    # Function_149_13B36 end

    def Function_150_13DF7(): pass

    label("Function_150_13DF7")

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

    # Function_150_13DF7 end

    SaveToFile()

Try(main)
