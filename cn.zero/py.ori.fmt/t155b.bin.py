from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t155b.bin",                # FileName
        "t155b",                    # MapName
        "t155b",                    # Location
        0x0052,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 82, 0, 1, 0, 2],
    )

    BuildStringList((
        "t155b",                  # 0
        "黑手党",                 # 1
        "黑手党",                 # 2
        "菲莉亚护士",             # 3
        "实习医生利顿",           # 4
        "勤杂工戴森",             # 5
        "盖巴尔议员",             # 6
        "盖巴尔议员",             # 7
        "塞茜尔",                 # 8
        "米海尔",                 # 9
        "拉格教授",               # 10
        "盖里教授",               # 11
        "阿修拉主任",             # 12
        "bt154b",                 # 13
    ))

    ATBonus("ATBonus_374", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_454", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 11, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_468", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_438", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_440", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_444", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_448", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_44C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_474", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31103.dat", "ms31003.dat", "ms31003.dat", "ms67101.dat", 0, 0, 0, 0, "MonsterBattlePostion_454", "MonsterBattlePostion_434", "ed7402", "ed7403", "ATBonus_374"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
        "apl/ch50363.itc",                   # 01
        "chr/ch29900.itc",                   # 02
        "chr/ch29400.itc",                   # 03
        "apl/ch50153.itc",                   # 04
        "chr/ch33602.itc",                   # 05
        "chr/ch05300.itc",                   # 06
        "apl/ch50144.itc",                   # 07
        "chr/ch29202.itc",                   # 08
        "chr/ch32702.itc",                   # 09
        "chr/ch32900.itc",                   # 0A
        "chr/ch33600.itc",                   # 0B
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-55169,  0,       -50069,  0,    261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-55930,  0,       -49529,  0,    261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-55549,  379,     -47700,  90,   342,  0x0, 1,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(54200,   -300,    -2799,   270,  389,  0x0, 0,   11,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-54500,  250,     -52330,  270,  468,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(6519,    0,       -48889,  0,    389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6150,    400,     -47400,  0,    468,  0x0, 0,   7,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-102150, 250,     -4730,   180,  469,  0x0, 0,   8,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-102150, 250,     -7550,   0,    469,  0x0, 0,   9,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-100489, 0,       -6130,   270,  389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)

    DeclEvent(0x0000, 0, 15,  -1.5,                  9.0,                   -1.0,                  110.25,                [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.5,                   -1.2857143878936768,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 29,  -9.0,                  21.0,                  0.0,                   110.25,                [0.1428571492433548,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.2857143878936768,    -7.0,                  -0.0,                  1.0])

    DeclActor(-6230,   0,       14490,   1200,    -6230,   1500,    14490,   0x007C, 0,  28, 0x0000)
    DeclActor(5240,    0,       -48080,  1200,    6340,    1500,    -47750,  0x007E, 0,  11, 0x0000)

    ScpFunction((
        "Function_0_530",          # 00, 0
        "Function_1_5E8",          # 01, 1
        "Function_2_699",          # 02, 2
        "Function_3_73E",          # 03, 3
        "Function_4_76A",          # 04, 4
        "Function_5_89F",          # 05, 5
        "Function_6_963",          # 06, 6
        "Function_7_988",          # 07, 7
        "Function_8_99A",          # 08, 8
        "Function_9_C5D",          # 09, 9
        "Function_10_F05",         # 0A, 10
        "Function_11_119E",        # 0B, 11
        "Function_12_11E1",        # 0C, 12
        "Function_13_140D",        # 0D, 13
        "Function_14_160D",        # 0E, 14
        "Function_15_170F",        # 0F, 15
        "Function_16_1AF5",        # 10, 16
        "Function_17_1B70",        # 11, 17
        "Function_18_251A",        # 12, 18
        "Function_19_28D5",        # 13, 19
        "Function_20_2933",        # 14, 20
        "Function_21_2991",        # 15, 21
        "Function_22_29EF",        # 16, 22
        "Function_23_2A4D",        # 17, 23
        "Function_24_2AAB",        # 18, 24
        "Function_25_2AF9",        # 19, 25
        "Function_26_341D",        # 1A, 26
        "Function_27_34C5",        # 1B, 27
        "Function_28_38B7",        # 1C, 28
        "Function_29_38DF",        # 1D, 29
    ))


    def Function_0_530(): pass

    label("Function_0_530")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_570"),
        (1, "loc_57C"),
        (2, "loc_588"),
        (3, "loc_594"),
        (4, "loc_5A0"),
        (5, "loc_5AC"),
        (6, "loc_5B8"),
        (SWITCH_DEFAULT, "loc_5C4"),
    )


    label("loc_570")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_57C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_588")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_594")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D0")

    label("loc_5E7")

    Return()

    # Function_0_530 end

    def Function_1_5E8(): pass

    label("Function_1_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_5FB")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_600")

    label("loc_5FB")

    ClearChrFlags(0xD, 0x80)

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_END)), "loc_62B")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_62B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64B")
    SetScenarioFlags(0xE6, 6)
    Jump("loc_689")

    label("loc_64B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66F")
    Event(0, 18)
    Jump("loc_689")

    label("loc_66F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_689")
    Event(0, 17)

    label("loc_689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_698")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)

    label("loc_698")

    Return()

    # Function_1_5E8 end

    def Function_2_699(): pass

    label("Function_2_699")

    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)

    label("loc_6C6")

    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_709")
    Call(0, 16)

    label("loc_709")

    ClearMapObjFlags(0x0, 0x10)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_720")
    OP_66(0x1, 0x1)

    label("loc_720")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_73D")

    Return()

    # Function_2_699 end

    def Function_3_73E(): pass

    label("Function_3_73E")

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

    # Function_3_73E end

    def Function_4_76A(): pass

    label("Function_4_76A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_86E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_817")

    #C0002
    ChrTalk(
        0xFE,
        "盖巴尔先生刚才回来了～\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "我还以为他一定会为\x01",
            "床位被占的事情而大发雷霆呢，\x01",
            "结果看上去却很消沉……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "看到他那么郁闷，\x01",
            "真是有点同情呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_869")

    label("loc_817")


    #C0005
    ChrTalk(
        0xFE,
        (
            "盖巴尔先生回到病房以后\x01",
            "就一直那样沮丧。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "到底遇到了什么\x01",
            "可怕的事情呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_869")

    Jump("loc_89B")

    label("loc_86E")


    #C0007
    ChrTalk(
        0xFE,
        (
            "在这种时候，盖巴尔先生\x01",
            "到底去了哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89B")

    TalkEnd(0xFE)
    Return()

    # Function_4_76A end

    def Function_5_89F(): pass

    label("Function_5_89F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_907")

    #C0008
    ChrTalk(
        0xFE,
        (
            "本想让戴森先生\x01",
            "早点接受\x01",
            "正式的治疗……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "可是这间病房的\x01",
            "设备实在是太匮乏了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95F")

    label("loc_907")


    #C0010
    ChrTalk(
        0xFE,
        (
            "总之，情况暂时稳定下来了……\x01",
            "但好像发烧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "暂时还要痛苦一阵子吧，\x01",
            "好可怜……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95F")

    TalkEnd(0xFE)
    Return()

    # Function_5_89F end

    def Function_6_963(): pass

    label("Function_6_963")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        "……呜、呜呜………………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_963 end

    def Function_7_988(): pass

    label("Function_7_988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_999")
    Call(0, 25)

    label("loc_999")

    Return()

    # Function_7_988 end

    def Function_8_99A(): pass

    label("Function_8_99A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2E")
    Jump("loc_A78")

    label("loc_A2E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A4E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A78")

    label("loc_A4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A78")

    label("loc_A6E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A78")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B99")

    #C0013
    ChrTalk(
        0xFE,
        (
            "啊啊……\x01",
            "我到底该怎么办好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "竟然实行了这么大胆的暗杀行动，\x01",
            "一定无处可逃了……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#0200F（在和妄想作战呢……）\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0103F（要是知道\x01",
            "  哈尔特曼议长人后的一面，\x01",
            "  这种反应也不是不可理解……）\x02\x03",

            "#0108F（……可怜的人……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_C55")

    label("loc_B99")


    #C0017
    ChrTalk(
        0xFE,
        (
            "……唉，既然如此，\x01",
            "干脆就向哈尔特曼议长掀起反旗吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "只要公开这个暗杀事件，\x01",
            "舆论就会站在我这边………………\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "…………不行。\x01",
            "这点小事，哈尔特曼议长\x01",
            "一定可以完全抹消掉吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C55")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_99A end

    def Function_9_C5D(): pass

    label("Function_9_C5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C72")
    Call(0, 10)
    Jump("loc_F01")

    label("loc_C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAA")

    #C0020
    ChrTalk(
        0xF,
        (
            "#1302F那个……你也在\x01",
            "协助罗伊德他们吧。\x02\x03",

            "#1309F刚才真是谢谢你了。\x01",
            "多亏了你，我们才能得救。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F……呵……\x01",
            "我不过是顺应形势，才会助他们一臂之力。\x02\x03",

            "要道谢的话，还是谢他们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xF,
        (
            "#1305F（……哎呀，\x01",
            "  这个人，好像曾在哪里……？）\x02\x03",

            "#1300F（……不，\x01",
            "  应该只是心理作用吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 0)
    Jump("loc_F01")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8D")

    #C0023
    ChrTalk(
        0xF,
        (
            "#1301F话说回来……\x01",
            "虽然已经听罗伊德说了，\x01",
            "但我直到现在都还难以相信呢。\x02\x03",

            "没想到那个约亚西姆医生\x01",
            "竟然会做出这么疯狂的事情……\x02\x03",

            "#1303F虽然他玩心很重，又爱偷懒，\x01",
            "但我一直都觉得他是个\x01",
            "深受病人爱戴的好医生……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F01")

    label("loc_E8D")


    #C0024
    ChrTalk(
        0xF,
        (
            "#1303F没想到那个约亚西姆医生\x01",
            "竟然会做出这么疯狂的事情……\x02\x03",

            "#1308F他在医院里的种种表现，\x01",
            "难道全都是在演戏吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F01")

    TalkEnd(0xFE)
    Return()

    # Function_9_C5D end

    def Function_10_F05(): pass

    label("Function_10_F05")

    EventBegin(0x0)
    Fade(500)
    OP_68(5950, 1000, -48900, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 5000, 0, -48900, 45)
    SetChrPos(0x102, 4130, 0, -49060, 45)
    SetChrPos(0x103, 3790, 0, -48130, 90)
    SetChrPos(0x104, 3320, 0, -47550, 90)
    SetChrPos(0x106, 5890, 0, -50380, 0)
    OP_93(0xF, 0x0, 0x0)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0025
    ChrTalk(
        0xF,
        (
            "#1302F……呼……\x01",
            "米海尔服下的药似乎起效了，\x01",
            "已经熟睡了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#0000F是吗，太好了……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xF, 400)

    #C0027
    ChrTalk(
        0x101,
        (
            "#0005F（对了，大哥的警徽……）\x02\x03",

            "#0008F（取回了大哥的遗物这件事，\x01",
            "  是不是也该告诉塞茜尔姐姐……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0028
    ChrTalk(
        0x101,
        (
            "#0006F（……不对，我在想什么呢！）\x02\x03",

            "（大家现在都已经精疲力尽了，\x01",
            "  不能再加重她的负担。）\x02\x03",

            "#0008F（等这件事情结束以后，\x01",
            "  再慢慢和塞茜尔姐姐说吧……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    #C0029
    ChrTalk(
        0xF,
        "#1305F……罗伊德，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0000F……不，没什么啦。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5000, 0, -48900, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xEC, 7)
    EventEnd(0x5)
    Return()

    # Function_10_F05 end

    def Function_11_119E(): pass

    label("Function_11_119E")

    TalkBegin(0x10)

    #C0031
    ChrTalk(
        0x10,
        "呼～……呼～……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "因为药物作用，似乎睡得很熟。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_11_119E end

    def Function_12_11E1(): pass

    label("Function_12_11E1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1275")
    Jump("loc_12BF")

    label("loc_1275")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1295")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12BF")

    label("loc_1295")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12B5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12BF")

    label("loc_12B5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12BF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C2")

    #C0033
    ChrTalk(
        0xFE,
        (
            "……的确，在约亚西姆的履历中，\x01",
            "有几个很不透明的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "出身于雷米菲利亚公国，\x01",
            "在药物学·神经科的研究中获得了重大成果……\x01",
            "……然后呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……仔细想想的话，关于他的事情，\x01",
            "我们似乎毫无了解。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1405")

    label("loc_13C2")


    #C0036
    ChrTalk(
        0xFE,
        "约亚西姆的才能、人品……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "我们或许只看到了\x01",
            "他的表面而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1405")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_11E1 end

    def Function_13_140D(): pass

    label("Function_13_140D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14A1")
    Jump("loc_14EB")

    label("loc_14A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14C1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14EB")

    label("loc_14C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14EB")

    label("loc_14E1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14EB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1599")

    #C0038
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "研究楼里弥漫的\x01",
            "那股浑浊的空气究竟是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "要是扩散到病房楼来的话，\x01",
            "难保不会加重患者们的病情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1605")

    label("loc_1599")


    #C0040
    ChrTalk(
        0xFE,
        (
            "研究楼里弥漫的\x01",
            "那股浑浊的空气到底是……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "虽然每天从早到晚地研究，\x01",
            "但难以理解的事情还是有很多啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1605")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_140D end

    def Function_14_160D(): pass

    label("Function_14_160D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A5")

    #C0042
    ChrTalk(
        0xFE,
        (
            "带着魔兽的人\x01",
            "登上了研究楼的四层。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "他没有穿黑衣服，\x01",
            "我想大概不是黑手党。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "但若无其事地带领魔兽的样子\x01",
            "实在是很诡异……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_170B")

    label("loc_16A5")


    #C0045
    ChrTalk(
        0xFE,
        (
            "上了研究楼四层的那个人……\x01",
            "我想大概不是黑手党。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "但若无其事地带领魔兽的样子\x01",
            "实在是很诡异……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_170B")

    TalkEnd(0xFE)
    Return()

    # Function_14_160D end

    def Function_15_170F(): pass

    label("Function_15_170F")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
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
    OP_68(-9000, 1000, 9000, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, -4800, 0, 9600, 270)
    SetChrPos(0x102, -4800, 0, 8300, 270)
    SetChrPos(0x103, -3500, 0, 8300, 270)
    SetChrPos(0x104, -3500, 0, 9600, 270)
    SetChrPos(0x106, -2200, 0, 8950, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -8430, 0, 21350, 180)
    SetChrPos(0x9, -9590, 0, 21100, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(23500, 3000)

    def lambda_185E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_185E)
    Sleep(50)

    def lambda_1876():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1876)
    Sleep(50)

    def lambda_188E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_188E)
    Sleep(50)

    def lambda_18A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18A6)
    Sleep(50)

    def lambda_18BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_18BE)
    WaitChrThread(0x101, 1)
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
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1958():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1958)
    Sleep(50)

    def lambda_1968():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1968)
    Sleep(50)

    def lambda_1978():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1978)
    Sleep(50)

    def lambda_1988():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1988)
    Sleep(50)

    def lambda_1998():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1998)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    Fade(500)
    OP_68(-8850, 1000, 16000, 0)
    OP_68(-8850, 1000, 10500, 1500)
    SetCameraDistance(25500, 0)
    SetCameraDistance(19500, 1500)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_1A08():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A08)

    def lambda_1A1D():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A1D)
    Sleep(500)
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
    Sleep(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    Battle("BattleInfo_474", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 16)
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
    SetChrPos(0x0, -8500, 0, 8500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE2, 3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_170F end

    def Function_16_1AF5(): pass

    label("Function_16_1AF5")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x1)
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
    SetChrPos(0x8, -8580, 0, 14110, 315)
    SetChrPos(0x9, -11600, 0, 11420, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_16_1AF5 end

    def Function_17_1B70(): pass

    label("Function_17_1B70")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-52500, 1000, -50000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -49550, 50, -49660, 270)
    SetChrPos(0x102, -49550, 50, -50640, 270)
    SetChrPos(0x103, -48250, 50, -50640, 270)
    SetChrPos(0x104, -48250, 50, -49660, 270)
    SetChrPos(0x106, -46950, 50, -50160, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -56730, 0, -50110, 0)
    SetChrPos(0xB, -55580, 0, -49500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_68(-54000, 1000, -50000, 3000)

    def lambda_1CDB():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CDB)
    Sleep(50)

    def lambda_1CF3():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CF3)
    Sleep(50)

    def lambda_1D0B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D0B)
    Sleep(50)

    def lambda_1D23():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D23)
    Sleep(50)

    def lambda_1D3B():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1D3B)
    Sleep(200)

    def lambda_1D53():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D53)

    def lambda_1D64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D64)
    Sleep(100)

    def lambda_1D78():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D78)
    Sleep(50)

    def lambda_1D88():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D88)
    Sleep(350)

    def lambda_1D98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1D98)

    def lambda_1DA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DA9)
    Sleep(500)

    def lambda_1DBD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1DBD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    #C0047
    ChrTalk(
        0xA,
        (
            "#3P啊啊～！\x01",
            "警察弟弟和兰迪先生！？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0302F#11P哈哈……\x01",
            "菲莉亚，你没事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "#6P你们是克洛斯贝尔警察局的……\x01",
            "莫非已经安全了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F#11P不，入侵者目前\x01",
            "仍然在医院内。\x02\x03",

            "#0013F话说回来，这位是……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "#3P嗯……\x01",
            "是勤杂工戴森先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        (
            "#3P被那些家伙\x01",
            "砍成了重伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "#6P我给他做了应急处理，\x01",
            "应该没有生命危险……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        "#6P但暂时还不能放松警惕呢。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#0006F#11P……是吗……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#0105F#11P这么说来……\x01",
            "这间病房的病人去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "#3P这里本来是个名叫盖巴尔的\x01",
            "议员大叔所住的病房……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "#3P嗯～这种时候，\x01",
            "他到底跑到哪里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xA,
        (
            "#3P不过，反正他一直都是\x01",
            "装病住院的，\x01",
            "我想应该不用担心～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0003F#11P总、总之，我们也会\x01",
            "去确认一下他的安危。\x02\x03",

            "#0005F……对了，菲莉亚小姐。\x02\x03",

            "#0001F您知道塞茜尔姐姐\x01",
            "在哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        "#3P塞茜尔前辈～？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "#3P嗯，我想大概是回\x01",
            "护士中心了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "#6P不，我记得塞茜尔\x01",
            "是到３０１号室的\x01",
            "米海尔那里去了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            "#6P她说因为小滴今天外出，\x01",
            "怕米海尔一个人寂寞，\x01",
            "所以要去给他读图画书……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_END)), "loc_23F3")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0065
    ChrTalk(
        0x103,
        (
            "#0205F#11P３０１号室，\x01",
            "就是在来这里的途中\x01",
            "曾经进去过的单人病房吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        "#0301F#11P嗯，但那里连一个人都没有啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0xA,
        "#3P真、真的吗～！？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        "#6P那、那是去了哪里呢……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#0008F#11P……塞茜尔姐姐和米海尔\x01",
            "由我们来寻找。\x02\x03",

            "#0013F请两位专心\x01",
            "治疗伤员吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        "#6P嗯，好的……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        "#3P那就拜托你们了哦～！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_24BB")

    label("loc_23F3")


    #C0072
    ChrTalk(
        0x103,
        (
            "#0205F#11P３０１号室就是\x01",
            "途中经过的那间单人病房吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#0006F#11P嗯，我们在来的路上\x01",
            "曾经从那里经过。\x02\x03",

            "#0000F我们会去确认一下的，\x01",
            "请两位专心\x01",
            "治疗伤员吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        "#6P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        "#3P嗯，放心吧～！\x02",
    )

    CloseMessageWindow()

    label("loc_24BB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -53190, 0, -50010, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xA, -55170, 0, -50070, 0)
    SetChrPos(0xB, -55930, 0, -49530, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE2, 4)
    OP_29(0x4D, 0x1, 0xA)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_1B70 end

    def Function_18_251A(): pass

    label("Function_18_251A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3300, 1000, -50000, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -800, 0, -50000, 90)
    SetChrPos(0x102, -800, 0, -50000, 90)
    SetChrPos(0x103, -800, 0, -50000, 90)
    SetChrPos(0x104, -800, 0, -50000, 90)
    SetChrPos(0x106, -800, 0, -50000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(4700, 1000, -50000, 3000)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 20)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(600)
    BeginChrThread(0x106, 3, 0, 23)
    WaitChrThread(0x101, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_END)), "loc_268C")

    #C0076
    ChrTalk(
        0x101,
        "#0001F#6P果然没人吗……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#0106F#6P该不会是藏在\x01",
            "床底下了吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2728")

    label("loc_268C")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0078
    ChrTalk(
        0x101,
        "#0005F#6P咦、咦……？\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#0301F#6P没人吗……\x01",
            "这里是３０１号室吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#0101F#6P应该没错……\x02\x03",

            "#0108F不会是藏在\x01",
            "床底下了吧……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2728")


    #C0081
    ChrTalk(
        0x103,
        (
            "#0201F#6P如果是那样的话，\x01",
            "我能察觉得到……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x106)
    OP_68(5790, 1000, -49750, 2500)
    BeginChrThread(0x106, 3, 0, 24)
    WaitChrThread(0x106, 3)
    OP_6F(0x1)
    Sound(820, 0, 100, 0)
    Sleep(1000)

    #C0082
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#11P……还留有温度。\x02\x03",

            "看来，这个房间的主人\x01",
            "不久前还在这里。\x02\x03",

            "和那个叫塞茜尔的护士一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F#6P呜……\x01",
            "总之，赶快去找吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        "#0307F#6P嗯……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    OP_68(3000, 1000, -50000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 3000, 0, -50000, 90)
    SetChrPos(0x1, 3000, 0, -50000, 90)
    SetChrPos(0x2, 3000, 0, -50000, 90)
    SetChrPos(0x3, 3000, 0, -50000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE2, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_251A end

    def Function_19_28D5(): pass

    label("Function_19_28D5")


    def lambda_28DA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28DA)

    def lambda_28EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28EF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2908():
        OP_95(0xFE, 3090, 0, -49370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2908)
    WaitChrThread(0x101, 1)

    def lambda_2926():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2926)
    WaitChrThread(0x101, 1)
    Return()

    # Function_19_28D5 end

    def Function_20_2933(): pass

    label("Function_20_2933")


    def lambda_2938():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2938)

    def lambda_294D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_294D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2966():
        OP_95(0xFE, 2350, 0, -51300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2966)
    WaitChrThread(0xFE, 1)

    def lambda_2984():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2984)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_2933 end

    def Function_21_2991(): pass

    label("Function_21_2991")


    def lambda_2996():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2996)

    def lambda_29AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29AB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_29C4():
        OP_95(0xFE, 2420, 0, -48520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29C4)
    WaitChrThread(0xFE, 1)

    def lambda_29E2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29E2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_2991 end

    def Function_22_29EF(): pass

    label("Function_22_29EF")


    def lambda_29F4():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29F4)

    def lambda_2A09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A09)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2A22():
        OP_95(0xFE, 1330, 0, -48080, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A22)
    WaitChrThread(0xFE, 1)

    def lambda_2A40():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A40)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_29EF end

    def Function_23_2A4D(): pass

    label("Function_23_2A4D")


    def lambda_2A52():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A52)

    def lambda_2A67():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A67)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_2A80():
        OP_95(0xFE, 1320, 50, -50150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A80)
    WaitChrThread(0xFE, 1)

    def lambda_2A9E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A9E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_2A4D end

    def Function_24_2AAB(): pass

    label("Function_24_2AAB")


    def lambda_2AB0():
        OP_95(0xFE, 4950, 0, -50540, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AB0)
    WaitChrThread(0xFE, 1)

    def lambda_2ACE():
        OP_95(0xFE, 5950, 0, -48890, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ACE)
    WaitChrThread(0xFE, 1)

    def lambda_2AEC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AEC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_2AAB end

    def Function_25_2AF9(): pass

    label("Function_25_2AF9")

    EventBegin(0x0)
    OP_4B(0xD, 0xFF)
    Fade(1000)
    OP_68(54550, 1300, -1040, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 54580, 0, -1490, 180)
    SetChrPos(0x102, 54860, 0, -360, 180)
    SetChrPos(0x103, 54100, 0, 400, 180)
    SetChrPos(0x104, 54810, 0, 1280, 180)
    SetChrPos(0x106, 54100, 0, 2190, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xD, 54620, 0, -2970, 0)
    OP_0D()

    #C0085
    ChrTalk(
        0x101,
        "#0005F#5P咦……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_9C(0xD, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0086
    ChrTalk(
        0xD,
        "#2P呜、呜咿咿……！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xD,
        (
            "#2P求你们，求求你们了，\x01",
            "饶命啊～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#0301F#5P这大叔是谁啊……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#0106F#5P帝国派的盖巴尔议员……\x01",
            "就是菲莉亚小姐说的那个人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xD)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0090
    ChrTalk(
        0xD,
        "#2P你、你们是什么人……！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xD,
        "#2P不是黑手党吗！？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0003F#5P我们是克洛斯贝尔警察局·特别\x01",
            "任务支援科的人。\x02\x03",

            "#0001F盖巴尔议员，您在这里做什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xD,
        (
            "#2P当、当然是\x01",
            "在藏身了！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xD,
        (
            "#2P那些黑手党们\x01",
            "一定是来杀我的！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xD,
        (
            "#2P哈尔特曼议长……\x01",
            "没想到会用这种手段\x01",
            "来了结我……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0096
    ChrTalk(
        0x101,
        "#0008F#5P（艾莉，你怎么看……？）\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        (
            "#0106F#5P（……我认为这完全是他的被害妄想。）\x02\x03",

            "#0111F（议长大概根本\x01",
            "  就不重视这个人。）\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        "#0206F#5P（嗯，就是这种感觉吧。）\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xD,
        (
            "#2P对、对了，你们几个！\x01",
            "赶快带着我逃离这里吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xD,
        "#2P我还不想死！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#0003F#5P……很不巧，还有其他人\x01",
            "在等着我们。\x02\x03",

            "#0001F我们必须要去\x01",
            "确认他们的安危才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0100F#5P您能先回自己的\x01",
            "房间中等候吗？\x02\x03",

            "这一带的黑手党都被我们制服了，\x01",
            "应该可以安全移动。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xD,
        (
            "#2P你、你、你们……\x01",
            "你们以为我是谁啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xD,
        (
            "#2P我可是代表着克洛斯贝尔自治州的\x01",
            "重要议员之一啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P……好吵的人，\x01",
            "要让他小睡一下吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0106
    ChrTalk(
        0xD,
        "#2P你、你是什么人……！？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        (
            "#2P那、那身打扮……\x01",
            "好像在哪里听过似的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P呵呵……是在哪里听过呢？\x02\x03",

            "该不会是关于『黑月』的\x01",
            "诡异传闻吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0109
    ChrTalk(
        0xD,
        "#2P呜，难道你是……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0006F#5P……不要\x01",
            "再耍弄他了。\x02\x03",

            "#0013F──议员，\x01",
            "如今的事态非常紧急。\x02\x03",

            "请您合作一下，\x01",
            "到房间里去避难吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xD,
        "#2P知、知、知道了……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xD,
        (
            "#2P要给我尽快把黑手党们\x01",
            "都赶走啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(56620, 500, 2080, 0)
    MoveCamera(70, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28000, 0)
    SetCameraDistance(27000, 2500)
    SetChrPos(0x101, 54770, 0, 2600, 270)
    SetChrPos(0x102, 55470, 0, 3170, 270)
    SetChrPos(0x103, 55830, 0, 2100, 270)
    SetChrPos(0x104, 56450, 0, 2800, 270)
    SetChrPos(0x106, 57130, 0, 2110, 270)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0xD, 3, 0, 26)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    Sound(107, 0, 100, 0)
    Sleep(500)

    #C0113
    ChrTalk(
        0x104,
        (
            "#0300F#5P哎呀呀，跑得那么快，\x01",
            "哪像个住院患者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#0211F#11P是啊，他好像只是\x01",
            "装病住院的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3384")

    #C0115
    ChrTalk(
        0x101,
        (
            "#0006F#5P──耽误了不少时间，\x01",
            "赶快去找塞茜尔姐姐吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BE")

    label("loc_3384")


    #C0116
    ChrTalk(
        0x101,
        (
            "#0006F#5P──耽误了不少时间，\x01",
            "赶快前往研究楼那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BE")


    #C0117
    ChrTalk(
        0x102,
        "#0101F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 50910, 0, 110, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetScenarioFlags(0xE2, 6)
    OP_29(0x4D, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_2AF9 end

    def Function_26_341D(): pass

    label("Function_26_341D")

    SetChrPos(0xFE, 54490, 0, 1290, 225)

    def lambda_3433():
        OP_95(0xFE, 53490, 0, 2450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3433)
    WaitChrThread(0xFE, 1)

    def lambda_3451():
        OP_95(0xFE, 51600, 0, 2360, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3451)
    WaitChrThread(0xFE, 1)

    def lambda_346F():
        OP_95(0xFE, 51080, 0, 40, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_346F)
    WaitChrThread(0xFE, 1)

    def lambda_348D():
        OP_95(0xFE, 48880, 0, 20, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_348D)
    Sound(107, 0, 100, 0)
    Sleep(200)

    def lambda_34B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34B0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_341D end

    def Function_27_34C5(): pass

    label("Function_27_34C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(5290, 2000, -50030, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21610, 0)
    SetChrPos(0x101, 4600, 0, -50000, 90)
    SetChrPos(0x102, 3600, 0, -49400, 90)
    SetChrPos(0x103, 3600, 0, -50600, 90)
    SetChrPos(0x104, 2200, 0, -49400, 90)
    SetChrPos(0x106, 2200, 0, -50600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetChrPos(0xF, 6200, 0, -50000, 270)
    FadeToBright(1000, 0)
    OP_68(5290, 1000, -50030, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    #C0118
    ChrTalk(
        0xF,
        (
            "#1306F#11P是吗……\x01",
            "发生了那样的事情，所以你们才来医院啊。\x02\x03",

            "#1308F难道说，是约亚西姆医生……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0006F#6P……目前还不能证明\x01",
            "他有嫌疑。\x02\x03",

            "#0001F他还在研究楼里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xF,
        (
            "#1303F#11P这倒不清楚……\x02\x03",

            "#1301F不过，可能还有其他几名教授\x01",
            "留在研究楼里呢。\x02\x03",

            "因为那些黑衣人带出来的\x01",
            "全都是实习医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#0003F#6P是吗……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        (
            "#0301F#6P对了，刚才的魔兽\x01",
            "到底是什么啊？\x02\x03",

            "感觉好诡异～……\x01",
            "或者说是不明底细。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#0208F#6P……是啊。\x02\x03",

            "感觉好像是\x01",
            "欠缺了某种平衡感……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#0101F#6P果然是那些黑手党\x01",
            "带进来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xF,
        (
            "#1306F#11P不清楚……\x01",
            "它们是突然从研究楼里出现的。\x02\x03",

            "#1301F然后我们就被\x01",
            "包围了起来……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P看起来，研究楼里\x01",
            "似乎藏有玄机啊。\x02\x03",

            "时间宝贵──\x01",
            "立刻过去吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    #C0127
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F#11P嗯……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3670, 0, -50220, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xF, 6520, 0, -48890, 0)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0xE2, 7)
    OP_29(0x4D, 0x1, 0xC)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_34C5 end

    def Function_28_38B7(): pass

    label("Function_28_38B7")

    TalkBegin(0xFF)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力似乎完全停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_28_38B7 end

    def Function_29_38DF(): pass

    label("Function_29_38DF")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_391F")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_391F")


    #C0129
    ChrTalk(
        0x103,
        (
            "#0200F……稍等一下，\x01",
            "刚才在左边的房间中感觉到了人的气息。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_397F")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_397F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39A0")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_39A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39C1")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_39C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39E2")
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_39E2")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A07")

    def lambda_39F9():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39F9)

    label("loc_3A07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A29")

    def lambda_3A1B():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A1B)

    label("loc_3A29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A4B")

    def lambda_3A3D():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3A3D)

    label("loc_3A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A6D")

    def lambda_3A5F():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A5F)

    label("loc_3A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A8F")

    def lambda_3A81():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3A81)

    label("loc_3A8F")

    Sleep(1000)
    Fade(500)
    OP_68(-16780, 1000, 8490, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    OP_0D()

    #C0130
    ChrTalk(
        0x101,
        "#0005F左边的房间……是那个房间吗？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        "#0101F罗伊德，赶快去确认一下吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3B55")

    label("loc_3B1C")


    #C0132
    ChrTalk(
        0x101,
        (
            "#0001F３０２号室里好像有人……\x01",
            "先去那边确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B55")

    Jump("loc_3B96")

    label("loc_3B5A")


    #C0133
    ChrTalk(
        0x101,
        (
            "#0001F……塞茜尔姐姐\x01",
            "也许在３０１号室。\x01",
            "赶快去看看吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B96")

    Sleep(50)
    SetChrPos(0x0, -8930, 0, 17770, 180)
    EventEnd(0x4)
    Return()

    # Function_29_38DF end

    SaveToFile()

Try(main)
