from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t6050.bin",                # FileName
        "t6050",                    # MapName
        "t6050",                    # Location
        0x00CA,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x25,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 202, 0, 0, 0, 1],
    )

    BuildStringList((
        "t6050",                  # 0
        "国防军士兵",             # 1
        "国防军士兵",             # 2
        "国防军士兵",             # 3
        "国防军士兵",             # 4
        "诺艾尔少尉",             # 5
        "加尔西亚",               # 6
        "看守梅尔文",             # 7
        "SE控制",                 # 8
        "BT6010",                 # 9
    ))

    ATBonus("ATBonus_334", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_414", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_400", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_404", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_408", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_40C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_434", 0x004A, 3, 6, 45, 3, 3, 30, 0, "BT6010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41400.dat", "ms41500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_3F4", "ed7540", "ed7453", "ATBonus_334"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51611.itc",                   # 00
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

    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 27,  30.0,                  -1.0,                  -1.0,                  144.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -10.0,                 0.125,                 0.20000001788139343,   1.0])

    DeclActor(83000,   0,       38500,   1200,    83000,   1000,    38500,   0x007C, 0,  2,  0x0000)
    DeclActor(42500,   0,       41000,   1200,    42500,   1000,    41000,   0x007C, 0,  3,  0x0000)
    DeclActor(80000,   0,       -17500,  1200,    80000,   1000,    -17500,  0x007C, 0,  4,  0x0000)
    DeclActor(1000,    0,       -4500,   1200,    1000,    1200,    -4000,   0x007C, 0,  8,  0x0000)
    DeclActor(13000,   0,       2500,    1200,    13000,   1200,    1750,    0x007C, 0,  10, 0x0000)
    DeclActor(-2520,   0,       38190,   1200,    -2520,   1000,    38190,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1308, 0)                                       # 0

    ScpFunction((
        "Function_0_51C",          # 00, 0
        "Function_1_540",          # 01, 1
        "Function_2_6D1",          # 02, 2
        "Function_3_7AB",          # 03, 3
        "Function_4_883",          # 04, 4
        "Function_5_95B",          # 05, 5
        "Function_6_9FA",          # 06, 6
        "Function_7_B06",          # 07, 7
        "Function_8_B83",          # 08, 8
        "Function_9_D2F",          # 09, 9
        "Function_10_E4F",         # 0A, 10
        "Function_11_FEC",         # 0B, 11
        "Function_12_4161",        # 0C, 12
        "Function_13_418E",        # 0D, 13
        "Function_14_41B5",        # 0E, 14
        "Function_15_41E9",        # 0F, 15
        "Function_16_4223",        # 10, 16
        "Function_17_4265",        # 11, 17
        "Function_18_42AB",        # 12, 18
        "Function_19_42E7",        # 13, 19
        "Function_20_4323",        # 14, 20
        "Function_21_452A",        # 15, 21
        "Function_22_47A1",        # 16, 22
        "Function_23_47C4",        # 17, 23
        "Function_24_482B",        # 18, 24
        "Function_25_4860",        # 19, 25
        "Function_26_489E",        # 1A, 26
        "Function_27_48DC",        # 1B, 27
        "Function_28_4C82",        # 1C, 28
        "Function_29_4CCE",        # 1D, 29
        "Function_30_4D4B",        # 1E, 30
        "Function_31_50FC",        # 1F, 31
        "Function_32_5163",        # 20, 32
        "Function_33_5DF7",        # 21, 33
        "Function_34_5E96",        # 22, 34
        "Function_35_5EEF",        # 23, 35
        "Function_36_5F48",        # 24, 36
        "Function_37_5FA1",        # 25, 37
        "Function_38_5FFA",        # 26, 38
        "Function_39_6053",        # 27, 39
        "Function_40_60AC",        # 28, 40
    ))


    def Function_0_51C(): pass

    label("Function_0_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_530")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)
    Jump("loc_53F")

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_53F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 32)

    label("loc_53F")

    Return()

    # Function_0_51C end

    def Function_1_540(): pass

    label("Function_1_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56E")

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_56E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59F")
    OP_52(0x10B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59F")

    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_618")
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0xFF, "red00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red02", 0x0, 0x1)
    Jump("loc_64B")

    label("loc_618")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "green00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "green01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "green02", 0x0, 0x1)

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65E")
    OP_70(0xB, 0x0)
    Jump("loc_662")

    label("loc_65E")

    OP_70(0xB, 0x1E)

    label("loc_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_675")
    OP_70(0xC, 0x0)
    Jump("loc_679")

    label("loc_675")

    OP_70(0xC, 0x1E)

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C")
    OP_70(0xD, 0x0)
    Jump("loc_690")

    label("loc_68C")

    OP_70(0xD, 0x1E)

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A1")
    Call(0, 23)

    label("loc_6A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B2")
    Call(0, 31)

    label("loc_6B2")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D0")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_6D0")

    Return()

    # Function_1_540 end

    def Function_2_6D1(): pass

    label("Function_2_6D1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77C")
    Sound(14, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xB, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了１０个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('战斗探测器', 10)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_799")

    label("loc_77C")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_799")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6D1 end

    def Function_3_7AB(): pass

    label("Function_3_7AB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_854")
    Sound(14, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xC, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了５个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('圣灵药', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_871")

    label("loc_854")


    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_871")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7AB end

    def Function_4_883(): pass

    label("Function_4_883")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0xD, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了２个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('土人偶', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_949")

    label("loc_92C")


    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_949")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_883 end

    def Function_5_95B(): pass

    label("Function_5_95B")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DC")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_9DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_9F8")

    Return()

    # Function_5_95B end

    def Function_6_9FA(): pass

    label("Function_6_9FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADF")

    #C0007
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00001F……他们完全晕过去了啊。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x10B,
        (
            "#11102F哼哼，说得好像事不关己一样。\x01",
            "把他们打晕的人不就是我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00003F……我知道。\x02\x03",

            "#00001F虽然有点对不起他们，\x01",
            "但我们这就走吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B02")

    label("loc_ADF")

    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "国防军士兵晕过去了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B02")

    TalkEnd(0xFE)
    Return()

    # Function_6_9FA end

    def Function_7_B06(): pass

    label("Function_7_B06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5C")

    #C0012
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "国防军士兵晕过去了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B7F")

    label("loc_B5C")

    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "国防军士兵晕过去了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B7F")

    TalkEnd(0xFE)
    Return()

    # Function_7_B06 end

    def Function_8_B83(): pass

    label("Function_8_B83")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAE")
    SetChrName("声音")
    Jump("loc_BC0")

    label("loc_BAE")

    SetChrName("黑手党成员的声音")

    label("loc_BC0")


    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……你们刚才有没有听到一声巨响？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C14")
    SetChrName("声音")
    Jump("loc_C26")

    label("loc_C14")

    SetChrName("黑手党成员的声音")

    label("loc_C26")


    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "什么……？\x01",
            "你幻听了吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D1E")

    label("loc_C58")

    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C76")
    SetChrName("声音")
    Jump("loc_C88")

    label("loc_C76")

    SetChrName("黑手党成员的声音")

    label("loc_C88")


    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "这、这场骚动是怎么回事……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDA")
    SetChrName("声音")
    Jump("loc_CEC")

    label("loc_CDA")

    SetChrName("黑手党成员的声音")

    label("loc_CEC")


    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "喂喂，难道发生了什么事吗！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2B")
    Call(0, 9)

    label("loc_D2B")

    TalkEnd(0xFF)
    Return()

    # Function_8_B83 end

    def Function_9_D2F(): pass

    label("Function_9_D2F")


    #C0019
    ChrTalk(
        0x101,
        "#00005F（这个房间是……？）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10B,
        (
            "#11100F（这个牢房和斜对面的牢房里\x01",
            "  关押着我们\x01",
            "  那群部下。）\x02\x03",

            "#11103F（这个拘留所的人手严重不足，\x01",
            "  所以把麻烦的犯人全都关在了这一层，\x01",
            "  以便同时看守。）\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F（原来如此……）\x02\x03",

            "#00001F（……总之，动作快点吧，\x01",
            "  在增援赶来之前突破这里。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 0)
    Return()

    # Function_9_D2F end

    def Function_10_E4F(): pass

    label("Function_10_E4F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F24")
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7A")
    SetChrName("声音")
    Jump("loc_E8C")

    label("loc_E7A")

    SetChrName("黑手党成员的声音")

    label("loc_E8C")


    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "从副头目的牢房中\x01",
            "传出了好大的声音！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE3")
    SetChrName("声音")
    Jump("loc_EF5")

    label("loc_EE3")

    SetChrName("黑手党成员的声音")

    label("loc_EF5")


    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "您没事吧！？副头目！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_FDB")

    label("loc_F24")

    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F42")
    SetChrName("声音")
    Jump("loc_F54")

    label("loc_F42")

    SetChrName("黑手党成员的声音")

    label("loc_F54")


    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "响、响起了警报……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9E")
    SetChrName("声音")
    Jump("loc_FB0")

    label("loc_F9E")

    SetChrName("黑手党成员的声音")

    label("loc_FB0")


    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "副头目！\x01",
            "您没事吧！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE8")
    Call(0, 9)

    label("loc_FE8")

    TalkEnd(0xFF)
    Return()

    # Function_10_E4F end

    def Function_11_FEC(): pass

    label("Function_11_FEC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0xA, 0xFF, 0xFF)
    OP_52(0x10B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xA, 0x0, 0x52)
    OP_32(0xA, 0x5, 0x64)
    OP_42(0xA, 0x46F, 0xFF)
    AddCraft(0xA, 0xFA)
    AddCraft(0xA, 0xFB)
    AddCraft(0xA, 0xFC)
    AddCraft(0xA, 0xFD)
    AddCraft(0xA, 0x14A)
    SetChrChipPat(0xA, 0x6, 0x14A)
    OP_32(0xFF, 0xFF, 0x0)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("apl/ch51616.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x21)
    LoadChrToIndex("apl/ch51606.itc", 0x22)
    LoadChrToIndex("chr/ch41450.itc", 0x23)
    LoadChrToIndex("chr/ch41451.itc", 0x24)
    LoadChrToIndex("chr/ch41452.itc", 0x25)
    LoadChrToIndex("chr/ch41453.itc", 0x26)
    LoadChrToIndex("apl/ch51608.itc", 0x27)
    LoadChrToIndex("apl/ch51609.itc", 0x28)
    LoadChrToIndex("chr/ch04156.itc", 0x29)
    LoadChrToIndex("apl/ch51605.itc", 0x2A)
    SoundLoad(4119)
    SoundLoad(3630)
    SoundLoad(3631)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis270.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis271.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11100.itp")
    LoadEffect(0x0, "event/ev16000.eff")
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -42100, 150, 38000, 90)
    SetChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x22)
    SetChrSubChip(0x10B, 0x0)
    SetChrFlags(0x10B, 0x4)
    SetChrPos(0x10B, 2100, 150, 37500, 270)
    SetChrFlags(0x10B, 0x8)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -121100, 0, 36000, 0)
    SetChrFlags(0xC, 0x8)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5000, 0, -1000, 90)
    SetChrFlags(0x8, 0x40)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 33000, 0, -400, 270)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_120C")
    Jump("loc_3154")

    label("loc_120C")

    BeginChrThread(0xF, 1, 0, 24)
    Sleep(3000)
    OP_68(27000, 1600, 0, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(3000, 1600, 0, 10000)
    MoveCamera(60, 12, 0, 10000)
    OP_6E(400, 10000)
    SetCameraDistance(33000, 10000)

    def lambda_127F():
        OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_127F)
    PlaceName2(340, 200, "c_plac70", 0x0, 3000)
    Sleep(9000)
    OP_0D()
    EndChrThread(0xF, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-42100, 3000, 38000, 0)
    MoveCamera(270, 36, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14650, 0)
    FadeToBright(1000, 0)
    OP_68(-42100, 1000, 38000, 5000)
    MoveCamera(270, 27, 0, 5000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_A1(0x101, 0x3E8, 0x2, 0x1, 0x2)
    Sleep(150)

    #C0026
    ChrTalk(
        0x101,
        "#00015F#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(14400, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, -122100, 150, 38000, 90)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x2)
    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x9, 0x10)
    OP_70(0x9, 0xA)
    OP_7D(0xCF, 0xAE, 0x5D, 0x0, 0x0)
    OP_68(-121550, 1600, 37000, 0)
    MoveCamera(230, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    PlayBGM("ed7534", 0)
    VolumeBGM(0x46, 0x64)
    FadeToBright(2500, 0)
    SetCameraDistance(20720, 2500)
    OP_6F(0x79)
    MoveCamera(226, 24, 0, 50000)
    OP_0D()
    Sleep(500)

    #C0027
    ChrTalk(
        0xC,
        (
            "#10203F#5P支援科的其他成员都在\x01",
            "别的地方接受保护。\x02\x03",

            "#10208F很抱歉，要把罗伊德警官\x01",
            "单独拘留在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00006F#11P……我的事情就不用说了。\x02\x03",

            "#00008F但『保护』这种说法\x01",
            "未免太奇怪了吧？\x02\x03",

            "#00002F你们到底……\x01",
            "要在什么势力的威胁下保护我们？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        "#10206F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00003F#11P……我想你应该\x01",
            "也已经察觉到了吧。\x02\x03",

            "#00008F究竟谁才是策动那起袭击\x01",
            "克洛斯贝尔市事件的幕后黑手。\x02\x03",

            "#00013F究竟是谁伤害了\x01",
            "你的妹妹──芙兰……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0031
    ChrTalk(
        0xC,
        "#10215F#5P#4S但是……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0032
    ChrTalk(
        0xC,
        (
            "#10207F#5P……即使如此，\x01",
            "我也依然是警备队的一员！\x02\x03",

            "既然警备队已改组为『国防军』，\x01",
            "我身为一名军人，就必须要履行自己的职责！\x02\x03",

            "#10208F否则的话，克洛斯贝尔……\x02\x03",

            "#10206F……克洛斯贝尔真的会被\x01",
            "帝国和共和国毁灭！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00005F#11P诺艾尔……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xC,
        (
            "#10206F#5P当然……\x01",
            "我并不认为琪雅应该继续遭受那种对待。\x02\x03",

            "也不赞同借助『结社』那群\x01",
            "来历不明的家伙的力量……！\x02\x03",

            "#10210F但是……帝国军真的用那种\x01",
            "恐怖至极的列车炮攻击我们了啊！\x02\x03",

            "他们动用了那种一旦命中，\x01",
            "就会造成数百人死伤的大规模破坏性武器！\x02\x03",

            "#10215F……所以……\x01",
            "所以已经没有其它办法了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#00008F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xC,
        (
            "#10206F#5P对不起……\x02\x03",

            "……我并没有资格对\x01",
            "罗伊德警官说这种话。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(400)

    #C0037
    ChrTalk(
        0xC,
        (
            "#10208F#11P你的拘留时间\x01",
            "应该不会太长。\x02\x03",

            "等克洛斯贝尔渡过这场危机之后，\x01",
            "一定会马上释放你的……\x02\x03",

            "#10203F所以……\x01",
            "暂时就请忍耐一阵子吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(21220, 3000)
    BeginChrThread(0xC, 3, 0, 12)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x3)
    SetChrFlags(0xC, 0x80)
    SetMapObjFlags(0x9, 0x10)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -42100, 150, 38000, 90)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    OP_68(-42100, 1000, 38000, 0)
    MoveCamera(270, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14400, 0)
    VolumeBGM(0x64, 0xBB8)
    FadeToBright(2000, 0)
    SetCameraDistance(14650, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_A1(0x101, 0x3E8, 0x2, 0xD, 0xE)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W（……那个时候……\x01",
            "  我根本无法反驳她。）\x02\x03",

            "#00008F（而且……\x01",
            "  我完全没有察觉到\x01",
            "  琪雅的苦恼……）\x02\x03",

            "（被忙碌的工作蒙蔽了双眼……\x01",
            "  连最该保护的人都没能保护好……）\x02\x03",

            "#00006F（……琪雅的来历，\x01",
            "  还有杀害大哥的犯人……）\x02\x03",

            "#00015F（我当初明明在心中发过誓，\x01",
            "  决心将这一切调查清楚的……！）\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(250, 20, -1, -1)
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W那么，杀害盖伊·班宁斯……\x01",
            "杀害我大哥的人也是你吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(110, 65, -1, -1)
    OP_C9(0x0, 0x80000000)

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4119V#30W嗯，正是。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0x1017)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(85, 110, -1, -1)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3630V#30W对不起。\x01",
            "……谢谢大家至今为止对我的照顾。\x02\x03",

            "#3631V我……最喜欢你们了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE2F)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x7D0)
    Sleep(500)
    OP_A1(0x101, 0x514, 0x4, 0x4, 0x5, 0x6, 0x7)

    #C0042
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W（大哥……对不起……）\x02\x03",

            "（我果然还是……\x01",
            "  完全追不上\x01",
            "  大哥的脚步……）\x02\x03",

            "#00015F（我甚至……\x01",
            "  甚至已经完全不知道……）\x02\x03",

            "（……今后该怎么办了…………）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2854, 255, 100, 0)    #voice#Garcia
    Sleep(500)

    #N0043
    NpcTalk(
        0x10B,
        "豪气的声音",
        "#5P真难看啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-1500, 1300, 38000, 0)
    OP_68(0, 1300, 38000, 2500)
    MoveCamera(49, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -2100, 150, 38000, 90)
    SetChrSubChip(0x101, 0x8)
    ClearChrFlags(0x10B, 0x8)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0044
    AnonymousTalk(
        0x10B,
        (
            "身为把我们逼得走投无路的队长，\x01",
            "如今却是一副如此落魄的狼狈样……\x02\x03",

            "我居然会因为你这种人\x01",
            "而吃了半年多的牢饭，\x01",
            "实在是太荒谬了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_A1(0x101, 0x3E8, 0x2, 0x9, 0xA)
    Sleep(150)

    #C0045
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W……不用你管。\x02\x03",

            "你会待在这种地方，\x01",
            "完全是自作自受……\x02\x03",

            "我们能成功逮捕你们，\x01",
            "也不过是因为运气好罢了……\x02\x03",

            "#00008F没错……我们并不是凭借\x01",
            "自己的实力而跨越『壁障』的……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x10B,
        "#11101F#11P哼，真是个麻烦的小鬼。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10B)
    Sleep(500)

    #C0047
    ChrTalk(
        0x10B,
        (
            "#11104F#11P不过，倒也情有可原。\x02\x03",

            "据我所知，现在的局势\x01",
            "好像相当麻烦。\x02\x03",

            "#11101FＩＢＣ的总裁就是一系列事件的幕后黑手，\x01",
            "而且他现在已经就任为独裁国家的总统……\x02\x03",

            "赤色星座、结社、\x01",
            "国防军，再加上风之剑圣，\x01",
            "全都成为你们的敌人了。\x02\x03",

            "#11102F哼哼，这可比抽到一副\x01",
            "同花顺还要惊人啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00006F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(2852, 255, 100, 0)    #voice#Garcia
    Sleep(500)
    OP_68(570, 1300, 37950, 1500)
    MoveCamera(51, 20, 0, 1500)
    Sound(898, 0, 100, 0)
    Sound(811, 0, 20, 0)
    OP_A1(0x10B, 0x4B0, 0x4, 0x1, 0x2, 0x3, 0x4)
    OP_6F(0x79)

    #C0049
    ChrTalk(
        0x10B,
        (
            "#11104F#5P总之，老老实实地待在这里，\x01",
            "静待这场风波过去才是正确的选择。\x02\x03",

            "只有彻头彻尾的大笨蛋才会\x01",
            "在这种状况下选择反抗。\x02\x03",

            "#11100F就像你的大哥一样。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x12C, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_A1(0x101, 0x3E8, 0x2, 0xB, 0xC)

    #C0050
    ChrTalk(
        0x101,
        (
            "#00011F#6P#30W………啊…………\x02\x03",

            "#00001F#20W这么说，你认识\x01",
            "我大哥……？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(22000, 20000)

    #C0051
    ChrTalk(
        0x10B,
        (
            "#11100F#5P哼，可不只是\x01",
            "『认识』这么简单。\x02\x03",

            "#11103F不管我威胁他多少次，\x01",
            "他都不长教训，继续四处调查……\x02\x03",

            "……可是，\x01",
            "当我们在街边酒摊偶然碰上时，\x01",
            "他又会满不在乎地邀我一起喝酒……\x02\x03",

            "#11101F真是个既麻烦又让人讨厌的小子。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00004F#6P#30W哈哈……大哥就是那样的人。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A1(0x10B, 0x3E8, 0x2, 0x5, 0x6)
    Sleep(300)

    #C0053
    ChrTalk(
        0x10B,
        (
            "#11103F#5P……真是的，他看起来\x01",
            "完全不像是会被轻易杀掉的家伙，\x01",
            "结果却一下子死掉了。\x02\x03",

            "真是世事难料啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W……………………………………\x02\x03",

            "#00001F……大哥他……\x01",
            "一直都在抗争吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x10B,
        (
            "#11104F#5P嗯，除了我们鲁巴彻之外，\x01",
            "他还调查过不少事情。\x02\x03",

            "从重要议员的贪污渎职，\x01",
            "到帝国和共和国的谍报行动，\x01",
            "乃至约亚西姆那家伙的动向……\x02\x03",

            "#11100F他的精力真是旺盛到了\x01",
            "让人瞠目结舌的程度。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#00006F#6P#30W……这样啊………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sound(898, 0, 100, 0)
    Sound(802, 0, 50, 0)
    OP_A1(0x10B, 0x4B0, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0)
    Sleep(150)

    #C0057
    ChrTalk(
        0x10B,
        (
            "#11103F#11P喂，\x01",
            "你可别搞错我的意思。\x02\x03",

            "#11101F其实盖伊·班宁斯并不是什么\x01",
            "了不起的男人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x101,
        "#00005F#6P哎……？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x10B,
        (
            "#11104F#11P要论战斗力和震慑力，\x01",
            "他应该不及马克莱因。\x02\x03",

            "说起见缝插针的能力和外交疏通能力，\x01",
            "赛尔盖显然在他之上。\x02\x03",

            "#11100F至于判断力与处理能力，\x01",
            "还是一科的达德利更胜一筹……\x02\x03",

            "总之，他的能力不过如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00011F#6P……这………\x02\x03",

            "#00008F（……仔细想想，\x01",
            "  他说的好像没错。）\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x10B,
        (
            "#11103F#11P要说他还有什么\x01",
            "胜过别人的长处……\x02\x03",

            "#11101F恐怕也就是那种\x01",
            "『永不放弃』的信念了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x101,
        "#00005F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x10B,
        (
            "#11100F#11P正因为拥有那种信念，\x01",
            "他才能产生惊人的行动力……\x02\x03",

            "这也是他在面对那些大人物时\x01",
            "可以永不放弃的原动力吧。\x02\x03",

            "#11103F话说回来，那小子从不顾虑周围的环境，\x01",
            "也完全不在乎场合和气氛……\x02\x03",

            "#11101F……我当时还在想，\x01",
            "这小子到底是怎么回事。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00008F#6P………………………………\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis000.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis008.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis088.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    CreatePortrait(5, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis020.itp")
    CreatePortrait(6, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07800.itp")
    FadeToDark(1000, 0, -1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(300)
    OP_CB(0x5, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x5, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x5, 0x3)
    OP_CB(0x6, 0x3, 0x99FFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(45, 100, -1, -1)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W听好了，罗伊德。\x02\x03",

            "身为男子汉，面对眼前的任何事物，\x01",
            "都要勇往直前地撞上去试试。\x02\x03",

            "要用你自己的心，去抓住\x01",
            "只属于你的真相。\x02\x03",

            "这样的话，你应该\x01",
            "就能找到自己的目标了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToBright(1000, 0)
    OP_CB(0x6, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x6, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x101, 0x12C, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0066
    ChrTalk(
        0x101,
        (
            "#00006F#6P……大哥那种『永不放弃』的精神，\x01",
            "应该是为了守护重要的人才形成的。\x02\x03",

            "#00008F他想守护的不只是自己的家人，\x01",
            "而是克洛斯贝尔这座城市……\x02\x03",

            "#00000F……从这层意义上来说，\x01",
            "也许连你们鲁巴彻都是\x01",
            "他想要守护的对象呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x10B,
        "#11105F#11P什么……？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈，使用守护这种说法，\x01",
            "听起来或许有些狂妄吧……\x02\x03",

            "#00008F大哥之所以拼尽全力，\x01",
            "恐怕是为了查明那股使克洛斯贝尔\x01",
            "陷入如今这种局面的暗流。\x02\x03",

            "#00004F在此基础上，他想以自己的方式\x01",
            "来守护克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x10B,
        (
            "#11103F#11P那家伙……\x02\x03",

            "#11110F……真是个比笨蛋\x01",
            "还笨的超级大笨蛋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00003F#6P是啊……\x02\x03",

            "#00008F……我终究无法成为\x01",
            "像他那样的笨蛋……\x02\x03",

            "#00000F但我们毕竟是兄弟，\x01",
            "还是有一些相似之处的。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x10B,
        "#11105F#11P什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrPos(0x101, -1600, 0, 38000, 90)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(900)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(500)
    OP_68(1500, 1100, 34500, 4000)
    MoveCamera(60, 18, 0, 4000)
    SetCameraDistance(24650, 4000)

    def lambda_2F19():
        OP_96(0xFE, 0x0, 0x0, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F19)
    Sleep(500)
    SetChrSubChip(0x10B, 0x7)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_6F(0x79)

    #C0072
    ChrTalk(
        0x10B,
        (
            "#11101F#5P你这小子……\x02\x03",

            "难道想逃出这里吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(150)

    #C0073
    ChrTalk(
        0x101,
        (
            "#00003F#12P并不是逃，我只是想\x01",
            "看清事实真相。\x02\x03",

            "#00001F身为克洛斯贝尔的警察，\x01",
            "身为特别任务支援科的搜查官……\x02\x03",

            "我必须要解救被囚禁的同伴，\x01",
            "并把琪雅夺回。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10B)

    #C0074
    ChrTalk(
        0x10B,
        (
            "#11104F#5P哼哼……哈哈……\x02\x03",

            "#11102F你也是个十足的\x01",
            "大笨蛋了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrPos(0x10B, 1200, 0, 37500, 270)
    ClearChrFlags(0x10B, 0x4)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    ClearChrFlags(0x10B, 0x2)
    OP_0D()
    Sleep(300)
    OP_93(0x10B, 0xB4, 0x1F4)

    #C0075
    ChrTalk(
        0x101,
        "#00005F#12P加尔西亚……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x10B,
        (
            "#11103F#5P那就让我见识一下吧，小鬼。\x02\x03",

            "让我看看你在这种\x01",
            "状况下还能做些什么……\x02\x03",

            "#11102F拿出全部觉悟吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(25650, 2000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()

    label("loc_3154")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3164")
    Jump("loc_373A")

    label("loc_3164")

    Sleep(1000)
    OP_68(28000, 1100, -1000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x8, 33000, 0, -1600, 270)
    ClearChrFlags(0x9, 0x8)

    def lambda_31B0():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31B0)
    Sleep(50)

    def lambda_31C8():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_31C8)
    FadeToBright(1000, 0)
    SetCameraDistance(25500, 2500)
    Sleep(2000)
    Sound(886, 0, 30, 0)
    Sleep(700)
    Sound(815, 0, 40, 0)
    Sleep(100)
    Sound(811, 0, 50, 0)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    #C0077
    ChrTalk(
        0x8,
        "#11P什么……？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        "#5P好像是从里面传出来的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7561", 0)
    BeginChrThread(0xF, 1, 0, 25)
    Fade(500)
    OP_68(2000, 1100, 1000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_68(1000, 1100, 1000, 2000)
    SetChrPos(0x8, 7000, 0, -1600, 270)
    SetChrPos(0x9, 7000, 0, -400, 270)

    def lambda_32BA():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_32BA)
    Sleep(50)

    def lambda_32D2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32D2)
    WaitChrThread(0x8, 1)

    def lambda_32EB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_32EB)
    WaitChrThread(0x9, 1)

    def lambda_32FC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32FC)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()
    SetChrPos(0x101, 1000, 0, 2000, 180)
    SetChrPos(0x10B, 1000, 0, 2000, 180)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x10B, 0x8)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #N0079
    NpcTalk(
        0x10B,
        "加尔西亚的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3S#11P混账东西！\x01",
            "你就只有这点实力吗！？死小鬼！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #N0080
    NpcTalk(
        0x101,
        "罗伊德的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#1S#11P#50W呜……咳咳……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x8,
        (
            "#11P打架……？\x01",
            "不对，是私刑？\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x9, 0x0, 0x5DC, 0x7D0, 0x0)
    EndChrThread(0xF, 0x1)
    Sound(100, 0, 50, 0)
    OP_71(0x8, 0x14, 0x19, 0x0, 0x8)
    OP_79(0x8)
    BeginChrThread(0xF, 1, 0, 26)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0082
    ChrTalk(
        0x9,
        (
            "#11P#4S喂！快住手！\x01",
            "你在做什么！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #N0083
    NpcTalk(
        0x10B,
        "加尔西亚的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4S#11P都是因为你这混蛋，\x01",
            "害得我们在这里吃冰冷的牢饭！\x02\x03",

            "#4S老子这就活活打死你！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0084
    NpcTalk(
        0x101,
        "罗伊德的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2S#11P#60W……呜……啊……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(100, 0, 50, 0)
    OP_71(0x8, 0x19, 0x14, 0x0, 0x8)
    OP_79(0x8)
    OP_9B(0x1, 0x9, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)

    #C0085
    ChrTalk(
        0x9,
        (
            "#11P……不行，\x01",
            "他完全不听劝。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    #C0086
    ChrTalk(
        0x9,
        "#5P没办法了，进去看看吧！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        "#11P好，千万别放松警惕！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x5A, 0x1F4)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0xFA0, 0x0)
    OP_93(0x9, 0x0, 0x1F4)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    Sleep(1)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0xFF, "red00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red02", 0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "green00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "green01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "green02", 0x1, 0x1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_9B(0x0, 0x8, 0x0, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    Sound(105, 0, 100, 0)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x5)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)

    def lambda_36BD():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_36BD)
    Sleep(100)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x10E, 0x1F4)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0xFA0, 0x1)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_3705():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3705)
    Sleep(100)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    EndChrThread(0xF, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_373A")

    OP_68(3300, 1100, 35000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x27)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, 3300, 600, 35000, 270)
    ClearChrFlags(0x101, 0x8)
    BeginChrThread(0x101, 3, 0, 13)
    SetChrFlags(0x10B, 0x20)
    SetChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x28)
    SetChrSubChip(0x10B, 0x0)
    SetChrPos(0x10B, 2750, 0, 35000, 90)
    ClearChrFlags(0x10B, 0x8)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 0, 28000, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 28000, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x8)
    Sound(815, 0, 80, 0)
    Sleep(100)
    Sound(811, 0, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(23500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    ClearMapObjFlags(0xA, 0x10)
    OP_70(0xA, 0xA)
    SetMapObjFlags(0xA, 0x1000)
    OP_68(1800, 1100, 33500, 2000)
    Sleep(300)
    BeginChrThread(0x8, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x9, 3, 0, 15)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0088
    ChrTalk(
        0x9,
        "#12P#4S快住手！加尔西亚！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        "#6P你再不停止行凶，我们就要开枪了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x10B, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    BeginChrThread(0x101, 3, 0, 18)
    BeginChrThread(0x10B, 3, 0, 19)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x10B, 3)

    #C0090
    ChrTalk(
        0x10B,
        (
            "#11104F#5P#30W呵呵……哈哈……\x02\x03",

            "#11102F……真不好意思，\x01",
            "我一时冲动，没能控制住情绪。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        "#12P混蛋……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "#6P本来还觉得你被拘留之后\x01",
            "一直都挺老实……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        "#6P废话少说！退后！举起双手！\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x10B,
        "#11104F#5P哼……\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x10B, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
    Sleep(100)
    Fade(150)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x10B, 0x20)
    SetChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0x10B, 0x28)
    OP_A1(0x10B, 0x4E2, 0x2, 0x1, 0x2)
    OP_0D()
    OP_68(3300, 1100, 35000, 1700)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0x9, 3, 0, 17)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)

    #C0095
    ChrTalk(
        0x9,
        (
            "#11P看来不管再怎么缺人手，\x01",
            "都不应该把他们关在一起啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        "#11P喂，你没事吧？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A6(0x101, 0x0, 0x14, 0x190, 0x7D0)
    Sleep(300)

    #C0097
    ChrTalk(
        0x101,
        "#1S#60W#5P………呜…………啊…………\x02",
    )

    CloseMessageWindow()
    Fade(100)
    PlayEffect(0x0, 0xFF, 0x101, 0x1, -400, 0, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    OP_0D()

    #C0098
    ChrTalk(
        0x101,
        "#5P#2S#40W呃……咳咳！\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#11P啧……\x01",
            "看样子，也许是内脏破裂了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        "#11P先去叫医生吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(22500, 1200)
    Sleep(300)
    OP_A1(0x101, 0x514, 0x6, 0x1, 0x2, 0x3, 0x2, 0x1, 0x2)
    OP_6F(0x79)

    #C0101
    ChrTalk(
        0x101,
        "#5P不，没有这个必要。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_63(0x9, 0xFFFFFED4, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    OP_68(-77000, 1000, 35000, 0)
    MoveCamera(140, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -77000, 0, 35000, 180)
    SetChrPos(0x10B, -79500, 0, 35150, 90)
    SetChrPos(0x8, -80350, 0, 33500, 90)
    SetChrPos(0x9, -77000, 0, 33500, 0)
    SetChrSubChip(0x101, 0x4)
    SetChrSubChip(0x10B, 0x3)
    PlayEffect(0x0, 0xFF, 0x101, 0x1, -400, 0, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 20)
    WaitChrThread(0x101, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-78550, 1100, 34300, 1000)
    MoveCamera(157, 30, 0, 1000)
    SetCameraDistance(23500, 1000)
    OP_93(0x8, 0x2D, 0x1F4)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x8, 0x25)
    OP_A1(0x8, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    OP_6F(0x79)

    #C0102
    ChrTalk(
        0x8,
        "#11P你……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x10B, 3, 0, 21)
    WaitChrThread(0x10B, 3)
    Sleep(500)
    OP_68(-79350, 1800, 34650, 3000)
    OP_6F(0x79)

    #C0103
    ChrTalk(
        0x101,
        "#00006F#5P呼……真有点过意不去。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x10B,
        (
            "#11100F#5P哼哼，事到如今，还说这些干什么。\x02\x03",

            "#11104F你主动要求我\x01",
            "揍你的时候，\x01",
            "我还以为你的脑子出毛病了呢……\x02\x03",

            "#11102F没想到你还挺有智谋的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 500)
    Sleep(150)

    #C0105
    ChrTalk(
        0x101,
        (
            "#00006F#5P彼此彼此，\x01",
            "你的演技也非常逼真啊。\x02\x03",

            "#00010F呜……\x01",
            "但没想到你会真的\x01",
            "打断我的臼齿……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 500)

    #C0106
    ChrTalk(
        0x10B,
        (
            "#11100F#11P呵，多亏如此，\x01",
            "这场戏才显得如此逼真啊。\x02\x03",

            "#11103F……我会遵守约定，\x01",
            "协助你离开这里。\x02\x03",

            "#11101F那么，接下来该怎么做？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00003F#5P这里是拘留所的三层……\x01",
            "看守的士兵应该比较少。\x02\x03",

            "#00013F想办法突破巡逻的士兵，\x01",
            "从一层的出口逃出去吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x10B,
        (
            "#11104F#11P呵呵，好吧。\x02\x03",

            "#11107F好久没有活动过了……\x01",
            "就让我尽情大闹一番吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23000, 1000)
    OP_6F(0x79)
    OP_0D()
    Sound(805, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德装备上了临时打造的\x01",
            "钢管旋棍。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "加尔西亚加入队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于艾尼格玛Ⅱ已被没收，\x01",
            "目前无法使用魔法。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，道具也被全部没收了，\x01",
            "请多加注意ＨＰ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_BC(0x0)
    OP_42(0x0, 0x3F6, 0xFF)
    RemoveCraft(0x0, 0xFFFF)
    OP_DA(0x0)
    OP_42(0xA, 0x46F, 0xFF)
    RemoveCraft(0xA, 0xFFFF)
    AddItemNumber('调查手册', 1)
    AddItemNumber('战斗手册', 1)
    OP_29(0xAE, 0x4, 0x2)
    OP_29(0xAE, 0x1, 0x0)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Call(0, 23)
    SetMapObjFlags(0xA, 0x10)
    ClearMapObjFlags(0xA, 0x1000)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_37()
    SetChrPos(0x0, 0, 0, 33000, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 4)
    OP_C9(0x0, 0x8000)
    ModifyEventFlags(1, 0, 0x80)
    OP_C7(0x1, 0x4)
    OP_32(0x0, 0x11, 0x0)
    OP_32(0xA, 0x11, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_11_FEC end

    def Function_12_4161(): pass

    label("Function_12_4161")


    def lambda_4166():
        OP_96(0xFE, 0xFFFE2B40, 0x0, 0x7148, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4166)
    Sleep(3000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_4161 end

    def Function_13_418E(): pass

    label("Function_13_418E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41B4")
    OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0x1388)
    Sleep(1000)
    Jump("Function_13_418E")

    label("loc_41B4")

    Return()

    # Function_13_418E end

    def Function_14_41B5(): pass

    label("Function_14_41B5")


    def lambda_41BA():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41BA)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x10B, 500)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_41B5 end

    def Function_15_41E9(): pass

    label("Function_15_41E9")


    def lambda_41EE():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41EE)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x10B, 500)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_41E9 end

    def Function_16_4223(): pass

    label("Function_16_4223")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_4237():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4237)
    WaitChrThread(0xFE, 1)

    def lambda_4250():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4250)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_4223 end

    def Function_17_4265(): pass

    label("Function_17_4265")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 3300, 0, 33750, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Sleep(250)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x2)
    OP_0D()
    Return()

    # Function_17_4265 end

    def Function_18_42AB(): pass

    label("Function_18_42AB")

    Sound(802, 0, 100, 0)
    Sleep(150)

    def lambda_42B9():
        OP_98(0xFE, 0x0, 0xFFFFFDA8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42B9)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(811, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_18_42AB end

    def Function_19_42E7(): pass

    label("Function_19_42E7")

    Fade(350)
    ClearChrFlags(0x10B, 0x20)
    ClearChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0x10B, 2450, 0, 35000, 90)
    OP_0D()
    Sleep(300)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE3E, 0x3E8, 0x0)
    Return()

    # Function_19_42E7 end

    def Function_20_4323(): pass

    label("Function_20_4323")

    SetCameraDistance(19500, 500)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x5)
    OP_0D()
    Sleep(150)
    Sound(533, 0, 80, 0)
    Sound(2011, 255, 100, 0)    #voice#Lloyd
    SetChrSubChip(0xFE, 0x6)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-77000, 1000, 31500, 500)
    MoveCamera(135, 25, 0, 500)
    SetCameraDistance(23500, 500)
    Sleep(1)
    CancelBlur(500)
    Sound(815, 0, 100, 0)
    OP_82(0xFA, 0x1F4, 0x2710, 0x1F4)

    #C0113
    ChrTalk(
        0x9,
        "#11P呜……\x05\x02",
    )

    PlayEffect(0x13, 0xFF, 0xFF, 0x0, -77000, 800, 34000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x12, 0xFF, 0xFF, 0x0, -77000, 800, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0x9, 0x5, 0x96)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x1)
    Sleep(100)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x800)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x9, 0x0)
    OP_96(0x9, 0xFFFED338, 0x2EE, 0x7724, 0x2AF8, 0x0)
    Sound(862, 0, 100, 0)
    PlayEffect(0x13, 0xFF, 0xFF, 0x0, -77350, 1550, 30500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A6(0x9, 0x0, 0x32, 0x1F4, 0x1388)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    SetChrSubChip(0x9, 0x1)

    def lambda_44C8():
        OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_44C8)
    WaitChrThread(0x9, 1)
    OP_A1(0x9, 0x3E8, 0x2, 0x2, 0x3)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x800)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    OP_0D()
    OP_6F(0x79)
    CloseMessageWindow()
    Return()

    # Function_20_4323 end

    def Function_21_452A(): pass

    label("Function_21_452A")

    OP_68(-79500, 1500, 35150, 500)
    MoveCamera(157, 22, 0, 500)
    SetCameraDistance(18500, 500)
    Fade(250)

    def lambda_4559():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4559)
    Sleep(150)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x10B, 0x20)
    ClearChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_457D():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_457D)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xFE, 2)
    OP_0D()
    OP_6F(0x79)
    #Sound(2820, 255, 100, 0)    #voice#Garcia

    #C0114
    ChrTalk(
        0x10B,
        "#11107F#4S#5P喝啊啊！\x05\x02",
    )

    Sound(534, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-82180, 1800, 31820, 500)
    SetCameraDistance(23500, 500)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)

    def lambda_45F8():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45F8)
    Sleep(100)
    CancelBlur(500)
    Sound(815, 0, 100, 0)
    OP_82(0xFA, 0x1F4, 0x2710, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 22)

    #C0115
    ChrTalk(
        0x8,
        "#11P哇……！\x05\x02",
    )

    PlayEffect(0x13, 0xFF, 0xFF, 0x0, -80350, 800, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x12, 0xFF, 0xFF, 0x0, -80350, 800, 33500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0x8, 0x5, 0x96)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x800)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_96(0x8, 0xFFFEBD8A, 0x5DC, 0x794A, 0x3A98, 0x0)
    Sound(862, 0, 100, 0)
    PlayEffect(0x13, 0xFF, 0xFF, 0x0, -82550, 2300, 31050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A6(0x8, 0x0, 0x32, 0x1F4, 0x1388)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 0x1)

    def lambda_4751():
        OP_98(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4751)
    WaitChrThread(0x8, 1)
    Sound(514, 0, 100, 0)
    OP_A1(0x8, 0x3E8, 0x2, 0x2, 0x3)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x800)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    CloseMessageWindow()
    Return()

    # Function_21_452A end

    def Function_22_47A1(): pass

    label("Function_22_47A1")

    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_22_47A1 end

    def Function_23_47C4(): pass

    label("Function_23_47C4")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, -3050, 0, 31450, 45)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 2650, 0, 33000, 0)
    Return()

    # Function_23_47C4 end

    def Function_24_482B(): pass

    label("Function_24_482B")

    Sound(882, 0, 100, 0)
    Sleep(2600)
    Sound(882, 0, 80, 0)

    label("loc_483A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_485F")
    Sleep(3800)
    Sound(882, 0, 40, 0)
    Sleep(2200)
    Sound(882, 0, 40, 0)
    Sleep(500)
    Jump("loc_483A")

    label("loc_485F")

    Return()

    # Function_24_482B end

    def Function_25_4860(): pass

    label("Function_25_4860")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_489D")
    Sound(815, 0, 40, 0)
    Sleep(100)
    Sound(811, 0, 40, 0)
    Sleep(600)
    Sound(886, 0, 40, 0)
    Sleep(700)
    Sound(862, 0, 30, 0)
    Sleep(100)
    Sound(815, 0, 30, 0)
    Sleep(700)
    Jump("Function_25_4860")

    label("loc_489D")

    Return()

    # Function_25_4860 end

    def Function_26_489E(): pass

    label("Function_26_489E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48DB")
    Sound(815, 0, 60, 0)
    Sleep(100)
    Sound(811, 0, 60, 0)
    Sleep(600)
    Sound(886, 0, 50, 0)
    Sleep(700)
    Sound(862, 0, 50, 0)
    Sleep(100)
    Sound(815, 0, 40, 0)
    Sleep(700)
    Jump("Function_26_489E")

    label("loc_48DB")

    Return()

    # Function_26_489E end

    def Function_27_48DC(): pass

    label("Function_27_48DC")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    LoadChrToIndex("chr/ch00051.itc", 0x20)
    LoadChrToIndex("chr/ch04151.itc", 0x21)
    SetChrPos(0x101, 27600, 0, -1600, 90)
    SetChrPos(0x10B, 27400, 0, -400, 90)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 38500, 0, -7000, 270)
    SetChrFlags(0xA, 0x40)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 38500, 0, -7000, 270)
    SetChrFlags(0xB, 0x40)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)
    OP_68(27500, 1000, -1000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetCameraDistance(25500, 1000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(38000, 1000, -7000, 3000)
    MoveCamera(60, 26, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(25500, 3000)
    OP_6F(0x79)
    SetChrPos(0x101, 24500, 0, -1700, 90)
    SetChrPos(0x10B, 24500, 0, -300, 90)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10B, 0x21)
    SetChrSubChip(0x10B, 0x0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x2)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 28)
    BeginChrThread(0xB, 3, 0, 29)
    OP_68(34500, 1000, -7000, 3000)
    MoveCamera(45, 23, 0, 3000)
    Sleep(500)

    #C0116
    ChrTalk(
        0xA,
        (
            "……他们两个到底\x01",
            "在做什么啊？\x05\x02",
        )
    )

    OP_6F(0x79)
    OP_68(34500, 1000, -1000, 4000)

    #C0117
    ChrTalk(
        0xB,
        (
            "#11P我还想赶快换班，\x01",
            "早点回家呢……\x05\x02",
        )
    )

    WaitChrThread(0xA, 3)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0118
    ChrTalk(
        0xA,
        "#5P咦……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xB,
        "#11P你们是……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(25500, 1000, -1000, 0)
    MoveCamera(45, 23, 0, 0)
    SetCameraDistance(33500, 0)
    OP_68(34500, 1000, -1000, 1500)
    SetCameraDistance(25500, 1500)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x10B, 0x1000)

    def lambda_4BDE():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BDE)

    def lambda_4BF3():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_4BF3)

    #C0120
    ChrTalk(
        0x10B,
        "#11107F#5P太慢了！\x05\x02",
    )


    #C0121
    ChrTalk(
        0x101,
        "#00007F#6P#N上吧……！\x05\x02",
    )

    Sleep(1000)
    SetCameraDistance(23500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x10B, 0x1)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x10B, 0x1000)
    Battle("BattleInfo_434", 0x0, 0x2, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 30)
    Return()

    # Function_27_48DC end

    def Function_28_4C82(): pass

    label("Function_28_4C82")


    def lambda_4C87():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C87)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_4C82 end

    def Function_29_4CCE(): pass

    label("Function_29_4CCE")

    Sleep(1000)

    def lambda_4CD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4CD6)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x2)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_4CCE end

    def Function_30_4D4B(): pass

    label("Function_30_4D4B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41453.itc", 0x1E)
    LoadChrToIndex("chr/ch41553.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch04150.itc", 0x21)
    SoundLoad(907)
    SetChrPos(0x101, 32500, 0, -1800, 90)
    SetChrPos(0x10B, 32500, 0, -200, 90)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10B, 0x21)
    SetChrSubChip(0x10B, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 35500, 0, 0, 270)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 35000, 0, -1600, 270)
    OP_68(34500, 1000, -1000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24860, 0)
    SetCameraDistance(23860, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0122
    ChrTalk(
        0xA,
        "#5P#30W唔……你们……\x02",
    )

    CloseMessageWindow()

    def lambda_4E4D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4E4D)
    Sleep(150)
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x1)
    OP_0D()
    WaitChrThread(0xA, 2)

    #C0123
    ChrTalk(
        0xB,
        "#11P#30W别、别想逃跑……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 1000)

    def lambda_4EAD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4EAD)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xB, 0x2)
    OP_0D()
    WaitChrThread(0xB, 2)
    Sleep(500)

    def lambda_4EE0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4EE0)
    Sleep(150)
    Fade(250)
    Sound(804, 0, 100, 0)
    OP_0D()
    WaitChrThread(0xB, 2)

    def lambda_4F0C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4F0C)
    Sleep(150)
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x1)
    SetChrPos(0xB, 35000, 0, -1600, 90)
    ClearChrFlags(0xB, 0x1)
    OP_0D()
    WaitChrThread(0xB, 2)
    OP_6F(0x79)
    Sleep(500)
    Sound(907, 2, 100, 0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0124
    ChrTalk(
        0x101,
        (
            "#00010F#6P啧，他们用艾尼格玛\x01",
            "启动了紧急警报系统……！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    OP_0D()
    TurnDirection(0x10B, 0x101, 500)

    #C0125
    ChrTalk(
        0x10B,
        (
            "#11104F#5P哼哼……\x01",
            "那接下来怎么办？\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    TurnDirection(0x101, 0x10B, 500)

    #C0126
    ChrTalk(
        0x101,
        (
            "#00007F#12P这种事态也在预料之中……\x01",
            "继续前进，强行突破吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x10B,
        "#11102F#5P哈哈，就这么办吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(907, 2000, 100)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Call(0, 31)
    ClearMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_37()
    SetChrPos(0x0, 32500, 0, -1000, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 5)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_30_4D4B end

    def Function_31_50FC(): pass

    label("Function_31_50FC")

    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 35500, 0, 0, 270)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0xB, 0x80)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, 35000, 0, -1600, 90)
    Return()

    # Function_31_50FC end

    def Function_32_5163(): pass

    label("Function_32_5163")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30000.itc", 0x1E)
    LoadChrToIndex("apl/ch51606.itc", 0x1F)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "green00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "green01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "green02", 0x0, 0x1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 1000, 150, 1000, 180)
    OP_68(610, 1000, -310, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 400, 0, -800, 0)
    SetChrPos(0x102, 1600, 0, -800, 0)
    SetChrPos(0x103, 300, 0, -2000, 0)
    SetChrPos(0x104, 1700, 0, -2000, 0)
    SetChrPos(0xF4, 200, 0, -3200, 0)
    SetChrPos(0xF5, 1800, 0, -3200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0128
    ChrTalk(
        0xE,
        "……会面时间只有十分钟。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xE,
        (
            "由于本次的探望对象是伤员，\x01",
            "所以采取特别措施，\x01",
            "允许你们在房间内见面……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xE,
        (
            "但不得与犯人进行直接接触或交接物品，\x01",
            "禁止一切有可能引发混乱的行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#12P#00000F嗯，我明白了。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        "嗯，那么……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    #C0133
    ChrTalk(
        0xE,
        "#11P加尔西亚，探监的人来了！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 10, -1, -1)
    SetChrName("加尔西亚的声音")

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……好，进来吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0xE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(1000)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0xFF, "red00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "red02", 0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0xFF, "green00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "green01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "green02", 0x1, 0x1)
    OP_0D()
    OP_93(0xE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(1000)
    Sound(105, 0, 100, 0)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x5)

    def lambda_5495():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5495)
    Sleep(100)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(750)
    BeginChrThread(0x102, 3, 0, 40)
    Sleep(250)
    BeginChrThread(0x103, 3, 0, 40)
    Sleep(750)
    BeginChrThread(0x104, 3, 0, 40)
    Sleep(250)
    BeginChrThread(0xF4, 3, 0, 40)
    Sleep(750)
    BeginChrThread(0xF5, 3, 0, 40)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0xF4, 0xFF)
    EndChrThread(0xF5, 0xFF)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x2)
    SetChrPos(0xD, 2100, 150, 38000, 270)
    OP_68(-540, 1000, 34330, 0)
    MoveCamera(41, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xE, 0, 0, 27000, 0)
    SetChrPos(0x101, 0, 0, 27000, 0)
    SetChrPos(0x102, 0, 0, 27000, 0)
    SetChrPos(0x103, 0, 0, 27000, 0)
    SetChrPos(0x104, 0, 0, 27000, 0)
    SetChrPos(0xF4, 0, 0, 27000, 0)
    SetChrPos(0xF5, 0, 0, 27000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xE, 3, 0, 33)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 35)
    Sleep(1000)
    BeginChrThread(0xF4, 3, 0, 36)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 37)
    Sleep(750)
    BeginChrThread(0x103, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0xF5, 3, 0, 39)
    Sleep(2000)
    OP_68(810, 800, 39690, 6000)
    OP_6F(0x79)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0xF5, 3)

    #C0135
    ChrTalk(
        0x101,
        "#6P#00000F加尔西亚……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        (
            "#11100F呵呵，我们又见面了，小鬼。\x02\x03",

            "#11104F看来你已经和同伴再会了，不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#6P#00305F哎呀，大叔，\x01",
            "你都可以起身了啊。\x02\x03",

            "#00303F听说你和国防军大战一场，\x01",
            "消耗了不少体力，没事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xD,
        (
            "#11103F哼，怎么可能没事。\x01",
            "我可是空手硬拼他们的\x01",
            "来复枪和斧枪啊。\x02\x03",

            "#11101F说来丢人……\x01",
            "其实我现在连坐起来都很勉强。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5843")

    #C0139
    ChrTalk(
        0x10A,
        (
            "#6P#00600F哼，话虽如此，\x01",
            "但你却显得相当从容呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C8")

    label("loc_5843")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_588D")

    #C0140
    ChrTalk(
        0x109,
        (
            "#6P#10102F话、话虽如此，\x01",
            "但我却觉得你很从容呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C8")

    label("loc_588D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58C8")

    #C0141
    ChrTalk(
        0x106,
        (
            "#6P#10701F但看上去却显得\x01",
            "很从容呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_590C")

    #C0142
    ChrTalk(
        0x105,
        (
            "#6P#10402F呵呵，真不愧是\x01",
            "『杀戮之熊』啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_598F")

    label("loc_590C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_595A")

    #C0143
    ChrTalk(
        0x106,
        (
            "#6P#10703F西风旅团的『杀戮之熊』，\x01",
            "果然名不虚传啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_598F")

    label("loc_595A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_598F")

    #C0144
    ChrTalk(
        0x109,
        (
            "#6P#10106F真不愧是\x01",
            "前猎兵呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_598F")


    #C0145
    ChrTalk(
        0x103,
        (
            "#6P#00200F不过，暂时还是\x01",
            "无法动弹吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0146
    ChrTalk(
        0x101,
        (
            "#6P#00001F……加尔西亚，我对你的\x01",
            "感激之情无以言表。\x02\x03",

            "#00003F当时要不是你\x01",
            "协助我逃离拘留所……\x02\x03",

            "#00000F我肯定无法和\x01",
            "同伴们再会，\x01",
            "更不可能走到现在这一步。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        "#6P#00102F罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xD,
        (
            "#11101F……嘿，你就是为了和我说这种话，\x01",
            "才专程前来探监的吗？\x02\x03",

            "#11103F我与你的合作，\x01",
            "从踏出拘留所大门的那一刻起\x01",
            "就已经结束了。\x02\x03",

            "#11102F对我来说，你依然是摧毁了我们的组织，\x01",
            "令人厌恶的混蛋……\x01",
            "至今都没有任何改变哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#6P#00004F……即使如此，\x01",
            "我也想对你说声谢谢。\x02\x03",

            "#00000F谢谢，加尔西亚。\x01",
            "多亏你，我现在\x01",
            "才能站在这里。\x02\x03",

            "#00000F我一定会查清\x01",
            "这一系列事件的真相，\x01",
            "尽我所能来守护克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    #C0150
    ChrTalk(
        0xD,
        (
            "#11103F哼……\x01",
            "你让我想起了一个讨厌的家伙。\x02\x03",

            "还有他那双无论遇到什么困境，遭受\x01",
            "多少次挫折都不显露出丝毫黯淡之色，\x01",
            "始终都紧紧盯住目标的眼睛……\x02\x03",

            "#11102F班宁斯……\x01",
            "你真不愧是盖伊的弟弟。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#6P#00305F大叔……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#6P#00004F……哈哈，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xD,
        (
            "#11103F……哼，\x01",
            "说了些不合\x01",
            "性格的废话。\x02\x03",

            "#11101F你们几个，\x01",
            "现在还有时间在这种地方\x01",
            "和我闲聊吗？\x02\x03",

            "#11103F……赶快从我眼前消失吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#6P#00004F……嗯，我明白。\x02\x03",

            "#00000F各位，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6000", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_32_5163 end

    def Function_33_5DF7(): pass

    label("Function_33_5DF7")


    def lambda_5DFC():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5DFC)

    def lambda_5E16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5E16)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_5E2F():
        OP_95(0xFE, 0, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E2F)
    WaitChrThread(0xFE, 1)

    def lambda_5E4D():
        OP_95(0xFE, 2000, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E4D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(5000)

    def lambda_5E75():
        OP_95(0xFE, 0, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E75)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_5DF7 end

    def Function_34_5E96(): pass

    label("Function_34_5E96")


    def lambda_5E9B():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E9B)

    def lambda_5EB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5EB5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_5ECE():
        OP_95(0xFE, -1370, 0, 39290, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5ECE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_5E96 end

    def Function_35_5EEF(): pass

    label("Function_35_5EEF")


    def lambda_5EF4():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5EF4)

    def lambda_5F0E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5F0E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_5F27():
        OP_95(0xFE, -160, 0, 39190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F27)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_35_5EEF end

    def Function_36_5F48(): pass

    label("Function_36_5F48")


    def lambda_5F4D():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F4D)

    def lambda_5F67():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5F67)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_5F80():
        OP_95(0xFE, -1240, 0, 38210, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F80)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_36_5F48 end

    def Function_37_5FA1(): pass

    label("Function_37_5FA1")


    def lambda_5FA6():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FA6)

    def lambda_5FC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5FC0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_5FD9():
        OP_95(0xFE, 0, 0, 38000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FD9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_37_5FA1 end

    def Function_38_5FFA(): pass

    label("Function_38_5FFA")


    def lambda_5FFF():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FFF)

    def lambda_6019():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6019)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6032():
        OP_95(0xFE, -300, 0, 36920, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6032)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_38_5FFA end

    def Function_39_6053(): pass

    label("Function_39_6053")


    def lambda_6058():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6058)

    def lambda_6072():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6072)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_608B():
        OP_95(0xFE, -1470, 0, 36720, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_608B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_6053 end

    def Function_40_60AC(): pass

    label("Function_40_60AC")

    OP_96(0xFE, 0x3E8, 0x96, 0x3E8, 0x7D0, 0x0)

    def lambda_60C5():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60C5)
    Sleep(100)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_40_60AC end

    SaveToFile()

Try(main)
