from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ノエル曹長",             # 1
        "車",                     # 2
        "SE制御",                 # 3
        "ウルスラ間道方面",       # 4
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

    PlaceName(-1.100000023841858, 0.0, -30.0, 0x0000, 0x0000, "ウルスラ間道方面")
    PlaceName(45.29999923706055, 0.0, 95.25, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_414",          # 00, 0
        "Function_1_4CC",          # 01, 1
        "Function_2_54F",          # 02, 2
        "Function_3_74F",          # 03, 3
        "Function_4_DB7",          # 04, 4
        "Function_5_EA6",          # 05, 5
        "Function_6_EB4",          # 06, 6
        "Function_7_107E",         # 07, 7
        "Function_8_13F8",         # 08, 8
        "Function_9_1460",         # 09, 9
        "Function_10_1466",        # 0A, 10
        "Function_11_146F",        # 0B, 11
        "Function_12_174E",        # 0C, 12
        "Function_13_1758",        # 0D, 13
        "Function_14_27FC",        # 0E, 14
        "Function_15_34BE",        # 0F, 15
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_76E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_804")

    Menu(
        0,
        32,
        26,
        1,
        (
            "ここで休憩をする\x01",      # 0
            "やめる\x01",                # 1
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EC")
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
    Jump("loc_7FF")

    label("loc_7EC")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FF")

    Jump("loc_76E")

    label("loc_804")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    label("loc_80C")

    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAF")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4C")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B5")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_8D1")

    label("loc_8B5")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_8D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_903")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_91D")

    label("loc_903")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_91D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_969")

    label("loc_94F")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99B")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_9B5")

    label("loc_99B")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_9B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E7")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_A01")

    label("loc_9E7")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_A01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2B")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_A3D")

    label("loc_A2B")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_A3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A67")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_A79")

    label("loc_A67")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_A79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA7")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_ABD")

    label("loc_AA7")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_ABD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_AF9")

    label("loc_AE7")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_AF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B25")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_B39")

    label("loc_B25")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_B39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_B85")

    label("loc_B6B")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_B85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAB")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_BB9")

    label("loc_BAB")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_BB9")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3D")
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
        (0, "loc_C90"),
        (1, "loc_C9E"),
        (2, "loc_CAC"),
        (3, "loc_CBA"),
        (4, "loc_CC8"),
        (5, "loc_CD6"),
        (6, "loc_CE4"),
        (7, "loc_CF2"),
        (8, "loc_D00"),
        (9, "loc_D0E"),
        (10, "loc_D1C"),
        (11, "loc_D2A"),
        (SWITCH_DEFAULT, "loc_D38"),
    )


    label("loc_C90")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_C9E")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_CAC")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_CBA")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_CC8")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_CD6")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_CE4")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_CF2")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_D00")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_D0E")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_D1C")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_D2A")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D38")

    label("loc_D38")

    Jump("loc_D47")

    label("loc_D3D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D47")

    Jump("loc_DAA")

    label("loc_D4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D97")
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
    Jump("loc_DAA")

    label("loc_D97")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DAA")

    Jump("loc_81F")

    label("loc_DAF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_74F end

    def Function_4_DB7(): pass

    label("Function_4_DB7")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E8B")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_E91")

    label("loc_E8B")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_E91")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_DB7 end

    def Function_5_EA6(): pass

    label("Function_5_EA6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 3)
    Return()

    # Function_5_EA6 end

    def Function_6_EB4(): pass

    label("Function_6_EB4")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0x8,
        (
            "#0500F皆さん、お疲れ様です！\x01",
            "……早速遺跡の探索を\x01",
            "再開しますか？\x02",
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
            "再開する\x01",            # 0
            "まだ準備がある\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDB")

    #C0002
    ChrTalk(
        0x101,
        "#0000Fああ、そろそろ探索に戻ろう。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#0500F了解です。\x01",
            "それでは《塔》の内部に\x01",
            "向かいましょう！\x02",
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
    Jump("loc_107A")

    label("loc_FDB")


    #C0004
    ChrTalk(
        0x8,
        (
            "#0503Fそうですか。\x01",
            "相手は危険な賊のようですし、\x01",
            "装備を整えた方がいいですよね。\x02\x03",

            "#0501F自分はここで待機していますので、\x01",
            "準備が整ったら声を掛けてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107A")

    TalkEnd(0xFE)
    Return()

    # Function_6_EB4 end

    def Function_7_107E(): pass

    label("Function_7_107E")

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
            "#0505Fあ、皆さん\x01",
            "街に戻られるんですか？\x02\x03",

            "#0500Fすみません、自分は\x01",
            "民間人が立ち入らないよう\x01",
            "見張ってないといけないもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#0005Fおっと、そうか……\x01",
            "一度戻って\x01",
            "装備を整えて来たかったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0306Fま、任務なんだし仕方ねえな。\x02\x03",

            "#0300Fノエル曹長、一旦別行動だ。\x01",
            "装備を補充してくるから\x01",
            "待機していてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#0500F了解です。\x01",
            "装甲車の傍で待機していますので、\x01",
            "どうかお気をつけて！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#0000Fああ、ノエルも気をつけてな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x0, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12E9")
    OP_32(0x0, 0xFC, 0x1)
    OP_32(0x0, 0x2, 0x1)

    label("loc_12E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x1, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1303")
    OP_32(0x1, 0xFC, 0x1)
    OP_32(0x1, 0x2, 0x1)

    label("loc_1303")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x2, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_131D")
    OP_32(0x2, 0xFC, 0x1)
    OP_32(0x2, 0x2, 0x1)

    label("loc_131D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x3, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1337")
    OP_32(0x3, 0xFC, 0x1)
    OP_32(0x3, 0x2, 0x1)

    label("loc_1337")

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

    # Function_7_107E end

    def Function_8_13F8(): pass

    label("Function_8_13F8")

    EventBegin(0x1)

    #C0010
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……\x02\x03",

            "#0000F塔の探索に入るなら\x01",
            "ノエル曹長に声を掛けないとな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 34460, -13190, 100280, 170)
    EventEnd(0x4)
    Return()

    # Function_8_13F8 end

    def Function_9_1460(): pass

    label("Function_9_1460")

    ClearMapFlags(0x10000000)
    Return()

    # Function_9_1460 end

    def Function_10_1466(): pass

    label("Function_10_1466")

    SetScenarioFlags(0x87, 6)
    ModifyEventFlags(0, 4, 0x80)
    Return()

    # Function_10_1466 end

    def Function_11_146F(): pass

    label("Function_11_146F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_1619")

    #C0011
    ChrTalk(
        0x101,
        "#0005F#6Pあれは……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0105F#12Pもしかして……\x01",
            "警備隊の車両かしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1699")

    label("loc_1619")


    #C0013
    ChrTalk(
        0x101,
        (
            "#0000F#6P《星見の塔》……\x01",
            "やっぱりこっちの方だったか。\x02\x03",

            "#0005Fでも、あれは……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0105F#12P警備隊の車両みたいだけど……\x02",
    )

    CloseMessageWindow()

    label("loc_1699")


    #C0015
    ChrTalk(
        0x104,
        (
            "#0303F#12Pああ、警備隊で使っている\x01",
            "軽装甲機動車だな。\x02\x03",

            "#0301F何だってこんな所に来てるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#0200F#6P直接、聞いた方が良さそうですね。\x02",
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

    # Function_11_146F end

    def Function_12_174E(): pass

    label("Function_12_174E")

    Sleep(2000)
    Sound(866, 0, 100, 0)
    Return()

    # Function_12_174E end

    def Function_13_1758(): pass

    label("Function_13_1758")

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
            "#0506F#11P一体、誰の仕業なのかな……？\x02\x03",

            "#0508Fこんな場所に入る物好きなんて\x01",
            "いると思えないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#1Pおーい！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_68(37250, -12300, 97250, 3000)

    def lambda_191E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_191E)
    Sleep(50)

    def lambda_1936():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1936)
    Sleep(50)

    def lambda_194E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_194E)
    Sleep(50)

    def lambda_1966():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1966)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0019
    ChrTalk(
        0x8,
        "#0505F#5P……あなたたちは……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0000F#12Pやっぱり君だったか。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#0302F#12Pはは、妙な所で会うもんだな。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#0505F#5Pロイドさん、ランディ先輩？\x02\x03",

            "#0502Fエリィさんにティオちゃんまで……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0102F#2Pご無沙汰しています。\x01",
            "ノエル曹長。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#0204F#12Pその節はどうも……\x02",
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
            "ふふっ、お久しぶりです。\x02\x03",

            "ところで……\x01",
            "どうしてこんな所へ？\x02\x03",

            "あまり人が立ち寄る場所じゃ\x01",
            "ないと思うんですけど……\x02",
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
            "#0006F#12Pああ、少し事情があってね。\x02\x03",

            "#0001Fそれより、そこのフェンスは\x01",
            "どうしたんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#0506F#5Pその、どうやら何者かによって\x01",
            "破壊されたみたいなんです。\x02\x03",

            "#0501F元々、この塔は危ないから\x01",
            "警備隊が封鎖してたんですけど……\x02\x03",

            "あたしも定期巡回をしていて\x01",
            "ちょうど発見したばかりで。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0013F#12Pそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#0303F#12Pこのタイミングで\x01",
            "破壊されたフェンスか……\x02\x03",

            "#0301F十中八九、犯人は見えたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#0103F#2Pそうね……\x02",
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
        "#0001F#12Pえっと、実は……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちはこれまでの経緯を\x01",
            "かいつまんでノエル曹長に説明した。\x07\x00\x02",
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
            "#0507F#5Pカルバードの東方人街から\x01",
            "やって来た暗殺者……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#0103F#2Pええ……そうなんです。\x02\x03",

            "#0101Fその人物から、この塔で\x01",
            "待っていると伝言を受け取って……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0003F#12Pそれでダメ元で\x01",
            "調べに来たんだけど……\x02\x03",

            "#0001Fどうやら本当に\x01",
            "待ち受けているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#0506F#5Pは～、街ではそんなことが……\x02\x03",

            "#0501Fそれで、どうするんですか？\x02\x03",

            "まさか本当に\x01",
            "誘いに乗るんじゃないですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0000F#12Pいや……\x01",
            "あえて乗ってみるつもりだ。\x02",
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
            "#0505F#5Pえ、で、でも……\x02\x03",

            "#0501F相手は危険な犯罪者でしょう？\x01",
            "どんな罠があるかもしれないし……\x02\x03",

            "何だったら副司令に頼んで\x01",
            "警備隊から応援を……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#0303F#12Pいや、相手は相当なプロだ。\x02\x03",

            "下手に大部隊を動かしたら\x01",
            "感づいて逃げられるだけだろう。\x02\x03",

            "#0301Fここは少人数で行くのが正解だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#0506F#5Pそ、それは……\x01",
            "そうかもしれないですけど。\x02",
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
            "#0503F#5P……分かりました。\x01",
            "だったら止めません。\x02\x03",

            "#0507Fその代わり……\x01",
            "あたしも助太刀します！\x02",
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
        "#0011F#12Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#0105F#2Pで、でも……いいんですか？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "#0503F#5P一応、この塔の管理は\x01",
            "クロスベル警備隊の仕事ですし。\x02\x03",

            "皆さんだけを危険な目に\x01",
            "遭わせるわけには行きません。\x02\x03",

            "#0500Fそれに、いつもフランが\x01",
            "お世話になってるみたいですし……\x02\x03",

            "ノエル・シーカー曹長、\x01",
            "全力で皆さんをサポートします！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0006F#12Pう、うーん……\x02\x03",

            "#0002F妹さんの事は、むしろ俺たちが\x01",
            "世話になってるくらいなんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0304F#12Pま、いいんじゃないか？\x02\x03",

            "#0302F腕も立ちそうだし、\x01",
            "ここは手を借りておこうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        (
            "#0204F#12Pそうですね。\x02\x03",

            "#0202Fバックアップがいれば\x01",
            "わたしたちも助かりますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        (
            "#0103F#2P問題は《銀》が警備隊員を\x01",
            "警戒しないかくらいだけど……\x02\x03",

            "#0100F一人なら大丈夫じゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0004F#12P……そうだな。\x02\x03",

            "#0000Fノエル曹長──\x01",
            "よろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "#0502F#5Pええ、こちらこそ！\x02",
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
            "ゲストパーティとして\x01",
            "ノエル曹長が仲間になりました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "パーティが４人を超えた場合、\x01",
            "余った人員は『サポートメンバー』に\x01",
            "登録される事になります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『サポートメンバー』は戦域外に待機し、\x01",
            "たまにＡＴ順に現れ、出番が回ってくると\x01",
            "様々な支援行動を取ってくれます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "パーティメンバーの入れ替えは\x01",
            "キャンプメニューの[TACTICS]から行えます。\x01",
            "ノエルを『アタックメンバー』に入れ、\x01",
            "ロイド、エリィ、ティオ、ランディの誰かを\x01",
            "『サポートメンバー』に回すことも可能です。\x07\x00\x02",
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

    # Function_13_1758 end

    def Function_14_27FC(): pass

    label("Function_14_27FC")

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
            "#6P#0001F星見の塔か……\x01",
            "《銀》とやりあった場所だな。\x02\x03",

            "#0003Fこうして眺めているぶんには\x01",
            "綺麗な場所だと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#6P#0108F内部の様子を知っていると、\x01",
            "どうもね……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#12P#0200Fこの場所、やはり一通り\x01",
            "公式に調査した方がいいのでは？\x02\x03",

            "#0203F不可解なものを不可解なまま\x01",
            "残しておくのは、\x01",
            "どうも気持ちが悪いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#0303F調査ってことになると\x01",
            "警備隊の管轄だろうが……\x01",
            "難しいだろうな。\x02\x03",

            "#0301F警備隊の司令は\x01",
            "出世の役に立たねえ事には\x01",
            "手を出さない野郎だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#6P#0003F……課題は山積みだな。\x02\x03",

            "#0000Fとにかく……\x01",
            "グレイスさんに依頼された写真、\x01",
            "ここならいいものが撮れそうだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_313B")
    TurnDirection(0x101, 0x102, 500)

    #C0061
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれじゃあエリィ、\x01",
            "撮影をお願いできるかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0062
    ChrTalk(
        0x102,
        (
            "#6P#0108Fえ、ええ。\x01",
            "ちょっと自信はないけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0063
    ChrTalk(
        0x104,
        (
            "#12P#0300Fいやいや、大丈夫だろ。\x02\x03",

            "ちょっとレンズを覗いて\x01",
            "パチリと撮っちまえば\x01",
            "終わりじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0064
    ChrTalk(
        0x102,
        (
            "#6P#0106Fあのねぇ……\x01",
            "いい写真を撮るのは\x01",
            "そんな簡単なことじゃないのよ。\x02\x03",

            "#0100Fフレームの中に\x01",
            "対象物をどう収めるか、\x01",
            "構成を練らなきゃいけないし……\x02\x03",

            "天気や風の影響で\x01",
            "写真の印象もガラリと変わってしまう。\x02\x03",

            "ある一瞬を逃したら\x01",
            "二度と撮れないことだって\x01",
            "あるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#12P#0200F素人とプロの写真を見比べると\x01",
            "一目で違いが分かりますからね。\x02\x03",

            "#0203F粗雑な人には、その繊細さが\x01",
            "理解できないかも知れませんが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0066
    ChrTalk(
        0x104,
        (
            "#12P#0306Fぐっ……\x01",
            "誰のことを言ってんだ、誰の。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#6P#0000Fま、まぁまぁ。\x01",
            "ここはエリィに任せてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#6P#0100Fそれじゃあ……\x01",
            "やってみるわね。\x02",
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
            "#6P#0103F……ふぅ。\x01",
            "念のため何枚か撮っておいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#6P#0000Fどうやら撮れたみたいだな。\x02\x03",

            "出来栄えはどんな感じだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#6P#0100F実際に現像してみないと\x01",
            "分からないけど……\x02\x03",

            "少なくとも、\x01",
            "悪い写真ではないとは思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        (
            "#12P#0200Fエリィさんも\x01",
            "カンを取り戻せたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x104,
        (
            "#12P#0300Fふーん……\x01",
            "俺にはさっぱりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#6P#0000Fまたこういう場所を見つけたら\x01",
            "写真に収めていこう。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3487")

    label("loc_313B")

    TurnDirection(0x101, 0x102, 500)

    #C0075
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれじゃあ……\x01",
            "エリィ、撮影を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x102,
        "#6P#0100Fええ、分かったわ。\x02",
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
            "#6P#0103F……ふぅ。\x01",
            "こんなところかしら。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_32D1")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_32E8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_32FF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_3316")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3316")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_332D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_332D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_3344")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3344")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_335B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_335B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_3372")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3372")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_3389")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3389")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3433")

    #C0078
    ChrTalk(
        0x101,
        (
            "#6P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "これでグレイスさんに提示された\x01",
            "５枚ってノルマは達成できた。\x01",
            "これでいつでも提出できそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3487")

    label("loc_3433")


    #C0079
    ChrTalk(
        0x101,
        (
            "#6P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3487")

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

    # Function_14_27FC end

    def Function_15_34BE(): pass

    label("Function_15_34BE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3614")

    #C0080
    ChrTalk(
        0x103,
        "#0200Fここは立ち入り禁止のようですね。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        (
            "#0300Fこのバリケードは\x01",
            "クロスベル警備隊の物だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0000Fああ、《星見の塔》とかいう\x01",
            "中世の遺跡だよ。\x02\x03",

            "崩れかかっている所もあるし、\x01",
            "普段は入れないみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0100F私も話は聞いた事があるけれど\x01",
            "訪れた事はないわね。\x02\x03",

            "もう１０年近く\x01",
            "封鎖されたままなんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x87, 4)
    Jump("loc_3679")

    label("loc_3614")

    SetChrName("")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "道はバリケードによって\x01",
            "封鎖されている。\x02\x03",

            "クロスベル警備隊のマークが\x01",
            "記されているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3679")

    TalkEnd(0xFF)
    Return()

    # Function_15_34BE end

    SaveToFile()

Try(main)
