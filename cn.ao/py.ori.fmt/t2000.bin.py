from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2000.bin",                # FileName
        "t2000",                    # MapName
        "t2000",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\x02',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 24450, 0, -890, 0, 0, 1, 89, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2000",                  # 0
        "卡塔队员",               # 1
        "罗金斯队员",             # 2
        "罗梅奥队员",             # 3
        "游客",                   # 4
        "巴士",                   # 5
        "特别任务支援科车辆",     # 6
        "飙车族",                 # 7
        "米蕾优三尉",             # 8
        "旅行者",                 # 9
        "旅行者",                 # 10
        "旅行者",                 # 11
        "旅行者",                 # 12
        "旅行者",                 # 13
        "旅行者",                 # 14
        "国防军士兵",             # 15
        "国防军士兵",             # 16
        "国防军士兵",             # 17
        "国防军士兵",             # 18
        "新型装甲车",             # 19
        "西克洛斯贝尔街道",       # 20
    ))

    AddCharChip((
        "chr/ch32600.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch31300.itc",                   # 02
        "chr/ch33200.itc",                   # 03
        "chr/ch41400.itc",                   # 04
        "chr/ch41500.itc",                   # 05
    ))

    DeclNpc(22430,   0,       4730,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(22239,   0,       -5489,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(13550,   0,       26559,   270,  389,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(24790,   200,     -19389,  180,  389,  0x0, 0,   3,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
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

    DeclActor(31260,   0,       27730,   1200,    31260,   1000,    27730,   0x007C, 0,  17, 0x0000)
    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  5,  0x0000)
    DeclActor(40580,   0,       3620,    1200,    40580,   2000,    3620,    0x007C, 0,  16, 0x0000)
    DeclActor(40350,   0,       5000,    1200,    40350,   2000,    5000,    0x007C, 0,  16, 0x0000)
    DeclActor(18980,   200,     -11720,  1200,    18980,   1700,    -11720,  0x007C, 0,  47, 0x0000)

    PlaceName(73.0, 0.0, -4.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(5.0, 0.0, -0.800000011920929, 0x0000, 0x0052, "")
    PlaceName(30.850000381469727, 0.0, 27.90999984741211, 0x0000, 0x0055, "")

    ChipFrameInfo(1136, 0)                                       # 0

    ScpFunction((
        "Function_0_470",          # 00, 0
        "Function_1_520",          # 01, 1
        "Function_2_54B",          # 02, 2
        "Function_3_577",          # 03, 3
        "Function_4_C67",          # 04, 4
        "Function_5_E1A",          # 05, 5
        "Function_6_F55",          # 06, 6
        "Function_7_1015",         # 07, 7
        "Function_8_1142",         # 08, 8
        "Function_9_1193",         # 09, 9
        "Function_10_1227",        # 0A, 10
        "Function_11_1318",        # 0B, 11
        "Function_12_1FA9",        # 0C, 12
        "Function_13_2197",        # 0D, 13
        "Function_14_2D65",        # 0E, 14
        "Function_15_2E8B",        # 0F, 15
        "Function_16_2F61",        # 10, 16
        "Function_17_328E",        # 11, 17
        "Function_18_32C8",        # 12, 18
        "Function_19_362C",        # 13, 19
        "Function_20_3990",        # 14, 20
        "Function_21_39E3",        # 15, 21
        "Function_22_3A36",        # 16, 22
        "Function_23_3A4D",        # 17, 23
        "Function_24_44CB",        # 18, 24
        "Function_25_45D2",        # 19, 25
        "Function_26_48F3",        # 1A, 26
        "Function_27_58B2",        # 1B, 27
        "Function_28_59D2",        # 1C, 28
        "Function_29_5A4D",        # 1D, 29
        "Function_30_5AD4",        # 1E, 30
        "Function_31_5AFE",        # 1F, 31
        "Function_32_5B58",        # 20, 32
        "Function_33_5B9D",        # 21, 33
        "Function_34_5BB9",        # 22, 34
        "Function_35_5BD5",        # 23, 35
        "Function_36_5BF1",        # 24, 36
        "Function_37_5C0D",        # 25, 37
        "Function_38_5C29",        # 26, 38
        "Function_39_5C6B",        # 27, 39
        "Function_40_5C8A",        # 28, 40
        "Function_41_5CA9",        # 29, 41
        "Function_42_5CC8",        # 2A, 42
        "Function_43_5CE7",        # 2B, 43
        "Function_44_5E00",        # 2C, 44
        "Function_45_710E",        # 2D, 45
        "Function_46_724B",        # 2E, 46
        "Function_47_7388",        # 2F, 47
    ))


    def Function_0_470(): pass

    label("Function_0_470")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4A8"),
        (1, "loc_4B4"),
        (2, "loc_4C0"),
        (3, "loc_4CC"),
        (4, "loc_4D8"),
        (5, "loc_4E4"),
        (6, "loc_4F0"),
        (SWITCH_DEFAULT, "loc_4FC"),
    )


    label("loc_4A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_508")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_51F")

    Return()

    # Function_0_470 end

    def Function_1_520(): pass

    label("Function_1_520")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54A")
    OP_94(0xFE, 0x60D6, 0xFFFFB442, 0x7346, 0xFFFFC888, 0x3E8)
    Sleep(400)
    Jump("Function_1_520")

    label("loc_54A")

    Return()

    # Function_1_520 end

    def Function_2_54B(): pass

    label("Function_2_54B")

    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570")
    ClearMapObjFlags(0x8, 0x2000000)
    Jump("loc_576")

    label("loc_570")

    ClearMapObjFlags(0x2, 0x2000000)

    label("loc_576")

    Return()

    # Function_2_54B end

    def Function_3_577(): pass

    label("Function_3_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_58D")
    SetChrChipByIndex(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x5)
    Jump("loc_641")

    label("loc_58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5A5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_641")

    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B3")
    Jump("loc_641")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E8")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x40)
    SetChrPos(0xF, 13370, 0, 26130, 270)

    label("loc_5E8")

    Jump("loc_641")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5FB")
    Jump("loc_641")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_609")
    Jump("loc_641")

    label("loc_609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_625")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_END)), "loc_620")
    ClearChrFlags(0xA, 0x80)

    label("loc_620")

    Jump("loc_641")

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_633")
    Jump("loc_641")

    label("loc_633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_641")
    ClearChrFlags(0xB, 0x80)

    label("loc_641")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    SetScenarioFlags(0x38, 0)

    label("loc_6CE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4")
    SetScenarioFlags(0x38, 1)

    label("loc_6E4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FA")
    SetScenarioFlags(0x38, 2)

    label("loc_6FA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_710")
    SetScenarioFlags(0x38, 3)

    label("loc_710")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_726")
    SetScenarioFlags(0x38, 4)

    label("loc_726")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C")
    SetScenarioFlags(0x38, 5)

    label("loc_73C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    SetScenarioFlags(0x38, 6)

    label("loc_752")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768")
    SetScenarioFlags(0x38, 7)

    label("loc_768")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77E")
    SetScenarioFlags(0x39, 0)

    label("loc_77E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_794")
    SetScenarioFlags(0x39, 1)

    label("loc_794")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA")
    SetScenarioFlags(0x39, 2)

    label("loc_7AA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C0")
    SetScenarioFlags(0x39, 3)

    label("loc_7C0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    SetScenarioFlags(0x39, 4)

    label("loc_7D6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EC")
    SetScenarioFlags(0x39, 5)

    label("loc_7EC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_802")
    SetScenarioFlags(0x39, 6)

    label("loc_802")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_818")
    SetScenarioFlags(0x39, 7)

    label("loc_818")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82E")
    SetScenarioFlags(0x3A, 0)

    label("loc_82E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_844")
    SetScenarioFlags(0x3A, 1)

    label("loc_844")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85A")
    SetScenarioFlags(0x3A, 2)

    label("loc_85A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_870")
    SetScenarioFlags(0x3A, 3)

    label("loc_870")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_886")
    SetScenarioFlags(0x3A, 4)

    label("loc_886")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C")
    SetScenarioFlags(0x3A, 5)

    label("loc_89C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B2")
    SetScenarioFlags(0x3A, 6)

    label("loc_8B2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C8")
    SetScenarioFlags(0x3A, 7)

    label("loc_8C8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DE")
    SetScenarioFlags(0x3B, 0)

    label("loc_8DE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F4")
    SetScenarioFlags(0x3B, 1)

    label("loc_8F4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A")
    SetScenarioFlags(0x3B, 2)

    label("loc_90A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_920")
    SetScenarioFlags(0x3B, 3)

    label("loc_920")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_936")
    SetScenarioFlags(0x3B, 4)

    label("loc_936")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94C")
    SetScenarioFlags(0x3B, 5)

    label("loc_94C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_962")
    SetScenarioFlags(0x3B, 6)

    label("loc_962")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_978")
    SetScenarioFlags(0x3B, 7)

    label("loc_978")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98E")
    SetScenarioFlags(0x3D, 5)

    label("loc_98E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A4")
    SetScenarioFlags(0x3D, 6)

    label("loc_9A4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BA")
    SetScenarioFlags(0x3D, 7)

    label("loc_9BA")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F5")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_AE5")

    label("loc_9F5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A18")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_AE5")

    label("loc_A18")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3B")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_AE5")

    label("loc_A3B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5E")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_AE5")

    label("loc_A5E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A81")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_AE5")

    label("loc_A81")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA4")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_AE5")

    label("loc_AA4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC7")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_AE5")

    label("loc_AC7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    SetScenarioFlags(0x3C, 7)

    label("loc_AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFB")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2D")
    SetChrPos(0x0, 40630, 0, 3050, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 9)

    label("loc_B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_B60")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B60")
    SetChrPos(0x0, 40350, 0, 5000, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_B8A")
    ClearScenarioFlags(0x3E, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B87")
    Event(0, 44)
    Jump("loc_B8A")

    label("loc_B87")

    Event(0, 8)

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_BA3")
    ClearScenarioFlags(0x22, 2)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_BC0")

    label("loc_BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_BC0")
    ClearScenarioFlags(0x22, 3)
    SetChrPos(0x0, 39720, 0, 2910, 135)

    label("loc_BC0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE9")
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_C66")

    label("loc_BE9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")
    Event(0, 18)
    Jump("loc_C66")

    label("loc_C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3A")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_C3A")

    Jump("loc_C66")

    label("loc_C3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    Event(0, 45)
    Jump("loc_C66")

    label("loc_C55")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C66")
    Event(0, 46)

    label("loc_C66")

    Return()

    # Function_3_577 end

    def Function_4_C67(): pass

    label("Function_4_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C83")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C95")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_C95")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D19")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xC8, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_D30")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_D30")

    label("loc_D30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D56")
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    Jump("loc_D69")

    label("loc_D56")

    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DA6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D93")
    SetMapObjFrame(0x8, "mark00", 0x0, 0x1)
    Jump("loc_DA1")

    label("loc_D93")

    SetMapObjFrame(0x2, "mark00", 0x0, 0x1)

    label("loc_DA1")

    Jump("loc_DD5")

    label("loc_DA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC7")
    SetMapObjFrame(0x8, "mark01", 0x0, 0x1)
    Jump("loc_DD5")

    label("loc_DC7")

    SetMapObjFrame(0x2, "mark01", 0x0, 0x1)

    label("loc_DD5")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xC, 0x80)
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E15")
    OP_70(0x4, 0x0)
    Jump("loc_E19")

    label("loc_E15")

    OP_70(0x4, 0x1E)

    label("loc_E19")

    Return()

    # Function_4_C67 end

    def Function_5_E1A(): pass

    label("Function_5_E1A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0C")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('狙击枪管', 1)"), scpexpr(EXPR_END)), "loc_E9D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_F07")

    label("loc_E9D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F07")

    Jump("loc_F49")

    label("loc_F0C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F49")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E1A end

    def Function_6_F55(): pass

    label("Function_6_F55")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市西出口\x01",          # 0
            "停靠站（警察学校附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FED")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_100D")

    label("loc_FED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100D")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_100D")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_F55 end

    def Function_7_1015(): pass

    label("Function_7_1015")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_113E")
    Fade(500)
    OP_68(27670, 1000, 21230, 0)
    MoveCamera(319, 34, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, 32119, 0, 25500, 270)
    SetChrPos(0x1, 32119, 0, 24000, 270)
    SetChrPos(0x2, 32119, 0, 22500, 270)
    SetChrPos(0x3, 32119, 0, 21000, 270)
    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xC)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, 27000, 0, 10810, 0)
    OP_D5(0xC, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)

    def lambda_10F5():
        OP_95(0xFE, 27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10F5)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_71(0x3, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x3)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_113E")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_1015 end

    def Function_8_1142(): pass

    label("Function_8_1142")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, 31190, 0, 26620, 270)
    OP_31(0x1)
    OP_68(31190, 1000, 26620, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_8_1142 end

    def Function_9_1193(): pass

    label("Function_9_1193")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_11EE")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11E3")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_11E9")

    label("loc_11E3")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_11E9")

    Jump("loc_1212")

    label("loc_11EE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_120C")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_1212")

    label("loc_120C")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_1212")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1193 end

    def Function_10_1227(): pass

    label("Function_10_1227")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1247")
    Call(0, 23)
    Return()

    label("loc_1247")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1258")
    Jump("loc_1314")

    label("loc_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1266")
    Jump("loc_1314")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12FD")

    #C0005
    ChrTalk(
        0xF,
        (
            "#07900F多亏有你们协助，\x01",
            "总算制止了那些飙车族。\x02\x03",

            "#07904F这样一来，我们暂时就可以\x01",
            "把全副精力都集中在边境警备上了。\x01",
            "真的太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1314")

    label("loc_12FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_130B")
    Jump("loc_1314")

    label("loc_130B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1314")

    label("loc_1314")

    TalkEnd(0xFE)
    Return()

    # Function_10_1227 end

    def Function_11_1318(): pass

    label("Function_11_1318")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150F")

    #N0006
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "哦哦，兰迪，是你们啊，\x01",
            "好像已经很久没见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00302F哟，卡塔，\x01",
            "贝尔加德门的状况如何？\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "……老实说，\x01",
            "因为发生了那种事情，\x01",
            "现正处于严重混乱中。\x02",
        )
    )

    CloseMessageWindow()

    #N0009
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "我们正在依照司令的指示，\x01",
            "严密警戒帝国军的\x01",
            "侵略行为。\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "不过，帝国的内战还在持续，\x01",
            "短时间内应该不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        (
            "#00104F是吗……\x01",
            "总算可以稍微安下心来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#00300F你们今后应该也会很辛苦……\x01",
            "总之就多多加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0013
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "嗯，放心吧，\x01",
            "我们一定会展现出\x01",
            "国防军成员的骨气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 1)
    Jump("loc_16A9")

    label("loc_150F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1606")

    #N0014
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "独立宣言被认定为无效，\x01",
            "连国防长官都不见踪影……\x01",
            "国防军目前已经陷入严重混乱。\x02",
        )
    )

    CloseMessageWindow()

    #N0015
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "不过……多亏有司令的指示，\x01",
            "我们至少不会迷失目标。\x02",
        )
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "身为守卫克洛斯贝尔的国防军，\x01",
            "现在正是我们必须要努力的时候。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A9")

    label("loc_1606")


    #N0017
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "独立宣言被宣布无效，\x01",
            "连国防长官都不见踪影……\x01",
            "国防军目前已经陷入严重混乱。\x02",
        )
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x8,
        "士兵卡塔",
        (
            "身为守卫克洛斯贝尔的国防军，\x01",
            "现在正是我们必须要努力的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A9")

    Jump("loc_1FA5")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1780")

    #C0019
    ChrTalk(
        0x8,
        (
            "自从发生了那起袭击事件之后，\x01",
            "克洛斯贝尔与两大国的关系相当紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "有传言说，两大国将会在近期内\x01",
            "举行大规模军事演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "这简直就像是回到了签署\x01",
            "《互不侵犯条约》之前的日子……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1800")

    label("loc_1780")


    #C0022
    ChrTalk(
        0x8,
        (
            "自从发生了那起袭击事件之后，\x01",
            "克洛斯贝尔与两大国的关系相当紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "这简直就像是回到了签署\x01",
            "《互不侵犯条约》之前的日子……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1800")

    Jump("loc_1FA5")

    label("loc_1805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_197D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A5")

    #C0024
    ChrTalk(
        0x8,
        (
            "总算赶在天亮之前\x01",
            "把铁路抢修\x01",
            "完毕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "话说回来，昨天遇到的\x01",
            "那个可怕的怪物……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "肯定就是引发事故的\x01",
            "元凶吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1906")

    label("loc_18A5")


    #C0027
    ChrTalk(
        0x8,
        (
            "老实说，那只怪物\x01",
            "当时肯主动逃离，\x01",
            "真让我松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "那个怪物肯定是\x01",
            "引发事故的元凶吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1906")

    Jump("loc_1978")

    label("loc_190B")


    #C0029
    ChrTalk(
        0x8,
        (
            "听说你们已经截住了\x01",
            "刚才那辆狂飙的导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "哈哈，多亏你们，\x01",
            "我们的麻烦又减少了一个。\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1978")

    Jump("loc_1FA5")

    label("loc_197D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A43")

    #C0031
    ChrTalk(
        0x8,
        (
            "最近这段时间，有辆驾驶得相当\x01",
            "野蛮的导力车经常开到这附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "真是的……\x01",
            "要是引起事故可怎么办啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "边境一带的局势本来就很紧张了，\x01",
            "却还有这种不懂顾全大局的家伙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AC5")

    label("loc_1A43")


    #C0034
    ChrTalk(
        0x8,
        (
            "最近这段时间，有辆驾驶得相当\x01",
            "野蛮的导力车经常开到这附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "边境一带的局势本来就很紧张了，\x01",
            "却还有这种不懂顾全大局的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC5")

    Jump("loc_1FA5")

    label("loc_1ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA1")

    #C0036
    ChrTalk(
        0x8,
        (
            "自从迪塔市长在通商会议上发表了独立提案，\x01",
            "边境这里的局势就变得相当紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "市长的发言实在是\x01",
            "太过大胆了，\x01",
            "会造成这种结果也是必然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "总之，我必须要打起精神，\x01",
            "专心完成警备工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C1F")

    label("loc_1BA1")


    #C0039
    ChrTalk(
        0x8,
        (
            "自从迪塔市长在通商会议上发表了独立提案，\x01",
            "边境这里的局势就变得相当紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "总之，我必须要打起精神，\x01",
            "专心完成警备工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1F")

    Jump("loc_1FA5")

    label("loc_1C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3F")
    Call(0, 12)
    Jump("loc_1CCB")

    label("loc_1C3F")


    #C0041
    ChrTalk(
        0x8,
        (
            "边境大门突然接到了\x01",
            "在今天的会议过程中，\x01",
            "要提升警备等级的指示。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "道格拉斯副司令也从\x01",
            "唐古拉姆门赶了过来，\x01",
            "正在和司令商讨相关的事项。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCB")

    Jump("loc_1FA5")

    label("loc_1CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CEB")
    Call(0, 12)
    Jump("loc_1E0A")

    label("loc_1CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9E")

    #C0043
    ChrTalk(
        0x8,
        (
            "在通商会议召开期间，\x01",
            "边境大门的警备也相当严密。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "周边诸国的首脑全都\x01",
            "聚集在克洛斯贝尔……\x01",
            "稍有不慎，就可能造成国际问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "所以警备队的责任相当重大。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E0A")

    label("loc_1D9E")


    #C0046
    ChrTalk(
        0x8,
        (
            "周边诸国的首脑全都\x01",
            "聚集在克洛斯贝尔……\x01",
            "稍有不慎，就可能造成国际问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "所以警备队的责任相当重大。\x02",
    )

    CloseMessageWindow()

    label("loc_1E0A")

    Jump("loc_1FA5")

    label("loc_1E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2A")
    Call(0, 12)
    Jump("loc_1FA5")

    label("loc_1E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F4A")

    #C0048
    ChrTalk(
        0x8,
        (
            "我们的队员在教团事件中被骗，误服下了\x01",
            "那种药物，留下的后遗症真是相当严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "由于身体机能被超负荷消耗，\x01",
            "导致全身都剧痛无比，\x01",
            "完全动弹不得。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "所以司令才会叫来兰迪，\x01",
            "带领大家进行\x01",
            "包含实战在内的复健训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "多亏兰迪的帮忙，大家才能顺利复原。\x01",
            "实在是太感谢了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FA5")

    label("loc_1F4A")


    #C0052
    ChrTalk(
        0x8,
        "复健训练时受到兰迪不少照顾。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "多亏兰迪的帮忙，大家才能顺利复原。\x01",
            "实在是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA5")

    TalkEnd(0xFE)
    Return()

    # Function_11_1318 end

    def Function_12_1FA9(): pass

    label("Function_12_1FA9")


    #C0054
    ChrTalk(
        0x8,
        (
            "这里是边境大门——贝尔加德门，\x01",
            "如果想前往帝国，\x01",
            "请在里面接受检查。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 500)

    #C0055
    ChrTalk(
        0x8,
        "……啊，这不是兰迪吗。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        "#00309F哟，今天也在精力十足地值勤啊。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        "哈哈，是啊，我们这里还是老样子。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "复健训练那时候，\x01",
            "真是受到你不少照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "多亏你的帮忙，大家才能顺利复原。\x01",
            "请容我再次表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#00302F哈，别这么客气。\x01",
            "那毕竟是新司令阁下\x01",
            "亲自向我下达的指示。\x02\x03",

            "#00309F如果以后还想锻炼一番，\x01",
            "随时都可以叫我过来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "别……饶了我吧，\x01",
            "我再也不想接受那种训练了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 5)
    OP_93(0x8, 0x5A, 0x0)
    Return()

    # Function_12_1FA9 end

    def Function_13_2197(): pass

    label("Function_13_2197")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_230E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2282")

    #N0062
    NpcTalk(
        0x9,
        "士兵罗金斯",
        (
            "看到湿地方向突然出现了\x01",
            "一棵巨大树木时，\x01",
            "我真是吓了一大跳。\x02",
        )
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0x9,
        "士兵罗金斯",
        (
            "再怎么看，那也不是我这种\x01",
            "普通士兵可以应对的东西。\x02",
        )
    )

    CloseMessageWindow()

    #N0064
    NpcTalk(
        0x9,
        "士兵罗金斯",
        (
            "现在还是集中精力，\x01",
            "做好国防军成员的分内工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2309")

    label("loc_2282")


    #N0065
    NpcTalk(
        0x9,
        "士兵罗金斯",
        (
            "那棵巨大的树木……\x01",
            "显然不是我这种\x01",
            "普通士兵可以应付的。\x02",
        )
    )

    CloseMessageWindow()

    #N0066
    NpcTalk(
        0x9,
        "士兵罗金斯",
        (
            "现在还是集中精力，\x01",
            "做好国防军成员的分内工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2309")

    Jump("loc_2D61")

    label("loc_230E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2452")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E6")

    #C0067
    ChrTalk(
        0x9,
        (
            "在玛因兹的那场战斗中，\x01",
            "第三中队全军覆没……\x01",
            "救援部队也伤亡惨重。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "连装甲车都被击毁了好几辆……\x01",
            "老实说，警备队这次蒙受的损失\x01",
            "简直不可计量。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "那群混蛋猎兵……\x01",
            "我绝对饶不了他们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_244D")

    label("loc_23E6")


    #C0070
    ChrTalk(
        0x9,
        (
            "在这一系列的袭击事件中，\x01",
            "警备队蒙受的损失\x01",
            "简直不可计量。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "那群混蛋猎兵……\x01",
            "我绝对饶不了他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_244D")

    Jump("loc_2D61")

    label("loc_2452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2580")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2516")

    #C0072
    ChrTalk(
        0x9,
        (
            "昨天出现的那头如同恶鬼般的巨大怪物\x01",
            "让我切身感受到了惊人的强大。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "但它似乎并不是报告中提到的\x01",
            "那种『幻兽』……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        "唔……总之，现在绝不可放松警惕。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_257B")

    label("loc_2516")


    #C0075
    ChrTalk(
        0x9,
        (
            "昨天出现的那头如同恶鬼般的巨大怪物\x01",
            "让我切身感受到了惊人的强大。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "唔……现在绝不可放松警惕。\x02",
    )

    CloseMessageWindow()

    label("loc_257B")

    Jump("loc_25DA")

    label("loc_2580")


    #C0077
    ChrTalk(
        0x9,
        (
            "真是的……\x01",
            "那些年轻人真会给别人添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "……赶快转换心情，\x01",
            "专心完成警备工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DA")

    Jump("loc_2D61")

    label("loc_25DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_26A1")

    #C0079
    ChrTalk(
        0x9,
        (
            "如果真的能实现独立，\x01",
            "我们警备队应该就能像正规军一样，\x01",
            "配置威力强大的武器装备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "虽然帝国和共和国的威胁不容忽视……\x01",
            "但为了展现我们克洛斯贝尔的荣耀，\x01",
            "真希望独立能够实现。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D61")

    label("loc_26A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2778")

    #C0081
    ChrTalk(
        0x9,
        (
            "正如宰相等人在通商会议上所说，\x01",
            "与各国的军队相比，\x01",
            "警备队显得脆弱不堪。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "但这种机制不正是由\x01",
            "帝国和共和国制定的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "如今他们竟然以此为口实，\x01",
            "向我们提出指责，实在是让人气愤。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27F4")

    label("loc_2778")


    #C0084
    ChrTalk(
        0x9,
        (
            "为了顺应帝国和共和国，\x01",
            "我们警备队只能配备\x01",
            "最基本的武装。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "这种机制不正是由\x01",
            "帝国和共和国制定的吗……\x01",
            "真是让人气愤。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F4")

    Jump("loc_2D61")

    label("loc_27F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2964")

    #C0086
    ChrTalk(
        0x9,
        (
            "要论白刃战……\x01",
            "道格拉斯副司令在\x01",
            "警备队中堪称最强者。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "如果有机会，真想和他\x01",
            "切磋一番啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        (
            "#00300F说起来，我们不久前\x01",
            "刚和道格拉斯老兄\x01",
            "切磋过一番。\x02\x03",

            "#00306F他确实是个劲敌啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 500)

    #C0089
    ChrTalk(
        0x9,
        "什么……？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "……兰迪，\x01",
            "可以和我比试一场吗？\x01",
            "我很想试试自己的实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，有这闲工夫，\x01",
            "倒不如打起精神，专心做好警备工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29FB")

    label("loc_2964")

    TurnDirection(0x9, 0x104, 0)

    #C0092
    ChrTalk(
        0x9,
        (
            "唔……说的也是，专心完成\x01",
            "现在的任务才是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        "……那么，等以后有机会时，一定要切磋一下啊。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        "#00304F好吧，如果我到时候还记得。\x02",
    )

    CloseMessageWindow()

    label("loc_29FB")

    OP_93(0x9, 0x5A, 0x0)
    Jump("loc_2D61")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AB7")

    #C0095
    ChrTalk(
        0x9,
        (
            "在米修拉姆保护首脑们的成员，\x01",
            "都是警备队中战斗能力\x01",
            "较为出众的队员。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "他们在实战演习中一直保持着\x01",
            "很好的成绩，只要有他们在，\x01",
            "首脑们的安全问题就不必担心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D61")

    label("loc_2AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD9")

    #C0097
    ChrTalk(
        0x9,
        (
            "索妮亚司令来此就任后，\x01",
            "贝尔加德门队员的士气\x01",
            "有了大幅提升。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "其证据就是，虽然大家在教团事件中\x01",
            "服下了那种奇怪的药物，但却能以\x01",
            "惊人的速度振作起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00306F嗯，和前任司令相比，\x01",
            "确实是天壤之别。\x02\x03",

            "#00300F只要能承受住那种魔鬼般的严厉要求，\x01",
            "就再也找不出比她更优秀的长官了。\x01",
            "也难怪大家这么有干劲。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "是啊……从现在起，\x01",
            "我必须要更加努力地锻炼自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "在教团那起事件中，\x01",
            "我竟然被约亚西姆·琼塔\x01",
            "控制了身体，并替他传话……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#00305F啊……说起来，\x01",
            "是有这么一回事呢。\x02\x03",

            "#00300F总之，我们就一起努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        "嗯。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D61")

    label("loc_2CD9")


    #C0104
    ChrTalk(
        0x9,
        (
            "在教团那起事件中，\x01",
            "我竟然被约亚西姆·琼塔\x01",
            "控制了身体，并替他传话……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "就算是为了挽回颜面，\x01",
            "我今后也必须要\x01",
            "更加努力地锻炼自己。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D61")

    TalkEnd(0xFE)
    Return()

    # Function_13_2197 end

    def Function_14_2D65(): pass

    label("Function_14_2D65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D76")
    Jump("loc_2E87")

    label("loc_2D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2A")

    #C0106
    ChrTalk(
        0xA,
        (
            "货运列车已经检查完毕，\x01",
            "我正在检查新型装甲车……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "唔……数量还是不对啊。\x01",
            "数来数去都少了一辆。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "车钥匙明明还在，\x01",
            "装甲车到底跑到哪里了呢……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E87")

    label("loc_2E2A")


    #C0109
    ChrTalk(
        0xA,
        (
            "唔，在警备队员的重重警戒之下，\x01",
            "自然不可能被人盗走……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        "装甲车到底跑到哪里了呢……？\x02",
    )

    CloseMessageWindow()

    label("loc_2E87")

    TalkEnd(0xFE)
    Return()

    # Function_14_2D65 end

    def Function_15_2E8B(): pass

    label("Function_15_2E8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E9C")
    Jump("loc_2F5D")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EAA")
    Jump("loc_2F5D")

    label("loc_2EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2EB8")
    Jump("loc_2F5D")

    label("loc_2EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2EC6")
    Jump("loc_2F5D")

    label("loc_2EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2ED4")
    Jump("loc_2F5D")

    label("loc_2ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EE2")
    Jump("loc_2F5D")

    label("loc_2EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F5D")

    #C0111
    ChrTalk(
        0xB,
        (
            "和卡雷利亚要塞相比，\x01",
            "这里的边境警备措施简直就是形同虚设。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xB,
        (
            "呵呵呵，这就是帝国和\x01",
            "克洛斯贝尔的巨大差别了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5D")

    TalkEnd(0xFE)
    Return()

    # Function_15_2E8B end

    def Function_16_2F61(): pass

    label("Function_16_2F61")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F93")
    SetScenarioFlags(0x31, 2)

    label("loc_2F93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2FD3")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FC8")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_2FCE")

    label("loc_2FC8")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_2FCE")

    Jump("loc_2FD9")

    label("loc_2FD3")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_2FD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3280")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_304A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_302A"),
        (SWITCH_DEFAULT, "loc_303B"),
    )


    label("loc_302A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3045")

    label("loc_303B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3045")

    Jump("loc_327B")

    label("loc_304A")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_307A")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_307A")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30A4"),
        (1, "loc_31A8"),
        (2, "loc_3239"),
        (SWITCH_DEFAULT, "loc_3271"),
    )


    label("loc_30A4")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_30D5")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_30E5")

    label("loc_30D5")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_30E5")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_313B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_313B")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315E")
    Sound(461, 0, 100, 0)

    label("loc_315E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_317E")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_318E")

    label("loc_317E")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_318E")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_2FD9")

    label("loc_31A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_321A")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_31DD")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_31F5")

    label("loc_31DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_31F0")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_31F5")

    label("loc_31F0")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_31F5")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3234")

    label("loc_321A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_322A")
    OP_AF(0xFB)
    Jump("loc_3234")

    label("loc_322A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3234")

    Jump("loc_327B")

    label("loc_3239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3252")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_326C")

    label("loc_3252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3262")
    OP_AF(0xFB)
    Jump("loc_326C")

    label("loc_3262")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_326C")

    Jump("loc_327B")

    label("loc_3271")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_327B")

    Jump("loc_2FD9")

    label("loc_3280")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_16_2F61 end

    def Function_17_328E(): pass

    label("Function_17_328E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_32C4")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力巴士已经停运了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_32C4")

    Call(0, 6)
    Return()

    # Function_17_328E end

    def Function_18_32C8(): pass

    label("Function_18_32C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 56500, -10000, -17750, 270)
    SetChrPos(0x106, 54930, -10000, -18100, 270)
    SetChrPos(0x103, 57350, -10000, -16910, 270)
    SetChrPos(0x104, 58650, -10000, -17610, 270)
    SetChrPos(0x107, 60460, -10000, -18210, 270)
    SetChrPos(0x105, 57950, -10000, -18590, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x16, 22000, 0, -4500, 90)
    SetChrPos(0x17, 22000, 0, 4500, 90)
    SetChrPos(0x18, 40000, 0, -1000, 270)
    SetChrPos(0x19, 13500, 0, 1500, 90)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x105, 0x8)
    OP_68(30000, 2600, 0, 0)
    MoveCamera(300, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(42000, 5000)

    def lambda_3449():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3449)

    def lambda_345E():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_345E)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(20000, 0, 0, 0)
    MoveCamera(295, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    OP_6F(0x79)
    OP_0D()
    PlaceName2(340, 40, "c_plac18", 0x0, 2000)
    OP_68(30000, -6000, -16300, 8000)
    MoveCamera(295, 23, 0, 8000)
    OP_6F(0x79)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x105, 0x8)
    Fade(1000)
    OP_68(34000, -9000, -18000, 0)
    MoveCamera(294, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(32000, 0)
    SetCameraDistance(26000, 3000)
    OP_9B(0x0, 0x106, 0x0, 0x36B0, 0x1388, 0x0)
    Sleep(500)
    OP_93(0x106, 0xB4, 0x1F4)
    Sleep(400)

    def lambda_3551():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3551)
    Sleep(50)

    def lambda_3569():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3569)
    Sleep(50)

    def lambda_3581():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3581)
    Sleep(50)

    def lambda_3599():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3599)
    Sleep(50)

    def lambda_35B1():
        OP_9B(0x0, 0xFE, 0x0, 0xEA60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_35B1)
    OP_93(0x106, 0x5A, 0x1F4)
    Sleep(1500)
    OP_68(34000, -7000, -18000, 6000)
    OP_93(0x106, 0x10E, 0x1F4)

    def lambda_35E8():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_35E8)
    OP_0D()
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x106, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x107, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("t2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_32C8 end

    def Function_19_362C(): pass

    label("Function_19_362C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 51930, 0, -950, 265)
    SetChrPos(0x104, 52610, 0, -1880, 265)
    SetChrPos(0x105, 52860, 0, -490, 265)
    SetChrPos(0x106, 53190, 0, -3040, 265)
    SetChrPos(0x107, 54210, 0, -1760, 265)
    SetChrPos(0x103, 53950, 0, 0, 265)
    SetChrSubChip(0x107, 0x5)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x16, 22090, 0, 4230, 90)
    SetChrPos(0x17, 22670, 0, -4790, 90)
    SetChrPos(0x18, 27780, 0, 18140, 0)
    SetChrPos(0x19, 30910, 0, 2200, 90)
    BeginChrThread(0x16, 1, 0, 0)
    BeginChrThread(0x17, 1, 0, 0)
    BeginChrThread(0x18, 1, 0, 20)
    BeginChrThread(0x19, 1, 0, 21)
    ClearChrFlags(0x1A, 0x80)
    OP_78(0x8, 0x1A)
    SetChrPos(0x1A, 23760, 100, 7200, 90)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_D5(0x1A, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(22660, 1000, 1180, 0)
    MoveCamera(313, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(19830, 0)
    FadeToBright(1000, 0)
    OP_68(26920, 1000, 190, 6000)
    MoveCamera(308, 27, 0, 6000)
    OP_6E(570, 6000)
    SetCameraDistance(34630, 6000)
    Sleep(6000)
    Fade(500)
    OP_68(52520, 1000, -1710, 0)
    MoveCamera(302, 25, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(14930, 0)
    OP_0D()

    #C0114
    ChrTalk(
        0x105,
        (
            "#10401F#12P（看来贝尔加德门的\x01",
            "  警备体制非常完善。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        "#00306F#12P（嗯，没有任何可趁之机。）\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x106,
        (
            "#10708F#6P（既然如此，我们还是\x01",
            "  就此离去为好吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#00006F#11P（嗯，是啊。）\x02",
    )

    CloseMessageWindow()
    OP_68(56150, 1000, -1420, 3000)
    MoveCamera(317, 29, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(19830, 3000)
    BeginChrThread(0x103, 1, 0, 22)
    Sleep(50)
    BeginChrThread(0x107, 1, 0, 22)
    Sleep(60)
    BeginChrThread(0x106, 1, 0, 22)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 22)
    Sleep(70)
    BeginChrThread(0x104, 1, 0, 22)
    Sleep(50)
    BeginChrThread(0x101, 1, 0, 22)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x107, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x106, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r1040", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_19_362C end

    def Function_20_3990(): pass

    label("Function_20_3990")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39E2")
    OP_95(0xFE, 27780, 0, 4550, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 27780, 0, 18140, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_20_3990")

    label("loc_39E2")

    Return()

    # Function_20_3990 end

    def Function_21_39E3(): pass

    label("Function_21_39E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A35")
    OP_95(0xFE, 30910, 0, -3330, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 30910, 0, 2200, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_21_39E3")

    label("loc_3A35")

    Return()

    # Function_21_39E3 end

    def Function_22_3A36(): pass

    label("Function_22_3A36")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_22_3A36 end

    def Function_23_3A4D(): pass

    label("Function_23_3A4D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14790, 900, 26150, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27410, 0)
    SetChrPos(0x101, 15240, 0, 25330, 270)
    SetChrPos(0x104, 15190, 0, 26760, 270)
    SetChrPos(0x102, 15590, 0, 23920, 315)
    SetChrPos(0x103, 16000, 0, 27520, 225)
    SetChrPos(0x105, 16620, 0, 26210, 270)
    SetChrPos(0x109, 16610, 0, 24810, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07900.itp")
    OP_4B(0xF, 0xFF)
    OP_93(0xF, 0x5A, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4379")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0118
    AnonymousTalk(
        0xF,
        (
            "兰迪……还有特别任务\x01",
            "支援科的各位。\x02\x03",

            "真是辛苦你们了，\x01",
            "谢谢你们特地赶来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0119
    ChrTalk(
        0x101,
        (
            "#00000F米蕾优三尉，你也辛苦了。\x02\x03",

            "#00004F为了完成抢修铁道的工作，\x01",
            "你们昨天一定十分劳累吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xF,
        (
            "#07902F是啊，幸好顺利\x01",
            "完工了……\x02\x03",

            "#07903F但直到最后也没能查到\x01",
            "那头巨大怪物的行踪。\x02\x03",

            "#07908F我今天还向在自治州内巡逻的\x01",
            "部队下达了搜索那头怪物的指示，\x01",
            "也不知道能不能有收获……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x105,
        "#10308F………………………………\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        (
            "#00303F……算啦，当时的首要\x01",
            "任务毕竟是抢修铁路。\x02\x03",

            "#00300F怪物的事情就先放在一边，\x01",
            "现在还是专心完成\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xF,
        "#07903F……嗯，说的也对。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#00100F对了，我们今天是为了\x01",
            "受理支援请求而来的。\x02\x03",

            "可以把委托内容\x01",
            "告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xF,
        (
            "#07900F嗯，好的。\x02\x03",

            "#07903F最近这段时间，有人在\x01",
            "西克洛斯贝尔街道危险驾驶……\x01",
            "也就是所谓的飙车。\x02\x03",

            "#07900F这种行为给帝国的旅行者和\x01",
            "定期巴士造成了很多麻烦。\x02\x03",

            "所以我希望各位\x01",
            "协助我们，\x01",
            "对其进行取缔。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC0")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0126
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆「取缔超速车」任务？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【已完成】\x01",        # 1
            "【未完成】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3FA7"),
        (1, "loc_3FAC"),
        (2, "loc_3FB6"),
        (SWITCH_DEFAULT, "loc_3FC0"),
    )


    label("loc_3FA7")

    Jump("loc_3FC0")

    label("loc_3FAC")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_3FC0")

    label("loc_3FB6")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_3FC0")

    label("loc_3FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4062")

    #C0127
    ChrTalk(
        0x109,
        (
            "#10103F飙车……\x01",
            "这个话题很耳熟呢。\x02\x03",

            "#10101F该不会是……\x01",
            "我们当时在市内\x01",
            "抓捕的那些青年吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        (
            "#00101F记得是叫『高贵之血』吧？\x01",
            "很有可能……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4096")

    label("loc_4062")


    #C0129
    ChrTalk(
        0x109,
        (
            "#10103F嗯……这种行为确实\x01",
            "会造成很严重的影响。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4096")


    #C0130
    ChrTalk(
        0xF,
        (
            "#07901F是啊，帝国和共和国都已经把\x01",
            "治安恶劣这个问题摆上台面了……\x02\x03",

            "#07903F如果在这种时期发生了将外国人\x01",
            "卷入其中的事故，后果可就严重了。\x02\x03",

            "#07901F更何况，昨天刚刚\x01",
            "发生过脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x105,
        (
            "#10303F原来如此，很容易使克洛斯贝尔\x01",
            "陷入更糟糕的局面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xF,
        (
            "#07900F另外，这个事件是由\x01",
            "我们和警方的公共安全科\x01",
            "联手调查的。\x02\x03",

            "由于飙车族的行驶路线\x01",
            "位于市外，因此才会\x01",
            "交给我们来处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#00000F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        (
            "#00205F那么，具体该如何\x01",
            "取缔他们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xF,
        (
            "#07903F他们会从西克洛斯贝尔\x01",
            "街道驶来，在抵达贝尔加德门\x01",
            "之后折返……\x02\x03",

            "#07900F希望你们埋伏在贝尔加德门，\x01",
            "等飙车族出现之后，\x01",
            "就驾驶导力车追捕。\x02\x03",

            "而我会在此期间内联络公共安全科，\x01",
            "让他们在西出口等着你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#00003F原来如此……两面夹击啊。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xF,
        (
            "#07900F嗯，正是。\x01",
            "……如何？你们可以帮忙吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8B, 0x1, 0x0)
    Jump("loc_4482")

    label("loc_4379")


    #C0138
    ChrTalk(
        0xF,
        (
            "#07900F飙车族会从西克洛斯贝尔\x01",
            "街道驶来，在抵达贝尔加德门\x01",
            "之后折返……\x02\x03",

            "#07903F希望你们埋伏在贝尔加德门，\x01",
            "等飙车族出现之后，\x01",
            "就驾驶导力车追捕。\x02\x03",

            "#07900F在克洛斯贝尔市西出口待命的\x01",
            "公共安全科会配合你们，\x01",
            "以两面夹击的战术将飙车族抓捕。\x02\x03",

            "……如何？你们可以帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4482")

    Call(0, 24)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xF, 0x10E, 0x0)
    OP_4C(0xF, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 15370, 0, 25960, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_3A4D end

    def Function_24_44CB(): pass

    label("Function_24_44CB")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_452E")
    Call(0, 25)
    Jump("loc_45D1")

    label("loc_452E")


    #C0139
    ChrTalk(
        0x101,
        (
            "#00006F……真抱歉，米蕾优三尉，\x01",
            "现在实在是腾不出时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xF,
        (
            "#07903F是吗……\x01",
            "那真是太遗憾了。\x02\x03",

            "#07900F即然如此，就等你们有空时\x01",
            "再来找我吧。\x02\x03",

            "拜托大家了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x178, 1)

    label("loc_45D1")

    Return()

    # Function_24_44CB end

    def Function_25_45D2(): pass

    label("Function_25_45D2")


    #C0141
    ChrTalk(
        0x101,
        (
            "#00000F明白了，\x01",
            "我们接受委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xF,
        (
            "#07902F谢谢，真是帮大忙了。\x02\x03",

            "#07903F那我这就\x01",
            "联络公共安全科，\x01",
            "通知他们开始作战。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#00100F嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(100)

    #C0144
    ChrTalk(
        0x104,
        (
            "#00300F我们也去准备\x01",
            "导力车吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4715")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K支援科的导力车是否停在贝尔加德门\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4715")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47A2")
    TurnDirection(0x101, 0x104, 500)
    Sleep(100)

    #C0146
    ChrTalk(
        0x101,
        "#00000F嗯，说的对。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    #C0147
    ChrTalk(
        0x101,
        (
            "#00000F诺艾尔，驾驶的任务\x01",
            "就交给你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x109,
        "#10102F没问题！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jump("loc_4892")

    label("loc_47A2")

    TurnDirection(0x101, 0x104, 500)
    Sleep(100)

    #C0149
    ChrTalk(
        0x101,
        (
            "#00000F嗯，说的对。\x01",
            "我们这就去把车开来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000F诺艾尔，驾驶的任务\x01",
            "就交给你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x109,
        "#10102F没问题！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "支援科众成员把停在其它地方的\x01",
            "导力车开到了贝尔加德门。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4892")

    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【追赶飙车族】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8B, 0x4, 0x2)
    OP_29(0x8B, 0x1, 0x1)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xF, 0x80)
    SetScenarioFlags(0x22, 2)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_45D2 end

    def Function_26_48F3(): pass

    label("Function_26_48F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch33002.itc", 0x1E)
    LoadChrToIndex("chr/ch20000.itc", 0x1F)
    LoadChrToIndex("chr/ch44000.itc", 0x20)
    LoadChrToIndex("chr/ch24400.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch21600.itc", 0x23)
    LoadEffect(0x6, "event\\eva04_00.eff")
    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xC)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, 27000, 0, 23850, 0)
    OP_D5(0xC, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    ClearChrFlags(0xD, 0x80)
    OP_78(0x5, 0xD)
    OP_49()
    SetChrPos(0xD, 8180, 0, 21490, 90)
    OP_D5(0xD, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x7, 0xE)
    OP_49()
    SetChrPos(0xE, 53480, 0, -180, 270)
    OP_D5(0xE, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 32119, 0, 25500, 270)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 32119, 0, 24000, 270)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 32119, 0, 22500, 270)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 32119, 0, 21000, 180)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 32119, 0, 19500, 0)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 32119, 0, 18000, 270)
    OP_68(28080, 1000, 21730, 0)
    MoveCamera(316, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25710, 0)
    SetChrPos(0xF, 13370, 0, 26130, 135)
    SetChrPos(0x101, 13930, 0, 21960, 135)
    SetChrPos(0x102, 13600, 0, 23380, 135)
    SetChrPos(0x103, 13010, 0, 24560, 135)
    SetChrPos(0x104, 13970, 0, 24800, 135)
    SetChrPos(0x109, 12600, 0, 21430, 135)
    SetChrPos(0x105, 12600, 0, 22840, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xF, 0xFF)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    BeginChrThread(0x10, 1, 0, 43)
    Sleep(20)
    BeginChrThread(0x13, 1, 0, 43)
    Sleep(50)
    BeginChrThread(0x11, 1, 0, 43)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x15, 1, 0, 43)
    Sleep(50)
    BeginChrThread(0x14, 1, 0, 43)
    Sleep(20)
    BeginChrThread(0x12, 1, 0, 43)
    Sleep(3000)
    OP_68(12730, 1000, 22990, 5000)
    MoveCamera(301, 22, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(24610, 5000)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x15, 0xFF)
    OP_6F(0x1)
    OP_0D()

    #C0154
    ChrTalk(
        0x104,
        (
            "#00301F……飙车族完全没有\x01",
            "要出现的迹象啊。\x02\x03",

            "#00306F他们真的会来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        (
            "#00000F这个……谁知道呢。\x02\x03",

            "#00003F据米蕾优三尉说，\x01",
            "他们的行驶路线包含了\x01",
            "西克洛斯贝尔街道在内……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#00100F嗯，所以凯特巡警等隶属于\x01",
            "公共安全科的警察无法处理。\x02\x03",

            "因为警察的管辖范围在一般情况下\x01",
            "仅限于克洛斯贝尔市内。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x105,
        (
            "#10300F出于这种考虑，\x01",
            "才会向我们这个特殊部门\x01",
            "提出支援请求啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        "#00203F嗯，应该就是这么回事。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x109,
        (
            "#10101F总之，无论是在市内还是市外，\x01",
            "我们都不能放任这种飙车行为。\x02\x03",

            "一定要把他们抓捕归案！\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xF,
        "#07902F呵呵，那就拜托大家了。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(26210, 1000, 21250, 0)
    MoveCamera(301, 34, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_70(0x3, 0x1E)
    OP_0D()
    Sound(463, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x1, 0x0)
    OP_79(0x1)
    Sleep(1500)
    OP_68(15610, 1000, 20790, 3000)
    MoveCamera(301, 34, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(23500, 3000)
    OP_6F(0x79)
    Sleep(500)
    Sound(488, 0, 100, 0)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5074")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆「取缔超速车辆」？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【完成】\x01",          # 1
            "【未完成】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_505B"),
        (1, "loc_5060"),
        (2, "loc_506A"),
        (SWITCH_DEFAULT, "loc_5074"),
    )


    label("loc_505B")

    Jump("loc_5074")

    label("loc_5060")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_5074")

    label("loc_506A")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_5074")

    label("loc_5074")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_50AC")

    #C0162
    ChrTalk(
        0x101,
        "#3P#00005F这声音……难道是……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_50CD")

    label("loc_50AC")


    #C0163
    ChrTalk(
        0x101,
        "#3P#00005F这声音是……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_50CD")

    Fade(500)
    OP_68(47820, 1000, 890, 0)
    MoveCamera(312, 34, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23760, 0)
    SetChrPos(0xF, 17120, 0, 24570, 135)
    SetChrPos(0x101, 16370, 0, 21380, 135)
    SetChrPos(0x102, 15090, 0, 21830, 135)
    SetChrPos(0x103, 16079, 0, 24050, 135)
    SetChrPos(0x104, 16340, 0, 22600, 135)
    SetChrPos(0x109, 14100, 0, 21100, 135)
    SetChrPos(0x105, 14900, 0, 23290, 135)
    OP_68(37310, 1000, 3570, 1000)
    MoveCamera(312, 34, 0, 1000)
    OP_6E(590, 1000)
    SetCameraDistance(24950, 1000)
    Sound(486, 0, 100, 0)
    BeginChrThread(0xE, 1, 0, 28)
    Sleep(1000)
    OP_68(24830, 1000, 19380, 1000)
    MoveCamera(311, 23, 0, 1000)
    OP_6E(590, 1000)
    SetCameraDistance(24950, 1000)
    OP_6F(0x79)
    Sound(487, 0, 100, 0)
    BeginChrThread(0xE, 3, 0, 27)
    Sleep(500)
    StopBGM(0xFA0)

    #N0164
    NpcTalk(
        0xC,
        "乘客",
        "哇！？\x02",
    )

    CloseMessageWindow()

    #N0165
    NpcTalk(
        0xC,
        "乘客",
        "呀！！\x02",
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0166
    NpcTalk(
        0xE,
        "瑞吉",
        "哈哈，真惊险啊！\x02",
    )

    CloseMessageWindow()

    #N0167
    NpcTalk(
        0xE,
        "瑞吉",
        "给我小心点啊！\x02",
    )

    CloseMessageWindow()
    OP_6B(0xE)
    BeginChrThread(0xE, 1, 0, 29)
    Sleep(3000)
    OP_6B(0xFF)
    OP_6F(0x79)
    OP_68(54850, 1000, -840, 2500)
    MoveCamera(310, 21, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(23500, 2500)
    Sound(494, 0, 100, 0)
    OP_0D()
    Sleep(4000)
    Fade(500)
    OP_68(15880, 1000, 21890, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22330, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_544E")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆「取缔超速车辆」？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【完成】\x01",          # 1
            "【未完成】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5435"),
        (1, "loc_543A"),
        (2, "loc_5444"),
        (SWITCH_DEFAULT, "loc_544E"),
    )


    label("loc_5435")

    Jump("loc_544E")

    label("loc_543A")

    OP_29(0x69, 0x4, 0x10)
    Jump("loc_544E")

    label("loc_5444")

    OP_29(0x69, 0x3, 0x10)
    Jump("loc_544E")

    label("loc_544E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_54A5")

    #C0169
    ChrTalk(
        0x101,
        "#00001F是、是『高贵之血』……！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        "#00101F果、果然是他们……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_54E9")

    label("loc_54A5")


    #C0171
    ChrTalk(
        0x101,
        "#00001F那、那就是飙车族吗……！\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        "#00101F真是太危险了……！\x02",
    )

    CloseMessageWindow()

    label("loc_54E9")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xF, 0x104, 500)
    Sleep(100)

    #C0173
    ChrTalk(
        0xF,
        (
            "#07907F各位！请马上开始追捕吧！\x02\x03",

            "我这就联络公共安全科！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5546():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5546)
    Sleep(50)

    def lambda_5556():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5556)
    Sleep(50)

    def lambda_5566():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5566)
    Sleep(50)

    def lambda_5576():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5576)
    Sleep(50)

    def lambda_5586():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5586)
    Sleep(50)

    def lambda_5596():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5596)
    Sleep(300)

    #C0174
    ChrTalk(
        0x101,
        "#00001F明白了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    #C0175
    ChrTalk(
        0x101,
        (
            "#00007F诺艾尔，指挥工作交给我，\x01",
            "你专心驾驶吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(100)

    #C0176
    ChrTalk(
        0x109,
        "#10107F是！队长！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 3, 0, 32)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 34)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 36)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 37)
    Sleep(300)

    def lambda_564D():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_564D)
    Sleep(1000)
    WaitChrThread(0x109, 3)
    Sleep(500)

    def lambda_5664():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5664)

    def lambda_5679():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5679)
    WaitChrThread(0x109, 2)
    Sound(461, 0, 100, 0)
    OP_71(0x5, 0x10F, 0x12C, 0x0, 0x0)
    Sleep(1500)
    OP_68(19350, 1000, 20110, 3000)
    MoveCamera(295, 33, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(22330, 3000)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 30)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)
    Sleep(1500)
    Sound(462, 0, 100, 0)
    OP_71(0x5, 0x12D, 0x14A, 0x0, 0x0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 39)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 41)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 40)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 42)
    WaitChrThread(0x102, 3)

    def lambda_573E():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_573E)

    def lambda_5753():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5753)
    WaitChrThread(0x104, 3)

    def lambda_5768():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5768)

    def lambda_577D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_577D)
    WaitChrThread(0x103, 3)

    def lambda_5792():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5792)

    def lambda_57A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_57A7)
    WaitChrThread(0x105, 3)

    def lambda_57BC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57BC)

    def lambda_57D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_57D1)
    OP_6F(0x1)
    Sleep(800)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_0D()
    Sound(461, 0, 100, 0)
    OP_71(0x5, 0x14B, 0x168, 0x1, 0x0)
    Sleep(1000)
    OP_68(29880, 1000, 3290, 2000)
    MoveCamera(295, 33, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(22330, 2000)
    Sound(493, 0, 100, 0)
    BeginChrThread(0xD, 1, 0, 31)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    Sleep(800)
    OP_68(40230, 1000, 1390, 1500)
    MoveCamera(295, 33, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(22330, 1500)
    Sound(494, 0, 100, 0)
    Sleep(3000)
    SetScenarioFlags(0x22, 0)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_48F3 end

    def Function_27_58B2(): pass

    label("Function_27_58B2")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 26730, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 27000, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 27700, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 27000, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 27000, 0, 14720, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_27_58B2 end

    def Function_28_59D2(): pass

    label("Function_28_59D2")

    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    OP_9F(0x0, 0xE)
    OP_9F(0x1, 53480, 0, -180)
    OP_9F(0x1, 35030, 0, -620)
    OP_9F(0x1, 27210, 0, 9320)
    OP_9F(0x1, 26730, 0, 14720)
    OP_9F(0x1, 27000, 0, 14720)
    OP_9F(0x2, 0xE, 18000, 0x6)
    OP_9B(0x1, 0xE, 0x10E, 0x7D0, 0x4650, 0x0)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    Return()

    # Function_28_59D2 end

    def Function_29_5A4D(): pass

    label("Function_29_5A4D")

    Sound(493, 0, 100, 0)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    OP_9E(0xFE, 0x7AD0, 0x212A, 0xFFFEDB08, 0x2710, 0x4)
    OP_9B(0x1, 0xE, 0xB4, 0x2AF8, 0x2EE0, 0x0)
    Sound(492, 0, 100, 0)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    Sleep(1000)
    Sound(486, 0, 100, 0)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    OP_9E(0xFE, 0x78BE, 0xFFFFE76E, 0x124F8, 0x2EE0, 0x1)
    OP_98(0xE, 0x9C40, 0x0, 0x0, 0x3A98, 0x0)
    Return()

    # Function_29_5A4D end

    def Function_30_5AD4(): pass

    label("Function_30_5AD4")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, 15520, 0, 21370)
    OP_9F(0x1, 19310, 0, 18600)
    OP_9F(0x2, 0xD, 5000, 0x6)
    Return()

    # Function_30_5AD4 end

    def Function_31_5AFE(): pass

    label("Function_31_5AFE")

    OP_9F(0x0, 0xD)
    OP_9F(0x1, 25620, 0, 9880)
    OP_9F(0x1, 30580, 0, 1500)
    OP_9F(0x1, 37950, 0, 230)
    OP_9F(0x1, 45610, 0, 160)
    OP_9F(0x2, 0xD, 10000, 0x6)
    OP_98(0xD, 0x6D60, 0x0, 0x0, 0x2710, 0x0)
    Return()

    # Function_31_5AFE end

    def Function_32_5B58(): pass

    label("Function_32_5B58")

    OP_95(0x109, 11600, 0, 19760, 4000, 0x0)
    OP_95(0x109, 8490, 0, 19730, 4000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_32_5B58 end

    def Function_33_5B9D(): pass

    label("Function_33_5B9D")

    OP_95(0x101, 21660, 0, 22150, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_33_5B9D end

    def Function_34_5BB9(): pass

    label("Function_34_5BB9")

    OP_95(0x102, 20460, 0, 22280, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_34_5BB9 end

    def Function_35_5BD5(): pass

    label("Function_35_5BD5")

    OP_95(0x103, 19000, 0, 23000, 2000, 0x0)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_35_5BD5 end

    def Function_36_5BF1(): pass

    label("Function_36_5BF1")

    OP_95(0x104, 20290, 0, 23430, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_36_5BF1 end

    def Function_37_5C0D(): pass

    label("Function_37_5C0D")

    OP_95(0x105, 18030, 0, 23200, 2000, 0x0)
    OP_93(0x105, 0xB4, 0x1F4)
    Return()

    # Function_37_5C0D end

    def Function_38_5C29(): pass

    label("Function_38_5C29")

    OP_95(0x101, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x101, 0xE1, 0x1F4)

    def lambda_5C49():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C49)

    def lambda_5C5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C5E)
    Return()

    # Function_38_5C29 end

    def Function_39_5C6B(): pass

    label("Function_39_5C6B")

    Sleep(800)
    OP_95(0x102, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_39_5C6B end

    def Function_40_5C8A(): pass

    label("Function_40_5C8A")

    Sleep(1000)
    OP_95(0x103, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_40_5C8A end

    def Function_41_5CA9(): pass

    label("Function_41_5CA9")

    Sleep(800)
    OP_95(0x104, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x104, 0xE1, 0x1F4)
    Return()

    # Function_41_5CA9 end

    def Function_42_5CC8(): pass

    label("Function_42_5CC8")

    Sleep(1200)
    OP_95(0x105, 20150, 0, 19950, 3000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_42_5CC8 end

    def Function_43_5CE7(): pass

    label("Function_43_5CE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DFF")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5D2A"),
        (1, "loc_5D44"),
        (2, "loc_5D5E"),
        (3, "loc_5D78"),
        (4, "loc_5D92"),
        (5, "loc_5DAC"),
        (6, "loc_5DC6"),
        (SWITCH_DEFAULT, "loc_5DE0"),
    )


    label("loc_5D2A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_5DFA")

    label("loc_5D44")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_5DFA")

    label("loc_5D5E")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_5DFA")

    label("loc_5D78")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_5DFA")

    label("loc_5D92")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_5DFA")

    label("loc_5DAC")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_5DFA")

    label("loc_5DC6")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_5DFA")

    label("loc_5DE0")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_5DFA")

    label("loc_5DFA")

    Jump("Function_43_5CE7")

    label("loc_5DFF")

    Return()

    # Function_43_5CE7 end

    def Function_44_5E00(): pass

    label("Function_44_5E00")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E72")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_5E72")

    SetMapObjFlags(0x5, 0x4)
    FadeToBright(1000, 0)
    OP_68(16650, 400, -10470, 0)
    MoveCamera(295, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22430, 0)
    OP_0D()
    Sleep(500)
    OP_68(14930, 400, 890, 5000)
    MoveCamera(280, 18, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(56040, 5000)
    PlaceName2(340, 200, "c_plac18", 0x0, 4000)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(50970, 1000, -460, 4700)
    MoveCamera(315, 30, 0, 4700)
    OP_6E(510, 4700)
    SetCameraDistance(26660, 4700)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6273")
    Sleep(2500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FB1")
    SetChrPos(0x101, 54820, 0, -130, 270)
    SetChrPos(0x102, 56020, 0, -1200, 270)
    SetChrPos(0x103, 56170, 0, 1010, 270)
    SetChrPos(0x104, 57750, 0, -1090, 270)
    SetChrPos(0x109, 57900, 0, 920, 270)
    SetChrPos(0x105, 59100, 0, -120, 270)
    Jump("loc_6006")

    label("loc_5FB1")

    SetChrPos(0x101, 54820, 0, -130, 270)
    SetChrPos(0x102, 56020, 0, -1200, 270)
    SetChrPos(0x104, 56170, 0, 1010, 270)
    SetChrPos(0x109, 57750, 0, -1090, 270)
    SetChrPos(0x105, 57900, 0, 920, 270)

    label("loc_6006")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_612C")

    def lambda_601B():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_601B)

    def lambda_6035():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6035)
    Sleep(100)

    def lambda_6049():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6049)

    def lambda_6063():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6063)
    Sleep(120)

    def lambda_6077():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6077)

    def lambda_6091():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6091)
    Sleep(90)

    def lambda_60A5():
        OP_95(0xFE, 53750, 0, -1090, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_60A5)

    def lambda_60BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_60BF)
    Sleep(100)

    def lambda_60D3():
        OP_95(0xFE, 53900, 0, 920, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_60D3)

    def lambda_60ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_60ED)
    Sleep(80)

    def lambda_6101():
        OP_95(0xFE, 55100, 0, -120, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6101)

    def lambda_611B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_611B)
    Jump("loc_620F")

    label("loc_612C")


    def lambda_6131():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6131)

    def lambda_614B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_614B)
    Sleep(100)

    def lambda_615F():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_615F)

    def lambda_6179():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6179)
    Sleep(120)

    def lambda_618D():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_618D)

    def lambda_61A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_61A7)
    Sleep(90)

    def lambda_61BB():
        OP_95(0xFE, 53750, 0, -1090, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_61BB)

    def lambda_61D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_61D5)
    Sleep(100)

    def lambda_61E9():
        OP_95(0xFE, 53900, 0, 920, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_61E9)

    def lambda_6203():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6203)

    label("loc_620F")

    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6237")
    WaitChrThread(0x103, 1)

    label("loc_6237")

    Fade(500)
    OP_68(52070, 1000, -280, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19600, 0)
    OP_0D()
    Sleep(1000)
    Jump("loc_679B")

    label("loc_6273")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6524")
    ClearChrFlags(0xD, 0x80)
    OP_78(0x5, 0xD)
    OP_49()
    SetChrPos(0xD, 63820, 0, -120, 0)
    OP_D5(0xD, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_0D()
    OP_49()
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Sleep(2200)

    def lambda_62EC():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_62EC)
    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(2500)
    Sound(492, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0x1)
    SetChrPos(0xD, 40000, 0, 5000, 0)
    OP_D5(0xD, 0x0, 0x15F90, 0x0, 0x0)
    OP_71(0x5, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x2)
    OP_66(0x2, 0x1)
    OP_68(50970, 1000, -460, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_648F")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 37700, 0, 1500, 135)
    SetChrPos(0x102, 37700, 0, -300, 45)
    SetChrPos(0x103, 38400, 0, 2000, 180)
    SetChrPos(0x104, 39000, 0, -800, 0)
    SetChrPos(0x109, 39900, 0, 1600, 225)
    SetChrPos(0x105, 39900, 0, -200, 315)
    OP_68(38860, 1200, 640, 0)
    MoveCamera(304, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19050, 0)
    Jump("loc_6512")

    label("loc_648F")

    SetChrPos(0x101, 37700, 0, 900, 90)
    SetChrPos(0x102, 39000, 0, -800, 0)
    SetChrPos(0x104, 38400, 0, 2000, 180)
    SetChrPos(0x109, 39900, 0, 1600, 225)
    SetChrPos(0x105, 39900, 0, -200, 315)
    OP_68(39330, 1200, 570, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)

    label("loc_6512")

    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_679B")

    label("loc_6524")

    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    OP_78(0x3, 0xC)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, 63820, 0, -120, 0)
    OP_D5(0xC, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_49()
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)
    Sleep(1700)
    Sound(473, 0, 100, 0)
    Sleep(500)

    def lambda_659D():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_659D)
    Sleep(1000)
    Sound(467, 0, 100, 0)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    SetMapObjFlags(0x3, 0x4)
    OP_68(50970, 1000, -460, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6708")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 30000, 0, 23620, 90)
    SetChrPos(0x102, 31600, 0, 24330, 180)
    SetChrPos(0x103, 30400, 0, 24330, 135)
    SetChrPos(0x104, 30500, 0, 22130, 45)
    SetChrPos(0x109, 32200, 0, 23020, 270)
    SetChrPos(0x105, 31700, 0, 22130, 315)
    OP_68(30750, 1100, 23130, 0)
    MoveCamera(314, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19050, 0)
    Jump("loc_678B")

    label("loc_6708")

    SetChrPos(0x101, 31110, 0, 22130, 0)
    SetChrPos(0x102, 29890, 0, 23410, 90)
    SetChrPos(0x104, 30510, 0, 24350, 135)
    SetChrPos(0x105, 32430, 0, 23120, 270)
    SetChrPos(0x109, 31750, 0, 24340, 180)
    OP_68(31460, 1400, 22950, 0)
    MoveCamera(311, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18180, 0)

    label("loc_678B")

    Sleep(1)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()

    label("loc_679B")


    #C0177
    ChrTalk(
        0x105,
        (
            "#12P#10300F原来如此……\x01",
            "这里就是贝尔加德门啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x109,
        (
            "#12P#10100F嗯，这里接壤帝国国境，\x01",
            "是警备队负责守卫的\x01",
            "重要场所。\x02\x03",

            "#10104F以前就和瓦吉说起过，\x01",
            "这里的指挥官是一位名叫\x01",
            "索妮亚·贝尔茨的优秀司令。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，虽然没有见过面……\x01",
            "但听说是位相当漂亮的冷美人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A59")

    #C0180
    ChrTalk(
        0x104,
        (
            "#6P#00306F确实是个大美人……\x01",
            "但如果给她分个类，\x01",
            "绝对属于很强势可怕的类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        (
            "#00001F说起来，前任司令\x01",
            "在教团事件中严重渎职，\x01",
            "好像已经被撤职罢免了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#6P#00303F嗯，其实要从实质上说，\x01",
            "真正意义上的指挥官\x01",
            "原本就是索妮亚司令。\x02\x03",

            "#00301F前任司令总是把工作全部推给属下，\x01",
            "自己只去参加各种应酬，\x01",
            "是个非常不像话的家伙。\x02\x03",

            "#00306F归根到底，都是因为他的失职，\x01",
            "队员们才会有那种遭遇，\x01",
            "以至于不得不参加复健训练。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BEC")

    label("loc_6A59")


    #C0183
    ChrTalk(
        0x104,
        (
            "#00306F确实是个大美人……\x01",
            "但如果给她分个类，\x01",
            "绝对属于很强势可怕的类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#00001F说起来，前任司令\x01",
            "在教团事件中严重渎职，\x01",
            "好像已经被撤职罢免了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        (
            "#00303F嗯，其实要从实质上说，\x01",
            "真正意义上的指挥官\x01",
            "原本就是索妮亚司令。\x02\x03",

            "#00301F前任司令总是把工作全部推给属下，\x01",
            "自己只去参加各种应酬，\x01",
            "是个非常不像话的家伙。\x02\x03",

            "#00306F归根到底，都是因为他的失职，\x01",
            "队员们才会有那种遭遇，\x01",
            "以至于不得不参加复健训练。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BEC")


    #C0186
    ChrTalk(
        0x102,
        (
            "#00108F嗯，司令轻易听信了约亚西姆的花言巧语，\x01",
            "把『真知』分发给了\x01",
            "队员们……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x105,
        (
            "#12P#10300F说起来……\x01",
            "复健训练的成果\x01",
            "如何？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E1A")

    #C0188
    ChrTalk(
        0x104,
        (
            "#6P#00300F哦，总算没有白费工夫，\x01",
            "大家都已经彻底恢复了。\x02\x03",

            "#00306F毕竟司令下达了魔鬼般\x01",
            "严厉的要求……\x01",
            "老实说，还真是累得不行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0189
    ChrTalk(
        0x104,
        (
            "#6P#00305F哦，对了，\x01",
            "说起复健训练，我想起一件事……\x02\x03",

            "#00300F听说米蕾优那家伙\x01",
            "要升职了。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#00205F米蕾优……\x01",
            "就是那位女性士官吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        (
            "#6P#00304F嗯，她至今为止累积的功绩\x01",
            "总算得到了上级的认可。\x02\x03",

            "#00309F难得来一趟，稍后去看看她，\x01",
            "顺便调侃几句好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FA6")

    label("loc_6E1A")


    #C0192
    ChrTalk(
        0x104,
        (
            "#00300F哦，总算没有白费工夫，\x01",
            "大家都已经彻底恢复了。\x02\x03",

            "#00306F毕竟司令下达了魔鬼般\x01",
            "严厉的要求……\x01",
            "老实说，还真是累得不行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0193
    ChrTalk(
        0x104,
        (
            "#00305F哦，对了，\x01",
            "说起复健训练，我想起一件事……\x02\x03",

            "#00300F听说米蕾优那家伙\x01",
            "要升职了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#00005F米蕾优？\x01",
            "就是那位女性士官吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        (
            "#00304F嗯，她至今为止累积的功绩\x01",
            "总算得到了上级的认可。\x02\x03",

            "#00309F难得来一趟，稍后去看看她，\x01",
            "顺便调侃几句好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FA6")


    #C0196
    ChrTalk(
        0x101,
        (
            "#00006F这……应该去祝贺人家才对吧……\x02\x03",

            "#00000F对了，也得去和索妮亚司令\x01",
            "打声招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x109,
        (
            "#12P#10100F那我们一会就去一趟\x01",
            "二层的司令室吧。\x02\x03",

            "不过，由于通商会议的缘故，\x01",
            "司令现在也许正忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#00000F嗯，我们去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70A9")
    SetChrPos(0x0, 50820, 0, -130, 270)
    Jump("loc_70DE")

    label("loc_70A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70CD")
    SetChrPos(0x0, 37700, 0, 900, 270)
    Jump("loc_70DE")

    label("loc_70CD")

    SetChrPos(0x0, 31110, 0, 22130, 180)

    label("loc_70DE")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7106")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_7106")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_44_5E00 end

    def Function_45_710E(): pass

    label("Function_45_710E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(46000, -9000, -17800, 0)
    MoveCamera(305, 19, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x0, 55000, -10000, -17800, 270)
    SetChrPos(0x1, 56800, -10000, -17800, 270)
    SetChrPos(0x2, 58600, -10000, -17800, 270)
    SetChrPos(0x3, 60400, -10000, -17800, 270)
    OP_68(42000, 3000, -17800, 7000)
    SetCameraDistance(24000, 7000)

    def lambda_71AB():
        OP_97(0x0, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_71AB)
    Sleep(300)

    def lambda_71C8():
        OP_97(0x1, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_71C8)
    Sleep(300)

    def lambda_71E5():
        OP_97(0x2, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_71E5)
    Sleep(300)

    def lambda_7202():
        OP_97(0x3, 0xFFFF15A0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_7202)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0xFF)
    EndChrThread(0x1, 0xFF)
    EndChrThread(0x2, 0xFF)
    EndChrThread(0x3, 0xFF)
    EventEnd(0x5)
    NewScene("t2030", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_45_710E end

    def Function_46_724B(): pass

    label("Function_46_724B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(46000, 3000, -17800, 0)
    MoveCamera(305, 19, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x0, 20000, -10000, -17800, 90)
    SetChrPos(0x1, 18200, -10000, -17800, 90)
    SetChrPos(0x2, 16400, -10000, -17800, 90)
    SetChrPos(0x3, 14600, -10000, -17800, 90)
    OP_68(50000, -9000, -17800, 7000)
    SetCameraDistance(24000, 7000)

    def lambda_72E8():
        OP_97(0x0, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_72E8)
    Sleep(300)

    def lambda_7305():
        OP_97(0x1, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_7305)
    Sleep(300)

    def lambda_7322():
        OP_97(0x2, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_7322)
    Sleep(300)

    def lambda_733F():
        OP_97(0x3, 0xEA60, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_733F)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0xFF)
    EndChrThread(0x1, 0xFF)
    EndChrThread(0x2, 0xFF)
    EndChrThread(0x3, 0xFF)
    EventEnd(0x5)
    NewScene("r1080", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_46_724B end

    def Function_47_7388(): pass

    label("Function_47_7388")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0199
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "埃雷波尼亚帝国方向边境\x01",
            "   『贝尔加德门』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_47_7388 end

    SaveToFile()

Try(main)
