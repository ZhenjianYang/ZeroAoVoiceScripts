from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "国防軍兵士",             # 1
        "国防軍兵士",             # 2
        "国防軍兵士",             # 3
        "国防軍兵士",             # 4
        "ノエル少尉",             # 5
        "ガルシア",               # 6
        "看守メルビン",           # 7
        "SE制御",                 # 8
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
        "Function_3_7B9",          # 03, 3
        "Function_4_89F",          # 04, 4
        "Function_5_985",          # 05, 5
        "Function_6_A2A",          # 06, 6
        "Function_7_B52",          # 07, 7
        "Function_8_BDF",          # 08, 8
        "Function_9_D7D",          # 09, 9
        "Function_10_EDF",         # 0A, 10
        "Function_11_107C",        # 0B, 11
        "Function_12_45C3",        # 0C, 12
        "Function_13_45F0",        # 0D, 13
        "Function_14_4617",        # 0E, 14
        "Function_15_464B",        # 0F, 15
        "Function_16_4685",        # 10, 16
        "Function_17_46C7",        # 11, 17
        "Function_18_470D",        # 12, 18
        "Function_19_4749",        # 13, 19
        "Function_20_4785",        # 14, 20
        "Function_21_4990",        # 15, 21
        "Function_22_4C0D",        # 16, 22
        "Function_23_4C30",        # 17, 23
        "Function_24_4C97",        # 18, 24
        "Function_25_4CCC",        # 19, 25
        "Function_26_4D0A",        # 1A, 26
        "Function_27_4D48",        # 1B, 27
        "Function_28_5104",        # 1C, 28
        "Function_29_5150",        # 1D, 29
        "Function_30_51CD",        # 1E, 30
        "Function_31_5582",        # 1F, 31
        "Function_32_55E9",        # 20, 32
        "Function_33_6417",        # 21, 33
        "Function_34_64B6",        # 22, 34
        "Function_35_650F",        # 23, 35
        "Function_36_6568",        # 24, 36
        "Function_37_65C1",        # 25, 37
        "Function_38_661A",        # 26, 38
        "Function_39_6673",        # 27, 39
        "Function_40_66CC",        # 28, 40
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_782")
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
            "を１０個手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20E, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_7A7")

    label("loc_782")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7A7")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6D1 end

    def Function_3_7B9(): pass

    label("Function_3_7B9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868")
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
            "を５個手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FC, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_88D")

    label("loc_868")


    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_88D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7B9 end

    def Function_4_89F(): pass

    label("Function_4_89F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94E")
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
            "を２個手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x55, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_973")

    label("loc_94E")


    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_973")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_89F end

    def Function_5_985(): pass

    label("Function_5_985")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0C")
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

    label("loc_A0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A28")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_A28")

    Return()

    # Function_5_985 end

    def Function_6_A2A(): pass

    label("Function_6_A2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23")

    #C0007
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00001F……完全に気絶してるみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x10B,
        (
            "#11102Fクク、何を他人事みてえに。\x01",
            "俺たちの手でやったんだろうが？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00003F……分かってる。\x02\x03",

            "#00001F彼らには悪いけど、\x01",
            "このまま進ませてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B4E")

    label("loc_B23")

    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "国防軍兵士は気を失っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B4E")

    TalkEnd(0xFE)
    Return()

    # Function_6_A2A end

    def Function_7_B52(): pass

    label("Function_7_B52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB0")

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
            "国防軍兵士は気を失っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BDB")

    label("loc_BB0")

    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "国防軍兵士は気を失っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BDB")

    TalkEnd(0xFE)
    Return()

    # Function_7_B52 end

    def Function_8_BDF(): pass

    label("Function_8_BDF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB2")
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C08")
    SetChrName("声")
    Jump("loc_C16")

    label("loc_C08")

    SetChrName("マフィアの声")

    label("loc_C16")


    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……今、何か大きな音がしなかったか？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6C")
    SetChrName("声")
    Jump("loc_C7A")

    label("loc_C6C")

    SetChrName("マフィアの声")

    label("loc_C7A")


    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "ああ……？\x01",
            "空耳じゃねえのか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6C")

    label("loc_CB2")

    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCE")
    SetChrName("声")
    Jump("loc_CDC")

    label("loc_CCE")

    SetChrName("マフィアの声")

    label("loc_CDC")


    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "な、なんだこの騒ぎは……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2A")
    SetChrName("声")
    Jump("loc_D38")

    label("loc_D2A")

    SetChrName("マフィアの声")

    label("loc_D38")


    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "おいおい、何かあったのかよ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D79")
    Call(0, 9)

    label("loc_D79")

    TalkEnd(0xFF)
    Return()

    # Function_8_BDF end

    def Function_9_D7D(): pass

    label("Function_9_D7D")


    #C0019
    ChrTalk(
        0x101,
        "#00005F（この部屋は……？）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10B,
        (
            "#11100F（ここと向こうの部屋には\x01",
            "  ウチ#4Rルバーチェ#の部下どもが\x01",
            "  まとめて押し込められているはずだ。）\x02\x03",

            "#11103F（人手も足りてねえみたいだし、\x01",
            "  このフロアで厄介な奴らを\x01",
            "  まとめて見張るつもりなんだろう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00003F（なるほどな……）\x02\x03",

            "#00001F（……とにかく、急ぐとしよう。\x01",
            "  増援が来ないうちに突破するぞ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 0)
    Return()

    # Function_9_D7D end

    def Function_10_EDF(): pass

    label("Function_10_EDF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB0")
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F08")
    SetChrName("声")
    Jump("loc_F16")

    label("loc_F08")

    SetChrName("マフィアの声")

    label("loc_F16")


    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "若頭の部屋から\x01",
            "すげえ音が聞こえたぞ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6D")
    SetChrName("声")
    Jump("loc_F7B")

    label("loc_F6D")

    SetChrName("マフィアの声")

    label("loc_F7B")


    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "大丈夫ですかい、若頭ー！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_106B")

    label("loc_FB0")

    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCC")
    SetChrName("声")
    Jump("loc_FDA")

    label("loc_FCC")

    SetChrName("マフィアの声")

    label("loc_FDA")


    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "こ、今度は警報だあ……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(120, 10, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1026")
    SetChrName("声")
    Jump("loc_1034")

    label("loc_1026")

    SetChrName("マフィアの声")

    label("loc_1034")


    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "若頭ァー！\x01",
            "大丈夫なんですかい！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_106B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1078")
    Call(0, 9)

    label("loc_1078")

    TalkEnd(0xFF)
    Return()

    # Function_10_EDF end

    def Function_11_107C(): pass

    label("Function_11_107C")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_129C")
    Jump("loc_34E6")

    label("loc_129C")

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

    def lambda_130F():
        OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_130F)
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
            "#10203F#5P──支援課の他のメンバーは\x01",
            "別の場所で保護しています。\x02\x03",

            "#10208Fロイドさん一人、こんな場所に\x01",
            "拘留するのは申し訳ありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00006F#11P……俺のことはいいさ。\x02\x03",

            "#00008Fでも“保護”っていうのは\x01",
            "さすがにおかしな言い方だな？\x02\x03",

            "#00002F一体何から……\x01",
            "保護してくれるっていうんだ？\x02",
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
            "#00003F#11P……君だってもう\x01",
            "とっくに気付いているはずだ。\x02\x03",

            "#00008Fクロスベル市の襲撃を企てた\x01",
            "真の黒幕が誰かということも。\x02\x03",

            "#00013Fフランを──君の妹さんを\x01",
            "傷つけたのが誰かということも……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0031
    ChrTalk(
        0xC,
        "#10215F#5P#4Sそれでも……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0032
    ChrTalk(
        0xC,
        (
            "#10207F#5P……それでもあたしは\x01",
            "警備隊のメンバーですから！\x02\x03",

            "それが『国防軍』に名を変えた以上、\x01",
            "軍人としての責務を果たすだけです！\x02\x03",

            "#10208Fそうでないとクロスベルは……\x02\x03",

            "#10206F……クロスベルは本当に\x01",
            "帝国と共和国に滅ぼされてしまう！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00005F#11Pノエル……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xC,
        (
            "#10206F#5Pキーアちゃんのことだって……\x01",
            "このままで良いとは思えません！\x02\x03",

            "《結社》みたいな得体の知れない\x01",
            "連中の力を借りることだって……！\x02\x03",

            "#10210Fでも──帝国軍は本当に#6R㈲　㈲　㈲#\x01",
            "あの恐ろしい列車砲を撃ったんです！\x02\x03",

            "命中したら何百人もの犠牲者が\x01",
            "出たかもしれない大量破壊兵器を！\x02\x03",

            "#10215F……だったら……\x01",
            "だったら仕方ないじゃないですか！\x02",
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
            "#10206F#5Pすみません……\x02\x03",

            "……ロイドさんにこんな事、\x01",
            "言えた義理はありませんよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(400)

    #C0037
    ChrTalk(
        0xC,
        (
            "#10208F#11P──拘留期間も\x01",
            "そう長くは続かないと思います。\x02\x03",

            "クロスベルが危機を乗り越えたら\x01",
            "きっと釈放されると思いますから……\x02\x03",

            "#10203Fだからどうか……\x01",
            "今は辛抱していてください。\x02",
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
            "#00006F#5P#30W（……あの時……\x01",
            "  俺はロクな言葉を返せなかった。）\x02\x03",

            "#00008F（それだけじゃない……\x01",
            "  キーアが思い詰めていたのだって\x01",
            "  ぜんぜん気付けなかった……）\x02\x03",

            "（忙しさに翻弄されるだけで……\x01",
            "  本当に守るべきものも守れずに……）\x02\x03",

            "#00006F（……キーアの素性にしても\x01",
            "  兄貴を殺した犯人にしても……）\x02\x03",

            "#00015F（ちゃんと突き止めようと\x01",
            "  心に誓ったはずなのに……！）\x02",
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
            "#30Wガイ・バニングスを──\x01",
            "兄貴を殺したのも貴方なのか？\x02",
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
            "#4119V#30Wああ──その通りだ。\x07\x00\x02",
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
            "#3630V#30Wゴメンね。\x01",
            "……今までありがとう。\x02\x03",

            "#3631V大好きだよ──みんな。\x07\x00\x02",
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
            "#00006F#5P#30W（兄貴……ゴメン……）\x02\x03",

            "（やっぱり俺……\x01",
            "  兄貴に全然追いつけて\x01",
            "  なかったみたいだ……）\x02\x03",

            "#00015F（だってもう……\x01",
            "  俺はどうしたらいいか……）\x02\x03",

            "（……それさえも…………）\x02",
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
        "逞しい声",
        "#5P──ザマぁねえな。\x02",
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
            "俺たちを追い詰めてパクった\x01",
            "リーダーがその体たらくとは……\x02\x03",

            "こんな場所で半年以上、\x01",
            "冷や飯を喰らっているのが\x01",
            "馬鹿馬鹿しくなってくるぜ。\x02",
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
            "#00006F#6P#30W……放っておいてくれ。\x02\x03",

            "あんたがこの場所にいるのは\x01",
            "どう考えても自業自得だし……\x02\x03",

            "あんた達を逮捕できたのだって\x01",
            "運が良かったのが重なっただけさ……\x02\x03",

            "#00008Fそうだ……別に俺たちは実力で\x01",
            "《壁》を越えたわけじゃないんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x10B,
        "#11101F#11Pケッ、辛気臭ぇ小僧だな。\x02",
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
            "#11104F#11Pま、無理もねぇか。\x02\x03",

            "噂を聞く限り、とんでもねぇ\x01",
            "状況になってるみたいだしな。\x02\x03",

            "#11101FＩＢＣ総裁が全ての黒幕で\x01",
            "今や独裁国家の大統領……\x02\x03",

            "赤い星座やら結社やら、\x01",
            "国防軍に風の剣聖まで\x01",
            "ことごとく敵に回ってるわけだ。\x02\x03",

            "#11102Fクク、トリプル役満どころの\x01",
            "話じゃなさそうだなァ？\x02",
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
            "#11104F#5Pま、今は嵐が通り過ぎるのを\x01",
            "待ってるのが正解ってモンだぜ。\x02\x03",

            "この状況で抗#2Rあらが#おうなんて\x01",
            "正真正銘の馬鹿しかいねぇだろ。\x02\x03",

            "#11100F──てめぇの兄貴みてぇな、な。\x02",
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
            "#00011F#6P#30W………ぁ…………\x02\x03",

            "#00001F#20Wそう言えば、うちの兄貴と\x01",
            "面識があるんだったか……？\x02",
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
            "#11100F#5Pフン、面識というほど\x01",
            "ぬるいモンじゃなかったがな。\x02\x03",

            "#11103Fこちらが幾ら脅しつけても\x01",
            "懲りもせずに嗅ぎ回ってくる……\x02\x03",

            "……かと思えば、\x01",
            "バッタリ屋台で出くわした時に\x01",
            "平気で一杯勧めてきやがる……\x02\x03",

            "#11101F厄介で忌々しい若造だったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00004F#6P#30Wはは……兄貴らしいな。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A1(0x10B, 0x3E8, 0x2, 0x5, 0x6)
    Sleep(300)

    #C0053
    ChrTalk(
        0x10B,
        (
            "#11103F#5P……ま、殺しても\x01",
            "死ぬようなタマには見えなかったが\x01",
            "アッサリ逝っちまったからな。\x02\x03",

            "世の中なんて分からねぇもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W……………………………………\x02\x03",

            "#00001F……兄貴はずっと……\x01",
            "抗#2Rあらが#い続けていたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x10B,
        (
            "#11104F#5Pああ、ウチ#4Rルバーチェ#以外にも\x01",
            "首を突っ込んでたらしいからな。\x02\x03",

            "大物議員の汚職から\x01",
            "帝国と共和国の諜報活動、\x01",
            "ヨアヒムの野郎の動きまで……\x02\x03",

            "#11100F呆れるくらい精力的だったのは\x01",
            "間違いねぇだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#00006F#6P#30W……そっか………\x02",
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
            "#11103F#11P──おい。\x01",
            "カン違いしてるみてぇだが。\x02\x03",

            "#11101Fガイ・バニングスってのは別に\x01",
            "“スゲエ男”じゃなかったぜ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x101,
        "#00005F#6Pえ……？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x10B,
        (
            "#11104F#11Pキレと凄みで言うなら\x01",
            "マクレインの方が上だろう。\x02\x03",

            "搦#2Rから#め手と根回しだったら\x01",
            "セルゲイの方が上だろうしな。\x02\x03",

            "#11100F合理的な判断と処理能力なら\x01",
            "一課のダドリーの方が上……\x02\x03",

            "つまりはその程度ってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00011F#6P……それは………\x02\x03",

            "#00008F（……考えてみれば\x01",
            "  確かにそうかもしれない。）\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x10B,
        (
            "#11103F#11Pヤツに抜きん出てたところが\x01",
            "あったとしたら……\x02\x03",

            "#11101Fせいぜい“諦めない”こと\x01",
            "くらいだろうぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x12C, 1800, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x101,
        "#00005F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x10B,
        (
            "#11100F#11Pそれが多分、ハンパねぇ行動力に\x01",
            "繋がったんだろうし……\x02\x03",

            "大物相手にも食い下がれる\x01",
            "原動力になってたんだろう。\x02\x03",

            "#11103Fそれでいて、周りが見えてない\x01",
            "空気の読めなさも無かったし……\x02\x03",

            "#11101F……何なんだこの若造はって、\x01",
            "当時は思ったモンだぜ。\x02",
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
            "#30W──いいか、ロイド。\x02\x03",

            "男だったら、目の前のものに\x01",
            "体当たりでぶつかってみろ。\x02\x03",

            "てめえの心で、てめえだけの\x01",
            "真実を掴みとってやるんだよ。\x02\x03",

            "そうすりゃ、てめえが\x01",
            "何をしたいか見えてくるはずだ。\x07\x00\x02",
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
            "#00006F#6P……多分、兄貴の諦めの悪さは\x01",
            "大切なものを守るためだったと思う。\x02\x03",

            "#00008Fそれも身内だけじゃなくて、\x01",
            "クロスベルという街そのもの……\x02\x03",

            "#00000F……その意味では、\x01",
            "あんたたちルバーチェですら\x01",
            "守る対象だったのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B, 0xFFFFFF38, 2100, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x10B,
        "#11105F#11Pなにィ……？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#00012F#6Pハハ、守るっていうと\x01",
            "おこがましいかもしれないけど……\x02\x03",

            "#00008F多分、兄貴は体当たりで\x01",
            "今のクロスベルを作ってきた流れを\x01",
            "見極めようとしてたんだと思う。\x02\x03",

            "#00004Fその上で、クロスベルそのものを\x01",
            "自分なりに守ろうと足掻いていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x10B,
        (
            "#11103F#11Pそいつは……\x02\x03",

            "#11110F……馬鹿以上の\x01",
            "とんでもねぇ大馬鹿じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00003F#6Pああ……\x02\x03",

            "#00008F……俺は到底、\x01",
            "そこまで馬鹿にはなれない……\x02\x03",

            "#00000F──でも兄弟だけあって\x01",
            "似ている部分もあるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x10B,
        "#11105F#11Pなに……\x02",
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

    def lambda_3267():
        OP_96(0xFE, 0x0, 0x0, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3267)
    Sleep(500)
    SetChrSubChip(0x10B, 0x7)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_6F(0x79)

    #C0072
    ChrTalk(
        0x10B,
        (
            "#11101F#5P……てめぇ、まさか。\x02\x03",

            "ここから逃げ出すつもりか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(150)

    #C0073
    ChrTalk(
        0x101,
        (
            "#00003F#12P逃げ出すんじゃない。\x01",
            "真実を見極めに行くつもりだ。\x02\x03",

            "#00001Fクロスベル警察、特務支援課に\x01",
            "所属する捜査官として……\x02\x03",

            "囚われたみんなを解放して、\x01",
            "キーアを取り戻すためにも。\x02",
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
            "#11104F#5Pクク……ハハ……\x02\x03",

            "#11102Fてめぇも十分、\x01",
            "大馬鹿野郎だろうが。\x02",
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
        "#00005F#12Pガルシア……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x10B,
        (
            "#11103F#5P──見せてみろ、小僧。\x02\x03",

            "この状況で、てめぇという男に\x01",
            "どんな事が出来るのか……\x02\x03",

            "#11102F覚悟と決意の程をな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(25650, 2000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()

    label("loc_34E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_34F6")
    Jump("loc_3AE6")

    label("loc_34F6")

    Sleep(1000)
    OP_68(28000, 1100, -1000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x8, 33000, 0, -1600, 270)
    ClearChrFlags(0x9, 0x8)

    def lambda_3542():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3542)
    Sleep(50)

    def lambda_355A():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_355A)
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
        "#11Pなんだ……？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        "#5P奥からみたいだが……\x02",
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

    def lambda_364A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_364A)
    Sleep(50)

    def lambda_3662():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3662)
    WaitChrThread(0x8, 1)

    def lambda_367B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_367B)
    WaitChrThread(0x9, 1)

    def lambda_368C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_368C)
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
        "ガルシアの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#3S#11Pオラあああッ！\x01",
            "その程度かガキがあああッ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #N0080
    NpcTalk(
        0x101,
        "ロイドの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#1S#11P#50Wぐっ……ゲホゲホ……\x07\x00\x02",
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
            "#11P喧嘩……\x01",
            "いや、リンチか？\x02",
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
            "#11P#4Sおい、止めろ！\x01",
            "何をやっている！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #N0083
    NpcTalk(
        0x10B,
        "ガルシアの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4S#11Pてめぇのせいで俺たちは\x01",
            "冷や飯を喰らうことになったんだ！\x02\x03",

            "#4Sこのままブチ殺してやらああっ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0084
    NpcTalk(
        0x101,
        "ロイドの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2S#11P#60W……ガッ……ぅぐ……\x07\x00\x02",
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
            "#11P……駄目だ。\x01",
            "聞いちゃいない。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    #C0086
    ChrTalk(
        0x9,
        "#5P仕方ない、踏み込むぞ！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        "#11Pああ、警戒を怠るな！\x02",
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

    def lambda_3A69():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A69)
    Sleep(100)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x10E, 0x1F4)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0xFA0, 0x1)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_3AB1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3AB1)
    Sleep(100)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    EndChrThread(0xF, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_3AE6")

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
        "#12P#4S止めろ、ガルシア！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        "#6Pそれ以上やると撃つぞ！\x02",
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
            "#11104F#5P#30Wクク……ハハ……\x02\x03",

            "#11102F……俺としたことがつい、\x01",
            "熱くなりすぎちまったようだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        "#12P貴様……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "#6Pここに入ってからずっと\x01",
            "大人しくしていたと思えば……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        "#6Pいいから下がって両手を上げろ！\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x10B,
        "#11104F#5Pフン……\x02",
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
            "#11Pいくら人手が足りないとはいえ、\x01",
            "同室にするべきじゃなかったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        "#11P──おい、大丈夫か？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A6(0x101, 0x0, 0x14, 0x190, 0x7D0)
    Sleep(300)

    #C0097
    ChrTalk(
        0x101,
        "#1S#60W#5P………ぅ…………ぁ…………\x02",
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
        "#5P#2S#40Wかはッ……ゴホゴホ！\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#11Pくっ……\x01",
            "内臓が破裂したかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        "#11Pとにかく医者を──\x02",
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
        "#5P──いや、必要ない。\x02",
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
        "#11P貴様──\x02",
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
        "#00006F#5Pはぁ……気が咎#2Rとが#めるな。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x10B,
        (
            "#11100F#5Pクク、今さらか？\x02\x03",

            "#11104F『俺を殴ってくれ』とか\x01",
            "言い出しやがった時は\x01",
            "トチ狂ったかと思ったが……\x02\x03",

            "#11102Fなかなかの策士じゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 500)
    Sleep(150)

    #C0105
    ChrTalk(
        0x101,
        (
            "#00006F#5Pあんたこそ\x01",
            "迫真の演技だったよ。\x02\x03",

            "#00010Fつッ……\x01",
            "本当に奥歯を折られるとは\x01",
            "思わなかったけどね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 500)

    #C0106
    ChrTalk(
        0x10B,
        (
            "#11100F#11Pフン、おかげで\x01",
            "それっぽくなっただろうが。\x02\x03",

            "#11103F……約束通り、ここから\x01",
            "出るまでは協力してやろう。\x02\x03",

            "#11101Fで、どうするつもりだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00003F#5Pここは拘置所の３階……\x01",
            "詰めている兵士も少ないはずだ。\x02\x03",

            "#00013F何とか巡回を突破して\x01",
            "１階の出口から脱出しよう！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x10B,
        (
            "#11104F#11Pクク、いいだろう。\x02\x03",

            "#11107F久々に俺も……\x01",
            "暴れさせてもらうとするか！\x02",
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
            "ロイドは急ごしらえで造った\x01",
            "パイプトンファーを装備した。\x02",
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
            "ガルシアがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エニグマⅡを奪われているため、\x01",
            "アーツを使用することが出来ません。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "また、アイテムも全て奪われたので\x01",
            "ＨＰには気をつけてください。\x07\x00\x02",
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
    AddItemNumber(0x1, 1)
    AddItemNumber(0x4, 1)
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

    # Function_11_107C end

    def Function_12_45C3(): pass

    label("Function_12_45C3")


    def lambda_45C8():
        OP_96(0xFE, 0xFFFE2B40, 0x0, 0x7148, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45C8)
    Sleep(3000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_45C3 end

    def Function_13_45F0(): pass

    label("Function_13_45F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4616")
    OP_A6(0xFE, 0x0, 0x23, 0x1F4, 0x1388)
    Sleep(1000)
    Jump("Function_13_45F0")

    label("loc_4616")

    Return()

    # Function_13_45F0 end

    def Function_14_4617(): pass

    label("Function_14_4617")


    def lambda_461C():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_461C)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x10B, 500)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_4617 end

    def Function_15_464B(): pass

    label("Function_15_464B")


    def lambda_4650():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4650)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x10B, 500)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_464B end

    def Function_16_4685(): pass

    label("Function_16_4685")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_4699():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4699)
    WaitChrThread(0xFE, 1)

    def lambda_46B2():
        TurnDirection(0xFE, 0x10B, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46B2)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_4685 end

    def Function_17_46C7(): pass

    label("Function_17_46C7")

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

    # Function_17_46C7 end

    def Function_18_470D(): pass

    label("Function_18_470D")

    Sound(802, 0, 100, 0)
    Sleep(150)

    def lambda_471B():
        OP_98(0xFE, 0x0, 0xFFFFFDA8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_471B)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(811, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_18_470D end

    def Function_19_4749(): pass

    label("Function_19_4749")

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

    # Function_19_4749 end

    def Function_20_4785(): pass

    label("Function_20_4785")

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
        "#11Pごふっ……\x05\x02",
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

    def lambda_492E():
        OP_98(0xFE, 0x0, 0xFFFFFD12, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_492E)
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

    # Function_20_4785 end

    def Function_21_4990(): pass

    label("Function_21_4990")

    OP_68(-79500, 1500, 35150, 500)
    MoveCamera(157, 22, 0, 500)
    SetCameraDistance(18500, 500)
    Fade(250)

    def lambda_49BF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49BF)
    Sleep(150)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x10B, 0x20)
    ClearChrFlags(0x10B, 0x2)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_49E3():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_49E3)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xFE, 2)
    OP_0D()
    OP_6F(0x79)
    #Sound(2820, 255, 100, 0)    #voice#Garcia

    #C0114
    ChrTalk(
        0x10B,
        "#11107F#4S#5Pらああっ！\x05\x02",
    )

    Sound(534, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-82180, 1800, 31820, 500)
    SetCameraDistance(23500, 500)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)

    def lambda_4A60():
        OP_9B(0x1, 0xFE, 0x0, 0x4B0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A60)
    Sleep(100)
    CancelBlur(500)
    Sound(815, 0, 100, 0)
    OP_82(0xFA, 0x1F4, 0x2710, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 22)

    #C0115
    ChrTalk(
        0x8,
        "#11Pがはっ……！\x05\x02",
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

    def lambda_4BBD():
        OP_98(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BBD)
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

    # Function_21_4990 end

    def Function_22_4C0D(): pass

    label("Function_22_4C0D")

    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_22_4C0D end

    def Function_23_4C30(): pass

    label("Function_23_4C30")

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

    # Function_23_4C30 end

    def Function_24_4C97(): pass

    label("Function_24_4C97")

    Sound(882, 0, 100, 0)
    Sleep(2600)
    Sound(882, 0, 80, 0)

    label("loc_4CA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CCB")
    Sleep(3800)
    Sound(882, 0, 40, 0)
    Sleep(2200)
    Sound(882, 0, 40, 0)
    Sleep(500)
    Jump("loc_4CA6")

    label("loc_4CCB")

    Return()

    # Function_24_4C97 end

    def Function_25_4CCC(): pass

    label("Function_25_4CCC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D09")
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
    Jump("Function_25_4CCC")

    label("loc_4D09")

    Return()

    # Function_25_4CCC end

    def Function_26_4D0A(): pass

    label("Function_26_4D0A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D47")
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
    Jump("Function_26_4D0A")

    label("loc_4D47")

    Return()

    # Function_26_4D0A end

    def Function_27_4D48(): pass

    label("Function_27_4D48")

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
            "……あいつら\x01",
            "いったい何をしてるんだ？\x05\x02",
        )
    )

    OP_6F(0x79)
    OP_68(34500, 1000, -1000, 4000)

    #C0117
    ChrTalk(
        0xB,
        (
            "#11Pこっちは早く引継ぎして\x01",
            "帰りたいってのに……\x05\x02",
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
        "#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xB,
        "#11Pお前たちは！\x02",
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

    def lambda_505E():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_505E)

    def lambda_5073():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_5073)

    #C0120
    ChrTalk(
        0x10B,
        "#11107F#5P遅えッ！\x05\x02",
    )


    #C0121
    ChrTalk(
        0x101,
        "#00007F#6P#N行くぞ……！\x05\x02",
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

    # Function_27_4D48 end

    def Function_28_5104(): pass

    label("Function_28_5104")


    def lambda_5109():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5109)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_5104 end

    def Function_29_5150(): pass

    label("Function_29_5150")

    Sleep(1000)

    def lambda_5158():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5158)
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

    # Function_29_5150 end

    def Function_30_51CD(): pass

    label("Function_30_51CD")

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
        "#5P#30Wぐっ……貴様ら……\x02",
    )

    CloseMessageWindow()

    def lambda_52D3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_52D3)
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
        "#11P#30Wに、逃がすものか……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25500, 1000)

    def lambda_5337():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5337)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xB, 0x2)
    OP_0D()
    WaitChrThread(0xB, 2)
    Sleep(500)

    def lambda_536A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_536A)
    Sleep(150)
    Fade(250)
    Sound(804, 0, 100, 0)
    OP_0D()
    WaitChrThread(0xB, 2)

    def lambda_5396():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5396)
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
            "#00010F#6Pくっ、エニグマを使った\x01",
            "緊急警報システムか……！\x02",
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
            "#11104F#5Pクク……\x01",
            "さぁて、どうする？\x02",
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
            "#00007F#12P想定内だ……\x01",
            "このまま強引に突破する！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x10B,
        "#11102F#5Pハハ、いいだろう！\x02",
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

    # Function_30_51CD end

    def Function_31_5582(): pass

    label("Function_31_5582")

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

    # Function_31_5582 end

    def Function_32_55E9(): pass

    label("Function_32_55E9")

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
        "……面会時間は１０分ほどだ。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xE,
        (
            "今回は相手が怪我人なので、\x01",
            "特別措置として部屋での面会を\x01",
            "許可することになったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xE,
        (
            "直接、相手に接触したり物を渡すこと、\x01",
            "騒ぎを起こすことは禁止する。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#12P#00000Fええ、わかりました。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        "うむ、では……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    #C0133
    ChrTalk(
        0xE,
        "#11P──ガルシア、面会だ！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(120, 10, -1, -1)
    SetChrName("ガルシアの声")

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……いいぜ、入りな。\x07\x00\x02",
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

    def lambda_5931():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5931)
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
        "#6P#00000Fガルシア……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        (
            "#11100Fクク、また会ったな小僧。\x02\x03",

            "#11104Fお仲間と再会できたようでなによりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#6P#00305Fありゃ、オッサン。\x01",
            "起き上がって平気なのか？\x02\x03",

            "#00303Fなんでも国防軍と派手にやりあって、\x01",
            "かなり消耗したって聞いたんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xD,
        (
            "#11103Fフン、平気ってほどでもねえ。\x01",
            "何せ素手でライフルやハルバードと\x01",
            "やり合わせてもらったからな。\x02\x03",

            "#11101Fざまあねえが……\x01",
            "起き上がるのがやっとってとこだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D33")

    #C0139
    ChrTalk(
        0x10A,
        (
            "#6P#00600Fフン、それにしては\x01",
            "余裕を感じさせるじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC4")

    label("loc_5D33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D7F")

    #C0140
    ChrTalk(
        0x109,
        (
            "#6P#10102Fそ、それにしては\x01",
            "余裕を感じさせますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC4")

    label("loc_5D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DC4")

    #C0141
    ChrTalk(
        0x106,
        (
            "#6P#10701Fそれにしては\x01",
            "余裕を感じさせますが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E18")

    #C0142
    ChrTalk(
        0x105,
        (
            "#6P#10402Fフフ、さすがは\x01",
            "《キリングベア》といった所だね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC9")

    label("loc_5E18")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E82")

    #C0143
    ChrTalk(
        0x106,
        (
            "#6P#10703F西風の旅団の《殺人熊#6Rキリングベア#》、\x01",
            "さすがと言った所でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC9")

    label("loc_5E82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EC9")

    #C0144
    ChrTalk(
        0x109,
        (
            "#6P#10106Fさすが、元猟兵というか\x01",
            "なんと言うか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC9")


    #C0145
    ChrTalk(
        0x103,
        (
            "#6P#00200Fまあ、どちらにしろ当分は\x01",
            "動けなさそうですけど……\x02",
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
            "#6P#00001F……ガルシア、あんたには\x01",
            "いくら礼を言っても足りない。\x02\x03",

            "#00003Fあの時、あんたが拘置所の脱出に\x01",
            "手を貸してくれなかったら……\x02\x03",

            "#00000F仲間達と再会して、\x01",
            "ここまでたどり着けることも\x01",
            "きっとなかったと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        "#6P#00102Fロイド……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xD,
        (
            "#11101F……ヘッ、そんなことを言うために\x01",
            "わざわざ面会に来やがったってか？\x02\x03",

            "#11103Fお前との馴れ合いは、\x01",
            "拘置所のゲートを出たところで\x01",
            "終わっていたはずだ。\x02\x03",

            "#11102F俺にとっちゃ、てめぇは\x01",
            "組織を潰したいけ好かない野郎……\x01",
            "それは今も変わらないんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#6P#00004F……それでも\x01",
            "一言礼を言わせてほしい。\x02\x03",

            "#00000Fありがとう、ガルシア。\x01",
            "今こうしていられるのは\x01",
            "あんたのおかげだ。\x02\x03",

            "#00000F今回の一連の事件、\x01",
            "必ず真実に辿り着いて、\x01",
            "クロスベルを守ってみせるよ。\x02",
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
            "#11103Fケッ……\x01",
            "胸糞悪ィものを思い出しちまった。\x02\x03",

            "どんな事があっても、何度退けても、\x01",
            "“諦めず”に食い下がってくる\x01",
            "呆れるほどしつこい野郎の目……\x02\x03",

            "#11102Fバニングス……\x01",
            "てめぇは間違いなくガイの弟だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#6P#00305Fオッサン……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#6P#00004F……ハハ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xD,
        (
            "#11103F……チッ。\x01",
            "ガラにもねえことを\x01",
            "言っちまったようだ。\x02\x03",

            "#11101Fお前ら、こんな所で\x01",
            "チンタラおしゃべりを\x01",
            "してる暇なんかねえんだろう。\x02\x03",

            "#11103F……とっとと失せるんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#6P#00004F……ああ、分かってるさ。\x02\x03",

            "#00000Fみんな、そろそろ行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6000", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_32_55E9 end

    def Function_33_6417(): pass

    label("Function_33_6417")


    def lambda_641C():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_641C)

    def lambda_6436():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6436)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_644F():
        OP_95(0xFE, 0, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_644F)
    WaitChrThread(0xFE, 1)

    def lambda_646D():
        OP_95(0xFE, 2000, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_646D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(5000)

    def lambda_6495():
        OP_95(0xFE, 0, 0, 31000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6495)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_6417 end

    def Function_34_64B6(): pass

    label("Function_34_64B6")


    def lambda_64BB():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64BB)

    def lambda_64D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64D5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_64EE():
        OP_95(0xFE, -1370, 0, 39290, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64EE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_34_64B6 end

    def Function_35_650F(): pass

    label("Function_35_650F")


    def lambda_6514():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6514)

    def lambda_652E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_652E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6547():
        OP_95(0xFE, -160, 0, 39190, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6547)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_35_650F end

    def Function_36_6568(): pass

    label("Function_36_6568")


    def lambda_656D():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_656D)

    def lambda_6587():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6587)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_65A0():
        OP_95(0xFE, -1240, 0, 38210, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65A0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_36_6568 end

    def Function_37_65C1(): pass

    label("Function_37_65C1")


    def lambda_65C6():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65C6)

    def lambda_65E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_65E0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_65F9():
        OP_95(0xFE, 0, 0, 38000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65F9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_37_65C1 end

    def Function_38_661A(): pass

    label("Function_38_661A")


    def lambda_661F():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_661F)

    def lambda_6639():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6639)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6652():
        OP_95(0xFE, -300, 0, 36920, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6652)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_38_661A end

    def Function_39_6673(): pass

    label("Function_39_6673")


    def lambda_6678():
        OP_95(0xFE, 0, 0, 29000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6678)

    def lambda_6692():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6692)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_66AB():
        OP_95(0xFE, -1470, 0, 36720, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_66AB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_6673 end

    def Function_40_66CC(): pass

    label("Function_40_66CC")

    OP_96(0xFE, 0x3E8, 0x96, 0x3E8, 0x7D0, 0x0)

    def lambda_66E5():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_66E5)
    Sleep(100)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_40_66CC end

    SaveToFile()

Try(main)
