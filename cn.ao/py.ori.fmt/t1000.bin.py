from ScenarioHelper import *

def main():
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
        "游客",                   # 1
        "游客",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "萨尔莎乘务员",           # 7
        "莉夏",                   # 8
        "琪雅",                   # 9
        "芙兰",                   # 10
        "塞茜尔",                 # 11
        "伊莉娅",                 # 12
        "修利",                   # 13
        "玛丽亚贝尔",             # 14
        "蔡特",                   # 15
        "水上巴士",               # 16
        "乘客",                   # 17
        "乘客",                   # 18
        "乘客",                   # 19
        "乘客",                   # 20
        "乘客",                   # 21
        "乘客",                   # 22
        "乘客",                   # 23
        "乘客",                   # 24
        "SE控制",                 # 25
        "船",                     # 26
        "船",                     # 27
        "主题公园方向",           # 28
        "宅邸方向",               # 29
        "湖水浴场方向",           # 30
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

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "主题公园方向")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "宅邸方向")
    PlaceName(75.0, 0.0, 15.0, 0x0000, 0x0000, "湖水浴场方向")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ChipFrameInfo(1296, 0)                                       # 0

    ScpFunction((
        "Function_0_510",          # 00, 0
        "Function_1_5C0",          # 01, 1
        "Function_2_5EB",          # 02, 2
        "Function_3_721",          # 03, 3
        "Function_4_8DF",          # 04, 4
        "Function_5_964",          # 05, 5
        "Function_6_9EE",          # 06, 6
        "Function_7_A58",          # 07, 7
        "Function_8_AD2",          # 08, 8
        "Function_9_BA1",          # 09, 9
        "Function_10_C15",         # 0A, 10
        "Function_11_CA3",         # 0B, 11
        "Function_12_D28",         # 0C, 12
        "Function_13_10F9",        # 0D, 13
        "Function_14_1144",        # 0E, 14
        "Function_15_120C",        # 0F, 15
        "Function_16_2A13",        # 10, 16
        "Function_17_2A7B",        # 11, 17
        "Function_18_2AAF",        # 12, 18
        "Function_19_2AEF",        # 13, 19
        "Function_20_2B2F",        # 14, 20
        "Function_21_2B6F",        # 15, 21
        "Function_22_2BAF",        # 16, 22
        "Function_23_2BEF",        # 17, 23
        "Function_24_2C2F",        # 18, 24
        "Function_25_2C6F",        # 19, 25
        "Function_26_2C85",        # 1A, 26
        "Function_27_325E",        # 1B, 27
        "Function_28_335C",        # 1C, 28
        "Function_29_3414",        # 1D, 29
        "Function_30_3429",        # 1E, 30
        "Function_31_3489",        # 1F, 31
        "Function_32_34D7",        # 20, 32
        "Function_33_3525",        # 21, 33
        "Function_34_3573",        # 22, 34
        "Function_35_35C1",        # 23, 35
        "Function_36_3615",        # 24, 36
        "Function_37_39A8",        # 25, 37
        "Function_38_39FD",        # 26, 38
        "Function_39_3A22",        # 27, 39
        "Function_40_3B2A",        # 28, 40
        "Function_41_3B50",        # 29, 41
        "Function_42_3BE1",        # 2A, 42
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
    Jump("loc_9EA")

    label("loc_975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9E1")

    #C0001
    ChrTalk(
        0x8,
        (
            "好啦，一边眺望湖面，\x01",
            "一边等待也是一种乐趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "逛得也已经有些累了，\x01",
            "就在这里等一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EA")

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9EA")

    label("loc_9EA")

    TalkEnd(0xFE)
    Return()

    # Function_5_964 end

    def Function_6_9EE(): pass

    label("Function_6_9EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9FF")
    Jump("loc_A54")

    label("loc_9FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A4B")

    #C0003
    ChrTalk(
        0x9,
        (
            "水上巴士\x01",
            "还没来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "早知如此，\x01",
            "真该多玩一段时间啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A54")

    label("loc_A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A54")

    label("loc_A54")

    TalkEnd(0xFE)
    Return()

    # Function_6_9EE end

    def Function_7_A58(): pass

    label("Function_7_A58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A69")
    Jump("loc_ACE")

    label("loc_A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A77")
    Jump("loc_ACE")

    label("loc_A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_ACE")

    #C0005
    ChrTalk(
        0xA,
        "老公，你可真是的……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xA,
        (
            "我们马上就要上船了，\x01",
            "别说这种让人\x01",
            "不安的话啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACE")

    TalkEnd(0xFE)
    Return()

    # Function_7_A58 end

    def Function_8_AD2(): pass

    label("Function_8_AD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_AE3")
    Jump("loc_B9D")

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B3E")

    #C0007
    ChrTalk(
        0xB,
        (
            "真不想离开这\x01",
            "热闹的米修拉姆啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        "这里真是个好地方，让人心情愉快……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9D")

    label("loc_B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B9D")

    #C0009
    ChrTalk(
        0xB,
        (
            "那个……没把什么东西\x01",
            "忘在酒店里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "应该……没有吧。\x01",
            "………………大概没有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9D")

    TalkEnd(0xFE)
    Return()

    # Function_8_AD2 end

    def Function_9_BA1(): pass

    label("Function_9_BA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BB2")
    Jump("loc_C11")

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BC0")
    Jump("loc_C11")

    label("loc_BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C11")

    #C0011
    ChrTalk(
        0xC,
        (
            "我和男朋友\x01",
            "走散了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xC,
        (
            "真是的～再不快点来，\x01",
            "我就一个人先回去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C11")

    TalkEnd(0xFE)
    Return()

    # Function_9_BA1 end

    def Function_10_C15(): pass

    label("Function_10_C15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C26")
    Jump("loc_C9F")

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C34")
    Jump("loc_C9F")

    label("loc_C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C9F")

    #C0013
    ChrTalk(
        0xD,
        (
            "我女朋友一个人\x01",
            "走掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xD,
        (
            "唉～她到底跑到什么地方去了。\x01",
            "必须要在水上巴士出发之前找到她……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9F")

    TalkEnd(0xFE)
    Return()

    # Function_10_C15 end

    def Function_11_CA3(): pass

    label("Function_11_CA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_CB4")
    Jump("loc_D24")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CC2")
    Jump("loc_D24")

    label("loc_CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D1B")

    #C0015
    ChrTalk(
        0xE,
        (
            "前往克洛斯贝尔码头\x01",
            "的水上巴士\x01",
            "即将出发。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xE,
        (
            "如需搭乘，\x01",
            "请抓紧时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D24")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_D24")

    label("loc_D24")

    TalkEnd(0xFE)
    Return()

    # Function_11_CA3 end

    def Function_12_D28(): pass

    label("Function_12_D28")

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
        "#01803F…………呼…………\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#12P#00005F……莉夏，\x01",
            "你在这种地方啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x5A, 0x1F4)

    #C0019
    ChrTalk(
        0xF,
        "#01805F罗伊德警官、小琪雅……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x153,
        (
            "#01105F莉夏，\x01",
            "你好像无精打采的。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#12P#00000F有什么烦心事吗？\x01",
            "如果愿意，可以和我……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xF,
        (
            "#01809F啊，不不，没什么大事……\x02\x03",

            "#01804F那个……只是觉得欢乐街\x01",
            "之外的地方也如此喧嚣，\x01",
            "稍微有些疲惫。\x02\x03",

            "#01802F不过，在这里吹了一阵风之后，\x01",
            "已经放松很多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#12P#00003F……是吗，那就好。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x153,
        "#01108F莉夏，你真的不要紧吗？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xF,
        (
            "#01809F嗯，已经没事了。\x02\x03",

            "#01803F罗伊德警官，\x01",
            "我这就回去找\x01",
            "伊莉娅小姐她们了。\x02\x03",

            "#01802F稍后会和大家\x01",
            "一起去集合地点，\x01",
            "请不必担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#12P#00005F啊，嗯……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xF, 0x40)
    OP_68(-7800, -800, -26950, 4000)
    BeginChrThread(0xF, 3, 0, 13)
    Sleep(300)

    def lambda_101C():

        label("loc_101C")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_101C")

    QueueWorkItem2(0x101, 2, lambda_101C)

    def lambda_102E():

        label("loc_102E")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_102E")

    QueueWorkItem2(0x153, 2, lambda_102E)
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
        "#01105F怎么了？罗伊德。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    #C0028
    ChrTalk(
        0x101,
        (
            "#6P#00003F……没什么。\x02\x03",

            "#00000F我们也该走啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x15A, 5)
    SetChrPos(0x0, -8850, -2000, -26600, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_D28 end

    def Function_13_10F9(): pass

    label("Function_13_10F9")

    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_1105():
        OP_95(0xFE, -8610, -2000, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1105)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x0)

    def lambda_112A():
        OP_95(0xFE, -610, -2000, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_112A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_10F9 end

    def Function_14_1144(): pass

    label("Function_14_1144")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0029
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1207")
    OP_E2(0x2)
    MiniGame(0x6, 0x5, 0x5B9A, 0xFFFFEC78, 0xFFFF296E, 0x5A, 0x72C4, 0xFFFFE890, 0xFFFF277A)

    label("loc_1207")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_14_1144 end

    def Function_15_120C(): pass

    label("Function_15_120C")

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
            "#00002F#6P嗯……\x01",
            "玛丽亚贝尔小姐\x01",
            "应该会在这里等我们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00104F#11P是的，约定的时间是九点半，\x01",
            "现在应该刚好……\x02",
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
        "女孩的声音",
        "#2713V#1P#30W啊，来了来了～！\x02",
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
        "#00005F#6P这声音是……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x109,
        "#10111F#11P难、难道……！？\x02",
    )

    CloseMessageWindow()

    def lambda_1AEF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AEF)
    Sleep(50)

    def lambda_1AFF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AFF)
    Sleep(50)

    def lambda_1B0F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B0F)
    Sleep(50)

    def lambda_1B1F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B1F)
    Sleep(50)

    def lambda_1B2F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B2F)
    Sleep(50)

    def lambda_1B3F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1B3F)
    Sleep(50)

    def lambda_1B4F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1B4F)
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

    def lambda_1BBF():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BBF)
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
            "#2714V#30W姐姐，还有大家，\x01",
            "早上好～！\x02\x03",

            "#2715V#30W小琪雅，早哦～！\x02",
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
        "#01109F#6P早上好！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#00305F#6P哦哦，这不是小芙兰吗！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x109,
        (
            "#10106F#5P你、你为何会来这里……\x02\x03",

            "#10101F昨天见面的时候，\x01",
            "你一句都没和我提过啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x11,
        (
            "#06409F#11P嘿嘿，只是想给姐姐\x01",
            "和大家一个惊喜嘛～\x02\x03",

            "#06402F另外，特别嘉宾\x01",
            "可不只我一人哦～\x02",
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
        "女性的声音",
        "#1P呵呵，大家都到了啊。\x02",
    )

    CloseMessageWindow()

    #N0042
    NpcTalk(
        0x13,
        "女性的声音",
        (
            "#1P好！全员到齐了，\x01",
            "今天一定能玩个痛快～！\x02",
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
        "#00005F#6P什么！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#00105F#6P这、这声音是……\x02",
    )

    CloseMessageWindow()
    OP_68(-5400, -3000, -50350, 3000)

    def lambda_1FBF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1FBF)
    Sleep(100)

    def lambda_1FD7():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1FD7)
    Sleep(100)

    def lambda_1FEF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1FEF)
    Sleep(100)

    def lambda_2007():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2007)
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
        "#00307F#6P哦哦哦哦哦！？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x10,
        "#01110F#6P啊，是塞茜尔！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#00205F#6P连伊莉娅小姐她们都……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x105,
        (
            "#10302F#6P嘿，又来了\x01",
            "一大群美女呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#00106F#6P安、安排这种场面的人……\x02\x03",

            "#00101F贝尔，肯定是你吧！？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_215F")
    OP_C9(0x0, 0x80000000)

    #N0051
    NpcTalk(
        0x15,
        "女性的声音",
        "#3774V#1P#30W呵呵呵，回答正确。\x02",
    )

    CloseMessageWindow()
    OP_24(0xEBE)
    OP_C9(0x1, 0x80000000)
    Jump("loc_2185")

    label("loc_215F")


    #N0052
    NpcTalk(
        0x15,
        "女性的声音",
        "#1P呵呵呵，回答正确。\x02",
    )

    CloseMessageWindow()

    label("loc_2185")

    OP_68(-4680, -3000, -50240, 2500)

    def lambda_219B():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_219B)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    #C0053
    ChrTalk(
        0x101,
        (
            "#00012F#6P玛丽亚贝尔小姐……\x01",
            "这到底是怎么回事？\x02",
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
            "呵呵，在招待你们的同时，\x01",
            "也邀请了平时与你们\x01",
            "关系很亲近的各位。\x02\x03",

            "另外，彩虹剧团的诸位要在\x01",
            "下个月开始新版舞剧的公演，\x01",
            "顺便也借此机会鼓舞大家。\x02",
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
        "警察弟弟，早啊！\x02",
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
            "呵呵，\x01",
            "好久不见了。\x02",
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
        "为、为何连我都要……\x02",
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
            "#00012F#6P哈哈……\x01",
            "该说什么才好呢……\x02\x03",

            "#00002F塞茜尔姐姐，你得到休假了？\x02",
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
            "嗯，偶然得到休假，\x01",
            "又正好接到伊莉娅的联络……\x02\x03",

            "因为听说你们也会来，\x01",
            "所以就接受了她的邀请。\x02\x03",

            "没给大家添麻烦吧？\x02",
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
        "#00009F#6P当然没有……我很高兴呢。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#00307F#6P噢噢噢噢噢！\x01",
            "我难道是在做梦吗！？\x02\x03",

            "#00306F不仅有塞茜尔小姐和伊莉娅小姐，\x01",
            "还有这么多美人……\x02\x03",

            "#00309F呀哈哈！\x01",
            "情绪高涨到了顶点～！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        "#00211F#5P兰迪前辈，你好吵啊。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        "#10304F#6P呼，但也可以理解他的心情。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#10112F#6P话说回来，真是有些吃惊呢……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#00102F#6P住宿方面……莫非也把\x01",
            "我们安排到了同一家酒店？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x15,
        (
            "#02904F#11P嗯，各位的房间\x01",
            "都在酒店三层的\x01",
            "贵宾区。\x02\x03",

            "我先带大家去房间\x01",
            "把行李放下吧。\x02\x03",

            "#02902F之后，你们可以去米修拉姆\x01",
            "新开业的招牌景点享受一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        "#00105F#6P新开业的招牌景点……？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#00205F#6P不是主题公园吗？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x11,
        (
            "#06409F#11P嘿嘿嘿，我当时听到之后，\x01",
            "真是大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xF,
        (
            "#01802F#11P听说有个刚开放\x01",
            "不久的新区域……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x13,
        (
            "#01709F#11P在中午之前，\x01",
            "好像包场给我们专用了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x15,
        (
            "#02904F#11P嗯，请大家\x01",
            "一定要尽情享受。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x10,
        "#01105F#6P嗯嗯……？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00005F#6P那个……\x01",
            "所谓的新区域究竟是……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x15,
        (
            "#02912F#11P呵呵……\x01",
            "那是专为处于内陆地区的\x01",
            "克洛斯贝尔而建造的乐园……\x02\x03",

            "#02909F临接美丽的艾鲁姆湖\x01",
            "的纯白『湖水浴场』。\x02",
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

    # Function_15_120C end

    def Function_16_2A13(): pass

    label("Function_16_2A13")

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

    # Function_16_2A13 end

    def Function_17_2A7B(): pass

    label("Function_17_2A7B")


    def lambda_2A80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A80)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0xFFA6, 0x3A98, 0x9C4, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_2A7B end

    def Function_18_2AAF(): pass

    label("Function_18_2AAF")


    def lambda_2AB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AB4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7250, -4000, -52000, 2500, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_2AAF end

    def Function_19_2AEF(): pass

    label("Function_19_2AEF")


    def lambda_2AF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AF4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -6250, -4000, -49500, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_2AEF end

    def Function_20_2B2F(): pass

    label("Function_20_2B2F")


    def lambda_2B34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B34)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7250, -4000, -50000, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_2B2F end

    def Function_21_2B6F(): pass

    label("Function_21_2B6F")


    def lambda_2B74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B74)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -8750, -4000, -51000, 2500, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_2B6F end

    def Function_22_2BAF(): pass

    label("Function_22_2BAF")


    def lambda_2BB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BB4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -7750, -4000, -48500, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_2BAF end

    def Function_23_2BEF(): pass

    label("Function_23_2BEF")


    def lambda_2BF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BF4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -8750, -4000, -49000, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_2BEF end

    def Function_24_2C2F(): pass

    label("Function_24_2C2F")


    def lambda_2C34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C34)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x9C4, 0x1)
    OP_95(0xFE, -6250, -4000, -51500, 2500, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_2C2F end

    def Function_25_2C6F(): pass

    label("Function_25_2C6F")

    Sound(475, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Sound(476, 0, 100, 0)
    Return()

    # Function_25_2C6F end

    def Function_26_2C85(): pass

    label("Function_26_2C85")

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
        "#00201F#11P#N是钟声……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3021")

    #C0077
    ChrTalk(
        0x101,
        (
            "#00011F#5P#N这是……\x01",
            "『镜之城』最上层的那口钟发出的……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0078
    ChrTalk(
        0x102,
        "#00101F#5P#N嗯……应该没错。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_308A")

    label("loc_3021")


    #C0079
    ChrTalk(
        0x102,
        (
            "#00101F#5P#N这是……\x01",
            "『镜之城』最上层的那口钟发出的……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0080
    ChrTalk(
        0x101,
        "#00001F#5P#N还有那种东西吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_308A")


    #C0081
    ChrTalk(
        0x104,
        (
            "#00306F#5P#N竟然连水面\x01",
            "都在隐隐发光……\x02\x03",

            "#00301F阿缇，能感觉到什么吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0082
    ChrTalk(
        0x103,
        (
            "#00203F#11P#N类似『灵压』的气场\x01",
            "似乎正在不断提升……\x02\x03",

            "#00201F这种感觉是从里面的\x01",
            "主题公园方向传来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00003F#5P#N是吗……\x02\x03",

            "#00013F看来亚里欧斯先生\x01",
            "很可能带琪雅去了那里。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0084
    ChrTalk(
        0x102,
        "#00107F#5P#N嗯……我们过去看看吧！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_321F")
    Jump("loc_3224")

    label("loc_321F")

    OP_29(0x94, 0x4, 0x40)

    label("loc_3224")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3235")
    Jump("loc_323A")

    label("loc_3235")

    OP_29(0x95, 0x4, 0x40)

    label("loc_323A")

    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_32(0xFF, 0xFF, 0x0)
    OP_66(0x2, 0x1)
    OP_24(0x1E3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_26_2C85 end

    def Function_27_325E(): pass

    label("Function_27_325E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_335B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B7")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("loc_3356")

    label("loc_32B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3305")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_3356")

    label("loc_3305")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3353")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 0, -5500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("loc_3356")

    label("loc_3353")

    Sleep(233)

    label("loc_3356")

    Jump("Function_27_325E")

    label("loc_335B")

    Return()

    # Function_27_325E end

    def Function_28_335C(): pass

    label("Function_28_335C")

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

    # Function_28_335C end

    def Function_29_3414(): pass

    label("Function_29_3414")

    OP_96(0xFE, 0x445C, 0xFFFFEE08, 0xFFFF1C76, 0x7D0, 0x0)
    Return()

    # Function_29_3414 end

    def Function_30_3429(): pass

    label("Function_30_3429")

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

    # Function_30_3429 end

    def Function_31_3489(): pass

    label("Function_31_3489")

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

    # Function_31_3489 end

    def Function_32_34D7(): pass

    label("Function_32_34D7")

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

    # Function_32_34D7 end

    def Function_33_3525(): pass

    label("Function_33_3525")

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

    # Function_33_3525 end

    def Function_34_3573(): pass

    label("Function_34_3573")

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

    # Function_34_3573 end

    def Function_35_35C1(): pass

    label("Function_35_35C1")

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

    # Function_35_35C1 end

    def Function_36_3615(): pass

    label("Function_36_3615")

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

    def lambda_38B6():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_38B6)
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

    # Function_36_3615 end

    def Function_37_39A8(): pass

    label("Function_37_39A8")


    def lambda_39AD():
        OP_95(0xFE, -7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39AD)
    Sleep(500)

    def lambda_39CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39CA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_39E3():
        OP_95(0xFE, 7250, -4000, -50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39E3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_37_39A8 end

    def Function_38_39FD(): pass

    label("Function_38_39FD")

    Sleep(1000)
    Sound(475, 0, 100, 0)
    Sleep(1500)
    Sound(477, 0, 100, 0)
    Sleep(4000)
    Sound(476, 0, 100, 0)
    Sleep(1000)
    Sound(477, 0, 100, 0)
    Return()

    # Function_38_39FD end

    def Function_39_3A22(): pass

    label("Function_39_3A22")

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

    def lambda_3ADE():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3ADE)
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

    # Function_39_3A22 end

    def Function_40_3B2A(): pass

    label("Function_40_3B2A")

    Sleep(1000)

    label("loc_3B2D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B4F")
    Sound(918, 0, 30, 0)
    Sleep(2200)
    Sound(918, 0, 20, 0)
    Sleep(5000)
    Jump("loc_3B2D")

    label("loc_3B4F")

    Return()

    # Function_40_3B2A end

    def Function_41_3B50(): pass

    label("Function_41_3B50")

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
            "前往『克洛斯贝尔市』的水上巴士·时刻表\x01\x01",
            "　　　　※期待着您的下次光临！\x01",
            "　            \x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_41_3B50 end

    def Function_42_3BE1(): pass

    label("Function_42_3BE1")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C7A")

    #C0086
    ChrTalk(
        0x101,
        "#00005F这艘红色的导力艇是……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#00101F嗯，恐怕正是\x01",
            "亚里欧斯先生\x01",
            "开来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00003F……总之，我们一定要\x01",
            "尽快追上他。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3CAA")

    label("loc_3C7A")

    SetChrName("")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "停泊着一艘红色的导力艇。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3CAA")

    EventEnd(0x3)
    Return()

    # Function_42_3BE1 end

    SaveToFile()

Try(main)
