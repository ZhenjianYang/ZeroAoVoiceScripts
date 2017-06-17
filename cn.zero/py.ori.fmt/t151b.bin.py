from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t151b.bin",                # FileName
        "t151b",                    # MapName
        "t151b",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t151b",                  # 0
        "黑手党",                 # 1
        "黑手党",                 # 2
        "玛罗奈",                 # 3
        "巴士的乘客",             # 4
        "巴士的乘客",             # 5
        "巴士的乘客",             # 6
        "巴士的乘客",             # 7
        "巴士的乘客",             # 8
        "玛萨护士长",             # 9
        "琪尔修宿舍长",           # 10
        "警备员托尼",             # 11
        "巴士的司机",             # 12
        "门诊患者",               # 13
        "门诊患者",               # 14
        "bt152b",                 # 15
    ))

    ATBonus("ATBonus_328", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_368", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_400", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_408", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt152b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_368", "MonsterBattlePostion_3E8", "ed7402", "ed7403", "ATBonus_328"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
        "chr/ch25600.itc",                   # 04
        "chr/ch20400.itc",                   # 05
        "chr/ch22102.itc",                   # 06
        "chr/ch21000.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch20300.itc",                   # 09
        "chr/ch29600.itc",                   # 0A
        "chr/ch24300.itc",                   # 0B
        "apl/ch50155.itc",                   # 0C
        "apl/ch50154.itc",                   # 0D
        "chr/ch20000.itc",                   # 0E
        "chr/ch22802.itc",                   # 0F
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(55459,   0,       -2079,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(55909,   0,       1330,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(59330,   449,     -3049,   180,  341,  0x0, 0,   6,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(59130,   0,       -5159,   225,  261,  0x0, 0,   7,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(57900,   0,       -6389,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(52869,   0,       -4570,   0,    261,  0x0, 0,   9,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(52490,   0,       51650,   0,    261,  0x0, 0,   10,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(60090,   0,       55479,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(59909,   449,     53849,   90,   343,  0x0, 1,   12,  0,   255, 255, 0,   12,  255,  0)
    DeclNpc(52569,   449,     53849,   90,   343,  0x0, 1,   13,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(58209,   0,       50250,   270,  261,  0x0, 0,   14,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(52270,   449,     56560,   180,  341,  0x0, 0,   15,  0,   255, 255, 0,   15,  255,  0)

    DeclEvent(0x0000, 0, 22,  6.0,                   4.0,                   -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.0,                  -1.3333333730697632,   0.10000000894069672,   1.0])

    DeclActor(4390,    3750,    16900,   1000,    4390,    5000,    16900,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_4A8",          # 00, 0
        "Function_1_560",          # 01, 1
        "Function_2_5B5",          # 02, 2
        "Function_3_648",          # 03, 3
        "Function_4_674",          # 04, 4
        "Function_5_70C",          # 05, 5
        "Function_6_73A",          # 06, 6
        "Function_7_88A",          # 07, 7
        "Function_8_8F7",          # 08, 8
        "Function_9_936",          # 09, 9
        "Function_10_97D",         # 0A, 10
        "Function_11_CDA",         # 0B, 11
        "Function_12_DE6",         # 0C, 12
        "Function_13_EFD",         # 0D, 13
        "Function_14_F5E",         # 0E, 14
        "Function_15_F9E",         # 0F, 15
        "Function_16_10C9",        # 10, 16
        "Function_17_112D",        # 11, 17
        "Function_18_1629",        # 12, 18
        "Function_19_1A8F",        # 13, 19
        "Function_20_1B0A",        # 14, 20
        "Function_21_221C",        # 15, 21
        "Function_22_28CC",        # 16, 22
    ))


    def Function_0_4A8(): pass

    label("Function_0_4A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4E8"),
        (1, "loc_4F4"),
        (2, "loc_500"),
        (3, "loc_50C"),
        (4, "loc_518"),
        (5, "loc_524"),
        (6, "loc_530"),
        (SWITCH_DEFAULT, "loc_53C"),
    )


    label("loc_4E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_4F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_500")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_50C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_518")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_524")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_530")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_53C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_548")

    label("loc_55F")

    Return()

    # Function_0_4A8 end

    def Function_1_560(): pass

    label("Function_1_560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57B")
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_5B4")

    label("loc_57B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59A")
    Event(0, 20)
    Jump("loc_5B4")

    label("loc_59A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B4")
    Event(0, 21)

    label("loc_5B4")

    Return()

    # Function_1_560 end

    def Function_2_5B5(): pass

    label("Function_2_5B5")

    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62A")
    Call(0, 19)

    label("loc_62A")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_647")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_647")

    Return()

    # Function_2_5B5 end

    def Function_3_648(): pass

    label("Function_3_648")

    TalkBegin(0xFE)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "黑手党成员失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_3_648 end

    def Function_4_674(): pass

    label("Function_4_674")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CD")

    #C0002
    ChrTalk(
        0xFE,
        (
            "和病房楼那边\x01",
            "完全联络不上。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "事务长和塞拉他们\x01",
            "都没事吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_708")

    label("loc_6CD")


    #C0004
    ChrTalk(
        0xFE,
        (
            "和病房楼那边\x01",
            "完全联络不上。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "事务长他们没事吧……\x02",
    )

    CloseMessageWindow()

    label("loc_708")

    TalkEnd(0xFE)
    Return()

    # Function_4_674 end

    def Function_5_70C(): pass

    label("Function_5_70C")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xFE,
        (
            "可恶，\x01",
            "我那在住院的朋友没事吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_70C end

    def Function_6_73A(): pass

    label("Function_6_73A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CE")
    Jump("loc_818")

    label("loc_7CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_818")

    label("loc_7EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_818")

    label("loc_80E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_818")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0007
    ChrTalk(
        0xFE,
        "还好你们来了……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "被关在这种地方，\x01",
            "都不知道会被怎样对待……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_73A end

    def Function_7_88A(): pass

    label("Function_7_88A")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "那、那些穿黑衣的人……\x01",
            "眼神很不正常。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "好像完全感觉不到一丝生气……\x01",
            "总有种令人恐怖的寂静感。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_88A end

    def Function_8_8F7(): pass

    label("Function_8_8F7")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        "可恶……为什么会变成这样！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "我到底做了什么！？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_8F7 end

    def Function_9_936(): pass

    label("Function_9_936")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        "巴士的司机不要紧吧……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "好像正在隔壁的房间接受治疗……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_936 end

    def Function_10_97D(): pass

    label("Function_10_97D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 0)), scpexpr(EXPR_END)), "loc_A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A21")

    #C0015
    ChrTalk(
        0xFE,
        (
            "哦哦，那不是黑衣人\x01",
            "从我这里抢走的钥匙吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "有这个的话，\x01",
            "应该就能进入病房楼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "那边就交给你们了。\x01",
            "救救塞茜尔\x01",
            "和大家吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A7C")

    label("loc_A21")


    #C0018
    ChrTalk(
        0xFE,
        (
            "有那把钥匙的话，\x01",
            "应该就能进入病房楼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "那边就交给你们了。\x01",
            "救救塞茜尔\x01",
            "和大家吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7C")

    Jump("loc_CD6")

    label("loc_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 5)), scpexpr(EXPR_END)), "loc_BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B62")

    #C0020
    ChrTalk(
        0xFE,
        (
            "什么，病房楼的入口\x01",
            "上锁了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "嘁，那些黑衣人，\x01",
            "竟然从里面锁了门……！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……病房楼的钥匙\x01",
            "本来是我拿着的……\x01",
            "可是被黑衣人抢走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "现在只能找出拿着钥匙的家伙，\x01",
            "然后抢回来了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 1)
    SetScenarioFlags(0x0, 1)
    Jump("loc_BF2")

    label("loc_B62")


    #C0024
    ChrTalk(
        0xFE,
        (
            "我拿着的病房楼钥匙\x01",
            "被黑衣人抢走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "黑衣人直接\x01",
            "上了宿舍楼梯，\x01",
            "所以我想他们多半还在楼内。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "只能想办法把他们找出来，\x01",
            "将钥匙夺回了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF2")

    Jump("loc_CD6")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA2")

    #C0027
    ChrTalk(
        0xFE,
        (
            "那些黑衣人……\x01",
            "对我们的职员和病人\x01",
            "做得太过分了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "我也拼命抵抗过，\x01",
            "但是立刻就被打倒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "……病房楼那边就交给你们了，\x01",
            "救救塞茜尔\x01",
            "和大家吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CD6")

    label("loc_CA2")


    #C0030
    ChrTalk(
        0xFE,
        (
            "病房楼那边就交给你们了，\x01",
            "救救塞茜尔\x01",
            "和大家吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD6")

    TalkEnd(0xFE)
    Return()

    # Function_10_97D end

    def Function_11_CDA(): pass

    label("Function_11_CDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7F")
    TurnDirection(0xFE, 0x12, 0)

    #C0031
    ChrTalk(
        0xFE,
        "喂，托尼先生，你振作点！\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "你想啊，多亏有你，\x01",
            "驾驶员先生才不至于\x01",
            "被射中第二枪呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "幸好两人都没有生命危险，\x01",
            "你可要坚强点啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_DE2")

    label("loc_D7F")


    #C0034
    ChrTalk(
        0xFE,
        (
            "唉唉，伤脑筋啊。\x01",
            "这里设备不足，\x01",
            "只能做做应急处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "其他病人也发烧了，\x01",
            "人手完全不够啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE2")

    TalkEnd(0xFE)
    Return()

    # Function_11_CDA end

    def Function_12_DE6(): pass

    label("Function_12_DE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA8")

    #C0036
    ChrTalk(
        0xFE,
        (
            "……你、你们……\x01",
            "竟然这种时候来医院，\x01",
            "也真是够倒霉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "那位驾驶员先生\x01",
            "和我一起反抗那些家伙，\x01",
            "结果被他们用枪打伤了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……可恶！\x01",
            "我这警备员到底有什么用啊……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_EF9")

    label("loc_EA8")


    #C0039
    ChrTalk(
        0xFE,
        (
            "我身为警备员……\x01",
            "竟然会让他们如此轻易地入侵进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "我真是太没用了啊……\x02",
    )

    CloseMessageWindow()

    label("loc_EF9")

    TalkEnd(0xFE)
    Return()

    # Function_12_DE6 end

    def Function_13_EFD(): pass

    label("Function_13_EFD")

    TalkBegin(0xFE)

    #C0041
    ChrTalk(
        0xFE,
        (
            "好痛……！\x01",
            "……呜呜，没想到会被枪击……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "枪口指向我的时候，\x01",
            "还以为彻底完蛋了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_EFD end

    def Function_14_F5E(): pass

    label("Function_14_F5E")

    TalkBegin(0xFE)

    #C0043
    ChrTalk(
        0xFE,
        (
            "……刚预约了傍晚的诊断，\x01",
            "竟然就被卷进这种事件中……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_F5E end

    def Function_15_F9E(): pass

    label("Function_15_F9E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1032")
    Jump("loc_107C")

    label("loc_1032")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1052")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_107C")

    label("loc_1052")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1072")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_107C")

    label("loc_1072")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_107C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0044
    ChrTalk(
        0xFE,
        "这是在做梦，一定是做梦……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_F9E end

    def Function_16_10C9(): pass

    label("Function_16_10C9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "３楼：女性职员宿舍→\x01\x01",
            "←２楼：男性职员宿舍\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_10C9 end

    def Function_17_112D(): pass

    label("Function_17_112D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(-7450, 1000, 12750, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 0, 0, -1300, 0)
    SetChrPos(0x102, 600, 50, -2800, 0)
    SetChrPos(0x103, -600, 50, -2800, 0)
    SetChrPos(0x104, -600, 0, -4300, 0)
    SetChrPos(0x106, 600, 0, -4300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 6500, 0, 9500, 180)
    SetChrPos(0x9, 4500, 0, 9500, 180)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_68(1750, 1000, 4550, 7000)
    Sleep(3000)

    def lambda_12B1():
        OP_95(0xFE, 0, 0, 3700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12B1)

    def lambda_12CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12CB)
    Sleep(50)

    def lambda_12DF():
        OP_95(0xFE, 600, 50, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12DF)

    def lambda_12F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12F9)
    Sleep(50)

    def lambda_130D():
        OP_95(0xFE, -600, 50, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_130D)

    def lambda_1327():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1327)
    Sleep(50)

    def lambda_133B():
        OP_95(0xFE, -600, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_133B)

    def lambda_1355():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1355)
    Sleep(50)

    def lambda_1369():
        OP_95(0xFE, 600, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1369)

    def lambda_1383():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1383)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_13CD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_13CD)
    Sleep(50)

    def lambda_13DD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_13DD)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    def lambda_1406():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1406)

    def lambda_1413():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1413)

    def lambda_1420():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_1420)
    Sleep(100)

    def lambda_1430():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_1430)

    def lambda_143D():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_143D)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x79)
    OP_0D()

    #C0046
    ChrTalk(
        0x101,
        "#0013F#6P呜……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#0301F#6P这么快就出现了啊……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0050
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#12P呼……不由分说吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0051
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0107F#6P来了……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)

    def lambda_15BF():
        OP_95(0xFE, 3650, 0, 6040, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_15BF)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_15E1():
        OP_95(0xFE, 2009, 0, 6190, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_15E1)
    Sleep(500)
    Battle("BattleInfo_408", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    Call(0, 18)
    Return()

    # Function_17_112D end

    def Function_18_1629(): pass

    label("Function_18_1629")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    OP_68(-280, 1100, 3650, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, -440, 0, 5250, 90)
    SetChrPos(0x102, -1750, 0, 5720, 90)
    SetChrPos(0x103, -2900, 0, 3020, 90)
    SetChrPos(0x104, -1020, 0, 3310, 90)
    SetChrPos(0x106, -3540, 0, 4380, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Call(0, 19)
    FadeToBright(1000, 0)
    SetCameraDistance(26500, 2000)
    OP_6F(0x10)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0052
    ChrTalk(
        0x104,
        (
            "#0303F#6P嘁……\x01",
            "还挺难收拾。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0203F#6P果然，几乎完全\x01",
            "感觉不到感情的波动……\x02\x03",

            "#0208F说不定，他们并不是\x01",
            "以自己的意志而行动的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1822():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1822)
    Sleep(50)

    def lambda_1832():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1832)
    Sleep(50)

    def lambda_1842():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1842)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0054
    ChrTalk(
        0x102,
        (
            "#0105F#5P不、不是以\x01",
            "自己的意志而行动……？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0013F#5P这……\x01",
            "也就是说，他们被操纵了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    #C0056
    ChrTalk(
        0x103,
        "#0206F#6P是的……虽然还不能断言。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P东方也存在利用药物及暗示\x01",
            "来操纵他人的『傀儡之术』。\x02\x03",

            "所以这种可能性并非为零吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        "#0106F#5P难、难以置信……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0306F#11P真是令人不舒服的话题啊……\x02\x03",

            "#0301F可是，不管怎么想，\x01",
            "这也不像是加尔西亚那个大叔的风格吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0003F#5P嗯……我知道。\x02\x03",

            "#0013F总之，现在最优先的是\x01",
            "确认院内相关人员的安全。\x02\x03",

            "先在这个住宿设施的\x01",
            "内部调查看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0101F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    SetChrPos(0x0, 0, 0, 4000, 0)
    SetScenarioFlags(0xE0, 4)
    EventEnd(0x5)
    Return()

    # Function_18_1629 end

    def Function_19_1A8F(): pass

    label("Function_19_1A8F")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, 2940, 0, 3630, 225)
    SetChrPos(0x9, 2480, 0, 5210, 315)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_19_1A8F end

    def Function_20_1B0A(): pass

    label("Function_20_1B0A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(57230, 1100, -1820, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19870, 0)
    OP_93(0xA, 0x5A, 0x0)
    SetChrPos(0x101, 47720, 0, 0, 90)
    SetChrPos(0x102, 46520, 0, 600, 90)
    SetChrPos(0x103, 46520, 0, -600, 90)
    SetChrPos(0x104, 45320, 0, -600, 90)
    SetChrPos(0x106, 45320, 0, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(55230, 1100, -1820, 4000)

    def lambda_1C00():
        OP_95(0xFE, 52720, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C00)

    def lambda_1C1A():
        OP_95(0xFE, 51520, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C1A)

    def lambda_1C34():
        OP_95(0xFE, 51520, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C34)

    def lambda_1C4E():
        OP_95(0xFE, 50320, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C4E)

    def lambda_1C68():
        OP_95(0xFE, 50320, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1C68)
    Sleep(1000)

    def lambda_1C85():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C85)
    Sleep(500)

    def lambda_1C99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C99)

    def lambda_1CAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CAA)
    Sleep(500)

    def lambda_1CBE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CBE)

    def lambda_1CCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1CCF)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1DAF():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1DAF)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)

    def lambda_1DC3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1DC3)

    def lambda_1DD0():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DD0)
    Sleep(50)

    def lambda_1DE0():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1DE0)

    def lambda_1DED():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1DED)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xA, 1)

    #N0062
    NpcTalk(
        0xB,
        "年轻男性",
        "#5P呜……！？\x02",
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0xD,
        "中年男性",
        "#11P你、你们是什么人……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E78")

    #C0064
    ChrTalk(
        0x101,
        "#0005F#6P你们是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EA4")

    label("loc_1E78")


    #C0065
    ChrTalk(
        0x101,
        (
            "#0002F#6P太好了……\x01",
            "你们也平安无事吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA4")

    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0066
    ChrTalk(
        0xA,
        (
            "#11P你们……\x01",
            "好像是警察吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0003F#6P嗯，我们是克洛斯贝尔警察局的人。\x02\x03",

            "#0000F察觉到这里的情况有异，\x01",
            "前来确认各位的安全。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0068
    NpcTalk(
        0xC,
        "年轻女性",
        "#5P得、得救了！\x02",
    )

    CloseMessageWindow()

    #N0069
    NpcTalk(
        0xE,
        "穿西装的男子",
        (
            "#11P从巴士里被拖出来的时候，\x01",
            "真不知道会变成怎样……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#0301F#6P#N你们是路中那辆巴士的\x01",
            "乘客吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0071
    ChrTalk(
        0xD,
        "#11P嗯……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        (
            "#11P巴士在行驶途中，突然就被\x01",
            "那些黑衣人挡住了去路。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xB,
        (
            "#5P连、连一句话不说，就用枪指着我们，\x01",
            "一直把我们逼到这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "#5P驾驶员先生试图反抗，\x01",
            "结、结果突然就挨了一枪……！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#0106F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#0003F#6P……请各位暂时\x01",
            "待在这里吧。\x02\x03",

            "#0001F我们一定会保证\x01",
            "大家的安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xB,
        "#5P明、明白了！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        "#5P拜托你们了啊！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 50500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_93(0xB, 0x0, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    OP_93(0xE, 0x2D, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0xE0, 5)
    OP_29(0x4D, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_20_1B0A end

    def Function_21_221C(): pass

    label("Function_21_221C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(56470, 700, 54520, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(23870, 0)
    SetChrPos(0x101, 48100, 0, 50000, 90)
    SetChrPos(0x102, 46900, 0, 50600, 90)
    SetChrPos(0x103, 46900, 0, 49400, 90)
    SetChrPos(0x104, 45700, 0, 50600, 90)
    SetChrPos(0x106, 45700, 0, 49400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 56000, 0, 54040, 180)
    SetChrPos(0x11, 56000, 0, 52770, 0)
    FadeToBright(1000, 0)
    OP_68(54450, 700, 52500, 3000)
    Sleep(150)

    def lambda_2330():
        OP_95(0xFE, 53100, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2330)

    def lambda_234A():
        OP_95(0xFE, 51900, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_234A)

    def lambda_2364():
        OP_95(0xFE, 51900, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2364)

    def lambda_237E():
        OP_95(0xFE, 50700, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_237E)

    def lambda_2398():
        OP_95(0xFE, 50700, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2398)
    Sleep(1000)

    def lambda_23B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23B5)
    Sleep(500)

    def lambda_23C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_23C9)

    def lambda_23DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_23DA)
    Sleep(500)

    def lambda_23EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23EE)

    def lambda_23FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_23FF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    def lambda_2424():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2424)

    def lambda_2431():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2431)

    def lambda_243E():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_243E)
    Sleep(100)

    def lambda_244E():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_244E)

    def lambda_245B():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_245B)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x1)
    OP_0D()
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_250B():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_250B)
    Sleep(30)

    def lambda_251B():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_251B)
    Sleep(300)

    #C0079
    ChrTalk(
        0x10,
        "#5P你们……！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x11,
        "#11P好像是警察局的……！\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0002F#12P护士长……\x01",
            "您没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        "#0202F#12P……太好了……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x10,
        "#5P你们怎么会在这里……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x10,
        (
            "#5P难道说，\x01",
            "外面已经安全了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#0106F#6P不……我们也是\x01",
            "刚刚才来的。\x02\x03",

            "#0101F目前正在确认院内人士的安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x10,
        "#5P是吗……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0301F#6P看起来，好像\x01",
            "有伤员啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x10,
        (
            "#5P嗯……\x01",
            "是我们的警备员和巴士的司机。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x10,
        (
            "#5P被那些黑衣人用枪打了……\x01",
            "但已经做好了应急处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0006F#12P是吗……\x02\x03",

            "#0001F塞茜尔姐姐和其他人\x01",
            "还在病房楼那边吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x10,
        (
            "#5P嗯，因为事件发生时刚好是工作时间，\x01",
            "所以病房楼内应该还有很多人。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x10,
        (
            "#5P我正好在休息，\x01",
            "才会来这边……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x10,
        (
            "#5P呜，在这么关键的时刻，\x01",
            "我竟然离开了病房楼……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        "#0208F#12P护士长……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#0003F#12P……请您放心。\x02\x03",

            "#0013F我们一定会救出\x01",
            "塞茜尔姐姐和其他人的！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        (
            "#0101F#6P护士长，请你们\x01",
            "留在这里照看\x01",
            "受伤的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x10,
        "#5P明白了……拜托你们了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 50500, 0, 50000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10, 52490, 0, 51650, 0)
    SetChrPos(0x11, 60090, 0, 55480, 180)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0xE0, 6)
    OP_29(0x4D, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_21_221C end

    def Function_22_28CC(): pass

    label("Function_22_28CC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2932")

    #C0098
    ChrTalk(
        0x101,
        (
            "#0001F刚才的黑手党们\x01",
            "好像在看守\x01",
            "一楼的住宿设施。\x02\x03",

            "先去那边调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2974")

    label("loc_2932")


    #C0099
    ChrTalk(
        0x101,
        (
            "#0001F……住宿设施内\x01",
            "应该还有一个房间。\x01",
            "也去那里调查看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2974")

    Sleep(50)
    SetChrPos(0x0, 4059, 0, 3600, 270)
    EventEnd(0x4)
    Return()

    # Function_22_28CC end

    SaveToFile()

Try(main)
