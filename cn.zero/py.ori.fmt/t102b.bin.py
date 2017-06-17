from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t102b.bin",                # FileName
        "t102b",                    # MapName
        "t102b",                    # Location
        0x0095,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 149, 0, 2, 0, 3],
    )

    BuildStringList((
        "t102b",                  # 0
        "艾丽洁",                 # 1
        "詹姆斯",                 # 2
        "尼基塔",                 # 3
        "青年",                   # 4
        "女性",                   # 5
        "女孩",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "店员",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "黑手党",                 # 12
        "黑手党",                 # 13
        "黑手党",                 # 14
        "犬１",                   # 15
        "犬２",                   # 16
        "SE控制",                 # 17
        "bt102b",                 # 18
    ))

    ATBonus("ATBonus_4BC", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_57C", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_560", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_564", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_568", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_56C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_570", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_574", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_59C", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt102b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", "ms31102.dat", "ms67100.dat", "ms67100.dat", 0, 0, 0, "MonsterBattlePostion_57C", "MonsterBattlePostion_55C", "ed7509", "ed7000", "ATBonus_4BC"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50363.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch32300.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch27800.itc",                   # 04
        "chr/ch26800.itc",                   # 05
        "chr/ch21100.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch24400.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch23600.itc",                   # 0B
        "chr/ch25900.itc",                   # 0C
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

    DeclNpc(12250,   0,       11149,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-24909,  0,       5570,    90,   385,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-23729,  0,       5570,    270,  385,  0x0, 0,   5,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(100139,  0,       18219,   0,    385,  0x0, 0,   11,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-23930,  0,       11470,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-22840,  0,       10689,   315,  401,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(3279,    0,       2970,    225,  385,  0x0, 0,   9,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2539,    0,       2380,    45,   385,  0x0, 0,   10,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-18940,  0,       12609,   180,  385,  0x0, 0,   12,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 15,  -11.0,                 8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.6666667461395264,    -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 14,  -19.030000686645508,   11.899999618530273,    -1.0,                  2.4964001178741455,    [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6329113841056824,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.515000343322754,     -7.53164529800415,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 34,  100.1500015258789,     23.260000228881836,    -1.0,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -12.518750190734863,   -11.630000114440918,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 36,  19.0,                  11.899999618530273,    -1.0,                  2.4964001178741455,    [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6329113841056824,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  -7.53164529800415,     0.20000000298023224,   1.0])

    DeclActor(27660,   0,       10070,   1200,    27660,   1500,    10070,   0x007C, 0,  33, 0x0000)

    ScpFunction((
        "Function_0_67C",          # 00, 0
        "Function_1_734",          # 01, 1
        "Function_2_75F",          # 02, 2
        "Function_3_7A6",          # 03, 3
        "Function_4_82E",          # 04, 4
        "Function_5_88C",          # 05, 5
        "Function_6_8E5",          # 06, 6
        "Function_7_938",          # 07, 7
        "Function_8_A24",          # 08, 8
        "Function_9_A7C",          # 09, 9
        "Function_10_AB3",         # 0A, 10
        "Function_11_AF2",         # 0B, 11
        "Function_12_B11",         # 0C, 12
        "Function_13_C04",         # 0D, 13
        "Function_14_CAD",         # 0E, 14
        "Function_15_1105",        # 0F, 15
        "Function_16_1780",        # 10, 16
        "Function_17_17C6",        # 11, 17
        "Function_18_180C",        # 12, 18
        "Function_19_184B",        # 13, 19
        "Function_20_18B7",        # 14, 20
        "Function_21_191C",        # 15, 21
        "Function_22_1988",        # 16, 22
        "Function_23_19F4",        # 17, 23
        "Function_24_1A97",        # 18, 24
        "Function_25_1AC6",        # 19, 25
        "Function_26_1AF5",        # 1A, 26
        "Function_27_1B11",        # 1B, 27
        "Function_28_1B30",        # 1C, 28
        "Function_29_1B55",        # 1D, 29
        "Function_30_1B83",        # 1E, 30
        "Function_31_2045",        # 1F, 31
        "Function_32_2097",        # 20, 32
        "Function_33_20E9",        # 21, 33
        "Function_34_2160",        # 22, 34
        "Function_35_2161",        # 23, 35
        "Function_36_223E",        # 24, 36
        "Function_37_225A",        # 25, 37
        "Function_38_2274",        # 26, 38
    ))


    def Function_0_67C(): pass

    label("Function_0_67C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_6BC"),
        (1, "loc_6C8"),
        (2, "loc_6D4"),
        (3, "loc_6E0"),
        (4, "loc_6EC"),
        (5, "loc_6F8"),
        (6, "loc_704"),
        (SWITCH_DEFAULT, "loc_710"),
    )


    label("loc_6BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_6C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_6D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_6E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_6EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_6F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_704")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_710")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_71C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_71C")

    label("loc_733")

    Return()

    # Function_0_67C end

    def Function_1_734(): pass

    label("Function_1_734")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75E")
    OP_94(0xFE, 0x17D0E, 0x3F0C, 0x19154, 0x47A4, 0x3E8)
    Sleep(150)
    Jump("Function_1_734")

    label("loc_75E")

    Return()

    # Function_1_734 end

    def Function_2_75F(): pass

    label("Function_2_75F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_772")
    Jump("loc_7A5")

    label("loc_772")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    BeginChrThread(0xB, 0, 0, 1)

    label("loc_7A5")

    Return()

    # Function_2_75F end

    def Function_3_7A6(): pass

    label("Function_3_7A6")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_END)), "loc_7CA")
    Call(0, 13)

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_7D3")

    label("loc_7D3")

    ModifyEventFlags(0, 2, 0x80)
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F6")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_7F6")

    OP_1B(0x5, 0xFF, 0xFFFF)
    OP_1B(0x7, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82D")
    ClearMapObjFlags(0x3, 0x10)
    OP_1B(0x5, 0x0, 0x23)
    OP_1B(0x7, 0x0, 0x25)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_82D")

    Return()

    # Function_3_7A6 end

    def Function_4_82E(): pass

    label("Function_4_82E")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "哎呀，游客也\x01",
            "差不多该回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "……？\x01",
            "那些往住宅街方向去的人\x01",
            "到底要做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_82E end

    def Function_5_88C(): pass

    label("Function_5_88C")

    TalkBegin(0xFE)

    #C0003
    ChrTalk(
        0xFE,
        (
            "那么，差不多也该\x01",
            "出发前往议长宅邸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "哈哈哈……\x01",
            "看来，今晚会充满乐趣。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_88C end

    def Function_6_8E5(): pass

    label("Function_6_8E5")

    TalkBegin(0xFE)

    #C0005
    ChrTalk(
        0xFE,
        (
            "这个人说，今天要为我\x01",
            "拍到饰品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "真是对不起他的夫人哦。\x01",
            "呵呵……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_8E5 end

    def Function_7_938(): pass

    label("Function_7_938")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C8")

    #C0007
    ChrTalk(
        0xFE,
        "哎呀，满足，太满足了。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "主题公园中最奇妙的\x01",
            "乐趣——『踢咪西』\x01",
            "也已经体验过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "……虽然险些被\x01",
            "工作人员赶走。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A20")

    label("loc_9C8")


    #C0010
    ChrTalk(
        0xFE,
        (
            "『踢咪西』是\x01",
            "只属于孩子的特权。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "不过，我真是相当满足，\x01",
            "已经彻底没有遗憾了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A20")

    TalkEnd(0xFE)
    Return()

    # Function_7_938 end

    def Function_8_A24(): pass

    label("Function_8_A24")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        (
            "虽然在主题公园玩过了……\x01",
            "但最后也没有去成珠宝店。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "呜呜，好遗憾啊～……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_A24 end

    def Function_9_A7C(): pass

    label("Function_9_A7C")

    TalkBegin(0xFE)

    #C0014
    ChrTalk(
        0xFE,
        (
            "妈妈……\x01",
            "水上巴士要开走了，\x01",
            "快点去乘坐吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_A7C end

    def Function_10_AB3(): pass

    label("Function_10_AB3")

    TalkBegin(0xFE)

    #C0015
    ChrTalk(
        0xFE,
        "哎呀，今天真开心！\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "克洛斯贝尔七十周年，万岁！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_AB3 end

    def Function_11_AF2(): pass

    label("Function_11_AF2")

    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        "呵呵，还想再来呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_AF2 end

    def Function_12_B11(): pass

    label("Function_12_B11")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0018
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE6")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_BE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C02")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_C02")

    Return()

    # Function_12_B11 end

    def Function_13_C04(): pass

    label("Function_13_C04")

    SetChrChipByIndex(0x13, 0x0)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x13, 0x1)
    SetChrPos(0x13, -170, 0, 10700, 225)
    SetChrChipByIndex(0x14, 0x0)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0x14, 0x1)
    SetChrPos(0x14, 3010, 0, 7590, 270)
    SetChrChipByIndex(0x15, 0x0)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x1)
    SetChrPos(0x15, 1980, 0, 4930, 315)
    Return()

    # Function_13_C04 end

    def Function_14_CAD(): pass

    label("Function_14_CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDB")
    EventBegin(0x1)
    Call(0, 38)
    Sleep(50)
    SetChrPos(0x0, -18610, 0, 9950, 180)
    EventEnd(0x4)
    Jump("loc_1104")

    label("loc_CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B2")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-19000, 1000, 11800, 0)
    SetChrPos(0x101, -19330, 0, 8810, 0)
    SetChrPos(0x102, -17960, 0, 8810, 0)
    SetChrPos(0x103, -20760, 0, 10150, 45)
    SetChrPos(0x104, -16940, 0, 9380, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D60")
    SetChrPos(0x151, -18610, 0, 7180, 0)

    label("loc_D60")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -19000, 0, 12900, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)

    def lambda_DA0():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x2C2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_DA0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    WaitChrThread(0x10, 1)

    #C0019
    ChrTalk(
        0x101,
        "#5005F#3P唔哇……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10,
        (
            "#11P欢迎来到\x01",
            "珠宝店『亮饰』。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x10,
        (
            "#11P……不好意思，这位客人。\x01",
            "请问您持有的是\x01",
            "谁的介绍信？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E77")

    #C0022
    ChrTalk(
        0x102,
        (
            "#0105F#6P那个……\x01",
            "必须要持有介绍信吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA3")

    label("loc_E77")


    #C0023
    ChrTalk(
        0x102,
        (
            "#5305F#6P那个……\x01",
            "必须要持有介绍信吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA3")


    #C0024
    ChrTalk(
        0x10,
        "#11P正是。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x10,
        (
            "#11P本店实行会员制，\x01",
            "非会员谢绝入内。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x10,
        "#11P那么，很抱歉……\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)
    Sleep(100)

    def lambda_F07():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x3264, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F07)
    Sleep(300)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    WaitChrThread(0x10, 1)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x10, 0x80)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDA")

    #C0027
    ChrTalk(
        0x103,
        "#0203F……一眼就看出我们不是会员了吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1006")

    label("loc_FDA")


    #C0028
    ChrTalk(
        0x103,
        "#5403F……一眼就看出我们不是会员了吗。\x02",
    )

    CloseMessageWindow()

    label("loc_1006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103D")

    #C0029
    ChrTalk(
        0x104,
        "#0310F#12P感、感觉真不爽啊～……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1065")

    label("loc_103D")


    #C0030
    ChrTalk(
        0x104,
        "#5610F#12P感、感觉真不爽啊～……！\x02",
    )

    CloseMessageWindow()

    label("loc_1065")


    #C0031
    ChrTalk(
        0x101,
        (
            "#5003F#3P总、总之……\x01",
            "进不去的话也没办法，\x01",
            "就先放弃吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0xAE, 1)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Jump("loc_1104")

    label("loc_10B2")

    EventBegin(0x1)

    #C0032
    ChrTalk(
        0x101,
        (
            "#5000F这里好像是实行\x01",
            "会员制的珠宝店。\x01",
            "这次就放弃吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -18610, 0, 9950, 180)
    EventEnd(0x4)

    label("loc_1104")

    Return()

    # Function_14_CAD end

    def Function_15_1105(): pass

    label("Function_15_1105")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0x98, 0xFF, 0xFF)
    AddParty(0x99, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("monster/ch67150.itc", 0x23)
    LoadChrToIndex("monster/ch67151.itc", 0x24)
    LoadChrToIndex("chr/ch31050.itc", 0x25)
    LoadChrToIndex("chr/ch31051.itc", 0x26)
    LoadChrToIndex("chr/ch31053.itc", 0x27)
    LoadChrToIndex("chr/ch31150.itc", 0x28)
    LoadChrToIndex("chr/ch31151.itc", 0x29)
    LoadChrToIndex("chr/ch31153.itc", 0x2A)
    LoadChrToIndex("chr/ch00000.itc", 0x2B)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x199, 0x80)
    SetChrBattleFlags(0x199, 0x8000)
    SetChrFlags(0x19A, 0x80)
    SetChrBattleFlags(0x19A, 0x8000)
    SetChrPos(0x101, -9430, 0, 7730, 90)
    SetChrPos(0x102, -10930, 0, 7250, 90)
    SetChrPos(0x103, -11440, 0, 9330, 90)
    SetChrPos(0x104, -13560, 0, 9140, 90)
    SetChrPos(0x105, -13830, 0, 7790, 90)
    SetChrPos(0x133, 0, 0, 0, 0)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x4)
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x13, 30, 0, 27560, 180)
    SetChrPos(0x14, -1600, 0, -5300, 0)
    SetChrPos(0x16, 1200, 0, -5300, 0)
    SetChrPos(0x15, 18000, 0, 7400, 270)
    SetChrPos(0x17, 18000, 0, 9200, 270)
    SetChrPos(0x11, 17000, 0, 7400, 270)
    SetChrPos(0x12, 17000, 0, 8600, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xB, 0, 0, 20560, 180)
    SetChrPos(0xC, 16500, 0, 6300, 270)
    SetChrPos(0xD, 14000, 0, 10400, 270)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    OP_68(-9750, 1600, 8000, 0)
    MoveCamera(315, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18190, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17190, 1000)
    OP_6F(0x10)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(9000, 1000, 8000, 0)
    MoveCamera(315, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24710, 0)
    OP_68(-1000, 1000, 8000, 5000)
    SetCameraDistance(15940, 5000)
    Sound(928, 0, 100, 0)
    Sound(919, 0, 100, 0)
    BeginChrThread(0x11, 3, 0, 21)
    BeginChrThread(0x12, 3, 0, 22)
    BeginChrThread(0xB, 3, 0, 23)
    BeginChrThread(0xC, 3, 0, 24)
    BeginChrThread(0xD, 3, 0, 25)
    BeginChrThread(0x13, 3, 0, 16)
    Sleep(1500)
    BeginChrThread(0x14, 3, 0, 17)
    BeginChrThread(0x15, 3, 0, 18)
    BeginChrThread(0x16, 3, 0, 19)
    BeginChrThread(0x17, 3, 0, 20)
    BeginChrThread(0x18, 1, 0, 29)
    Sleep(300)

    def lambda_158F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_158F)

    def lambda_15A4():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15A4)

    def lambda_15B9():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15B9)

    def lambda_15CE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15CE)

    def lambda_15E3():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15E3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    EndChrThread(0x18, 0x1)
    OP_6F(0x79)
    OP_0D()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0007F#5P住手……！\x01",
            "不要把无辜市民卷进来！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x14,
        "#6P哼，谁管这些！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x15,
        (
            "#12P如果让你们逃跑了，\x01",
            "我们可就要遭殃了！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x133, -3840, 0, 8710, 90)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetCameraDistance(12940, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Battle("BattleInfo_59C", 0x30200011, 0x0, 0x0, 0x16, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 30)
    Return()

    # Function_15_1105 end

    def Function_16_1780(): pass

    label("Function_16_1780")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_178D():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_178D)

    def lambda_17A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17A2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_16_1780 end

    def Function_17_17C6(): pass

    label("Function_17_17C6")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_17D3():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17D3)

    def lambda_17E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17E8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_17_17C6 end

    def Function_18_180C(): pass

    label("Function_18_180C")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1819():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1819)

    def lambda_182E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_182E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_180C end

    def Function_19_184B(): pass

    label("Function_19_184B")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 26)

    def lambda_1869():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1869)

    def lambda_187E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_187E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_19_184B end

    def Function_20_18B7(): pass

    label("Function_20_18B7")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 26)

    def lambda_18D5():
        OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18D5)

    def lambda_18EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18EA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_20_18B7 end

    def Function_21_191C(): pass

    label("Function_21_191C")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1933():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1933)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_1953():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1953)
    WaitChrThread(0xFE, 1)

    def lambda_196C():
        OP_A6(0xFE, 0x0, 0x28, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_196C)
    WaitChrThread(0xFE, 2)
    OP_64(0xFE)
    Return()

    # Function_21_191C end

    def Function_22_1988(): pass

    label("Function_22_1988")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_199F():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_199F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_19BF():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19BF)
    WaitChrThread(0xFE, 1)

    def lambda_19D8():
        OP_A6(0xFE, 0x0, 0x28, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_19D8)
    WaitChrThread(0xFE, 2)
    OP_64(0xFE)
    Return()

    # Function_22_1988 end

    def Function_23_19F4(): pass

    label("Function_23_19F4")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1A0B():
        OP_95(0xFE, -160, 0, 17680, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A0B)
    WaitChrThread(0xFE, 1)

    def lambda_1A29():
        OP_95(0xFE, -5000, 0, 14360, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A29)
    WaitChrThread(0xFE, 1)

    def lambda_1A47():
        OP_95(0xFE, -7030, 1240, 16610, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A47)
    WaitChrThread(0xFE, 1)

    def lambda_1A65():
        OP_95(0xFE, -7110, 1710, 17620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A65)

    def lambda_1A7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A7F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_64(0xFE)
    Return()

    # Function_23_19F4 end

    def Function_24_1A97(): pass

    label("Function_24_1A97")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1AAE():
        OP_9B(0x0, 0xFE, 0x0, 0x7148, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AAE)
    WaitChrThread(0xFE, 1)
    OP_64(0xFE)
    Return()

    # Function_24_1A97 end

    def Function_25_1AC6(): pass

    label("Function_25_1AC6")

    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1ADD():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1ADD)
    WaitChrThread(0xFE, 1)
    OP_64(0xFE)
    Return()

    # Function_25_1AC6 end

    def Function_26_1AF5(): pass

    label("Function_26_1AF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B10")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_26_1AF5")

    label("loc_1B10")

    Return()

    # Function_26_1AF5 end

    def Function_27_1B11(): pass

    label("Function_27_1B11")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B2F")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_27_1B11")

    label("loc_1B2F")

    Return()

    # Function_27_1B11 end

    def Function_28_1B30(): pass

    label("Function_28_1B30")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    SetChrSubChip(0xFE, 0x3)
    OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
    Return()

    # Function_28_1B30 end

    def Function_29_1B55(): pass

    label("Function_29_1B55")

    Sleep(1500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Return()

    # Function_29_1B55 end

    def Function_30_1B83(): pass

    label("Function_30_1B83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x98, 0xFF)
    RemoveParty(0x99, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch00000.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -2410, 0, 7740, 90)
    SetChrPos(0x102, -3820, 0, 9270, 90)
    SetChrPos(0x103, -3820, 0, 7190, 90)
    SetChrPos(0x104, -5680, 0, 9660, 90)
    SetChrPos(0x105, -6650, 0, 8520, 90)
    SetChrPos(0x133, -5070, 0, 6600, 90)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    Call(0, 13)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x11, -4750, 0, 12450, 135)
    SetChrPos(0x12, -4019, 0, 13570, 135)
    OP_68(2410, 1600, 7740, 0)
    MoveCamera(315, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(15510, 0)
    FadeToBright(1000, 0)
    OP_68(-2410, 1600, 7740, 3000)
    OP_6F(0x1)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    def lambda_1D32():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D32)

    def lambda_1D3F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D3F)
    Sleep(100)

    def lambda_1D4F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D4F)

    def lambda_1D5C():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D5C)
    Sleep(100)

    def lambda_1D6C():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D6C)

    def lambda_1D79():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_1D79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x133, 1)

    #C0036
    ChrTalk(
        0x101,
        "#0001F#6P你们两个还好吗？\x02",
    )

    CloseMessageWindow()

    def lambda_1DBD():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1DBD)

    def lambda_1DCA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1DCA)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1DF7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E1E")

    label("loc_1DF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1E14")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E1E")

    label("loc_1E14")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E1E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E3A"),
        (1, "loc_1E78"),
        (2, "loc_1EB6"),
        (SWITCH_DEFAULT, "loc_1EFA"),
    )


    label("loc_1E3A")

    OP_2C(0x47, 0x3)

    #C0037
    ChrTalk(
        0x11,
        "#11P啊……！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x12,
        "#11P那、那些是什么人……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EFA")

    label("loc_1E78")

    OP_2C(0x47, 0x1)

    #C0039
    ChrTalk(
        0x11,
        "#11P唔，还好……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x12,
        "#11P那、那些是什么人……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EFA")

    label("loc_1EB6")


    #C0041
    ChrTalk(
        0x11,
        "#11P唔，还好……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x12,
        (
            "#11P……呜呜……\x01",
            "那些是什么人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFA")

    label("loc_1EFA")


    #C0043
    ChrTalk(
        0x102,
        (
            "#0101F#6P请快点去\x01",
            "酒店避难……！\x02\x03",

            "他们应该还没有\x01",
            "闯入那里！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x11,
        "#11P知、知道了！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x12,
        "#11P我、我已经受够了……！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x12,
        (
            "#11P米修拉姆什么的，\x01",
            "如果不来就好了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x11, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 32)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    SetChrPos(0x0, -3910, 0, 7710, 90)
    SetScenarioFlags(0xA7, 5)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_30_1B83 end

    def Function_31_2045(): pass

    label("Function_31_2045")


    def lambda_204A():
        OP_95(0xFE, -6640, 1090, 16630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_204A)
    WaitChrThread(0xFE, 1)

    def lambda_2068():
        OP_95(0xFE, -6850, 1750, 17950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2068)

    def lambda_2082():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2082)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_31_2045 end

    def Function_32_2097(): pass

    label("Function_32_2097")


    def lambda_209C():
        OP_95(0xFE, -6640, 1090, 16630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_209C)
    WaitChrThread(0xFE, 1)

    def lambda_20BA():
        OP_95(0xFE, -6850, 1750, 17950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_20BA)

    def lambda_20D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_20D4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_32_2097 end

    def Function_33_20E9(): pass

    label("Function_33_20E9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前方区域正在开发，\x01",
            "禁止入内。\x01",
            "　　　　──米修拉姆开发事业部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_33_20E9 end

    def Function_34_2160(): pass

    label("Function_34_2160")

    Return()

    # Function_34_2160 end

    def Function_35_2161(): pass

    label("Function_35_2161")

    EventBegin(0x1)

    #C0048
    ChrTalk(
        0x101,
        (
            "#0008F（虽然时间有些紧……\x01",
            "　但还是稍微休息一下为好吧？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "休息一下\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21E4"),
        (SWITCH_DEFAULT, "loc_2219"),
    )


    label("loc_21E4")

    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_2227")

    label("loc_2219")

    FadeToBright(300, 0)
    Jump("loc_2227")

    label("loc_2227")

    Sleep(50)
    SetChrPos(0x0, -5150, 0, 14030, 135)
    EventEnd(0x4)
    Return()

    # Function_35_2161 end

    def Function_36_223E(): pass

    label("Function_36_223E")

    EventBegin(0x1)
    Call(0, 38)
    Sleep(50)
    SetChrPos(0x0, 19600, 0, 9770, 180)
    EventEnd(0x4)
    Return()

    # Function_36_223E end

    def Function_37_225A(): pass

    label("Function_37_225A")

    EventBegin(0x1)
    Call(0, 38)
    OP_5A()
    SetChrPos(0x0, 40, 0, 17030, 180)
    EventEnd(0x4)
    Return()

    # Function_37_225A end

    def Function_38_2274(): pass

    label("Function_38_2274")


    #C0049
    ChrTalk(
        0x101,
        (
            "#0013F没时间绕远路了……\x01",
            "赶快带着这孩子去码头！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_38_2274 end

    SaveToFile()

Try(main)
