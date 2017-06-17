from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1000.bin",                # FileName
        "t1000",                    # MapName
        "t1000",                    # Location
        0x0041,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1000",                  # 0
        "観光客",                 # 1
        "観光客",                 # 2
        "観光客",                 # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
        "乗組員サルサ",           # 7
        "リーシャ",               # 8
        "キーア",                 # 9
        "フラン",                 # 10
        "セシル",                 # 11
        "イリア",                 # 12
        "シュリ",                 # 13
        "マリアベル",             # 14
        "ツァイト",               # 15
        "水上バス",               # 16
        "乗客",                   # 17
        "乗客",                   # 18
        "乗客",                   # 19
        "乗客",                   # 20
        "乗客",                   # 21
        "乗客",                   # 22
        "乗客",                   # 23
        "乗客",                   # 24
        "SE制御",                 # 25
        "ボート",                 # 26
        "ボート",                 # 27
        "テーマパーク方面",       # 28
        "邸宅方面",               # 29
        "湖水浴場方面",           # 30
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch20900.itc",                   # 01
        "chr/ch20300.itc",                   # 02
        "chr/ch20200.itc",                   # 03
        "chr/ch21300.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch28400.itc",                   # 06
        "chr/ch05200.itc",                   # 07
    ))

    DeclNpc(7730,    -2000,   -24510,  90,   389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(9050,    -2000,   -24510,  270,  389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-7389,   -4000,   -48110,  180,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-7389,   -4000,   -49110,  0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-27649,  -4000,   -50220,  270,  389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-639,    -2000,   -26030,  180,  389,  0x0, 0,   5,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-3740,   -4000,   -47180,  180,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(23450,   -5000,   -54930,  1200,    29380,   -6000,   -55430,  0x007C, 0,  14, 0x0000)
    DeclActor(10350,   -3990,   -46410,  1200,    10350,   -2500,   -46410,  0x007C, 0,  41, 0x0000)
    DeclActor(3300,    -5000,   -58160,  2500,    3300,    -3500,   -58160,  0x007C, 0,  42, 0x0000)

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "テーマパーク方面")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "邸宅方面")
    PlaceName(75.0, 0.0, 15.0, 0x0000, 0x0000, "湖水浴場方面")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ChipFrameInfo(1296, 0)                                       # 0

    ScpFunction((
        "Function_0_510",          # 00, 0
        "Function_1_5C0",          # 01, 1
        "Function_2_5EB",          # 02, 2
        "Function_3_721",          # 03, 3
        "Function_4_8DF",          # 04, 4
        "Function_5_964",          # 05, 5
        "Function_6_A02",          # 06, 6
        "Function_7_A86",          # 07, 7
        "Function_8_B16",          # 08, 8
        "Function_9_BFB",          # 09, 9
        "Function_10_C83",         # 0A, 10
        "Function_11_D2B",         # 0B, 11
        "Function_12_DDE",         # 0C, 12
        "Function_13_1253",        # 0D, 13
        "Function_14_129E",        # 0E, 14
        "Function_15_1372",        # 0F, 15
        "Function_16_2D35",        # 10, 16
        "Function_17_2D9D",        # 11, 17
        "Function_18_2DD1",        # 12, 18
        "Function_19_2E11",        # 13, 19
        "Function_20_2E51",        # 14, 20
        "Function_21_2E91",        # 15, 21
        "Function_22_2ED1",        # 16, 22
        "Function_23_2F11",        # 17, 23
        "Function_24_2F51",        # 18, 24
        "Function_25_2F91",        # 19, 25
        "Function_26_2FA7",        # 1A, 26
        "Function_27_35B6",        # 1B, 27
        "Function_28_36B4",        # 1C, 28
        "Function_29_376C",        # 1D, 29
        "Function_30_3781",        # 1E, 30
        "Function_31_37E1",        # 1F, 31
        "Function_32_382F",        # 20, 32
        "Function_33_387D",        # 21, 33
        "Function_34_38CB",        # 22, 34
        "Function_35_3919",        # 23, 35
        "Function_36_396D",        # 24, 36
        "Function_37_3D00",        # 25, 37
        "Function_38_3D55",        # 26, 38
        "Function_39_3D7A",        # 27, 39
        "Function_40_3E82",        # 28, 40
        "Function_41_3EA8",        # 29, 41
        "Function_42_3F3B",        # 2A, 42
    ))


    def Function_0_510(): pass

    label("Function_0_510")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_548"),
        (1, "loc_554"),
        (2, "loc_560"),
        (3, "loc_56C"),
        (4, "loc_578"),
        (5, "loc_584"),
        (6, "loc_590"),
        (SWITCH_DEFAULT, "loc_59C"),
    )


    label("loc_548")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_554")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_560")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_56C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_578")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_584")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_590")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_59C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A8")

    label("loc_5BF")

    Return()

    # Function_0_510 end

    def Function_1_5C0(): pass

    label("Function_1_5C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EA")
    OP_94(0xFE, 0xFFFFE3A4, 0xFFFFA132, 0x1AB8, 0xFFFF90A2, 0x3E8)
    Sleep(500)
    Jump("Function_1_5C0")

    label("loc_5EA")

    Return()

    # Function_1_5C0 end

    def Function_2_5EB(): pass

    label("Function_2_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_6D5")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_634")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -10480, -2000, -26610, 270)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_634")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1130, -4000, -53460, 180)
    Jump("loc_6D5")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_69B")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1130, -4000, -53460, 180)
    Jump("loc_6D5")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6CC")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_6D5")

    label("loc_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_6D5")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6E9")
    ClearScenarioFlags(0x22, 0)
    Event(0, 15)
    Jump("loc_720")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_6FD")
    ClearScenarioFlags(0x22, 1)
    Event(0, 26)
    Jump("loc_720")

    label("loc_6FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_711")
    ClearScenarioFlags(0x22, 2)
    Event(0, 36)
    Jump("loc_720")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_720")
    ClearScenarioFlags(0x22, 3)
    Event(0, 39)

    label("loc_720")

    Return()

    # Function_2_5EB end

    def Function_3_721(): pass

    label("Function_3_721")

    SetMapObjFrame(0xFF, "t1000_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1000_sky_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_757")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_757")

    Sound(126, 1, 80, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_774")
    SoundLoad(918)
    BeginChrThread(0x20, 3, 0, 40)

    label("loc_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79E")
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_70(0x0, 0x1E)
    Jump("loc_7A4")

    label("loc_79E")

    SetMapObjFlags(0x0, 0x4)

    label("loc_7A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C9")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_7DB")

    label("loc_7C9")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)

    label("loc_7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EF")
    ClearMapObjFlags(0x1, 0x4)

    label("loc_7EF")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80B")
    ClearMapObjFlags(0x7, 0x4)
    OP_66(0x2, 0x1)

    label("loc_80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_829")
    OP_11(0xD1, 0xED, 0xFC, 0x32, 0xC8, 0x0)

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84B")
    SetMapObjFrame(0xFF, "t1000_water", 0x2, "loop_off")

    label("loc_84B")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 29380, -6000, -55430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8BC")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x3C, 0x1F4, 0x0)
    Jump("loc_8DE")

    label("loc_8BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_8DE")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x3C, 0x1F4, 0x0)

    label("loc_8DE")

    Return()

    # Function_3_721 end

    def Function_4_8DF(): pass

    label("Function_4_8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F6")
    Call(0, 12)
    Return()

    label("loc_8F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_907")
    Jump("loc_960")

    label("loc_907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_915")
    Jump("loc_960")

    label("loc_915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_923")
    Jump("loc_960")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_93B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_936")

    label("loc_936")

    Jump("loc_960")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_949")
    Jump("loc_960")

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_957")
    Jump("loc_960")

    label("loc_957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_960")

    label("loc_960")

    TalkEnd(0xFE)
    Return()

    # Function_4_8DF end

    def Function_5_964(): pass

    label("Function_5_964")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_975")
    Jump("loc_9FE")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9F5")

    #C0001
    ChrTalk(
        0x8,
        (
            "まあまあ、湖を眺めながら\x01",
            "待つのも一興じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "歩き回るのも少々疲れたし、\x01",
            "ここで待っていようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FE")

    label("loc_9F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9FE")

    label("loc_9FE")

    TalkEnd(0xFE)
    Return()

    # Function_5_964 end

    def Function_6_A02(): pass

    label("Function_6_A02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A13")
    Jump("loc_A82")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A79")

    #C0003
    ChrTalk(
        0x9,
        (
            "水上バスはまだ\x01",
            "来ていないみたいだねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "やっぱりもう少し\x01",
            "遊んでいましょうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A82")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A82")

    label("loc_A82")

    TalkEnd(0xFE)
    Return()

    # Function_6_A02 end

    def Function_7_A86(): pass

    label("Function_7_A86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A97")
    Jump("loc_B12")

    label("loc_A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_AA5")
    Jump("loc_B12")

    label("loc_AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B12")

    #C0005
    ChrTalk(
        0xA,
        "ちょっと、あなたったら……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xA,
        (
            "いざ乗り込もうって時に\x01",
            "不安になることを\x01",
            "言わないでちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B12")

    TalkEnd(0xFE)
    Return()

    # Function_7_A86 end

    def Function_8_B16(): pass

    label("Function_8_B16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B27")
    Jump("loc_BF7")

    label("loc_B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B96")

    #C0007
    ChrTalk(
        0xB,
        (
            "ミシュラムの賑やかさから\x01",
            "ちょっと離れたくなってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        "ここはいい場所だよ、癒されるな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF7")

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BF7")

    #C0009
    ChrTalk(
        0xB,
        (
            "えっと、ホテルに\x01",
            "忘れ物はないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "……ない、ハズだな。\x01",
            "………………たぶん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF7")

    TalkEnd(0xFE)
    Return()

    # Function_8_B16 end

    def Function_9_BFB(): pass

    label("Function_9_BFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C0C")
    Jump("loc_C7F")

    label("loc_C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C1A")
    Jump("loc_C7F")

    label("loc_C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C7F")

    #C0011
    ChrTalk(
        0xC,
        (
            "ボーイフレンドと\x01",
            "はぐれちゃったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xC,
        (
            "も～、早く来ないと\x01",
            "先に帰っちゃうんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7F")

    TalkEnd(0xFE)
    Return()

    # Function_9_BFB end

    def Function_10_C83(): pass

    label("Function_10_C83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C94")
    Jump("loc_D27")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CA2")
    Jump("loc_D27")

    label("loc_CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D27")

    #C0013
    ChrTalk(
        0xD,
        (
            "ガールフレンドが先に\x01",
            "行っちゃったみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xD,
        (
            "ああ～、どこに行ったんだろう。\x01",
            "水上バスが出る前に見つけないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D27")

    TalkEnd(0xFE)
    Return()

    # Function_10_C83 end

    def Function_11_D2B(): pass

    label("Function_11_D2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D3C")
    Jump("loc_DDA")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D4A")
    Jump("loc_DDA")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_DD1")

    #C0015
    ChrTalk(
        0xE,
        (
            "水上バスは、間もなく\x01",
            "クロスベル発着場へと向けて\x01",
            "出発いたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xE,
        (
            "お乗りの際は、\x01",
            "お早めにご搭乗くださいませー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDA")

    label("loc_DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_DDA")

    label("loc_DDA")

    TalkEnd(0xFE)
    Return()

    # Function_11_D2B end

    def Function_12_DDE(): pass

    label("Function_12_DDE")

    EventBegin(0x0)
    OP_4B(0xF, 0xFF)
    Fade(500)
    OP_68(-9680, -800, -26810, 0)
    MoveCamera(314, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30350, 0)
    SetChrPos(0x101, -7850, -2000, -27000, 270)
    SetChrPos(0x153, -7850, -2000, -26200, 270)
    OP_0D()
    Sleep(2000)
    OP_64(0xF)

    #C0017
    ChrTalk(
        0xF,
        "#01803F…………ふう…………\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#12P#00005F……リーシャ？\x01",
            "こんなところに居たのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x5A, 0x1F4)

    #C0019
    ChrTalk(
        0xF,
        "#01805Fロイドさん、キーアちゃん……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x153,
        (
            "#01105Fねえリーシャ、\x01",
            "なんだか元気ないよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#00000F何か悩み事でもあるのか？\x01",
            "俺でよかったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xF,
        (
            "#01809Fああいえ、大した事じゃ……\x02\x03",

            "#01804Fその、歓楽街以外でも\x01",
            "にぎやかな場所はあるんだなって、\x01",
            "ちょっと気疲れしちゃって。\x02\x03",

            "#01802Fでも、ここで風にあたってたら\x01",
            "だいぶ気が休まりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#12P#00003F……そうか、ならいいんだけど。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x153,
        "#01108Fリーシャ、ほんとに大丈夫ー？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xF,
        (
            "#01809Fうん、もう平気だから。\x02\x03",

            "#01803Fそれじゃあ、ロイドさん。\x01",
            "私はイリアさんたちの所に\x01",
            "行ってますね。\x02\x03",

            "#01802F待ち合わせには皆さんと\x01",
            "一緒に行きますので\x01",
            "心配しないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#12P#00005Fあ、ああ……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xF, 0x40)
    OP_68(-7800, -800, -26950, 4000)
    BeginChrThread(0xF, 3, 0, 13)
    Sleep(300)

    def lambda_1158():

        label("loc_1158")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_1158")

    QueueWorkItem2(0x101, 2, lambda_1158)

    def lambda_116A():

        label("loc_116A")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_116A")

    QueueWorkItem2(0x153, 2, lambda_116A)
    WaitChrThread(0xF, 3)
    SetChrFlags(0xF, 0x80)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x153, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    TurnDirection(0x153, 0x101, 500)
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0027
    ChrTalk(
        0x153,
        "#01105Fどうしたの、ロイド？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    #C0028
    ChrTalk(
        0x101,
        (
            "#6P#00003F……いや、なんでもないよ。\x02\x03",

            "#00000F俺たちもそろそろ行こうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15A, 5)
    SetChrPos(0x0, -8850, -2000, -26600, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_DDE end

    def Function_13_1253(): pass

    label("Function_13_1253")

    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_125F():
        OP_95(0xFE, -8610, -2000, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_125F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x0)

    def lambda_1284():
        OP_95(0xFE, -610, -2000, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1284)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_1253 end

    def Function_14_129E(): pass

    label("Function_14_129E")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0029
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(27760, -3400, -57630, 1500)
    MoveCamera(315, 28, 0, 1500)
    OP_6E(300, 1500)
    SetCameraDistance(35500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0030
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136D")
    OP_E2(0x2)
    MiniGame(0x6, 0x5, 0x5B9A, 0xFFFFEC78, 0xFFFF296E, 0x5A, 0x72C4, 0xFFFFE890, 0xFFFF277A)

    label("loc_136D")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_14_129E end

    def Function_15_1372(): pass

    label("Function_15_1372")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08500.itc", 0x1F)
    LoadChrToIndex("chr/ch05200.itc", 0x20)
    LoadChrToIndex("chr/ch05100.itc", 0x21)
    LoadChrToIndex("chr/ch07500.itc", 0x22)
    LoadChrToIndex("chr/ch10100.itc", 0x23)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    LoadChrToIndex("chr/ch20600.itc", 0x28)
    LoadChrToIndex("chr/ch20200.itc", 0x29)
    LoadChrToIndex("chr/ch20300.itc", 0x2A)
    LoadChrToIndex("chr/ch21600.itc", 0x2B)
    LoadChrToIndex("chr/ch21300.itc", 0x2C)
    LoadChrToIndex("chr/ch21200.itc", 0x2D)
    LoadChrToIndex("chr/ch27700.itc", 0x2E)
    LoadChrToIndex("chr/ch23600.itc", 0x2F)
    SoundLoad(2713)
    SoundLoad(2714)
    SoundLoad(2715)
    SoundLoad(3774)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis406.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05900.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu14000.itp")
    CreatePortrait(6, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -7250, -4000, -41000, 180)
    SetChrPos(0x102, -7250, -4000, -41000, 180)
    SetChrPos(0x103, -7250, -4000, -41000, 180)
    SetChrPos(0x104, -7250, -4000, -41000, 180)
    SetChrPos(0x109, -7250, -4000, -41000, 180)
    SetChrPos(0x105, -7250, -4000, -41000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -7250, -4000, -41000, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 2500, -4000, -50000, 270)
    SetChrFlags(0x11, 0x8)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 4500, -4000, -49500, 270)
    SetChrFlags(0x13, 0x8)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 4350, -4000, -51000, 270)
    SetChrFlags(0x12, 0x8)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 5650, -4000, -51000, 270)
    SetChrFlags(0xF, 0x8)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6000, -4000, -49350, 270)
    SetChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 4650, -4000, -50000, 270)
    SetChrFlags(0x15, 0x8)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x0, 0x17)
    OP_49()
    SetChrPos(0x17, -25070, -5500, -38200, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x18, 0x28)
    SetChrChipByIndex(0x19, 0x29)
    SetChrChipByIndex(0x1A, 0x2A)
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrChipByIndex(0x1C, 0x2C)
    SetChrChipByIndex(0x1D, 0x2D)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrChipByIndex(0x1F, 0x2F)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x18, -7250, -4000, -41000, 180)
    SetChrPos(0x19, -7250, -4000, -41000, 180)
    SetChrPos(0x1A, -7250, -4000, -41000, 180)
    SetChrPos(0x1B, -7250, -4000, -41000, 180)
    SetChrPos(0x1C, -7250, -4000, -41000, 180)
    SetChrPos(0x1D, -7250, -4000, -41000, 180)
    SetChrPos(0x1E, -7250, -4000, -41000, 180)
    SetChrPos(0x1F, -7250, -4000, -41000, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-5070, 1300, -18200, 0)
    MoveCamera(330, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(78000, 0)
    PlaceName2(340, 40, "c_plac20", 0x0, 2500)
    OP_68(-5070, -2700, -18200, 10000)
    MoveCamera(330, 9, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(78000, 10000)
    FadeToBright(1000, 0)
    BeginChrThread(0x17, 3, 0, 16)
    BeginChrThread(0x20, 1, 0, 25)
    WaitChrThread(0x17, 3)
    OP_0D()
    Fade(500)
    OP_68(-7250, -3000, -46000, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(50000, 0)
    OP_0D()
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x8)
    Sound(108, 0, 80, 0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xF1, 0x12C, 0x0, 0x20)
    BeginChrThread(0x18, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x19, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1A, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1B, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1C, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1D, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1E, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x1F, 3, 0, 17)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 18)
    Sleep(800)
    BeginChrThread(0x10, 3, 0, 24)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(800)
    BeginChrThread(0x103, 3, 0, 20)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 19)
    Sleep(800)
    BeginChrThread(0x105, 3, 0, 23)
    Sleep(800)
    BeginChrThread(0x109, 3, 0, 22)
    Fade(500)
    OP_68(-7460, -3000, -50070, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32000, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x10, 3)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x1E, 0x3)
    EndChrThread(0x1F, 0x3)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)

    #C0031
    ChrTalk(
        0x101,
        (
            "#00002F#6Pさてと……\x01",
            "確かマリアベルさんが\x01",
            "待っててくれてるんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00104F#11Pええ、９時半に待ち合わせだから\x01",
            "ちょうど時間のはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x11, 0x8)
    OP_C9(0x0, 0x80000000)

    #N0033
    NpcTalk(
        0x11,
        "娘の声",
        "#2713V#1P#30Wあ、来た来た～！\x02",
    )

    CloseMessageWindow()
    OP_24(0xA99)
    OP_C9(0x1, 0x80000000)
    OP_63(0x10, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x101,
        "#00005F#6Pこの声って……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x109,
        "#10111F#11Pま、まさか……！？\x02",
    )

    CloseMessageWindow()

    def lambda_1C73():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C73)
    Sleep(50)

    def lambda_1C83():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C83)
    Sleep(50)

    def lambda_1C93():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1C93)
    Sleep(50)

    def lambda_1CA3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CA3)
    Sleep(50)

    def lambda_1CB3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1CB3)
    Sleep(50)

    def lambda_1CC3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1CC3)
    Sleep(50)

    def lambda_1CD3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1CD3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x10, 2)
    Sleep(300)
    Fade(500)
    OP_68(-3250, -3000, -50350, 0)
    MoveCamera(30, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32000, 0)
    OP_68(-6250, -3000, -50350, 2500)

    def lambda_1D43():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D43)
    Sleep(500)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0036
    AnonymousTalk(
        0x11,
        (
            "#2714V#30Wお姉ちゃん、皆さん、\x01",
            "おはようございま～す！\x02\x03",

            "#2715V#30Wキーアちゃんも、おはよ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA9B)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0037
    ChrTalk(
        0x10,
        "#01109F#6Pおはよー！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#00305F#6Pおお、フランちゃんかよ！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x109,
        (
            "#10106F#5Pど、どうしてここに……\x02\x03",

            "#10101F昨日会った時、そんなこと、\x01",
            "言ってなかったじゃない！？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x11,
        (
            "#06409F#11Pえへへ、お姉ちゃんたちを\x01",
            "びっくりさせたくって～。\x02\x03",

            "#06402Fそれに特別ゲストは\x01",
            "わたしだけじゃないよ～。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x14, 0x8)

    #N0041
    NpcTalk(
        0x12,
        "女性の声",
        "#1Pふふっ、来たみたいね。\x02",
    )

    CloseMessageWindow()

    #N0042
    NpcTalk(
        0x13,
        "女性の声",
        (
            "#1Pよーし、メンツも揃ったし\x01",
            "今日は楽しめそうね～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x101,
        "#00005F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#00105F#6Pこ、この声は……\x02",
    )

    CloseMessageWindow()
    OP_68(-5400, -3000, -50350, 3000)

    def lambda_218F():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_218F)
    Sleep(100)

    def lambda_21A7():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_21A7)
    Sleep(100)

    def lambda_21BF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_21BF)
    Sleep(100)

    def lambda_21D7():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_21D7)
    WaitChrThread(0x13, 1)

    #C0045
    ChrTalk(
        0x101,
        "#00011F#6P！？\x02",
    )

    WaitChrThread(0x12, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x14, 1)
    OP_6F(0x79)
    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x104,
        "#00307F#6Pおおおおっ！？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x10,
        "#01110F#6Pあー、セシルだぁ！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#00205F#6Pそれにイリアさんたちまで……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x105,
        (
            "#10302F#6Pへえ、また綺麗どころが\x01",
            "集まってるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#00106F#6Pこ、こんな事をしそうなのは……\x02\x03",

            "#00101F──ベル、あなたね！？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2357")
    OP_C9(0x0, 0x80000000)

    #N0051
    NpcTalk(
        0x15,
        "女性の声",
        "#3774V#1P#30Wうふふ──正解ですわ。\x02",
    )

    CloseMessageWindow()
    OP_24(0xEBE)
    OP_C9(0x1, 0x80000000)
    Jump("loc_237F")

    label("loc_2357")


    #N0052
    NpcTalk(
        0x15,
        "女性の声",
        "#1Pうふふ──正解ですわ。\x02",
    )

    CloseMessageWindow()

    label("loc_237F")

    OP_68(-4680, -3000, -50240, 2500)

    def lambda_2395():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2395)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    #C0053
    ChrTalk(
        0x101,
        (
            "#00012F#6Pマリアベルさん……\x01",
            "これは一体、どういう？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x6, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x6, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    OP_CC(0x0, 0x6, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0054
    AnonymousTalk(
        0x15,
        (
            "フフ、皆さんを招待したついでに\x01",
            "日頃仲がいいと聞いている方々も\x01",
            "お呼びしたわけですわ。\x02\x03",

            "アルカンシェルの方々は\x01",
            "来月始まるリニューアル公演の\x01",
            "激励も兼ねていますけれど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x6, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x6, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    OP_CC(0x0, 0x6, 0x0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0055
    AnonymousTalk(
        0x13,
        "弟君たち、やっほー。\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    #Sound(2634, 255, 100, 0)    #voice#Rixia
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0056
    AnonymousTalk(
        0xF,
        (
            "ふふっ。\x01",
            "どうもご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    OP_CB(0x5, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0057
    AnonymousTalk(
        0x14,
        "な、なんでオレまで……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x5, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x5, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CC(0x0, 0x5, 0x0)
    Sleep(300)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは……\x01",
            "何て言ったらいいのか。\x02\x03",

            "#00002Fセシル姉、休暇取れたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0059
    AnonymousTalk(
        0x12,
        (
            "ええ、偶然取れたところに\x01",
            "イリアから連絡があって……\x02\x03",

            "ロイドたちも来るというから\x01",
            "お言葉に甘えちゃったの。\x02\x03",

            "迷惑じゃなかったかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0060
    ChrTalk(
        0x101,
        "#00009F#6Pいや……すごく嬉しいよ。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#00307F#6Pうおおおおおっ！\x01",
            "俺は夢でも見てんのか！？\x02\x03",

            "#00306Fセシルさんにイリアさんに\x01",
            "綺麗どころがこんなに沢山……\x02\x03",

            "#00309Fひゃっほう！\x01",
            "テンションＭＡＸだぜ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#00211F#5Pランディさん、ウザイです。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        "#10304F#6Pま、気持ちは分かるけどね。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#10112F#6Pでも、ちょっと驚きました……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#00102F#6Pひょっとして泊まる場所も\x01",
            "同じホテルに用意してくれたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x15,
        (
            "#02904F#11Pええ、皆さんのお部屋は\x01",
            "ホテル３ＦのＶＩＰフロアに\x01",
            "用意しています。\x02\x03",

            "まずは部屋に案内しますから\x01",
            "荷物を置いてくるといいでしょう。\x02\x03",

            "#02902Fその後、ミシュラムリゾートの\x01",
            "新たな目玉に行かれるといいですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        "#00105F#6P新たな目玉……？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#00205F#6Pテーマパークではなく？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x11,
        (
            "#06409F#11Pえへへ、わたしも聞いて\x01",
            "ビックリしちゃったんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xF,
        (
            "#01802F#11P実はその、新しい施設が\x01",
            "オープンしたらしくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x13,
        (
            "#01709F#11P昼まで貸し切り状態に\x01",
            "してくれるらしいのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x15,
        (
            "#02904F#11Pええ、是非とも皆さんで\x01",
            "楽しんでもらいたいですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x10,
        "#01105F#6Pふえ～……？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00005F#6Pえっと？\x01",
            "その施設というのは一体……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x15,
        (
            "#02912F#11Pうふふ……\x01",
            "内陸にあるクロスベルのために\x01",
            "わざわざ作り上げた楽園#4Rパラダイス#……\x02\x03",

            "#02909F美しきエルム湖を臨む\x01",
            "純白の『湖水浴場#8Rレイク・ビーチ#』ですわ。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(126, 1000, 80)
    SetCameraDistance(32375, 1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t1020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1372 end

    def Function_16_2D35(): pass

    label("Function_16_2D35")

    OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0xBB8, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
    Sound(478, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x1F4)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x5B, 0x78, 0x1F4, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x12D, 0x168, 0x0, 0x20)
    Return()

    # Function_16_2D35 end

    def Function_17_2D9D(): pass

    label("Function_17_2D9D")


    def lambda_2DA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DA2)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0xFFA6, 0x3A98, 0x9C4, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_2D9D end

    def Function_18_2DD1(): pass

    label("Function_18_2DD1")


    def lambda_2DD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DD6)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7250, -4000, -52000, 2500, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_2DD1 end

    def Function_19_2E11(): pass

    label("Function_19_2E11")


    def lambda_2E16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E16)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -6250, -4000, -49500, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_2E11 end

    def Function_20_2E51(): pass

    label("Function_20_2E51")


    def lambda_2E56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E56)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7250, -4000, -50000, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_2E51 end

    def Function_21_2E91(): pass

    label("Function_21_2E91")


    def lambda_2E96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E96)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -8750, -4000, -51000, 2500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_2E91 end

    def Function_22_2ED1(): pass

    label("Function_22_2ED1")


    def lambda_2ED6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ED6)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7750, -4000, -48500, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_2ED1 end

    def Function_23_2F11(): pass

    label("Function_23_2F11")


    def lambda_2F16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F16)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -8750, -4000, -49000, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_2F11 end

    def Function_24_2F51(): pass

    label("Function_24_2F51")


    def lambda_2F56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F56)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -6250, -4000, -51500, 2500, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_2F51 end

    def Function_25_2F91(): pass

    label("Function_25_2F91")

    Sound(475, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Sound(476, 0, 100, 0)
    Return()

    # Function_25_2F91 end

    def Function_26_2FA7(): pass

    label("Function_26_2FA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00302.itc", 0x1E)
    LoadChrToIndex("chr/ch00001.itc", 0x1F)
    LoadChrToIndex("chr/ch00101.itc", 0x20)
    LoadChrToIndex("chr/ch00201.itc", 0x21)
    LoadChrToIndex("chr/ch00301.itc", 0x22)
    LoadEffect(0x0, "event\\ev315_00.eff")
    SoundLoad(483)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x21, 0x80)
    OP_78(0x1, 0x21)
    OP_49()
    SetChrPos(0x21, -20090, -5500, -68880, 90)
    OP_D5(0x21, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0x1, "light00", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0x7, 0x22)
    OP_49()
    SetChrPos(0x22, 1700, -5500, -59250, 90)
    OP_D5(0x22, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x1, 0x3C, 0x0, 0x20)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0x104, 0x20)
    OP_90(0x101, -20090, 0, -68280, 90)
    OP_90(0x102, -20090, 0, -69480, 90)
    OP_90(0x103, -21090, 0, -68880, 90)
    OP_90(0x104, -18290, 0, -68880, 90)
    OP_11(0xD1, 0xED, 0xFC, 0x32, 0xC8, 0x0)
    SetMapObjFrame(0xFF, "t1000_water", 0x2, "loop")
    OP_68(740, -4500, -59120, 0)
    MoveCamera(325, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(60000, 0)
    FadeToBright(1000, 0)
    OP_68(14740, -4500, -59120, 10000)
    SetCameraDistance(35000, 10000)
    BeginChrThread(0x21, 3, 0, 28)
    BeginChrThread(0x20, 1, 0, 35)
    WaitChrThread(0x21, 3)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(3500, -4000, -58250, 0)
    MoveCamera(318, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x101, 17500, 0, -58250, 0)
    OP_90(0x102, 16500, 0, -58750, 0)
    OP_90(0x103, 17500, 0, -59750, 0)
    OP_90(0x104, 16500, 0, -60250, 0)
    OP_68(22000, -4000, -54650, 10000)
    MoveCamera(0, 28, 0, 10000)
    SetCameraDistance(18500, 10000)
    Sleep(1500)
    BeginChrThread(0x101, 3, 0, 31)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 32)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 33)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 34)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Fade(500)
    OP_68(20020, 4600, -48340, 0)
    MoveCamera(342, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(20020, 1000, -48340, 4000)
    OP_6F(0x79)

    #C0076
    ChrTalk(
        0x103,
        "#00201F#11P#N鐘の音が……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3345")

    #C0077
    ChrTalk(
        0x101,
        (
            "#00011F#5P#Nこれは……\x01",
            "《鏡の城》の最上階にあった？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0078
    ChrTalk(
        0x102,
        "#00101F#5P#Nええ……そうみたいね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_33AA")

    label("loc_3345")


    #C0079
    ChrTalk(
        0x102,
        (
            "#00101F#5P#Nこれは……\x01",
            "《鏡の城》の上にある鐘？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0080
    ChrTalk(
        0x101,
        "#00001F#5P#Nそんなものがあるのか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_33AA")


    #C0081
    ChrTalk(
        0x104,
        (
            "#00306F#5P#Nなんか水面も\x01",
            "ボンヤリ光ってやがるし……\x02\x03",

            "#00301Fティオすけ、何だか分かるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0082
    ChrTalk(
        0x103,
        (
            "#00203F#11P#Nどうやら“霊圧”のようなものが\x01",
            "高まりつつあるようです……\x02\x03",

            "#00201Fそれも奥にある\x01",
            "テーマパーク方面から。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00003F#5P#Nそうか……\x02\x03",

            "#00013Fそちらにアリオスさんたちが\x01",
            "向かった可能性は高そうだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0084
    ChrTalk(
        0x102,
        "#00107F#5P#Nええ……行ってみましょう！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x0, 22000, -4910, -53650, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 5)
    OP_29(0xAD, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3577")
    Jump("loc_357C")

    label("loc_3577")

    OP_29(0x94, 0x4, 0x40)

    label("loc_357C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_358D")
    Jump("loc_3592")

    label("loc_358D")

    OP_29(0x95, 0x4, 0x40)

    label("loc_3592")

    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_32(0xFF, 0xFF, 0x0)
    OP_66(0x2, 0x1)
    OP_24(0x1E3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_26_2FA7 end

    def Function_27_35B6(): pass

    label("Function_27_35B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36B3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360F")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_36AE")

    label("loc_360F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365D")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_36AE")

    label("loc_365D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36AB")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_36AE")

    label("loc_36AB")

    Sleep(233)

    label("loc_36AE")

    Jump("Function_27_35B6")

    label("loc_36B3")

    Return()

    # Function_27_35B6 end

    def Function_28_36B4(): pass

    label("Function_28_36B4")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x21, 0, 0, 27)
    OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x1D4C, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1964, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9B(0x1, 0xFE, 0xFFF1, 0x7D0, 0xFA0, 0x0)
    OP_9B(0x1, 0xFE, 0xFFE2, 0x2EE0, 0xBB8, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9B(0x1, 0xFE, 0xFFD3, 0xBB8, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x5DC, 0x3E8, 0x0)
    OP_82(0x1E, 0x0, 0xBB8, 0x1F4)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_71(0x1, 0x1, 0x3C, 0x1F4, 0x20)
    Return()

    # Function_28_36B4 end

    def Function_29_376C(): pass

    label("Function_29_376C")

    OP_96(0xFE, 0x445C, 0xFFFFEE08, 0xFFFF1C76, 0x7D0, 0x0)
    Return()

    # Function_29_376C end

    def Function_30_3781(): pass

    label("Function_30_3781")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0x445C, 0xFFFFEFCA, 0xFFFF1F00, 0x258, 0x7D0)
    Sound(30, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    OP_9D(0xFE, 0x445C, 0xFFFFEC78, 0xFFFF2478, 0x320, 0x7D0)
    ClearChrFlags(0xFE, 0x4)
    Sound(31, 0, 100, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_3781 end

    def Function_31_37E1(): pass

    label("Function_31_37E1")

    BeginChrThread(0xFE, 2, 0, 29)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 2, 0, 30)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_95(0xFE, 22000, -4900, -53650, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_31_37E1 end

    def Function_32_382F(): pass

    label("Function_32_382F")

    BeginChrThread(0xFE, 2, 0, 29)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 2, 0, 30)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_95(0xFE, 21400, -4900, -54650, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_32_382F end

    def Function_33_387D(): pass

    label("Function_33_387D")

    BeginChrThread(0xFE, 2, 0, 29)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 2, 0, 30)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_95(0xFE, 22600, -4900, -54650, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_387D end

    def Function_34_38CB(): pass

    label("Function_34_38CB")

    BeginChrThread(0xFE, 2, 0, 29)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 2, 0, 30)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_95(0xFE, 22000, -4900, -55650, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_34_38CB end

    def Function_35_3919(): pass

    label("Function_35_3919")

    Sound(483, 2, 50, 0)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(200)
    OP_25(0x1E3, 0x50)
    Sleep(200)
    OP_25(0x1E3, 0x5A)
    Sleep(200)
    OP_25(0x1E3, 0x64)
    Sleep(2000)
    StopSound(483, 500, 100)
    Sound(481, 0, 100, 0)
    Sleep(2500)
    Sound(484, 0, 70, 0)
    Sleep(500)
    Sound(477, 0, 60, 0)
    Sleep(5000)
    Sound(478, 0, 60, 0)
    Return()

    # Function_35_3919 end

    def Function_36_396D(): pass

    label("Function_36_396D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20600.itc", 0x1E)
    LoadChrToIndex("chr/ch20200.itc", 0x1F)
    LoadChrToIndex("chr/ch20300.itc", 0x20)
    LoadChrToIndex("chr/ch21600.itc", 0x21)
    LoadChrToIndex("chr/ch21300.itc", 0x22)
    LoadChrToIndex("chr/ch21200.itc", 0x23)
    LoadChrToIndex("chr/ch27700.itc", 0x24)
    LoadChrToIndex("chr/ch23600.itc", 0x25)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x0, 0x17)
    OP_49()
    SetChrPos(0x17, -45000, -5500, -38200, 0)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrChipByIndex(0x1F, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, -7250, -4000, -40000, 180)
    SetChrPos(0x19, -7250, -4000, -40000, 180)
    SetChrPos(0x1A, -7250, -4000, -40000, 180)
    SetChrPos(0x1B, -7250, -4000, -40000, 180)
    SetChrPos(0x1C, -7250, -4000, -40000, 180)
    SetChrPos(0x1D, -7250, -4000, -40000, 180)
    SetChrPos(0x1E, -7250, -4000, -40000, 180)
    SetChrPos(0x1F, -7250, -4000, -40000, 180)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    PlaceName2(340, 200, "c_plac20", 0x0, 3000)
    FadeToBright(2000, 0)
    OP_68(20240, -2400, -36530, 0)
    MoveCamera(334, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(64730, 0)
    OP_68(-1240, -2400, -36530, 15000)
    BeginChrThread(0x20, 1, 0, 38)

    def lambda_3C0E():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3C0E)
    WaitChrThread(0x17, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    Sound(478, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0x12D, 0x168, 0x0, 0x20)
    OP_6F(0x1)
    EndChrThread(0x20, 0x1)
    OP_0D()
    Fade(1000)
    OP_68(-5240, -1300, -48610, 0)
    MoveCamera(327, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(31570, 0)
    OP_0D()
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0xF1, 0x12C, 0x0, 0x20)
    BeginChrThread(0x18, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1A, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1B, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1C, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1D, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 37)
    Sleep(1000)
    BeginChrThread(0x1F, 3, 0, 37)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1030", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_36_396D end

    def Function_37_3D00(): pass

    label("Function_37_3D00")


    def lambda_3D05():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D05)
    Sleep(500)

    def lambda_3D22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D22)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3D3B():
        OP_95(0xFE, 7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D3B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_37_3D00 end

    def Function_38_3D55(): pass

    label("Function_38_3D55")

    Sleep(1000)
    Sound(475, 0, 100, 0)
    Sleep(1500)
    Sound(477, 0, 100, 0)
    Sleep(4000)
    Sound(476, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Return()

    # Function_38_3D55 end

    def Function_39_3D7A(): pass

    label("Function_39_3D7A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(479)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x0, 0x17)
    OP_49()
    SetChrPos(0x17, -5000, -5500, -38200, 0)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x0)
    Sound(475, 0, 100, 0)
    OP_68(1000, -500, -38550, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(35000, 0)
    MoveCamera(325, 17, 0, 4500)
    Sound(477, 0, 100, 0)
    Sound(479, 2, 100, 0)
    SetChrPos(0x17, -5000, -5500, -38200, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_3E36():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3E36)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x17, 0x1)
    SetMapObjFlags(0x0, 0x4)
    StopBGM(0xFA0)
    StopSound(479, 3000, 100)
    StopSound(126, 3000, 80)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_3D7A end

    def Function_40_3E82(): pass

    label("Function_40_3E82")

    Sleep(1000)

    label("loc_3E85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EA7")
    Sound(918, 0, 30, 0)
    Sleep(2200)
    Sound(918, 0, 20, 0)
    Sleep(5000)
    Jump("loc_3E85")

    label("loc_3EA7")

    Return()

    # Function_40_3E82 end

    def Function_41_3EA8(): pass

    label("Function_41_3EA8")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《クロスベル市》行き水上バス・時刻表\x01\x01",
            "   ※またのお越しを\x01",
            "　       お待ちしております！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_41_3EA8 end

    def Function_42_3F3B(): pass

    label("Function_42_3F3B")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4002")

    #C0086
    ChrTalk(
        0x101,
        "#00005Fこの赤い導力ボートは……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#00101Fええ、アリオスさんが\x01",
            "乗ってきたものでおそらく\x01",
            "間違いないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00003F……とにかく、\x01",
            "急いで後を追いかけないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4038")

    label("loc_4002")

    SetChrName("")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赤い導力ボートが停泊している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4038")

    EventEnd(0x3)
    Return()

    # Function_42_3F3B end

    SaveToFile()

Try(main)
