from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "幻獣",                   # 1
        "メルカバ玖号機",         # 2
        "メルカバ光学迷彩",       # 3
        "メルカバ影",             # 4
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
        "Function_3_6D1",          # 03, 3
        "Function_4_7E8",          # 04, 4
        "Function_5_B2B",          # 05, 5
        "Function_6_BFF",          # 06, 6
        "Function_7_C58",          # 07, 7
        "Function_8_13C0",         # 08, 8
        "Function_9_1C2C",         # 09, 9
        "Function_10_2F06",        # 0A, 10
        "Function_11_31F7",        # 0B, 11
        "Function_12_3DF4",        # 0C, 12
        "Function_13_3E5F",        # 0D, 13
        "Function_14_3EEE",        # 0E, 14
        "Function_15_3F3F",        # 0F, 15
        "Function_16_3F8D",        # 10, 16
        "Function_17_3FF2",        # 11, 17
        "Function_18_400D",        # 12, 18
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

    Jump("loc_6D0")

    label("loc_64F")

    EventBegin(0x2)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "蒼い花が咲いている。\x07\x00\x02",
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
            "#00000F（なんていうか、綺麗な花だな。\x01",
            "  淡く輝いているみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 3)
    EventEnd(0x3)

    label("loc_6D0")

    Return()

    # Function_2_623 end

    def Function_3_6D1(): pass

    label("Function_3_6D1")

    EventBegin(0x1)

    #C0003
    ChrTalk(
        0x101,
        (
            "#00003F（これで幻獣は２体とも\x01",
            "  倒したわけだけど……\x01",
            "  なにかが気になるな。）\x02\x03",

            "#00000Fみんな、ちょっと現場を\x01",
            "改めて調べ直してもいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#00100F確かに、ここでするべきことは\x01",
            "まだありそうな気もするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        "#00200Fでは、早速戻って調べましょう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2120, 0, -3710, 90)
    EventEnd(0x4)
    Return()

    # Function_3_6D1 end

    def Function_4_7E8(): pass

    label("Function_4_7E8")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81A")
    SetScenarioFlags(0x31, 2)

    label("loc_81A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_860")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_85A")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_84F")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_855")

    label("loc_84F")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_855")

    Jump("loc_860")

    label("loc_85A")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_860")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_8D9")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8B9"),
        (SWITCH_DEFAULT, "loc_8CA"),
    )


    label("loc_8B9")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_8D4")

    label("loc_8CA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D4")

    Jump("loc_B18")

    label("loc_8D9")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_90D")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_90D")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_941"),
        (1, "loc_A45"),
        (2, "loc_AD6"),
        (SWITCH_DEFAULT, "loc_B0E"),
    )


    label("loc_941")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_972")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_982")

    label("loc_972")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_982")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D8")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FB")
    Sound(461, 0, 100, 0)

    label("loc_9FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A1B")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_A2B")

    label("loc_A1B")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_A2B")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_860")

    label("loc_A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_AB7")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_A7A")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_A92")

    label("loc_A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A8D")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_A92")

    label("loc_A8D")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_A92")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD1")

    label("loc_AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_AC7")
    OP_AF(0xFB)
    Jump("loc_AD1")

    label("loc_AC7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD1")

    Jump("loc_B18")

    label("loc_AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B09")

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_AFF")
    OP_AF(0xFB)
    Jump("loc_B09")

    label("loc_AFF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B09")

    Jump("loc_B18")

    label("loc_B0E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B18")

    Jump("loc_860")

    label("loc_B1D")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_7E8 end

    def Function_5_B2B(): pass

    label("Function_5_B2B")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0006
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFA")
    OP_E2(0x2)
    MiniGame(0x6, 0xE, 0xF032, 0xFFFFFC18, 0x1AAE, 0x5A, 0x10DE2, 0x0, 0x143C)

    label("loc_BFA")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_5_B2B end

    def Function_6_BFF(): pass

    label("Function_6_BFF")

    Battle("BattleInfo_2E0", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C41")
    OP_90(0x0, 37650, 0, -3750, 90)
    EventEnd(0x5)
    Jump("loc_C57")

    label("loc_C41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C54")
    Jump("loc_C57")

    label("loc_C54")

    Call(0, 8)

    label("loc_C57")

    Return()

    # Function_6_BFF end

    def Function_7_C58(): pass

    label("Function_7_C58")

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

    def lambda_D34():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D34)
    Sleep(0)

    def lambda_D4C():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D4C)
    Sleep(0)

    def lambda_D64():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D64)
    Sleep(0)

    def lambda_D7C():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D7C)
    Sleep(0)

    def lambda_D94():
        OP_9B(0x0, 0x109, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D94)
    Sleep(0)

    def lambda_DAC():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DAC)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC5")

    #C0008
    ChrTalk(
        0x109,
        "#10111F#5P（あ……！）\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00013F#5P（あれが《幻獣》か……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_F03")

    label("loc_EC5")


    #C0010
    ChrTalk(
        0x105,
        "#10305F#6P（おっと……）\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#00013F#5P（いたか……！）\x02",
    )

    CloseMessageWindow()

    label("loc_F03")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FA")

    #C0012
    ChrTalk(
        0x104,
        (
            "#00303F#9P（報告通り、結構デケェな……）\x02\x03",

            "#00301F（ティオすけ、場の歪みはどうだ？）\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#00203F#9P（時・空・幻……\x01",
            "  上位三属性の発現を確認しました。）\x02\x03",

            "#00201F（今のところ原因は不明です。）\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#00108F#9P（そう……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(3100, 1000, -3700, 0)
    MoveCamera(45, 22, 0, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    def lambda_10B2():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10B2)
    Sleep(0)

    def lambda_10C2():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10C2)
    Sleep(0)

    def lambda_10D2():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10D2)
    Sleep(0)

    def lambda_10E2():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10E2)
    Sleep(0)

    def lambda_10F2():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10F2)
    Sleep(0)

    def lambda_1102():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1102)
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
            "#10301F#6P（それで……\x01",
            "  結局どうするんだい？）\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00003F#11P（警備隊の報告では\x01",
            "  かなり危険なタイプみたいだ……）\x02\x03",

            "#00013F（退治するなら慎重に仕掛けよう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x109,
        "#10101F#5P（了解しました……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_138A")

    label("loc_11FA")


    #C0018
    ChrTalk(
        0x102,
        (
            "#00101F#9P（ティオちゃん……\x01",
            "  場の歪みの方はどう？）\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#00203F#9P（同じく上位三属性の発現を確認……）\x02\x03",

            "#00201F（やはり原因は不明です。）\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        "#00306F#9P（やっぱりか……）\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        (
            "#10308F#9P（どうやら幻獣そのものが\x01",
            "  原因じゃなさそうだけど……）\x02",
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
            "#10101F#5P（ロイドさん……\x01",
            "  さっそく仕掛けますか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00013F#5P（ああ、慎重に行こう……！）\x02",
    )

    CloseMessageWindow()

    label("loc_138A")

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

    # Function_7_C58 end

    def Function_8_13C0(): pass

    label("Function_8_13C0")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1772")

    #C0024
    ChrTalk(
        0x101,
        (
            "#00006F#5Pくっ……\x01",
            "さすがに手強かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#00108F#6Pそれにやっぱり……\x01",
            "不思議な消え方をしたわね。\x02",
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

    def lambda_15CC():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15CC)
    Sleep(50)

    def lambda_15DC():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15DC)
    Sleep(50)

    def lambda_15EC():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_15EC)
    Sleep(50)

    def lambda_15FC():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15FC)
    Sleep(50)

    def lambda_160C():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_160C)
    Sleep(50)

    def lambda_161C():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_161C)
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
            "#10108F#12Pティオちゃん。\x01",
            "“場の歪み”の方は？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00206F#6P……駄目です。\x01",
            "上位三属性が働いたままです。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F#11Pったく……\x01",
            "いったい何が原因なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x105,
        (
            "#10303F#5Pどうやら《幻獣》そのものが\x01",
            "原因じゃなさそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00013F#11P……やっぱりもう一方も\x01",
            "当たってみる必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8C")

    label("loc_1772")


    #C0031
    ChrTalk(
        0x105,
        (
            "#10306F#5Pやれやれ……\x01",
            "こっちの方も手強かったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#10101F#6Pでも、消え方は同じ……\x02",
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

    def lambda_1816():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1816)
    Sleep(50)

    def lambda_1826():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1826)
    Sleep(50)

    def lambda_1836():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1836)
    Sleep(50)

    def lambda_1846():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1846)
    Sleep(50)

    def lambda_1856():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1856)
    Sleep(50)

    def lambda_1866():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1866)
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
            "#00301F#11Pやっぱり“場の歪み”ってのは\x01",
            "続いたままかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#00203F#6Pそうですね……\x02\x03",

            "#00201Fただ、何か具体的な原因が\x01",
            "ありそうな気はします。\x02",
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
            "#00005F#11P具体的な原因……\x01",
            "たとえばどんな？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#00206F#6P……その……\x01",
            "先ほどからわたしの感覚が\x01",
            "“歪み”に撹乱されていて……\x02\x03",

            "#00200Fむしろ、皆さんの方が原因を\x01",
            "見つけられるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#00105F#5Pそ、そう？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00003F#11Pよし……\x01",
            "この付近を捜索してみよう。\x02\x03",

            "#00000F“場の歪み”をもたらしているものが\x01",
            "必ずあるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1ACB():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1ACB)
    Sleep(50)

    def lambda_1ADB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1ADB)
    Sleep(50)

    def lambda_1AEB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1AEB)
    Sleep(50)

    def lambda_1AFB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1AFB)
    Sleep(50)

    def lambda_1B0B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B0B)
    Sleep(50)

    def lambda_1B1B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1B1B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0039
    ChrTalk(
        0x109,
        "#10100F#6P了解しました！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        "#00300F#12P手当たり次第、探してみっか！\x02",
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_1B8C")

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
            "ウルスラ間道方面の幻獣を倒した！\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1C")
    OP_1B(0x0, 0x0, 0x3)

    label("loc_1C1C")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_8_13C0 end

    def Function_9_1C2C(): pass

    label("Function_9_1C2C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2015")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0042
    AnonymousTalk(
        0x101,
        "#00005Fこの花は……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 4)), scpexpr(EXPR_END)), "loc_1E3F")

    #A0043
    AnonymousTalk(
        0x102,
        (
            "#00108F確か、東クロスベル街道方面の\x01",
            "沼地でも咲いていたような……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0044
    AnonymousTalk(
        0x104,
        "#00305Fああ、そういや見かけたな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1EE7")

    label("loc_1E3F")


    #A0045
    AnonymousTalk(
        0x105,
        (
            "#10302F確か、東クロスベル街道方面の\x01",
            "沼地でも咲いていなかったっけ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0046
    AnonymousTalk(
        0x101,
        "#00011Fそ、そうだったか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0047
    AnonymousTalk(
        0x102,
        (
            "#00108Fええ、確かに私も\x01",
            "見たような気がするけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1EE7")


    #A0048
    AnonymousTalk(
        0x109,
        (
            "#10109Fすごく綺麗な花ですね……\x02\x03",

            "#10102F……見たことがありませんけど\x01",
            "なんていう名前なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0049
    AnonymousTalk(
        0x101,
        "#00001Fうーん……\x02",
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
            "#00003F#11P（……まさかとは思うけど……）\x02\x03",

            "#00001F（いや、試す価値はあるか？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x160, 5)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_20CB")

    label("loc_2015")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0051
    AnonymousTalk(
        0x101,
        (
            "#00003F#11P（……まさかとは思うけど……）\x02\x03",

            "#00001F（いや、試す価値はあるか？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_20CB")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "蒼い花を摘んでみる\x01",      # 0
            "止めておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2123"),
        (1, "loc_2EC7"),
        (SWITCH_DEFAULT, "loc_2F05"),
    )


    label("loc_2123")

    OP_9B(0x0, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0052
    ChrTalk(
        0x102,
        "#00105Fロイド……？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x105,
        (
            "#10305F#6Pなに、その花を\x01",
            "摘んでいくつもりかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00003F#11Pああ……\x01",
            "ちょっと可哀想だけど──\x02",
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
        "#00301F#5Pな、なんだ！？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        "#00205F#12Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00001F#11Pくっ……！\x02",
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
        "#10111F#5Pい、今のは……\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        "#00108F何か空間が揺らいだような……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    #C0061
    ChrTalk(
        0x105,
        (
            "#10308F#6P……ティオ。\x01",
            "“場の歪み”の方は？\x02",
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
            "#00203F#12P……上位三属性の\x01",
            "気配が消滅しました。\x02\x03",

            "#00201F既にこの一帯に\x01",
            "異常は感じられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00006F#11Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00305F#5Pちょ、ちょっと待て。\x02\x03",

            "#00307Fまさかその蒼い花が\x01",
            "異常を引き起こしてたのかよ！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0065
    ChrTalk(
        0x105,
        (
            "#10304F#6Pまあ、そういう事だろうね。\x02\x03",

            "#10300F……そのちっぽけな花程度に\x01",
            "そんな力があるとも思えないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#00101Fし、信じられない……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x109,
        (
            "#10101F#5Pい、いったい\x01",
            "どういう花なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#00206F#12P……もう、その花からは\x01",
            "おかしな気配は感じませんが……\x02\x03",

            "#00200Fとりあえずどこかで\x01",
            "調べてもらった方がいいのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00008F#11Pそうだな……\x02\x03",

            "#00003F……医科大学あたりも\x01",
            "ちょっと専門が違うだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00100Fと、とにかく失くさないよう\x01",
            "保管しておきましょう。\x02\x03",

            "心当たりが見つかったら\x01",
            "調べてもらえばいいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00006F#11Pああ、そうするか。\x02",
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
        "#10303F#6P……ふむ………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_28A9():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28A9)
    Sleep(50)

    def lambda_28B9():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_28B9)
    Sleep(50)

    def lambda_28C9():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_28C9)
    Sleep(50)

    def lambda_28D9():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_28D9)
    Sleep(50)

    def lambda_28E9():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28E9)
    Sleep(50)

    def lambda_28F9():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_28F9)
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
        "#00005F#11Pワジ……？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        "#10101F#5P何か心当たりでもあるの？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x105,
        (
            "#10303F#6Pいや……\x01",
            "僕のウロ覚えかもしれないけど。\x02\x03",

            "#10301F教会の聖典に、不思議な蒼い花の\x01",
            "言い伝えがあった気がする。\x02",
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
        "#00011F#11Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        "#00305F#5Pおいおい、マジかよ！？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x105,
        (
            "#10306F#6Pいや、大分前に流し読みした時に\x01",
            "見かけた気がするんだけど……\x02\x03",

            "#10300Fエリィとか心当たりはないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#00112F#11P私もさすがに聖典の全てに\x01",
            "目は通していないけど……\x02\x03",

            "#00103F……でも、確かに\x01",
            "そんな下りを読んだ気がするわ。\x02\x03",

            "#00108F不思議な力を持っているという\x01",
            "『蒼き花』の言い伝えを……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0080
    ChrTalk(
        0x109,
        (
            "#10111F#6Pそ、それって……\x01",
            "ビンゴなんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0081
    ChrTalk(
        0x103,
        (
            "#00201F#12P少なくとも教会関係者に\x01",
            "確認する価値はありそうです。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C5A():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C5A)
    Sleep(50)

    def lambda_2C6A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2C6A)
    Sleep(50)

    def lambda_2C7A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2C7A)
    Sleep(50)

    def lambda_2C8A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2C8A)
    Sleep(50)

    def lambda_2C9A():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C9A)
    Sleep(50)

    def lambda_2CAA():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2CAA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D68")

    #C0082
    ChrTalk(
        0x101,
        (
            "#00003F#11P……そうだな。\x02\x03",

            "#00000Fマーブル先生かリースさんの\x01",
            "どちらかに相談してみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#00104Fそうね……\x01",
            "どちらも適任だと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E17")

    label("loc_2D68")


    #C0084
    ChrTalk(
        0x101,
        (
            "#00003F#11P……そうだな。\x02\x03",

            "#00000Fやっぱりマーブル先生が\x01",
            "一番相談しやすいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#00104Fええ、適任だと思うわ。\x02\x03",

            "#00108F（“彼女”にも相談できそうだけど……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E17")


    #C0086
    ChrTalk(
        0x104,
        (
            "#00300F#5Pおーし、そんじゃあ\x01",
            "クロスベル大聖堂に向かうか！\x02",
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
    Jump("loc_2F05")

    label("loc_2EC7")

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
    Jump("loc_2F05")

    label("loc_2F05")

    Return()

    # Function_9_1C2C end

    def Function_10_2F06(): pass

    label("Function_10_2F06")

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
            "#10100Fそ、そういえば……\x02\x03",

            "こっちの花も\x01",
            "摘んだ方がいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0088
    AnonymousTalk(
        0x101,
        (
            "#00000Fいや……\x01",
            "こちらの方は様子を見よう。\x02\x03",

            "ひょっとしたら貴重な\x01",
            "サンプルになるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0089
    AnonymousTalk(
        0x103,
        (
            "#00200F……確かに。\x01",
            "摘んだら力を失うみたいですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0090
    AnonymousTalk(
        0x102,
        (
            "#00100Fでも……また幻獣が現れたら\x01",
            "摘むしかないかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0091
    AnonymousTalk(
        0x104,
        "#00300Fま、そん時はそん時だ。\x02",
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

    # Function_10_2F06 end

    def Function_11_31F7(): pass

    label("Function_11_31F7")

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

    def lambda_34F8():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34F8)
    Sleep(50)

    def lambda_3510():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3510)
    Sleep(50)

    def lambda_3528():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3528)
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

    def lambda_3598():
        OP_96(0xFE, 0x927C, 0x7A120, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3598)

    def lambda_35B2():
        OP_96(0xFE, 0x927C, 0x7A120, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35B2)
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
        "#00001Fいったん上空に戻るのか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0093
    AnonymousTalk(
        0x105,
        (
            "#10403Fああ、地上に留まったままだと\x01",
            "感知される危険があるからね。\x02\x03",

            "#10400Fさてと──\x02",
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
            "#10403F#5P#40W──空の女神の名において\x01",
            "聖別されし七耀#4Rしちよう#ここに在り。\x07\x00\x02",
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
            "#00005F#5Pあ……\x01",
            "（マーブル先生と同じ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x107,
        "#01200F#6P#3Cふむ、星杯の法術か。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#5P#40W大地の琥耀#4Rこよう#、空の金耀#4Rきんよう#──\x02\x03",

            "#10401Fその融合をもって\x01",
            "巨#2Rおお#いなる“目”より逃れる\x01",
            "小さき聖域を改めて成せ。\x02",
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
        "#00001Fこれは……\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)

    #C0099
    ChrTalk(
        0x105,
        (
            "#10404F#11P力場の“隙間”を\x01",
            "固定してくれる“法陣”さ。\x02\x03",

            "僕ら以外には見えない\x01",
            "おまじないも掛かっていてね。\x02\x03",

            "#10402Fまあ、しばらくの間なら\x01",
            "何とか持ってくれるだろう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AAC():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3AAC)
    Sleep(50)

    def lambda_3ABC():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3ABC)
    Sleep(50)

    def lambda_3ACC():
        TurnDirection(0x107, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3ACC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)

    #C0100
    ChrTalk(
        0x101,
        (
            "#00012F#5Pな、なるほど。\x02\x03",

            "#00002Fしかしワジ……\x01",
            "本当に教会の関係者なんだな。\x02\x03",

            "今までの言動を見てると\x01",
            "いまいち実感が無かったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#10404F#11Pフフ、お堅いのが\x01",
            "趣味じゃないってのは\x01",
            "別に変わっちゃいないからね。\x02\x03",

            "#10400F──それで、どうする？\x02\x03",

            "やっぱりウルスラ病院あたりに\x01",
            "行ってみるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00003F#5Pああ、様子を見に行こう。\x02\x03",

            "#00008Fそれと……\x01",
            "余裕があればクロスベル市の\x01",
            "方向も見ておきたいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3Cふむ、それもよかろう。\x02\x03",

            "#01201Fただしプレロマ草のせいで\x01",
            "街道に幻獣が出現している状況だ。\x02\x03",

            "くれぐれも気を付けるがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xD7, 0x1F4)

    #C0104
    ChrTalk(
        0x101,
        "#00013F#5Pああ、分かった。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x105,
        "#10400F#11Pそれじゃあ行こうか。\x02",
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

    # Function_11_31F7 end

    def Function_12_3DF4(): pass

    label("Function_12_3DF4")

    OP_96(0xFE, 0x927C, 0x1D4C, 0xFFFFD508, 0x9C4, 0x1)
    OP_96(0xFE, 0x927C, 0x1B58, 0xFFFFD508, 0x7D0, 0x1)
    OP_96(0xFE, 0x927C, 0x1964, 0xFFFFD508, 0x5DC, 0x1)
    OP_96(0xFE, 0x927C, 0x1770, 0xFFFFD508, 0x3E8, 0x1)
    OP_96(0xFE, 0x927C, 0x157C, 0xFFFFD508, 0x1F4, 0x1)
    BeginChrThread(0xFE, 3, 0, 13)
    Return()

    # Function_12_3DF4 end

    def Function_13_3E5F(): pass

    label("Function_13_3E5F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EED")
    OP_96(0xFE, 0x927C, 0x14B4, 0xFFFFD508, 0x190, 0x1)
    OP_96(0xFE, 0x927C, 0x1450, 0xFFFFD508, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0x927C, 0x14B4, 0xFFFFD508, 0xC8, 0x1)
    OP_96(0xFE, 0x927C, 0x1644, 0xFFFFD508, 0x190, 0x1)
    OP_96(0xFE, 0x927C, 0x16A8, 0xFFFFD508, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0x927C, 0x1644, 0xFFFFD508, 0xC8, 0x1)
    Jump("Function_13_3E5F")

    label("loc_3EED")

    Return()

    # Function_13_3E5F end

    def Function_14_3EEE(): pass

    label("Function_14_3EEE")

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

    # Function_14_3EEE end

    def Function_15_3F3F(): pass

    label("Function_15_3F3F")

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

    # Function_15_3F3F end

    def Function_16_3F8D(): pass

    label("Function_16_3F8D")

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

    # Function_16_3F8D end

    def Function_17_3FF2(): pass

    label("Function_17_3FF2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_400C")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_17_3FF2")

    label("loc_400C")

    Return()

    # Function_17_3FF2 end

    def Function_18_400D(): pass

    label("Function_18_400D")

    SetMapObjFrame(0x6, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0x6, "Null_fream", 0x2, "loop")
    Return()

    # Function_18_400D end

    SaveToFile()

Try(main)
