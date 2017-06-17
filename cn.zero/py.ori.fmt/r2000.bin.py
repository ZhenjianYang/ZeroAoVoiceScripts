from ZeroScenarioHelper import *

def main():
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
        "哈罗德车",               # 1
        "巴士",                   # 2
        "车",                     # 3
        "SE控制",                 # 4
        "克洛斯贝尔市方向",       # 5
        "克洛斯贝尔大圣堂方向",   # 6
        "矿山镇玛因兹方向",       # 7
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

    PlaceName(-1.7999999523162842, 0.0, -15.550000190734863, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(45.0, 0.0, 37.0, 0x0000, 0x0000, "克洛斯贝尔大圣堂方向")
    PlaceName(-23.0, 0.0, 75.30000305175781, 0x0000, 0x0000, "矿山镇玛因兹方向")
    PlaceName(11.25, 0.0, 16.450000762939453, 0x0000, 0x0055, "")
    PlaceName(-1.0, 0.0, 19.5, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_390",          # 00, 0
        "Function_1_65D",          # 01, 1
        "Function_2_843",          # 02, 2
        "Function_3_857",          # 03, 3
        "Function_4_90C",          # 04, 4
        "Function_5_A2E",          # 05, 5
        "Function_6_AC3",          # 06, 6
        "Function_7_1047",         # 07, 7
        "Function_8_1136",         # 08, 8
        "Function_9_1305",         # 09, 9
        "Function_10_1340",        # 0A, 10
        "Function_11_1CC3",        # 0B, 11
        "Function_12_1D06",        # 0C, 12
        "Function_13_2411",        # 0D, 13
        "Function_14_259B",        # 0E, 14
        "Function_15_26FC",        # 0F, 15
        "Function_16_27BB",        # 10, 16
        "Function_17_283A",        # 11, 17
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
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "矿山镇玛因兹\x01",                # 0
            "停靠站（人偶工房附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E4")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_904")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_904")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_904")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_857 end

    def Function_4_90C(): pass

    label("Function_4_90C")

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

    def lambda_9E7():
        OP_9E(0xFE, 0x3174, 0x82A0, 0xFFFF15A0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9E7)
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

    # Function_4_90C end

    def Function_5_A2E(): pass

    label("Function_5_A2E")

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

    # Function_5_A2E end

    def Function_6_AC3(): pass

    label("Function_6_AC3")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDC")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B69")
    MenuCmd(1, 1, "★克洛斯贝尔·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_B83")

    label("loc_B69")

    MenuCmd(1, 1, "　克洛斯贝尔·中央广场")

    label("loc_B83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB3")
    MenuCmd(1, 1, "★克洛斯贝尔·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_BCB")

    label("loc_BB3")

    MenuCmd(1, 1, "　克洛斯贝尔·东出口")

    label("loc_BCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    MenuCmd(1, 1, "★克洛斯贝尔·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_C13")

    label("loc_BFB")

    MenuCmd(1, 1, "　克洛斯贝尔·西出口")

    label("loc_C13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C43")
    MenuCmd(1, 1, "★克洛斯贝尔·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_C5B")

    label("loc_C43")

    MenuCmd(1, 1, "　克洛斯贝尔·南出口")

    label("loc_C5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8B")
    MenuCmd(1, 1, "★克洛斯贝尔·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_CA3")

    label("loc_C8B")

    MenuCmd(1, 1, "　克洛斯贝尔·北出口")

    label("loc_CA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCB")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_CDB")

    label("loc_CCB")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_CDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D03")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_D13")

    label("loc_D03")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_D13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D41")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_D57")

    label("loc_D41")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_D57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D81")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_D93")

    label("loc_D81")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_D93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBD")
    MenuCmd(1, 1, "★玛因兹矿山镇")
    MenuCmd(3, 1, 0x9)
    Jump("loc_DCF")

    label("loc_DBD")

    MenuCmd(1, 1, "　玛因兹矿山镇")

    label("loc_DCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFF")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_E17")

    label("loc_DFF")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_E17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3D")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_E4B")

    label("loc_E3D")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_E4B")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FCD")
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
        (0, "loc_F20"),
        (1, "loc_F2E"),
        (2, "loc_F3C"),
        (3, "loc_F4A"),
        (4, "loc_F58"),
        (5, "loc_F66"),
        (6, "loc_F74"),
        (7, "loc_F82"),
        (8, "loc_F90"),
        (9, "loc_F9E"),
        (10, "loc_FAC"),
        (11, "loc_FBA"),
        (SWITCH_DEFAULT, "loc_FC8"),
    )


    label("loc_F20")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F2E")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F3C")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F4A")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F58")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F66")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F74")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F82")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F90")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_F9E")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_FAC")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_FBA")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FC8")

    label("loc_FC8")

    Jump("loc_FD7")

    label("loc_FCD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD7")

    Jump("loc_103A")

    label("loc_FDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1027")
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
    Jump("loc_103A")

    label("loc_1027")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_103A")

    Jump("loc_ADD")

    label("loc_103F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_AC3 end

    def Function_7_1047(): pass

    label("Function_7_1047")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_111B")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1121")

    label("loc_111B")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1121")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_1047 end

    def Function_8_1136(): pass

    label("Function_8_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_116B")
    TalkBegin(0xFF)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_1304")

    label("loc_116B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A5")
    TalkBegin(0xFF)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_1304")

    label("loc_11A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_11B6")
    Call(0, 3)
    Jump("loc_1304")

    label("loc_11B6")

    TalkBegin(0xFF)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_END)), "loc_1233")

    #C0005
    ChrTalk(
        0x101,
        (
            "#0001F今天还是不要坐巴士了吧。\x02\x03",

            "为了进行调查，\x01",
            "还是徒步走一走比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FE")

    label("loc_1233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1272")

    #C0006
    ChrTalk(
        0x101,
        (
            "#0001F继昨天之后……\x01",
            "今天也没法乘坐巴士啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FE")

    label("loc_1272")


    #C0007
    ChrTalk(
        0x101,
        (
            "#0001F继昨天之后……\x01",
            "今天也没法乘坐巴士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0104F嗯，走路去吧。\x02\x03",

            "#0100F说不定在路上\x01",
            "还会发现什么线索呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#0201F……加油吧。\x02",
    )

    CloseMessageWindow()

    label("loc_12FE")

    SetScenarioFlags(0x0, 1)
    TalkEnd(0xFF)

    label("loc_1304")

    Return()

    # Function_8_1136 end

    def Function_9_1305(): pass

    label("Function_9_1305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1329")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)
    Jump("loc_133F")

    label("loc_1329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133F")
    Call(0, 12)

    label("loc_133F")

    Return()

    # Function_9_1305 end

    def Function_10_1340(): pass

    label("Function_10_1340")

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

    def lambda_1412():
        OP_95(0xFE, 3270, 0, 13110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1412)

    def lambda_142C():
        OP_95(0xFE, 4430, 0, 12180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_142C)

    def lambda_1446():
        OP_95(0xFE, 2180, 0, 11520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1446)

    def lambda_1460():
        OP_95(0xFE, 2900, 0, 10410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1460)
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
        "#0205F#12P啊……\x02",
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

    def lambda_1509():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1509)
    Sleep(50)

    def lambda_1519():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1519)
    Sleep(50)

    def lambda_1529():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1529)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0011
    ChrTalk(
        0x101,
        "#0005F#5P缇欧，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0105F#5P莫非……\x01",
            "你又听到什么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#0201F#12P是……\x01",
            "我提高一下传感器的感知度！\x02",
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
        "#0007F#5P刚才的是……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#0101F#5P虽然很微弱……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0303F#11P嗯，大概是魔兽的远吠吧。\x02\x03",

            "#0300F要不是有阿缇注意到，\x01",
            "我们就都会听漏了。\x02",
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
        "#0203F#5P#40W呼……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0018
    ChrTalk(
        0x103,
        (
            "#0201F#12P……刚才的远吠\x01",
            "应该是从山道那边传来的。\x02\x03",

            "大概是在西北偏北方向，距离此处４０赛尔矩左右的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#0001F#5P西北偏北，距离４０赛尔矩……\x01",
            "大概是在山道途中吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        "#0305F#11P也就是说……\x02",
    )

    CloseMessageWindow()

    def lambda_18A6():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18A6)

    def lambda_18B3():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18B3)
    Sleep(50)

    def lambda_18C3():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18C3)

    def lambda_18D0():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18D0)
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
            "#0006F#5P那个……艾莉、缇欧。\x02\x03",

            "虽然继昨天之后，\x01",
            "这么说有点不太好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    def lambda_19A7():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19A7)

    #C0022
    ChrTalk(
        0x102,
        (
            "#0104F#11P不，不用介意。\x02\x03",

            "#0100F这也是机缘巧合吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0204F#12P……我也没问题。\x02\x03",

            "#0208F而且，刚才的远吠……\x01",
            "我感觉好像是在向\x01",
            "我们传达什么信息……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A4E():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A4E)
    Sleep(50)

    def lambda_1A5E():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A5E)

    #C0024
    ChrTalk(
        0x101,
        "#0005F#5P传达信息……？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        "#0301F#11P是威吓之类的感觉吗？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#0208F#12P不……我感觉到其中包含有\x01",
            "更加清晰的意志……\x02\x03",

            "#0206F……对不起，\x01",
            "好像找不到合适的语言来表达。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#0003F#5P是吗……\x02\x03",

            "#0001F……不管怎样，如果警备队出动，\x01",
            "就很可能会被它们逃掉。\x02\x03",

            "现在也只有靠我们自己\x01",
            "想办法将它们找出来了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0101F#5P是呀，加油吧。\x02\x03",

            "要正式调查山道的话，\x01",
            "最好多做些准备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0001F#5P嗯，而且到时候也没空闲\x01",
            "去处理其它支援请求了吧。\x02\x03",

            "先把该做的事情都解决掉，\x01",
            "再开始探索山道吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0302F#11P那么，准备完毕之后，\x01",
            "再踏上快乐的远足之行吧。\x02",
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

    # Function_10_1340 end

    def Function_11_1CC3(): pass

    label("Function_11_1CC3")

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

    # Function_11_1CC3 end

    def Function_12_1D06(): pass

    label("Function_12_1D06")

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
            "#0000F#11P这好像就是上士\x01",
            "驾驶的车辆吧？\x02\x03",

            "以前也曾\x01",
            "搭乘过几次……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        (
            "#0504F#11P嗯，是的。\x02\x03",

            "#0502F无论路况多么恶劣都能顺利行进，\x01",
            "是警备队引以为傲的轻装甲机动车呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0306F#11P不过，大概还是抵挡不了\x01",
            "战车的炮轰吧。\x02\x03",

            "#0300F最多也只能弹开\x01",
            "加特林炮弹这种级别的火力吧？\x02",
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
            "#0506F#12P呜呜……\x01",
            "请不要这么说嘛～\x02\x03",

            "#0501F它毕竟也算是汇集了最新技术的\x01",
            "高性能车辆～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F42():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F42)
    Sleep(50)

    def lambda_1F52():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F52)
    Sleep(50)

    def lambda_1F62():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F62)
    Sleep(50)

    def lambda_1F72():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F72)
    Sleep(300)

    #C0035
    ChrTalk(
        0x102,
        (
            "#0106F#6P嗯，说不定，是因为克洛斯贝尔\x01",
            "被限制储备战车……\x02\x03",

            "#0100F所以就打算\x01",
            "凭机动性来弥补吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#0203F#5P不仅是战车，连军用飞艇\x01",
            "也是一艘都没有呢。\x02\x03",

            "#0200F以克洛斯贝尔那充足的财政资源来说，\x01",
            "完全可以买下很多架了……\x02\x03",

            "果然还是因为帝国\x01",
            "与共和国施加了压力吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        (
            "#0506F#12P嗯……是啊。\x02\x03",

            "#0501F特别是帝国，在十二年前\x01",
            "的战争中，似乎曾因为利贝尔的\x01",
            "军用飞艇而吃尽苦头。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        (
            "#0103F#6P如果让克洛斯贝尔随意拥有，\x01",
            "万一敌对起来，对他们就很有威胁了……\x02\x03",

            "#0101F帝国和共和国的意图\x01",
            "都是不言自明啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0003F#5P原来如此……\x02\x03",

            "#0001F像克洛斯贝尔这样的地形，\x01",
            "要是有飞艇的话，\x01",
            "巡逻效率一定会更高的。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#0506F#12P唉，就是说嘛～\x02\x03",

            "#0504F──算啦，就不提这些啦。\x02\x03",

            "#0500F如果想乘坐车辆移动，\x01",
            "随时都可以和我说。\x02\x03",

            "只要是车子能去的地方，\x01",
            "我都可以送大家去。\x02",
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
            "今天一天，可以搭乘诺艾尔的警备队车辆，\x01",
            "在自治州各地自由移动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请在场景中调查警备队车辆，\x01",
            "并选择目的地。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "此外，如果丢下警备队车辆，\x01",
            "乘坐巴士或徒步移动至其它地点时，\x01",
            "警备队车辆依然会停留在原地。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请一定留意，\x01",
            "不要忘记停车地点。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※需要前往山道尽头的遗迹时，\x01",
            "  选择『玛因兹山道·隧道内』\x01",
            "  便可以抄近道。\x07\x00\x02",
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

    # Function_12_1D06 end

    def Function_13_2411(): pass

    label("Function_13_2411")

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

    def lambda_2551():
        OP_95(0xFE, 50, -2930, -8070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2551)
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

    # Function_13_2411 end

    def Function_14_259B(): pass

    label("Function_14_259B")

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

    # Function_14_259B end

    def Function_15_26FC(): pass

    label("Function_15_26FC")

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
            "调查停靠站的告示牌后，\x01",
            "就能乘坐导力巴士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进而便可迅速移动至所选目的地，\x01",
            "以更高的效率来往于各处。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_15_26FC end

    def Function_16_27BB(): pass

    label("Function_16_27BB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　南·克洛斯贝尔市\x01",
            "　东·克洛斯贝尔大圣堂\x01",
            "西北·矿山镇玛因兹　３１１赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_27BB end

    def Function_17_283A(): pass

    label("Function_17_283A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_28B2")

    #C0049
    ChrTalk(
        0x101,
        (
            "#0000F这边是玛因兹山道吗……\x02\x03",

            "#0003F现在更加在意乌尔拉斯医院那边。\x01",
            "还是不要绕道了，\x01",
            "直接去医院吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F5")

    label("loc_28B2")


    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F可不能带着琪雅\x01",
            "在市外乱走啊。\x02\x03",

            "#0000F还是不要绕道了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F5")

    SetChrPos(0x0, -27230, -2000, 65230, 135)
    EventEnd(0x4)
    Return()

    # Function_17_283A end

    SaveToFile()

Try(main)
