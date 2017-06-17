from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m1000.bin",                # FileName
        "m1000",                    # MapName
        "m1000",                    # Location
        0x006B,                     # MapIndex
        "ed7202",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 4000, 3000, -9000, 0, 0, 1, 107, 0, 1, 0, 2],
    )

    BuildStringList((
        "m1000",                  # 0
        "诺艾尔上士",             # 1
        "车",                     # 2
        "SE控制",                 # 3
        "乌尔斯拉间道",           # 4
    ))

    AddCharChip((
        "chr/ch00800.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
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

    DeclNpc(37250,   -13199,  98250,   0,    389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  6.5,                   27.799999237060547,    -5.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.6500000357627869,   -9.266666412353516,    1.0,                   1.0])
    DeclEvent(0x0000, 0, 13,  34.599998474121094,    85.44999694824219,     -14.199999809265137,   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.4599997997283936,   -28.483333587646484,   2.8399999141693115,    1.0])
    DeclEvent(0x0000, 0, 7,   34.599998474121094,    71.5999984741211,      -14.199999809265137,   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.4599997997283936,   -23.866666793823242,   2.8399999141693115,    1.0])
    DeclEvent(0x0000, 0, 8,   34.599998474121094,    104.0,                 -14.199999809265137,   56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.919999599456787,    -34.66666793823242,    2.8399999141693115,    1.0])
    DeclEvent(0x0000, 0, 10,  6.5,                   7.0,                   -5.0,                  2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   -0.6500000357627869,   -0.699999988079071,    0.5,                   1.0])

    DeclActor(36310,   -13200,  85240,   1200,    36310,   -11700,  85240,   0x007C, 0,  15, 0x0000)
    DeclActor(44360,   -13190,  93720,   1200,    44360,   -11190,  93720,   0x007C, 0,  5,  0x0000)
    DeclActor(5980,    -3710,   24960,   5000,    5980,    -3710,   24960,   0x007C, 0,  14, 0x0000)

    PlaceName(-1.100000023841858, 0.0, -30.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(45.29999923706055, 0.0, 95.25, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_414",          # 00, 0
        "Function_1_4CC",          # 01, 1
        "Function_2_54F",          # 02, 2
        "Function_3_74F",          # 03, 3
        "Function_4_D95",          # 04, 4
        "Function_5_E84",          # 05, 5
        "Function_6_E92",          # 06, 6
        "Function_7_1024",         # 07, 7
        "Function_8_1370",         # 08, 8
        "Function_9_13D2",         # 09, 9
        "Function_10_13D8",        # 0A, 10
        "Function_11_13E1",        # 0B, 11
        "Function_12_1690",        # 0C, 12
        "Function_13_169A",        # 0D, 13
        "Function_14_2596",        # 0E, 14
        "Function_15_314C",        # 0F, 15
    ))


    def Function_0_414(): pass

    label("Function_0_414")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_454"),
        (1, "loc_460"),
        (2, "loc_46C"),
        (3, "loc_478"),
        (4, "loc_484"),
        (5, "loc_490"),
        (6, "loc_49C"),
        (SWITCH_DEFAULT, "loc_4A8"),
    )


    label("loc_454")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_460")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_46C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_478")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_484")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_490")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_49C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_4A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_4CB")

    Return()

    # Function_0_414 end

    def Function_1_4CC(): pass

    label("Function_1_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E2")
    SetMapFlags(0x10000000)
    Event(0, 9)

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F0")
    Jump("loc_536")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_END)), "loc_523")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 43020, -13200, 93370, 34)

    label("loc_51E")

    Jump("loc_536")

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_END)), "loc_536")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_54E")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_54E")

    Return()

    # Function_1_4CC end

    def Function_2_54F(): pass

    label("Function_2_54F")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58E")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BB")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B6")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_5BB")

    label("loc_5B6")

    ModifyEventFlags(1, 3, 0x80)

    label("loc_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CF")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_610")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFB, 0xC4, 0xA6, 0x14, 0x190, 0x0)
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    Jump("loc_62C")

    label("loc_610")

    SetMapObjFrame(0xFF, "allback", 0x2, "blue")
    SetMapObjFrame(0xFF, "sky", 0x2, "blue")

    label("loc_62C")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_662")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    Jump("loc_698")

    label("loc_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_END)), "loc_67C")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_698")

    label("loc_67C")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    OP_66(0x0, 0x1)

    label("loc_698")

    SetMapObjFlags(0x0, 0x4)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C7")
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_66(0x1, 0x1)

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FA")
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_66(0x1, 0x1)
    Jump("loc_6FF")

    label("loc_6FA")

    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_6FF")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_711")
    Jump("loc_74E")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_74E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_72B")
    Jump("loc_74E")

    label("loc_72B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_73D")
    Jump("loc_74E")

    label("loc_73D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_74E")
    OP_66(0x2, 0x1)

    label("loc_74E")

    Return()

    # Function_2_54F end

    def Function_3_74F(): pass

    label("Function_3_74F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_804")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_76E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC")

    Menu(
        0,
        32,
        26,
        1,
        (
            "在此处休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E4")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_7F7")

    label("loc_7E4")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F7")

    Jump("loc_76E")

    label("loc_7FC")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    label("loc_804")

    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_817")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8D")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2A")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A5")
    MenuCmd(1, 1, "★克洛斯贝尔市·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_8C1")

    label("loc_8A5")

    MenuCmd(1, 1, "　克洛斯贝尔市·中央广场")

    label("loc_8C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F3")
    MenuCmd(1, 1, "★克洛斯贝尔市·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_90D")

    label("loc_8F3")

    MenuCmd(1, 1, "　克洛斯贝尔市·东出口")

    label("loc_90D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93F")
    MenuCmd(1, 1, "★克洛斯贝尔市·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_959")

    label("loc_93F")

    MenuCmd(1, 1, "　克洛斯贝尔市·西出口")

    label("loc_959")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98B")
    MenuCmd(1, 1, "★克洛斯贝尔市·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_9A5")

    label("loc_98B")

    MenuCmd(1, 1, "　克洛斯贝尔市·南出口")

    label("loc_9A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D7")
    MenuCmd(1, 1, "★克洛斯贝尔市·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_9F1")

    label("loc_9D7")

    MenuCmd(1, 1, "　克洛斯贝尔市·北出口")

    label("loc_9F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A19")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_A29")

    label("loc_A19")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_A29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A51")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_A61")

    label("loc_A51")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_A61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8F")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_AA5")

    label("loc_A8F")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_AA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_AE1")

    label("loc_ACF")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_AE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0B")
    MenuCmd(1, 1, "★矿山镇玛因兹")
    MenuCmd(3, 1, 0x9)
    Jump("loc_B1D")

    label("loc_B0B")

    MenuCmd(1, 1, "　矿山镇玛因兹")

    label("loc_B1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4D")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_B65")

    label("loc_B4D")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_B65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8B")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_B99")

    label("loc_B8B")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_B99")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1B")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C6E"),
        (1, "loc_C7C"),
        (2, "loc_C8A"),
        (3, "loc_C98"),
        (4, "loc_CA6"),
        (5, "loc_CB4"),
        (6, "loc_CC2"),
        (7, "loc_CD0"),
        (8, "loc_CDE"),
        (9, "loc_CEC"),
        (10, "loc_CFA"),
        (11, "loc_D08"),
        (SWITCH_DEFAULT, "loc_D16"),
    )


    label("loc_C6E")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_C7C")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_C8A")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_C98")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_CA6")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_CB4")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_CC2")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_CD0")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_CDE")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_CEC")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_CFA")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_D08")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16")

    label("loc_D16")

    Jump("loc_D25")

    label("loc_D1B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D25")

    Jump("loc_D88")

    label("loc_D2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D75")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_D88")

    label("loc_D75")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D88")

    Jump("loc_817")

    label("loc_D8D")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_74F end

    def Function_4_D95(): pass

    label("Function_4_D95")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 42720, -13190, 92310, 215)
    SetChrPos(0x1, 42720, -13190, 92310, 215)
    SetChrPos(0x2, 42720, -13190, 92310, 215)
    SetChrPos(0x3, 42720, -13190, 92310, 215)
    SetChrPos(0x4, 42720, -13190, 92310, 215)
    SetChrPos(0x5, 42720, -13190, 92310, 215)
    Sleep(1)
    OP_68(42720, -11190, 92310, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E69")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_E6F")

    label("loc_E69")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_E6F")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_D95 end

    def Function_5_E84(): pass

    label("Function_5_E84")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 3)
    Return()

    # Function_5_E84 end

    def Function_6_E92(): pass

    label("Function_6_E92")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0x8,
        (
            "#0500F各位辛苦啦！\x01",
            "……要立即重新开始\x01",
            "对遗迹的探索吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "重新开始\x01",            # 0
            "还要再准备一下\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA3")

    #C0002
    ChrTalk(
        0x101,
        "#0000F嗯，差不多也该继续去探索了。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#0500F了解。\x01",
            "那我们就向『塔』\x01",
            "的内部出发吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    AddParty(0x8, 0xFF, 0xFF)
    OP_49()
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    FadeToBright(250, 0)
    OP_0D()
    Jump("loc_1020")

    label("loc_FA3")


    #C0004
    ChrTalk(
        0x8,
        (
            "#0503F是吗。\x01",
            "对手应该相当狡猾危险，\x01",
            "还是先整理一下装备比较好呢。\x02\x03",

            "#0501F我就在这里待命，\x01",
            "各位准备好之后，就来和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1020")

    TalkEnd(0xFE)
    Return()

    # Function_6_E92 end

    def Function_7_1024(): pass

    label("Function_7_1024")

    EventBegin(0x0)
    Fade(500)
    OP_68(34420, -11200, 71170, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14220, 0)
    SetChrPos(0x101, 34730, -13200, 70340, 350)
    SetChrPos(0x102, 33310, -13200, 70960, 35)
    SetChrPos(0x103, 36380, -13200, 71570, 305)
    SetChrPos(0x104, 36730, -13200, 73240, 260)
    SetChrPos(0x109, 34420, -13200, 73610, 170)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0005
    ChrTalk(
        0x109,
        (
            "#0505F啊，各位，\x01",
            "要返回市里吗？\x02\x03",

            "#0500F抱歉，我必须要\x01",
            "在这里守卫，防止民间人士\x01",
            "随意入内。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#0005F噢，是吗……\x01",
            "我们是想先回去一趟，\x01",
            "整理好装备之后再回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0306F哈，既然是任务，那也没办法了啊。\x02\x03",

            "#0300F诺艾尔上士，我们就暂时分开行动吧。\x01",
            "在我们补充好装备之前，\x01",
            "请你先在这里稍等。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#0500F了解。\x01",
            "我就在装甲车旁边待命，\x01",
            "请各位多加小心！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#0000F嗯，诺艾尔你也要小心啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x0, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1261")
    OP_32(0x0, 0xFC, 0x1)
    OP_32(0x0, 0x2, 0x1)

    label("loc_1261")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x1, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_127B")
    OP_32(0x1, 0xFC, 0x1)
    OP_32(0x1, 0x2, 0x1)

    label("loc_127B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x2, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1295")
    OP_32(0x2, 0xFC, 0x1)
    OP_32(0x2, 0x2, 0x1)

    label("loc_1295")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x3, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12AF")
    OP_32(0x3, 0xFC, 0x1)
    OP_32(0x3, 0x2, 0x1)

    label("loc_12AF")

    OP_32(0x8, 0xFC, 0x0)
    OP_32(0x8, 0xFE, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_49()
    OP_68(34730, -11200, 70340, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 34730, -13200, 70340, 170)
    SetChrPos(0x1, 34730, -13200, 70340, 170)
    SetChrPos(0x2, 34730, -13200, 70340, 170)
    SetChrPos(0x3, 34730, -13200, 70340, 170)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 43020, -13200, 93370, 34)
    BeginChrThread(0x8, 0, 0, 0)
    FadeToBright(250, 0)
    OP_0D()
    EventEnd(0x6)
    Return()

    # Function_7_1024 end

    def Function_8_1370(): pass

    label("Function_8_1370")

    EventBegin(0x1)

    #C0010
    ChrTalk(
        0x101,
        (
            "#0005F啊……\x02\x03",

            "#0000F如果要进入塔内探索，\x01",
            "一定要先叫上诺艾尔上士啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 34460, -13190, 100280, 170)
    EventEnd(0x4)
    Return()

    # Function_8_1370 end

    def Function_9_13D2(): pass

    label("Function_9_13D2")

    ClearMapFlags(0x10000000)
    Return()

    # Function_9_13D2 end

    def Function_10_13D8(): pass

    label("Function_10_13D8")

    SetScenarioFlags(0x87, 6)
    ModifyEventFlags(0, 4, 0x80)
    Return()

    # Function_10_13D8 end

    def Function_11_13E1(): pass

    label("Function_11_13E1")

    EventBegin(0x0)
    OP_E0(0x1)
    OP_68(35980, -5200, 92810, 0)
    MoveCamera(22, 6, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(93640, 0)
    SetChrPos(0x101, 7280, -3700, 24800, 19)
    SetChrPos(0x102, 8330, -3700, 23560, 19)
    SetChrPos(0x103, 6260, -3700, 24230, 19)
    SetChrPos(0x104, 7250, -3700, 22830, 19)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 37250, -13200, 98250, 0)
    SetChrFlags(0x8, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    BeginChrThread(0xA, 1, 0, 12)
    Fade(1000)
    OP_68(27780, -5200, 96400, 10000)
    PlaceName2(340, 40, "c_plac28", 0x0, 5000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(35000, -10600, 104630, 0)
    MoveCamera(25, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    OP_68(35000, -10600, 87130, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    ClearChrFlags(0x8, 0x8000)
    OP_68(5190, -1800, 22500, 0)
    MoveCamera(20, 5, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21370, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_1583")

    #C0011
    ChrTalk(
        0x101,
        "#0005F#6P那是……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0105F#12P那莫非……\x01",
            "是警备队的车辆吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F7")

    label("loc_1583")


    #C0013
    ChrTalk(
        0x101,
        (
            "#0000F#6P『星见之塔』……\x01",
            "果然是在这里吗。\x02\x03",

            "#0005F不过，那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0105F#12P看起来好像是警备队的车辆呢……\x02",
    )

    CloseMessageWindow()

    label("loc_15F7")


    #C0015
    ChrTalk(
        0x104,
        (
            "#0303F#12P嗯，是警备队使用的\x01",
            "轻型装甲机动车啊。\x02\x03",

            "#0301F为什么开到这里来了？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#0200F#6P不如直接去问一问吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6500, -3700, 24300, 19)
    SetScenarioFlags(0x84, 1)
    EndChrThread(0xA, 0x1)
    OP_E0(0x0)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_11_13E1 end

    def Function_12_1690(): pass

    label("Function_12_1690")

    Sleep(2000)
    Sound(866, 0, 100, 0)
    Return()

    # Function_12_1690 end

    def Function_13_169A(): pass

    label("Function_13_169A")

    EventBegin(0x0)
    Fade(1000)
    OP_68(37250, -12300, 98250, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 3000)
    SetChrPos(0x101, 36650, -13200, 89750, 0)
    SetChrPos(0x102, 37850, -13200, 89750, 0)
    SetChrPos(0x103, 36650, -13200, 88450, 0)
    SetChrPos(0x104, 37850, -13200, 88450, 0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 37250, -13200, 98250, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrSubChip(0x8, 0x0)
    ModifyEventFlags(0, 1, 0x80)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis202.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    OP_0D()
    OP_6F(0x79)
    Sound(1494, 255, 85, 0)    #voice#Noel
    Sleep(800)

    #C0017
    ChrTalk(
        0x8,
        (
            "#0506F#11P这究竟是谁干的呢……？\x02\x03",

            "#0508F实在是想不出谁会对\x01",
            "这种地方感兴趣……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#1P喂～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_68(37250, -12300, 97250, 3000)

    def lambda_1846():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1846)
    Sleep(50)

    def lambda_185E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_185E)
    Sleep(50)

    def lambda_1876():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1876)
    Sleep(50)

    def lambda_188E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_188E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0019
    ChrTalk(
        0x8,
        "#0505F#5P……你们是……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0000F#12P果然是你啊。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0302F#12P哈哈，在奇妙的地方重逢了呢。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#0505F#5P罗伊德警官、兰迪前辈？\x02\x03",

            "#0502F连艾莉小姐和小缇欧也……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0102F#2P好久不见了，\x01",
            "诺艾尔上士。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#0204F#12P上次真是十分感谢……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0025
    AnonymousTalk(
        0x8,
        (
            "呵呵，好久不见了。\x02\x03",

            "不过……\x01",
            "各位为什么要来这里呢？\x02\x03",

            "这种地方一般并不会\x01",
            "有什么人来呢……\x02",
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

    #C0026
    ChrTalk(
        0x101,
        (
            "#0006F#12P嗯，算是稍微有些隐情吧。\x02\x03",

            "#0001F先不说这个，那边的\x01",
            "路障是怎么回事啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#0506F#5P那个，看起来好像\x01",
            "是被人为破坏的。\x02\x03",

            "#0501F原本就是因为这座塔很危险，\x01",
            "所以警备队才将它封锁……\x02\x03",

            "我也是在定期巡逻的途中\x01",
            "正好发现的。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0013F#12P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#0303F#12P路障恰好在这种\x01",
            "时候被破坏掉吗……\x02\x03",

            "#0301F犯人十有八九就是那个人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#0103F#2P是啊……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#0505F#5P？？？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0001F#12P嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将至今为止的案情经过\x01",
            "向诺艾尔上士做了详细的说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x8,
        (
            "#0507F#5P从卡尔瓦德的东方人街\x01",
            "来的暗杀者……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#0103F#2P嗯……是的。\x02\x03",

            "#0101F那个人留言给我们说，\x01",
            "会在这座塔中等着我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0003F#12P我们抱着姑且信之\x01",
            "的想法前来调查……\x02\x03",

            "#0001F现在看来，犯人好像\x01",
            "还真的在这里等着我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#0506F#5P呼～市里居然发生了这种事……\x02\x03",

            "#0501F那么，各位打算怎么办呢？\x02\x03",

            "总不会真的要\x01",
            "直接进去赴约吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0000F#12P嗯……\x01",
            "正是打算进去和对方会面。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0039
    ChrTalk(
        0x8,
        (
            "#0505F#5P哎，可、可是……\x02\x03",

            "#0501F对方是个很危险的犯罪者吧？\x01",
            "说不定布下了什么陷阱呢……\x02\x03",

            "不然还是先去拜托副司令，\x01",
            "向警备队那边请求支援……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#0303F#12P不，对方是职业杀手。\x02\x03",

            "如果随便出动大部队，恐怕只会\x01",
            "让他马上察觉到，并立刻逃走吧。\x02\x03",

            "#0301F在这种时候，小队行动才是正确做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#0506F#5P这、这个……\x01",
            "好像也有道理呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0042
    ChrTalk(
        0x8,
        (
            "#0503F#5P……明白了。\x01",
            "既然如此，我就不阻止各位了。\x02\x03",

            "#0507F但是……\x01",
            "请让我也助各位一臂之力吧！\x02",
        )
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
    Sleep(1000)

    #C0043
    ChrTalk(
        0x101,
        "#0011F#12P哎！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#0105F#2P可、可是……这样好吗？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "#0503F#5P毕竟，这座塔的管理工作\x01",
            "也是由克洛斯贝尔警备队负责的。\x02\x03",

            "总不能只让各位\x01",
            "前去犯险。\x02\x03",

            "#0500F而且，各位平时\x01",
            "也总是关照芙兰……\x02\x03",

            "作为回报，诺艾尔·希卡上士\x01",
            "一定会尽全力援助各位！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0006F#12P嗯、嗯～……\x02\x03",

            "#0002F不过，其实是你妹妹\x01",
            "经常关照我们才对呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0304F#12P哈，这样不是也挺好的吗？\x02\x03",

            "#0302F上士也具备相当的实力呢，\x01",
            "我们就接受她的帮助吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        (
            "#0204F#12P是啊。\x02\x03",

            "#0202F如果有了后援，\x01",
            "也能减轻我们的压力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        (
            "#0103F#2P问题就剩下──『银』会不会\x01",
            "对警备队员有所警戒呢……\x02\x03",

            "#0100F不过，只有一名的话，应该没什么问题吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0004F#12P……是啊。\x02\x03",

            "#0000F诺艾尔上士──\x01",
            "那就请你多多指教了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#0502F#5P嗯，彼此彼此！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "诺艾尔上士以临时队员\x01",
            "的身份加入了队伍中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当队伍中的成员超过四人时，\x01",
            "多出的队员就会被默认为\x01",
            "『支援队员』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『支援队员』会在战场区域外待命，\x01",
            "偶尔出现在ＡＴ顺序栏中，当顺序轮到时，\x01",
            "就会展开各种各样的支援行动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "队伍成员可以在\x01",
            "菜单中的[TACTICS]中进行更替。\x01",
            "可以将诺艾尔设置为『战斗成员』，\x01",
            "并将罗伊德、艾莉、缇欧、兰迪\x01",
            "中的任意一人设置为『援护角色』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    AddParty(0x8, 0xFF, 0xFF)
    OP_49()
    OP_32(0x8, 0x0, 0x12)
    RemoveCraft(0x8, 0xFFFF)
    OP_38(0x8, 0x80, 0x2)
    OP_38(0x8, 0x81, 0x1)
    OP_38(0x8, 0x82, 0x1)
    OP_38(0x8, 0x83, 0x1)
    OP_38(0x8, 0x84, 0x1)
    OP_38(0x8, 0x85, 0x1)
    OP_38(0x8, 0x86, 0x1)
    OP_42(0x8, 0x44C, 0xFF)
    OP_42(0x8, 0x5E1, 0xFF)
    OP_42(0x8, 0x645, 0xFF)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0x122)
    SetChrChipPat(0x8, 0x6, 0x122)
    AddCraft(0x8, 0x144)
    OP_42(0x8, 0x6E, 0x0)
    OP_42(0x8, 0x91, 0x4)
    OP_42(0x8, 0x7A, 0x3)
    OP_42(0x8, 0x7F, 0x2)
    OP_42(0x8, 0x65, 0x1)
    OP_42(0x8, 0x6B, 0x6)
    OP_42(0x8, 0xAC, 0x5)
    AddCraft(0x0, 0x12C)
    AddCraft(0x1, 0x12F)
    AddCraft(0x2, 0x132)
    AddCraft(0x3, 0x135)
    OP_CA(0x1, 0xFF, 0x0)
    OP_37()
    SetChrPos(0x0, 34150, -13190, 97220, 0)
    ModifyEventFlags(1, 2, 0x80)
    SetScenarioFlags(0x84, 2)
    OP_29(0x43, 0x1, 0x8)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_13_169A end

    def Function_14_2596(): pass

    label("Function_14_2596")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(7760, 1400, 36490, 0)
    MoveCamera(16, -4, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24350, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, 4360, -3710, 22360, 19)
    SetChrPos(0x102, 5820, -3710, 23960, 19)
    SetChrPos(0x103, 7950, -3710, 23220, 19)
    SetChrPos(0x104, 6240, -3710, 21720, 19)
    OP_68(7890, -2300, 27250, 6000)
    MoveCamera(17, 4, 0, 6000)
    SetCameraDistance(20950, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0x101,
        (
            "#6P#0001F星见之塔吗……\x01",
            "是和『银』交战过的场所呢。\x02\x03",

            "#0003F像这样从外部眺望时，\x01",
            "倒是个很美丽的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#6P#0108F但一想到内部的样子，\x01",
            "就有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#12P#0200F这个场所，果然也应该\x01",
            "彻底进行一次正式调查吧？\x02\x03",

            "#0203F那些不可理解的现象，\x01",
            "如果就一直这么放着不管，\x01",
            "总觉得很不舒服。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#0303F不过调查工作是\x01",
            "警备队的管辖范围……\x01",
            "恐怕很难把问题解决吧。\x02\x03",

            "#0301F因为警备队的司令\x01",
            "是个白痴，对升官没好处的事，\x01",
            "他全都不会管的。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#6P#0003F……问题真是堆积如山呢。\x02\x03",

            "#0000F总之……\x01",
            "格蕾丝小姐委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E0B")
    TurnDirection(0x101, 0x102, 500)

    #C0061
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么艾莉，\x01",
            "可以拜托你来拍照吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0062
    ChrTalk(
        0x102,
        (
            "#6P#0108F哎，好的。\x01",
            "虽然我没什么自信……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0063
    ChrTalk(
        0x104,
        (
            "#12P#0300F哪里哪里，应该没问题吧。\x02\x03",

            "只要看看镜头，\x01",
            "然后咔嚓一下拍下来\x01",
            "不就搞定了嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0064
    ChrTalk(
        0x102,
        (
            "#6P#0106F我说你啊……\x01",
            "要拍出好照片，\x01",
            "可没有那么简单哦。\x02\x03",

            "#0100F要注意确认\x01",
            "拍摄对象有没有被收入取景框中，\x01",
            "还要构思摄影角度……\x02\x03",

            "而且受到天气和风的影响，\x01",
            "照片所呈现出的感觉也会有很大不同。\x02\x03",

            "有时只要错过那一瞬的时机，\x01",
            "就再也拍不到\x01",
            "那么好的风景了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#12P#0200F外行和专家所拍出的照片，\x01",
            "差别可是一目了然的。\x02\x03",

            "#0203F不过，某些粗神经的人\x01",
            "大概无法理解这种细致的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0066
    ChrTalk(
        0x104,
        (
            "#12P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#6P#0000F好啦好啦，\x01",
            "总之就交给艾莉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#6P#0100F那么……\x01",
            "我来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x13, 0x1F4)
    OP_93(0x101, 0x13, 0x1F4)
    OP_93(0x103, 0x13, 0x1F4)
    OP_93(0x104, 0x13, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "为了保险起见，我多拍了几张。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#6P#0000F看样子，似乎已经拍好了呢。\x02\x03",

            "感觉怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#6P#0100F在没有实际显像出来之前，\x01",
            "还无法确定……\x02\x03",

            "不过，我觉得至少\x01",
            "不会很差吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        (
            "#12P#0200F艾莉前辈似乎\x01",
            "找回感觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x104,
        (
            "#12P#0300F哼……\x01",
            "反正只有我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#6P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3115")

    label("loc_2E0B")

    TurnDirection(0x101, 0x102, 500)

    #C0075
    ChrTalk(
        0x101,
        (
            "#6P#0000F那么……\x01",
            "艾莉，麻烦你拍照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        "#6P#0100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x13, 0x1F4)
    OP_93(0x101, 0x13, 0x1F4)
    OP_93(0x103, 0x13, 0x1F4)
    OP_93(0x104, 0x13, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0077
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "大概就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2F8D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2FA4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2FBB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2FD2")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2FE9")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_3000")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3000")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_3017")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3017")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_302E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_302E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_3045")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3045")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D5")

    #C0078
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "这样一来，就拍完了格蕾丝小姐\x01",
            "所要求的五张照片了。\x01",
            "现在随时都可以去交付了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3115")

    label("loc_30D5")


    #C0079
    ChrTalk(
        0x101,
        (
            "#6P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3115")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5980, -3710, 24960, 19)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x8)
    Sleep(500)
    OP_65(0x2, 0x1)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_14_2596 end

    def Function_15_314C(): pass

    label("Function_15_314C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326E")

    #C0080
    ChrTalk(
        0x103,
        "#0200F这里好像禁止进入呢。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        (
            "#0300F这里的路障是\x01",
            "克洛斯贝尔警备队设置的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0000F嗯，这是一座名叫『星见之塔』\x01",
            "的中世纪建筑哦。\x02\x03",

            "有些部分已经坍塌了，\x01",
            "所以平时好像是禁止入内的。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0100F我虽然听说过这座塔，\x01",
            "但也从没来过呢。\x02\x03",

            "好像都已经封锁\x01",
            "将近十年了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x87, 4)
    Jump("loc_32B3")

    label("loc_326E")

    SetChrName("")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "道路被路障\x01",
            "封锁了。\x02\x03",

            "上面贴有克洛斯贝尔\x01",
            "警备队的警示单。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_32B3")

    TalkEnd(0xFF)
    Return()

    # Function_15_314C end

    SaveToFile()

Try(main)
