from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "セルゲイ課長",           # 1
        "看守メルビン",           # 2
        "警官",                   # 3
        "婦警",                   # 4
        "イベント用軍用犬",       # 5
        "イベント用軍用犬",       # 6
        "イベント用軍用犬",       # 7
        "国防軍兵士",             # 8
        "国防軍兵士",             # 9
        "国防軍兵士",             # 10
        "国防軍兵士",             # 11
        "国防軍兵士",             # 12
        "国防軍兵士",             # 13
        "車",                     # 14
        "SE制御",                 # 15
        "ノックス森林道",         # 16
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

    PlaceName(90.0, 0.0, -80.0, 0x0000, 0x0000, "ノックス森林道")

    ChipFrameInfo(1292, 0)                                       # 0

    ScpFunction((
        "Function_0_50C",          # 00, 0
        "Function_1_5BC",          # 01, 1
        "Function_2_6B7",          # 02, 2
        "Function_3_922",          # 03, 3
        "Function_4_FBD",          # 04, 4
        "Function_5_1051",         # 05, 5
        "Function_6_1EE5",         # 06, 6
        "Function_7_2173",         # 07, 7
        "Function_8_21D0",         # 08, 8
        "Function_9_225A",         # 09, 9
        "Function_10_259D",        # 0A, 10
        "Function_11_2671",        # 0B, 11
        "Function_12_2A19",        # 0C, 12
        "Function_13_2E1D",        # 0D, 13
        "Function_14_39A2",        # 0E, 14
        "Function_15_3AB0",        # 0F, 15
        "Function_16_3B77",        # 10, 16
        "Function_17_4814",        # 11, 17
        "Function_18_4844",        # 12, 18
        "Function_19_4874",        # 13, 19
        "Function_20_4890",        # 14, 20
        "Function_21_48AA",        # 15, 21
        "Function_22_48E3",        # 16, 22
        "Function_23_4908",        # 17, 23
        "Function_24_4931",        # 18, 24
        "Function_25_494D",        # 19, 25
        "Function_26_496F",        # 1A, 26
        "Function_27_4EC2",        # 1B, 27
        "Function_28_4F1D",        # 1C, 28
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

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C7A")
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_A24")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A04"),
        (SWITCH_DEFAULT, "loc_A15"),
    )


    label("loc_A04")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_A1F")

    label("loc_A15")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A1F")

    Jump("loc_C63")

    label("loc_A24")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A58")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_A58")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A8C"),
        (1, "loc_B90"),
        (2, "loc_C21"),
        (SWITCH_DEFAULT, "loc_C59"),
    )


    label("loc_A8C")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ABD")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_ACD")

    label("loc_ABD")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_ACD")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B23")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B23")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B46")
    Sound(461, 0, 100, 0)

    label("loc_B46")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B66")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_B76")

    label("loc_B66")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_B76")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_9AB")

    label("loc_B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_C02")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_BC5")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_BDD")

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_BD8")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_BDD")

    label("loc_BD8")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_BDD")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C1C")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C12")
    OP_AF(0xFB)
    Jump("loc_C1C")

    label("loc_C12")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C1C")

    Jump("loc_C63")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C54")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_C4A")
    OP_AF(0xFB)
    Jump("loc_C54")

    label("loc_C4A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C54")

    Jump("loc_C63")

    label("loc_C59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C63")

    Jump("loc_9AB")

    label("loc_C68")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Jump("loc_FBC")

    label("loc_C7A")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CAC")
    SetScenarioFlags(0x31, 2)

    label("loc_CAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_CEC")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE1")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_CE7")

    label("loc_CE1")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_CE7")

    Jump("loc_CF2")

    label("loc_CEC")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_CF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_D6B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D4B"),
        (SWITCH_DEFAULT, "loc_D5C"),
    )


    label("loc_D4B")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_D66")

    label("loc_D5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D66")

    Jump("loc_FAA")

    label("loc_D6B")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_D9F")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_D9F")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DD3"),
        (1, "loc_ED7"),
        (2, "loc_F68"),
        (SWITCH_DEFAULT, "loc_FA0"),
    )


    label("loc_DD3")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_E04")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_E14")

    label("loc_E04")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_E14")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E6A")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8D")
    Sound(461, 0, 100, 0)

    label("loc_E8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_EAD")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_EBD")

    label("loc_EAD")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_EBD")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_CF2")

    label("loc_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F49")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_F0C")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_F24")

    label("loc_F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F1F")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_F24")

    label("loc_F1F")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_F24")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F63")

    label("loc_F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F59")
    OP_AF(0xFB)
    Jump("loc_F63")

    label("loc_F59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F63")

    Jump("loc_FAA")

    label("loc_F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F81")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F9B")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F91")
    OP_AF(0xFB)
    Jump("loc_F9B")

    label("loc_F91")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F9B")

    Jump("loc_FAA")

    label("loc_FA0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FAA")

    Jump("loc_CF2")

    label("loc_FAF")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)

    label("loc_FBC")

    Return()

    # Function_3_922 end

    def Function_4_FBD(): pass

    label("Function_4_FBD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1018")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100D")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_1013")

    label("loc_100D")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_1013")

    Jump("loc_103C")

    label("loc_1018")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1036")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_103C")

    label("loc_1036")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_103C")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_FBD end

    def Function_5_1051(): pass

    label("Function_5_1051")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1277")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D3")

    #C0001
    ChrTalk(
        0xFE,
        (
            "拘置所の警備も、国防軍から\x01",
            "我々の管轄へと戻ることになった。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "少し厳重すぎると\x01",
            "言っていい状態だったからな……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#00101F帝国と共和国の\x01",
            "侵攻が続いていたとはいえ……\x01",
            "確かにそうかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00008F多分、俺が拘留されてたから\x01",
            "見張りを強化していたんだろうな。\x02\x03",

            "#00003Fディーターさんは、\x01",
            "俺たち支援課が団結するのを\x01",
            "警戒していたみたいだし……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1272")

    label("loc_11D3")


    #C0005
    ChrTalk(
        0xFE,
        (
            "拘置所の警備も、国防軍から\x01",
            "我々の管轄へと戻ることになった。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "適切な場所に適切な人員が\x01",
            "割り振られる事で、以前のような\x01",
            "効率的な警備が可能になるだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1272")

    Jump("loc_1EE1")

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1373")

    #C0007
    ChrTalk(
        0x9,
        (
            "襲撃事件の報を聞いて、\x01",
            "拘置所の収監者たちも\x01",
            "動揺を隠せないようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "一応、収監者の家族の安否確認は\x01",
            "こちらでもとっているが、\x01",
            "やはり無事ではなかった者もいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "……それを伝えるのは、\x01",
            "相手が犯罪者だとて心が痛いな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13F5")

    label("loc_1373")


    #C0010
    ChrTalk(
        0x9,
        (
            "彼らの中にはクロスベルに\x01",
            "家族を残しているものも多数いる。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "……その無事が伝えられない時は、\x01",
            "相手が犯罪者だとて心が痛い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F5")

    Jump("loc_1EE1")

    label("loc_13FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1496")

    #C0012
    ChrTalk(
        0x9,
        (
            "今回の脱線事故は\x01",
            "何者かの手によるもの\x01",
            "なのだろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "だとすればあまりに重罪だ。\x01",
            "罪も無い一般人にあれだけの\x01",
            "被害を与えたのだから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE1")

    label("loc_1496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_160E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156F")

    #C0014
    ChrTalk(
        0x9,
        (
            "先ほどの地の底から\x01",
            "聞こえてくるような叫び声……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        (
            "拘置所内の収監者たちも\x01",
            "ざわめいているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "この機に乗じて、などと考える\x01",
            "不届き者もいるかもしれん。\x01",
            "細心の注意を払わねばな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1609")

    label("loc_156F")


    #C0017
    ChrTalk(
        0x9,
        (
            "拘置所内の収監者たちも、\x01",
            "この異常事態に\x01",
            "ざわめいているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "この機に乗じて、などと考える\x01",
            "不届き者もいるかもしれん。\x01",
            "細心の注意を払わねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1609")

    Jump("loc_1EE1")

    label("loc_160E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_17A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170E")

    #C0019
    ChrTalk(
        0x9,
        (
            "一番近い場所で犯罪者たちを\x01",
            "見ていなければならない重圧に、\x01",
            "潰れてしまう看守も多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "正直、私も休日以外は\x01",
            "心休まるときなど無いが……\x01",
            "それでも誰かがやらねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "強靭な精神力が必要なのだ。\x01",
            "……ここで働く以上はな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179F")

    label("loc_170E")


    #C0022
    ChrTalk(
        0x9,
        (
            "一番近い場所で犯罪者たちを\x01",
            "見ていなければならない重圧に、\x01",
            "潰れてしまう看守も多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "強靭な精神力が必要なのだ。\x01",
            "……ここで働く以上はな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179F")

    Jump("loc_1EE1")

    label("loc_17A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1884")

    #C0024
    ChrTalk(
        0x9,
        (
            "独立すれば、クロスベルでの犯罪も\x01",
            "より強固に取り締まれるように\x01",
            "制度が見直されるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "課題だった外国人の犯罪者たちも、\x01",
            "確実に数を減らしていけるはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x9,
        "……実現すれば、の話だがな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1902")

    label("loc_1884")


    #C0027
    ChrTalk(
        0x9,
        (
            "独立すれば、クロスベルでの犯罪も\x01",
            "より強固に取り締まれるように\x01",
            "制度が見直されるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        "……実現すれば、の話だがな。\x02",
    )

    CloseMessageWindow()

    label("loc_1902")

    Jump("loc_1EE1")

    label("loc_1907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A32")

    #C0029
    ChrTalk(
        0x9,
        (
            "外国人が罪を犯した場合、\x01",
            "自治州法ではあまり長い期間\x01",
            "拘留させることはできない。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "それがクロスベルに\x01",
            "帝国、共和国系の犯罪者が多く入り込む\x01",
            "ひとつの要因となっているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "新市長による法改正が進められて\x01",
            "少しは改善されてきたが……\x01",
            "まだまだ完全とは言えんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AF2")

    label("loc_1A32")


    #C0032
    ChrTalk(
        0x9,
        (
            "クロスベルで外国人が罪を犯した場合、\x01",
            "自治州法ではあまり長い期間\x01",
            "拘留させることはできない。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "新市長による法改正が進められて\x01",
            "少しは改善されてきたが……\x01",
            "まだまだ完全とは言えんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF2")

    Jump("loc_1EE1")

    label("loc_1AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C00")

    #C0034
    ChrTalk(
        0x9,
        (
            "拘置所の警備は、教団事件の後\x01",
            "かなりの見直しがなされた。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "操られた警備隊に襲われたとはいえ、\x01",
            "収監者の脱獄を許してしまうなど\x01",
            "あるまじき出来事だったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "今後は一切そんな事がないよう、\x01",
            "我々もより厳重な警備に勤めるつもりだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C8E")

    label("loc_1C00")


    #C0037
    ChrTalk(
        0x9,
        (
            "拘置所の警備は、教団事件の後\x01",
            "かなりの見直しがなされた。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "今後は一切脱獄などが起こらないよう、\x01",
            "我々もより厳重な警備に勤めるつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8E")

    Jump("loc_1EE1")

    label("loc_1C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCA")

    #C0039
    ChrTalk(
        0x9,
        (
            "この拘置所に拘留されているのは、\x01",
            "重きを問わず自治州内で\x01",
            "犯罪の嫌疑を受けた者たちだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "最近では、教団事件に関わっていた\x01",
            "一部の議員やマフィアども、\x01",
            "そして例の元市長秘書などが拘留された。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "いずれ裁判の準備が整い次第、\x01",
            "彼らは自治州法に基づいた\x01",
            "裁きを受ける事になるだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E86")

    label("loc_1DCA")


    #C0042
    ChrTalk(
        0x9,
        (
            "最近では、教団事件に関わっていた\x01",
            "一部の議員やマフィアども、\x01",
            "例の元市長秘書などが拘留された。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "いずれ裁判の準備が整い次第、\x01",
            "彼らは自治州法に基づいた\x01",
            "裁きを受ける事になるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E86")

    Jump("loc_1EE1")

    label("loc_1E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1EE1")

    #C0044
    ChrTalk(
        0x9,
        "……ここは拘置所だ。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "用が無いなら、\x01",
            "あまり近づかないでもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE1")

    TalkEnd(0xFE)
    Return()

    # Function_5_1051 end

    def Function_6_1EE5(): pass

    label("Function_6_1EE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210E")

    #C0046
    ChrTalk(
        0x8,
        (
            "#01005F……ん、どうした。\x01",
            "乗らないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00012Fい、いや～……\x01",
            "いざ乗り込むとなると\x01",
            "なんだか恐れ多いというか。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#00100F私たちの専用車だなんて……\x01",
            "今までの状況を考えると、\x01",
            "どうしても尻込みするわよね。\x02\x03",

            "#00104F本当に、一課の人たちを\x01",
            "羨ましがってたのが懐かしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#01004Fクク、気持ちは\x01",
            "分からんでもないが。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x109,
        (
            "#10109Fささ、皆さん！\x01",
            "早く乗り込みましょうよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、こっちは\x01",
            "ノリノリみたいだし、\x01",
            "焦らすと悪いんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00003Fそ、それもそうだな。\x02\x03",

            "#00000Fよし、それじゃあ\x01",
            "乗り込んでみるとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_216F")

    label("loc_210E")


    #C0053
    ChrTalk(
        0x8,
        (
            "#01002Fさあ、さっさと乗り込め。\x02\x03",

            "#01004Fコイツなら、クロスベル市まで\x01",
            "あっという間だろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216F")

    TalkEnd(0xFE)
    Return()

    # Function_6_1EE5 end

    def Function_7_2173(): pass

    label("Function_7_2173")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21CC")

    #C0054
    ChrTalk(
        0xFE,
        (
            "現状、警察学校周辺に\x01",
            "異常はありません！\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "引き続き、警戒を続けます！\x02",
    )

    CloseMessageWindow()

    label("loc_21CC")

    TalkEnd(0xFE)
    Return()

    # Function_7_2173 end

    def Function_8_21D0(): pass

    label("Function_8_21D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2256")

    #C0056
    ChrTalk(
        0xFE,
        (
            "ジョーリッジ課長と一緒に、\x01",
            "警備隊が撤退して手薄となった\x01",
            "こちらに駆けつけたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        "ここは私たちに任せてちょうだい。\x02",
    )

    CloseMessageWindow()

    label("loc_2256")

    TalkEnd(0xFE)
    Return()

    # Function_8_21D0 end

    def Function_9_225A(): pass

    label("Function_9_225A")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228C")
    SetScenarioFlags(0x31, 2)

    label("loc_228C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_22CC")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22C1")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_22C7")

    label("loc_22C1")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_22C7")

    Jump("loc_22D2")

    label("loc_22CC")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_22D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_258F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_234B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_232B"),
        (SWITCH_DEFAULT, "loc_233C"),
    )


    label("loc_232B")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2346")

    label("loc_233C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2346")

    Jump("loc_258A")

    label("loc_234B")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_237F")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_237F")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23B3"),
        (1, "loc_24B7"),
        (2, "loc_2548"),
        (SWITCH_DEFAULT, "loc_2580"),
    )


    label("loc_23B3")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_23E4")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_23F4")

    label("loc_23E4")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_23F4")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_244A")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246D")
    Sound(461, 0, 100, 0)

    label("loc_246D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_248D")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_249D")

    label("loc_248D")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_249D")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_22D2")

    label("loc_24B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2529")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_24EC")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2504")

    label("loc_24EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_24FF")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2504")

    label("loc_24FF")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2504")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2543")

    label("loc_2529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2539")
    OP_AF(0xFB)
    Jump("loc_2543")

    label("loc_2539")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2543")

    Jump("loc_258A")

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2561")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_257B")

    label("loc_2561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2571")
    OP_AF(0xFB)
    Jump("loc_257B")

    label("loc_2571")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_257B")

    Jump("loc_258A")

    label("loc_2580")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_258A")

    Jump("loc_22D2")

    label("loc_258F")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_225A end

    def Function_10_259D(): pass

    label("Function_10_259D")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0058
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266C")
    OP_E2(0x2)
    MiniGame(0x6, 0x15, 0x8B10, 0xFFFFD8F0, 0xFFFFC1BC, 0x10E, 0x7D00, 0xFFFFD8F0, 0xFFFFC180)

    label("loc_266C")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_259D end

    def Function_11_2671(): pass

    label("Function_11_2671")

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

    def lambda_26FD():
        OP_95(0xFE, 12000, -10000, -21650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26FD)

    def lambda_2717():
        OP_95(0xFE, 11000, -10000, -23350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2717)

    def lambda_2731():
        OP_95(0xFE, 13000, -10000, -22650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2731)

    def lambda_274B():
        OP_95(0xFE, 12000, -10000, -24350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_274B)
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
            "#00002F#5Pさてと……\x01",
            "ここが警察学校の建物だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x105,
        "#10306F#12Pふう、やっと到着か。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#00102F#12Pさすが森の中だけあって\x01",
            "閑静#4Rかんせい#な場所にあるのね。\x02\x03",

            "#00100F課長はどこにいるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        (
            "#10104F#11Pとりあえず、正面の入口が\x01",
            "警察学校の受付になります。\x02\x03",

            "#10100F中に入ってみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00000F#5Pああ、そうしよう。\x02",
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

    # Function_11_2671 end

    def Function_12_2A19(): pass

    label("Function_12_2A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCE")
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
        "#00105F#11Pあら、そっちの建物は？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00008F#11Pああ……拘置所だよ。\x02\x03",

            "#00001F警察学校の隣の敷地に\x01",
            "併設されているんだ。\x02",
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
            "#00101F#5Pそれじゃあアーネストさんは\x01",
            "こちらの方に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#00003F#11Pああ、ダドリーさんたちが\x01",
            "収監したばかりのはずだ。\x02\x03",

            "#00000F面会を申請すれば\x01",
            "会えるかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#00108F#5Pあ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    #C0070
    ChrTalk(
        0x102,
        (
            "#00106F#5P……ううん、止めておく。\x02\x03",

            "#00108F酷い目に遭ったみたいだし、\x01",
            "今は自分を見つめ直す時間が\x01",
            "必要だと思うから……\x02\x03",

            "#00102Fいずれ機会を見て\x01",
            "おじいさまと訪ねてみるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#00002F#11Pそうか……\x01",
            "それがいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x105,
        "#10304F#12P（なんか色々あるみたいだねぇ。）\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x109,
        (
            "#10100F#6P（うん……\x01",
            "  あたしも詳しくは知らないけど。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -11250, -10000, 7200, 180)
    SetScenarioFlags(0x127, 4)
    EventEnd(0x5)
    Jump("loc_2E1C")

    label("loc_2DCE")

    EventBegin(0x1)

    #C0074
    ChrTalk(
        0x101,
        (
            "#00000Fこの先は拘置所だ。\x01",
            "今は近付かないでおこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -12250, -10000, 8310, 180)
    EventEnd(0x4)

    label("loc_2E1C")

    Return()

    # Function_12_2A19 end

    def Function_13_2E1D(): pass

    label("Function_13_2E1D")

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
        "#00005F#6Pこ、これが……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        (
            "#00105F#6P特務支援課に支給される\x01",
            "導力車……\x02",
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
        "#10302F#5Pへえ、悪くないデザインだね。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x109,
        (
            "#10101F#6Pこ、これって……\x02\x03",

            "ヴェルヌにもラインフォルトにも\x01",
            "見えないデザインラインですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "#01009F#11Pクク、正解だ。\x02\x03",

            "#01004Fこいつの型番はＸＤ－７８。\x02\x03",

            "#01002Fリベール製──\x01",
            "Ｚ Ｃ Ｆ#8Rツァイス中央工房#の新型だ。\x02",
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
        "#10107F#6Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#00011F#6PＺＣＦが導力車を\x01",
            "開発していたんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x105,
        "#10305F#5Pそんなに驚く事なのかい？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#00104F#6Pええ、リベールは\x01",
            "国土が険しいこともあって\x01",
            "導力車が普及していないの。\x02\x03",

            "#00100Fその代わり、ＺＣＦは\x01",
            "世界最高の飛行船メーカーとして\x01",
            "知られているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x109,
        (
            "#10108F#6Pそ、そのＺＣＦが\x01",
            "導力車を開発したなんて！\x02\x03",

            "#10109Fスペックは！？\x01",
            "最高時速はどのくらいですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "#01005F#11Pどうどう、落ち着け。\x02\x03",

            "#01004F何でも飛行船用の新型エンジンの\x01",
            "小型版が搭載されているらしい。\x02\x03",

            "#01002F最高時速にしたら\x01",
            "１５００セルジュは固いらしいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        "#10102F#6Pす、凄いです……！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#00005F#6P鉄道以上の速さですか……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#00100F#6Pでも、よくこんな車を\x01",
            "手配することが出来ましたね？\x02\x03",

            "まだ正式に発売もされていない\x01",
            "新型みたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "#01004F#11Pああ、本当ならお前らに\x01",
            "支給されるはずがない代物だ。\x02\x03",

            "#01002Fこいつを融通してくれたのは\x01",
            "ディーター新市長でな。\x02",
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
        "#00011F#6Pディーター市長が！？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#00105F#6Pた、確かにおじさまなら\x01",
            "ＺＣＦとの付き合いもあるから\x01",
            "納得ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        (
            "#10109F#6Pは～、さすがは\x01",
            "天下のＩＢＣ総裁ですね！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        (
            "#10309F#5Pフフ、ここまで用意がいいと\x01",
            "逆に警戒しちゃうけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "#01004F#11Pクク、まあその分、\x01",
            "働いて返せってことだろう。\x02\x03",

            "#01000F荷が重いんだったら\x01",
            "辞退することもできるぞ？\x02\x03",

            "その場合、警察で採用されてる\x01",
            "ヴェルヌ社の汎用車を回してやる。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00004F#6Pいえ……\x01",
            "ありがたく使わせてもらいます。\x02\x03",

            "#00000Fもう動かせるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "#01000F#11P整備と試運転は済んでいる。\x02\x03",

            "ほら、コイツがキーだ。\x02",
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
            "を受け取った。\x02",
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
            "#00002F#6P……はは……\x01",
            "何だかちょっと感慨深いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00104F#6Pそうね……一課の人たちを\x01",
            "羨ましがってたのが懐かしいわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0100
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、それじゃあ早速、\x01",
            "ひとっ走りしてみるかい？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0101
    ChrTalk(
        0x101,
        (
            "#00000F#12Pああ、せっかくだから\x01",
            "これでクロスベル市に戻ろう。\x02\x03",

            "ノエル、運転をお願いできるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    #C0102
    ChrTalk(
        0x109,
        "#10109F#5Pええ、お任せください！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#01004F#11Pフッ、そんじゃあ俺も\x01",
            "便乗させてもらうとするか。\x02",
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

    # Function_13_2E1D end

    def Function_14_39A2(): pass

    label("Function_14_39A2")

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

    # Function_14_39A2 end

    def Function_15_3AB0(): pass

    label("Function_15_3AB0")


    def lambda_3AB5():
        OP_95(0xFE, 16500, -10000, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AB5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    WaitChrThread(0xFE, 1)

    def lambda_3AF8():
        OP_9E(0xFE, 0x4074, 0xFFFFCF2C, 0xFFFEA070, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AF8)
    Sleep(2600)
    StopSound(468, 1000, 80)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x0)
    Sleep(300)
    Sound(492, 0, 100, 0)
    Sleep(700)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_3B3B():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B3B)
    Sound(457, 0, 100, 0)
    Sound(494, 0, 80, 0)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    OP_71(0x5, 0xB5, 0xF0, 0x1, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_3AB0 end

    def Function_16_3B77(): pass

    label("Function_16_3B77")

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

    def lambda_3E50():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E50)
    Sleep(100)

    def lambda_3E68():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3E68)
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

    def lambda_3F68():
        OP_9B(0x0, 0xFE, 0x5, 0x2EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F68)
    Sleep(100)

    def lambda_3F80():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3F80)
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
        "#00005F#11Pガルシア……？\x02",
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
            "#11103F#11P──馴れ合いはここまでだ。\x02\x03",

            "#11100Fここから先は、\x01",
            "てめぇ一人で行くんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#00011F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x10B,
        (
            "#11104F#11Pこれでも一応、\x01",
            "ルバーチェの“若頭”でな。\x02\x03",

            "#11101F手下は勿論、あの会長だって\x01",
            "放って逃げるわけにはいかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00013F#11Pま、待ってくれ！\x02\x03",

            "だったらどうして\x01",
            "ここまで付き合ってくれて……\x02\x03",

            "#00007Fそれに幾らあんたでも\x01",
            "一人じゃどうしようもないだろ！？\x02\x03",

            "だったら俺も──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #C0109
    ChrTalk(
        0x10B,
        "#11107F#5S#11P履き違えるな、小僧！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0110
    ChrTalk(
        0x10B,
        (
            "#11103F#11P真実を見極める……\x01",
            "てめぇはそう言ったはずだ。\x02\x03",

            "捕まった仲間を解放して\x01",
            "あのガキを取り戻すとな。\x02\x03",

            "#11100F……こんな場所で\x01",
            "グズグズしてる暇はあんのか？\x02",
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
            "#00003F#5P──ありがとう、ガルシア。\x02\x03",

            "#00008F立場上、あんたたちの脱走を\x01",
            "歓迎する事はできないけど……\x02\x03",

            "#00001Fどうか無事でいてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x10B,
        (
            "#11104F#11Pハッ……\x01",
            "無用な心配ってモンだぜ。\x02",
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

    def lambda_444A():
        OP_9B(0x0, 0xFE, 0x5, 0x2AF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_444A)
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
            "#11104F#11Pロイド・バニングス……\x01",
            "……あの野郎の弟か。\x02\x03",

            "#11100Fなかなか良い面構えに\x01",
            "なってきたじゃねぇか。\x02",
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
        "#2Sいたぞ……！\x05\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    Sleep(500)
    SetMessageWindowPos(90, 50, -1, -1)

    #A0116
    AnonymousTalk(
        0x13,
        "#2S絶対に逃がすな！\x05\x02",
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
        "#11102F#11Pクク、地の利は十分だ……\x02",
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
            "#11107F#11P#4Sこの《キリングベア》の鉄拳、\x01",
            "存分に味わってもらおうかあッ！\x02",
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

    # Function_16_3B77 end

    def Function_17_4814(): pass

    label("Function_17_4814")

    SetChrPos(0xFE, 2550, -10000, -1700, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_17_4814 end

    def Function_18_4844(): pass

    label("Function_18_4844")

    SetChrPos(0xFE, 700, -10000, -1250, 135)
    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x1770, 0x0)
    Return()

    # Function_18_4844 end

    def Function_19_4874(): pass

    label("Function_19_4874")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_488F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_19_4874")

    label("loc_488F")

    Return()

    # Function_19_4874 end

    def Function_20_4890(): pass

    label("Function_20_4890")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48A9")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_20_4890")

    label("loc_48A9")

    Return()

    # Function_20_4890 end

    def Function_21_48AA(): pass

    label("Function_21_48AA")

    OP_82(0x64, 0x12C, 0xBB8, 0x1F4)
    Sleep(500)

    label("loc_48BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48E2")
    OP_82(0x0, 0x1E, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("loc_48BE")

    label("loc_48E2")

    Return()

    # Function_21_48AA end

    def Function_22_48E3(): pass

    label("Function_22_48E3")


    def lambda_48E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48E8)
    OP_9B(0x0, 0xFE, 0x0, 0x7530, 0xFA0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_48E3 end

    def Function_23_4908(): pass

    label("Function_23_4908")

    OP_95(0xFE, -16000, -10050, 15000, 5000, 0x1)
    OP_95(0xFE, 11500, -10000, -15650, 5000, 0x0)
    Return()

    # Function_23_4908 end

    def Function_24_4931(): pass

    label("Function_24_4931")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_494C")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_24_4931")

    label("loc_494C")

    Return()

    # Function_24_4931 end

    def Function_25_494D(): pass

    label("Function_25_494D")

    Sound(910, 0, 30, 0)
    Sleep(800)
    Sound(909, 0, 30, 0)
    Sleep(1400)
    Sound(909, 0, 20, 0)
    Sleep(850)
    Sound(910, 0, 20, 0)
    Return()

    # Function_25_494D end

    def Function_26_496F(): pass

    label("Function_26_496F")

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
            "#6P#00306Fやれやれ、思ったより\x01",
            "元気そうだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        (
            "#5P#00100Fそうね、あの調子なら\x01",
            "近い内に回復できるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B14")

    #C0121
    ChrTalk(
        0x105,
        (
            "#6P#10400Fそれにしても、意外だったね。\x01",
            "彼みたいな人が僕らを\x01",
            "激励してくれるなんてさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE9")

    label("loc_4B14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B7B")

    #C0122
    ChrTalk(
        0x106,
        (
            "#6P#10703Fでも、意外でした。\x01",
            "彼のような人が私たちを\x01",
            "激励してくれるなんて……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE9")

    label("loc_4B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BE9")

    #C0123
    ChrTalk(
        0x109,
        (
            "#6P#10100Fそれにしても、意外でしたね。\x01",
            "元マフィアがあたしたちを\x01",
            "激励してくれるなんて……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE9")


    #C0124
    ChrTalk(
        0x101,
        (
            "#00000Fああ……色々な事件を通じて、\x01",
            "彼も変わったのかもしれないな。\x02",
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
        "#00005Fな、なんだよ皆？\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x103,
        "#12P#00211Fいえ、なぜ他人事なのかと。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        "#00102F多分、あなたの影響だと思うけど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0128
    ChrTalk(
        0x101,
        "#00005F……へ……！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#6P#00306Fやれやれ、これだから\x01",
            "天然ジゴロってやつはよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DF9")

    #C0130
    ChrTalk(
        0x10A,
        (
            "#6P#00602F……ヤツが言っていた\x01",
            "ガイに似ているという言葉も、\x01",
            "あながち間違いではないらしい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E92")

    label("loc_4DF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E49")

    #C0131
    ChrTalk(
        0x109,
        (
            "#6P#10102Fふふ、ロイドさんも\x01",
            "本当に相変わらずですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E92")

    label("loc_4E49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E92")

    #C0132
    ChrTalk(
        0x106,
        (
            "#6P#10702Fあはは……\x01",
            "ロイドさんも相変わらずですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E92")

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

    # Function_26_496F end

    def Function_27_4EC2(): pass

    label("Function_27_4EC2")

    EventBegin(0x1)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00000Fおっと、こっちは森林道方面だな。\x01",
            "導力車はガレージ前だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11900, -10000, -15540, 0)
    EventEnd(0x4)
    Return()

    # Function_27_4EC2 end

    def Function_28_4F1D(): pass

    label("Function_28_4F1D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西・クロスベル警察学校\x01",
            "北・ノックス森林地帯入り口\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_4F1D end

    SaveToFile()

Try(main)
