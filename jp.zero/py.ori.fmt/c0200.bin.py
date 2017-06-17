from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0200.bin",                # FileName
        "c0200",                    # MapName
        "c0200",                    # Location
        0x000A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 9, 0, 10],
    )

    BuildStringList((
        "c0200",                  # 0
        "リュウ",                 # 1
        "アンリ",                 # 2
        "ポンス",                 # 3
        "ブリック",               # 4
        "モモ",                   # 5
        "ベネット",               # 6
        "ルーヴィック老人",       # 7
        "エルサ",                 # 8
        "ツァイト",               # 9
        "ダドリー捜査官",         # 10
        "ツァイト",               # 11
        "車１",                   # 12
        "群衆１",                 # 13
        "群衆２",                 # 14
        "群衆３",                 # 15
        "群衆４",                 # 16
        "群衆５",                 # 17
        "オスカー",               # 18
        "中央広場",               # 19
        "西通り",                 # 20
        "行政区",                 # 21
        "住宅街",                 # 22
        "歓楽街",                 # 23
        "東通り",                 # 24
        "旧市街",                 # 25
        "港湾区",                 # 26
        "ＩＢＣ",                 # 27
        "駅前通り",               # 28
        "裏通り",                 # 29
        "ウルスラ間道",           # 30
        "東クロスベル街道",       # 31
        "西クロスベル街道",       # 32
        "マインツ山道",           # 33
    ))

    AddCharChip((
        "chr/ch20600.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20402.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch34300.itc",                   # 05
        "chr/ch21600.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch02707.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(449,     0,       610,     90,   257,  0x0, 0,   0,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(-1000,   0,       610,     90,   257,  0x0, 0,   1,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(-15119,  0,       5829,    270,  261,  0x0, 0,   2,   0,   0,   2,   0,   17,  255,  0)
    DeclNpc(6570,    -150,    5119,    90,   341,  0x0, 0,   3,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    257,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(3240,    -300,    4559,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-14420,  0,       4199,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    261,  0x0, 0,   7,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(29809,   -4000,   -18139,  225,  404,  0x0, 0,   8,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       180,  453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  11.5,                  15.5,                  2.0,                   49.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.75,                 -2.2142858505249023,   -0.4000000059604645,   1.0])
    DeclEvent(0x0000, 0, 32,  39.5,                  -19.0,                 -4.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -19.75,                9.5,                   0.9000000357627869,    1.0])

    DeclActor(14410,   -6500,   -13590,  1200,    14410,   -5500,   -13590,  0x007C, 0,  11, 0x0000)
    DeclActor(-32070,  -1000,   11050,   1200,    -32070,  0,       11050,   0x007C, 0,  12, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "中央広場")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "西通り")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "行政区")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "住宅街")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "東通り")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "旧市街")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "港湾区")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "裏通り")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")
    PlaceName(82.0, 0.0, -19.0, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_6EC",          # 00, 0
        "Function_1_7A4",          # 01, 1
        "Function_2_805",          # 02, 2
        "Function_3_866",          # 03, 3
        "Function_4_891",          # 04, 4
        "Function_5_965",          # 05, 5
        "Function_6_A39",          # 06, 6
        "Function_7_B0D",          # 07, 7
        "Function_8_BE1",          # 08, 8
        "Function_9_CB5",          # 09, 9
        "Function_10_11C3",        # 0A, 10
        "Function_11_13EE",        # 0B, 11
        "Function_12_1551",        # 0C, 12
        "Function_13_169E",        # 0D, 13
        "Function_14_1FC6",        # 0E, 14
        "Function_15_2536",        # 0F, 15
        "Function_16_265D",        # 10, 16
        "Function_17_3006",        # 11, 17
        "Function_18_3DCA",        # 12, 18
        "Function_19_4C31",        # 13, 19
        "Function_20_5242",        # 14, 20
        "Function_21_53E1",        # 15, 21
        "Function_22_54BD",        # 16, 22
        "Function_23_5815",        # 17, 23
        "Function_24_594C",        # 18, 24
        "Function_25_653D",        # 19, 25
        "Function_26_7633",        # 1A, 26
        "Function_27_795F",        # 1B, 27
        "Function_28_7D7D",        # 1C, 28
        "Function_29_833A",        # 1D, 29
        "Function_30_877A",        # 1E, 30
        "Function_31_882A",        # 1F, 31
        "Function_32_8846",        # 20, 32
        "Function_33_8862",        # 21, 33
    ))


    def Function_0_6EC(): pass

    label("Function_0_6EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_72C"),
        (1, "loc_738"),
        (2, "loc_744"),
        (3, "loc_750"),
        (4, "loc_75C"),
        (5, "loc_768"),
        (6, "loc_774"),
        (SWITCH_DEFAULT, "loc_780"),
    )


    label("loc_72C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_738")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_744")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_750")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_75C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_768")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_774")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_780")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_78C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_7A3")

    Return()

    # Function_0_6EC end

    def Function_1_7A4(): pass

    label("Function_1_7A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_804")
    OP_95(0xFE, 7000, -300, 610, 6000, 0x0)
    OP_95(0xFE, 7000, 0, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, -10, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, 0, 610, 6000, 0x0)
    Jump("Function_1_7A4")

    label("loc_804")

    Return()

    # Function_1_7A4 end

    def Function_2_805(): pass

    label("Function_2_805")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_865")
    OP_95(0xFE, -5160, 0, 5750, 800, 0x0)
    OP_95(0xFE, -5160, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 5750, 800, 0x0)
    Jump("Function_2_805")

    label("loc_865")

    Return()

    # Function_2_805 end

    def Function_3_866(): pass

    label("Function_3_866")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_890")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_3_866")

    label("loc_890")

    Return()

    # Function_3_866 end

    def Function_4_891(): pass

    label("Function_4_891")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_964")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D0")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF40C, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_8D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F8")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF3A8, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_8F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_920")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF344, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_920")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_948")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF2E0, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_948")

    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF27C, 0x12C, 0x0)

    label("loc_95C")

    Sleep(500)
    Jump("Function_4_891")

    label("loc_964")

    Return()

    # Function_4_891 end

    def Function_5_965(): pass

    label("Function_5_965")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A38")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A4")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF40C, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9CC")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF3A8, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9F4")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF344, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1C")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF2E0, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_A1C")

    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF27C, 0xC8, 0x0)

    label("loc_A30")

    Sleep(600)
    Jump("Function_5_965")

    label("loc_A38")

    Return()

    # Function_5_965 end

    def Function_6_A39(): pass

    label("Function_6_A39")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B0C")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A78")
    OP_96(0xFE, 0x11A8, 0x0, 0xFFFFF1AA, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_A78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA0")
    OP_96(0xFE, 0x11DA, 0x0, 0xFFFFF1DC, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AC8")
    OP_96(0xFE, 0x120C, 0x0, 0xFFFFF20E, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF0")
    OP_96(0xFE, 0x123E, 0x0, 0xFFFFF240, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AF0")

    OP_96(0xFE, 0x1270, 0x0, 0xFFFFF272, 0x12C, 0x0)

    label("loc_B04")

    Sleep(500)
    Jump("Function_6_A39")

    label("loc_B0C")

    Return()

    # Function_6_A39 end

    def Function_7_B0D(): pass

    label("Function_7_B0D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE0")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B4C")
    OP_96(0xFE, 0xE24, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B74")
    OP_96(0xFE, 0xDF2, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B9C")
    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BC4")
    OP_96(0xFE, 0xD8E, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_BC4")

    OP_96(0xFE, 0xD5C, 0x0, 0xFFFFF92A, 0xFA, 0x0)

    label("loc_BD8")

    Sleep(550)
    Jump("Function_7_B0D")

    label("loc_BE0")

    Return()

    # Function_7_B0D end

    def Function_8_BE1(): pass

    label("Function_8_BE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CB4")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C20")
    OP_96(0xFE, 0x910, 0x0, 0xFFFFF272, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C48")
    OP_96(0xFE, 0x942, 0x0, 0xFFFFF240, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C70")
    OP_96(0xFE, 0x974, 0x0, 0xFFFFF20E, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C98")
    OP_96(0xFE, 0x9A6, 0x0, 0xFFFFF1DC, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C98")

    OP_96(0xFE, 0x9D8, 0x0, 0xFFFFF1AA, 0xC8, 0x0)

    label("loc_CAC")

    Sleep(600)
    Jump("Function_8_BE1")

    label("loc_CB4")

    Return()

    # Function_8_BE1 end

    def Function_9_CB5(): pass

    label("Function_9_CB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E21")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D80")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D53")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_D72")

    label("loc_D53")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D72")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_D72")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E21")

    label("loc_D80")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF9")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_E18")

    label("loc_DF9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E18")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_E18")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E21")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E91")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xA, -25120, 0, 4140, 180)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_EE3")
    SetChrPos(0x9, 8670, 0, -5340, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0x8, -1000, 0, 610, 90)
    SetChrPos(0xC, 450, 0, 610, 90)
    BeginChrThread(0xC, 0, 0, 1)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_F3B")
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 6)
    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 7)
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 8)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F81")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 4)
    SetChrPos(0xC, 2580, 0, -3260, 90)
    BeginChrThread(0xC, 0, 0, 5)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_FDA")
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_FA7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_FD5")

    label("loc_FA7")

    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_FD5")

    Jump("loc_1177")

    label("loc_FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1020")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1038")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1083")
    SetChrPos(0x8, 29770, -4000, -19580, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 27640, -4000, -18980, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1177")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10CE")
    SetChrPos(0x8, 29770, -4000, -19580, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 27640, -4000, -18980, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1177")

    label("loc_10CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_111C")
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1117")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_1117")

    Jump("loc_1177")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1139")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1156")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1169")
    SetChrFlags(0xC, 0x80)
    Jump("loc_1177")

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1177")
    SetChrFlags(0xC, 0x80)

    label("loc_1177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1188")
    Event(0, 27)

    label("loc_1188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_119C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)
    Jump("loc_11AB")

    label("loc_119C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_11AB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 26)

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C2")
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_11C2")

    Return()

    # Function_9_CB5 end

    def Function_10_11C3(): pass

    label("Function_10_11C3")

    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_11F9")
    ClearMapObjFlags(0xD, 0x4)

    label("loc_11F9")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1211")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1211")

    SetMapObjFrame(0xFF, "br02", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_126E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_12DF")

    label("loc_126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12BA")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_12DF")

    label("loc_12BA")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_12DF")

    ClearMapObjFlags(0x9, 0x10)
    OP_70(0x9, 0x1E)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1301")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1314")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1327")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133A")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1348")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1348")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1374")
    OP_1B(0x0, 0x0, 0x1E)
    OP_1B(0x1, 0x0, 0x1F)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_139E")
    OP_1B(0x0, 0x0, 0x1E)

    label("loc_139E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B1")
    OP_70(0x7, 0x0)
    Jump("loc_13B5")

    label("loc_13B1")

    OP_70(0x7, 0x1E)

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C8")
    OP_70(0x8, 0x0)
    Jump("loc_13CC")

    label("loc_13C8")

    OP_70(0x8, 0x1E)

    label("loc_13CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E8")
    Jump("loc_13ED")

    label("loc_13E8")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_13ED")

    Return()

    # Function_10_11C3 end

    def Function_11_13EE(): pass

    label("Function_11_13EE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151A")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x7, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×８０\x01\x07\x02",

            "#57I水のセピス×８０\x01\x07\x02",

            "#58I火のセピス×８０\x01\x07\x02",

            "#59I風のセピス×８０\x01\x07\x02",

            "#60I時のセピス×８０\x01\x07\x02",

            "#61I空のセピス×８０\x01\x07\x02",

            "#62I幻のセピス×８０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x110, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_153F")

    label("loc_151A")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_153F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_13EE end

    def Function_12_1551(): pass

    label("Function_12_1551")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164D")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_15D6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1648")

    label("loc_15D6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1648")

    Jump("loc_1692")

    label("loc_164D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1692")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1551 end

    def Function_13_169E(): pass

    label("Function_13_169E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BC")
    Call(0, 14)
    Jump("loc_1724")

    label("loc_16BC")


    #C0006
    ChrTalk(
        0xFE,
        (
            "モモを脅かしたら\x01",
            "泣きながら逃げてったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ちぇっ、やっぱり\x01",
            "ジョシと遊ぶのって疲れるよな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1724")

    Jump("loc_1FC2")

    label("loc_1729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1780")

    #C0008
    ChrTalk(
        0xFE,
        "オラオラ、がお～っ……！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "もたもたしてっと\x01",
            "追いついちまうぞ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_1780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1791")
    Call(0, 15)
    Jump("loc_1FC2")

    label("loc_1791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_18CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1868")
    OP_4B(0xC, 0xFF)

    #C0010
    ChrTalk(
        0xFE,
        (
            "へっ、石けりはオレの\x01",
            "ちょー得意分野だぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)

    #C0011
    ChrTalk(
        0xFE,
        (
            "ほらモモ、そっちいったぞ！\x01",
            "ちゃんと取れよなっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0012
    ChrTalk(
        0xC,
        "……うん……！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_18C9")

    label("loc_1868")


    #C0013
    ChrTalk(
        0xFE,
        "アンリのやつ、今日はおっせ～なー。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "ちぇっ、しょうがねえから\x01",
            "しばらくモモと遊ぶかな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C9")

    Jump("loc_1FC2")

    label("loc_18CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_194B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E9")
    Call(0, 14)
    Jump("loc_1946")

    label("loc_18E9")


    #C0015
    ChrTalk(
        0xFE,
        "はー、べんきょーとか退屈だぜ。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "アンリはいいよなー。\x01",
            "シスターにも怒られねーしさぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1946")

    Jump("loc_1FC2")

    label("loc_194B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_19FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1966")
    Call(0, 14)
    Jump("loc_19FA")

    label("loc_1966")


    #C0017
    ChrTalk(
        0xFE,
        (
            "ちくしょー、支援課のくせに\x01",
            "ナマイキだぞー！\x02",
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

    label("loc_19FA")

    Jump("loc_1FC2")

    label("loc_19FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A3C")

    #C0018
    ChrTalk(
        0xFE,
        (
            "へっへー、今日は\x01",
            "どこに遊びに行くかな～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B47")
    OP_93(0x8, 0x0, 0x0)

    #C0019
    ChrTalk(
        0xFE,
        (
            "ツァイトってよく\x01",
            "この辺りパトロールしてんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "へへっ、いいじゃん。\x01",
            "今日はオレも連れてってくれよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x12,
        "#1200Fグルルルル……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#0200F（また気が向いたらな、\x01",
            "  と言っています。）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#0000F（まるで立場が逆だなぁ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BA6")

    label("loc_1B47")


    #C0024
    ChrTalk(
        0xFE,
        (
            "ツァイトってよくこの辺りを\x01",
            "パトロールしてんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "警察犬かぁ、カッコイイよな～！\x02",
    )

    CloseMessageWindow()

    label("loc_1BA6")

    Jump("loc_1FC2")

    label("loc_1BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1CE6")
    SetScenarioFlags(0x90, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7B")

    #C0026
    ChrTalk(
        0xFE,
        (
            "ツァイトって大きくて\x01",
            "カッコイイよな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "余裕ありげな感じがたまんねーぜ！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0000Fすっかりヒーロー扱いだな……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#0100F男の子にとっては\x01",
            "そうなのかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CE1")

    label("loc_1C7B")

    OP_93(0x8, 0x0, 0x0)

    #C0030
    ChrTalk(
        0xFE,
        "ツァイト～、こっち向いてくれよ～！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "うおお、牙でっけえ～！\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    label("loc_1CE1")

    Jump("loc_1FC2")

    label("loc_1CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1E1B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0E")
    Call(0, 14)
    Jump("loc_1D57")

    label("loc_1D0E")


    #C0032
    ChrTalk(
        0xFE,
        (
            "やっぱケーサツなんて\x01",
            "ダメダメだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "頼りになんのは遊撃士だぜ！\x02",
    )

    CloseMessageWindow()

    label("loc_1D57")

    Jump("loc_1E16")

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE3")

    #C0034
    ChrTalk(
        0xFE,
        "あ、支援課の兄ちゃんたち。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "……フン、仕事頑張れよなっ！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0000Fはは……\x01",
            "（少しは認めてくれたのかな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E16")

    label("loc_1DE3")


    #C0037
    ChrTalk(
        0xFE,
        (
            "支援課の兄ちゃんたち\x01",
            "……仕事、頑張れよなっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E16")

    Jump("loc_1FC2")

    label("loc_1E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1E29")
    Jump("loc_1FC2")

    label("loc_1E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1E37")
    Jump("loc_1FC2")

    label("loc_1E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1E74")

    #C0038
    ChrTalk(
        0xFE,
        (
            "とりゃとりゃ～！\x01",
            "最強のゆーげきし参上～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC2")

    label("loc_1E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8D")

    #C0039
    ChrTalk(
        0xFE,
        "あっ、あの時の兄ちゃんじゃん！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "なんだよー、いっちょ前に\x01",
            "パトロールか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0006F……あのな。\x01",
            "警察官は色々と忙しいんだよ。\x02\x03",

            "#0000Fってそれより、そっちこそ\x01",
            "もう無茶な真似はするなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "うっ……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "へ、へーんだ。\x01",
            "知らねーな、そんな事～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FC2")

    label("loc_1F8D")


    #C0044
    ChrTalk(
        0xFE,
        (
            "それそれ～、オレが\x01",
            "アリオス・マクレインだぜ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC2")

    TalkEnd(0xFE)
    Return()

    # Function_13_169E end

    def Function_14_1FC6(): pass

    label("Function_14_1FC6")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_206B")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    #C0045
    ChrTalk(
        0x8,
        (
            "なんだよ～\x01",
            "ただの鬼ごっこじゃんかー。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "だからぁ、リュウは\x01",
            "やりすぎなんだって～！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "明日ちゃんと\x01",
            "謝らないとダメだよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2527")

    label("loc_206B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2122")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    #C0048
    ChrTalk(
        0x8,
        (
            "今日は日曜学校なんだよな～。\x01",
            "ちぇっ、サボっちまおうかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "ダメだよリュウ。\x01",
            "ちゃんとしないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "ほら、モモちゃんもさそって\x01",
            "早く行こうよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2527")

    label("loc_2122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_22B2")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    #C0051
    ChrTalk(
        0x8,
        (
            "なあアンリ～、ちょっと\x01",
            "街道の方に出てみようぜ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "へへっ、父ちゃん\x01",
            "最近忙しくしてっからな。\x01",
            "今なら楽勝だぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x9,
        "あ、あのリュウ～。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0054
    ChrTalk(
        0x8,
        "ん～、なんだよ～……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0001Fお・ま・え・ら～……\x01",
            "子供だけで街道に出るなんて\x01",
            "ダメに決まってるだろ！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0056
    ChrTalk(
        0x8,
        (
            "うわあ、支援課の兄ちゃんだ！\x01",
            "やっべー……っ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 0)
    Jump("loc_2527")

    label("loc_22B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_22C0")
    Jump("loc_2527")

    label("loc_22C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2527")
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0057
    ChrTalk(
        0x8,
        "あ、支援課の兄ちゃんじゃん。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "プププー、遅かったな～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        "#0005Fへ……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CD")

    #C0060
    ChrTalk(
        0x9,
        (
            "実は迷子の仔猫を\x01",
            "見つけたんですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23F8")

    label("loc_23CD")


    #C0061
    ChrTalk(
        0x9,
        (
            "実は昨日の\x01",
            "迷子の仔猫なんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F8")


    #C0062
    ChrTalk(
        0x9,
        (
            "通りがかった\x01",
            "遊撃士のお姉さんが\x01",
            "解決してくれたんです！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "黒髪の兄ちゃんとコンビでさ、\x01",
            "あっという間だったよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "へへっ、さっすが遊撃士。\x01",
            "オンナなのにすごかったぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        "#0105Fそ、その２人って……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#0200Fエステルさんと\x01",
            "ヨシュアさん……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#0303F先、越されちまったか……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x5A, 0x0)

    label("loc_2527")

    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_14_1FC6 end

    def Function_15_2536(): pass

    label("Function_15_2536")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0x8, 0xC, 0)
    TurnDirection(0xC, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25EA")

    #C0068
    ChrTalk(
        0x8,
        (
            "やっぱ３人の方が\x01",
            "遊びがいがあるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "よしモモ、お前\x01",
            "今度から遊びにこいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xC,
        "……………………！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        "うん、一緒にあそぶ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2643")

    label("loc_25EA")


    #C0072
    ChrTalk(
        0x8,
        (
            "ほらモモ、パスだ！\x01",
            "ちゃんと受け取れよなっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0073
    ChrTalk(
        0xC,
        "うん……！\x02",
    )

    CloseMessageWindow()

    label("loc_2643")

    OP_93(0x8, 0x13B, 0x0)
    OP_93(0xC, 0x2D, 0x0)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_15_2536 end

    def Function_16_265D(): pass

    label("Function_16_265D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_26AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267B")
    Call(0, 14)
    Jump("loc_26A8")

    label("loc_267B")


    #C0074
    ChrTalk(
        0xFE,
        (
            "リュウ、明日は\x01",
            "ちゃんと謝らなくちゃ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A8")

    Jump("loc_3002")

    label("loc_26AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2708")
    OP_93(0xFE, 0x10E, 0x0)

    #C0075
    ChrTalk(
        0xFE,
        "ちょ、ちょっとリュウ～！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "そんなに追いかけちゃ可哀相だよ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3002")

    label("loc_2708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2767")

    #C0077
    ChrTalk(
        0xFE,
        "今日は３人で遊んでるんです。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "えへへ……\x01",
            "２人より３人の方が楽しいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3002")

    label("loc_2767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2775")
    Jump("loc_3002")

    label("loc_2775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_27F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2790")
    Call(0, 14)
    Jump("loc_27EF")

    label("loc_2790")


    #C0079
    ChrTalk(
        0xFE,
        "今日は僕たち日曜学校なんです。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "リュウはいっつもサボろうとするから\x01",
            "大変なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EF")

    Jump("loc_3002")

    label("loc_27F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_280F")
    Call(0, 14)
    Jump("loc_287B")

    label("loc_280F")


    #C0081
    ChrTalk(
        0xFE,
        (
            "す、すみません、前に\x01",
            "危ない所を助けてもらったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "リュウにはよく\x01",
            "言い聞かせておきますから～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287B")

    Jump("loc_3002")

    label("loc_2880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_29A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2964")

    #C0083
    ChrTalk(
        0xFE,
        (
            "はあ、日曜学校をさぼったこと、\x01",
            "僕もお父さんにすごく怒られました。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "前にマンホールに入ったときも\x01",
            "すごく怒られたんですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "リュウと遊ぶようになってから\x01",
            "いっつも怒られてる気がするなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_299D")

    label("loc_2964")


    #C0086
    ChrTalk(
        0xFE,
        (
            "ちょっとリュウ、\x01",
            "少しは反省しないとダメだよっ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_299D")

    Jump("loc_3002")

    label("loc_29A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2ACB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A60")

    #C0087
    ChrTalk(
        0xFE,
        (
            "リュウは口では\x01",
            "警察のこと馬鹿にしてますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "ほんとはちょっと憧れてるんです。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "えへへ……だって警察には\x01",
            "皆さんみたいな\x01",
            "カッコイイ人もいますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AC6")

    label("loc_2A60")


    #C0090
    ChrTalk(
        0xFE,
        (
            "リュウ、ほんとはちょっと\x01",
            "警察に憧れてるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "いじっぱりだから\x01",
            "口じゃ言わないんですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC6")

    Jump("loc_3002")

    label("loc_2ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2E")

    #C0092
    ChrTalk(
        0xFE,
        (
            "皆さん、この前は\x01",
            "リュウが助けてもらっちゃって……\x01",
            "ほんとにありがとうございました！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "でもツァイトって\x01",
            "すっごくカッコイイですよね！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "僕、こんな警察犬を飼ってるなんて\x01",
            "皆さんはすごいと思います！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#0300Fはは、飼ってるっつーのは\x01",
            "ちょいと語弊があるけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        (
            "#0200F支援課にいるのは\x01",
            "あくまでツァイトの意思ですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D3E")

    label("loc_2C2E")

    OP_93(0xFE, 0x5A, 0x0)

    #C0097
    ChrTalk(
        0xFE,
        "あ、でも……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0098
    ChrTalk(
        0xFE,
        (
            "ねえリュウ～、大聖堂に行かなくていいの～？\x01",
            "日曜学校、もう始まっちゃってるよ～！\x02",
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

    #C0099
    ChrTalk(
        0x101,
        "#0012F学校をさぼっちゃダメだぞ……？\x02",
    )

    CloseMessageWindow()

    label("loc_2D3E")

    Jump("loc_3002")

    label("loc_2D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2E59")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6B")
    Call(0, 14)
    Jump("loc_2DF5")

    label("loc_2D6B")


    #C0100
    ChrTalk(
        0xFE,
        "遊撃士のお姉さん、凄かったです！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "『猫関連の依頼は慣れてるのよね』\x01",
            "って言ってましたよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0100Fそ、そう。\x01",
            "さすが遊撃士ね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF5")

    Jump("loc_2E54")

    label("loc_2DFA")


    #C0103
    ChrTalk(
        0xFE,
        (
            "皆さん、昨日は\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "また何かあったら\x01",
            "皆さんに連絡しますね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E54")

    Jump("loc_3002")

    label("loc_2E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2E67")
    Jump("loc_3002")

    label("loc_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E75")
    Jump("loc_3002")

    label("loc_2E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2ECC")

    #C0105
    ChrTalk(
        0xFE,
        "はあ、はあ……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "もう～、リュウは\x01",
            "ルールが滅茶苦茶なんだから～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3002")

    label("loc_2ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD1")

    #C0107
    ChrTalk(
        0xFE,
        (
            "あ、支援課のみなさん……\x01",
            "先日はありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "僕たち、あの後お父さんたちに\x01",
            "すごく怒られちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#0000Fははは、そっか。\x01",
            "まぁ、君たちが無事でよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "えへへ……みなさん、\x01",
            "お仕事頑張ってくださいね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3002")

    label("loc_2FD1")


    #C0111
    ChrTalk(
        0xFE,
        (
            "待ってよリュウ～、\x01",
            "ルールが間違ってるよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3002")

    TalkEnd(0xFE)
    Return()

    # Function_16_265D end

    def Function_17_3006(): pass

    label("Function_17_3006")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BB")

    #C0112
    ChrTalk(
        0xFE,
        (
            "うーん、今日は\x01",
            "哀愁を誘う夕日だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "そろそろクロスベル大聖堂の\x01",
            "鐘が鳴る頃だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "夕日をバックに大聖堂を\x01",
            "撮るのもいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3114")

    label("loc_30BB")


    #C0115
    ChrTalk(
        0xFE,
        "今日は格別の夕日だね。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "夕日をバックに立つ大聖堂なんて\x01",
            "いい絵になる気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3114")

    Jump("loc_3DC6")

    label("loc_3119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3187")

    #C0117
    ChrTalk(
        0xFE,
        (
            "昨日、港湾区の方で\x01",
            "銃撃戦があったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "怖いねぇ、あんな\x01",
            "オフィス街の真ん中で……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC6")

    label("loc_3187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3216")

    #C0119
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の方にも\x01",
            "遺跡があるんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "僕は最近風景写真に凝ってるんだ。\x01",
            "今度行ってみたいところだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3282")

    label("loc_3216")


    #C0121
    ChrTalk(
        0xFE,
        (
            "クロスベルにはまだまだ\x01",
            "知らない遺跡があるんだなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "市街で暮らしていると\x01",
            "知らない事ばかりだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3282")

    Jump("loc_3DC6")

    label("loc_3287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3417")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338A")

    #C0123
    ChrTalk(
        0xFE,
        (
            "マインツ山道の途中にある遺跡は\x01",
            "中々の撮影スポットだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "僕も風景写真を求めて\x01",
            "あちこち回ったけど……\x01",
            "あそこが一番ぐっとくる気がしたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "静けさが漂っていて\x01",
            "なかなか荘厳な廃墟なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "……中には入れなかったけどね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3412")

    label("loc_338A")


    #C0127
    ChrTalk(
        0xFE,
        (
            "マインツ山道の途中にある遺跡は\x01",
            "落ち着いていて中々の穴場だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "警備隊がロープを張っていたから\x01",
            "中には入れなかったけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3412")

    Jump("loc_3DC6")

    label("loc_3417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_34F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A4")

    #C0129
    ChrTalk(
        0xFE,
        (
            "記念祭中はたくさん\x01",
            "いい写真が撮れたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "どこも賑やかで、笑顔で溢れてて……\x01",
            "いや～、来年も楽しみだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34ED")

    label("loc_34A4")


    #C0131
    ChrTalk(
        0xFE,
        (
            "来年の記念祭では\x01",
            "どんな写真が撮れるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "いや～、楽しみだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_34ED")

    Jump("loc_3DC6")

    label("loc_34F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D3")

    #C0133
    ChrTalk(
        0xFE,
        (
            "クロスベルにはいくつもの\x01",
            "中世の遺跡が残されているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "でもガイドブックに\x01",
            "載っていないことも多くてね。\x01",
            "ほとんど知られていないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "……まあ、それを\x01",
            "探し出すのが楽しいんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3630")

    label("loc_35D3")


    #C0136
    ChrTalk(
        0xFE,
        (
            "クロスベルにはいくつもの\x01",
            "中世の遺跡が残されているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "あまり知られてないけどね。\x02",
    )

    CloseMessageWindow()

    label("loc_3630")

    Jump("loc_3DC6")

    label("loc_3635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_36AD")

    #C0138
    ChrTalk(
        0xFE,
        (
            "今日もいい天気だなぁ。\x01",
            "絶好の行楽日和だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "よーし、カメラを持って\x01",
            "どこかに出掛けるとするかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC6")

    label("loc_36AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_371D")

    #C0140
    ChrTalk(
        0xFE,
        (
            "近頃イアン先生は\x01",
            "とても忙しそうだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "最近なんだかトラブルが\x01",
            "増えたって仰っていたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC6")

    label("loc_371D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_385D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C9")

    #C0142
    ChrTalk(
        0xFE,
        (
            "この道を進めば\x01",
            "西クロスベル街道に出るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "帝国側の国境、\x01",
            "ベルガード門に通じているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "運送トラックなんかは\x01",
            "よく通るんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3858")

    label("loc_37C9")


    #C0145
    ChrTalk(
        0xFE,
        (
            "この道を進めば\x01",
            "西クロスベル街道に出られるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "まあベルガード門の他には\x01",
            "警察学校くらいしかないし……\x01",
            "運送トラックしか通らないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3858")

    Jump("loc_3DC6")

    label("loc_385D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_39A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3923")

    #C0147
    ChrTalk(
        0xFE,
        (
            "導力カメラにも、色々な\x01",
            "メーカーや規格品があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "僕のお気に入りは\x01",
            "ＺＣＦ製のシリーズだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "奇をてらった作りがなくて\x01",
            "初心者にも上級者にも扱い易いんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39A4")

    label("loc_3923")


    #C0150
    ChrTalk(
        0xFE,
        (
            "僕のお気に入りは\x01",
            "ＺＣＦ製のシリーズだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "このカメラシリーズは\x01",
            "１１８０年頃から続いていてね。\x01",
            "コレクターも多いんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39A4")

    Jump("loc_3DC6")

    label("loc_39A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A53")

    #C0152
    ChrTalk(
        0xFE,
        (
            "知ってるかい？\x01",
            "ウルスラ間道の途中には\x01",
            "遺跡があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "中世の頃に作られた塔らしい。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "うーん、ぜひカメラに\x01",
            "収めたいところだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AC3")

    label("loc_3A53")


    #C0155
    ChrTalk(
        0xFE,
        (
            "ウルスラ間道の途中には\x01",
            "中世の頃に作られた塔があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "写真好きとしては\x01",
            "ぜひカメラに収めたい所だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC3")

    Jump("loc_3DC6")

    label("loc_3AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B67")

    #C0157
    ChrTalk(
        0xFE,
        (
            "この前の旧市街の事件、\x01",
            "警察が介入してたんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        "……珍しい話だよね。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "旧市街なんて\x01",
            "パトロールも止めちゃったのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BCD")

    label("loc_3B67")


    #C0160
    ChrTalk(
        0xFE,
        (
            "最近は警察の中にも\x01",
            "珍しい事をする人がいるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "いち市民として\x01",
            "ちょっと興味があるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BCD")

    Jump("loc_3DC6")

    label("loc_3BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8C")

    #C0162
    ChrTalk(
        0xFE,
        (
            "さっきビシッとスーツを着た人が\x01",
            "そこを通って行ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "警察のバッジを\x01",
            "付けていたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "こんなのどかな通りに\x01",
            "警察の人が何の用なのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CF4")

    label("loc_3C8C")


    #C0165
    ChrTalk(
        0xFE,
        (
            "そういえばあの人、\x01",
            "最近見かける気がするなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "警察の人が西通りなんかに\x01",
            "一体何の用だろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CF4")

    Jump("loc_3DC6")

    label("loc_3CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D89")

    #C0167
    ChrTalk(
        0xFE,
        (
            "最近は導力車を\x01",
            "持つ人が増えてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "僕は写真が趣味だから\x01",
            "気軽に郊外に出かけられるのは\x01",
            "魅力だなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DC6")

    label("loc_3D89")


    #C0169
    ChrTalk(
        0xFE,
        (
            "導力車には憧れるなぁ……\x01",
            "もう少し安くなるといいんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC6")

    TalkEnd(0xFE)
    Return()

    # Function_17_3006 end

    def Function_18_3DCA(): pass

    label("Function_18_3DCA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E5E")
    Jump("loc_3EA8")

    label("loc_3E5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EA8")

    label("loc_3E7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E9E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EA8")

    label("loc_3E9E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EA8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3FDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6A")

    #C0170
    ChrTalk(
        0xFE,
        (
            "おっと、もう夕方かぁ……\x01",
            "そろそろ帰らなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "自治州議会も\x01",
            "何とか終わったらしいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        "しばらくは平和になるかな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FDA")

    label("loc_3F6A")


    #C0173
    ChrTalk(
        0xFE,
        "自治州議会もいつも通りだったな。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "まったく、やれやれだよ。\x01",
            "クロスベルって\x01",
            "結局何も変わらないんだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FDA")

    Jump("loc_4C29")

    label("loc_3FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407B")

    #C0175
    ChrTalk(
        0xFE,
        (
            "最近市街で行方不明に\x01",
            "なる人が増えてるんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "マフィアの起こす事件も\x01",
            "続いているし……\x01",
            "どうもおかしな話ばかりだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40D0")

    label("loc_407B")


    #C0177
    ChrTalk(
        0xFE,
        "景気がいいのはいいんだけど……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "最近治安が悪いなぁ。\x01",
            "どうなってるのかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D0")

    Jump("loc_4C29")

    label("loc_40D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_41BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_416B")

    #C0179
    ChrTalk(
        0xFE,
        "クロスベルタイムズ、臨時休刊！？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "そんな……僕の朝食のお供が……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "これじゃ議会の様子も\x01",
            "分からないじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41BA")

    label("loc_416B")


    #C0182
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズが\x01",
            "臨時休刊するなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "一体何があったんだろう。\x02",
    )

    CloseMessageWindow()

    label("loc_41BA")

    Jump("loc_4C29")

    label("loc_41BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_42A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4250")

    #C0184
    ChrTalk(
        0xFE,
        (
            "今、市庁舎で行われてる\x01",
            "予算議会が荒れてるそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "毎年のことだけど、もっとなんとか\x01",
            "ならないものなのかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_429F")

    label("loc_4250")


    #C0186
    ChrTalk(
        0xFE,
        (
            "予算議会はいつも通り荒れてるそうだ。\x01",
            "もっとなんとかならないものなのかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_429F")

    Jump("loc_4C29")

    label("loc_42A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D6")

    #C0187
    ChrTalk(
        0xFE,
        (
            "自治州議会の\x01",
            "予算審議会、ついに始まったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "予算審議会はクロスベルの\x01",
            "年間予算を決めるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "直接ミラの話だからね……\x01",
            "派閥とか利権、議員の見栄も絡んで\x01",
            "議会としても大荒れに荒れるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "今年はどうなるのかなぁ……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "まあ、なるようにしか\x01",
            "ならないんだろうけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4453")

    label("loc_43D6")


    #C0192
    ChrTalk(
        0xFE,
        (
            "予算審議会は毎年\x01",
            "大荒れに荒れるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "ま、要するに議員達の派閥争いだし\x01",
            "市民としちゃ\x01",
            "遠巻きに見守るしかないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4453")

    Jump("loc_4C29")

    label("loc_4458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4501")

    #C0194
    ChrTalk(
        0xFE,
        (
            "マクダエル市長が\x01",
            "今期で引退するって本当なのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "もう１０年以上\x01",
            "市長を務めてきた人だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "良識のある人だから\x01",
            "やめて欲しくないんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C29")

    label("loc_4501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_468E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4605")

    #C0197
    ChrTalk(
        0xFE,
        (
            "エプスタイン財団が進めている\x01",
            "導力ネットワーク計画って、\x01",
            "ＩＢＣが多額の出資をしてるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "ＩＢＣは導力ネットを使って\x01",
            "大陸中の支店を接続する\x01",
            "プロジェクトを進めてるそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "さすがＩＢＣ……\x01",
            "事業の規模が桁外れだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4689")

    label("loc_4605")


    #C0200
    ChrTalk(
        0xFE,
        (
            "導力ネットワーク計画には\x01",
            "莫大なミラが掛かってるそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "将来を見据えてそこまでするなんて\x01",
            "さすがＩＢＣは格が違うな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4689")

    Jump("loc_4C29")

    label("loc_468E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_47A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4724")

    #C0202
    ChrTalk(
        0xFE,
        (
            "そういえば最近\x01",
            "クロスベルタイムズの\x01",
            "女記者さんを見ないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "あの人、ときどき取材で\x01",
            "この辺りにも来てたんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_479C")

    label("loc_4724")


    #C0204
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズの女記者さんは\x01",
            "時々この辺りにも来てたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "警察の人を尾行しては\x01",
            "ネタを掴んでたみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_479C")

    Jump("loc_4C29")

    label("loc_47A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4858")

    #C0206
    ChrTalk(
        0xFE,
        (
            "毎年記念祭が近くなると\x01",
            "街が華やいでくるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "それに……知ってるかい？\x01",
            "今年は自治州創立７０周年に当たるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "きっと例年より\x01",
            "大規模なお祭りになるはずさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C29")

    label("loc_4858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_48F6")

    #C0209
    ChrTalk(
        0xFE,
        (
            "なんだか警備隊が\x01",
            "出動してるって聞いたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "国境の方で何かあったのかな。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "その割にはニュースに\x01",
            "なってない気がするけどなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C29")

    label("loc_48F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4966")

    #C0212
    ChrTalk(
        0xFE,
        (
            "ふう、ここの\x01",
            "クロワッサンは絶品だな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "エスプレッソと一緒に頂くと\x01",
            "もうたまんないよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C29")

    label("loc_4966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A02")

    #C0214
    ChrTalk(
        0xFE,
        (
            "そういや、遊撃士協会に\x01",
            "新しい人が着任したんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "どんな人なんだろ。\x01",
            "遊撃士ってみんな凄い人たち\x01",
            "だから興味あるよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A44")

    label("loc_4A02")


    #C0216
    ChrTalk(
        0xFE,
        (
            "新しくクロスベルに\x01",
            "着任した遊撃士……\x01",
            "どんな人なんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A44")

    Jump("loc_4C29")

    label("loc_4A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4AD8")

    #C0217
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズには\x01",
            "腕利きの女性記者がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "時々スクープなんかを\x01",
            "すっぱ抜いてさ、\x01",
            "ちょっとした有名人なんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C29")

    label("loc_4AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA2")

    #C0219
    ChrTalk(
        0xFE,
        "遊撃士協会、またお手柄……か。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "子供を助け出すなんて\x01",
            "さすがは遊撃士だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "でも……市のずさんな\x01",
            "管理体制は許せないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "ちゃんと対策を\x01",
            "とって欲しいもんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C29")

    label("loc_4BA2")


    #C0223
    ChrTalk(
        0xFE,
        (
            "クロスベル市って\x01",
            "何かと事件や事故が多いよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "大抵は遊撃士の人が\x01",
            "何とかしてくれるけど……\x01",
            "市も少しは反省して欲しいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C29")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_3DCA end

    def Function_19_4C31(): pass

    label("Function_19_4C31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E01")

    #C0225
    ChrTalk(
        0x101,
        (
            "#0000Fちょっといいかな。\x02\x03",

            "君は猫を\x01",
            "飼ってたりしない？\x01",
            "小さい仔猫なんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0226
    ChrTalk(
        0xFE,
        "しらないけど……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "仔猫、くれるの？\x01",
            "……飼いたいかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "あ、でもおうち\x01",
            "お商売やってるし、\x01",
            "ダメかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#0006Fゴメン……\x01",
            "仔猫を飼い主の所に\x01",
            "連れて行ってあげる所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        "そっか……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "うん、それがいいよね。\x01",
            "そうしてあげて……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        "#0100Fここのお宅は空振りみたいね。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x4)
    Jump("loc_4E9D")

    label("loc_4E01")


    #C0233
    ChrTalk(
        0xFE,
        "仔猫のことはしらないけど……\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "そういえばリュウ君たちが\x01",
            "猫をひろったって言ってたかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "いいなぁ、リュウ君たち。\x01",
            "モモもお世話してみたいな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E9D")

    Jump("loc_523E")

    label("loc_4EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4EB0")
    Jump("loc_523E")

    label("loc_4EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F4A")
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0236
    ChrTalk(
        0xFE,
        "わーん……！\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "リュウ君、走るのはやいぃ～！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#0012F目をつぶったまま\x01",
            "走っちゃ危ないぞ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F7B")

    label("loc_4F4A")


    #C0239
    ChrTalk(
        0xFE,
        (
            "リュウ君、コワイ～！\x01",
            "走るのはやいぃ～……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F7B")

    Jump("loc_523E")

    label("loc_4F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4F91")
    Call(0, 15)
    Jump("loc_523E")

    label("loc_4F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4FFC")

    #C0240
    ChrTalk(
        0xFE,
        (
            "リュウ君がね、\x01",
            "一緒に遊んでもいいって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0241
    ChrTalk(
        0xFE,
        "や、やったぁ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_523E")

    label("loc_4FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_500A")
    Jump("loc_523E")

    label("loc_500A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5018")
    Jump("loc_523E")

    label("loc_5018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5026")
    Jump("loc_523E")

    label("loc_5026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5034")
    Jump("loc_523E")

    label("loc_5034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5042")
    Jump("loc_523E")

    label("loc_5042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5050")
    Jump("loc_523E")

    label("loc_5050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_50B6")

    #C0242
    ChrTalk(
        0xFE,
        (
            "リュウ君とアンリちゃん、\x01",
            "今日も元気だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "モモも一緒に\x01",
            "遊んじゃダメかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_523E")

    label("loc_50B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_514D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5124")

    #C0244
    ChrTalk(
        0xFE,
        (
            "リュウ君とアンリちゃん、\x01",
            "さいきん遊びにきてないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "なにしてるのかな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5148")

    label("loc_5124")


    #C0246
    ChrTalk(
        0xFE,
        "モモも仔猫、飼いたかったな……\x02",
    )

    CloseMessageWindow()

    label("loc_5148")

    Jump("loc_523E")

    label("loc_514D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5227")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F7")

    #C0247
    ChrTalk(
        0xFE,
        (
            "リュウ君とアンリちゃん、\x01",
            "さいきん見かけないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "なにかヒミツのこと\x01",
            "してるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "いいなぁ……モモも\x01",
            "仲間にいれてほしいな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5222")

    label("loc_51F7")


    #C0250
    ChrTalk(
        0xFE,
        (
            "くすん、モモには\x01",
            "教えてくれないの……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5222")

    Jump("loc_523E")

    label("loc_5227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5235")
    Jump("loc_523E")

    label("loc_5235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_523E")

    label("loc_523E")

    TalkEnd(0xFE)
    Return()

    # Function_19_4C31 end

    def Function_20_5242(): pass

    label("Function_20_5242")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5331")

    #C0251
    ChrTalk(
        0xFE,
        (
            "私の焼いた最高傑作を\x01",
            "オスカーに食べさせたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "嬉しそうに\x01",
            "『はは、これ美味いじゃんか！』\x01",
            "……とか言うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "うう……\x01",
            "ライバルのパンを\x01",
            "褒めるわけないわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        "オスカーめ……騙されないぞ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5329")
    SetScenarioFlags(0xED, 1)

    label("loc_5329")

    SetScenarioFlags(0x0, 7)
    Jump("loc_53DD")

    label("loc_5331")


    #C0255
    ChrTalk(
        0xFE,
        (
            "本当においしいって\x01",
            "思ってたらもっと驚くはず……\x01",
            "うん、そうに違いないもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "くそっくそっ、オスカーめ……！\x01",
            "もっともっと修行して\x01",
            "絶対ぎゃふんと言わせてやるっ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53DD")

    TalkEnd(0xFE)
    Return()

    # Function_20_5242 end

    def Function_21_53E1(): pass

    label("Function_21_53E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5463")

    #C0257
    ChrTalk(
        0xFE,
        (
            "ついに導力車を\x01",
            "購入してみたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "ほほほ、明日は\x01",
            "初ドライブと洒落込むか。\x01",
            "実に楽しみじゃのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54B9")

    label("loc_5463")


    #C0259
    ChrTalk(
        0xFE,
        (
            "ついに導力車を\x01",
            "購入してみたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "ほほほ、老後は目一杯\x01",
            "楽しまんとのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B9")

    TalkEnd(0xFE)
    Return()

    # Function_21_53E1 end

    def Function_22_54BD(): pass

    label("Function_22_54BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_55E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5589")

    #C0261
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー。\x01",
            "タリーズ商店へようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "あら可愛らしい子ね。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "うちのモモとも\x01",
            "仲良くしてあげてね～？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x153,
        "#1110Fうん、わかった～！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#0000Fははは……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_55E0")

    label("loc_5589")


    #C0266
    ChrTalk(
        0xFE,
        (
            "うちのモモは\x01",
            "ちょーっと引っ込み思案なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        "仲良くしてくれると嬉しいわ～。\x02",
    )

    CloseMessageWindow()

    label("loc_55E0")

    Jump("loc_5811")

    label("loc_55E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_55F3")
    Jump("loc_5811")

    label("loc_55F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_573D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_56A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5672")

    #C0268
    ChrTalk(
        0xFE,
        (
            "ピート君が来てるわ。\x01",
            "先生の食事を作るんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        "ほんとにしっかりしてるわねえ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_569D")

    label("loc_5672")


    #C0270
    ChrTalk(
        0xFE,
        (
            "うちのモモも\x01",
            "少しは見習って欲しいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_569D")

    Jump("loc_5738")

    label("loc_56A2")


    #C0271
    ChrTalk(
        0xFE,
        (
            "旧市街の方じゃ、不良グループ同士が\x01",
            "しょっちゅう喧嘩してるんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "噂に聞くだけだけど、怖いわね～。\x01",
            "ウチのモモには近づいて欲しくないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5738")

    Jump("loc_5811")

    label("loc_573D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5811")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D0")

    #C0273
    ChrTalk(
        0xFE,
        (
            "あらおはよう、\x01",
            "《タリーズ商店》へようこそ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "お陰さまでウチも創業１０周年なの。\x01",
            "いつもお世話になってまーす。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5811")

    label("loc_57D0")


    #C0275
    ChrTalk(
        0xFE,
        (
            "ウチもついに創業１０周年なの。\x01",
            "これも近所の皆さんのお陰ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5811")

    TalkEnd(0xFE)
    Return()

    # Function_22_54BD end

    def Function_23_5815(): pass

    label("Function_23_5815")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_592A")

    #C0276
    ChrTalk(
        0x10,
        "#1200Fグルルルル…………\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#0000Fティオ、なんて言ってるんだ？\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x103,
        (
            "#0200F『心地よい日差しだ』\x01",
            "……と言っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        (
            "#0300Fなんだよ……\x01",
            "てっきりガキに纏わりつかれて\x01",
            "機嫌が悪いのかと思ったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#0100Fふふ、ツァイトなりに\x01",
            "寛いでいるみたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 3)
    Jump("loc_5948")

    label("loc_592A")


    #C0281
    ChrTalk(
        0x10,
        "#1200Fグルルルル…………\x02",
    )

    CloseMessageWindow()

    label("loc_5948")

    TalkEnd(0xFE)
    Return()

    # Function_23_5815 end

    def Function_24_594C(): pass

    label("Function_24_594C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    OP_4B(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    OP_68(16500, 6000, 15500, 0)
    MoveCamera(66, 2, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 10500, 3000, 14800, 90)
    SetChrPos(0x102, 10500, 3000, 16200, 90)
    SetChrPos(0x103, 9300, 3000, 14800, 90)
    SetChrPos(0x104, 9300, 3000, 16200, 90)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 21000, 3000, 15500, 270)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    OP_68(14500, 6000, 15500, 6000)
    MoveCamera(56, 2, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(500)

    #C0282
    ChrTalk(
        0x102,
        (
            "#0100Fグリムウッド法律事務所……\x02\x03",

            "うん、ここがそうみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ、その先生のことも\x01",
            "何度か見かけたことがあるよ。\x02\x03",

            "そんな偉い先生だなんて\x01",
            "思ってもみなかったけど……\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    Sleep(300)

    #N0284
    NpcTalk(
        0x11,
        "男の声",
        (
            "#1P#2S……それでは先生。\x01",
            "今後とも宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #N0285
    NpcTalk(
        0x11,
        "男性の声",
        (
            "#11P#2Sああ、それはいいが……\x02\x03",

            "#2Sしかし君たちのところは\x01",
            "もう少し何とかならんのかね？\x02\x03",

            "#2S少しは市民の\x01",
            "気持ちというものをだね……\x02",
        )
    )

    CloseMessageWindow()

    #N0286
    NpcTalk(
        0x11,
        "男の声",
        (
            "#1P#2S……市民の人気取りが\x01",
            "仕事ではありませんので。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1553, 255, 90, 0)    #voice#Dudley
    Sleep(1000)
    Fade(500)
    OP_68(13070, 3700, 15860, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23790, 0)
    OP_0D()

    def lambda_5D1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5D1E)

    def lambda_5D2F():
        OP_95(0xFE, 14000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5D2F)
    WaitChrThread(0x11, 2)
    Sleep(800)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x11, 1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    #Sound(1554, 255, 100, 0)    #voice#Dudley
    SetChrName("眼鏡の男性")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            "お前たちは……\x02\x03",

            "………………………………………\x02",
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

    #C0288
    ChrTalk(
        0x101,
        "#6P#0005Fな、何か……？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1555, 255, 100, 0)    #voice#Dudley
    Sleep(500)

    #N0289
    NpcTalk(
        0x11,
        "眼鏡の男性",
        (
            "#0604F#11P……なるほどな。\x02\x03",

            "#0602Fセルゲイさんが飼い始めた\x01",
            "仔犬どもというわけか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0290
    ChrTalk(
        0x101,
        "#6P#0011Fえっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x101,
        (
            "#6P#0001Fそのバッジ……\x01",
            "あなたもクロスベル警察の？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1556, 255, 100, 0)    #voice#Dudley
    Sleep(500)

    #N0292
    NpcTalk(
        0x11,
        "眼鏡の男性",
        (
            "#0603F#11P私のことはどうでもいい。\x02\x03",

            "#0601Fどうやらイアン先生を\x01",
            "訪ねてきたようだが……\x02\x03",

            "くれぐれも余計な時間を\x01",
            "取らせるんじゃないぞ。\x02\x03",

            "お前たちのような役立たずと違って\x01",
            "色々と忙しい人だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        "#6P#0013Fなっ……！？\x02",
    )

    CloseMessageWindow()

    def lambda_607D():

        label("loc_607D")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_607D")

    QueueWorkItem2(0x101, 2, lambda_607D)

    def lambda_608F():

        label("loc_608F")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_608F")

    QueueWorkItem2(0x102, 2, lambda_608F)

    def lambda_60A1():

        label("loc_60A1")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_60A1")

    QueueWorkItem2(0x103, 2, lambda_60A1)

    def lambda_60B3():

        label("loc_60B3")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_60B3")

    QueueWorkItem2(0x104, 2, lambda_60B3)

    def lambda_60C5():
        OP_95(0xFE, 2100, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_60C5)
    Sleep(600)
    OP_68(11850, 3700, 16440, 3000)

    def lambda_60F3():
        OP_96(0xFE, 0x2904, 0xBB8, 0x3840, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60F3)
    Sleep(400)

    def lambda_6110():
        OP_96(0xFE, 0x2454, 0xBB8, 0x3840, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6110)
    Sleep(2500)

    def lambda_612D():
        OP_96(0xFE, 0x2904, 0xBB8, 0x39D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_612D)
    Sleep(400)

    def lambda_614A():
        OP_96(0xFE, 0x2454, 0xBB8, 0x39D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_614A)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    ClearChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0294
    ChrTalk(
        0x101,
        "#11P#0007Fな、なんだ今のは！？\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        (
            "#11P#0101Fどうやら本部の\x01",
            "捜査官みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        "#12P#0211F……居丈高な感じですね。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x104,
        (
            "#0303F#5Pしかしあの眼鏡……\x01",
            "随分とやるみたいだったぞ。\x02\x03",

            "#0301F左脇のところに\x01",
            "デカイ得物を吊るしてたな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    #C0298
    ChrTalk(
        0x101,
        "#11P#0005Fそ、そうなのか？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        "#11P#0105Fよく気付いたわね……\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        (
            "#12P#0203Fわたしも\x01",
            "センサーで感知しました。\x02\x03",

            "#0200F大型の軍用拳銃……\x01",
            "そんな所でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x104,
        "#0300F#5Pああ、多分そうだろ。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        "#11P#0000Fは～……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        "#11P#0100F２人とも凄いわね……\x02",
    )

    CloseMessageWindow()

    def lambda_640F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_640F)
    Sleep(50)

    def lambda_641F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_641F)
    Sleep(300)

    #C0304
    ChrTalk(
        0x104,
        "#0304F#6Pハハ、たまたまさ。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#6P#0200Fそれより、その先生を\x01",
            "訪ねなくてもいいんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0306
    ChrTalk(
        0x101,
        "#11P#0005Fああ……\x02",
    )

    CloseMessageWindow()

    def lambda_64AD():
        OP_93(0xFE, 0x59, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_64AD)
    Sleep(100)

    def lambda_64BD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_64BD)
    Sleep(500)

    #C0307
    ChrTalk(
        0x101,
        (
            "#6P#0001F忙しいところを悪いけど\x01",
            "挨拶させてもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x0, 10200, 3000, 15500, 90)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x42, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_594C end

    def Function_25_653D(): pass

    label("Function_25_653D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17100, 4000, 15500, 0)
    MoveCamera(57, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_4B(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x101, 20500, 3000, 15500, 270)
    SetChrPos(0x102, 20500, 3000, 15500, 270)
    SetChrPos(0x103, 20500, 3000, 15500, 270)
    SetChrPos(0x104, 20500, 3000, 15500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6634")
    LoadChrToIndex("chr/ch07000.itc", 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 8000, 3300, 21000, 180)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_6634")

    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    OP_68(11900, 4000, 15500, 5500)
    MoveCamera(45, 27, 0, 5500)
    SetCameraDistance(20500, 5500)

    def lambda_667F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_667F)

    def lambda_6690():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6690)
    Sleep(700)

    def lambda_66AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_66AD)

    def lambda_66BE():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66BE)
    Sleep(700)

    def lambda_66DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_66DB)

    def lambda_66EC():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_66EC)
    Sleep(700)

    def lambda_6709():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6709)

    def lambda_671A():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_671A)
    WaitChrThread(0x101, 1)

    def lambda_6738():
        OP_95(0xFE, 11200, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6738)
    WaitChrThread(0x102, 1)

    def lambda_6756():
        OP_95(0xFE, 11200, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6756)
    WaitChrThread(0x103, 1)

    def lambda_6774():
        OP_95(0xFE, 12600, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6774)
    WaitChrThread(0x104, 1)

    def lambda_6792():
        OP_95(0xFE, 12600, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6792)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)

    def lambda_67C2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67C2)
    WaitChrThread(0x102, 1)

    def lambda_67D3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_67D3)
    WaitChrThread(0x103, 1)

    def lambda_67E4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_67E4)
    WaitChrThread(0x104, 1)

    def lambda_67F5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_67F5)
    WaitChrThread(0x104, 2)
    OP_79(0x3)
    OP_6F(0x79)

    #C0308
    ChrTalk(
        0x102,
        (
            "#0100Fそれで、どうするの？\x02\x03",

            "考えをまとめるんだったら\x01",
            "支援課に戻りましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x101,
        (
            "#6P#0008Fそうだな……\x02\x03",

            "#0003Fその前に、他に片付けたい\x01",
            "用事があるなら済ませておこう。\x02\x03",

            "#0001F俺が考えていることが\x01",
            "事件の真相だったとしたら……\x01",
            "かなり面倒な事になるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#5P#0309Fへへッ、何だかんだ言って\x01",
            "自信があるみたいじゃねえか。\x02\x03",

            "#0300Fそういう事なら、\x01",
            "とっとと他の用事を済ませて\x01",
            "支援課に戻るとするかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        (
            "#0202F……はい。\x01",
            "急いで片付けましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75EE")
    OP_68(11050, 4000, 15990, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(20500, 3000)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(500)

    def lambda_6A1E():
        OP_95(0xFE, 8000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6A1E)

    def lambda_6A38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_6A38)
    Sleep(1000)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x2)
    Sleep(500)
    WaitChrThread(0x19, 1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_6A7A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6A7A)
    Sleep(1000)

    #N0312
    NpcTalk(
        0x19,
        "青年",
        (
            "あれ……？\x01",
            "……ロイドじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6AB6():
        OP_95(0xFE, 9500, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6AB6)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_6B18():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B18)
    Sleep(60)

    def lambda_6B28():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B28)
    Sleep(60)

    def lambda_6B38():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B38)
    Sleep(60)

    def lambda_6B48():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B48)
    Sleep(60)
    WaitChrThread(0x19, 1)

    #C0313
    ChrTalk(
        0x101,
        "#0005F#11Pオスカー……！？\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x19,
        (
            "わはは、久し振りだな！\x01",
            "お前いつの間に戻ってやがったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x19,
        (
            "この３年、一度も顔を見せねえから\x01",
            "心配してたんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#0004F#11Pははは……悪い。\x01",
            "早く挨拶に行こうとは\x01",
            "思ってたんたけど……\x02\x03",

            "#0002Fちょっと仕事の方が\x01",
            "立て込んでてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x19,
        (
            "そっか、今も仕事中みてえだな……\x01",
            "ええと……同僚と捜査中ってトコか？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#0005F#11Pえ、ああ、そうだけど。\x02\x03",

            "#0006F……何でそこまで分かるんだよ。\x01",
            "相変わらずお前って\x01",
            "鋭いんだか大ざっぱなんだか……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x19,
        (
            "わはは、ちょいと深刻そうだったから\x01",
            "何となくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x19,
        (
            "……そうだロイド。\x01",
            "そんならこいつだけ持っていけよ。\x01",
            "再会の印ってやつだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6DB3():
        OP_98(0xFE, 0x1F4, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6DB3)
    WaitChrThread(0x19, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0321
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    AddItemNumber(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F62")
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0322
    AnonymousTalk(
        0xFF,
        (
            "手帳には",
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピが書かれていた。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xD)

    def lambda_6E81():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6E81)
    WaitChrThread(0x19, 1)

    #C0324
    ChrTalk(
        0x19,
        "ロイド、結構料理は得意だったろ？\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x19,
        (
            "こいつはレシピのバリエーションまで\x01",
            "記録できるし、複数の人間で使えるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x19,
        (
            "サンドイッチのレシピだけ\x01",
            "書き込んでおいたからよ。\x01",
            "良けりゃ活用してくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7008")

    label("loc_6F62")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_6F7A():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6F7A)
    WaitChrThread(0x19, 1)

    #C0327
    ChrTalk(
        0x19,
        "ロイド、結構料理は得意だったろ？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x19,
        (
            "こいつはレシピのバリエーションまで\x01",
            "記録できるし、複数の人間で使えるんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7008")


    #C0329
    ChrTalk(
        0x101,
        (
            "#0002F#11Pへえ、中々便利そうだな……\x02\x03",

            "#0009Fサンキュー、オスカー。\x01",
            "ありがたく使わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x19,
        "おう、んじゃあな。\x02",
    )

    CloseMessageWindow()

    def lambda_708A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_708A)
    WaitChrThread(0x19, 1)
    Sleep(300)

    #C0331
    ChrTalk(
        0x19,
        (
            "俺はそこのモルジュって\x01",
            "パン屋に勤め始めたんだ。\x01",
            "またヒマなときに寄ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        (
            "#0004F#11Pパン屋か……そういや手紙に\x01",
            "そんな事書いてたよな。\x02\x03",

            "#0000F分かった、今度立ち寄るよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7155():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7155)
    WaitChrThread(0x19, 1)

    #C0333
    ChrTalk(
        0x19,
        "はは、あんま無理すんなよ？\x02",
    )

    CloseMessageWindow()

    def lambda_7186():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7186)
    WaitChrThread(0x19, 1)

    def lambda_7197():
        OP_95(0xFE, 1000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_7197)
    Sleep(3000)

    #C0334
    ChrTalk(
        0x103,
        (
            "#0202F#11Pロイドさんの\x01",
            "お知り合いみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        (
            "#0004F#11Pああ、オスカーっていって\x01",
            "幼馴染なんだ。\x02\x03",

            "#0002Fずっと手紙でやり取りしてたけど\x01",
            "ぜんぜん変わってないな、あいつ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7269():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7269)
    WaitChrThread(0x102, 1)

    #C0336
    ChrTalk(
        0x102,
        (
            "#0100Fロイド……よかったら\x01",
            "もうちょっと話してきたら？\x02\x03",

            "会うのは久しぶりなんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_72D5():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72D5)
    WaitChrThread(0x101, 1)

    #C0337
    ChrTalk(
        0x101,
        (
            "#0006Fいや、イアン先生から聞いた話も\x01",
            "早く考えてみたいし……\x02\x03",

            "#0000Fまあ、まだ街を回るんだったら\x01",
            "そこのパン屋にも寄ってみようか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_736C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_736C)
    WaitChrThread(0x104, 1)

    #C0338
    ChrTalk(
        0x104,
        (
            "#0304F#5Pああ、それでいいんじゃね？\x02\x03",

            "#0302F一通り用事を済ませたら\x01",
            "さくっと支援課に戻るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    OP_49()
    OP_D5(0x1E)
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※人々に話しかけたり、特定の場所を調べると、\x01",
            "  料理の『レシピ』を覚えることがあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※『レシピ』は『料理手帳』に記録されていきます。\x01",
            "  『料理手帳』を使えば、いつでも\x01",
            "  様々な効力のある料理を作ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※また、『大成功』料理や、『予想外』料理など、\x01",
            "  一定の確率で完成する料理が変化します。\x01",
            "  （料理に『失敗』してしまうこともあります。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※料理に使う『食材』は\x01",
            "  雑貨屋などの商店で販売されています。\x01",
            "  また、魔獣が落とす場合もあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 1)
    SetScenarioFlags(0x4A, 7)

    label("loc_75EE")

    SetChrPos(0x0, 11500, 3000, 15500, 270)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x43, 0)
    OP_29(0x3E, 0x1, 0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7630")
    OP_1B(0x0, 0x0, 0x1E)
    OP_1B(0x1, 0x0, 0x1F)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_7630")

    EventEnd(0x5)
    Return()

    # Function_25_653D end

    def Function_26_7633(): pass

    label("Function_26_7633")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("chr/ch05900.itc", 0x1F)
    LoadChrToIndex("chr/ch07000.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch25000.itc", 0x23)
    OP_68(6600, 1400, -11300, 0)
    MoveCamera(27, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 11700, 0, -9200, 270)
    SetChrPos(0x102, 11900, 0, -10200, 270)
    SetChrPos(0x103, 13300, 0, -10200, 270)
    SetChrPos(0x104, 13100, 0, -9200, 270)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 8200, 0, -9400, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 6800, 0, -9900, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6600, 0, -8800, 125)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 10510, 0, -7890, 243)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 8940, 0, -4080, 210)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 7260, 0, -5600, 157)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 8900, 0, -6230, 217)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 4310, 0, -7050, 127)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12470, 0, -6780, 240)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 5760, 0, -4940, 178)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0x13)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x13, 1500, 0, -13500, 0)
    OP_D3(0x13, 0x0, 0x29810, 0x4E20, 0x0)
    OP_70(0xC, 0x0)
    SetMapObjFrame(0xFF, "br02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "br00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "br01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "br_mul", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "◆未入力。\x01",
            "西通りのセピアの回想シーン。\x01",
            "事故にあった子供をツァイトが助ける。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    SetScenarioFlags(0x5C, 7)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_7633 end

    def Function_27_795F(): pass

    label("Function_27_795F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17100, 4000, 15500, 0)
    MoveCamera(57, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 20500, 3000, 15500, 270)
    SetChrPos(0x102, 20500, 3000, 15500, 270)
    SetChrPos(0x103, 20500, 3000, 15500, 270)
    SetChrPos(0x104, 20500, 3000, 15500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    OP_68(11900, 4000, 15500, 5500)
    MoveCamera(45, 27, 0, 5500)
    SetCameraDistance(20500, 5500)

    def lambda_7A58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A58)

    def lambda_7A69():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A69)
    Sleep(700)

    def lambda_7A86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7A86)

    def lambda_7A97():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A97)
    Sleep(700)

    def lambda_7AB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7AB4)

    def lambda_7AC5():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7AC5)
    Sleep(700)

    def lambda_7AE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7AE2)

    def lambda_7AF3():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7AF3)
    WaitChrThread(0x101, 1)

    def lambda_7B11():
        OP_95(0xFE, 11200, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B11)
    WaitChrThread(0x102, 1)

    def lambda_7B2F():
        OP_95(0xFE, 11200, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B2F)
    WaitChrThread(0x103, 1)

    def lambda_7B4D():
        OP_95(0xFE, 12600, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7B4D)
    WaitChrThread(0x104, 1)

    def lambda_7B6B():
        OP_95(0xFE, 12600, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7B6B)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)

    def lambda_7B9B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B9B)
    WaitChrThread(0x102, 1)

    def lambda_7BAC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7BAC)
    WaitChrThread(0x103, 1)

    def lambda_7BBD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7BBD)
    WaitChrThread(0x104, 1)

    def lambda_7BCE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7BCE)
    WaitChrThread(0x104, 2)
    OP_79(0x3)
    OP_6F(0x79)

    #C0344
    ChrTalk(
        0x101,
        (
            "#6P#0003Fさてと……\x01",
            "《黒月貿易公司》に行こうか。\x02\x03",

            "#0000F確か、港湾区にあるはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x103,
        (
            "#0203F……場所的には\x01",
            "港湾区の北東の外れですね。\x02\x03",

            "#0200F川辺に面しているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x104,
        (
            "#5P#0300Fああ、あの赤っぽい\x01",
            "東方風の建物だよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        (
            "#0106Fあの周辺はＩＢＣや\x01",
            "クロスベルタイムズがあるくらい、\x01",
            "まともな場所のはずだけど……\x02\x03",

            "#0101Fまあいいわ。\x01",
            "とにかく行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 11500, 3000, 15500, 270)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x81, 1)
    OP_29(0x42, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_27_795F end

    def Function_28_7D7D(): pass

    label("Function_28_7D7D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(8000, 5000, 15590, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15560, 0)
    OP_68(16710, 5000, 15520, 4000)
    MoveCamera(70, 18, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(18910, 4000)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-14910, 2400, -11820, 0)
    MoveCamera(29, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7830, 0)
    OP_68(-9970, 3700, 9790, 5000)
    MoveCamera(23, 15, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(16270, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(10660, 3700, 2040, 0)
    MoveCamera(59, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18420, 0)
    OP_68(6220, 1660, 5470, 5000)
    MoveCamera(45, 37, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(44100, 5000)
    PlaceName2(340, 200, "c_plac03", 0x0, 1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80FD")

    #A0348
    AnonymousTalk(
        0x103,
        (
            "#0205Fここは……\x01",
            "クロスベル市の西通りですね。\x02",
        )
    )

    CloseMessageWindow()

    #A0349
    AnonymousTalk(
        0x101,
        (
            "#0004Fああ、アパルトメントが多くて\x01",
            "ベッドタウンみたいな感じだよ。\x02\x03",

            "#0000F知り合いが何人かいて……\x01",
            "ちょっと挨拶しときたいんだけど\x01",
            "いいかな？\x02",
        )
    )

    CloseMessageWindow()

    #A0350
    AnonymousTalk(
        0x104,
        (
            "#0300Fそっか、お前ってここの出身なワケだ。\x02\x03",

            "#0304Fま、いいんじゃねえか？\x01",
            "のんびり行こうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #A0351
    AnonymousTalk(
        0x102,
        (
            "#0102Fそうね、久しぶりでしょうし\x01",
            "私たちも付き合わせてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    #A0352
    AnonymousTalk(
        0x101,
        (
            "#0002Fサンキュー、助かるよ。\x02\x03",

            "#0004F（ベルハイムにいるおばさんたちと\x01",
            "  ……あとはオスカーだな。\x01",
            "  パン屋に勤めてるはずだけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_80FD")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西通りは、街の西側にあるベッドタウンです。\x02",
        )
    )

    CloseMessageWindow()

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "住宅やアパートが建ち並び、\x01",
            "所々にカフェや雑貨屋などが点在しています。\x02",
        )
    )

    CloseMessageWindow()

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "主人公の１人、ロイドが\x01",
            "生まれ育った街区でもあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_END)), "loc_82CC")
    FadeToBright(300, 0)
    OP_0D()

    #A0356
    AnonymousTalk(
        0x101,
        (
            "#0005F（そういえば……\x01",
            "  まだおばさん達やオスカーには\x01",
            "  挨拶してなかったな。）\x02\x03",

            "#0008F（おばさんはベルハイムにいるだろうし、\x01",
            "  オスカーはパン屋に勤めてるはずだ……）\x02\x03",

            "#0000F（時間があれば立ち寄ってみようかな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_82CC")

    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8334")
    OP_68(110, 5000, 22760, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)

    label("loc_8334")

    SetScenarioFlags(0x44, 6)
    EventEnd(0x5)
    Return()

    # Function_28_7D7D end

    def Function_29_833A(): pass

    label("Function_29_833A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83CE")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0357
    ChrTalk(
        0x101,
        (
            "#0000Fおっと……\x02\x03",

            "仔猫をつれたままだしな。\x01",
            "遠くへ行くのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_83CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8488")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8447")

    #C0358
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街の西口だな。\x02\x03",

            "今は外に出る必要はない……\x01",
            "市内の仕事に専念しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8472")

    label("loc_8447")

    SetChrName("")

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街の外に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8472")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_8488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8551")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8512")

    #C0360
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街の西口だな。\x01",
            "西クロスベル街道があるけど……\x02\x03",

            "今回の調査では\x01",
            "寄る必要は無さそうだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_853B")

    label("loc_8512")

    SetChrName("")

    #A0361
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街道に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_853B")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_8551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8616")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85D7")

    #C0362
    ChrTalk(
        0x101,
        (
            "#0000Fっと、こっちは西口だ。\x02\x03",

            "キーアを危険な目に\x01",
            "遭わせたくないし、\x01",
            "外に出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8600")

    label("loc_85D7")

    SetChrName("")

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街道に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8600")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_8616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86D0")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8691")

    #C0364
    ChrTalk(
        0x101,
        (
            "#0003Fこっちは街の西口だな。\x02\x03",

            "黒月のこともある……\x01",
            "……今は市内の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_86BA")

    label("loc_8691")

    SetChrName("")

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今は市内の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_86BA")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_86D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8779")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_872E")

    #C0366
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街の西口だな。\x01",
            "……今はウルスラ病院に急ごう！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8763")

    label("loc_872E")

    SetChrName("")

    #A0367
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西クロスベル街道に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8763")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_8779")

    Return()

    # Function_29_833A end

    def Function_30_877A(): pass

    label("Function_30_877A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_880E")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0368
    ChrTalk(
        0x101,
        (
            "#0000Fおっと……\x02\x03",

            "仔猫をつれたままだしな。\x01",
            "遠くへ行くのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 24460, 0, -8180, 270)
    EventEnd(0x4)
    Return()

    label("loc_880E")

    EventBegin(0x1)
    Call(0, 33)
    Sleep(50)
    SetChrPos(0x0, 24460, 0, -8180, 270)
    EventEnd(0x4)
    Return()

    # Function_30_877A end

    def Function_31_882A(): pass

    label("Function_31_882A")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 33)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)
    Return()

    # Function_31_882A end

    def Function_32_8846(): pass

    label("Function_32_8846")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 33)
    SetChrPos(0x0, 36500, -4000, -19000, 270)
    EventEnd(0x4)
    Return()

    # Function_32_8846 end

    def Function_33_8862(): pass

    label("Function_33_8862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89F7")

    #C0369
    ChrTalk(
        0x101,
        "#0000Fっと、そうだ……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        "#0300Fん、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#0000Fいや、実は西通りにオスカーって\x01",
            "幼馴染が居てさ、\x01",
            "一度顔を出すって約束してたんだ。\x02\x03",

            "ついでだし\x01",
            "寄って来てもいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#0100Fええ、そのくらいなら\x01",
            "いいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x103,
        "#0200Fこの近くなんですか？\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x101,
        (
            "#0000Fああ、モルジュっていう\x01",
            "パン屋に勤めてるはずなんだ。\x02\x03",

            "大通りに面してるって\x01",
            "言ってたけど……\x01",
            "どの辺りなのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8A56")

    label("loc_89F7")


    #C0375
    ChrTalk(
        0x101,
        (
            "#0000Fモルジュっていうパン屋に\x01",
            "幼馴染が勤めてるはずなんだ。\x02\x03",

            "ついでだし立ち寄ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A56")

    Return()

    # Function_33_8862 end

    SaveToFile()

Try(main)
