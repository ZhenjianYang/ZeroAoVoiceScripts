from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r1610.bin",                # FileName
        "r1610",                    # MapName
        "r1610",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x33,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 2000, 0, -3700, 0, 0, 1, 96, 0, 0, 0, 1],
    )

    BuildStringList((
        "r1610",                  # 0
        "幻兽",                   # 1
        "梅尔卡瓦九号机",         # 2
        "梅尔卡瓦光学迷彩",       # 3
        "梅尔卡瓦影子",           # 4
        "br1520",                 # 5
    ))

    ATBonus("ATBonus_200", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2C0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2E0", 0x0042, 255, 6, 45, 10, 1, 30, 0, "br1520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2C0", "MonsterBattlePostion_2A0", "ed7454", "ed7453", "ATBonus_200"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0040, 0, 6,   48.400001525878906,    -2.0,                  -2.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   -6.050000190734863,    0.25,                  0.20000000298023224,   1.0])

    DeclActor(48150,   0,       14450,   2000,    48150,   1000,    14450,   0x007C, 0,  2,  0x0000)
    DeclActor(40700,   0,       -14350,  1200,    40700,   2000,    -14350,  0x007C, 0,  4,  0x0000)
    DeclActor(61490,   -1000,   6830,    1200,    69090,   0,       5180,    0x007C, 0,  5,  0x0000)

    ChipFrameInfo(880, 0)                                        # 0

    ScpFunction((
        "Function_0_370",          # 00, 0
        "Function_1_407",          # 01, 1
        "Function_2_623",          # 02, 2
        "Function_3_6C1",          # 03, 3
        "Function_4_7B0",          # 04, 4
        "Function_5_ADD",          # 05, 5
        "Function_6_BA5",          # 06, 6
        "Function_7_BFE",          # 07, 7
        "Function_8_133A",         # 08, 8
        "Function_9_1B1C",         # 09, 9
        "Function_10_2C5E",        # 0A, 10
        "Function_11_2F23",        # 0B, 11
        "Function_12_3A8A",        # 0C, 12
        "Function_13_3AF5",        # 0D, 13
        "Function_14_3B84",        # 0E, 14
        "Function_15_3BD5",        # 0F, 15
        "Function_16_3C23",        # 10, 16
        "Function_17_3C88",        # 11, 17
        "Function_18_3CA3",        # 12, 18
    ))


    def Function_0_370(): pass

    label("Function_0_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_386")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39C")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3CF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    SetChrPos(0x0, 40700, 0, -14350, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E3")
    SetScenarioFlags(0x0, 0)
    Event(0, 7)

    label("loc_3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3F7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_406")

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_406")
    ClearScenarioFlags(0x22, 1)
    Event(0, 11)

    label("loc_406")

    Return()

    # Function_0_370 end

    def Function_1_407(): pass

    label("Function_1_407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_421")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_454")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_442")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_454")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_454")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_454")

    Sound(136, 1, 80, 0)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 69090, 0, 5180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BF")
    OP_66(0x0, 0x1)

    label("loc_4BF")

    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_510")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0xB4, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_53A")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_END)), "loc_534")
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFrame(0x4, "flower04", 0x0, 0x1)
    Jump("loc_53A")

    label("loc_534")

    ClearMapObjFlags(0x4, 0x4)

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B1")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_5B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_END)), "loc_5CA")
    SetMapObjFlags(0x0, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_5E4")

    label("loc_5CA")

    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 48390, -1000, -2000, 180)

    label("loc_5E4")

    MiniGame(0x2F, 0xFFFFFFFF, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_622")
    OP_1B(0x0, 0x0, 0x3)

    label("loc_622")

    Return()

    # Function_1_407 end

    def Function_2_623(): pass

    label("Function_2_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_END)), "loc_64F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_END)), "loc_63D")
    Call(0, 10)
    Jump("loc_64A")

    label("loc_63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A")
    Call(0, 9)

    label("loc_64A")

    Jump("loc_6C0")

    label("loc_64F")

    EventBegin(0x2)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "蓝花在地上绽放。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0002
    ChrTalk(
        0x101,
        (
            "#00000F（哦，这花可真漂亮啊，\x01",
            "  还散发着一层淡淡的晕光……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 3)
    EventEnd(0x3)

    label("loc_6C0")

    Return()

    # Function_2_623 end

    def Function_3_6C1(): pass

    label("Function_3_6C1")

    EventBegin(0x1)

    #C0003
    ChrTalk(
        0x101,
        (
            "#00003F（虽然已经把两个地点的\x01",
            "  幻兽都消灭了……\x01",
            "  但总觉得有点不对劲。）\x02\x03",

            "#00000F各位，我们不如再去\x01",
            "调查一下现场吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#00100F说的也是，总觉得还有\x01",
            "值得调查的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        "#00200F那就赶快回去，再调查一下吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2120, 0, -3710, 90)
    EventEnd(0x4)
    Return()

    # Function_3_6C1 end

    def Function_4_7B0(): pass

    label("Function_4_7B0")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E2")
    SetScenarioFlags(0x31, 2)

    label("loc_7E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_822")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_817")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_81D")

    label("loc_817")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_81D")

    Jump("loc_828")

    label("loc_822")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_828")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_899")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_879"),
        (SWITCH_DEFAULT, "loc_88A"),
    )


    label("loc_879")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_894")

    label("loc_88A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_894")

    Jump("loc_ACA")

    label("loc_899")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_8C9")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_8C9")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8F3"),
        (1, "loc_9F7"),
        (2, "loc_A88"),
        (SWITCH_DEFAULT, "loc_AC0"),
    )


    label("loc_8F3")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_924")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_934")

    label("loc_924")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_934")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_98A")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AD")
    Sound(461, 0, 100, 0)

    label("loc_9AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CD")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_9DD")

    label("loc_9CD")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_9DD")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_828")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A69")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_A2C")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_A44")

    label("loc_A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A3F")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_A44")

    label("loc_A3F")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_A44")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A83")

    label("loc_A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A79")
    OP_AF(0xFB)
    Jump("loc_A83")

    label("loc_A79")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A83")

    Jump("loc_ACA")

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ABB")

    label("loc_AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_AB1")
    OP_AF(0xFB)
    Jump("loc_ABB")

    label("loc_AB1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ABB")

    Jump("loc_ACA")

    label("loc_AC0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ACA")

    Jump("loc_828")

    label("loc_ACF")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_7B0 end

    def Function_5_ADD(): pass

    label("Function_5_ADD")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0006
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(64940, 850, 5910, 1500)
    MoveCamera(37, 19, 0, 1500)
    OP_6E(680, 1500)
    SetCameraDistance(17000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0007
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA0")
    OP_E2(0x2)
    MiniGame(0x6, 0xE, 0xF032, 0xFFFFFC18, 0x1AAE, 0x5A, 0x10DE2, 0x0, 0x143C)

    label("loc_BA0")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_5_ADD end

    def Function_6_BA5(): pass

    label("Function_6_BA5")

    Battle("BattleInfo_2E0", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE7")
    OP_90(0x0, 37650, 0, -3750, 90)
    EventEnd(0x5)
    Jump("loc_BFD")

    label("loc_BE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFA")
    Jump("loc_BFD")

    label("loc_BFA")

    Call(0, 8)

    label("loc_BFD")

    Return()

    # Function_6_BA5 end

    def Function_7_BFE(): pass

    label("Function_7_BFE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(2100, 1000, -3700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_68(3100, 1000, -3700, 1300)
    SetCameraDistance(18000, 1300)
    SetChrPos(0x101, 2400, 0, -3700, 90)
    SetChrPos(0x102, 1700, 0, -5000, 90)
    SetChrPos(0x103, 1500, 0, -3000, 90)
    SetChrPos(0x104, 700, 0, -4500, 90)
    SetChrPos(0x109, 900, 0, -2500, 90)
    SetChrPos(0x105, -500, 0, -3700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)

    def lambda_CDA():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CDA)
    Sleep(0)

    def lambda_CF2():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CF2)
    Sleep(0)

    def lambda_D0A():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D0A)
    Sleep(0)

    def lambda_D22():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D22)
    Sleep(0)

    def lambda_D3A():
        OP_9B(0x0, 0x109, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D3A)
    Sleep(0)

    def lambda_D52():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D52)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_6F(0x79)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6B")

    #C0008
    ChrTalk(
        0x109,
        "#10111F#5P（啊……！）\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00013F#5P（那就是『幻兽』吗……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_E6B")


    #C0010
    ChrTalk(
        0x105,
        "#10305F#6P（哦……）\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#00013F#5P（在这里啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_EA5")

    PlayBGM("ed7573", 0)
    OP_68(46900, 1050, -2950, 4000)
    MoveCamera(65, 10, 0, 4000)
    SetCameraDistance(21000, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(46900, 1050, -2950, 0)
    MoveCamera(41, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24310, 0)
    OP_68(47700, 1050, -1800, 6000)
    MoveCamera(127, 30, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(23000, 6000)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1186")

    #C0012
    ChrTalk(
        0x104,
        (
            "#00303F#9P（和报告中提到的一样，相当巨大呢……）\x02\x03",

            "#00301F（阿缇，力场扭曲了吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#00203F#9P（时、空、幻……\x01",
            "  这里确实出现了上级三属性。）\x02\x03",

            "#00201F（目前还不清楚发生此现象的原因。）\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#00108F#9P（是吗……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(3100, 1000, -3700, 0)
    MoveCamera(45, 22, 0, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    def lambda_1050():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1050)
    Sleep(0)

    def lambda_1060():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1060)
    Sleep(0)

    def lambda_1070():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1070)
    Sleep(0)

    def lambda_1080():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1080)
    Sleep(0)

    def lambda_1090():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1090)
    Sleep(0)

    def lambda_10A0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10A0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0015
    ChrTalk(
        0x105,
        (
            "#10301F#6P（那么……\x01",
            "  我们该怎么办？）\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00003F#11P（根据警备队的报告来看，\x01",
            "  是相当危险的类型呢……）\x02\x03",

            "#00013F（消灭它的时候一定要多加小心。）\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x109,
        "#10101F#5P（明白了……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1304")

    label("loc_1186")


    #C0018
    ChrTalk(
        0x102,
        (
            "#00101F#9P（缇欧……\x01",
            "  力场的扭曲情况如何？）\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#00203F#9P（这里也出现了上级三属性……）\x02\x03",

            "#00201F（发生此现象的原因仍旧不明。）\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        "#00306F#9P（果然如此……）\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        (
            "#10308F#9P（但幻兽似乎并不是\x01",
            "  引发此现象的原因呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(3100, 1000, -3700, 0)
    MoveCamera(45, 22, 0, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    #C0022
    ChrTalk(
        0x109,
        (
            "#10101F#5P（罗伊德警官……\x01",
            "  要马上动手把它消灭吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00013F#5P（嗯，大家一定要小心行事……！）\x02",
    )

    CloseMessageWindow()

    label("loc_1304")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3400, 0, -3700, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 3)
    EventEnd(0x5)
    Return()

    # Function_7_BFE end

    def Function_8_133A(): pass

    label("Function_8_133A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    OP_68(42650, 1500, -3700, 0)
    MoveCamera(50, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(38650, 1000, -3700, 3000)
    MoveCamera(45, 16, 0, 3000)
    SetCameraDistance(17000, 3000)
    SetChrPos(0x101, 39650, 0, -3700, 90)
    SetChrPos(0x102, 38500, 0, -2850, 90)
    SetChrPos(0x103, 37100, 0, -3850, 90)
    SetChrPos(0x104, 39350, 0, -4900, 90)
    SetChrPos(0x109, 37500, 0, -5150, 90)
    SetChrPos(0x105, 40000, 0, -2000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_29(0xA6, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B6")

    #C0024
    ChrTalk(
        0x101,
        (
            "#00006F#5P唔……！\x01",
            "真是相当难对付啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#00108F#6P而且，果然还是一样……\x01",
            "以不可思议的方式消失了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_1544():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1544)
    Sleep(50)

    def lambda_1554():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1554)
    Sleep(50)

    def lambda_1564():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1564)
    Sleep(50)

    def lambda_1574():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1574)
    Sleep(50)

    def lambda_1584():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1584)
    Sleep(50)

    def lambda_1594():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1594)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    #C0026
    ChrTalk(
        0x109,
        (
            "#10108F#12P缇欧，\x01",
            "『力场扭曲』的情况如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00206F#6P……还没消失，\x01",
            "上级三属性仍然存在。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F#11P真是的……\x01",
            "到底是什么原因啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x105,
        (
            "#10303F#5P看来『幻兽』并不是\x01",
            "引发力场扭曲的原因……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00013F#11P……有必要去\x01",
            "调查另一头幻兽呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A82")

    label("loc_16B6")


    #C0031
    ChrTalk(
        0x105,
        (
            "#10306F#5P哎呀呀……\x01",
            "这头幻兽也很难对付。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#10101F#6P而且消失的方式和之前那头一样……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_175C():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_175C)
    Sleep(50)

    def lambda_176C():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_176C)
    Sleep(50)

    def lambda_177C():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_177C)
    Sleep(50)

    def lambda_178C():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_178C)
    Sleep(50)

    def lambda_179C():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_179C)
    Sleep(50)

    def lambda_17AC():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_17AC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    #C0033
    ChrTalk(
        0x104,
        (
            "#00301F#11P所谓的『力场扭曲』现象\x01",
            "还是没有消失吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#00203F#6P是啊……\x02\x03",

            "#00201F我认为应该存在某些\x01",
            "具体原因。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x101,
        (
            "#00005F#11P具体原因……？\x01",
            "比如说呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#00206F#6P……这个嘛……\x01",
            "从刚才开始，我的感觉就\x01",
            "一直被『扭曲』所干扰……\x02\x03",

            "#00200F各位说不定能在我\x01",
            "之前发现原因呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#00105F#5P是、是吗？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00003F#11P好……\x01",
            "那我们就在这里搜索一圈吧。\x02\x03",

            "#00000F这附近肯定存在着某种可以引发\x01",
            "『力场扭曲』现象的东西。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19D1():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19D1)
    Sleep(50)

    def lambda_19E1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19E1)
    Sleep(50)

    def lambda_19F1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19F1)
    Sleep(50)

    def lambda_1A01():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A01)
    Sleep(50)

    def lambda_1A11():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A11)
    Sleep(50)

    def lambda_1A21():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A21)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0039
    ChrTalk(
        0x109,
        "#10100F#6P明白了！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        "#00300F#12P那就四处找找看吧！\x02",
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_1A82")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了乌尔斯拉间道的幻兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 39650, 0, -3700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 4)
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B0C")
    OP_1B(0x0, 0x0, 0x3)

    label("loc_1B0C")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_8_133A end

    def Function_9_1B1C(): pass

    label("Function_9_1B1C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51216.itc", 0x1E)
    SoundLoad(961)
    SoundLoad(828)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis252.itp")
    LoadEffect(0x0, "event/ev14005.eff")
    LoadEffect(0x1, "event/ev14007.eff")
    OP_68(48500, 1000, 14050, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(19000, 1000)
    SetChrPos(0x101, 49400, 0, 14050, 270)
    SetChrPos(0x102, 49600, 0, 15400, 225)
    SetChrPos(0x103, 49200, 0, 12900, 315)
    SetChrPos(0x104, 49200, 0, 16300, 225)
    SetChrPos(0x109, 48000, 0, 16000, 180)
    SetChrPos(0x105, 46200, 0, 14200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9D")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0042
    AnonymousTalk(
        0x101,
        "#00005F这花是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 4)), scpexpr(EXPR_END)), "loc_1D21")

    #A0043
    AnonymousTalk(
        0x102,
        (
            "#00108F我记得东克洛斯贝尔街道的\x01",
            "沼泽也开着这种花呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0044
    AnonymousTalk(
        0x104,
        "#00305F是啊，确实见到过这种花。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1DA1")

    label("loc_1D21")


    #A0045
    AnonymousTalk(
        0x105,
        (
            "#10302F东克洛斯贝尔街道的沼泽\x01",
            "好像也开着这种花吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0046
    AnonymousTalk(
        0x101,
        "#00011F有、有这回事吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0047
    AnonymousTalk(
        0x102,
        (
            "#00108F嗯，\x01",
            "我也有些印象……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1DA1")


    #A0048
    AnonymousTalk(
        0x109,
        (
            "#10109F好漂亮的花啊……\x02\x03",

            "#10102F……以前从没见过这种花，\x01",
            "它的名字是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0049
    AnonymousTalk(
        0x101,
        "#00001F唔……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0050
    ChrTalk(
        0x101,
        (
            "#00003F#11P（……难道……）\x02\x03",

            "#00001F（嗯，姑且一试吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x160, 5)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_1F3D")

    label("loc_1E9D")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0051
    AnonymousTalk(
        0x101,
        (
            "#00003F#11P（……难道……）\x02\x03",

            "#00001F（嗯，姑且一试吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_1F3D")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "摘下蓝花\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F85"),
        (1, "loc_2C1F"),
        (SWITCH_DEFAULT, "loc_2C5D"),
    )


    label("loc_1F85")

    OP_9B(0x0, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0052
    ChrTalk(
        0x102,
        "#00105F罗伊德……？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x105,
        (
            "#10305F#6P怎么？你想把\x01",
            "这朵花摘下来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00003F#11P是啊……\x01",
            "虽说有点残忍……\x02",
        )
    )

    CloseMessageWindow()
    Sound(929, 0, 40, 0)
    Sound(828, 2, 30, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 48200, 600, 14450, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
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

    #C0055
    ChrTalk(
        0x104,
        "#00301F#5P怎、怎么回事！？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        "#00205F#12P这是……！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00001F#11P唔……！\x02",
    )

    CloseMessageWindow()
    SetMapObjFrame(0x4, "flower04", 0x0, 0x1)
    StopEffect(0x0, 0x2)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(961, 2, 70, 0)
    Sound(233, 0, 100, 0)
    Sound(929, 0, 60, 0)
    PlayEffect(0x1, 0x1, 0x101, 0x3, 0, 1050, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x5DC)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0xB4, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    MoveCamera(45, 30, 10, 3000)
    SetCameraDistance(8000, 3000)
    OP_6E(1000, 3000)
    Sleep(2500)
    Sound(829, 0, 100, 0)
    StopSound(961, 2000, 60)
    StopSound(828, 2000, 20)
    FadeToDark(500, 16777215, -1)
    Sleep(800)
    FadeToBright(300, 16777215)
    CancelBlur(300)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x32)
    OP_11(0xA7, 0xDD, 0xFE, 0x1E, 0xB4, 0x32)
    MoveCamera(45, 16, 0, 50)
    SetCameraDistance(19000, 50)
    OP_6E(500, 50)
    StopEffect(0x1, 0x2)
    Sleep(500)
    OP_6F(0x79)
    StopBGM(0x1770)

    #C0058
    ChrTalk(
        0x101,
        "#00013F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x109,
        "#10111F#5P刚、刚才那是……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        "#00108F空间似乎晃动了一下呢……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    #C0061
    ChrTalk(
        0x105,
        (
            "#10308F#6P……缇欧，\x01",
            "『力场扭曲』的情况如何了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0062
    ChrTalk(
        0x103,
        (
            "#00203F#12P……上级三属性的\x01",
            "气息完全消失了。\x02\x03",

            "#00201F在这一带已经感知不到\x01",
            "任何异常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00006F#11P是吗……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00305F#5P等、等等。\x02\x03",

            "#00307F难道就是这种蓝花\x01",
            "引起了异常现象吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0065
    ChrTalk(
        0x105,
        (
            "#10304F#6P目前看来，正是如此。\x02\x03",

            "#10300F虽然我也很难相信\x01",
            "小小一朵花就有如此力量……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#00101F真、真不敢相信……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x109,
        (
            "#10101F#5P这、这到底是\x01",
            "什么花啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#00206F#12P……现在已经无法从这朵花上\x01",
            "感知到奇怪的气息了……\x02\x03",

            "#00200F不管怎么说，还是找个地方\x01",
            "调查一下这种花为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00008F#11P说的也是……\x02\x03",

            "#00003F……但医科大学好像\x01",
            "和这种事情挂不上钩。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00100F总、总之，一定要把它小心收好，\x01",
            "注意别弄丢了。\x02\x03",

            "以后要是想到了适合咨询的地方，\x01",
            "再继续调查就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00006F#11P嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x2EE, 0x3E8, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x105)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0072
    ChrTalk(
        0x105,
        "#10303F#6P……唔………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_2699():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2699)
    Sleep(50)

    def lambda_26A9():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_26A9)
    Sleep(50)

    def lambda_26B9():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_26B9)
    Sleep(50)

    def lambda_26C9():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_26C9)
    Sleep(50)

    def lambda_26D9():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_26D9)
    Sleep(50)

    def lambda_26E9():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_26E9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x101,
        "#00005F#11P瓦吉……？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        "#10101F#5P莫非你有什么头绪吗？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x105,
        (
            "#10303F#6P这个嘛……\x01",
            "说不定只是我记错了。\x02\x03",

            "#10301F印象中，似乎曾在教会的圣典中\x01",
            "看过一个有关奇异蓝花的传说。\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(1000)

    #C0076
    ChrTalk(
        0x101,
        "#00011F#11P咦……！？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        "#00305F#5P喂喂，你是说真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x105,
        (
            "#10306F#6P这个嘛，毕竟是很久以前看到的了，\x01",
            "而且只是随便扫了一眼……\x02\x03",

            "#10300F艾莉，你有没有什么印象？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#00112F#11P我也不可能把\x01",
            "所有圣典看遍啊……\x02\x03",

            "#00103F……不过，好像确实\x01",
            "看过类似的记载。\x02\x03",

            "#00108F关于拥有奇异力量的\x01",
            "『蓝花』的传说……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0080
    ChrTalk(
        0x109,
        (
            "#10111F#6P那、那应该……\x01",
            "就没错了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0081
    ChrTalk(
        0x103,
        (
            "#00201F#12P看来有必要去向\x01",
            "教会的人员确认一下呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29E6():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29E6)
    Sleep(50)

    def lambda_29F6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_29F6)
    Sleep(50)

    def lambda_2A06():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2A06)
    Sleep(50)

    def lambda_2A16():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2A16)
    Sleep(50)

    def lambda_2A26():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A26)
    Sleep(50)

    def lambda_2A36():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2A36)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2AE0")

    #C0082
    ChrTalk(
        0x101,
        (
            "#00003F#11P……是啊。\x02\x03",

            "#00000F那我们就去找玛布尔老师\x01",
            "或莉丝小姐问问看吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#00104F说的也是……\x01",
            "这两人都很适合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B79")

    label("loc_2AE0")


    #C0084
    ChrTalk(
        0x101,
        (
            "#00003F#11P……是啊。\x02\x03",

            "#00000F最适合的咨询对象\x01",
            "显然还是玛布尔老师吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#00104F嗯，我也这样想。\x02\x03",

            "#00108F（不过，其实也可以找『她』咨询一下……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B79")


    #C0086
    ChrTalk(
        0x104,
        (
            "#00300F#5P好～那我们这就去\x01",
            "克洛斯贝尔大圣堂吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 49400, 0, 14050, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    AddItemNumber(0x333, 1)
    SetScenarioFlags(0x160, 6)
    OP_29(0xA6, 0x1, 0x5)
    OP_65(0x0, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7200", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3C1)
    OP_24(0x33C)
    EventEnd(0x5)
    Jump("loc_2C5D")

    label("loc_2C1F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 49400, 0, 14050, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_2C5D")

    label("loc_2C5D")

    Return()

    # Function_9_1B1C end

    def Function_10_2C5E(): pass

    label("Function_10_2C5E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis252.itp")
    OP_68(48500, 1000, 14050, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 49400, 0, 14050, 270)
    SetChrPos(0x102, 49600, 0, 15400, 225)
    SetChrPos(0x103, 49200, 0, 12900, 315)
    SetChrPos(0x104, 49200, 0, 16300, 225)
    SetChrPos(0x109, 48000, 0, 16000, 180)
    SetChrPos(0x105, 46200, 0, 14200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #A0087
    AnonymousTalk(
        0x109,
        (
            "#10100F对、对了……\x02\x03",

            "是不是应该把这里的花\x01",
            "也一并摘掉呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0088
    AnonymousTalk(
        0x101,
        (
            "#00000F不了……\x01",
            "这里的花就先留着吧。\x02\x03",

            "说不定会成为\x01",
            "珍贵的样品。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0089
    AnonymousTalk(
        0x103,
        (
            "#00200F……说的也是。\x01",
            "毕竟摘下之后，它的力量就会随之消失。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0090
    AnonymousTalk(
        0x102,
        (
            "#00100F不过……如果幻兽再次出现，\x01",
            "可就不得不把它摘掉了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0091
    AnonymousTalk(
        0x104,
        "#00300F嗯，那就到时再说吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 49400, 0, 14050, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 7)
    EventEnd(0x5)
    Return()

    # Function_10_2C5E end

    def Function_11_2F23(): pass

    label("Function_11_2F23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch03154.itc", 0x1E)
    LoadEffect(0x0, "event/ev17025.eff")
    LoadEffect(0x1, "event/ev17026.eff")
    CreatePortrait(0, 67, 20, 413, 252, 0, 0, 512, 256, 0, 0, 346, 232, 0xFFFFFF, 0x0, "c_vis242.itp")
    SoundLoad(497)
    SoundLoad(950)
    SoundLoad(852)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x8, 0x9)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    OP_75(0x8, 0x1, 0x0)
    OP_71(0x8, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x8, 0x2EE, 0x2EE, 0x2EE)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x1, 0x65, 0xA0, 0x0, 0x20)
    OP_FF(0x1, 0x307, 0x307, 0x307)
    ClearChrFlags(0xB, 0x80)
    OP_78(0xA, 0xB)
    OP_49()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_75(0xA, 0x1, 0x0)
    OP_FF(0xA, 0x2EE, 0x2EE, 0x2EE)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x107, 0x80)
    SetMapObjFlags(0x5, 0x4)
    OP_68(35000, 1850, -1900, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(67500, 0)
    OP_68(37500, 5500, -11350, 8000)
    MoveCamera(45, 30, 0, 8000)
    OP_6E(680, 8000)
    SetCameraDistance(41500, 8000)
    SetChrPos(0x9, 37500, 15250, -11350, 315)
    OP_D5(0x9, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0xA, 37500, 15250, -11350, 315)
    OP_D5(0xA, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0xB, 37500, 0, -11350, 315)
    OP_D5(0xB, 0x0, 0x4CE78, 0x0, 0x0)
    OP_82(0x64, 0x64, 0xBB8, 0x1F40)
    BeginChrThread(0x9, 0, 0, 14)
    BeginChrThread(0x9, 1, 0, 12)
    BeginChrThread(0xA, 1, 0, 12)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x0)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x101, 36500, 0, -10050, 315)
    SetChrPos(0x105, 38000, 0, -10200, 315)
    SetChrPos(0x107, 37550, 0, -12100, 315)
    SetChrPos(0x9, 37500, 5500, -11000, 0)
    SetChrPos(0xA, 37500, 5500, -11000, 0)
    BeginChrThread(0x9, 0, 0, 13)
    BeginChrThread(0xA, 0, 0, 13)
    OP_68(36500, 1000, -12500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(16000, 0)
    OP_68(33500, 1000, -8500, 3000)

    def lambda_3224():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3224)
    Sleep(50)

    def lambda_323C():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_323C)
    Sleep(50)

    def lambda_3254():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3254)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    OP_25(0x1F1, 0x50)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x107, 0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x107, 0x80)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrPos(0x9, 37500, 20250, -11350, 315)
    SetChrPos(0xA, 37500, 20250, -11350, 315)

    def lambda_32C4():
        OP_96(0xFE, 0x927C, 0x7A120, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32C4)

    def lambda_32DE():
        OP_96(0xFE, 0x927C, 0x7A120, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_32DE)
    BeginChrThread(0x9, 0, 0, 16)
    BeginChrThread(0xA, 0, 0, 15)
    OP_68(36500, 16000, -12500, 0)
    MoveCamera(90, -65, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(1000)
    StopSound(497, 6000, 60)

    #A0092
    AnonymousTalk(
        0x101,
        "#00001F梅尔卡瓦要暂时返回上空吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0093
    AnonymousTalk(
        0x105,
        (
            "#10403F嗯，如果一直停留在地面，\x01",
            "会有被感知到的危险。\x02\x03",

            "#10400F那么……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x101, 38250, 0, -11450, 135)
    SetChrPos(0x105, 38250, 0, -12250, 135)
    SetChrPos(0x107, 36250, 0, -12950, 135)
    SetChrSubChip(0x107, 0x5)
    OP_68(38250, 1000, -12250, 0)
    MoveCamera(70, 20, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(15500, 0)
    OP_68(39230, 1000, -13300, 1500)
    OP_95(0x105, 39050, 0, -13100, 1000, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    SetCameraDistance(15000, 800)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0094
    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#5P#40W以空之女神之名，\x01",
            "祝圣之七耀，于此处显现。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(357, 0, 50, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x105, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(13000, 20000)
    BeginChrThread(0x105, 3, 0, 17)
    BeginChrThread(0x9, 1, 0, 18)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1500)

    #C0095
    ChrTalk(
        0x101,
        (
            "#00005F#5P啊……\x01",
            "（和玛布尔老师那时的法术一样……）\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x107,
        "#01200F#6P#3C唔，是星杯法术啊。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#5P#40W大地之琥耀、空之金耀──\x02\x03",

            "#10401F以此融合为契，\x01",
            "形成避过『巨目』监视\x01",
            "的微小圣域吧。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x105, 0x3)
    SetCameraDistance(13000, 1000)
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x105, 0x3)
    Sleep(50)
    Sound(3091, 255, 80, 0)    #voice#Lazy
    SetChrSubChip(0x105, 0x4)
    SetMapObjFrame(0x7, "Null_fream", 0x2, "start")
    Sleep(500)
    Sound(222, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 40700, 100, -14350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    FadeToDark(250, 16777215, -1)
    Sound(928, 0, 100, 0)
    Sound(934, 0, 50, 0)
    OP_0D()
    Sleep(500)
    StopSound(852, 1000, 100)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    FadeToBright(2000, 16777215)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(500)

    #C0098
    ChrTalk(
        0x101,
        "#00001F这是……\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)

    #C0099
    ChrTalk(
        0x105,
        (
            "#10404F#11P将力场的『狭间』\x01",
            "固定于此的『法阵』。\x02\x03",

            "已经施加了特殊法术，\x01",
            "除了我们之外，没人能看到它。\x02\x03",

            "#10402F总之，至少在短时间\x01",
            "之内可以勉强应付一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3780():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3780)
    Sleep(50)

    def lambda_3790():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3790)
    Sleep(50)

    def lambda_37A0():
        TurnDirection(0x107, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_37A0)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)

    #C0100
    ChrTalk(
        0x101,
        (
            "#00012F#5P原、原来如此。\x02\x03",

            "#00002F话说回来，瓦吉……\x01",
            "看来你还真是教会中的人士啊。\x02\x03",

            "但从你以往的言谈举止来看，\x01",
            "真是完全没有真实感。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#10404F#11P呵呵，总之我不喜欢\x01",
            "太过死板的作风，\x01",
            "至少这一点是一直没变的。\x02\x03",

            "#10400F好啦，接下来要怎么做？\x02\x03",

            "要去乌尔斯拉医院\x01",
            "那边看看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00003F#5P嗯，过去看看吧。\x02\x03",

            "#00008F另外……\x01",
            "如果情势允许，我还想去\x01",
            "克洛斯贝尔市那边看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3C嗯，那样也好。\x02\x03",

            "#01201F不过，由于受到灵智之草的影响，\x01",
            "郊外的道路上有时会出现幻兽。\x02\x03",

            "一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xD7, 0x1F4)

    #C0104
    ChrTalk(
        0x101,
        "#00013F#5P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x105,
        "#10400F#11P那我们就出发吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_37()
    SetChrPos(0x0, 37370, 0, -13400, 270)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x9, 0x80)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x1, 0x4)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0xA, 0x4)
    SetScenarioFlags(0x1A0, 2)
    OP_29(0xAF, 0x1, 0x1)
    OP_24(0x1F1)
    OP_24(0x3B6)
    OP_24(0x354)
    SetScenarioFlags(0x20, 5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_2F23 end

    def Function_12_3A8A(): pass

    label("Function_12_3A8A")

    OP_96(0xFE, 0x927C, 0x1D4C, 0xFFFFD508, 0x9C4, 0x1)
    OP_96(0xFE, 0x927C, 0x1B58, 0xFFFFD508, 0x7D0, 0x1)
    OP_96(0xFE, 0x927C, 0x1964, 0xFFFFD508, 0x5DC, 0x1)
    OP_96(0xFE, 0x927C, 0x1770, 0xFFFFD508, 0x3E8, 0x1)
    OP_96(0xFE, 0x927C, 0x157C, 0xFFFFD508, 0x1F4, 0x1)
    BeginChrThread(0xFE, 3, 0, 13)
    Return()

    # Function_12_3A8A end

    def Function_13_3AF5(): pass

    label("Function_13_3AF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B83")
    OP_96(0xFE, 0x927C, 0x14B4, 0xFFFFD508, 0x190, 0x1)
    OP_96(0xFE, 0x927C, 0x1450, 0xFFFFD508, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0x927C, 0x14B4, 0xFFFFD508, 0xC8, 0x1)
    OP_96(0xFE, 0x927C, 0x1644, 0xFFFFD508, 0x190, 0x1)
    OP_96(0xFE, 0x927C, 0x16A8, 0xFFFFD508, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0x927C, 0x1644, 0xFFFFD508, 0xC8, 0x1)
    Jump("Function_13_3AF5")

    label("loc_3B83")

    Return()

    # Function_13_3AF5 end

    def Function_14_3B84(): pass

    label("Function_14_3B84")

    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0x1, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_75(0x8, 0x2, 0x7D0)
    OP_75(0xA, 0x2, 0x7D0)
    Sleep(1000)
    OP_79(0x1)
    OP_71(0x8, 0x65, 0xA0, 0x1, 0x20)
    Return()

    # Function_14_3B84 end

    def Function_15_3BD5(): pass

    label("Function_15_3BD5")

    OP_75(0x8, 0x1, 0x7D0)
    OP_75(0xA, 0x1, 0x7D0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0x1, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_79(0x1)
    OP_71(0x1, 0x65, 0xA0, 0x0, 0x20)
    Return()

    # Function_15_3BD5 end

    def Function_16_3C23(): pass

    label("Function_16_3C23")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_16_3C23 end

    def Function_17_3C88(): pass

    label("Function_17_3C88")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CA2")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_17_3C88")

    label("loc_3CA2")

    Return()

    # Function_17_3C88 end

    def Function_18_3CA3(): pass

    label("Function_18_3CA3")

    SetMapObjFrame(0x6, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0x6, "Null_fream", 0x2, "loop")
    Return()

    # Function_18_3CA3 end

    SaveToFile()

Try(main)
