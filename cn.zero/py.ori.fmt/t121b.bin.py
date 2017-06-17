from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t121b.bin",                # FileName
        "t121b",                    # MapName
        "t121b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 1, 0, 2],
    )

    BuildStringList((
        "t121b",                  # 0
        "管家寇恩",               # 1
        "黑衣人",                 # 2
        "黑手党",                 # 3
        "黑手党",                 # 4
        "黑手党",                 # 5
        "黑手党",                 # 6
        "黑手党",                 # 7
        "黑手党",                 # 8
        "雷克特",                 # 9
        "伊丽莎白",               # 10
        "声音",                   # 11
        "银",                     # 12
        "bt113b",                 # 13
    ))

    ATBonus("ATBonus_3B8", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3F8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_464", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_468", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_46C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_470", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_478", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt113b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", "ms31102.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_458", "ed7509", "ed7000", "ATBonus_3B8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch25900.itc",                   # 00
        "chr/ch36000.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch07400.itc",                   # 05
        "chr/ch39100.itc",                   # 06
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

    DeclNpc(-58000,  0,       -49500,  180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(58000,   0,       -49500,  180,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(60700,   0,       2400,    0,    389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(63099,   0,       4000,    315,  389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(63099,   0,       4000,    315,  389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -55500,  0,    389,  0x0, 3,   2,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -56500,  0,    389,  0x0, 3,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -57500,  0,    389,  0x0, 3,   4,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-54029,  0,       6579,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-52930,  0,       6579,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 13,  58.0,                  -57.5,                 -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.600000381469727,   19.166667938232422,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 14,  58.0,                  -57.5,                 -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.600000381469727,   19.166667938232422,    0.20000000298023224,   1.0])

    DeclActor(55540,   0,       6000,    2500,    55540,   1500,    6000,    0x007C, 0,  8,  0x0000)
    DeclActor(-57850,  0,       4860,    2500,    -57850,  1500,    4860,    0x007C, 0,  8,  0x0000)
    DeclActor(55540,   0,       1500,    2500,    55540,   1500,    1500,    0x007C, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_540",          # 00, 0
        "Function_1_5F8",          # 01, 1
        "Function_2_68C",          # 02, 2
        "Function_3_7C6",          # 03, 3
        "Function_4_996",          # 04, 4
        "Function_5_9DE",          # 05, 5
        "Function_6_B76",          # 06, 6
        "Function_7_CC9",          # 07, 7
        "Function_8_CDE",          # 08, 8
        "Function_9_D7D",          # 09, 9
        "Function_10_DBA",         # 0A, 10
        "Function_11_E72",         # 0B, 11
        "Function_12_F2A",         # 0C, 12
        "Function_13_11BD",        # 0D, 13
        "Function_14_18CC",        # 0E, 14
        "Function_15_1EF3",        # 0F, 15
        "Function_16_2B72",        # 10, 16
        "Function_17_2BD3",        # 11, 17
        "Function_18_2C34",        # 12, 18
        "Function_19_2C95",        # 13, 19
        "Function_20_30EC",        # 14, 20
        "Function_21_345C",        # 15, 21
        "Function_22_34A0",        # 16, 22
        "Function_23_34C6",        # 17, 23
        "Function_24_4C53",        # 18, 24
        "Function_25_4CA8",        # 19, 25
        "Function_26_4CED",        # 1A, 26
        "Function_27_4D32",        # 1B, 27
        "Function_28_4D69",        # 1C, 28
        "Function_29_4DA7",        # 1D, 29
        "Function_30_4DEB",        # 1E, 30
        "Function_31_4E2F",        # 1F, 31
        "Function_32_4E73",        # 20, 32
    ))


    def Function_0_540(): pass

    label("Function_0_540")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_580"),
        (1, "loc_58C"),
        (2, "loc_598"),
        (3, "loc_5A4"),
        (4, "loc_5B0"),
        (5, "loc_5BC"),
        (6, "loc_5C8"),
        (SWITCH_DEFAULT, "loc_5D4"),
    )


    label("loc_580")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_58C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_598")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5F7")

    Return()

    # Function_0_540 end

    def Function_1_5F8(): pass

    label("Function_1_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_END)), "loc_61A")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_657")

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_632")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_657")

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_640")
    Jump("loc_657")

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_64E")
    Jump("loc_657")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_657")

    label("loc_657")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_671")
    Event(0, 19)

    label("loc_671")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68B")
    Event(0, 23)

    label("loc_68B")

    Return()

    # Function_1_5F8 end

    def Function_2_68C(): pass

    label("Function_2_68C")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BC")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E4")
    Call(0, 9)

    label("loc_6E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_END)), "loc_707")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_707")
    Call(0, 10)

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_72A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_72A")
    Call(0, 11)

    label("loc_72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_END)), "loc_754")
    SetMapObjFrame(0xFF, "mado_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x1, 0x1)
    Jump("loc_770")

    label("loc_754")

    SetMapObjFrame(0xFF, "mado_a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x0, 0x1)

    label("loc_770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_779")

    label("loc_779")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_791")
    OP_1B(0x2, 0x0, 0x20)

    label("loc_791")

    SetMapObjFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AB")
    ClearMapObjFlags(0x8, 0x10)

    label("loc_7AB")

    SetMapObjFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C5")
    ClearMapObjFlags(0x9, 0x10)

    label("loc_7C5")

    Return()

    # Function_2_68C end

    def Function_3_7C6(): pass

    label("Function_3_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DC")
    Call(0, 12)
    Jump("loc_995")

    label("loc_7DC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_7ED")
    Jump("loc_992")

    label("loc_7ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_84B")

    #C0001
    ChrTalk(
        0xFE,
        (
            "老爷正在和马尔克尼会长\x01",
            "就竞拍会的安排\x01",
            "进行最终确认。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "请不要打扰他们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_992")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_8B0")

    #C0003
    ChrTalk(
        0xFE,
        (
            "这里是本馆的主人\x01",
            "哈尔特曼议长阁下的\x01",
            "居室。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "竞拍会即将开始，\x01",
            "请尽快前往会场。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_992")

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_992")

    #C0005
    ChrTalk(
        0xFE,
        (
            "这里是本馆的主人\x01",
            "哈尔特曼议长阁下的\x01",
            "居室。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_944")

    #C0006
    ChrTalk(
        0xFE,
        (
            "老爷现在应该\x01",
            "在一楼左手边的\x01",
            "客厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "如果有事的话，\x01",
            "请到那边去找他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_992")

    label("loc_944")


    #C0008
    ChrTalk(
        0xFE,
        (
            "老爷正准备前往一楼\x01",
            "左手边的客厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "如果有什么要事，\x01",
            "请到那边去等候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_992")

    TalkEnd(0x8)

    label("loc_995")

    Return()

    # Function_3_7C6 end

    def Function_4_996(): pass

    label("Function_4_996")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎完全失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_4_996 end

    def Function_5_9DE(): pass

    label("Function_5_9DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_9EF")
    Jump("loc_B72")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_9FD")
    Jump("loc_B72")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_A53")

    #C0012
    ChrTalk(
        0xFE,
        (
            "实在失礼……\x01",
            "您待在这边\x01",
            "会影响商品的搬运。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "请在会场耐心等候。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B72")

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B34")

    #C0014
    ChrTalk(
        0xFE,
        "……客人，还有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#5100F啊，不……\x01",
            "没什么。\x02\x03",

            "#5108F（……刚才的声音到底是……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0016
    ChrTalk(
        0xFE,
        (
            "……拍卖品在开场之前\x01",
            "都是非公开的。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "请耐心等待\x01",
            "竞拍会的展出。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B72")

    label("loc_B34")


    #C0018
    ChrTalk(
        0xFE,
        (
            "拍卖品在开场之前都是非公开的，\x01",
            "请耐心等待\x01",
            "竞拍会的展出。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B72")

    TalkEnd(0xFE)
    Return()

    # Function_5_9DE end

    def Function_6_B76(): pass

    label("Function_6_B76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")

    #C0019
    ChrTalk(
        0x10,
        (
            "#3505F啊，\x01",
            "本该去了后院的人\x01",
            "竟然还在这里呢。\x02\x03",

            "#3502F你们还有时间在这里磨磨蹭蹭吗～？\x02",
        )
    )

    CloseMessageWindow()

    #N0020
    NpcTalk(
        0x101,
        "琪雅",
        "#5810F#N奇怪的人，再见哦！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x10,
        (
            "#3504F好好，再见啦～\x02\x03",

            "#3501F……话说，叫我奇怪的人，\x01",
            "未免也太过分了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CC5")

    label("loc_C57")

    OP_4B(0x11, 0xFF)
    TurnDirection(0xFE, 0x11, 0)

    #C0022
    ChrTalk(
        0x10,
        (
            "#3509F房间的主人好像不在，\x01",
            "可以尽情玩了哦，小黑。\x02\x03",

            "#3507F好，不如来踢罐子吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x11,
        "喵呜？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)

    label("loc_CC5")

    TalkEnd(0xFE)
    Return()

    # Function_6_B76 end

    def Function_7_CC9(): pass

    label("Function_7_CC9")

    TalkBegin(0xFE)

    #C0024
    ChrTalk(
        0xFE,
        "咕噜喵～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_CC9 end

    def Function_8_CDE(): pass

    label("Function_8_CDE")

    OP_F2(0x3)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5F")
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

    label("loc_D5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_D7B")

    Return()

    # Function_8_CDE end

    def Function_9_D7D(): pass

    label("Function_9_D7D")

    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 58930, 0, -51280, 0)
    Return()

    # Function_9_D7D end

    def Function_10_DBA(): pass

    label("Function_10_DBA")

    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 59800, 0, 1810, 0)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, 58650, 0, 3490, 45)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 64230, 0, 4180, 315)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)
    Return()

    # Function_10_DBA end

    def Function_11_E72(): pass

    label("Function_11_E72")

    SetChrChipByIndex(0xD, 0x3)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xD, 58290, 0, -55060, 45)
    SetChrChipByIndex(0xE, 0x3)
    SetChrSubChip(0xE, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xE, 59250, 0, -56490, 180)
    SetChrChipByIndex(0xF, 0x3)
    SetChrSubChip(0xF, 0x1)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x1)
    SetChrPos(0xF, 56290, 0, -58070, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)
    Return()

    # Function_11_E72 end

    def Function_12_F2A(): pass

    label("Function_12_F2A")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(-57790, 1200, -50440, 0)
    MoveCamera(315, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18290, 0)
    SetChrPos(0x101, -57400, 0, -51000, 0)
    SetChrPos(0xEF, -58600, 0, -51000, 0)
    OP_0D()

    #C0025
    ChrTalk(
        0x8,
        "#11P客人，实在抱歉。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#11P这里是本馆主人的\x01",
            "居室。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0027
    ChrTalk(
        0x101,
        (
            "#5105F#6P这么说……\x01",
            "是哈尔特曼议长阁下的？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#11P是的，正是如此。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_10AE")

    #C0029
    ChrTalk(
        0x8,
        "#11P只是很不巧，老爷刚好不在。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#11P现在应该在一楼左手边的\x01",
            "客厅里……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#5100F#6P嗯，刚才看到了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1125")

    label("loc_10AE")


    #C0032
    ChrTalk(
        0x8,
        (
            "#11P差不多应该去一楼左手边的\x01",
            "客厅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#11P如果您找老爷有事，\x01",
            "可以在那边等候……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#5100F#6P是吗，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_1125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1150")

    #C0035
    ChrTalk(
        0x102,
        "#5302F#6P呵呵，打扰了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_119F")

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1179")

    #C0036
    ChrTalk(
        0x103,
        "#5404F#6P……打扰了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_119F")

    label("loc_1179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_119F")

    #C0037
    ChrTalk(
        0x104,
        "#5609F#6P那么，打扰啦。\x02",
    )

    CloseMessageWindow()

    label("loc_119F")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -58000, 0, -51500, 180)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xA5, 7)
    EventEnd(0x5)
    Return()

    # Function_12_F2A end

    def Function_13_11BD(): pass

    label("Function_13_11BD")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(1000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, 58000, 0, -48500, 0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(58220, 1100, -52980, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19200, 0)
    SetChrPos(0x101, 57410, 0, -62690, 0)
    SetChrPos(0xEF, 58150, 0, -63610, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")

    def lambda_126F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_126F)

    def lambda_1284():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1284)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(58220, 1100, -53580, 1800)

    def lambda_12C0():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12C0)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x9,
        (
            "#5P──客人，\x01",
            "非常抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "#5P这里是工作人员\x01",
            "专用的房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#5106F#12P啊，这真是失礼了。\x01",
            "这里实在太大，我们似乎迷路了。\x02\x03",

            "#5108F（这里是黑手党的\x01",
            "  待命场所吗……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(58220, 1100, -51980, 1800)
    OP_6F(0x1)

    #N0041
    NpcTalk(
        0x12,
        "男人的声音",
        (
            "#2P#2S喂，清单上的物品\x01",
            "都齐了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #N0042
    NpcTalk(
        0x12,
        "男人的声音",
        (
            "#5P#2S嗯，差不多该把\x01",
            "前半场的拍卖品搬去会场了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x9,
        "#11P嘁，那些家伙……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#5105F#12P难不成……\x01",
            "拍卖品都放在这里？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(58220, 1100, -53580, 1200)
    OP_93(0x9, 0xB4, 0x190)
    OP_6F(0x1)

    #C0045
    ChrTalk(
        0x9,
        (
            "#5P嗯、嗯。\x01",
            "为了确保万无一失，\x01",
            "现在由我们保管。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "#5P敬请期待它们在\x01",
            "竞拍会中的展出。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#5104F#12P……嗯，\x01",
            "当然期待啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    #C0048
    ChrTalk(
        0x101,
        "#5100F#5P──那么，回去吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_15D3")

    #C0049
    ChrTalk(
        0x102,
        "#5302F#11P嗯，知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1624")

    label("loc_15D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_15FF")

    #C0050
    ChrTalk(
        0x103,
        "#5402F#11P……是，哥哥。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1624")

    label("loc_15FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1624")

    #C0051
    ChrTalk(
        0x104,
        "#5602F#11P好啊，走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1624")


    def lambda_1629():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1629)

    def lambda_1636():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1636)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    Fade(1000)
    OP_68(58390, 1100, -58100, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18240, 0)
    OP_68(58390, 1100, -60100, 3000)

    def lambda_168F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_168F)

    def lambda_16A4():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_16A4)
    Sleep(2000)
    OP_0D()
    OP_C7(0x0, 0x800)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 75, 0)    #voice#KeA
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    FadeToBright(500, 0)
    SetChrSubChip(0x101, 0x0)

    def lambda_1721():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1721)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_C7(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_4B(0xEF, 0xFF)
    Sleep(500)
    OP_93(0xEF, 0x0, 0x1F4)

    #C0052
    ChrTalk(
        0x101,
        "#5111F#5P哎……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_17CC")

    #C0053
    ChrTalk(
        0x102,
        "#5305F#12P（……罗伊德？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_182D")

    label("loc_17CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_17FE")

    #C0054
    ChrTalk(
        0x103,
        "#5405F#12P（……罗伊德前辈？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_182D")

    label("loc_17FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_182D")

    #C0055
    ChrTalk(
        0x104,
        "#5605F#12P（……什么，怎么了？）\x02",
    )

    CloseMessageWindow()

    label("loc_182D")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0056
    ChrTalk(
        0x101,
        (
            "#5106F#5P（不……\x01",
            "  抱歉，没什么。）\x02\x03",

            "#5101F（赶快离开这里吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetScenarioFlags(0xA6, 0)
    OP_29(0x47, 0x1, 0xA)
    EventEnd(0x5)
    NewScene("t119B", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_13_11BD end

    def Function_14_18CC(): pass

    label("Function_14_18CC")

    EventBegin(0x2)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch31150.itc", 0x1E)
    LoadChrToIndex("chr/ch31151.itc", 0x1F)
    LoadChrToIndex("chr/ch31050.itc", 0x21)
    LoadChrToIndex("chr/ch31051.itc", 0x22)
    LoadChrToIndex("chr/ch00500.itc", 0x24)
    LoadChrToIndex("apl/ch50364.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31000.itc", 0x27)
    LoadChrToIndex("chr/ch00550.itc", 0x28)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 58810, 0, -53260, 0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 61240, 0, 1290, 0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 63510, 0, 4260, 315)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 60110, 0, 2400, 0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 60800, 0, 6500, 180)
    SetChrPos(0x101, 58000, 0, -59000, 0)
    SetChrPos(0xEF, 58700, 0, -60000, 0)
    SetChrPos(0x151, 57300, 0, -60500, 0)
    SetChrPos(0x9, 58930, 0, -51280, 0)
    OP_68(57900, 1500, -60140, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    FadeToBright(1000, 0)
    OP_68(57900, 1500, -58090, 1200)
    OP_6F(0x1)
    OP_0D()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(57900, 1300, -52450, 2000)
    SetCameraDistance(17330, 2000)

    def lambda_1ACB():
        OP_95(0xFE, 58340, 0, -52690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ACB)
    Sleep(100)

    def lambda_1AE8():
        OP_95(0xFE, 59000, 0, -53630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1AE8)
    Sleep(100)

    def lambda_1B05():
        OP_95(0xFE, 57030, 0, -53980, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1B05)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x151, 1)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0057
    ChrTalk(
        0x101,
        "#5110F#11P不行了，昏迷过去了……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x151,
        (
            "#5700F#12P哦，看来是一击\x01",
            "就被打晕了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1BC0")

    #C0059
    ChrTalk(
        0x102,
        "#5301F#12P能、能做到这一点的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C23")

    label("loc_1BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1BF4")

    #C0060
    ChrTalk(
        0x103,
        "#5401F#12P……能做到这一点的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C23")

    label("loc_1BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1C23")

    #C0061
    ChrTalk(
        0x104,
        "#5601F#12P嘁，能做到这一点的……\x02",
    )

    CloseMessageWindow()

    label("loc_1C23")


    #C0062
    ChrTalk(
        0x101,
        "#5113F#11P……总之，快进去吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    OP_68(61440, 1200, 3040, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19300, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x0)
    FadeToBright(1000, 0)
    OP_68(61440, 1200, 5040, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0063
    ChrTalk(
        0xA,
        "#12P你、你小子……！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        "#2P几时出现的……！\x02",
    )

    CloseMessageWindow()
    #Sound(1628, 255, 100, 0)    #voice#Yin
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0065
    AnonymousTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "呵呵……吾名为『银』。\x02\x03",

            "于月光洒落之处\x01",
            "悄然现身。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0066
    ChrTalk(
        0xA,
        "#4P胡、胡说八道……！\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        "#6P去死吧……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P太慢了──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14300, 400)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)

    def lambda_1E4E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E4E)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)

    def lambda_1E6B():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E6B)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)

    def lambda_1E88():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1E88)
    Sleep(300)
    Battle(0xFFFFFFFF, 0x30200004, "", 0x30000500, 0x0, 0x0, 0x0, 0x30031100, 0x30031000, 0x30031000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x200, 0x8)
    FadeToDark(0, 0, -1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    Call(0, 15)
    Return()

    # Function_14_18CC end

    def Function_15_1EF3(): pass

    label("Function_15_1EF3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31151.itc", 0x1F)
    LoadChrToIndex("chr/ch31153.itc", 0x20)
    LoadChrToIndex("chr/ch31051.itc", 0x22)
    LoadChrToIndex("chr/ch31053.itc", 0x23)
    LoadChrToIndex("chr/ch00500.itc", 0x24)
    LoadChrToIndex("chr/ch00501.itc", 0x25)
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    LoadChrToIndex("chr/ch00551.itc", 0x27)
    LoadEffect(0x0, "event\\ev307_00.eff")
    LoadEffect(0x1, "battle\\ms00001.eff")
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xA, 60780, 0, 4520, 0)
    SetChrPos(0xB, 60140, 0, 5260, 45)
    SetChrPos(0xC, 61710, 0, 5140, 315)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, 61000, 0, 6300, 180)
    FadeToBright(0, 0)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(834, 0, 100, 0)
    OP_68(61000, 700, 5300, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14530, 0)
    SetCameraDistance(17660, 500)
    BeginChrThread(0xA, 3, 0, 16)
    BeginChrThread(0xB, 3, 0, 17)
    BeginChrThread(0xC, 3, 0, 18)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    OP_6F(0x79)
    CancelBlur(0)

    #C0069
    ChrTalk(
        0xC,
        "#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        "#6P不可能……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    Sound(514, 0, 100, 0)
    Call(0, 10)
    OP_0D()
    Sleep(750)
    SetChrPos(0x101, 58160, 0, -4030, 0)
    SetChrPos(0xEF, 58160, 0, -4030, 0)
    SetChrPos(0x151, 58160, 0, -4030, 0)
    OP_68(61500, 1000, 4019, 2000)
    MoveCamera(42, 16, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(18540, 2000)
    Sleep(200)

    def lambda_20EA():
        OP_95(0xFE, 61080, 0, 1250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20EA)
    Sleep(200)

    def lambda_2107():
        OP_95(0xFE, 61590, 0, 160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2107)
    Sleep(200)

    def lambda_2124():
        OP_95(0xFE, 60490, 0, 60, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2124)
    WaitChrThread(0x101, 1)

    def lambda_2142():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2142)
    WaitChrThread(0xEF, 1)

    def lambda_2153():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2153)
    WaitChrThread(0x151, 1)

    def lambda_2164():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2164)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0071
    ChrTalk(
        0x101,
        "#5107F#12P什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_220D")

    #C0072
    ChrTalk(
        0x102,
        "#5307F#12P果、果然是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_225C")

    label("loc_220D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2235")

    #C0073
    ChrTalk(
        0x103,
        "#5401F#12P果然……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_225C")

    label("loc_2235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_225C")

    #C0074
    ChrTalk(
        0x104,
        "#5607F#12P出现了吗……！\x02",
    )

    CloseMessageWindow()

    label("loc_225C")

    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x13)
    Sleep(300)
    Sound(1609, 255, 100, 0)    #voice#Yin
    Sleep(800)

    #C0075
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P……我就觉得有奇怪的气息，\x01",
            "原来你们也潜进来了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5113F#12P你……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x151,
        (
            "#5705F#12P嘿……\x01",
            "这人看起来很危险啊。\x02\x03",

            "#5702F没猜错的话，阁下就是在街头巷尾中\x01",
            "广为流传的『银』大人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P正是……\x01",
            "『圣书会』的首领，\x01",
            "瓦吉·赫米斯菲亚。\x02\x03",

            "看来奇怪的气息之一\x01",
            "就是你啊。\x02\x03",

            "除你以外似乎还有其他人……\x01",
            "哼哼，还真是群魔乱舞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x151,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5704F#12P呵，你说话很有趣呢。\x02\x03",

            "#5700F那么……\x01",
            "你打算像对付他们一样，\x01",
            "以武力来解决我们吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13)
    Fade(250)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0x101,
        "#5111F#12P喂、喂……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0081
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11P呵呵，要解决你们\x01",
            "本是易如反掌……\x02\x03",

            "不过，把这里交给你们\x01",
            "似乎也很有趣。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0082
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5105F#12P哎……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x13, 0x10E, 0x1F4)
    Sleep(300)

    #C0083
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11P在那里面的房间中，\x01",
            "存放着将在竞拍会后半场展出的拍卖品……\x02\x03",

            "根据『黑月』收到的情报，\x01",
            "里面似乎藏着很有趣的『炸弹』哦。\x02\x03",

            "你们不妨去亲眼确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1614, 255, 100, 0)    #voice#Yin
    OP_93(0x13, 0x0, 0x190)
    Sleep(1200)
    Fade(500)
    OP_68(61000, 1000, 4500, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18540, 0)
    SetCameraDistance(17540, 1000)
    OP_0D()
    OP_6F(0x79)
    OP_68(61000, 1500, 8000, 1500)
    MoveCamera(0, 7, 0, 1500)
    OP_6E(800, 1500)
    SetCameraDistance(7250, 1500)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    SetChrChip(0x0, 0x13, 0x1E, 0x12C)

    def lambda_267A():
        OP_95(0xFE, 61000, 0, 7500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_267A)
    WaitChrThread(0x13, 1)
    SetChrSubChip(0x13, 0x2)
    SetChrFlags(0x13, 0x4)
    Sleep(200)
    Sound(854, 0, 100, 0)

    def lambda_26AA():
        OP_9D(0xFE, 0xEE48, 0xFFFFD8F0, 0x2AF8, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_26AA)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 60800, 0, 9000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0x1770, 0x1F4)
    Sound(921, 0, 100, 0)
    Sound(812, 0, 100, 0)
    SetMapObjFrame(0xFF, "mado_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x1, 0x1)
    WaitChrThread(0x13, 1)
    SetChrChip(0x1, 0x13, 0x0, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    OP_6F(0x79)
    Sleep(750)
    StopBGM(0x1F40)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(61020, 1000, 7200, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19540, 0)
    SetCameraDistance(16540, 2000)

    def lambda_27A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27A6)
    Sleep(300)

    def lambda_27BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_27BE)
    Sleep(300)

    def lambda_27D6():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_27D6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x151, 1)
    OP_6F(0x79)
    OP_0D()

    #C0084
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5107F#11P喂、喂……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2843")

    #C0085
    ChrTalk(
        0x102,
        "#5301F#11P好轻盈的身法……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_289C")

    label("loc_2843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_286F")

    #C0086
    ChrTalk(
        0x103,
        "#5401F#11P……好快……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_289C")

    label("loc_286F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_289C")

    #C0087
    ChrTalk(
        0x104,
        "#5607F#11P好惊人的身手啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_289C")


    #C0088
    ChrTalk(
        0x151,
        (
            "#5706F#12P哎呀呀……\x01",
            "果然是个名不虚传的怪物啊。\x02\x03",

            "#5703F能免于和他交手，\x01",
            "实在是幸运……\x02\x03",

            "#5701F接下来该怎么办，罗伊德？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0089
    ChrTalk(
        0x101,
        (
            "#5103F#5P……没时间了，\x01",
            "去里面的房间调查一下吧。\x02\x03",

            "#5101F那家伙刚才说的『炸弹』……\x01",
            "如果真的存在，就必须要确认一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x151,
        (
            "#5702F#12P呵呵……\x01",
            "就知道你会这么说。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2A39")

    #C0091
    ChrTalk(
        0x102,
        (
            "#5306F#12P呼，没办法呢。\x02\x03",

            "#5300F那就尽快行动，\x01",
            "能调查多少就调查多少吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF6")

    label("loc_2A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2A9A")

    #C0092
    ChrTalk(
        0x103,
        (
            "#5406F#12P……唉，没办法呢。\x02\x03",

            "#5402F以最快速度行动，\x01",
            "能调查多少就调查多少吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF6")

    label("loc_2A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2AF6")

    #C0093
    ChrTalk(
        0x104,
        (
            "#5606F#12P真是的，没办法啊……\x02\x03",

            "#5600F动作利落一点，\x01",
            "能调查多少就调查多少吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF6")


    #C0094
    ChrTalk(
        0x101,
        "#5100F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrPos(0x0, 60190, 0, -200, 180)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xA6, 3)
    OP_29(0x47, 0x1, 0xD)
    OP_1B(0x2, 0x0, 0x20)
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7302", 0)
    ReplaceBGM("ed7125", "ed7302")
    EventEnd(0x5)
    Return()

    # Function_15_1EF3 end

    def Function_16_2B72(): pass

    label("Function_16_2B72")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60780, 800, 4520, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2BAE():
        OP_9D(0xFE, 0xE998, 0x0, 0x712, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BAE)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_16_2B72 end

    def Function_17_2BD3(): pass

    label("Function_17_2BD3")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60140, 800, 5260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2C0F():
        OP_9D(0xFE, 0xE51A, 0x0, 0xDA2, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C0F)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_17_2BD3 end

    def Function_18_2C34(): pass

    label("Function_18_2C34")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 61710, 800, 5140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2C70():
        OP_9D(0xFE, 0xFAE6, 0x0, 0x1054, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C70)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_18_2C34 end

    def Function_19_2C95(): pass

    label("Function_19_2C95")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch31050.itc", 0x23)
    LoadChrToIndex("chr/ch31051.itc", 0x24)
    LoadChrToIndex("chr/ch31150.itc", 0x25)
    LoadChrToIndex("chr/ch31151.itc", 0x26)
    LoadChrToIndex("chr/ch00000.itc", 0x29)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xD, 58100, 0, -73510, 0)
    SetChrPos(0xE, 58900, 0, -74710, 0)
    SetChrPos(0xF, 57170, 0, -75310, 0)
    SetChrPos(0x101, 57950, 0, -52700, 180)
    SetChrPos(0xEF, 58860, 0, -52240, 180)
    SetChrPos(0x105, 57560, 0, -50980, 180)
    SetChrPos(0x133, 57250, 0, -52700, 90)
    OP_68(58000, 1200, -51840, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(58100, 1200, -68860, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(58100, 1200, -73860, 1500)
    OP_6F(0x1)
    OP_0D()

    #C0095
    ChrTalk(
        0xD,
        "#11P在这里……！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        "#11P是入侵者……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(58000, 1200, -51840, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    #C0097
    ChrTalk(
        0x101,
        "#0010F#5P呜……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0098
    ChrTalk(
        0x101,
        (
            "#0007F#11P……琪雅！\x01",
            "你退后！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x133,
        "#5801F#6P嗯……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x133, 3, 0, 21)
    Sleep(200)
    OP_93(0x101, 0xB4, 0x12C)
    WaitChrThread(0x133, 3)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2F7E")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Jump("loc_2FA5")

    label("loc_2F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2F94")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_2FA5")

    label("loc_2F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2FA5")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_2FA5")

    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2FD5")

    #C0100
    ChrTalk(
        0x102,
        "#0107F#5P来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_301E")

    label("loc_2FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2FFC")

    #C0101
    ChrTalk(
        0x103,
        "#0201F#5P来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_301E")

    label("loc_2FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_301E")

    #C0102
    ChrTalk(
        0x104,
        "#0307F#5P来了……！\x02",
    )

    CloseMessageWindow()

    label("loc_301E")

    OP_68(57960, 1200, -53640, 1300)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xD, 58100, 0, -60510, 0)
    SetChrPos(0xE, 58900, 0, -61710, 0)
    SetChrPos(0xF, 57170, 0, -62310, 0)

    def lambda_307F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_307F)
    Sleep(100)

    def lambda_3097():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3097)
    Sleep(100)

    def lambda_30AF():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_30AF)
    Sleep(800)
    Battle("BattleInfo_478", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    Call(0, 20)
    Return()

    # Function_19_2C95 end

    def Function_20_30EC(): pass

    label("Function_20_30EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch00000.itc", 0x23)
    LoadChrToIndex("apl/ch50364.itc", 0x24)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 57950, 0, -52700, 180)
    SetChrPos(0xEF, 58860, 0, -52240, 180)
    SetChrPos(0x105, 57560, 0, -50980, 180)
    SetChrPos(0x133, 56620, 0, -49950, 180)
    Call(0, 11)
    OP_68(57960, 1200, -53640, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(18290, 2500)
    OP_6F(0x10)
    OP_0D()

    #C0103
    ChrTalk(
        0x101,
        "#0010F#5P呜……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_68(58380, 1200, -50320, 1500)
    MoveCamera(38, 19, 0, 1500)

    def lambda_320F():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_320F)

    def lambda_321C():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_321C)
    Sleep(100)

    def lambda_322C():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_322C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    #C0104
    ChrTalk(
        0x101,
        "#0001F#11P琪雅，不要紧吗！？\x02",
    )

    CloseMessageWindow()

    def lambda_3269():

        label("loc_3269")

        TurnDirection(0x101, 0x133, 500)
        Yield()
        Jump("loc_3269")

    QueueWorkItem2(0x101, 1, lambda_3269)

    def lambda_327B():

        label("loc_327B")

        TurnDirection(0xEF, 0x133, 500)
        Yield()
        Jump("loc_327B")

    QueueWorkItem2(0xEF, 1, lambda_327B)

    def lambda_328D():

        label("loc_328D")

        TurnDirection(0x105, 0x133, 500)
        Yield()
        Jump("loc_328D")

    QueueWorkItem2(0x105, 1, lambda_328D)
    OP_68(58380, 1200, -51450, 1000)
    BeginChrThread(0x133, 3, 0, 22)
    WaitChrThread(0x133, 3)
    OP_6F(0x1)
    Sleep(300)

    #C0105
    ChrTalk(
        0x133,
        (
            "#5810F#6P嗯，不要紧。\x02\x03",

            "#5809F琪雅没事哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#0002F#11P是吗……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x5)
    Sound(910, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    OP_0D()
    Sleep(300)

    #C0107
    ChrTalk(
        0x105,
        (
            "#0404F#5P呵呵，好有\x01",
            "胆量的孩子啊。\x02\x03",

            "#0400F希望能保持这种势头，\x01",
            "顺利逃掉。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_33D4")

    #C0108
    ChrTalk(
        0x102,
        "#0101F#11P总之，赶快走吧……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3433")

    label("loc_33D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3406")

    #C0109
    ChrTalk(
        0x103,
        "#0201F#11P……快点离开吧……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3433")

    label("loc_3406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3433")

    #C0110
    ChrTalk(
        0x104,
        "#0301F#11P总之，动作快点……！\x02",
    )

    CloseMessageWindow()

    label("loc_3433")

    Sleep(150)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    SetChrPos(0x0, 57210, 0, -54060, 180)
    SetScenarioFlags(0xA6, 6)
    EventEnd(0x5)
    Return()

    # Function_20_30EC end

    def Function_21_345C(): pass

    label("Function_21_345C")


    def lambda_3461():
        OP_95(0xFE, 56620, 0, -52700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3461)
    WaitChrThread(0xFE, 1)

    def lambda_347F():
        OP_95(0xFE, 56620, 0, -49950, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_347F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_345C end

    def Function_22_34A0(): pass

    label("Function_22_34A0")


    def lambda_34A5():
        OP_95(0xFE, 57250, 0, -52700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34A5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_22_34A0 end

    def Function_23_34C6(): pass

    label("Function_23_34C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("apl/ch50371.itc", 0x20)
    OP_68(-58000, 1200, 3580, 0)
    MoveCamera(322, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -58000, 0, -4970, 0)
    SetChrPos(0xEF, -58350, 0, -4920, 0)
    SetChrPos(0x105, -57990, 0, -6140, 0)
    SetChrPos(0x133, -52560, 0, -2430, 0)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, -59700, 0, 8000, 180)
    SetChrFlags(0x10, 0x8000)
    VolumeBGM(0x32, 0x7D0)
    FadeToBright(1000, 0)
    OP_68(-58000, 1200, -1480, 4000)

    def lambda_35A3():
        OP_95(0xFE, -58000, 0, -1860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35A3)
    Sleep(800)

    def lambda_35C0():
        OP_95(0xFE, -58680, 0, -2920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_35C0)
    Sleep(300)

    def lambda_35DD():
        OP_95(0xFE, -57580, 0, -3520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_35DD)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40CA")

    #C0111
    ChrTalk(
        0x101,
        "#0005F#6P这里是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3661")

    #C0112
    ChrTalk(
        0x102,
        (
            "#0101F#6P好像是哈尔特曼议长\x01",
            "的房间吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D6")

    label("loc_3661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_369D")

    #C0113
    ChrTalk(
        0x103,
        (
            "#0201F#6P……记得他们说是\x01",
            "议长的房间……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D6")

    label("loc_369D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_36D6")

    #C0114
    ChrTalk(
        0x104,
        (
            "#0305F#1P记得他们说是议长\x01",
            "那家伙的房间吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D6")


    #C0115
    ChrTalk(
        0x105,
        (
            "#0402F#6P哦，这房间看上去\x01",
            "还真豪华呢──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x105,
        (
            "#0404F#6P……不过，看起来\x01",
            "好像已经有客人先到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()
    OP_68(-57830, 1200, 4080, 2000)
    OP_6F(0x1)

    #N0118
    NpcTalk(
        0x10,
        "轻佻的声音",
        "#11P喂喂，不要抢先察觉到啊。\x02",
    )

    CloseMessageWindow()

    #N0119
    NpcTalk(
        0x10,
        "轻佻的声音",
        (
            "#11P难得的好机会，我还准备\x01",
            "吓你们一跳呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_381F():

        label("loc_381F")

        TurnDirection(0x101, 0x10, 500)
        Yield()
        Jump("loc_381F")

    QueueWorkItem2(0x101, 1, lambda_381F)

    def lambda_3831():

        label("loc_3831")

        TurnDirection(0xEF, 0x10, 500)
        Yield()
        Jump("loc_3831")

    QueueWorkItem2(0xEF, 1, lambda_3831)

    def lambda_3843():

        label("loc_3843")

        TurnDirection(0x105, 0x10, 500)
        Yield()
        Jump("loc_3843")

    QueueWorkItem2(0x105, 1, lambda_3843)

    def lambda_3855():
        OP_95(0xFE, -61300, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3855)
    WaitChrThread(0x10, 1)
    OP_68(-58780, 1200, -1460, 4000)
    OP_93(0x10, 0x87, 0x1F4)

    def lambda_388B():
        OP_96(0xFE, 0xFFFF138E, 0x0, 0x2DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_388B)
    WaitChrThread(0x10, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x1)

    #C0120
    ChrTalk(
        0x101,
        "#0011F#6P雷克特先生……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3906")

    #C0121
    ChrTalk(
        0x102,
        "#0105F#6P你、你怎么会在这里……\x02",
    )

    CloseMessageWindow()
    Jump("loc_396A")

    label("loc_3906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3939")

    #C0122
    ChrTalk(
        0x103,
        "#0205F#6P……你怎么会在这里……\x02",
    )

    CloseMessageWindow()
    Jump("loc_396A")

    label("loc_3939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_396A")

    #C0123
    ChrTalk(
        0x104,
        (
            "#0301F#6P嘁……\x01",
            "竟然隐藏了气息啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396A")

    OP_68(-58540, 1200, -1840, 1500)

    def lambda_3980():
        OP_95(0xFE, -59360, 0, -570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3980)
    WaitChrThread(0x10, 1)
    OP_6F(0x1)

    #C0124
    ChrTalk(
        0x10,
        (
            "#3505F#5P哦，这可真是……\x02\x03",

            "#3504F呼……看来你们也钓上了\x01",
            "很有意思的鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()

    #N0126
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#5805F#12P鱼是指琪雅吗？\x02\x03",

            "#5801F琪雅会被吃掉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x10,
        (
            "#3502F#5P嗯嗯，要被从头到脚\x01",
            "一口吞掉哦！\x02\x03",

            "#3509F啊呜～！我咬我咬！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A6(0x10, 0x14, 0x14, 0x190, 0x7D0)
    Sleep(300)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x10, 0x0, 0x3E8)
    Sleep(500)
    OP_93(0x10, 0x10E, 0x3E8)
    OP_64(0x10)

    #C0128
    ChrTalk(
        0x10,
        (
            "#3507F#11P唔唔，糟了！\x01",
            "卡在喉咙里啦～！\x02",
        )
    )

    CloseMessageWindow()

    #N0129
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#5809F#12P啊哈哈！\x01",
            "这个人，好奇怪哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#0006F#6P关于这一点，我们真是\x01",
            "再清楚不过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x105,
        (
            "#0404F#6P呵呵，『银』也好，\x01",
            "ＩＢＣ的大小姐也好，\x01",
            "你们认识的怪人还真多啊。\x02\x03",

            "#0402F这也是因为你们人缘好吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BC5():
        TurnDirection(0xFE, 0x105, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BC5)
    Sleep(50)

    def lambda_3BD5():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3BD5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0132
    ChrTalk(
        0x101,
        "#0013F#11P这种人缘我可是一点都不喜欢……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3C55")

    #C0133
    ChrTalk(
        0x102,
        (
            "#0111F#5P话说，你也算是个\x01",
            "足够奇怪的人了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD4")

    label("loc_3C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3C9B")

    #C0134
    ChrTalk(
        0x103,
        (
            "#0211F#5P话说，瓦吉先生也算是个\x01",
            "足够奇怪的人了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD4")

    label("loc_3C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3CD4")

    #C0135
    ChrTalk(
        0x104,
        (
            "#0306F#5P话说～你也算是个\x01",
            "足够奇怪的人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD4")

    OP_93(0x10, 0x87, 0x1F4)
    Sleep(300)

    #C0136
    ChrTalk(
        0x10,
        (
            "#3506F#5P喂喂，我说你们啊，\x01",
            "会不会太放松了点～？\x02\x03",

            "#3501F要再多点身为逃亡者的\x01",
            "紧张感才行啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3D77():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D77)

    def lambda_3D84():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3D84)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0137
    ChrTalk(
        0x101,
        (
            "#0012F#6P这个，就算你突然\x01",
            "说出这种正确的道理，我们也……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-58780, 1200, -2750, 1500)
    OP_6F(0x1)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -57500, -1000, -8000, 0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    #N0138
    NpcTalk(
        0x12,
        "男人的声音",
        "#2P#2S喂，找到了吗……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3E8C():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E8C)

    def lambda_3E99():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3E99)
    Sleep(100)

    def lambda_3EA9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3EA9)

    def lambda_3EB6():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3EB6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x10, 1)

    #N0139
    NpcTalk(
        0x12,
        "男人的声音",
        (
            "#2P#2S右侧已经找过了！\x01",
            "接下来只剩左侧了！\x02",
        )
    )

    CloseMessageWindow()

    #N0140
    NpcTalk(
        0x12,
        "男人的声音",
        "#2P#2S议长的房间也要去确认一下！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_68(-58780, 1200, -1840, 1000)

    def lambda_3F59():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3F59)
    Sleep(100)

    def lambda_3F69():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F69)

    def lambda_3F76():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3F76)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x1)

    #C0141
    ChrTalk(
        0x101,
        "#0010F#11P呜……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x10,
        (
            "#3505F#5P……你们在磨蹭什么？\x02\x03",

            "#3504F不是还有我之前藏身的地方吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x10, 500)

    #C0143
    ChrTalk(
        0x101,
        "#0005F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_406D")

    #C0144
    ChrTalk(
        0x102,
        "#0101F#6P没时间犹豫了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_40CA")

    label("loc_406D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_40A0")

    #C0145
    ChrTalk(
        0x103,
        "#0201F#6P看来没时间犹豫了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_40CA")

    label("loc_40A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_40CA")

    #C0146
    ChrTalk(
        0x104,
        "#0301F#6P没时间犹豫啦……！\x02",
    )

    CloseMessageWindow()

    label("loc_40CA")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, -57000, 0, 8000, 180)
    SetChrPos(0xEF, -58000, 0, 8000, 180)
    SetChrPos(0x105, -59000, 0, 8000, 180)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xD, -58000, 0, -5900, 0)
    SetChrPos(0xE, -58000, 0, -5900, 0)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -61000, 0, 4000, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_68(-58000, 1200, 3580, 0)
    MoveCamera(322, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(-58000, 1200, -280, 4000)
    BeginChrThread(0x10, 3, 0, 24)
    Sleep(2000)
    Sound(103, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 26)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x10, 3)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0147
    ChrTalk(
        0xD,
        "#6P这不是雷克特先生吗……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x10,
        (
            "#3504F#11P哦，巡逻辛苦啦。\x02\x03",

            "#3500F宅邸里好像出现了可疑人士，\x01",
            "差不多也该抓到了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xD,
        (
            "#6P还没有……\x01",
            "但这也只是时间问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xE,
        (
            "#6P不过，雷克特先生\x01",
            "怎么会在这里……？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x10,
        (
            "#3503F#11P哦，我在这附近\x01",
            "听到了奇怪的动静……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xE,
        "#6P奇怪的动静……？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xD,
        "#6P难道是入侵者……！？\x02",
    )

    CloseMessageWindow()
    OP_68(-58000, 1200, 3280, 1500)
    OP_93(0x10, 0x0, 0x12C)
    OP_6F(0x1)

    #C0154
    ChrTalk(
        0x10,
        (
            "#3509F#6P喂～出来吧。\x02\x03",

            "不要害怕哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#0013F#11P（呜……要干什么……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_43FD")

    #C0156
    ChrTalk(
        0x102,
        (
            "#0108F#11P（从一开始就打算\x01",
            "  出卖我们吗……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4482")

    label("loc_43FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4440")

    #C0157
    ChrTalk(
        0x103,
        (
            "#0208F#11P（从一开始就打算\x01",
            "  出卖我们吗……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4482")

    label("loc_4440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4482")

    #C0158
    ChrTalk(
        0x104,
        (
            "#0310F#11P（嘁，从一开始就打算\x01",
            "  出卖我们吗……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4482")


    #C0159
    ChrTalk(
        0x105,
        "#0404F#5P（不……）\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(823, 0, 100, 0)
    Sleep(300)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x11, -57150, 0, 2300, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_68(-58000, 1200, 1000, 3500)

    def lambda_450A():

        label("loc_450A")

        TurnDirection(0x10, 0x11, 500)
        Yield()
        Jump("loc_450A")

    QueueWorkItem2(0x10, 1, lambda_450A)

    def lambda_451C():
        OP_95(0xFE, -57000, 0, 1000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_451C)

    def lambda_4536():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4536)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x11, 2)
    OP_93(0x11, 0x10E, 0x1F4)
    EndChrThread(0x10, 0x1)
    OP_6F(0x1)

    #C0160
    ChrTalk(
        0xD,
        "#6P猫……？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x10,
        (
            "#3500F#5P哦，小黑，\x01",
            "不要那么害怕啦。\x02\x03",

            "来～来。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x11, -57200, 0, 1000, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrSubChip(0x10, 0x1)
    Sleep(500)

    #C0162
    ChrTalk(
        0x10,
        (
            "#3509F#5P过来过来……\x01",
            "被大狗追赶，\x01",
            "吓坏你了吧。\x02\x03",

            "#3507F好，对这些黑衣的家伙\x01",
            "抱怨几句吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    OP_68(-58000, 1200, 0, 1200)
    OP_93(0x11, 0xB4, 0x1F4)
    OP_6F(0x1)
    Sound(823, 0, 100, 0)
    Sleep(1000)

    #C0163
    ChrTalk(
        0xD,
        "#6P嘁，真会耍人……\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xE,
        "#6P失陪了……！\x02",
    )

    CloseMessageWindow()

    def lambda_468D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_468D)
    Sleep(100)

    def lambda_469D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_469D)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    #C0165
    ChrTalk(
        0x10,
        (
            "#3505F#11P啊，对了对了，\x01",
            "我刚刚想起来。\x02\x03",

            "#3510F刚才好像在那扇窗口\x01",
            "看到了几个奇怪的人……\x02\x03",

            "嗯～难道那就是所谓的\x01",
            "可疑人士吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4769():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4769)
    Sleep(50)

    def lambda_4779():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4779)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    #C0166
    ChrTalk(
        0xD,
        "#6P奇怪的人！？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        "#6P是怎样的人！？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x10,
        (
            "#3503F#11P好像带着个\x01",
            "小女孩……\x02\x03",

            "#3501F往后院那边去了哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47F9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_47F9)
    Sleep(100)

    def lambda_4809():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4809)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    #C0169
    ChrTalk(
        0xD,
        (
            "#11P不会错……\x01",
            "和目击情报一致！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xE,
        (
            "#6P呜……\x01",
            "什么时候跑到屋外去了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xE,
        "#6P快向副头目报告！\x02",
    )

    CloseMessageWindow()
    OP_68(-58000, 1200, -1500, 2000)
    BeginChrThread(0xE, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 27)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Fade(250)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x10, 0x5)
    SetChrSubChip(0x10, 0x0)
    Sound(820, 0, 100, 0)
    OP_93(0x10, 0xB4, 0x0)
    OP_0D()
    Sleep(1000)
    OP_68(-56670, 1200, 1310, 5000)

    def lambda_4901():

        label("loc_4901")

        TurnDirection(0x10, 0x101, 500)
        Yield()
        Jump("loc_4901")

    QueueWorkItem2(0x10, 1, lambda_4901)

    def lambda_4913():

        label("loc_4913")

        TurnDirection(0x11, 0x101, 500)
        Yield()
        Jump("loc_4913")

    QueueWorkItem2(0x11, 1, lambda_4913)
    BeginChrThread(0x101, 3, 0, 29)
    Sleep(500)
    BeginChrThread(0xEF, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 31)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x105, 3)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    OP_6F(0x1)

    #C0172
    ChrTalk(
        0x105,
        "#0402F#12P呵呵，实在高明呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_49B3")

    #C0173
    ChrTalk(
        0x102,
        (
            "#0111F#12P那只猫，是从一开始\x01",
            "就准备好的吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A33")

    label("loc_49B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_49F1")

    #C0174
    ChrTalk(
        0x103,
        "#0211F#12P那只猫，是一开始就准备好的……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A33")

    label("loc_49F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4A33")

    #C0175
    ChrTalk(
        0x104,
        (
            "#0302F#12P真是的，从一开始\x01",
            "就准备好要演这场戏了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A33")


    #C0176
    ChrTalk(
        0x10,
        (
            "#3504F#5P嗯～……你们在说什么啊？\x02\x03",

            "#3505F哎呀，本该逃到后院去的人\x01",
            "为什么会在这里……？\x02\x03",

            "#3509F世界真奇妙啊～\x02",
        )
    )

    CloseMessageWindow()

    #N0177
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#5809F#11P啊哈哈！\x01",
            "果然是个奇怪的人！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#0012F#12P哈哈……真是帮大忙了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0179
    ChrTalk(
        0x101,
        (
            "#0000F#5P──各位，接下来就赌一把，\x01",
            "去正门那边看看吧……！\x02\x03",

            "有了刚才的误导，\x01",
            "那边的守备说不定已经变得薄弱了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4B9E")

    #C0180
    ChrTalk(
        0x102,
        "#0100F#12P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BE7")

    label("loc_4B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4BC6")

    #C0181
    ChrTalk(
        0x103,
        "#0202F#12P明白……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BE7")

    label("loc_4BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4BE7")

    #C0182
    ChrTalk(
        0x104,
        "#0300F#12P知道啦！\x02",
    )

    CloseMessageWindow()

    label("loc_4BE7")

    OP_57(0x0)
    SetCameraDistance(18750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, -58000, 0, 0, 180)
    SetChrPos(0x10, -54030, 0, 6580, 90)
    SetChrPos(0x11, -52930, 0, 6580, 270)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0xA7, 2)
    OP_29(0x47, 0x1, 0x11)
    VolumeBGM(0x64, 0xBB8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_34C6 end

    def Function_24_4C53(): pass

    label("Function_24_4C53")

    SetChrPos(0x10, -61000, 0, 4000, 180)

    def lambda_4C69():
        OP_95(0xFE, -61000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C69)
    WaitChrThread(0xFE, 1)

    def lambda_4C87():
        OP_95(0xFE, -58000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C87)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_24_4C53 end

    def Function_25_4CA8(): pass

    label("Function_25_4CA8")


    def lambda_4CAD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CAD)
    OP_95(0xFE, -57980, 0, -4080, 4000, 0x1)
    OP_95(0xFE, -58000, 0, -2240, 4000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_25_4CA8 end

    def Function_26_4CED(): pass

    label("Function_26_4CED")


    def lambda_4CF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CF2)
    OP_95(0xFE, -57980, 0, -4080, 4000, 0x1)
    OP_95(0xFE, -58360, 0, -3500, 4000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_4CED end

    def Function_27_4D32(): pass

    label("Function_27_4D32")


    def lambda_4D37():
        OP_95(0xFE, -58000, 0, -5900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D37)
    Sleep(500)

    def lambda_4D54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D54)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_27_4D32 end

    def Function_28_4D69(): pass

    label("Function_28_4D69")

    OP_93(0xFE, 0xB4, 0x320)

    def lambda_4D75():
        OP_95(0xFE, -58000, 0, -5900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D75)
    Sleep(300)

    def lambda_4D92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D92)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_4D69 end

    def Function_29_4DA7(): pass

    label("Function_29_4DA7")


    def lambda_4DAC():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DAC)
    WaitChrThread(0xFE, 1)

    def lambda_4DCA():
        OP_95(0xFE, -55680, 0, 1190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DCA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_29_4DA7 end

    def Function_30_4DEB(): pass

    label("Function_30_4DEB")


    def lambda_4DF0():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DF0)
    WaitChrThread(0xFE, 1)

    def lambda_4E0E():
        OP_95(0xFE, -54290, 0, 200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E0E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_30_4DEB end

    def Function_31_4E2F(): pass

    label("Function_31_4E2F")


    def lambda_4E34():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E34)
    WaitChrThread(0xFE, 1)

    def lambda_4E52():
        OP_95(0xFE, -54730, 0, 2230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E52)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_31_4E2F end

    def Function_32_4E73(): pass

    label("Function_32_4E73")

    EventBegin(0x1)

    #C0183
    ChrTalk(
        0x101,
        (
            "#5103F里面的房间令人在意……\x02\x03",

            "#5101F时间也不多了，\x01",
            "尽快调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 58000, 0, -4000, 0)
    EventEnd(0x4)
    Return()

    # Function_32_4E73 end

    SaveToFile()

Try(main)
