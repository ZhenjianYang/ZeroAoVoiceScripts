from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "国防軍兵士",             # 1
        "国防軍兵士",             # 2
        "国防軍兵士",             # 3
        "国防軍兵士",             # 4
        "国防軍兵士",             # 5
        "国防軍隊長",             # 6
        "国防軍兵士",             # 7
        "国防軍兵士",             # 8
        "国防軍兵士",             # 9
        "国防軍兵士",             # 10
        "イベント用軍用犬",       # 11
        "イベント用軍用犬",       # 12
        "イベント用軍用犬",       # 13
        "SE制御",                 # 14
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
        "Function_3_991",          # 03, 3
        "Function_4_AE2",          # 04, 4
        "Function_5_B6F",          # 05, 5
        "Function_6_FC4",          # 06, 6
        "Function_7_1325",         # 07, 7
        "Function_8_188D",         # 08, 8
        "Function_9_1BF6",         # 09, 9
        "Function_10_1C12",        # 0A, 10
        "Function_11_1C2E",        # 0B, 11
        "Function_12_1C48",        # 0C, 12
        "Function_13_1EC2",        # 0D, 13
        "Function_14_1F29",        # 0E, 14
        "Function_15_22FA",        # 0F, 15
        "Function_16_235A",        # 10, 16
        "Function_17_23A3",        # 11, 17
        "Function_18_23EA",        # 12, 18
        "Function_19_241F",        # 13, 19
        "Function_20_2431",        # 14, 20
        "Function_21_247D",        # 15, 21
        "Function_22_24DE",        # 16, 22
        "Function_23_278F",        # 17, 23
        "Function_24_2829",        # 18, 24
        "Function_25_3257",        # 19, 25
        "Function_26_3767",        # 1A, 26
        "Function_27_379E",        # 1B, 27
        "Function_28_37C7",        # 1C, 28
        "Function_29_37E6",        # 1D, 29
        "Function_30_3802",        # 1E, 30
        "Function_31_3902",        # 1F, 31
        "Function_32_3AE2",        # 20, 32
        "Function_33_3CDC",        # 21, 33
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95A")
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
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を１０個手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F6, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F6, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_97F")

    label("loc_95A")


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

    label("loc_97F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_8A9 end

    def Function_3_991(): pass

    label("Function_3_991")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A91")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_A1A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F6, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_A8C")

    label("loc_A1A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A8C")

    Jump("loc_AD6")

    label("loc_A91")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_AD6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_991 end

    def Function_4_AE2(): pass

    label("Function_4_AE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B40")

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
            "国防軍兵士は気を失っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B6B")

    label("loc_B40")

    SetChrName("")

    #A0008
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

    label("loc_B6B")

    TalkEnd(0xFE)
    Return()

    # Function_4_AE2 end

    def Function_5_B6F(): pass

    label("Function_5_B6F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F56")
    SetMessageWindowPos(120, 10, -1, -1)
    SetChrName("傲慢そうな声")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "お、お前たち……\x01",
            "この騒ぎはお前たちの仕業か！？\x07\x00\x02",
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
            "#00005Fこ、この声……\x01",
            "もしかして、マルコーニ会長？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("マルコーニの声")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "そ、そこにいるのは警察の小僧！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("マルコーニの声")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "ガルシア、なぜ一緒に……！？\x01",
            "い、行くならワシも連れて行かんか！\x07\x00\x02",
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
            "#11103F……会長、申しわけありませんが\x01",
            "それはできません。\x02\x03",

            "#11101Fすぐに戻りますので、\x01",
            "大人しくしておいてください。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("マルコーニの声")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "お、おい待て！　ガルシアー！！\x07\x00\x02",
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
            "#00011F（い、意外と元気そうだな……）\x02\x03",

            "#00006F（……あの傲慢そうな性格も\x01",
            "  変わってないみたいだし。）\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x10B,
        (
            "#11100F（クク、そう言ってくれるな。）\x02\x03",

            "#11104F（俺にとっちゃ、ルバーチェっつう\x01",
            "  居心地のいい場所を与えてくれた\x01",
            "  恩のある人でもあるんでな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#00005F（……あんた達にも色々あるんだな。）\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10B,
        (
            "#11103F（……フン、柄にもねぇ事を\x01",
            "  口走っちまったようだ。）\x02\x03",

            "#11101F（さっさと行くぞ、小僧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 1)
    Jump("loc_FC0")

    label("loc_F56")

    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("マルコーニの声")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "ガルシア、警察の小僧！！\x01",
            "い、行くならワシも連れて行かんか！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_FC0")

    TalkEnd(0xFF)
    Return()

    # Function_5_B6F end

    def Function_6_FC4(): pass

    label("Function_6_FC4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1266")
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("怯えた声")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "い、一体何が起こっているのだ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("怯えた声")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "看守っ……どこにいるんだ！\x01",
            "は、はやくこの事態を収拾してくれ！\x07\x00\x02",
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
            "#11103F（……この部屋に収容されているのは、\x01",
            "  確かハルトマンの野郎だ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00001F（ハルトマン元議長……\x01",
            "  アルタイルロッジ以来だな。）\x02\x03",

            "#00003F（なんだか怯えた印象に\x01",
            "  なってしまっているけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x10B,
        (
            "#11104F（拘置所に入れられてからは、\x01",
            "  ずっとあんな調子らしいな。）\x02\x03",

            "#11102F（富も地位も失っちまって、\x01",
            "  己を支えられるものが\x01",
            "  何も無くなっちまったんだろう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00003F（……少し心配だけど……\x01",
            "  これも彼に与えられた罰か。）\x02\x03",

            "#00001F（……そろそろ行くとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 2)
    Jump("loc_1321")

    label("loc_1266")

    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("ハルトマンの声")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "い、一体何が起こっているのだ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("ハルトマンの声")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "看守っ……どこにいるんだ！\x01",
            "は、はやくこの事態を収拾してくれ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1321")

    TalkEnd(0xFF)
    Return()

    # Function_6_FC4 end

    def Function_7_1325(): pass

    label("Function_7_1325")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x193, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179A")
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("落ち着いた声")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "そこにいるのは……\x01",
            "もしかしてロイド君かい？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("落ち着いた声")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "そうか、この騒ぎは君が……\x07\x00\x02",
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
            "#00005Fこの声……もしかして、\x01",
            "アーネストさんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x10B,
        (
            "#11101F……元市長秘書か。\x01",
            "そういえばここに\x01",
            "入っていたんだったな。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("アーネストの声")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "ロイド君がここに入れられたと\x01",
            "聞いた時は驚いていたけど……\x01",
            "……はは、また会えて嬉しいよ。\x07\x00\x02",
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
            "#00002Fよかった……その様子だと、\x01",
            "もうグノーシスはほとんど\x01",
            "抜けているみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("アーネストの声")

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "ああ、おかげさまでね。\x01",
            "君たちには本当に申し訳ない事を……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("アーネストの声")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……いや、今はやめておこう。\x01",
            "どうやらそんな状況でもなさそうだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("アーネストの声")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "罪を償ってここを出たら、\x01",
            "改めて、君やエリィたちに\x01",
            "謝罪をさせてもらいたいと思ってる。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("アーネストの声")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "どうか、今は構わず行ってくれ。\x01",
            "……女神の加護を祈っているよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0038
    ChrTalk(
        0x101,
        "#00004F……ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x10B,
        (
            "#11103F……話は済んだか？\x01",
            "モタモタしてる暇はねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00001Fああ……急ごう！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x193, 3)
    Jump("loc_1889")

    label("loc_179A")

    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("アーネストの声")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "罪を償ってここを出たら、\x01",
            "改めて、君やエリィたちに\x01",
            "謝罪をさせてもらいたいと思ってる。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(160, 160, -1, -1)
    SetChrName("アーネストの声")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "どうか、今は構わず行ってくれ。\x01",
            "……女神の加護を祈っているよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1889")

    TalkEnd(0xFF)
    Return()

    # Function_7_1325 end

    def Function_8_188D(): pass

    label("Function_8_188D")

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
        "#6Pいたぞ！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        "そこを動くな！\x02",
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

    def lambda_1AE2():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AE2)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_1AFF():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1AFF)
    EndChrThread(0x12, 0x0)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 10)
    BeginChrThread(0x15, 1, 0, 11)

    def lambda_1B37():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1B37)
    EndChrThread(0x13, 0x0)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 10)

    def lambda_1B69():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1B69)
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

    # Function_8_188D end

    def Function_9_1BF6(): pass

    label("Function_9_1BF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C11")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_9_1BF6")

    label("loc_1C11")

    Return()

    # Function_9_1BF6 end

    def Function_10_1C12(): pass

    label("Function_10_1C12")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C2D")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_10_1C12")

    label("loc_1C2D")

    Return()

    # Function_10_1C12 end

    def Function_11_1C2E(): pass

    label("Function_11_1C2E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C47")
    Sound(845, 0, 100, 0)
    Sleep(500)
    Jump("Function_11_1C2E")

    label("loc_1C47")

    Return()

    # Function_11_1C2E end

    def Function_12_1C48(): pass

    label("Function_12_1C48")

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
            "#00006F#11P……軍用犬を使い始めたのか。\x02\x03",

            "#00008F警備隊の時にはそんなの\x01",
            "使っていなかった筈なのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x10B,
        (
            "#11104F#5Pフン、俺たち#6Rルバーチェ#の運用成果を\x01",
            "利用したのかもしれねぇな。\x02\x03",

            "#11102Fひょっとしたらクスリで\x01",
            "操っているのかもしれねぇ。\x02\x03",

            "#11109Fクク、いい感じでエゲつなく\x01",
            "なってるみてぇじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10B, 500)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00010F#12Pくっ……あんたが言うな！\x02\x03",

            "#00008F（ソーニャ司令やダグラス副司令の\x01",
            "  判断とは思えないけど……）\x02",
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

    # Function_12_1C48 end

    def Function_13_1EC2(): pass

    label("Function_13_1EC2")

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

    # Function_13_1EC2 end

    def Function_14_1F29(): pass

    label("Function_14_1F29")

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

    def lambda_219B():
        OP_93(0xA, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_219B)
    Sleep(50)

    def lambda_21AB():
        OP_93(0xB, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_21AB)
    Sleep(50)

    def lambda_21BB():
        OP_93(0xC, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_21BB)
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
        "#5Pガ、ガルシア！？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        "#5P支援課の若造もいるぞ！？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xC,
        (
            "#6Pええい！\x01",
            "まとめて捕らえろ！\x02",
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

    # Function_14_1F29 end

    def Function_15_22FA(): pass

    label("Function_15_22FA")

    OP_93(0xFE, 0xF0, 0x0)
    OP_74(0x8, 0xA)
    OP_71(0x8, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x8)
    OP_74(0x8, 0x1E)
    Sleep(100)

    def lambda_2320():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2320)
    OP_96(0xFE, 0xFFFF19BA, 0x0, 0xFFFFF79A, 0x1388, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    WaitChrThread(0xFE, 2)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_15_22FA end

    def Function_16_235A(): pass

    label("Function_16_235A")

    Sleep(1300)

    def lambda_2362():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2362)
    OP_95(0xFE, -57850, 0, -1050, 5000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0x10B, 0x27)
    SetChrSubChip(0x10B, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x10B, 0x1)
    Return()

    # Function_16_235A end

    def Function_17_23A3(): pass

    label("Function_17_23A3")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -60700, 0, 4700, 5000, 0x1)
    OP_95(0xFE, -58250, 0, 4700, 5000, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x1388, 0x1)
    Return()

    # Function_17_23A3 end

    def Function_18_23EA(): pass

    label("Function_18_23EA")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1388, 0x1)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    Return()

    # Function_18_23EA end

    def Function_19_241F(): pass

    label("Function_19_241F")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_19_241F end

    def Function_20_2431(): pass

    label("Function_20_2431")

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

    # Function_20_2431 end

    def Function_21_247D(): pass

    label("Function_21_247D")

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

    # Function_21_247D end

    def Function_22_24DE(): pass

    label("Function_22_24DE")

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
        "#00015F#11Pくっ……はあはあ。\x02",
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
            "#11102F#5Pクク……\x01",
            "息が上がって来たじゃねえか。\x02\x03",

            "そんな体たらくでこの先を\x01",
            "切り抜けられると思ってんのか？\x02",
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
            "#00006F#12Pああ、俺一人じゃ\x01",
            "無理だとは思うけど……\x02\x03",

            "#00000Fあんたの助けがあれば\x01",
            "拘置所からの脱出は可能だ。\x02\x03",

            "使える力は使わせてもらうさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x10B,
        (
            "#11104F#5P……フン。\x01",
            "開き直りやがったな。\x02\x03",

            "#11107Fいいだろう……\x01",
            "とっとと抜け出すぞ！\x02",
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

    # Function_22_24DE end

    def Function_23_278F(): pass

    label("Function_23_278F")

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

    # Function_23_278F end

    def Function_24_2829(): pass

    label("Function_24_2829")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BA6")
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
            "#00013F#5P（数が多い……\x01",
            "  でも、あれを突破できれば！）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x10B,
        (
            "#11100F#5P（フン、このまま一気に\x01",
            "  ブチかましてやるとするか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x184, 0)

    label("loc_2BA6")

    OP_0D()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "このまま突入する\x01",          # 0
            "いったん準備を整える\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C07"),
        (1, "loc_31C4"),
        (SWITCH_DEFAULT, "loc_3256"),
    )


    label("loc_2C07")

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
        "#5P──脱走者は２名！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xD,
        (
            "#5P元マフィア幹部のガルシアと\x01",
            "支援課のバニングスと思われる！\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xD,
        (
            "#5P国防軍の誇りにかけて\x01",
            "絶対に拘置所から出すな！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(260, 30, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    SetChrName("国防軍兵士たち")

    #A0060
    AnonymousTalk(
        0xFF,
        "#4Sイエス・サー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0061
    ChrTalk(
        0x10B,
        "#11109Fハッ……誇りときたか。\x02",
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

    def lambda_2DD6():
        OP_93(0xD, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2DD6)
    Sleep(50)

    def lambda_2DE6():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2DE6)
    Sleep(50)

    def lambda_2DF6():
        OP_93(0xF, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_2DF6)
    Sleep(50)

    def lambda_2E06():
        OP_93(0x10, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2E06)
    Sleep(50)

    def lambda_2E16():
        OP_93(0x11, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2E16)
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

    def lambda_2EA0():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2EA0)
    Sleep(0)

    def lambda_2EB8():
        OP_9B(0x0, 0x10B, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_2EB8)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10B, 0)
    OP_6F(0x79)
    OP_0D()

    #C0062
    ChrTalk(
        0xE,
        "#11Pなっ……！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xD,
        "#11Pも、もう降りて来たのか！？\x02",
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
            "#00007F#5P悪いけど……\x01",
            "ここは押し通らせてもらう！\x02",
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
            "#11102F#5Pクク、その誇りとやらを\x01",
            "見せてもらおうじゃねぇか？\x02",
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
        "#11P#4Sくっ……かかれ！\x02",
    )

    CloseMessageWindow()
    OP_68(85000, 1000, 0, 1000)
    SetCameraDistance(25500, 1000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_304F():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_304F)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)

    def lambda_306F():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_306F)
    Sleep(100)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)

    def lambda_308F():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_308F)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x15, 1, 0, 11)
    BeginChrThread(0x12, 0, 0, 10)

    def lambda_30C6():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_30C6)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 10)

    def lambda_30F4():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_30F4)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 10)

    def lambda_3122():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3122)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_3142():
        OP_9B(0x0, 0xFE, 0x2, 0x1F40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3142)
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
    Jump("loc_3256")

    label("loc_31C4")

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
    Jump("loc_3256")

    label("loc_3256")

    Return()

    # Function_24_2829 end

    def Function_25_3257(): pass

    label("Function_25_3257")

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
        "#00006F#5Pふう……何とかなったか。\x02",
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
            "#00004F#6Pしかしあんた……\x01",
            "やっぱり凄まじい戦闘力だな。\x02\x03",

            "#00000Fランディや赤い星座のボスも\x01",
            "相当なものだったけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 500)

    #C0069
    ChrTalk(
        0x10B,
        (
            "#11103F#11Pフン……\x01",
            "《赤の戦鬼#8Rオーガ・ロッソ#》シグムントか。\x02\x03",

            "#11100F猟兵時代に何度か遭遇したが\x01",
            "正直、本物の化物だったぜ。\x02\x03",

            "噂じゃ娘の方も\x01",
            "相当ヤバイと聞いているが。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00001F#6Pああ……《結社》の連中より、\x01",
            "単純な戦闘力では上かもしれない。\x02\x03",

            "#00006Fまあ《結社》の方にも\x01",
            "とんでもない使い手がいたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x10B,
        (
            "#11104F#11Pクク、そんな化物どもと\x01",
            "この先やり合う必要があるわけか。\x02\x03",

            "#11102F前途多難じゃねぇか、オイ？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#00006F#6Pああ、まったくだよ。\x02",
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
            "#00001F#11P封鎖されているな……\x02\x03",

            "近くでロックを\x01",
            "解除できると思うけど。\x02",
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
            "#11104F#5Pハッ、そこの部屋だろう。\x02\x03",

            "#11100Fとっとと解除してずらかるぞ。\x02",
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

    # Function_25_3257 end

    def Function_26_3767(): pass

    label("Function_26_3767")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 90400, 0, -1800, 2300, 0x1)
    OP_95(0xFE, 92070, 0, -6230, 2500, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_26_3767 end

    def Function_27_379E(): pass

    label("Function_27_379E")

    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(700)
    OP_95(0xFE, 91230, 0, -2860, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_27_379E end

    def Function_28_37C7(): pass

    label("Function_28_37C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37E5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_28_37C7")

    label("loc_37E5")

    Return()

    # Function_28_37C7 end

    def Function_29_37E6(): pass

    label("Function_29_37E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3801")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_29_37E6")

    label("loc_3801")

    Return()

    # Function_29_37E6 end

    def Function_30_3802(): pass

    label("Function_30_3802")

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

    # Function_30_3802 end

    def Function_31_3902(): pass

    label("Function_31_3902")

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
        "#00002F#5Pやった……！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x10B,
        "#11100F#5Pよし、とっとと出るぞ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 147480, 0, 3020, 270)
    OP_69(0xFF, 0x0)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x184, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x184, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ADF")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_3ADF")

    EventEnd(0x5)
    Return()

    # Function_31_3902 end

    def Function_32_3AE2(): pass

    label("Function_32_3AE2")

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
            "取り上げられた装備・アイテムと\x01",
            "エニグマⅡを全て取り戻した。\x02",
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
            "#00006F#5Pよかった……\x01",
            "ここに保管してあったか。\x02\x03",

            "#00002Fどうやらクオーツも\x01",
            "全部揃ってるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x10B,
        (
            "#11103F#5Pオラ、さっさと行くぞ。\x02\x03",

            "#11100F兵士どもに囲まれて\x01",
            "ブチ込まれたくなければな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#00000F#5Pああ……！\x02",
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

    # Function_32_3AE2 end

    def Function_33_3CDC(): pass

    label("Function_33_3CDC")

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
            "#00005F#5P（そういえば……\x01",
            "  取り上げられた装備や所持品が\x01",
            "  どこかに保管されているはずだ。）\x02\x03",

            "#00008F（ひょっとして……）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(147390, 1000, -2320, 1500)
    SetCameraDistance(23010, 1500)

    def lambda_3DED():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3DED)
    Sleep(200)

    def lambda_3DFD():
        OP_93(0x10B, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_3DFD)
    Sleep(200)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10B, 0)
    OP_6F(0x79)
    Sleep(500)
    SetChrPos(0x0, 145760, 0, 3760, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_33_3CDC end

    SaveToFile()

Try(main)
