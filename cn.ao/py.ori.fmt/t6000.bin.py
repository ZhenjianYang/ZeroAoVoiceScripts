from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t6000.bin",                # FileName
        "t6000",                    # MapName
        "t6000",                    # Location
        0x00A4,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x25,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 164, 0, 1, 0, 2],
    )

    BuildStringList((
        "t6000",                  # 0
        "赛尔盖科长",             # 1
        "看守梅尔文",             # 2
        "警官",                   # 3
        "女警",                   # 4
        "事件用军犬",             # 5
        "事件用军犬",             # 6
        "事件用军犬",             # 7
        "国防军士兵",             # 8
        "国防军士兵",             # 9
        "国防军士兵",             # 10
        "国防军士兵",             # 11
        "国防军士兵",             # 12
        "国防军士兵",             # 13
        "车辆",                   # 14
        "SE控制",                 # 15
        "诺克斯森林道",           # 16
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch30600.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
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

    DeclNpc(17000,   -10000,  -5000,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-16000,  -10000,  29500,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(17549,   -10000,  -14779,  225,  389,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-7170,   -10000,  140,     270,  389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 12,  -13.0,                 11.0,                  -11.0,                 324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.0833333730697632,    -3.6666667461395264,   2.200000047683716,     1.0])
    DeclEvent(0x0040, 0, 13,  18.5,                  -8.0,                  -11.0,                 36.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.5416667461395264,   0.6666666865348816,    2.200000047683716,     1.0])
    DeclEvent(0x0000, 0, 27,  12.0,                  -18.600000381469727,   -11.0,                 441.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.8571429252624512,   6.200000286102295,     2.200000047683716,     1.0])

    DeclActor(18500,   -10000,  -8000,   3200,    18500,   -8000,   -8000,   0x007C, 0,  3,  0x0000)
    DeclActor(-10480,  -10000,  3490,    1200,    -10480,  -8000,   3490,    0x007C, 0,  9,  0x0000)
    DeclActor(-11000,  -10000,  4750,    1200,    -11000,  -8000,   4750,    0x007C, 0,  9,  0x0000)
    DeclActor(32000,   -10000,  -16000,  1500,    32000,   -8000,   -16000,  0x007C, 0,  10, 0x0000)
    DeclActor(24920,   -310,    -69390,  1500,    24920,   1510,    -69390,  0x007C, 0,  28, 0x0000)

    PlaceName(90.0, 0.0, -80.0, 0x0000, 0x0000, "诺克斯森林道")

    ChipFrameInfo(1292, 0)                                       # 0

    ScpFunction((
        "Function_0_50C",          # 00, 0
        "Function_1_5BC",          # 01, 1
        "Function_2_6B7",          # 02, 2
        "Function_3_922",          # 03, 3
        "Function_4_F91",          # 04, 4
        "Function_5_1025",         # 05, 5
        "Function_6_1D29",         # 06, 6
        "Function_7_1F61",         # 07, 7
        "Function_8_1FA8",         # 08, 8
        "Function_9_2024",         # 09, 9
        "Function_10_2351",        # 0A, 10
        "Function_11_2419",        # 0B, 11
        "Function_12_2799",        # 0C, 12
        "Function_13_2B35",        # 0D, 13
        "Function_14_3608",        # 0E, 14
        "Function_15_3716",        # 0F, 15
        "Function_16_37DD",        # 10, 16
        "Function_17_43F2",        # 11, 17
        "Function_18_4422",        # 12, 18
        "Function_19_4452",        # 13, 19
        "Function_20_446E",        # 14, 20
        "Function_21_4488",        # 15, 21
        "Function_22_44C1",        # 16, 22
        "Function_23_44E6",        # 17, 23
        "Function_24_450F",        # 18, 24
        "Function_25_452B",        # 19, 25
        "Function_26_454D",        # 1A, 26
        "Function_27_4A0E",        # 1B, 27
        "Function_28_4A63",        # 1C, 28
    ))


    def Function_0_50C(): pass

    label("Function_0_50C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_544"),
        (1, "loc_550"),
        (2, "loc_55C"),
        (3, "loc_568"),
        (4, "loc_574"),
        (5, "loc_580"),
        (6, "loc_58C"),
        (SWITCH_DEFAULT, "loc_598"),
    )


    label("loc_544")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_550")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_55C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_568")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_574")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_580")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_58C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_598")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_5A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5A4")

    label("loc_5BB")

    Return()

    # Function_0_50C end

    def Function_1_5BC(): pass

    label("Function_1_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D9")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5EC")

    label("loc_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC")
    ClearChrFlags(0x8, 0x80)

    label("loc_5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_600")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)
    Jump("loc_60F")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_60F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 26)

    label("loc_60F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62A")
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_63B")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63B")
    Event(0, 16)

    label("loc_63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_651")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_683")
    SetChrPos(0x0, -10410, -10000, 2530, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 4)

    label("loc_683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_6B6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B6")
    SetChrPos(0x0, -11000, -10000, 4750, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_6B6")

    Return()

    # Function_1_5BC end

    def Function_2_6B7(): pass

    label("Function_2_6B7")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF2D100C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x1C2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70C")
    OP_52(0x10B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70C")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_722")
    OP_66(0x0, 0x1)

    label("loc_722")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_744")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_757")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76A")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_779")
    ClearMapObjFlags(0x7, 0x4)

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FD")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xA, 0xC8, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_814")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_814")

    label("loc_814")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_837")
    SetMapObjFrame(0xFF, "t6000:layer21", 0x0, 0x1)

    label("loc_837")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 32000, -10000, -16000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_897")
    OP_66(0x3, 0x1)

    label("loc_897")

    MiniGame(0x2F, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_921")
    OP_65(0x1, 0x1)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x5, 0x15)
    SetChrPos(0x15, 18500, -10000, -8000, 270)
    OP_D5(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x5, 0x2)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA0)

    label("loc_921")

    Return()

    # Function_2_6B7 end

    def Function_3_922(): pass

    label("Function_3_922")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C64")
    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_965")
    SetScenarioFlags(0x31, 2)

    label("loc_965")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_9A5")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99A")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_9A0")

    label("loc_99A")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_9A0")

    Jump("loc_9AB")

    label("loc_9A5")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_9AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_A1C")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9FC"),
        (SWITCH_DEFAULT, "loc_A0D"),
    )


    label("loc_9FC")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_A17")

    label("loc_A0D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A17")

    Jump("loc_C4D")

    label("loc_A1C")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A4C")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_A4C")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A76"),
        (1, "loc_B7A"),
        (2, "loc_C0B"),
        (SWITCH_DEFAULT, "loc_C43"),
    )


    label("loc_A76")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA7")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_AB7")

    label("loc_AA7")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_AB7")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B0D")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B30")
    Sound(461, 0, 100, 0)

    label("loc_B30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B50")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_B60")

    label("loc_B50")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_B60")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_9AB")

    label("loc_B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_BEC")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_BAF")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_BC7")

    label("loc_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_BC2")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_BC7")

    label("loc_BC2")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_BC7")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C06")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_BFC")
    OP_AF(0xFB)
    Jump("loc_C06")

    label("loc_BFC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C06")

    Jump("loc_C4D")

    label("loc_C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C24")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C3E")

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C34")
    OP_AF(0xFB)
    Jump("loc_C3E")

    label("loc_C34")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C3E")

    Jump("loc_C4D")

    label("loc_C43")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C4D")

    Jump("loc_9AB")

    label("loc_C52")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Jump("loc_F90")

    label("loc_C64")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C96")
    SetScenarioFlags(0x31, 2)

    label("loc_C96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_CD6")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CCB")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_CD1")

    label("loc_CCB")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_CD1")

    Jump("loc_CDC")

    label("loc_CD6")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_CDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_D4D")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D2D"),
        (SWITCH_DEFAULT, "loc_D3E"),
    )


    label("loc_D2D")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_D48")

    label("loc_D3E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D48")

    Jump("loc_F7E")

    label("loc_D4D")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_D7D")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_D7D")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DA7"),
        (1, "loc_EAB"),
        (2, "loc_F3C"),
        (SWITCH_DEFAULT, "loc_F74"),
    )


    label("loc_DA7")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_DD8")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_DE8")

    label("loc_DD8")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_DE8")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E3E")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E61")
    Sound(461, 0, 100, 0)

    label("loc_E61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_E81")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_E91")

    label("loc_E81")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_E91")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_CDC")

    label("loc_EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F1D")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_EE0")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_EF8")

    label("loc_EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_EF3")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_EF8")

    label("loc_EF3")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_EF8")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F37")

    label("loc_F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F2D")
    OP_AF(0xFB)
    Jump("loc_F37")

    label("loc_F2D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F37")

    Jump("loc_F7E")

    label("loc_F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F55")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F6F")

    label("loc_F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F65")
    OP_AF(0xFB)
    Jump("loc_F6F")

    label("loc_F65")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6F")

    Jump("loc_F7E")

    label("loc_F74")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F7E")

    Jump("loc_CDC")

    label("loc_F83")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)

    label("loc_F90")

    Return()

    # Function_3_922 end

    def Function_4_F91(): pass

    label("Function_4_F91")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_FEC")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FE1")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_FE7")

    label("loc_FE1")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_FE7")

    Jump("loc_1010")

    label("loc_FEC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100A")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_1010")

    label("loc_100A")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_1010")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_F91 end

    def Function_5_1025(): pass

    label("Function_5_1025")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1177")

    #C0001
    ChrTalk(
        0xFE,
        (
            "我们已经从国防军手中\x01",
            "拿回了拘留所的警备权限。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "之前的警备力度\x01",
            "未免也太强了……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#00101F嗯，虽然帝国和共和国\x01",
            "之前一直在持续进攻……\x01",
            "但警备力度确实是有些过强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00008F大概是因为我当时被拘留在此，\x01",
            "所以特意加强了警备力度。\x02\x03",

            "#00003F迪塔先生似乎一直\x01",
            "想尽力避免我们支援科的\x01",
            "成员再次聚集起来……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F2")

    label("loc_1177")


    #C0005
    ChrTalk(
        0xFE,
        (
            "我们已经从国防军手中\x01",
            "拿回了拘留所的警备权限。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "给每个岗位分配最合适的人选，\x01",
            "一定能使警备工作的效率\x01",
            "像以前一样高。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F2")

    Jump("loc_1D25")

    label("loc_11F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D9")

    #C0007
    ChrTalk(
        0x9,
        (
            "得知袭击事件的消息之后，\x01",
            "拘留所里的犯人们\x01",
            "也难掩不安之情。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "所以我们正在确认\x01",
            "犯人家属的人身安全。\x01",
            "不过……果然还是有人出事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "……尽管对方是犯罪者，\x01",
            "但还是不忍心把这种噩耗告诉他们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_134B")

    label("loc_12D9")


    #C0010
    ChrTalk(
        0x9,
        (
            "有不少犯人的家属\x01",
            "都生活在克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "……虽说对方是犯罪者，但还是不忍心\x01",
            "把其家属遇难的噩耗告诉他们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134B")

    Jump("loc_1D25")

    label("loc_1350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13D4")

    #C0012
    ChrTalk(
        0x9,
        (
            "这次的脱轨事故\x01",
            "难道是人为\x01",
            "造成的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "若真如此，那可是滔天大罪。\x01",
            "犯人竟使无辜的普通人\x01",
            "遭受那么巨大的伤害……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D25")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148F")

    #C0014
    ChrTalk(
        0x9,
        (
            "从刚才开始，就一直能听到\x01",
            "那种仿佛来自地底的嚎叫声……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        (
            "拘留所内的犯人们似乎\x01",
            "也开始骚动起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "说不定会有犯人想\x01",
            "趁机做出什么事，\x01",
            "必须要多加留意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14FF")

    label("loc_148F")


    #C0017
    ChrTalk(
        0x9,
        (
            "拘留所内的犯人们似乎\x01",
            "也因这异常事态\x01",
            "而骚动起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "说不定会有犯人想\x01",
            "趁机做出什么事，\x01",
            "必须要多加留意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FF")

    Jump("loc_1D25")

    label("loc_1504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1626")

    #C0019
    ChrTalk(
        0x9,
        (
            "从事我们这份工作，必须要在离犯人\x01",
            "最近的地方严加监视，因此有不少\x01",
            "看守人员都被巨大的压力击垮。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "老实说，我也撑得很辛苦，\x01",
            "除了休假日之外，完全没有可以放松的时候……\x01",
            "话虽如此，但这份工作必须要有人做。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "总之，如果要在这里工作，\x01",
            "就必须拥有坚韧不催的精神。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16C1")

    label("loc_1626")


    #C0022
    ChrTalk(
        0x9,
        (
            "从事我们这份工作，必须要在离犯人\x01",
            "最近的地方严加监视，因此有不少\x01",
            "看守人员都被巨大的压力击垮。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "总之，如果要在这里工作，\x01",
            "就必须拥有坚韧不催的精神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C1")

    Jump("loc_1D25")

    label("loc_16C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178E")

    #C0024
    ChrTalk(
        0x9,
        (
            "一旦独立，应该就能建立新制度，\x01",
            "从而进一步加强惩治克洛斯贝尔\x01",
            "地区内的犯罪行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "一直让我们束手无策的外国犯罪者\x01",
            "也必然会随之减少。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x9,
        "……但前提还是顺利实现独立。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1804")

    label("loc_178E")


    #C0027
    ChrTalk(
        0x9,
        (
            "一旦独立，应该就能建立新制度，\x01",
            "从而进一步加强惩治克洛斯贝尔\x01",
            "地区内的犯罪行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        "……但前提还是顺利实现独立。\x02",
    )

    CloseMessageWindow()

    label("loc_1804")

    Jump("loc_1D25")

    label("loc_1809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1908")

    #C0029
    ChrTalk(
        0x9,
        (
            "依据自治州法，\x01",
            "如果犯罪者是外国人，\x01",
            "我们便无权长期拘留他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "这就是帝国、共和国的\x01",
            "犯罪者大量涌入这里的\x01",
            "主要原因之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "在新市长的提案下，如今已经修正了一部分法律，\x01",
            "这种情况也稍有改善……\x01",
            "不过，离完全杜绝还差得远。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19BC")

    label("loc_1908")


    #C0032
    ChrTalk(
        0x9,
        (
            "依据自治州法，外国人就算\x01",
            "在克洛斯贝尔地区内犯罪，\x01",
            "我们也无权长期拘留他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "在新市长的提案下，如今已经修正了一部分法律，\x01",
            "这种情况也稍有改善……\x01",
            "不过，离完全杜绝还差得远。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BC")

    Jump("loc_1D25")

    label("loc_19C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB4")

    #C0034
    ChrTalk(
        0x9,
        (
            "在教团事件结束后，拘留所的\x01",
            "警备体制已经重新整顿了一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "虽说警备队员遭到操控，向这里发动了袭击，\x01",
            "但我们竟然没能阻止犯人越狱，\x01",
            "实在是太不应该了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "为了彻底杜绝此类事件，\x01",
            "我们决定施行更为严密的警备措施。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B2E")

    label("loc_1AB4")


    #C0037
    ChrTalk(
        0x9,
        (
            "在教团事件结束后，拘留所的\x01",
            "警备体制已经重新整顿了一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "为了彻底杜绝越狱事件，\x01",
            "我们决定施行更为严密的警备措施。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2E")

    Jump("loc_1D25")

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3E")

    #C0039
    ChrTalk(
        0x9,
        (
            "关押在这个拘留所的人都有在\x01",
            "自治州内从事犯罪行为的嫌疑，\x01",
            "只是罪行轻重各不相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "与教团事件有所牵连的部分议员和\x01",
            "黑手党成员，还有那个前市长秘书\x01",
            "都在最近被关押进来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "等上面做好审判的准备之后，\x01",
            "就会依据自治州法\x01",
            "对他们做出判决。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CDA")

    label("loc_1C3E")


    #C0042
    ChrTalk(
        0x9,
        (
            "与教团事件有所牵连的部分议员和\x01",
            "黑手党成员，还有那个前市长秘书\x01",
            "都在最近被关押进来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "等上面做好审判的准备之后，\x01",
            "就会依据自治州法\x01",
            "对他们做出判决。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDA")

    Jump("loc_1D25")

    label("loc_1CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1D25")

    #C0044
    ChrTalk(
        0x9,
        "……这里是拘留所。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "如果没事，\x01",
            "请不要随便接近这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D25")

    TalkEnd(0xFE)
    Return()

    # Function_5_1025 end

    def Function_6_1D29(): pass

    label("Function_6_1D29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F00")

    #C0046
    ChrTalk(
        0x8,
        (
            "#01005F……怎么了？\x01",
            "不坐上去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00012F这、这个……\x01",
            "突然让我们坐上去，\x01",
            "总觉得有些惶恐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#00100F竟然给我们配发专用车……\x01",
            "回想一下以前遭受的冷遇，\x01",
            "实在是有些不知所措。\x02\x03",

            "#00104F不知为何，反倒有些怀念起\x01",
            "当初那种羡慕一科的心情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#01004F呵呵，可以理解\x01",
            "你们的心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x109,
        (
            "#10109F好了，各位！\x01",
            "赶快坐上去看看吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，某人倒是\x01",
            "充满了干劲，\x01",
            "让她久等也不大好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00003F说、说的也是啊。\x02\x03",

            "#00000F好，那我们就\x01",
            "坐上去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F5D")

    label("loc_1F00")


    #C0053
    ChrTalk(
        0x8,
        (
            "#01002F嗯，赶快上车吧。\x02\x03",

            "#01004F有了这辆车，想从这里回到\x01",
            "克洛斯贝尔市，也只需片刻工夫。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5D")

    TalkEnd(0xFE)
    Return()

    # Function_6_1D29 end

    def Function_7_1F61(): pass

    label("Function_7_1F61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FA4")

    #C0054
    ChrTalk(
        0xFE,
        (
            "警察学校附近\x01",
            "没有异常！\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "我们会继续保持警戒！\x02",
    )

    CloseMessageWindow()

    label("loc_1FA4")

    TalkEnd(0xFE)
    Return()

    # Function_7_1F61 end

    def Function_8_1FA8(): pass

    label("Function_8_1FA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2020")

    #C0056
    ChrTalk(
        0xFE,
        (
            "由于警备队已经撤退，这里的警备\x01",
            "略显薄弱，所以我和乔里基科长\x01",
            "一起来这里帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        "这里就交给我们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2020")

    TalkEnd(0xFE)
    Return()

    # Function_8_1FA8 end

    def Function_9_2024(): pass

    label("Function_9_2024")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2056")
    SetScenarioFlags(0x31, 2)

    label("loc_2056")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_209C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2096")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_208B")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_2091")

    label("loc_208B")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_2091")

    Jump("loc_209C")

    label("loc_2096")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_209C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_210D")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20ED"),
        (SWITCH_DEFAULT, "loc_20FE"),
    )


    label("loc_20ED")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2108")

    label("loc_20FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2108")

    Jump("loc_233E")

    label("loc_210D")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_213D")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_213D")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2167"),
        (1, "loc_226B"),
        (2, "loc_22FC"),
        (SWITCH_DEFAULT, "loc_2334"),
    )


    label("loc_2167")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2198")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_21A8")

    label("loc_2198")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_21A8")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21FE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21FE")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2221")
    Sound(461, 0, 100, 0)

    label("loc_2221")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_2241")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2251")

    label("loc_2241")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2251")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_209C")

    label("loc_226B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_22DD")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_22A0")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_22B8")

    label("loc_22A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_22B3")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_22B8")

    label("loc_22B3")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_22B8")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22F7")

    label("loc_22DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_22ED")
    OP_AF(0xFB)
    Jump("loc_22F7")

    label("loc_22ED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22F7")

    Jump("loc_233E")

    label("loc_22FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2315")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_232F")

    label("loc_2315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2325")
    OP_AF(0xFB)
    Jump("loc_232F")

    label("loc_2325")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_232F")

    Jump("loc_233E")

    label("loc_2334")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_233E")

    Jump("loc_209C")

    label("loc_2343")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_2024 end

    def Function_10_2351(): pass

    label("Function_10_2351")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0058
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(33030, -9000, -16129, 1500)
    MoveCamera(54, 38, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(10340, 1500)
    Sleep(1000)
    SetChrName("")

    #A0059
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2414")
    OP_E2(0x2)
    MiniGame(0x6, 0x15, 0x8B10, 0xFFFFD8F0, 0xFFFFC1BC, 0x10E, 0x7D00, 0xFFFFD8F0, 0xFFFFC180)

    label("loc_2414")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_2351 end

    def Function_11_2419(): pass

    label("Function_11_2419")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(13330, 750, -64160, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18500, 0)
    OP_90(0x101, 12000, 0, -63650, 0)
    OP_90(0x102, 11000, 0, -65349, 0)
    OP_90(0x109, 13000, 0, -64650, 0)
    OP_90(0x105, 12000, 0, -66350, 0)
    FadeToBright(1000, 0)

    def lambda_24A5():
        OP_95(0xFE, 12000, -10000, -21650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24A5)

    def lambda_24BF():
        OP_95(0xFE, 11000, -10000, -23350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24BF)

    def lambda_24D9():
        OP_95(0xFE, 13000, -10000, -22650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_24D9)

    def lambda_24F3():
        OP_95(0xFE, 12000, -10000, -24350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24F3)
    OP_68(-8680, 750, -39570, 9000)
    SetCameraDistance(33500, 9000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(28490, 750, -27110, 0)
    MoveCamera(27, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(26430, 0)
    OP_68(-30330, 750, 3140, 18000)
    Sleep(16000)
    OP_0D()
    Fade(1000)
    OP_68(13270, -4850, 4770, 0)
    MoveCamera(54, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(37650, 0)
    SetCameraDistance(73520, 9000)
    Sleep(4000)
    PlaceName2(340, 200, "c_plac37", 0x0, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(11860, -9000, -22290, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19650, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrPos(0x101, 12000, -10000, -21650, 0)
    SetChrPos(0x102, 11000, -10000, -23350, 0)
    SetChrPos(0x109, 13000, -10000, -22650, 0)
    SetChrPos(0x105, 12000, -10000, -24350, 0)
    OP_0D()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00002F#5P到了……\x01",
            "这里就是警察学校的主建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x105,
        "#10306F#12P呼，终于到了啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#00102F#12P不愧是坐落在森林之中的建筑，\x01",
            "有种清幽的气氛呢。\x02\x03",

            "#00100F科长在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        (
            "#10104F#11P不知道，不过从正面入口进去，\x01",
            "就是警察学校的接待处了。\x02\x03",

            "#10100F我们进去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00000F#5P嗯，走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 12000, -10000, -22000, 0)
    SetScenarioFlags(0x127, 3)
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0xA1, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_11_2419 end

    def Function_12_2799(): pass

    label("Function_12_2799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEE")
    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-15200, -8350, 11350, 0)
    MoveCamera(24, 9, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x102, -12700, -10000, 11550, 0)
    SetChrPos(0x101, -11800, -10000, 10000, 0)
    SetChrPos(0x109, -13500, -10000, 8300, 0)
    SetChrPos(0x105, -12400, -10000, 7950, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0065
    ChrTalk(
        0x102,
        "#00105F#11P咦，那栋建筑物是？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00008F#11P哦……那是拘留所。\x02\x03",

            "#00001F建造在了警察学校\x01",
            "主建筑的旁边。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0067
    ChrTalk(
        0x102,
        (
            "#00101F#5P也就是说，阿奈斯特先生\x01",
            "就被关在这里……？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#00003F#11P嗯，不久前刚被\x01",
            "达德利警官他们送进去。\x02\x03",

            "#00000F如果想见他，\x01",
            "只要申请探监就可以了……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#00108F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    #C0070
    ChrTalk(
        0x102,
        (
            "#00106F#5P……算了，还是不用了。\x02\x03",

            "#00108F他刚刚经历过那种沉痛的遭遇，\x01",
            "现在应该留给他一些\x01",
            "重新审视自己的时间……\x02\x03",

            "#00102F等以后有机会，\x01",
            "我再和外公一起来看他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#00002F#11P嗯……\x01",
            "这样也好。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x105,
        "#10304F#12P（似乎有不少隐情呢。）\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x109,
        (
            "#10100F#6P（嗯……\x01",
            "  我也不太清楚。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -11250, -10000, 7200, 180)
    SetScenarioFlags(0x127, 4)
    EventEnd(0x5)
    Jump("loc_2B34")

    label("loc_2AEE")

    EventBegin(0x1)

    #C0074
    ChrTalk(
        0x101,
        (
            "#00000F前方是拘留所，\x01",
            "我们还是不要接近了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -12250, -10000, 8310, 180)
    EventEnd(0x4)

    label("loc_2B34")

    Return()

    # Function_12_2799 end

    def Function_13_2B35(): pass

    label("Function_13_2B35")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(16000, -8900, -6550, 0)
    MoveCamera(56, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14750, 0)
    SetChrPos(0x101, 14200, -10000, -7000, 90)
    SetChrPos(0x102, 13550, -10000, -5950, 90)
    SetChrPos(0x109, 14750, -10000, -5750, 90)
    SetChrPos(0x105, 14550, -10000, -4300, 135)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 17000, -10000, -5000, 225)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0075
    ChrTalk(
        0x101,
        "#00005F#6P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#00105F#6P这就是配给特别任务\x01",
            "支援科的导力车……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(19250, -8950, -8000, 0)
    MoveCamera(145, 45, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13650, 0)
    OP_68(17500, -8950, -8000, 7500)
    MoveCamera(56, 10, 0, 7500)
    SetCameraDistance(8000, 6500)
    OP_6F(0x10)
    SetCameraDistance(9500, 4500)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(16000, -8900, -6550, 0)
    MoveCamera(56, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    #C0077
    ChrTalk(
        0x105,
        "#10302F#5P哦？设计式样还不错啊。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x109,
        (
            "#10101F#6P这、这是……\x02\x03",

            "既不是乌尔努公司的产品，也不是莱恩福尔特\x01",
            "公司的产品，从来没见过这种车型……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "#01009F#11P呵呵，没错。\x02\x03",

            "#01004F它的型号是ＸＤ－７８。\x02\x03",

            "#01002F产自利贝尔，\x01",
            "由蔡斯中央工房制造的新车型。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0080
    ChrTalk(
        0x109,
        "#10107F#6P什么！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#00011F#6P蔡斯中央工房竟然\x01",
            "开发了导力车！？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x105,
        "#10305F#5P有必要如此吃惊吗？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#00104F#6P嗯，由于利贝尔的\x01",
            "地形比较复杂，\x01",
            "所以导力车并不普及。\x02\x03",

            "#00100F而蔡斯中央工房\x01",
            "则是全世界最强的\x01",
            "著名飞船制造商……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x109,
        (
            "#10108F#6P没、没想到蔡斯中央工房\x01",
            "开发了导力车！\x02\x03",

            "#10109F具体规格如何！？\x01",
            "最高时速是多少！？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "#01005F#11P好了好了，冷静点。\x02\x03",

            "#01004F听说这辆车装载了\x01",
            "飞船用新型引擎的小型版。\x02\x03",

            "#01002F如果开到最快，时速应该能\x01",
            "保持在１５００赛尔矩左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        "#10102F#6P太、太厉害了……！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#00005F#6P居然比铁路列车的速度还快……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#00100F#6P话说回来，这么高级的车\x01",
            "竟然会配发给我们？\x02\x03",

            "看起来，好像还是尚未\x01",
            "正式发售的新型车吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "#01004F#11P嗯，按理来说，\x01",
            "这么高级的车是不会配发给你们的。\x02\x03",

            "#01002F你们能拥有它，\x01",
            "完全是得益于迪塔新市长的安排。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    #C0090
    ChrTalk(
        0x101,
        "#00011F#6P迪塔市长吗！？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#00105F#6P说、说起来，迪塔叔叔\x01",
            "一直与蔡斯中央工房有所往来，\x01",
            "确实可以做出这样的安排……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        (
            "#10109F#6P呼～真不愧是天下闻名的\x01",
            "ＩＢＣ总裁啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        (
            "#10309F#5P呵呵，如此关照我们，\x01",
            "反倒会让人不由自主地产生警觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "#01004F#11P呵呵，你们就用努力工作的方式\x01",
            "来回报他这份恩情吧。\x02\x03",

            "#01000F如果觉得这份负担太过沉重，\x01",
            "也可以谢绝哦。\x02\x03",

            "那样的话，就会给你们调来一辆警察局\x01",
            "统一配备的乌尔努公司量产车。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00004F#6P不……\x01",
            "我们还是心怀感激地接受吧。\x02\x03",

            "#00000F这辆车现在就可以开了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#01000F#11P嗯，之前已经检查并试驾过了。\x02\x03",

            "给，这是车钥匙。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x35C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0098
    ChrTalk(
        0x101,
        (
            "#00002F#6P……哈哈……\x01",
            "不知为何，总有些感慨。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00104F#6P是啊，反倒有些怀念起\x01",
            "当初那种羡慕一科的心情了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0100
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，那就赶快启动，\x01",
            "痛痛快快地开上一程吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0101
    ChrTalk(
        0x101,
        (
            "#00000F#12P嗯，难得得到了导力车，\x01",
            "我们就开它回克洛斯贝尔市吧。\x02\x03",

            "诺艾尔，可以麻烦你来驾驶吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    #C0102
    ChrTalk(
        0x109,
        "#10109F#5P没问题，交给我吧！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#01004F#11P呵呵……那我也\x01",
            "搭个便车吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x8, 17000, -10000, -5000, 270)
    SetChrPos(0x0, 14500, -10000, -8000, 90)
    SetScenarioFlags(0x127, 6)
    ModifyEventFlags(0, 1, 0x80)
    OP_66(0x0, 0x1)
    OP_29(0xA1, 0x1, 0x9)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x1D, (scpexpr(EXPR_PUSH_LONG, 0x21260000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_13_2B35 end

    def Function_14_3608(): pass

    label("Function_14_3608")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(468)
    OP_68(17550, -9000, -8000, 0)
    MoveCamera(60, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(8650, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x8, 0x8)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(12000, -9000, -12550, 6000)
    MoveCamera(48, 30, 0, 6000)
    OP_6E(650, 6000)
    SetCameraDistance(17350, 6000)
    Sleep(500)
    Sound(494, 0, 60, 0)
    Sound(468, 2, 80, 0)
    BeginChrThread(0x15, 3, 0, 15)
    OP_6F(0x79)
    Fade(500)
    OP_F0(0x0, 0x1)
    OP_68(13550, -9000, -13850, 0)
    MoveCamera(19, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16880, 0)
    OP_68(13550, -9000, -20850, 4000)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x15, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("r4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3608 end

    def Function_15_3716(): pass

    label("Function_15_3716")


    def lambda_371B():
        OP_95(0xFE, 16500, -10000, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_371B)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    WaitChrThread(0xFE, 1)

    def lambda_375E():
        OP_9E(0xFE, 0x4074, 0xFFFFCF2C, 0xFFFEA070, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_375E)
    Sleep(2600)
    StopSound(468, 1000, 80)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)
    Sleep(300)
    Sound(492, 0, 100, 0)
    Sleep(700)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_37A1():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37A1)
    Sound(457, 0, 100, 0)
    Sound(494, 0, 80, 0)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_3716 end

    def Function_16_37DD(): pass

    label("Function_16_37DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch41551.itc", 0x21)
    LoadChrToIndex("monster/ch80851.itc", 0x23)
    LoadChrToIndex("chr/ch04150.itc", 0x24)
    LoadChrToIndex("chr/ch04154.itc", 0x25)
    LoadChrToIndex("apl/ch51612.itc", 0x26)
    LoadEffect(0x0, "event\\ev306_00.eff")
    SoundLoad(825)
    SoundLoad(907)
    SetChrPos(0x101, -16000, -10050, 36750, 180)
    SetChrPos(0x10B, -16000, -10050, 38750, 180)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 11500, -9500, 10500, 180)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 12500, -9500, 10500, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 11500, -9500, 10500, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12500, -9500, 10500, 180)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -16000, -10050, 30750, 180)
    SetChrFlags(0x13, 0x8)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -16000, -10050, 32750, 180)
    SetChrFlags(0x14, 0x8)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 11500, -9500, 10500, 180)
    SetChrFlags(0xC, 0x20)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 0, 0, 24)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 12500, -9500, 10500, 180)
    SetChrFlags(0xD, 0x20)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 24)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -16000, -10050, 35750, 180)
    SetChrFlags(0xE, 0x20)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 0, 0, 24)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x9, 0x80)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x19)
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x14)
    OP_68(-16000, -3950, 30750, 0)
    MoveCamera(30, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(35000, 0)
    FadeToBright(1000, 0)
    OP_68(-16000, -8750, 30750, 3000)
    MoveCamera(30, 20, 0, 3000)
    SetCameraDistance(25000, 3000)
    Sleep(1000)

    def lambda_3AB6():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AB6)
    Sleep(100)

    def lambda_3ACE():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3ACE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10B, 1)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(3400, -7600, -7700, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    OP_68(8000, -8000, -11000, 5000)
    MoveCamera(36, 27, 0, 5000)
    SetCameraDistance(30000, 5000)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0x10B, 3, 0, 18)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x10B, 3)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0x1388)
    Fade(1000)
    OP_68(12700, -4450, -51000, 0)
    MoveCamera(36, 36, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 13550, -7000, -43950, 180)
    SetChrPos(0x10B, 12300, -7300, -42650, 180)
    MoveCamera(36, 30, 0, 3500)
    SetCameraDistance(21500, 3500)

    def lambda_3BCE():
        OP_9B(0x0, 0xFE, 0x5, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BCE)
    Sleep(100)

    def lambda_3BE6():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3BE6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10B, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)

    #C0104
    ChrTalk(
        0x101,
        "#00005F#11P加尔西亚……？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7356", 0)
    Fade(500)
    OP_68(12300, -3350, -53000, 0)
    MoveCamera(135, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 1000)
    SetChrPos(0x101, 12100, -3920, -54150, 0)
    SetChrPos(0x10B, 12500, -4650, -51750, 180)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(15000, 20000)
    OP_93(0x10B, 0x0, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x26)
    SetChrSubChip(0x10B, 0x1)
    OP_0D()
    Sleep(300)

    #C0105
    ChrTalk(
        0x10B,
        (
            "#11103F#11P我们的合作关系就到此为止了。\x02\x03",

            "#11100F之后的路，\x01",
            "你就一个人走下去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#00011F#11P什么……？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x10B,
        (
            "#11104F#11P再怎么说，\x01",
            "我也是鲁巴彻的副头目。\x02\x03",

            "#11101F总不能丢下部下和会长，\x01",
            "独自一人逃跑。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00013F#11P等、等一下！\x02\x03",

            "既然如此，你为何要\x01",
            "陪我一起逃到这里……\x02\x03",

            "#00007F再说了，无论你有多强，\x01",
            "也不可能以一敌众吧！？\x02\x03",

            "不然的话，干脆我也……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #C0109
    ChrTalk(
        0x10B,
        "#11107F#5S#11P你别本末倒置！小鬼！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0110
    ChrTalk(
        0x10B,
        (
            "#11103F#11P你不是说过吗……\x01",
            "要看清真相。\x02\x03",

            "而且还要解救被捕的同伴，\x01",
            "并夺回那个小丫头。\x02\x03",

            "#11100F……你现在还有时间\x01",
            "在这种地方磨磨蹭蹭吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#00008F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0112
    ChrTalk(
        0x101,
        (
            "#00003F#5P谢谢你，加尔西亚。\x02\x03",

            "#00008F站在我的立场上，\x01",
            "自然无法支持你们越狱……\x02\x03",

            "#00001F但希望你能平安无事。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x10B,
        (
            "#11104F#11P哈……\x01",
            "多余的担心。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(13200, -3350, -55250, 0)
    MoveCamera(30, 35, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21500, 0)
    OP_68(12500, -3650, -51750, 4000)
    MoveCamera(30, 30, 0, 4000)
    SetCameraDistance(18500, 4000)
    SetChrSubChip(0x10B, 0x0)

    def lambda_404A():
        OP_9B(0x0, 0xFE, 0x5, 0x2AF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_404A)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x10B, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10B)

    #C0114
    ChrTalk(
        0x10B,
        (
            "#11104F#11P罗伊德·班宁斯……\x01",
            "那家伙的弟弟吗……\x02\x03",

            "#11100F如今已经成长得\x01",
            "挺像样了嘛。\x02",
        )
    )

    CloseMessageWindow()
    Sound(907, 2, 70, 0)
    Sleep(800)
    Fade(1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0xA)
    OP_68(500, -4500, 6000, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(40000, 0)
    OP_68(500, -4500, -1000, 5000)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0xE, 0x8)
    BeginChrThread(0x13, 3, 0, 23)
    BeginChrThread(0x14, 3, 0, 23)
    BeginChrThread(0xE, 3, 0, 23)
    BeginChrThread(0xF, 3, 0, 22)
    BeginChrThread(0x10, 3, 0, 22)
    Sleep(400)
    BeginChrThread(0x11, 3, 0, 22)
    BeginChrThread(0x12, 3, 0, 22)
    Sleep(600)
    BeginChrThread(0xD, 3, 0, 22)
    Sleep(400)
    BeginChrThread(0xC, 3, 0, 22)
    OP_0D()
    BeginChrThread(0x16, 1, 0, 25)
    SetMessageWindowPos(280, 120, -1, -1)

    #A0115
    AnonymousTalk(
        0xF,
        "#2S在这里……！\x05\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    Sleep(500)
    SetMessageWindowPos(90, 50, -1, -1)

    #A0116
    AnonymousTalk(
        0x13,
        "#2S绝不能让他们逃掉！\x05\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    Sleep(1000)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Fade(1000)
    OP_68(11910, -3250, -50960, 0)
    MoveCamera(135, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14200, 0)
    SetChrSubChip(0x10B, 0x1)
    SetCameraDistance(13700, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(150)
    Fade(250)
    Sound(908, 0, 100, 0)
    #Sound(2854, 255, 100, 0)    #voice#Garcia
    ClearChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x24)
    SetChrSubChip(0x10B, 0x0)
    BeginChrThread(0x10B, 0, 0, 19)
    OP_0D()

    #C0117
    ChrTalk(
        0x10B,
        "#11102F#11P呵呵，地势条件对我很有利……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    PlayEffect(0x0, 0x1, 0x10B, 0x1, 0, 0, 0, 0, 0, 0, 1250, 1250, 1250, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(12000, 500)
    EndChrThread(0x10B, 0x0)
    SetChrChipByIndex(0x10B, 0x25)
    SetChrSubChip(0x10B, 0x0)
    Sound(881, 0, 40, 0)
    Sound(833, 0, 60, 0)
    Sound(825, 2, 70, 0)
    BeginChrThread(0x10B, 0, 0, 20)
    BeginChrThread(0x10B, 3, 0, 21)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x320)

    #C0118
    ChrTalk(
        0x10B,
        (
            "#11107F#11P#4S就让你们好好尝尝\x01",
            "我『杀戮之熊』的铁拳吧！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(825, 1000, 70)
    StopSound(907, 1000, 60)
    FadeToDark(1000, 0, -1)
    SetCameraDistance(11750, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x10B, 0x3)
    EndChrThread(0x10B, 0x0)
    RemoveParty(0xA, 0xFF)
    OP_24(0x38B)
    SetScenarioFlags(0x22, 1)
    NewScene("r4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_37DD end

    def Function_17_43F2(): pass

    label("Function_17_43F2")

    SetChrPos(0xFE, 2550, -10000, -1700, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_17_43F2 end

    def Function_18_4422(): pass

    label("Function_18_4422")

    SetChrPos(0xFE, 700, -10000, -1250, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_18_4422 end

    def Function_19_4452(): pass

    label("Function_19_4452")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_446D")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_19_4452")

    label("loc_446D")

    Return()

    # Function_19_4452 end

    def Function_20_446E(): pass

    label("Function_20_446E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4487")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_20_446E")

    label("loc_4487")

    Return()

    # Function_20_446E end

    def Function_21_4488(): pass

    label("Function_21_4488")

    OP_82(0x64, 0x12C, 0xBB8, 0x1F4)
    Sleep(500)

    label("loc_449C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44C0")
    OP_82(0x0, 0x1E, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("loc_449C")

    label("loc_44C0")

    Return()

    # Function_21_4488 end

    def Function_22_44C1(): pass

    label("Function_22_44C1")


    def lambda_44C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44C6)
    OP_9B(0x0, 0xFE, 0x0, 0x7530, 0xFA0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_44C1 end

    def Function_23_44E6(): pass

    label("Function_23_44E6")

    OP_95(0xFE, -16000, -10050, 15000, 5000, 0x1)
    OP_95(0xFE, 11500, -10000, -15650, 5000, 0x0)
    Return()

    # Function_23_44E6 end

    def Function_24_450F(): pass

    label("Function_24_450F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_452A")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_24_450F")

    label("loc_452A")

    Return()

    # Function_24_450F end

    def Function_25_452B(): pass

    label("Function_25_452B")

    Sound(910, 0, 30, 0)
    Sleep(800)
    Sound(909, 0, 30, 0)
    Sleep(1400)
    Sound(909, 0, 20, 0)
    Sleep(850)
    Sound(910, 0, 20, 0)
    Return()

    # Function_25_452B end

    def Function_26_454D(): pass

    label("Function_26_454D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10760, -9000, 21160, 0)
    MoveCamera(44, 34, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15080, 0)
    SetChrPos(0x101, -9700, -10000, 20860, 270)
    SetChrPos(0x102, -10100, -10000, 21870, 225)
    SetChrPos(0x103, -10320, -10000, 19680, 315)
    SetChrPos(0x104, -12120, -10000, 20670, 90)
    SetChrPos(0xF4, -11320, -10000, 22270, 135)
    SetChrPos(0xF5, -11520, -10000, 19680, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0119
    ChrTalk(
        0x104,
        (
            "#6P#00306F哎呀呀，他比我想象中\x01",
            "还要有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        (
            "#5P#00100F嗯，从他那种状态来看，\x01",
            "应该很快就能痊愈了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46CE")

    #C0121
    ChrTalk(
        0x105,
        (
            "#6P#10400F话说回来，真是很意外啊。\x01",
            "没想到他还会\x01",
            "激励我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477B")

    label("loc_46CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4723")

    #C0122
    ChrTalk(
        0x106,
        (
            "#6P#10703F话说回来，真让人意外。\x01",
            "没想到他还会\x01",
            "激励我们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477B")

    label("loc_4723")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_477B")

    #C0123
    ChrTalk(
        0x109,
        (
            "#6P#10100F话说回来，真叫人意外啊。\x01",
            "前黑手党干部\x01",
            "竟然会激励我们……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477B")


    #C0124
    ChrTalk(
        0x101,
        (
            "#00000F是啊……经过这么多的事情，\x01",
            "他或许也已经有所改变了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    #C0125
    ChrTalk(
        0x101,
        "#00005F怎、怎么了？各位。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x103,
        "#12P#00211F说得就像事不关己一样。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        "#00102F我看他多半是受到了你的影响呢……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0128
    ChrTalk(
        0x101,
        "#00005F……什么……！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#6P#00306F真是的，所以我才说这小子\x01",
            "是个天生的危险分子。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_495B")

    #C0130
    ChrTalk(
        0x10A,
        (
            "#6P#00602F……那家伙说你\x01",
            "很像盖伊，\x01",
            "看来还真没说错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49DE")

    label("loc_495B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_499F")

    #C0131
    ChrTalk(
        0x109,
        (
            "#6P#10102F呵呵，罗伊德警官\x01",
            "还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49DE")

    label("loc_499F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49DE")

    #C0132
    ChrTalk(
        0x106,
        (
            "#6P#10702F哈哈……\x01",
            "罗伊德警官还是老样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49DE")

    OP_5A()
    SetScenarioFlags(0x1BC, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -9700, -10000, 20860, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_26_454D end

    def Function_27_4A0E(): pass

    label("Function_27_4A0E")

    EventBegin(0x1)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00000F等等，这条路是通往森林道的，\x01",
            "导力车就在车库前哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11900, -10000, -15540, 0)
    EventEnd(0x4)
    Return()

    # Function_27_4A0E end

    def Function_28_4A63(): pass

    label("Function_28_4A63")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西·克洛斯贝尔警察学校\x01",
            "北·诺克斯森林地带入口\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_4A63 end

    SaveToFile()

Try(main)
