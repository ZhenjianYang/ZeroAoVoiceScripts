from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t6051.bin",                # FileName
        "t6051",                    # MapName
        "t6051",                    # Location
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
        "t6051",                  # 0
        "国防军士兵",             # 1
        "国防军士兵",             # 2
        "国防军士兵",             # 3
        "国防军士兵",             # 4
        "国防军士兵",             # 5
        "国防军队长",             # 6
        "国防军士兵",             # 7
        "国防军士兵",             # 8
        "国防军士兵",             # 9
        "国防军士兵",             # 10
        "剧情用军犬",             # 11
        "剧情用军犬",             # 12
        "剧情用军犬",             # 13
        "SE控制",                 # 14
        "BT6010",                 # 15
        "BT6020",                 # 16
        "BT6030",                 # 17
    ))

    ATBonus("ATBonus_480", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_540", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_544", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_548", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_550", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_520", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_524", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_528", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_52C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_530", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_534", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_538", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_53C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_560", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_570", 9, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_57C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 12, 14, 180)

    # monster count: 0

    # event battle count: 3

    BattleInfo(
        "BattleInfo_5A0", 0x004A, 3, 6, 45, 3, 3, 30, 0, "BT6010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80800.dat", "ms80800.dat", "ms41400.dat", "ms41500.dat", 0, 0, 0, 0, "MonsterBattlePostion_540", "MonsterBattlePostion_520", "ed7540", "ed7453", "ATBonus_480"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5E4", 0x004A, 3, 6, 45, 3, 3, 30, 0, "BT6020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41500.dat", "ms41400.dat", "ms41400.dat", "ms80800.dat", "ms80800.dat", 0, 0, 0, "MonsterBattlePostion_560", "MonsterBattlePostion_520", "ed7540", "ed7453", "ATBonus_480"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_628", 0x004A, 3, 6, 45, 3, 3, 30, 0, "BT6030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41400.dat", "ms41400.dat", "ms41400.dat", "ms41500.dat", "ms41500.dat", "ms80800.dat", "ms80800.dat", "ms80800.dat", "MonsterBattlePostion_580", "MonsterBattlePostion_520", "ed7540", "ed7453", "ATBonus_480"),
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

    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  70.0,                  3.0,                   0.0,                   144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -8.75,                 -1.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 33,  143.0,                 3.5,                   0.0,                   20.25,                 [0.6666666865348816,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -95.33333587646484,    -0.5833333730697632,   -0.0,                  1.0])

    DeclActor(149250,  0,       3250,    1200,    149250,  1500,    3250,    0x007C, 0,  31, 0x0000)
    DeclActor(147000,  0,       -3500,   1200,    147000,  1500,    -3500,   0x007C, 0,  32, 0x0000)
    DeclActor(37000,   0,       59000,   1200,    37000,   1000,    59000,   0x007C, 0,  2,  0x0000)
    DeclActor(-12500,  0,       14000,   1200,    -12500,  1000,    14000,   0x007C, 0,  3,  0x0000)
    DeclActor(19000,   0,       4500,    1200,    19000,   1200,    3750,    0x007C, 0,  5,  0x0000)
    DeclActor(7000,    0,       -2500,   1200,    7000,    1200,    -2000,   0x007C, 0,  6,  0x0000)
    DeclActor(-5000,   0,       -2500,   1200,    -5000,   1200,    -2000,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1780, 0)                                       # 0

    ScpFunction((
        "Function_0_6F4",          # 00, 0
        "Function_1_725",          # 01, 1
        "Function_2_8A9",          # 02, 2
        "Function_3_983",          # 03, 3
        "Function_4_ABE",          # 04, 4
        "Function_5_B3B",          # 05, 5
        "Function_6_F1C",          # 06, 6
        "Function_7_1231",         # 07, 7
        "Function_8_16C7",         # 08, 8
        "Function_9_1A34",         # 09, 9
        "Function_10_1A50",        # 0A, 10
        "Function_11_1A6C",        # 0B, 11
        "Function_12_1A86",        # 0C, 12
        "Function_13_1CA0",        # 0D, 13
        "Function_14_1D07",        # 0E, 14
        "Function_15_20DA",        # 0F, 15
        "Function_16_213A",        # 10, 16
        "Function_17_2183",        # 11, 17
        "Function_18_21CA",        # 12, 18
        "Function_19_21FF",        # 13, 19
        "Function_20_2211",        # 14, 20
        "Function_21_225D",        # 15, 21
        "Function_22_22BE",        # 16, 22
        "Function_23_253D",        # 17, 23
        "Function_24_25D7",        # 18, 24
        "Function_25_2FD7",        # 19, 25
        "Function_26_3469",        # 1A, 26
        "Function_27_34A0",        # 1B, 27
        "Function_28_34C9",        # 1C, 28
        "Function_29_34E8",        # 1D, 29
        "Function_30_3504",        # 1E, 30
        "Function_31_3604",        # 1F, 31
        "Function_32_37E0",        # 20, 32
        "Function_33_399C",        # 21, 33
    ))


    def Function_0_6F4(): pass

    label("Function_0_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A")
    Event(0, 8)
    Jump("loc_724")

    label("loc_70A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_724")
    Event(0, 14)

    label("loc_724")

    Return()

    # Function_0_6F4 end

    def Function_1_725(): pass

    label("Function_1_725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_741")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_753")

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_753")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_753")

    OP_52(0x10B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78C")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_78C")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A4")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_7A4")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BA")
    OP_66(0x0, 0x1)

    label("loc_7BA")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0")
    OP_66(0x1, 0x1)

    label("loc_7D0")

    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F6")
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_807")
    Call(0, 13)

    label("loc_807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_818")
    Call(0, 23)

    label("loc_818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_829")
    Call(0, 30)

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_852")
    OP_70(0xA, 0x2D)
    SetMapObjFlags(0xA, 0x2)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jump("loc_868")

    label("loc_852")

    OP_70(0xA, 0x0)
    ClearMapObjFlags(0xA, 0x2)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87B")
    OP_70(0xC, 0x0)
    Jump("loc_87F")

    label("loc_87B")

    OP_70(0xC, 0x1E)

    label("loc_87F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892")
    OP_70(0xD, 0x0)
    Jump("loc_896")

    label("loc_892")

    OP_70(0xD, 0x1E)

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A8")
    OP_70(0x0, 0xA)

    label("loc_8A8")

    Return()

    # Function_1_725 end

    def Function_2_8A9(): pass

    label("Function_2_8A9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_954")
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

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了１０个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('大回复药', 10)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_971")

    label("loc_954")


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

    label("loc_971")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_8A9 end

    def Function_3_983(): pass

    label("Function_3_983")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A75")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('还魂粉', 1)"), scpexpr(EXPR_END)), "loc_A06")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '还魂粉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F6, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_A70")

    label("loc_A06")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '还魂粉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '还魂粉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A70")

    Jump("loc_AB2")

    label("loc_A75")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_AB2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_983 end

    def Function_4_ABE(): pass

    label("Function_4_ABE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B14")

    #C0006
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0007
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
    SetScenarioFlags(0x0, 0)
    Jump("loc_B37")

    label("loc_B14")

    SetChrName("")

    #A0008
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

    label("loc_B37")

    TalkEnd(0xFE)
    Return()

    # Function_4_ABE end

    def Function_5_B3B(): pass

    label("Function_5_B3B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAE")
    SetMessageWindowPos(120, 10, -1, -1)
    SetChrName("口气傲慢的声音")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "这、这骚乱……\x01",
            "是你们引起的吗！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x101,
        (
            "#00005F这、这声音……\x01",
            "难道是马尔克尼会长？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("马尔克尼的声音")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "警、警察小鬼吗！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("马尔克尼的声音")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "加尔西亚，你为什么会跟他一起……！？\x01",
            "如、如果要逃，把我也带上啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0013
    ChrTalk(
        0x10B,
        (
            "#11103F……会长，实在抱歉，\x01",
            "我不能那样做。\x02\x03",

            "#11101F我很快就会回来，\x01",
            "请您老老实实地待在里面吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("马尔克尼的声音")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "喂！喂！等等！加尔西亚！！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0015
    ChrTalk(
        0x101,
        (
            "#00011F（没、没想到他这么有精神……）\x02\x03",

            "#00006F（……那种傲慢自大的性格\x01",
            "  好像完全没有改变。）\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x10B,
        (
            "#11100F（呵呵，别这么说。）\x02\x03",

            "#11104F（会长是我的恩人，\x01",
            "  多亏他，我才能得到鲁巴彻\x01",
            "  这个舒适的容身之所。）\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#00005F（……看来你们之间发生过不少事啊。）\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10B,
        (
            "#11103F（……哼，不小心\x01",
            "  说了些不合时宜的话。）\x02\x03",

            "#11101F（赶紧动身吧，小鬼。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 1)
    Jump("loc_F18")

    label("loc_EAE")

    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("马尔克尼的声音")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "加尔西亚，还有那个警察小鬼！！\x01",
            "如、如果要逃，把我也带上啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_F18")

    TalkEnd(0xFF)
    Return()

    # Function_5_B3B end

    def Function_6_F1C(): pass

    label("Function_6_F1C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1180")
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("胆怯的声音")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "到、到底发生了什么事！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("胆怯的声音")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "守卫……都跑到哪里去了！？\x01",
            "快、快点处理一下这个事态啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0022
    ChrTalk(
        0x10B,
        (
            "#11103F（……这间牢房里的人\x01",
            "  应该是哈尔特曼那家伙。）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00001F（哈尔特曼原议长……自阿尔泰尔据点的\x01",
            "  行动之后，这还是第一次遇到他呢。）\x02\x03",

            "#00003F（他的性格好像\x01",
            "  变得很怯懦……）\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x10B,
        (
            "#11104F（自从被关进拘留所之后，\x01",
            "  他一直都是那副德性。）\x02\x03",

            "#11102F（大概是因为失去了财富和地位，\x01",
            "  已经没有任何可以支撑\x01",
            "  自己的东西了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00003F（……虽然有点担心……\x01",
            "  但这也是他应受的惩罚。）\x02\x03",

            "#00001F（……还是赶快出发吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 2)
    Jump("loc_122D")

    label("loc_1180")

    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("哈尔特曼的声音")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "到、到底发生了什么事！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("哈尔特曼的声音")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "守卫……都跑到哪里去了！？\x01",
            "快、快点处理一下这个事态啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_122D")

    TalkEnd(0xFF)
    Return()

    # Function_6_F1C end

    def Function_7_1231(): pass

    label("Function_7_1231")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1604")
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("平静的声音")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "外面的人难道是……\x01",
            "罗伊德吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("平静的声音")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "原来如此，这场混乱是你引起的啊……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x101,
        (
            "#00005F这声音……难道是\x01",
            "阿奈斯特先生吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x10B,
        (
            "#11101F……是前市长秘书啊。\x01",
            "说起来，他确实被\x01",
            "关押在这里了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("阿奈斯特的声音")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "听说你被抓到这里时，\x01",
            "我真是大吃一惊……\x01",
            "……哈哈，能与你再会，我真的很高兴。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0033
    ChrTalk(
        0x101,
        (
            "#00002F太好了……看来你已经\x01",
            "不再受『真知』的\x01",
            "影响了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("阿奈斯特的声音")

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "嗯，多亏你们的帮助。\x01",
            "实在抱歉，我以前做过很多……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("阿奈斯特的声音")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……算了，还是不说这些了，\x01",
            "现在不是慢慢道歉的时候。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("阿奈斯特的声音")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "等我刑满离开之后，\x01",
            "一定会正式向你和\x01",
            "艾莉他们致歉的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("阿奈斯特的声音")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不用管我，你们赶快走吧。\x01",
            "……愿女神保佑你们。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0038
    ChrTalk(
        0x101,
        "#00004F……谢谢。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x10B,
        (
            "#11103F……聊完了吗？\x01",
            "现在可没时间磨蹭哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00001F嗯……立刻动身吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 3)
    Jump("loc_16C3")

    label("loc_1604")

    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("阿奈斯特的声音")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "等我刑满离开之后，\x01",
            "一定会正式向你和\x01",
            "艾莉他们致歉的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("阿奈斯特的声音")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不用管我，你们赶快走吧。\x01",
            "……愿女神保佑你们。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_16C3")

    TalkEnd(0xFF)
    Return()

    # Function_7_1231 end

    def Function_8_16C7(): pass

    label("Function_8_16C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch41550.itc", 0x20)
    LoadChrToIndex("chr/ch41551.itc", 0x21)
    LoadChrToIndex("monster/ch80850.itc", 0x22)
    LoadChrToIndex("monster/ch80851.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch04152.itc", 0x25)
    SetChrPos(0x101, 21200, 0, 200, 270)
    SetChrPos(0x10B, 21500, 0, 1600, 270)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 4500, 0, 400, 90)
    SetChrFlags(0x8, 0x40)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 4500, 0, 1600, 90)
    SetChrFlags(0x9, 0x40)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 7000, 0, 250, 90)
    SetChrFlags(0x12, 0x20)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 9)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 7000, 0, 1750, 90)
    SetChrFlags(0x13, 0x20)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 9)
    OP_68(21400, 1000, 1000, 0)
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
    OP_68(6850, 1000, 1000, 2000)
    MoveCamera(45, 23, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(25500, 2000)
    OP_6F(0x79)

    #C0043
    ChrTalk(
        0x8,
        "#6P在这里！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        "你们两个！不许动！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(12400, 1000, 1000, 0)
    MoveCamera(45, 23, 0, 0)
    SetCameraDistance(33500, 0)
    OP_68(21400, 1000, 1000, 1800)
    SetCameraDistance(25500, 1800)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)

    def lambda_1920():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1920)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_193D():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_193D)
    EndChrThread(0x12, 0x0)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 10)
    BeginChrThread(0x15, 1, 0, 11)

    def lambda_1975():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1975)
    EndChrThread(0x13, 0x0)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 10)

    def lambda_19A7():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_19A7)
    Sleep(200)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0x25)
    SetChrSubChip(0x10B, 0x0)
    Sleep(50)
    SetChrSubChip(0x10B, 0x1)
    OP_6F(0x79)
    SetCameraDistance(23500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x15, 0x1)
    Battle("BattleInfo_5A0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 12)
    Return()

    # Function_8_16C7 end

    def Function_9_1A34(): pass

    label("Function_9_1A34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A4F")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_9_1A34")

    label("loc_1A4F")

    Return()

    # Function_9_1A34 end

    def Function_10_1A50(): pass

    label("Function_10_1A50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A6B")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_10_1A50")

    label("loc_1A6B")

    Return()

    # Function_10_1A50 end

    def Function_11_1A6C(): pass

    label("Function_11_1A6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A85")
    Sound(845, 0, 100, 0)
    Sleep(500)
    Jump("Function_11_1A6C")

    label("loc_1A85")

    Return()

    # Function_11_1A6C end

    def Function_12_1A86(): pass

    label("Function_12_1A86")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 21400, 0, 400, 270)
    SetChrPos(0x10B, 21400, 0, 1600, 270)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Call(0, 13)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_68(21070, 1100, 1110, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(24500, 1000)
    OP_6F(0x79)
    OP_0D()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00006F#11P……开始使用军犬了啊。\x02\x03",

            "#00008F在警备队时期，\x01",
            "并没有投入过这种东西啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x10B,
        (
            "#11104F#5P哼，恐怕是利用了\x01",
            "我们鲁巴彻的训练方式。\x02\x03",

            "#11102F可能是通过药物\x01",
            "来操控的。\x02\x03",

            "#11109F哼哼，这些家伙\x01",
            "真是越来越无耻了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 500)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00010F#12P啧……用不着你来说！\x02\x03",

            "#00008F（这应该不是索妮亚司令\x01",
            "  或道格拉斯副司令的意思……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 21400, 0, 1000, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 6)
    EventEnd(0x5)
    Return()

    # Function_12_1A86 end

    def Function_13_1CA0(): pass

    label("Function_13_1CA0")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 18400, 0, -200, 45)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 17400, 0, 2250, 90)
    Return()

    # Function_13_1CA0 end

    def Function_14_1D07(): pass

    label("Function_14_1D07")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch41450.itc", 0x20)
    LoadChrToIndex("chr/ch41451.itc", 0x21)
    LoadChrToIndex("chr/ch41550.itc", 0x22)
    LoadChrToIndex("chr/ch41551.itc", 0x23)
    LoadChrToIndex("monster/ch80850.itc", 0x24)
    LoadChrToIndex("monster/ch80851.itc", 0x25)
    LoadChrToIndex("chr/ch00050.itc", 0x26)
    LoadChrToIndex("chr/ch04152.itc", 0x27)
    SetChrPos(0x101, -55500, 0, -1000, 270)
    SetChrPos(0x10B, -55500, 0, -1000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -61600, 0, 2200, 270)
    SetChrFlags(0xA, 0x40)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -61600, 0, 3600, 225)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -63000, 0, 2500, 90)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -63150, 0, 6800, 180)
    SetChrFlags(0x12, 0x20)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 9)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -61950, 0, 9700, 180)
    SetChrFlags(0x13, 0x20)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 9)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x10)
    OP_70(0x8, 0x0)
    OP_68(-62100, 1000, 3900, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(25500, 1000)
    OP_6F(0x79)
    OP_0D()
    Sound(103, 0, 100, 0)
    Sound(121, 0, 50, 0)
    Sleep(300)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-60800, 1400, 950, 2000)
    MoveCamera(60, 23, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(25500, 2000)
    BeginChrThread(0x101, 3, 0, 15)
    BeginChrThread(0x10B, 3, 0, 16)

    def lambda_1F79():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1F79)
    Sleep(50)

    def lambda_1F89():
        OP_93(0xB, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1F89)
    Sleep(50)

    def lambda_1F99():
        OP_93(0xC, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1F99)
    Sleep(50)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x10B, 3)
    Sleep(200)

    #C0048
    ChrTalk(
        0xA,
        "#5P加、加尔西亚！？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        "#5P还有那个支援科的年轻人！？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xC,
        (
            "#6P可恶！\x01",
            "把他们两个都抓起来！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    OP_68(-59500, 1400, -1150, 1200)
    MoveCamera(36, 23, 0, 1200)
    BeginChrThread(0xA, 3, 0, 19)
    BeginChrThread(0xB, 3, 0, 17)
    BeginChrThread(0xC, 3, 0, 18)
    BeginChrThread(0x12, 3, 0, 20)
    BeginChrThread(0x13, 3, 0, 21)
    Sleep(1000)
    SetCameraDistance(22500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x15, 0x1)
    Battle("BattleInfo_5E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 22)
    Return()

    # Function_14_1D07 end

    def Function_15_20DA(): pass

    label("Function_15_20DA")

    OP_93(0xFE, 0xF0, 0x0)
    OP_74(0x8, 0xA)
    OP_71(0x8, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x8)
    OP_74(0x8, 0x1E)
    Sleep(100)

    def lambda_2100():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2100)
    OP_96(0xFE, 0xFFFF19BA, 0x0, 0xFFFFF79A, 0x1388, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    WaitChrThread(0xFE, 2)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_15_20DA end

    def Function_16_213A(): pass

    label("Function_16_213A")

    Sleep(1300)

    def lambda_2142():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2142)
    OP_95(0xFE, -57850, 0, -1050, 5000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0x10B, 0x27)
    SetChrSubChip(0x10B, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x10B, 0x1)
    Return()

    # Function_16_213A end

    def Function_17_2183(): pass

    label("Function_17_2183")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -60700, 0, 4700, 5000, 0x1)
    OP_95(0xFE, -58250, 0, 4700, 5000, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x1388, 0x1)
    Return()

    # Function_17_2183 end

    def Function_18_21CA(): pass

    label("Function_18_21CA")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1388, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    Return()

    # Function_18_21CA end

    def Function_19_21FF(): pass

    label("Function_19_21FF")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_19_21FF end

    def Function_20_2211(): pass

    label("Function_20_2211")

    Sleep(300)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x15, 1, 0, 11)
    BeginChrThread(0xFE, 0, 0, 10)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1388, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    Return()

    # Function_20_2211 end

    def Function_21_225D(): pass

    label("Function_21_225D")

    Sleep(600)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 10)
    OP_95(0xFE, -63150, 0, 6800, 5000, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1388, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    Return()

    # Function_21_225D end

    def Function_22_22BE(): pass

    label("Function_22_22BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch04152.itc", 0x1F)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -58950, 0, -2350, 270)
    SetChrChipByIndex(0x10B, 0x1F)
    SetChrSubChip(0x10B, 0x1)
    SetChrPos(0x10B, -57850, 0, -850, 270)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Call(0, 23)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_68(-59800, 1400, -1100, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(23000, 1000)
    OP_6F(0x79)
    OP_0D()

    #C0051
    ChrTalk(
        0x101,
        "#00015F#11P唔……呼……呼……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x10B, 0x0)
    Sleep(180)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    OP_0D()
    Sleep(200)
    TurnDirection(0x10B, 0x101, 500)

    #C0052
    ChrTalk(
        0x10B,
        (
            "#11102F#5P呵呵……\x01",
            "你已经气喘吁吁了啊。\x02\x03",

            "就凭这种体质，\x01",
            "难道还想逃离这里吗？\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    TurnDirection(0x101, 0x10B, 500)

    #C0053
    ChrTalk(
        0x101,
        (
            "#00006F#12P如果只有我一个人，\x01",
            "自然无法成功……\x02\x03",

            "#00000F但只要有你的帮助，\x01",
            "就有可能逃离拘留所。\x02\x03",

            "我要利用一切可以利用的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x10B,
        (
            "#11104F#5P……哼，\x01",
            "你好像已经豁出去了啊。\x02\x03",

            "#11107F好……\x01",
            "就趁现在冲出去吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, -59350, 0, -1450, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 7)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_22_22BE end

    def Function_23_253D(): pass

    label("Function_23_253D")

    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, -58400, 0, 1950, 180)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, -63350, 0, -1400, 135)
    SetChrChipByIndex(0xC, 0x0)
    SetChrSubChip(0xC, 0x3)
    ClearChrFlags(0xC, 0x80)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, -61500, 0, -3350, 90)
    Return()

    # Function_23_253D end

    def Function_24_25D7(): pass

    label("Function_24_25D7")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch41550.itc", 0x20)
    LoadChrToIndex("chr/ch41551.itc", 0x21)
    LoadChrToIndex("monster/ch80850.itc", 0x22)
    LoadChrToIndex("monster/ch80851.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch04150.itc", 0x25)
    SetChrPos(0x101, 70300, 0, 3500, 135)
    SetChrPos(0x10B, 69100, 0, 3500, 135)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 92000, 0, 1000, 180)
    SetChrFlags(0xD, 0x40)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 91300, 0, -1500, 0)
    SetChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 92700, 0, -1500, 0)
    SetChrFlags(0xF, 0x40)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 91300, 0, -3000, 0)
    SetChrFlags(0x10, 0x40)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 92700, 0, -3000, 0)
    SetChrFlags(0x11, 0x40)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 96000, 0, 500, 270)
    SetChrFlags(0x12, 0x20)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 9)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 96000, 0, -1000, 270)
    SetChrFlags(0x13, 0x20)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 9)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 96000, 0, -2500, 270)
    SetChrFlags(0x14, 0x20)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 9)
    OP_68(70000, 1000, 3500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetCameraDistance(25500, 1000)
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294C")
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(92000, 1000, -1000, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(25500, 3000)
    OP_6F(0x79)
    SetCameraDistance(24500, 3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(70000, 1000, 3500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_0D()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00013F#5P（人数不少……\x01",
            "  不过，只要能突破这道防线……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x10B,
        (
            "#11100F#5P（哼，直接冲上去，\x01",
            "  把他们全部干掉吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x184, 0)

    label("loc_294C")

    OP_0D()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "直接冲向敌阵\x01",      # 0
            "先做一番准备\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29A1"),
        (1, "loc_2F44"),
        (SWITCH_DEFAULT, "loc_2FD6"),
    )


    label("loc_29A1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(92390, 1000, -960, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0057
    ChrTalk(
        0xD,
        "#5P有两名在押人员企图越狱！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xD,
        (
            "#5P分别为前黑手党干部加尔西亚\x01",
            "和支援科的班宁斯！\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xD,
        (
            "#5P赌上我们国防军的荣耀！\x01",
            "绝不能让他们逃出拘留所！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(260, 30, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    SetChrName("国防军士兵们")

    #A0060
    AnonymousTalk(
        0xFF,
        "#4S是！长官！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0061
    ChrTalk(
        0x10B,
        "#11109F哼……还扯什么荣耀。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2B64():
        OP_93(0xD, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2B64)
    Sleep(50)

    def lambda_2B74():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2B74)
    Sleep(50)

    def lambda_2B84():
        OP_93(0xF, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_2B84)
    Sleep(50)

    def lambda_2B94():
        OP_93(0x10, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2B94)
    Sleep(50)

    def lambda_2BA4():
        OP_93(0x11, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2BA4)
    Sleep(50)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)
    Fade(500)
    SetChrPos(0x101, 78700, 0, -1000, 90)
    SetChrPos(0x10B, 78700, 0, 400, 90)
    OP_68(92000, 1000, 1000, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    OP_68(85500, 1000, 1000, 3000)

    def lambda_2C2E():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C2E)
    Sleep(0)

    def lambda_2C46():
        OP_9B(0x0, 0x10B, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_2C46)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10B, 0)
    OP_6F(0x79)
    OP_0D()

    #C0062
    ChrTalk(
        0xE,
        "#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xD,
        "#11P已、已经来到这一层了！？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    BeginChrThread(0x101, 0, 0, 28)
    OP_0D()

    #C0064
    ChrTalk(
        0x101,
        (
            "#00007F#5P抱歉……\x01",
            "我们必须突破这里！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(908, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0x25)
    SetChrSubChip(0x10B, 0x0)
    BeginChrThread(0x10B, 0, 0, 29)
    OP_0D()

    #C0065
    ChrTalk(
        0x10B,
        (
            "#11102F#5P哼哼，就让我看看你们\x01",
            "那所谓的荣耀是什么货色吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(90000, 1000, 0, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    OP_0D()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    #C0066
    ChrTalk(
        0xD,
        "#11P#4S可恶……大家上！\x02",
    )

    CloseMessageWindow()
    OP_68(85000, 1000, 0, 1000)
    SetCameraDistance(25500, 1000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_2DCF():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2DCF)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)

    def lambda_2DEF():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2DEF)
    Sleep(100)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)

    def lambda_2E0F():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2E0F)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x15, 1, 0, 11)
    BeginChrThread(0x12, 0, 0, 10)

    def lambda_2E46():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E46)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 10)

    def lambda_2E74():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2E74)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 10)

    def lambda_2EA2():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2EA2)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_2EC2():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2EC2)
    SetCameraDistance(20500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x10B, 0x0)
    Battle("BattleInfo_628", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 25)
    Jump("loc_2FD6")

    label("loc_2F44")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_37()
    SetChrPos(0x0, 70000, 0, 5000, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_2FD6")

    label("loc_2FD6")

    Return()

    # Function_24_25D7 end

    def Function_25_2FD7(): pass

    label("Function_25_2FD7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch04150.itc", 0x1F)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 86700, 0, -1000, 90)
    BeginChrThread(0x101, 0, 0, 28)
    SetChrChipByIndex(0x10B, 0x1F)
    SetChrSubChip(0x10B, 0x0)
    SetChrPos(0x10B, 86700, 0, 400, 90)
    BeginChrThread(0x10B, 0, 0, 29)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Call(0, 30)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_68(90500, 1000, 0, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(86890, 1000, 250, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(200)

    #C0067
    ChrTalk(
        0x101,
        "#00006F#5P呼……总算赢了。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0x101, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    EndChrThread(0x10B, 0x0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10B, 0xFF)
    SetChrSubChip(0x10B, 0x0)
    OP_0D()
    TurnDirection(0x101, 0x10B, 500)
    Sleep(100)

    #C0068
    ChrTalk(
        0x101,
        (
            "#00004F#6P话说回来……\x01",
            "你的战斗力果然很惊人。\x02\x03",

            "#00000F虽然之前也见识过\x01",
            "兰迪和赤色星座首领……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 500)

    #C0069
    ChrTalk(
        0x10B,
        (
            "#11103F#11P哼……\x01",
            "『赤色战鬼』西格蒙德吗？\x02\x03",

            "#11100F我在猎兵时代见过他很多次，\x01",
            "还真是个名副其实的怪物。\x02\x03",

            "听说他的女儿也\x01",
            "是个相当危险的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00001F#6P是啊……单论战斗力，\x01",
            "他们说不定比『结社』的那些家伙还要强。\x02\x03",

            "#00006F但『结社』中也有不少\x01",
            "很厉害的人物……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x10B,
        (
            "#11104F#11P哼哼，你以后恐怕还要\x01",
            "面对那些怪物吧？\x02\x03",

            "#11102F小子，你还真是前途多难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#00006F#6P嗯，确实如此。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(91750, 1800, -4000, 0)
    OP_68(91750, 1000, -4000, 4000)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    BeginChrThread(0x101, 3, 0, 26)
    BeginChrThread(0x10B, 3, 0, 27)
    WaitChrThread(0x101, 3)
    VolumeBGM(0x50, 0x1F4)
    WaitChrThread(0x10B, 3)
    OP_6F(0x79)
    Sound(807, 0, 100, 0)
    Sleep(300)
    VolumeBGM(0x64, 0x7D0)

    #C0073
    ChrTalk(
        0x101,
        (
            "#00001F#11P锁住了……\x02\x03",

            "附近应该有\x01",
            "解锁的装置……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(91750, 1000, -2500, 1000)
    OP_93(0x10B, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x79)

    #C0074
    ChrTalk(
        0x10B,
        (
            "#11104F#5P哈，应该就在那个房间吧。\x02\x03",

            "#11100F赶快解锁，然后逃离这里吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(25150, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, 91400, 0, -4450, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x184, 1)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_25_2FD7 end

    def Function_26_3469(): pass

    label("Function_26_3469")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 90400, 0, -1800, 2300, 0x1)
    OP_95(0xFE, 92070, 0, -6230, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_26_3469 end

    def Function_27_34A0(): pass

    label("Function_27_34A0")

    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(700)
    OP_95(0xFE, 91230, 0, -2860, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_27_34A0 end

    def Function_28_34C9(): pass

    label("Function_28_34C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34E7")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_28_34C9")

    label("loc_34E7")

    Return()

    # Function_28_34C9 end

    def Function_29_34E8(): pass

    label("Function_29_34E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3503")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_29_34E8")

    label("loc_3503")

    Return()

    # Function_29_34E8 end

    def Function_30_3504(): pass

    label("Function_30_3504")

    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xD, 93100, 0, -950, 45)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xE, 90000, 0, 2100, 270)
    SetChrChipByIndex(0xF, 0x0)
    SetChrSubChip(0xF, 0x2)
    ClearChrFlags(0xF, 0x80)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x1)
    SetChrPos(0xF, 89150, 0, -3300, 315)
    SetChrChipByIndex(0x10, 0x0)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x1)
    SetChrPos(0x10, 94350, 0, -3850, 270)
    SetChrChipByIndex(0x11, 0x0)
    SetChrSubChip(0x11, 0x3)
    ClearChrFlags(0x11, 0x80)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x11, 0x1)
    SetChrPos(0x11, 96050, 0, -200, 90)
    Return()

    # Function_30_3504 end

    def Function_31_3604(): pass

    label("Function_31_3604")

    EventBegin(0x0)
    Fade(500)
    OP_68(148250, 1000, 3250, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 148100, 0, 3000, 90)
    SetChrPos(0x10B, 147000, 0, 3250, 90)
    OP_0D()
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x8)
    Sleep(150)
    Sound(139, 0, 100, 0)
    OP_79(0x1)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    OP_0D()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(92000, 1000, -5500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(24500, 2500)
    OP_6F(0x79)
    OP_0D()
    Sound(454, 0, 100, 0)
    Sound(147, 0, 100, 0)
    OP_82(0x0, 0x19, 0x1388, 0x7D0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x2D, 0x0, 0x0, 0x8)
    OP_79(0xA)
    OP_82(0x32, 0x0, 0x1388, 0x1F4)
    ClearMapObjFlags(0xA, 0x2)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(148250, 1000, 3250, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)

    #C0075
    ChrTalk(
        0x101,
        "#00002F#5P成功了……！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x10B,
        "#11100F#5P很好，赶快出去吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 147480, 0, 3020, 270)
    OP_69(0xFF, 0x0)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x184, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DD")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_37DD")

    EventEnd(0x5)
    Return()

    # Function_31_3604 end

    def Function_32_37E0(): pass

    label("Function_32_37E0")

    EventBegin(0x0)
    Fade(500)
    OP_68(147740, 1000, -1680, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 147000, 0, -2300, 180)
    SetChrPos(0x10B, 146700, 0, -1200, 180)
    OP_0D()
    Sleep(300)
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x8)
    OP_79(0x0)
    Sleep(200)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "取回了被夺走的装备、道具\x01",
            "和艾尼格玛Ⅱ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #C0078
    ChrTalk(
        0x101,
        (
            "#00006F#5P太好了……\x01",
            "原来在这里啊。\x02\x03",

            "#00002F回路也都\x01",
            "在里面。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x10B,
        (
            "#11103F#5P喂，赶快出发。\x02\x03",

            "#11100F如果你不想被那些士兵\x01",
            "围住群殴，就别再磨磨蹭蹭的。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#00000F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 147000, 0, -1800, 0)
    OP_69(0xFF, 0x0)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0x184, 3)
    ModifyEventFlags(0, 1, 0x80)
    OP_C7(0x1, 0x0)
    OP_32(0x0, 0x11, 0x0)
    OP_DA(0x2)
    EventEnd(0x5)
    Return()

    # Function_32_37E0 end

    def Function_33_399C(): pass

    label("Function_33_399C")

    EventBegin(0x0)
    Fade(500)
    OP_68(144140, 1000, 3510, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 144000, 0, 3650, 270)
    SetChrPos(0x10B, 145500, 0, 4150, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00005F#5P（话说回来……\x01",
            "  被夺走的装备和物品\x01",
            "  应该都在某处。）\x02\x03",

            "#00008F（说不定……）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(147390, 1000, -2320, 1500)
    SetCameraDistance(23010, 1500)

    def lambda_3A8B():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A8B)
    Sleep(200)

    def lambda_3A9B():
        OP_93(0x10B, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_3A9B)
    Sleep(200)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10B, 0)
    OP_6F(0x79)
    Sleep(500)
    SetChrPos(0x0, 145760, 0, 3760, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_33_399C end

    SaveToFile()

Try(main)
