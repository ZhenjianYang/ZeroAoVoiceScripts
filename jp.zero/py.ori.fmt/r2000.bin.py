from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2000.bin",                # FileName
        "r2000",                    # MapName
        "r2000",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2000", "r0000_1", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -60, 1060, 3730, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r2000",                  # 0
        "ハロルド車",             # 1
        "バス",                   # 2
        "車",                     # 3
        "SE制御",                 # 4
        "クロスベル市方面",       # 5
        "クロスベル大聖堂方面",   # 6
        "鉱山町マインツ方面",     # 7
    ))

    DeclNpc(8430,    0,       33990,   225,  197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 10,  0.0,                   7.0,                   -1.0,                  144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.0,                  -2.3333334922790527,   0.20000001788139343,   1.0])

    DeclActor(11200,   0,       16200,   1500,    11200,   1500,    16200,   0x007C, 0,  8,  0x0000)
    DeclActor(-700,    0,       19910,   1800,    -700,    2000,    19910,   0x007C, 0,  9,  0x0000)
    DeclActor(-16960,  -2000,   50350,   1200,    -16960,  -2000,   50350,   0x007C, 0,  2,  0x0000)
    DeclActor(4200,    0,       36290,   2500,    4200,    1700,    36290,   0x007C, 0,  16, 0x0000)

    PlaceName(-1.7999999523162842, 0.0, -15.550000190734863, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(45.0, 0.0, 37.0, 0x0000, 0x0000, "クロスベル大聖堂方面")
    PlaceName(-23.0, 0.0, 75.30000305175781, 0x0000, 0x0000, "鉱山町マインツ方面")
    PlaceName(11.25, 0.0, 16.450000762939453, 0x0000, 0x0055, "")
    PlaceName(-1.0, 0.0, 19.5, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_390",          # 00, 0
        "Function_1_65D",          # 01, 1
        "Function_2_843",          # 02, 2
        "Function_3_857",          # 03, 3
        "Function_4_914",          # 04, 4
        "Function_5_A36",          # 05, 5
        "Function_6_ACB",          # 06, 6
        "Function_7_107D",         # 07, 7
        "Function_8_116C",         # 08, 8
        "Function_9_1383",         # 09, 9
        "Function_10_13BE",        # 0A, 10
        "Function_11_1E05",        # 0B, 11
        "Function_12_1E48",        # 0C, 12
        "Function_13_2661",        # 0D, 13
        "Function_14_27EB",        # 0E, 14
        "Function_15_294C",        # 0F, 15
        "Function_16_2A2F",        # 10, 16
        "Function_17_2AB2",        # 11, 17
    ))


    def Function_0_390(): pass

    label("Function_0_390")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xF9, 6)
    SetScenarioFlags(0xFB, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3AE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3BD")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 5)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_3D5")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_3D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_65C")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B")
    SetScenarioFlags(0x7A, 0)

    label("loc_43B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451")
    SetScenarioFlags(0x7A, 1)

    label("loc_451")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467")
    SetScenarioFlags(0x7A, 2)

    label("loc_467")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47D")
    SetScenarioFlags(0x7A, 3)

    label("loc_47D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493")
    SetScenarioFlags(0x7A, 4)

    label("loc_493")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A9")
    SetScenarioFlags(0x7A, 5)

    label("loc_4A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BF")
    SetScenarioFlags(0x7A, 6)

    label("loc_4BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D5")
    SetScenarioFlags(0x7A, 7)

    label("loc_4D5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EB")
    SetScenarioFlags(0x7B, 0)

    label("loc_4EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_501")
    SetScenarioFlags(0x7B, 1)

    label("loc_501")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_517")
    SetScenarioFlags(0x7B, 2)

    label("loc_517")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D")
    SetScenarioFlags(0x7B, 3)

    label("loc_52D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_543")
    SetScenarioFlags(0x7B, 4)

    label("loc_543")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_559")
    SetScenarioFlags(0x7B, 5)

    label("loc_559")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F")
    SetScenarioFlags(0x7B, 6)

    label("loc_56F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")
    SetScenarioFlags(0x7B, 7)

    label("loc_585")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C0")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_65C")

    label("loc_5C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D7")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_65C")

    label("loc_5D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EE")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_65C")

    label("loc_5EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_605")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_65C")

    label("loc_605")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61C")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_65C")

    label("loc_61C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_633")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_65C")

    label("loc_633")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64A")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_65C")

    label("loc_64A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65C")
    SetScenarioFlags(0x7C, 7)

    label("loc_65C")

    Return()

    # Function_0_390 end

    def Function_1_65D(): pass

    label("Function_1_65D")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_675")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_675")

    SetMapObjFlags(0x1, 0x4)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F7")
    OP_66(0x1, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x8000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0xA)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    SetChrPos(0xA, -1120, 0, 19360, 315)
    OP_D3(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x0)
    Jump("loc_6FC")

    label("loc_6F7")

    OP_16(0x3, 0x4, 0x1, 0x0)

    label("loc_6FC")

    OP_78(0x2, 0x8)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_721")
    Jump("loc_743")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_743")
    ClearMapObjFlags(0x2, 0x4)
    OP_D3(0x8, 0x0, 0x36EE8, 0x0, 0x0)

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_759")
    Event(0, 15)

    label("loc_759")

    SetChrFlags(0x9, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77D")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_783")

    label("loc_77D")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7BA")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)

    label("loc_7BA")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 0)), scpexpr(EXPR_END)), "loc_817")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -16960, -2000, 50350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_817")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_82F")
    OP_1B(0x2, 0x0, 0x11)
    Jump("loc_842")

    label("loc_82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_842")
    OP_1B(0x2, 0x0, 0x11)

    label("loc_842")

    Return()

    # Function_1_65D end

    def Function_2_843(): pass

    label("Function_2_843")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_2_843 end

    def Function_3_857(): pass

    label("Function_3_857")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "鉱山町マインツ\x01",              # 0
            "停留所（人形工房付近）\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_90C")

    label("loc_8EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90C")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_90C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_857 end

    def Function_4_914(): pass

    label("Function_4_914")

    Fade(1000)
    OP_68(10010, 600, 21560, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(630, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, 10190, 0, 16230, 0)
    SetChrPos(0x1, 9210, 0, 16200, 0)
    SetChrPos(0x2, 8170, 0, 16290, 0)
    SetChrPos(0x3, 7240, 0, 16350, 0)
    ClearChrFlags(0x9, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0x9)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x9, -40, 0, 30670, 105)
    OP_D3(0x9, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_9EF():
        OP_9E(0xFE, 0x3174, 0x82A0, 0xFFFF15A0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9EF)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x9, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_4_914 end

    def Function_5_A36(): pass

    label("Function_5_A36")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 10030, 0, 16580, 0)
    SetChrPos(0x1, 10030, 0, 16580, 0)
    SetChrPos(0x2, 10030, 0, 16580, 0)
    SetChrPos(0x3, 10030, 0, 16580, 0)
    OP_68(10030, 600, 16580, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_5_A36 end

    def Function_6_ACB(): pass

    label("Function_6_ACB")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1075")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1012")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_B97")

    label("loc_B7B")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_B97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC9")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_BE3")

    label("loc_BC9")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_BE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C15")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_C2F")

    label("loc_C15")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_C2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C61")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_C7B")

    label("loc_C61")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_C7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAD")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_CC7")

    label("loc_CAD")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_CC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF1")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_D03")

    label("loc_CF1")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_D03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2D")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_D3F")

    label("loc_D2D")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_D3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6D")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_D83")

    label("loc_D6D")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_D83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAD")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_DBF")

    label("loc_DAD")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_DBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEB")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_DFF")

    label("loc_DEB")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_DFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E31")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_E4B")

    label("loc_E31")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_E4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E71")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_E7F")

    label("loc_E71")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_E7F")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1003")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x1)
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
        (0, "loc_F56"),
        (1, "loc_F64"),
        (2, "loc_F72"),
        (3, "loc_F80"),
        (4, "loc_F8E"),
        (5, "loc_F9C"),
        (6, "loc_FAA"),
        (7, "loc_FB8"),
        (8, "loc_FC6"),
        (9, "loc_FD4"),
        (10, "loc_FE2"),
        (11, "loc_FF0"),
        (SWITCH_DEFAULT, "loc_FFE"),
    )


    label("loc_F56")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_F64")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_F72")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_F80")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_F8E")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_F9C")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_FAA")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_FB8")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_FC6")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_FD4")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_FE2")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_FF0")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FFE")

    label("loc_FFE")

    Jump("loc_100D")

    label("loc_1003")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_100D")

    Jump("loc_1070")

    label("loc_1012")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105D")
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
    Jump("loc_1070")

    label("loc_105D")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1070")

    Jump("loc_AE5")

    label("loc_1075")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_ACB end

    def Function_7_107D(): pass

    label("Function_7_107D")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 2740, 0, 21060, 89)
    SetChrPos(0x1, 2740, 0, 21060, 89)
    SetChrPos(0x2, 2740, 0, 21060, 89)
    SetChrPos(0x3, 2740, 0, 21060, 89)
    SetChrPos(0x4, 2740, 0, 21060, 89)
    SetChrPos(0x5, 2740, 0, 21060, 89)
    Sleep(1)
    OP_68(2740, 600, 21060, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1151")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1157")

    label("loc_1151")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1157")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_107D end

    def Function_8_116C(): pass

    label("Function_8_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_11A3")
    TalkBegin(0xFF)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_1382")

    label("loc_11A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DF")
    TalkBegin(0xFF)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_1382")

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_11F0")
    Call(0, 3)
    Jump("loc_1382")

    label("loc_11F0")

    TalkBegin(0xFF)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_END)), "loc_127F")

    #C0005
    ChrTalk(
        0x101,
        (
            "#0001F今日はバスは使わないでおこう。\x02\x03",

            "調査の為には、街道も\x01",
            "足で歩いた方が良さそうだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137C")

    label("loc_127F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12C8")

    #C0006
    ChrTalk(
        0x101,
        (
            "#0001F昨日に続いてだけど……\x01",
            "今日もバスは使えないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137C")

    label("loc_12C8")


    #C0007
    ChrTalk(
        0x101,
        (
            "#0001F昨日に続いてだけど……\x01",
            "今日もバスは使えないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0104Fええ、歩いてみましょう。\x02\x03",

            "#0100F途中で何か手がかりが\x01",
            "見つかるかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#0201F……頑張りましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_137C")

    SetScenarioFlags(0x0, 1)
    TalkEnd(0xFF)

    label("loc_1382")

    Return()

    # Function_8_116C end

    def Function_9_1383(): pass

    label("Function_9_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)
    Jump("loc_13BD")

    label("loc_13A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BD")
    Call(0, 12)

    label("loc_13BD")

    Return()

    # Function_9_1383 end

    def Function_10_13BE(): pass

    label("Function_10_13BE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(3230, 900, 11740, 0)
    MoveCamera(90, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 1600, 0, 9670, 0)
    SetChrPos(0x102, 2680, 0, 8580, 0)
    SetChrPos(0x103, 840, 0, 8350, 0)
    SetChrPos(0x104, 1240, 120, 7280, 0)

    def lambda_1490():
        OP_95(0xFE, 3270, 0, 13110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1490)

    def lambda_14AA():
        OP_95(0xFE, 4430, 0, 12180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14AA)

    def lambda_14C4():
        OP_95(0xFE, 2180, 0, 11520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14C4)

    def lambda_14DE():
        OP_95(0xFE, 2900, 0, 10410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14DE)
    FadeToBright(1000, 0)
    SetCameraDistance(19500, 3000)
    OP_0D()
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x103,
        "#0205F#12Pあ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1587():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1587)
    Sleep(50)

    def lambda_1597():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1597)
    Sleep(50)

    def lambda_15A7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15A7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0011
    ChrTalk(
        0x101,
        "#0005F#5Pティオ、どうした？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0105F#5Pもしかして……\x01",
            "また、何か聞こえたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#0201F#12Pはい……\x01",
            "センサーの感度を上げます！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(300)
    VolumeBGM(0x3C, 0x3E8)
    Sound(1278, 255, 100, 0)    #voice#Tio
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Sound(839, 0, 100, 0)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x101,
        "#0007F#5P今のは……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#0101F#5P微かにだけど……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0303F#11Pああ、魔獣の遠吠えだろう。\x02\x03",

            "#0300Fティオすけが気付かなかったら\x01",
            "俺たちも聴き逃してたな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x103, 0x2)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sound(820, 0, 100, 0)
    BeginChrThread(0xB, 1, 0, 11)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)

    #C0017
    ChrTalk(
        0x103,
        "#0203F#5P#40Wふう……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0018
    ChrTalk(
        0x103,
        (
            "#0201F#12P……やはり今の遠吠えは\x01",
            "山道方面から聞こえたようです。\x02\x03",

            "北北西に４０セルジュくらいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#0001F#5P北北西に４０セルジュ……\x01",
            "山道の途中あたりになるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        "#0305F#11Pって事は……\x02",
    )

    CloseMessageWindow()

    def lambda_1946():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1946)

    def lambda_1953():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1953)
    Sleep(50)

    def lambda_1963():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1963)

    def lambda_1970():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1970)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    TurnDirection(0x101, 0x102, 500)
    Sleep(800)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0021
    ChrTalk(
        0x101,
        (
            "#0006F#5Pその……エリィ、ティオ。\x02\x03",

            "昨日に引き続いて\x01",
            "こんな事を言うのもなんだけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    def lambda_1A57():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A57)

    #C0022
    ChrTalk(
        0x102,
        (
            "#0104F#11Pううん、気にしないで。\x02\x03",

            "#0100Fこれも巡り合わせでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0204F#12P……わたしも大丈夫です。\x02\x03",

            "#0208Fそれに今の遠吠え……\x01",
            "どこか語りかけてくるような\x01",
            "感じがして……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B1A():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B1A)
    Sleep(50)

    def lambda_1B2A():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B2A)

    #C0024
    ChrTalk(
        0x101,
        "#0005F#5P語りかけてくる……？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        "#0301F#11P威嚇してるとか、そんな感じか？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#0208F#12Pいえ……もっとはっきりとした\x01",
            "意志みたいなものを感じて……\x02\x03",

            "#0206F……すみません。\x01",
            "上手く言葉に出来ないみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#0003F#5Pそうか……\x02\x03",

            "#0001F……どのみち、警備隊が動いたら\x01",
            "逃げられてしまう可能性が高そうだ。\x02\x03",

            "俺たちだけで何とか\x01",
            "見つけ出すしかないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0101F#5Pそうね、頑張りましょう。\x02\x03",

            "本格的に山道を調べるとなると\x01",
            "色々と準備した方がよさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0001F#5Pああ、それに他の支援要請を\x01",
            "やってる余裕も無くなるだろう。\x02\x03",

            "一通りケリを付けたら\x01",
            "山道探索を始めることにしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0302F#11Pそんじゃま、準備を済ませたら\x01",
            "楽しいハイキングと行きますかね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_37()
    SetChrPos(0x0, 1200, 0, 13100, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x64, 2)
    OP_29(0x40, 0x1, 0x1)
    EndChrThread(0xB, 0x1)
    OP_24(0x348)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_13BE end

    def Function_11_1E05(): pass

    label("Function_11_1E05")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_11_1E05 end

    def Function_12_1E48(): pass

    label("Function_12_1E48")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(2110, 2900, 19980, 0)
    MoveCamera(32, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20380, 0)
    OP_68(2110, 900, 19980, 3000)
    SetChrPos(0x101, 2130, 0, 19420, 270)
    SetChrPos(0x102, 2130, 0, 17710, 270)
    SetChrPos(0x103, 3640, 0, 21250, 270)
    SetChrPos(0x104, 4200, 0, 19810, 270)
    SetChrPos(0x109, 3910, 0, 17590, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_6F(0x79)

    #C0031
    ChrTalk(
        0x101,
        (
            "#0000F#11Pこれが曹長が\x01",
            "乗ってきた車両だよな？\x02\x03",

            "前にも何度か\x01",
            "乗せてもらってるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        (
            "#0504F#11Pええ、そうです。\x02\x03",

            "#0502Fどんな悪路もなんのその。\x01",
            "警備隊が誇る軽装甲機動車ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0306F#11Pま、戦車の砲撃には\x01",
            "耐えられないだろうけどなぁ。\x02\x03",

            "#0300Fせいぜいガトリング砲の弾を\x01",
            "跳ね返せる程度だったか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x104, 500)

    #C0034
    ChrTalk(
        0x109,
        (
            "#0506F#12Pうう……\x01",
            "それを言わないでくださいよ～。\x02\x03",

            "#0501F一応、最新技術が盛り込まれた\x01",
            "高性能な車両なんですから～。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20C6():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20C6)
    Sleep(50)

    def lambda_20D6():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20D6)
    Sleep(50)

    def lambda_20E6():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20E6)
    Sleep(50)

    def lambda_20F6():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20F6)
    Sleep(300)

    #C0035
    ChrTalk(
        0x102,
        (
            "#0106F#6Pまあ、クロスベルでは\x01",
            "戦車の保持が自粛されてるから……\x02\x03",

            "#0100F機動性で勝負するしか\x01",
            "ないのかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#0203F#5P戦車もそうですが、軍用飛行艇も\x01",
            "一隻も保有していませんよね。\x02\x03",

            "#0200Fクロスベルの豊かな財政なら\x01",
            "何隻でも購入できそうですけど……\x02\x03",

            "やはり帝国と共和国からの\x01",
            "圧力によるものですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        (
            "#0506F#12Pうん……そうだね。\x02\x03",

            "#0501F特に帝国は、１２年前の紛争で\x01",
            "リベールの軍用飛行艇に\x01",
            "痛い目に遭わされたそうだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        (
            "#0103F#6P下手に持たせて\x01",
            "相手側に付かれたら厄介だ……\x02\x03",

            "#0101F帝国にしても共和国にしても\x01",
            "そんな思惑が見え隠れするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0003F#5Pなるほど……\x02\x03",

            "#0001Fクロスベルみたいな地形、\x01",
            "飛行艇があればもっと効率的に\x01",
            "パトロールができそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#0506F#12Pはあ、そうなんですよね～。\x02\x03",

            "#0504F──まあ、それはともかく。\x02\x03",

            "#0500Fもし車両で移動したければ\x01",
            "いつでも言ってください。\x02\x03",

            "車で行ける場所ならどこでも\x01",
            "皆さんを送れると思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今日一日、ノエルの警備隊車両で\x01",
            "自治州各地に移動する事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "マップ上にある警備隊車両を調べて\x01",
            "行き先を選択してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なお、警備隊車両を放置して\x01",
            "バスや徒歩で別の場所に移動した場合、\x01",
            "警備隊車両はその場に残り続けます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "くれぐれも停車している場所を\x01",
            "忘れないよう心がけてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※山道の外れにある遺跡に行く場合、\x01",
            "  『マインツ山道・隧道内』\x01",
            "  を選ぶと近道をすることが出来ます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 2850, 0, 18840, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 1)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_12_1E48 end

    def Function_13_2661(): pass

    label("Function_13_2661")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-3190, 6260, 780, 0)
    MoveCamera(30, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17120, 0)
    OP_68(-3190, 2960, 780, 5000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x2)
    SetMapObjFlags(0x1, 0x400)
    SetChrFlags(0xA, 0x8000)
    OP_78(0x1, 0xA)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_D3(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)
    Sound(485, 0, 100, 0)
    FadeToBright(1000, 0)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 70, 0, 17900, 0)

    def lambda_27A1():
        OP_95(0xFE, 50, -2930, -8070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_27A1)
    OP_0D()
    Sleep(1100)
    BeginChrThread(0xA, 3, 0, 14)
    Sound(470, 0, 100, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 3)
    OP_6F(0x1)
    SetScenarioFlags(0x5D, 3)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2661 end

    def Function_14_27EB(): pass

    label("Function_14_27EB")

    OP_D3(0xFE, 0x0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x3E8, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x7D0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0xBB8, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0xFA0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x1388, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x1770, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x1B58, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x1F40, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x2328, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x2710, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x2AF8, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x2EE0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x32C8, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x36B0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x3A98, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    Return()

    # Function_14_27EB end

    def Function_15_294C(): pass

    label("Function_15_294C")

    EventBegin(0x0)
    Sleep(1000)
    OP_EE(0x0, 0x1)
    OP_68(14140, -670, 19290, 5000)
    MoveCamera(45, 21, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(23500, 5000)
    OP_6F(0x79)
    OP_EE(0x0, 0xA)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "停留所の看板を調べると、\x01",
            "導力バスに乗ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "選択した行き先へ素早く移動することができ、\x01",
            "各地を効率的に回ることが可能です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_15_294C end

    def Function_16_2A2F(): pass

    label("Function_16_2A2F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　南・クロスベル市\x01",
            "　東・クロスベル大聖堂\x01",
            "北西・鉱山町マインツ　３１１セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_2A2F end

    def Function_17_2AB2(): pass

    label("Function_17_2AB2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2B38")

    #C0049
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはマインツ山道か……\x02\x03",

            "#0003F今はウルスラ病院の方が気になる。\x01",
            "あまり寄り道はしないで\x01",
            "病院へ向かおう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B8F")

    label("loc_2B38")


    #C0050
    ChrTalk(
        0x101,
        (
            "#0003Fキーアを連れて\x01",
            "街道を歩くわけにはいかないな。\x02\x03",

            "#0000F寄り道はやめておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8F")

    SetChrPos(0x0, -27230, -2000, 65230, 135)
    EventEnd(0x4)
    Return()

    # Function_17_2AB2 end

    SaveToFile()

Try(main)
