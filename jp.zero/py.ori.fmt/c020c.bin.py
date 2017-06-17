from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c020c.bin",                # FileName
        "c020c",                    # MapName
        "c020c",                    # Location
        0x000A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 2, 0, 3],
    )

    BuildStringList((
        "c020c",                  # 0
        "ポンス",                 # 1
        "ブリック",               # 2
        "ベネット",               # 3
        "エルサ",                 # 4
        "モモ",                   # 5
        "ルーヴィック老人",       # 6
        "オリガ夫人",             # 7
        "カテリーナ",             # 8
        "チルル",                 # 9
        "見物客",                 # 10
        "見物客",                 # 11
        "見物客",                 # 12
        "見物客",                 # 13
        "見物客",                 # 14
        "レイズ老人",             # 15
        "コリン",                 # 16
        "ハロルド",               # 17
        "ソフィア",               # 18
        "シュリ",                 # 19
        "SE制御",                 # 20
        "中央広場",               # 21
        "西通り",                 # 22
        "行政区",                 # 23
        "住宅街",                 # 24
        "歓楽街",                 # 25
        "東通り",                 # 26
        "旧市街",                 # 27
        "港湾区",                 # 28
        "ＩＢＣ",                 # 29
        "駅前通り",               # 30
        "裏通り",                 # 31
        "ウルスラ間道",           # 32
        "東クロスベル街道",       # 33
        "西クロスベル街道",       # 34
        "マインツ山道",           # 35
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch20402.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch10400.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch21600.itc",                   # 05
        "chr/ch20100.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch21800.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch21602.itc",                   # 0C
        "chr/ch21100.itc",                   # 0D
        "chr/ch21602.itc",                   # 0E
        "chr/ch24400.itc",                   # 0F
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

    DeclNpc(-25120,  0,       4139,    180,  261,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(6570,    -150,    5119,    90,   341,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4869,    0,       629,     225,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4820,    3000,    17420,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6309,    3000,    17329,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-6579,   0,       7170,    90,   261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-5219,   0,       7170,    270,  261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-15020,  -2599,   -8350,   180,  405,  0x0, 0,   10,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-13739,  -2599,   -8350,   180,  405,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3349,    0,       -9760,   270,  261,  0x0, 0,   15,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(2089,    0,       -9760,   90,   261,  0x0, 0,   11,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1629,    3000,    13079,   180,  261,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8039,    -150,    6960,    180,  469,  0x0, 0,   12,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(6980,    -300,    7619,    180,  389,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5500,    -200,    8000,    270,  469,  0x0, 0,   14,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 39,  39.5,                  -19.0,                 -4.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -19.75,                9.5,                   0.9000000357627869,    1.0])

    DeclActor(14410,   -6500,   -13590,  1200,    14410,   -5500,   -13590,  0x007C, 0,  4,  0x0000)
    DeclActor(-32070,  -1000,   11050,   1200,    -32070,  0,       11050,   0x007C, 0,  5,  0x0000)
    DeclActor(4050,    0,       -190,    1000,    4870,    1500,    630,     0x007E, 0,  8,  0x0000)
    DeclActor(-31040,  -1000,   9420,    1500,    -29950,  1000,    8850,    0x007C, 0,  30, 0x0000)

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

    ScpFunction((
        "Function_0_710",          # 00, 0
        "Function_1_7C8",          # 01, 1
        "Function_2_7F3",          # 02, 2
        "Function_3_A97",          # 03, 3
        "Function_4_C3E",          # 04, 4
        "Function_5_DA1",          # 05, 5
        "Function_6_F07",          # 06, 6
        "Function_7_121B",         # 07, 7
        "Function_8_1600",         # 08, 8
        "Function_9_1604",         # 09, 9
        "Function_10_1B11",        # 0A, 10
        "Function_11_1C5F",        # 0B, 11
        "Function_12_1CC1",        # 0C, 12
        "Function_13_1EE5",        # 0D, 13
        "Function_14_2062",        # 0E, 14
        "Function_15_22C8",        # 0F, 15
        "Function_16_2329",        # 10, 16
        "Function_17_23A9",        # 11, 17
        "Function_18_2551",        # 12, 18
        "Function_19_2703",        # 13, 19
        "Function_20_29A8",        # 14, 20
        "Function_21_2B1B",        # 15, 21
        "Function_22_2BF1",        # 16, 22
        "Function_23_2E08",        # 17, 23
        "Function_24_2EB3",        # 18, 24
        "Function_25_3D67",        # 19, 25
        "Function_26_3DCF",        # 1A, 26
        "Function_27_3E37",        # 1B, 27
        "Function_28_417A",        # 1C, 28
        "Function_29_42AC",        # 1D, 29
        "Function_30_47AF",        # 1E, 30
        "Function_31_4837",        # 1F, 31
        "Function_32_5200",        # 20, 32
        "Function_33_523D",        # 21, 33
        "Function_34_5259",        # 22, 34
        "Function_35_5275",        # 23, 35
        "Function_36_5291",        # 24, 36
        "Function_37_52AD",        # 25, 37
        "Function_38_5472",        # 26, 38
        "Function_39_54EF",        # 27, 39
    ))


    def Function_0_710(): pass

    label("Function_0_710")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_750"),
        (1, "loc_75C"),
        (2, "loc_768"),
        (3, "loc_774"),
        (4, "loc_780"),
        (5, "loc_78C"),
        (6, "loc_798"),
        (SWITCH_DEFAULT, "loc_7A4"),
    )


    label("loc_750")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_75C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_768")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_774")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_780")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_78C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_798")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7C7")

    Return()

    # Function_0_710 end

    def Function_1_7C8(): pass

    label("Function_1_7C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F2")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_1_7C8")

    label("loc_7F2")

    Return()

    # Function_1_7C8 end

    def Function_2_7F3(): pass

    label("Function_2_7F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BE")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_891")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_8B0")

    label("loc_891")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B0")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_8B0")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95F")

    label("loc_8BE")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_937")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_956")

    label("loc_937")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_956")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_956")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95F")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_98C")
    SetChrPos(0x13, 21980, 0, -10790, 135)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_A4E")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9D3")
    SetChrPos(0x13, -2410, 0, -1730, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9CE")
    LoadEffect(0x0, "event\\eva02_00.eff")

    label("loc_9CE")

    Jump("loc_A4E")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A3B")
    ClearChrFlags(0xB, 0x80)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0xE, 0xE1, 0x0)
    SetChrPos(0x13, -6580, 0, 5810, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A36")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_A36")

    Jump("loc_A4E")

    label("loc_A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A4E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5F")
    Event(0, 24)

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_A73")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)
    Jump("loc_A96")

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_A87")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 28)
    Jump("loc_A96")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_A96")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 31)

    label("loc_A96")

    Return()

    # Function_2_7F3 end

    def Function_3_A97(): pass

    label("Function_3_A97")

    ClearMapObjFlags(0x9, 0x10)
    OP_70(0x9, 0x1E)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x8, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACD")
    OP_1B(0x1, 0x0, 0x25)
    OP_1B(0x8, 0x0, 0x26)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE0")
    OP_1B(0x1, 0x0, 0x25)

    label("loc_AE0")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFD")
    OP_66(0x3, 0x1)

    label("loc_AFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1E")
    OP_65(0x1, 0x1)
    OP_66(0x3, 0x1)

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31")
    OP_70(0x7, 0x0)
    Jump("loc_B35")

    label("loc_B31")

    OP_70(0x7, 0x1E)

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B48")
    OP_70(0x8, 0x0)
    Jump("loc_B4C")

    label("loc_B48")

    OP_70(0x8, 0x1E)

    label("loc_B4C")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -25000, -4000, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 24000, -4000, -8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 4000, -1000, 18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_A97 end

    def Function_4_C3E(): pass

    label("Function_4_C3E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6A")
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
    Jump("loc_D8F")

    label("loc_D6A")


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

    label("loc_D8F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C3E end

    def Function_5_DA1(): pass

    label("Function_5_DA1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9D")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_E26")
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
    Jump("loc_E98")

    label("loc_E26")

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

    label("loc_E98")

    Jump("loc_EE2")

    label("loc_E9D")

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

    label("loc_EE2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F06")
    Call(0, 29)

    label("loc_F06")

    Return()

    # Function_5_DA1 end

    def Function_6_F07(): pass

    label("Function_6_F07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F8E")

    #C0006
    ChrTalk(
        0xFE,
        (
            "今日は日が落ちてから\x01",
            "締めの花火が打ち上げられるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "これは見逃せないな。\x01",
            "いい場所を確保しておかないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1217")

    label("loc_F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_110A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1097")

    #C0008
    ChrTalk(
        0xFE,
        "ハッピー、アニバーサリー！\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ポンスは導力カメラを構えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)

    #C0010
    ChrTalk(
        0xFE,
        (
            "君たちもどうだい？\x01",
            "楽しんでるかい？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1105")

    label("loc_1097")


    #C0011
    ChrTalk(
        0xFE,
        (
            "今日は一段と\x01",
            "素晴らしい写真ばかりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "ふふふ、クロスベル万歳だねぇ～！\x01",
            "ハッピー、アニバーサリー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1105")

    Jump("loc_1217")

    label("loc_110A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1169")

    #C0013
    ChrTalk(
        0xFE,
        (
            "うーん、みんな\x01",
            "笑顔でいい感じだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "これは写真の現像がたのしみだなぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1217")

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11CC")

    #C0015
    ChrTalk(
        0xFE,
        "おお、飛行船まで飛んでいるのか……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "どれどれ、記念に\x01",
            "もう一枚撮っておこう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1217")

    label("loc_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1217")

    #C0017
    ChrTalk(
        0xFE,
        "うーん、さすがは創立記念祭！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "写真の題材には困らないよ。\x02",
    )

    CloseMessageWindow()

    label("loc_1217")

    TalkEnd(0xFE)
    Return()

    # Function_6_F07 end

    def Function_7_121B(): pass

    label("Function_7_121B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12AF")
    Jump("loc_12F9")

    label("loc_12AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12CF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12F9")

    label("loc_12CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12EF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12F9")

    label("loc_12EF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12F9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1392")

    #C0019
    ChrTalk(
        0xFE,
        (
            "今日は午後から\x01",
            "市庁舎で閉会式があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "マクダエル市長も出席なさるし\x01",
            "僕も見にいこうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F8")

    label("loc_1392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1415")

    #C0021
    ChrTalk(
        0xFE,
        (
            "こうして外国の人と\x01",
            "まったり話すと、\x01",
            "記念祭って気がするね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "できれば来年も\x01",
            "クロスベルに来て欲しいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F8")

    label("loc_1415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1469")
    SetChrSubChip(0xFE, 0x1)

    #C0023
    ChrTalk(
        0xFE,
        "はっは、僕は全然構いませんよ。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "さあ、一緒にかんぱ～い！\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F8")

    label("loc_1469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14EF")

    #C0025
    ChrTalk(
        0xFE,
        (
            "観光バスに飛行船かあ……\x01",
            "まったく今年は派手だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "おちおち本も読んでられないや。\x01",
            "僕も一回りしてみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F8")

    label("loc_14EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_15F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A1")

    #C0027
    ChrTalk(
        0xFE,
        (
            "僕は昨日、市長の\x01",
            "開会演説を聞いてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "マクダエル市長って\x01",
            "もう７０過ぎだっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "あんな事件があったのに\x01",
            "衰えを感じさせない人だよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F8")

    label("loc_15A1")


    #C0030
    ChrTalk(
        0xFE,
        "やっぱりマクダエル市長は凄いよ。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "まだまだ引退するには\x01",
            "早いんじゃないかなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_121B end

    def Function_8_1600(): pass

    label("Function_8_1600")

    Call(0, 9)
    Return()

    # Function_8_1600 end

    def Function_9_1604(): pass

    label("Function_9_1604")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1611")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_166F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_166F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168F")
    OP_AF(0xCF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B08")

    label("loc_168F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16A3")
    Jump("loc_1B08")

    label("loc_16A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B08")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1726")

    #C0032
    ChrTalk(
        0xA,
        (
            "ふふ……\x01",
            "オスカー、遊んでくるがいいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        (
            "その間に次の新作パンを\x01",
            "研究してやるから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B08")

    label("loc_1726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_1787")

    #C0034
    ChrTalk(
        0xA,
        "ふふ、この人出は好都合だわ。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "私の焼いたパン、\x01",
            "みんなにアピールしてやる！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B08")

    label("loc_1787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CF")

    #C0036
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0038
    ChrTalk(
        0xA,
        (
            "…………？\x01",
            "どこかで見た子かも……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "……でも今日は見てないわね。\x01",
            "子供が１人だと目立つもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 23)
    Jump("loc_1921")

    label("loc_18CF")


    #C0041
    ChrTalk(
        0xA,
        (
            "少なくとも\x01",
            "試食には来てないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "……来てたら絶対\x01",
            "パンを勧めてるもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1921")

    Jump("loc_1B08")

    label("loc_1926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1987")

    #C0043
    ChrTalk(
        0xA,
        "ふふ、この人出は好都合だわ。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "私の焼いたパン、\x01",
            "みんなにアピールしてやる！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B08")

    label("loc_1987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19D6")

    #C0045
    ChrTalk(
        0xA,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xA,
        (
            "ふふ、遠慮せずに\x01",
            "買っていってね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B08")

    label("loc_19D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A5F")

    #C0047
    ChrTalk(
        0xA,
        (
            "ふふ……今月の新作パンは\x01",
            "私が担当になったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "記念祭の人出なら\x01",
            "大売れ間違いなし！\x01",
            "オスカーに差をつけてやるわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B08")

    label("loc_1A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC0")

    #C0049
    ChrTalk(
        0xA,
        "……お、お一つ試食をどうぞ。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        "美味しかったら買っていってね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B08")

    label("loc_1AC0")


    #C0051
    ChrTalk(
        0xA,
        "今日のパンは私が焼いてるのよ。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        "よ、よかったら買っていってね。\x02",
    )

    CloseMessageWindow()

    label("loc_1B08")

    Jump("loc_1611")

    label("loc_1B0D")

    TalkEnd(0xA)
    Return()

    # Function_9_1604 end

    def Function_10_1B11(): pass

    label("Function_10_1B11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B67")

    #C0053
    ChrTalk(
        0xFE,
        "タリーズ商店へようこそ～。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "どうぞご贔屓に～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1BD6")

    label("loc_1B67")


    #C0055
    ChrTalk(
        0xFE,
        (
            "モモったら\x01",
            "もう引っ込んじゃったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "うーん、この人出じゃ\x01",
            "引っ込み思案のあの子には\x01",
            "辛かったかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD6")

    Jump("loc_1C5B")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C5B")

    #C0057
    ChrTalk(
        0xFE,
        "いらっしゃいませー。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ウチの人ったら、いつも通り\x01",
            "のほほんとしているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "私がしっかり売り込まないとね。\x02",
    )

    CloseMessageWindow()

    label("loc_1C5B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1B11 end

    def Function_11_1C5F(): pass

    label("Function_11_1C5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9F")

    #C0060
    ChrTalk(
        0xFE,
        (
            "お祭り……\x01",
            "お客さんが多くてやだな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1CBD")

    label("loc_1C9F")


    #C0061
    ChrTalk(
        0xFE,
        "い、いらっしゃいませ……\x02",
    )

    CloseMessageWindow()

    label("loc_1CBD")

    TalkEnd(0xFE)
    Return()

    # Function_11_1C5F end

    def Function_12_1CC1(): pass

    label("Function_12_1CC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D38")

    #C0062
    ChrTalk(
        0xFE,
        (
            "今日は中央広場の辺りを\x01",
            "回ってみるかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "我が家に合う調度品が\x01",
            "売り出されておるやもしれん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1DB3")
    OP_93(0xFE, 0x5A, 0x0)

    #C0064
    ChrTalk(
        0xFE,
        (
            "むむ、ワシは今夜は\x01",
            "晩餐会に呼ばれておるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "お前、すっかり\x01",
            "忘れてるんじゃないだろうな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1E1A")

    #C0066
    ChrTalk(
        0xFE,
        "やれやれ、もう行ってしまったか。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "毎年のことじゃが\x01",
            "終わってしまうと寂しいのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E7A")
    OP_93(0xFE, 0x5A, 0x0)

    #C0068
    ChrTalk(
        0xFE,
        (
            "高いところの方が\x01",
            "見やすいじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "お前は本当に気が利かんのう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E8B")
    Call(0, 13)
    Jump("loc_1EE1")

    label("loc_1E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1EE1")

    #C0070
    ChrTalk(
        0xFE,
        (
            "めでたい祭りじゃ。\x01",
            "みなで楽しむとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "祭りの間は無礼講じゃよ。\x02",
    )

    CloseMessageWindow()

    label("loc_1EE1")

    TalkEnd(0xFE)
    Return()

    # Function_12_1CC1 end

    def Function_13_1EE5(): pass

    label("Function_13_1EE5")

    OP_4B(0xD, 0xFF)
    OP_4B(0x13, 0xFF)
    TurnDirection(0xD, 0x13, 0)
    TurnDirection(0x13, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCA")

    #C0072
    ChrTalk(
        0x13,
        "おやおや、議員じゃありませんか。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x13,
        (
            "おっと、引退なさったから\x01",
            "今は元議員でしたなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xD,
        (
            "あんたは確か\x01",
            "委員会の役員だった……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xD,
        (
            "ほほほ、達者にしておったかの？\x01",
            "それは何よりじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2059")

    label("loc_1FCA")


    #C0076
    ChrTalk(
        0xD,
        (
            "ほほ、わしは\x01",
            "もう政治には関わらんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xD,
        (
            "それより我が家に来んか？\x01",
            "共に一杯飲むとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x13,
        (
            "はっはっは、ぜひ\x01",
            "お邪魔させて頂きますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2059")

    OP_4C(0xD, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_13_1EE5 end

    def Function_14_2062(): pass

    label("Function_14_2062")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20EA")
    OP_93(0xFE, 0x10E, 0x0)

    #C0079
    ChrTalk(
        0xFE,
        (
            "あら、今日はアルカンシェルを\x01",
            "見に行くのではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "寄り道なんてしていたら\x01",
            "公演が終わってしまうわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C4")

    label("loc_20EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2157")
    OP_93(0xFE, 0x10E, 0x0)

    #C0081
    ChrTalk(
        0xFE,
        (
            "あら、試食して\x01",
            "帰るくらいいいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "ついでに買って\x01",
            "帰ればいいんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C4")

    label("loc_2157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_21C9")

    #C0083
    ChrTalk(
        0xFE,
        (
            "毎年のことだけど\x01",
            "パレードを見るとすっとするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "日ごろのうっ憤も\x01",
            "忘れてしまいそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C4")

    label("loc_21C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2240")
    OP_93(0xFE, 0x10E, 0x0)

    #C0085
    ChrTalk(
        0xFE,
        (
            "あら、パレードは\x01",
            "あちらから来るのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "ここで待っているのが\x01",
            "一番に決まっているじゃない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C4")

    label("loc_2240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2292")

    #C0087
    ChrTalk(
        0xFE,
        "主人は一応議員をしていたの。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "それなりの人脈はあるのよね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22C4")

    label("loc_2292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_22C4")

    #C0089
    ChrTalk(
        0xFE,
        (
            "記念祭くらい\x01",
            "夫婦で楽しもうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C4")

    TalkEnd(0xFE)
    Return()

    # Function_14_2062 end

    def Function_15_22C8(): pass

    label("Function_15_22C8")

    TalkBegin(0xFE)

    #C0090
    ChrTalk(
        0xFE,
        "あ、みてみて飛行船よ！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "ふわ～……\x01",
            "すごい飾りつけられてる。\x01",
            "さっすが記念祭ね～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_22C8 end

    def Function_16_2329(): pass

    label("Function_16_2329")

    TalkBegin(0xFE)
    OP_4B(0xF, 0xFF)

    #C0092
    ChrTalk(
        0xFE,
        (
            "うー、わたしは\x01",
            "家で寝ていたいのに……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xFE, 500)

    #C0093
    ChrTalk(
        0xF,
        "えー、もったいないよ～。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xF,
        "チルル、一緒に回ろ！\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x0)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_16_2329 end

    def Function_17_23A9(): pass

    label("Function_17_23A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2403")

    #C0095
    ChrTalk(
        0xFE,
        "ふう、もう最終日だよ……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "街が広すぎて\x01",
            "まだ半分も回ってないや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254D")

    label("loc_2403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_246B")

    #C0097
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "そこのパン屋さんで\x01",
            "試食をやってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "君らも食ってきたらどうだい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_254D")

    label("loc_246B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_24F2")

    #C0099
    ChrTalk(
        0xFE,
        (
            "君ら知ってる？\x01",
            "綺麗な噴水の前で\x01",
            "なんとか村の人が出店やってたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "マジオススメだ！\x01",
            "あのオムライスはウマかった！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_254D")

    label("loc_24F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_254D")

    #C0101
    ChrTalk(
        0xFE,
        (
            "帝国から鉄道に\x01",
            "揺られる事３時間……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "ようやく\x01",
            "クロスベルに着いたぞーっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254D")

    TalkEnd(0xFE)
    Return()

    # Function_17_23A9 end

    def Function_18_2551(): pass

    label("Function_18_2551")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_25C7")
    OP_93(0xFE, 0x5A, 0x0)

    #C0103
    ChrTalk(
        0xFE,
        "ほら、歓楽街の方を見に行こっ。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "折角家を\x01",
            "抜け出してきたんだもん。\x01",
            "楽しまなくっちゃ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26FF")

    label("loc_25C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_261D")
    OP_93(0xFE, 0x5A, 0x0)

    #C0105
    ChrTalk(
        0xFE,
        "こらっ、浮気モノ！\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "ハナシはぐらかすんじゃ\x01",
            "ないわよ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26FF")

    label("loc_261D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2688")

    #C0107
    ChrTalk(
        0xFE,
        (
            "あたしは中央広場にあった\x01",
            "スイーツ屋さんがグッドだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        "ちょー美味しいんだから！\x02",
    )

    CloseMessageWindow()
    Jump("loc_26FF")

    label("loc_2688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26FF")

    #C0109
    ChrTalk(
        0xFE,
        (
            "ママが許してくんなくって\x01",
            "お祭りにくるのが遅れちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "こうなったらパーっと\x01",
            "楽しまなくっちゃね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26FF")

    TalkEnd(0xFE)
    Return()

    # Function_18_2551 end

    def Function_19_2703(): pass

    label("Function_19_2703")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A0")

    #C0111
    ChrTalk(
        0xFE,
        (
            "あの建物は確か\x01",
            "クロスベル通信社だったはずだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "あれはビジネス街に\x01",
            "移転したはずだな。\x01",
            "今はどうなっているんだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2800")

    label("loc_27A0")


    #C0113
    ChrTalk(
        0xFE,
        (
            "街を歩き回ると\x01",
            "色々と発見があるものだねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "あの建物、今は\x01",
            "どうなっているんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2800")

    Jump("loc_29A4")

    label("loc_2805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2848")

    #C0115
    ChrTalk(
        0xFE,
        (
            "ふう、今年のパレードは\x01",
            "大した熱気だったなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A4")

    label("loc_2848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_28C2")

    #C0116
    ChrTalk(
        0xFE,
        (
            "さて、パレードの位置取りは\x01",
            "この辺りでいいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "記念祭の目玉行事だ、\x01",
            "見逃さないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A4")

    label("loc_28C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28D3")
    Call(0, 13)
    Jump("loc_29A4")

    label("loc_28D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_29A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294C")

    #C0118
    ChrTalk(
        0xFE,
        (
            "記念祭はやはり\x01",
            "ぶらぶらと回るのが楽しいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "いつもの街が\x01",
            "違って見えるからねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_29A4")

    label("loc_294C")


    #C0120
    ChrTalk(
        0xFE,
        (
            "あちこちに\x01",
            "屋台なんかが出ているねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "うむうむ、いつもの街が\x01",
            "違って見えるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A4")

    TalkEnd(0xFE)
    Return()

    # Function_19_2703 end

    def Function_20_29A8(): pass

    label("Function_20_29A8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A3C")
    Jump("loc_2A86")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A5C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A86")

    label("loc_2A5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A7C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A86")

    label("loc_2A7C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A86")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0122
    ChrTalk(
        0xFE,
        (
            "クロスベル人はよそ者でも\x01",
            "温かく迎えてくれるんじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "中々住み心地の\x01",
            "良さそうな街じゃわい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_29A8 end

    def Function_21_2B1B(): pass

    label("Function_21_2B1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2B82")

    #C0124
    ChrTalk(
        0xFE,
        (
            "まさにワンダフルな\x01",
            "パレードだったわね！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "うーん、やっぱり\x01",
            "来てよかったわ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BED")

    label("loc_2B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2BED")

    #C0126
    ChrTalk(
        0xFE,
        (
            "クロスベルのお祭りと\x01",
            "言ったらパレードでしょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "これを見に遠い所を\x01",
            "やって来たんだから～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BED")

    TalkEnd(0xFE)
    Return()

    # Function_21_2B1B end

    def Function_22_2BF1(): pass

    label("Function_22_2BF1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C85")
    Jump("loc_2CCF")

    label("loc_2C85")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CA5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CCF")

    label("loc_2CA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CC5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CCF")

    label("loc_2CC5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CCF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2D42")

    #C0128
    ChrTalk(
        0x16,
        (
            "今日は西通りで\x01",
            "のんびりさせてもらおうかのう。\x01",
            "ほっほっほ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E00")

    label("loc_2D42")


    #C0129
    ChrTalk(
        0x16,
        (
            "わしはいつも住宅街で\x01",
            "のんびり過ごしとるんじゃが。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x16,
        (
            "今日はお気に入りのベンチに\x01",
            "疲れた顔のスーツの男が座っておってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x16,
        (
            "ほっほ、たそがれておったので\x01",
            "席を譲ってやったんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_2E00")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_2BF1 end

    def Function_23_2E08(): pass

    label("Function_23_2E08")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB2")
    OP_29(0x46, 0x1, 0xB)

    #C0132
    ChrTalk(
        0x101,
        (
            "#0000F（これで西通りも\x01",
            "  一通り回ったけど……）\x02\x03",

            "（……みんなの捜索状況は\x01",
            "  どうなってるかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_2EB2")

    Return()

    # Function_23_2E08 end

    def Function_24_2EB3(): pass

    label("Function_24_2EB3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(13500, 1000, -8500, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 12700, 0, -8500, 90)
    SetChrPos(0x160, 14300, 0, -8500, 270)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(40, 19, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0134
    AnonymousTalk(
        0x101,
        "#0001Fはい、ロイドです。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3006():
        OP_9A(0xFE, 0x101, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_3006)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィです。\x01",
            "気になることがあったので\x01",
            "報告するわね。\x02\x03",

            "今ちょうど、ティオちゃんと\x01",
            "一緒にいるんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうも、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0137
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fああ、合流したのか。\x02\x03",

            "それで、どうしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0138
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "コリン君だけど、桟橋の所で\x01",
            "水上バスを眺めていたらしいわ。\x02\x03",

            "その後、どこに行ったのか\x01",
            "分からなかったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そこでツァイトに頼んで\x01",
            "匂いを探ってもらったんです。\x02\x03",

            "そしたら……\x01",
            "桟橋から階段を登ったところで\x01",
            "突然、匂いが途切れたそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0140
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F匂いが途切れた……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、港湾区の南東の端だけど……\x02\x03",

            "これってどういう事なのかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0142
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F……もしかして……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x160, 1)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【車両の中に入った】\x01",          # 0
            "【川に落ちてしまった】\x01",        # 1
            "【誰かに抱き上げられた】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_336F"),
        (1, "loc_34D4"),
        (2, "loc_3770"),
        (SWITCH_DEFAULT, "loc_398D"),
    )


    label("loc_336F")

    OP_2C(0x46, 0x2)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0143
    AnonymousTalk(
        0x101,
        (
            "#0003Fある程度密閉され、\x01",
            "匂いが外に漏れない場所……\x02\x03",

            "#0001F何らかの車両に乗り込んだ\x01",
            "可能性があるかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0144
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なるほど……\x01",
            "それなら納得ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0146
    AnonymousTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304Fええ、レンも同意見よ。\x02\x03",

            "#3301Fそうなると、どこの車両に\x01",
            "乗り込んだかが問題になるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_398D")

    label("loc_34D4")

    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0147
    AnonymousTalk(
        0x101,
        (
            "#0011Fまさか……\x01",
            "川に落ちたんじゃないだろうな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0148
    AnonymousTalk(
        0x160,
        (
            "#3306Fもう、お兄さん。\x01",
            "何を聞いていたのかしら。\x02\x03",

            "#3301F桟橋から階段を登ったところって\x01",
            "狼さんが言っていたんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0149
    AnonymousTalk(
        0x101,
        "#0006Fあ、そうか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0150
    AnonymousTalk(
        0x160,
        (
            "#3303Fたとえ抱っこされていても\x01",
            "多少の匂いは残されるはずよ。\x02\x03",

            "#3300Fでも、ある程度密閉された\x01",
            "場所に入ったのだとしたら……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0151
    AnonymousTalk(
        0x101,
        "#0005Fそうか……車両か！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なるほど……\x01",
            "それなら納得ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0154
    AnonymousTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304Fええ、そういうこと。\x02\x03",

            "#3301Fそうなると、どこの車両に\x01",
            "乗り込んだかが問題になるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_398D")

    label("loc_3770")

    OP_2C(0x46, 0x1)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0155
    AnonymousTalk(
        0x101,
        (
            "#0013F誰かに抱き上げられた状態で\x01",
            "その場を離れた……\x02\x03",

            "#0008Fいや……違う気がする。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0156
    AnonymousTalk(
        0x160,
        (
            "#3303Fええ、たとえ抱っこされていても\x01",
            "多少の匂いは残されるはずよ。\x02\x03",

            "#3300Fでも、ある程度密閉された\x01",
            "場所に入ったのだとしたら……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0157
    AnonymousTalk(
        0x101,
        "#0005Fそうか……車両か！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なるほど……\x01",
            "それなら納得ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0160
    AnonymousTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304Fええ、そういうこと。\x02\x03",

            "#3301Fそうなると、どこの車両に\x01",
            "乗り込んだかが問題になるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_398D")

    label("loc_398D")

    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ところで……\x01",
            "誰か他にそこにいるの？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どこかで聞いたような\x01",
            "女の子の声がしますけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0163
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006Fいや、色々あってさ。\x02\x03",

            "#0001Fとにかく、いったん集まって\x01",
            "状況を整理した方が──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3AA3():
        OP_96(0xFE, 0x37DC, 0x0, 0xFFFFDECC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_3AA3)
    WaitChrThread(0x160, 1)
    SetMessageWindowPos(50, 30, -1, -1)

    #A0164
    AnonymousTalk(
        0x160,
        (
            "#3304F──ねえ、お兄さん。\x02\x03",

            "#3300F支援課の端末、貸してもらうわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0165
    AnonymousTalk(
        0x101,
        "#0005Fへっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x160, 3, 0, 25)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0166
    ChrTalk(
        0x101,
        "#5P#0011Fちょ、ちょっと待った！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x5)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0167
    AnonymousTalk(
        0x101,
        (
            "#0013F──エリィ、ティオ！\x01",
            "ランディにも連絡して\x01",
            "いったん支援課に戻ってくれ！\x02\x03",

            "その時に一通り説明するから！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("エリィの声")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "え、ええ……分かったわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ティオの声")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よく分かりませんが了解です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    SetCameraDistance(18500, 3000)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x160, 0xFF)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 3)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2EB3 end

    def Function_25_3D67(): pass

    label("Function_25_3D67")

    OP_92(0x160, 0x4650, 0xFFFFD440, 0x1F4)

    def lambda_3D79():
        OP_95(0xFE, 18000, 0, -11200, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_3D79)
    WaitChrThread(0x160, 1)

    def lambda_3D97():
        OP_95(0xFE, 18000, -2000, -19600, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_3D97)
    WaitChrThread(0x160, 1)

    def lambda_3DB5():
        OP_95(0xFE, 27000, -4000, -19600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_3DB5)
    WaitChrThread(0x160, 1)
    Return()

    # Function_25_3D67 end

    def Function_26_3DCF(): pass

    label("Function_26_3DCF")

    OP_92(0x101, 0x4650, 0xFFFFD440, 0x1F4)

    def lambda_3DE1():
        OP_95(0xFE, 18000, 0, -11200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DE1)
    WaitChrThread(0x101, 1)

    def lambda_3DFF():
        OP_95(0xFE, 18000, -2000, -19600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DFF)
    WaitChrThread(0x101, 1)

    def lambda_3E1D():
        OP_95(0xFE, 27000, -4000, -19600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E1D)
    WaitChrThread(0x101, 1)
    Return()

    # Function_26_3DCF end

    def Function_27_3E37(): pass

    label("Function_27_3E37")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07200.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    LoadChrToIndex("chr/ch09400.itc", 0x20)
    OP_68(32800, -3000, -19000, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 35000, -4000, -19500, 270)
    SetChrPos(0x102, 35000, -4000, -18500, 270)
    SetChrPos(0x103, 36300, -4000, -19500, 270)
    SetChrPos(0x104, 36300, -4000, -18500, 270)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 31300, -4000, -19000, 90)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 30300, -4000, -18300, 90)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 30300, -4000, -19700, 90)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    MoveCamera(43, 23, 0, 11000)
    SetCameraDistance(21500, 11000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0x17, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0x17, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_93(0x17, 0x10E, 0x1F4)

    def lambda_405A():

        label("loc_405A")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_405A")

    QueueWorkItem2(0x18, 2, lambda_405A)

    def lambda_406C():

        label("loc_406C")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_406C")

    QueueWorkItem2(0x19, 2, lambda_406C)

    def lambda_407E():
        OP_96(0xFE, 0x75F8, 0xFFFFF060, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_407E)
    WaitChrThread(0x17, 1)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    OP_63(0x17, 0x0, 1600, 0x8, 0x9, 0xFA, 0x0)

    def lambda_40B6():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_40B6)

    def lambda_40D0():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_40D0)

    def lambda_40EA():
        OP_98(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_40EA)
    WaitChrThread(0x18, 1)

    def lambda_4108():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4108)

    def lambda_4122():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4122)

    def lambda_413C():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_413C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x17)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x17, 0x1)
    OP_6F(0x79)
    SetScenarioFlags(0x5C, 5)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_3E37 end

    def Function_28_417A(): pass

    label("Function_28_417A")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(160, 5000, 20460, 0)
    MoveCamera(23, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -1000, 3000, 22200, 180)
    SetChrPos(0x102, 400, 3000, 22700, 180)
    SetChrPos(0x103, 400, 3000, 24260, 180)
    SetChrPos(0x104, -1000, 3000, 23860, 180)
    Sleep(50)

    def lambda_4201():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4201)
    Sleep(100)

    def lambda_4219():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4219)
    Sleep(100)

    def lambda_4231():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4231)
    Sleep(100)

    def lambda_4249():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4249)
    OP_68(-2940, 5000, 12880, 4800)
    MoveCamera(41, 28, 0, 4800)
    OP_6E(600, 4800)
    SetCameraDistance(16500, 4800)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0240", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_417A end

    def Function_29_42AC(): pass

    label("Function_29_42AC")

    EventBegin(0x0)
    Fade(800)
    OP_68(-29840, 700, 9950, 0)
    MoveCamera(301, 36, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    SetChrPos(0x101, -31110, -1000, 11250, 270)
    SetChrPos(0x102, -28840, -1000, 11440, 270)
    SetChrPos(0x103, -29910, -1000, 11720, 270)
    SetChrPos(0x104, -27680, -1000, 11600, 270)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_93(0x101, 0xB4, 0x190)
    Sleep(600)

    #C0170
    ChrTalk(
        0x101,
        "#5P#0005Fあれ……？\x02",
    )

    CloseMessageWindow()

    def lambda_4370():

        label("loc_4370")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_4370")

    QueueWorkItem2(0x104, 1, lambda_4370)

    def lambda_4382():

        label("loc_4382")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_4382")

    QueueWorkItem2(0x102, 1, lambda_4382)

    def lambda_4394():

        label("loc_4394")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_4394")

    QueueWorkItem2(0x103, 1, lambda_4394)
    OP_95(0x101, -31250, -1000, 9570, 700, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手すりに真新しい傷跡がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0172
    ChrTalk(
        0x104,
        "#12P#0305Fロイド、何かあったのか？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#5P#0001Fああ……何かを\x01",
            "引っ掛けた跡みたいだな。\x02\x03",

            "#0003Fそれも手前側についている……\x01",
            "通行人が付けたとは\x01",
            "考えにくいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        (
            "#11P#0200Fそういえば、この裏口は\x01",
            "アパートに入るのに最適ですね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    TurnDirection(0x101, 0x103, 500)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_453C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_453C)
    Sleep(10)

    def lambda_454C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_454C)

    def lambda_4559():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4559)
    Sleep(12)

    def lambda_4569():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4569)
    Sleep(200)
    OP_68(-19620, 700, 13840, 4000)
    MoveCamera(16, 20, 0, 4000)
    Sleep(5200)
    Fade(500)
    OP_68(-29840, 700, 9950, 0)
    MoveCamera(301, 36, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    OP_0D()

    #C0175
    ChrTalk(
        0x104,
        (
            "#12P#0305F確かにここを使えば\x01",
            "大通りを避けて侵入できそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        (
            "#12P#0103F目撃情報が少ないのは\x01",
            "そのせいかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4705")

    #C0177
    ChrTalk(
        0x101,
        (
            "#5P#0000Fよし、下調べはこんな所だな。\x02\x03",

            "一旦イリアさんの部屋に戻って\x01",
            "整理してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        "#12P#0300F了解、そろそろ作戦を考えるか！\x02",
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x9)
    Jump("loc_478D")

    label("loc_4705")


    #C0179
    ChrTalk(
        0x101,
        (
            "#5P#0003F…………………………\x02\x03",

            "#0001Fまだ断定するのは危険だ。\x01",
            "もう少し聞き込みをしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        "#12P#0300F了解、行ってみるかね。\x02",
    )

    CloseMessageWindow()

    label("loc_478D")

    SetChrPos(0x0, -30970, -1000, 11070, 270)
    OP_66(0x3, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_29_42AC end

    def Function_30_47AF(): pass

    label("Function_30_47AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C9")
    Call(0, 29)
    Return()

    label("loc_47C9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手すりには\x01",
            "引っ掻いたような跡がある。\x02",
        )
    )

    CloseMessageWindow()

    #A0182
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最近付いた物のようだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_30_47AF end

    def Function_31_4837(): pass

    label("Function_31_4837")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10100.itc", 0x1E)
    OP_68(-19540, 660, 12830, 0)
    MoveCamera(53, 41, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x101, -29500, -1000, 11640, 56)
    SetChrPos(0x102, -8400, 0, 6880, 0)
    SetChrPos(0x103, -8400, 0, 6880, 0)
    SetChrPos(0x104, -10300, 0, 13950, 0)
    SetChrPos(0x1A, -19560, -1000, 14750, 180)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0xA)
    MoveCamera(37, 31, 0, 3900)

    def lambda_4917():
        OP_95(0xFE, -19560, -1000, 12750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4917)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1200)
    OP_95(0x104, -10300, 0, 7880, 4000, 0x0)
    Sleep(900)

    #N0183
    NpcTalk(
        0x104,
        "声",
        "#5C#1Pいたか……！？\x02",
    )

    CloseMessageWindow()

    #N0184
    NpcTalk(
        0x102,
        "声",
        (
            "#5C#1Pダメみたい。\x01",
            "表通りで見た人は居ないそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0185
    NpcTalk(
        0x103,
        "声",
        "#5C#3Pおかしいですね……\x02",
    )

    CloseMessageWindow()

    #N0186
    NpcTalk(
        0x1A,
        "少年",
        (
            "#5Pへっ……\x01",
            "……このオレが\x01",
            "そう簡単に捕まるかよ。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-19540, 660, 12830, 0)
    MoveCamera(40, 36, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(27430, 0)
    OP_0D()
    Sleep(200)
    OP_93(0x1A, 0x10E, 0x190)
    Sleep(300)

    #N0187
    NpcTalk(
        0x1A,
        "少年",
        (
            "#5Pこんな都会の\x01",
            "腑抜け連中なんかに……\x02",
        )
    )

    CloseMessageWindow()

    #N0188
    NpcTalk(
        0x1A,
        "少年",
        (
            "#5Pフン、見てろ。\x01",
            "後で仕返ししてやるからな……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-22720, 660, 11450, 1200)
    MoveCamera(56, 36, 0, 1200)
    OP_95(0x1A, -19900, -1000, 11430, 6000, 0x1)
    OP_95(0x1A, -22720, -1000, 11450, 6000, 0x0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x1A, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)

    #N0189
    NpcTalk(
        0x1A,
        "少年",
        "#11Pあっ……！？\x02",
    )

    CloseMessageWindow()

    #N0190
    NpcTalk(
        0x101,
        "声",
        "#2Pそう甘くは行かないぞ。\x02",
    )

    CloseMessageWindow()
    OP_68(-24890, 660, 11580, 2000)
    SetCameraDistance(31610, 2000)
    OP_95(0x101, -26250, -1000, 12160, 1800, 0x0)

    #C0191
    ChrTalk(
        0x101,
        (
            "#6P#0001F君がこのルートを使うのは知っている。\x01",
            "今回はこちらの作戦勝ちだな。\x02",
        )
    )

    CloseMessageWindow()

    #N0192
    NpcTalk(
        0x1A,
        "少年",
        "#11Pくそっ……！\x02",
    )

    CloseMessageWindow()

    def lambda_4C03():
        OP_95(0xFE, -21200, -1000, 11420, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4C03)
    Sleep(50)

    #C0193
    ChrTalk(
        0x101,
        "#5P#0007Fいい加減に諦めろ！\x02",
    )

    OP_68(-20560, 660, 11200, 2000)
    MoveCamera(306, 36, 0, 2000)
    OP_95(0x101, -21850, -1000, 11450, 6000, 0x0)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    CloseMessageWindow()

    #N0194
    NpcTalk(
        0x1A,
        "少年",
        (
            "#12Pわっ……くそっ……！！\x01",
            "このやろう……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x1A, 2, 0, 32)
    Sleep(100)
    BeginChrThread(0x101, 2, 0, 32)

    #N0195
    NpcTalk(
        0x1A,
        "少年",
        "#12Pは、離せ……離せよっ……！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#5P#0001Fそういう訳には行かない。\x01",
            "君の行為は犯罪で……\x02\x03",

            "#0006F……というか\x01",
            "大人しくしてろって……！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x1B, 1, 0, 36)

    #N0197
    NpcTalk(
        0x1A,
        "少年",
        "#12Pこの……このっ！！\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#5P#0010F痛っ……\x01",
            "こら、腕を振り回すな！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x104, -11580, 0, 6930, 261)
    SetChrPos(0x102, -10570, 0, 6180, 261)
    SetChrPos(0x103, -10050, 0, 7210, 261)

    #C0199
    ChrTalk(
        0x104,
        (
            "#0300Fはは、こいつはまた\x01",
            "活きのいいのが掛かったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1A)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    EndChrThread(0x1A, 0x2)

    def lambda_4E49():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4E49)

    def lambda_4E56():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E56)
    OP_68(-18900, 860, 8630, 2000)
    MoveCamera(309, 24, 0, 2000)
    BeginChrThread(0x104, 1, 0, 35)
    Sleep(200)
    BeginChrThread(0x102, 1, 0, 33)
    Sleep(200)
    BeginChrThread(0x103, 1, 0, 34)
    Sleep(1200)

    #N0200
    NpcTalk(
        0x1A,
        "少年",
        "#11Pお、お前らさっきの……\x02",
    )

    CloseMessageWindow()

    #N0201
    NpcTalk(
        0x1A,
        "少年",
        "#11Pだ、騙しやがったなッ……！？\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        (
            "#0202F#12Pくす……\x01",
            "演技するのも肩が懲りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#6P#0100Fすばしこいから\x01",
            "驚いてしまったけど、\x01",
            "何とか捕まえられたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        "#5P#0000Fああ、でも……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1B58)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x1A, 0x5A, 0x1F4)
    OP_93(0x101, 0x5A, 0x1F4)
    BeginChrThread(0x1A, 2, 0, 32)
    Sleep(800)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    #C0205
    ChrTalk(
        0x104,
        (
            "#6P#0303F何だかイメージと違うなぁ。\x02\x03",

            "#0300F地味な奴とは聞いてたが、\x01",
            "どっちかてえと粗末つーか\x01",
            "みすぼらしいっつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#6P#0105Fクロスベルの子でも\x01",
            "なさそうだし……\x02\x03",

            "どこか辺境の出身かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        (
            "#12P#0200F犯行を見ても\x01",
            "熱狂的ファンと言うよりは\x01",
            "ただの空き巣でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#5P#0001Fまあその辺りの事情は\x01",
            "ゆっくり喋ってもらおう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0209
    ChrTalk(
        0x101,
        (
            "#5P#0006Fというか……\x01",
            "そろそろ大人しくしろって！\x02",
        )
    )

    CloseMessageWindow()

    #N0210
    NpcTalk(
        0x1A,
        "少年",
        (
            "#11Pやめろっ、離せ……！\x01",
            "……離せこのおおっ！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(35190, 1800)
    OP_0D()
    EndChrThread(0x1B, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0240", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4837 end

    def Function_32_5200(): pass

    label("Function_32_5200")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_523C")
    OP_A6(0xFE, 0x0, 0x14, 0x258, 0xBB8)
    Sleep(800)
    OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
    Sleep(1200)
    Jump("Function_32_5200")

    label("loc_523C")

    Return()

    # Function_32_5200 end

    def Function_33_523D(): pass

    label("Function_33_523D")

    OP_95(0x102, -17370, 0, 6510, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_33_523D end

    def Function_34_5259(): pass

    label("Function_34_5259")

    OP_95(0x103, -16239, 0, 7090, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_34_5259 end

    def Function_35_5275(): pass

    label("Function_35_5275")

    OP_95(0x104, -17830, 0, 7480, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_35_5275 end

    def Function_36_5291(): pass

    label("Function_36_5291")

    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Return()

    # Function_36_5291 end

    def Function_37_52AD(): pass

    label("Function_37_52AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F8")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_536E")

    #C0211
    ChrTalk(
        0x101,
        (
            "#0003F住宅街の方はハロルドさんが\x01",
            "探しているはずだ……\x02\x03",

            "もし見つかれば\x01",
            "すぐに連絡があるだろうし。\x02\x03",

            "#0001F予定通り、分担した街区で\x01",
            "聞き込みを続けていこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_53E2")

    label("loc_536E")


    #C0212
    ChrTalk(
        0x101,
        (
            "#0003F住宅街の方はハロルドさんが\x01",
            "探しているはずだ……\x02\x03",

            "#0001F予定通り、分担した街区で\x01",
            "聞き込みを続けていこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E2")

    Sleep(50)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)

    label("loc_53F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5471")
    EventBegin(0x1)

    #C0213
    ChrTalk(
        0x101,
        (
            "#0001F寄り道してる場合じゃない……\x02\x03",

            "なるべく急いで\x01",
            "西クロスベル街道に行こう！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)

    label("loc_5471")

    Return()

    # Function_37_52AD end

    def Function_38_5472(): pass

    label("Function_38_5472")

    EventBegin(0x1)

    #C0214
    ChrTalk(
        0x101,
        (
            "#0000F今のところ\x01",
            "街の外に出たって情報はないな。\x02\x03",

            "……もう少しこの辺りで\x01",
            "聞き込みをしてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    # Function_38_5472 end

    def Function_39_54EF(): pass

    label("Function_39_54EF")

    EventBegin(0x1)

    #C0215
    ChrTalk(
        0x101,
        (
            "#0000F今は特に用事がないな……\x01",
            "コリン君の捜索に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 36500, -4000, -19000, 270)
    EventEnd(0x4)
    Return()

    # Function_39_54EF end

    SaveToFile()

Try(main)
