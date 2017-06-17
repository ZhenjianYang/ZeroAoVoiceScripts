from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t100b.bin",                # FileName
        "t100b",                    # MapName
        "t100b",                    # Location
        0x0041,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t100b",                  # 0
        "萨尔莎乘务员",           # 1
        "游客",                   # 2
        "贵族青年",               # 3
        "游客",                   # 4
        "游客",                   # 5
        "加尔西亚",               # 6
        "黑手党",                 # 7
        "黑手党",                 # 8
        "黑手党",                 # 9
        "黑手党",                 # 10
        "黑手党",                 # 11
        "狗１",                   # 12
        "狗２",                   # 13
        "狗３",                   # 14
        "赛尔盖科长",             # 15
        "蔡特",                   # 16
        "水上巴士",               # 17
        "船",                     # 18
        "SE控制",                 # 19
        "bt100b",                 # 20
        "主题公园方向",           # 21
        "宅邸方向",               # 22
    ))

    ATBonus("ATBonus_3D4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_494", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_478", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_47C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_480", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_484", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_488", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_48C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_4B4", 0x0042, 27, 6, 0, 0, 0, 0, 0, "bt100b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02201.dat", "ms31900.dat", "ms31900.dat", "ms67100.dat", "ms67100.dat", "ms67100.dat", 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_474", "ed7404", "ed7000", "ATBonus_3D4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch28400.itc",                   # 00
        "chr/ch26700.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch23700.itc",                   # 04
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

    DeclNpc(-3740,   -4000,   -47180,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-3529,   -5000,   -56490,  180,  385,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5909,    -4000,   -50770,  86,   385,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5760,    -2000,   -28799,  90,   385,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(6960,    -2000,   -28799,  270,  385,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-24500,  -4000,   -45660,  1200,    -24490,  -6000,   -38830,  0x007C, 0,  8,  0x0000)
    DeclActor(10350,   -3990,   -46410,  1200,    10350,   -2500,   -46410,  0x007C, 0,  76, 0x0000)

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "主题公园方向")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "宅邸方向")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ScpFunction((
        "Function_0_62C",          # 00, 0
        "Function_1_6E4",          # 01, 1
        "Function_2_71E",          # 02, 2
        "Function_3_7C4",          # 03, 3
        "Function_4_856",          # 04, 4
        "Function_5_8CD",          # 05, 5
        "Function_6_923",          # 06, 6
        "Function_7_988",          # 07, 7
        "Function_8_9B4",          # 08, 8
        "Function_9_A7C",          # 09, 9
        "Function_10_254B",        # 0A, 10
        "Function_11_256F",        # 0B, 11
        "Function_12_25A0",        # 0C, 12
        "Function_13_25C8",        # 0D, 13
        "Function_14_25F0",        # 0E, 14
        "Function_15_2618",        # 0F, 15
        "Function_16_263F",        # 10, 16
        "Function_17_26A7",        # 11, 17
        "Function_18_2849",        # 12, 18
        "Function_19_2878",        # 13, 19
        "Function_20_28AA",        # 14, 20
        "Function_21_28EC",        # 15, 21
        "Function_22_292E",        # 16, 22
        "Function_23_2957",        # 17, 23
        "Function_24_2A61",        # 18, 24
        "Function_25_2B92",        # 19, 25
        "Function_26_2BBB",        # 1A, 26
        "Function_27_2BE1",        # 1B, 27
        "Function_28_2C0C",        # 1C, 28
        "Function_29_2CBD",        # 1D, 29
        "Function_30_2EAF",        # 1E, 30
        "Function_31_2FE4",        # 1F, 31
        "Function_32_3085",        # 20, 32
        "Function_33_3170",        # 21, 33
        "Function_34_3218",        # 22, 34
        "Function_35_3238",        # 23, 35
        "Function_36_3258",        # 24, 36
        "Function_37_327B",        # 25, 37
        "Function_38_32BE",        # 26, 38
        "Function_39_5308",        # 27, 39
        "Function_40_5322",        # 28, 40
        "Function_41_5347",        # 29, 41
        "Function_42_537C",        # 2A, 42
        "Function_43_53AE",        # 2B, 43
        "Function_44_5428",        # 2C, 44
        "Function_45_556E",        # 2D, 45
        "Function_46_5586",        # 2E, 46
        "Function_47_5615",        # 2F, 47
        "Function_48_5691",        # 30, 48
        "Function_49_5720",        # 31, 49
        "Function_50_57B0",        # 32, 50
        "Function_51_582C",        # 33, 51
        "Function_52_5A0D",        # 34, 52
        "Function_53_5A3B",        # 35, 53
        "Function_54_5B48",        # 36, 54
        "Function_55_5C58",        # 37, 55
        "Function_56_5C82",        # 38, 56
        "Function_57_5CAC",        # 39, 57
        "Function_58_5CD6",        # 3A, 58
        "Function_59_5D00",        # 3B, 59
        "Function_60_5D2A",        # 3C, 60
        "Function_61_5D54",        # 3D, 61
        "Function_62_5D6E",        # 3E, 62
        "Function_63_5DAD",        # 3F, 63
        "Function_64_5DEC",        # 40, 64
        "Function_65_5E2B",        # 41, 65
        "Function_66_5E7A",        # 42, 66
        "Function_67_5F3F",        # 43, 67
        "Function_68_5FCA",        # 44, 68
        "Function_69_6055",        # 45, 69
        "Function_70_60B1",        # 46, 70
        "Function_71_60F8",        # 47, 71
        "Function_72_6141",        # 48, 72
        "Function_73_618E",        # 49, 73
        "Function_74_61D1",        # 4A, 74
        "Function_75_621E",        # 4B, 75
        "Function_76_6261",        # 4C, 76
    ))


    def Function_0_62C(): pass

    label("Function_0_62C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_66C"),
        (1, "loc_678"),
        (2, "loc_684"),
        (3, "loc_690"),
        (4, "loc_69C"),
        (5, "loc_6A8"),
        (6, "loc_6B4"),
        (SWITCH_DEFAULT, "loc_6C0"),
    )


    label("loc_66C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_678")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_684")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_690")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_69C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_6A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_6B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_6C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_6CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6CC")

    label("loc_6E3")

    Return()

    # Function_0_62C end

    def Function_1_6E4(): pass

    label("Function_1_6E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F5")
    Event(0, 9)

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_704")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 38)

    label("loc_704")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Return()

    # Function_1_6E4 end

    def Function_2_71E(): pass

    label("Function_2_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_727")

    label("loc_727")

    SetMapObjFlags(0x1, 0x4)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_741")
    OP_65(0x0, 0x1)
    Jump("loc_78B")

    label("loc_741")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -24490, -6000, -38830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_78B")

    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BD")
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)

    label("loc_7BD")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_71E end

    def Function_3_7C4(): pass

    label("Function_3_7C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_827")

    #C0001
    ChrTalk(
        0xFE,
        (
            "驶往克洛斯贝尔市的水上巴士\x01",
            "已经到达。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "回程的乘客\x01",
            "请在这边稍等片刻～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_852")

    label("loc_827")


    #C0003
    ChrTalk(
        0xFE,
        (
            "返回克洛斯贝尔市的乘客\x01",
            "请在这边排队～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_852")

    TalkEnd(0xFE)
    Return()

    # Function_3_7C4 end

    def Function_4_856(): pass

    label("Function_4_856")

    TalkBegin(0xFE)

    #C0004
    ChrTalk(
        0xFE,
        (
            "本想来这里找个\x01",
            "出身名门的女朋友……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "但我根本搞不定这里的女人。\x01",
            "关于这一点，我总算是得到深刻教训了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_856 end

    def Function_5_8CD(): pass

    label("Function_5_8CD")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xFE,
        "哼……终于到了。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "离竞拍会开始，没有多少时间了啊……\x01",
            "稍微抓紧一点吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_8CD end

    def Function_6_923(): pass

    label("Function_6_923")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        (
            "我和朋友一整天\x01",
            "都在主题公园游玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "回过神的时候，都已经是晚上了，\x01",
            "真是吓了一大跳呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_923 end

    def Function_7_988(): pass

    label("Function_7_988")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "不好，船好像都要开了！\x01",
            "快走吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_988 end

    def Function_8_9B4(): pass

    label("Function_8_9B4")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0011
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
    )

    CloseMessageWindow()
    OP_68(-23140, -2400, -43580, 1500)
    MoveCamera(315, 36, 0, 1500)
    OP_6E(200, 1500)
    SetCameraDistance(50000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0012
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A77")
    OP_E0(0x2)
    MiniGame(0x6, 0x3, 0xFFFFA04C, 0xFFFFF060, 0xFFFF4912, 0x0, 0xFFFFA056, 0xFFFFE890, 0xFFFF6852)

    label("loc_A77")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_8_9B4 end

    def Function_9_A7C(): pass

    label("Function_9_A7C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31050.itc", 0x1F)
    LoadChrToIndex("chr/ch31051.itc", 0x20)
    LoadChrToIndex("chr/ch31150.itc", 0x23)
    LoadChrToIndex("chr/ch31151.itc", 0x24)
    LoadChrToIndex("chr/ch31952.itc", 0x27)
    LoadChrToIndex("chr/ch31951.itc", 0x28)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00150.itc", 0x2C)
    LoadChrToIndex("chr/ch00151.itc", 0x2D)
    LoadChrToIndex("chr/ch00250.itc", 0x2E)
    LoadChrToIndex("chr/ch00251.itc", 0x2F)
    LoadChrToIndex("chr/ch00350.itc", 0x30)
    LoadChrToIndex("chr/ch00351.itc", 0x31)
    LoadChrToIndex("chr/ch00450.itc", 0x32)
    LoadChrToIndex("chr/ch00451.itc", 0x33)
    LoadChrToIndex("chr/ch02200.itc", 0x34)
    LoadChrToIndex("chr/ch02250.itc", 0x35)
    LoadChrToIndex("monster/ch67150.itc", 0x36)
    LoadChrToIndex("monster/ch67151.itc", 0x37)
    LoadChrToIndex("chr/ch00052.itc", 0x38)
    LoadChrToIndex("chr/ch00152.itc", 0x39)
    LoadChrToIndex("chr/ch00254.itc", 0x3A)
    LoadChrToIndex("chr/ch00352.itc", 0x3B)
    LoadChrToIndex("chr/ch00452.itc", 0x3C)
    LoadChrToIndex("chr/ch31052.itc", 0x3D)
    LoadChrToIndex("chr/ch31152.itc", 0x3E)
    LoadChrToIndex("chr/ch31952.itc", 0x3F)
    LoadChrToIndex("monster/ch67152.itc", 0x40)
    LoadChrToIndex("chr/ch00457.itc", 0x41)
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg040_00.eff")
    LoadEffect(0x4, "battle/btgun00.eff")
    LoadEffect(0x5, "event\\eva01_01.eff")
    SoundLoad(479)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x18)
    OP_49()
    SetChrPos(0x18, -5000, -5500, -38200, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x0)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 17000, -5500, -63000, 270)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 300, -2000, -7520, 180)
    SetChrPos(0x102, 1240, -2000, -6340, 180)
    SetChrPos(0x103, -780, -2000, -5850, 180)
    SetChrPos(0x104, -1000, -2000, -4030, 180)
    SetChrPos(0x105, 610, -2000, -4000, 180)
    SetChrPos(0x133, 0, 0, 0, 0)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0x13, 0x36)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x36)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x36)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 0, -1300, 5000, 0)
    SetChrPos(0x11, 0, -1300, 5000, 0)
    SetChrPos(0x12, 0, -1300, 5000, 0)
    SetChrPos(0xE, 0, -1300, 5000, 0)
    SetChrPos(0xF, 0, -1300, 5000, 0)
    SetChrPos(0x13, 0, -1300, 5000, 0)
    SetChrPos(0x14, 0, -1300, 5000, 0)
    SetChrPos(0x15, 0, -1300, 5000, 0)
    SetChrPos(0xD, 0, -1300, 5000, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_F35")
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_1576")

    label("loc_F35")

    OP_68(0, -800, -4970, 0)
    MoveCamera(315, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    Sound(475, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_68(0, -800, -6970, 1500)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0013
    ChrTalk(
        0x101,
        "#0007F#11P糟了……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(1000, -500, -38550, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(35000, 0)
    MoveCamera(325, 17, 0, 4500)
    SetChrPos(0x101, 300, -2000, -7520, 180)
    SetChrPos(0x102, 1240, -2000, -6340, 180)
    SetChrPos(0x103, -780, -2000, -5850, 180)
    SetChrPos(0x104, -1000, -2000, -4030, 180)
    SetChrPos(0x105, 610, -2000, -4000, 180)

    def lambda_1054():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1054)

    def lambda_1069():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1069)

    def lambda_107E():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_107E)

    def lambda_1093():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1093)

    def lambda_10A8():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10A8)
    Sound(477, 0, 100, 0)
    Sound(479, 2, 100, 0)

    def lambda_10C9():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_10C9)
    Sleep(3500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    Fade(1000)
    OP_68(0, -500, -27850, 0)
    MoveCamera(315, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(21570, 0)
    SetCameraDistance(17570, 2000)
    SetChrPos(0x101, 300, -2000, -18520, 180)
    SetChrPos(0x102, 1240, -2000, -17340, 180)
    SetChrPos(0x103, -780, -2000, -16850, 180)
    SetChrPos(0x104, -1000, -2000, -15030, 180)
    SetChrPos(0x105, 610, -2000, -15000, 180)

    def lambda_118B():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_118B)

    def lambda_11A0():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11A0)

    def lambda_11B5():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11B5)

    def lambda_11CA():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11CA)

    def lambda_11DF():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11DF)
    EndChrThread(0x18, 0x1)
    SetChrPos(0x18, -5000, -5500, -38200, 0)

    def lambda_1209():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1209)
    WaitChrThread(0x18, 1)
    SetMapObjFlags(0x0, 0x4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_0D()
    BeginChrThread(0x1A, 1, 0, 37)

    #N0014
    NpcTalk(
        0x101,
        "琪雅",
        "#5805F#5P船，走掉了呢～\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        (
            "#0201F#11P怎么会……\x01",
            "应该还没到出航时刻啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0103F#11P说不定，是因为听到骚乱的声音，\x01",
            "所以提早出航了……\x02\x03",

            "#0108F从某种意义上说，\x01",
            "或许算是正确的决定……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x105,
        (
            "#0401F#11P但对我们来说，\x01",
            "好像是最糟糕的决定啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x10,
        "男人的声音",
        "#3P找到了……！\x02",
    )

    CloseMessageWindow()

    #N0019
    NpcTalk(
        0x10,
        "男人的声音",
        "#3P快点追……！\x02",
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_1405():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1405)

    def lambda_1412():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1412)
    Sleep(100)

    def lambda_1422():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1422)

    def lambda_142F():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_142F)
    Sleep(100)

    def lambda_143F():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_143F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    #C0020
    ChrTalk(
        0x101,
        "#0013F#6P呜……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        (
            "#0307F#5P能逃多远就逃多远吧！\x02\x03",

            "码头说不定\x01",
            "还停着小船什么的！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0007F#6P嗯……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22570, 3000)

    def lambda_14D7():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14D7)
    Sleep(100)

    def lambda_14F4():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14F4)
    Sleep(100)

    def lambda_1511():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1511)
    Sleep(100)

    def lambda_152E():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_152E)
    Sleep(100)

    def lambda_154B():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_154B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    label("loc_1576")

    EndChrThread(0x1A, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1838")
    Fade(1000)
    SetChrPos(0x101, 14070, -4000, -46390, 180)
    SetChrPos(0x102, 13870, -4000, -42060, 180)
    SetChrPos(0x103, 14480, -4000, -43440, 180)
    SetChrPos(0x104, 14910, -4000, -45400, 180)
    SetChrPos(0x105, 13200, -4000, -44750, 180)
    OP_68(14000, -2800, -44500, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    OP_68(14000, -1700, -58400, 3000)
    MoveCamera(0, 16, 0, 3000)
    SetCameraDistance(21390, 3000)

    def lambda_1637():
        OP_95(0xFE, 14020, -4000, -52980, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1637)

    def lambda_1651():
        OP_95(0xFE, 13510, -4000, -49680, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1651)

    def lambda_166B():
        OP_95(0xFE, 14570, -4000, -50590, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_166B)

    def lambda_1685():
        OP_95(0xFE, 15240, -4000, -52410, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1685)

    def lambda_169F():
        OP_95(0xFE, 12940, -4000, -51750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_169F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_0D()
    Sleep(750)
    Fade(1000)
    OP_68(14000, -2800, -52500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0310F#11P嘁……\x01",
            "一条船也没有啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0008F#5P呜，这样下去……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2E)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x32)
    SetChrSubChip(0x105, 0x0)
    OP_68(11810, -1400, -43680, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(14500, 1250)
    BeginChrThread(0x12, 3, 0, 20)
    BeginChrThread(0xE, 3, 0, 21)
    Sleep(2500)
    OP_6F(0x79)
    OP_0D()
    OP_68(10910, -1400, -52370, 1500)
    MoveCamera(35, 17, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(16000, 1500)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x102, 3, 0, 23)
    BeginChrThread(0x104, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 24)
    BeginChrThread(0x105, 3, 0, 26)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)

    label("loc_1838")

    FadeToBright(1000, 0)
    OP_68(-11450, -2000, -50000, 0)
    MoveCamera(90, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(29000, 0)
    OP_68(-11450, -3500, -50000, 2000)
    MoveCamera(50, 16, 0, 2000)
    SetCameraDistance(21000, 2000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x102, 3, 0, 28)
    BeginChrThread(0x104, 3, 0, 30)
    BeginChrThread(0x103, 3, 0, 29)
    BeginChrThread(0x105, 3, 0, 32)
    BeginChrThread(0x13, 3, 0, 33)
    BeginChrThread(0x11, 3, 0, 31)
    BeginChrThread(0x12, 3, 0, 34)
    BeginChrThread(0xE, 3, 0, 35)
    BeginChrThread(0xF, 3, 0, 36)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_190B")
    Sleep(1)
    Jump("loc_18F4")

    label("loc_190B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x12, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x101, -23200, -4000, -50300, 270)
    SetChrPos(0x102, -21660, -4000, -48980, 270)
    SetChrPos(0x103, -21820, -4000, -51340, 270)
    SetChrPos(0x104, -20110, -4000, -50710, 270)
    SetChrPos(0x105, -20210, -4000, -49230, 270)
    SetChrPos(0x10, -10750, -4000, -48500, 270)
    SetChrPos(0x11, -10750, -4000, -51500, 270)
    SetChrPos(0xE, -9750, -4000, -47000, 270)
    SetChrPos(0xF, -9750, -4000, -53000, 270)
    SetChrPos(0x13, -8400, -4000, -48500, 270)
    SetChrPos(0x14, -8400, -4000, -51500, 270)
    SetChrPos(0xD, -13000, -4000, -50000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x28)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x28)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0x13, 0x37)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x37)
    SetChrSubChip(0x14, 0x0)
    FadeToBright(1000, 0)
    OP_68(-30770, -3000, -50000, 0)
    MoveCamera(30, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(28860, 0)
    SetCameraDistance(19860, 2000)

    def lambda_1AC8():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AC8)

    def lambda_1ADD():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1ADD)

    def lambda_1AF2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AF2)

    def lambda_1B07():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B07)

    def lambda_1B1C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1B1C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_0D()
    OP_68(-24770, -3000, -50000, 2000)
    BeginChrThread(0x13, 0, 0, 18)
    BeginChrThread(0x14, 0, 0, 18)

    def lambda_1B65():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1B65)

    def lambda_1B7A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1B7A)

    def lambda_1B8F():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B8F)

    def lambda_1BA4():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1BA4)

    def lambda_1BB9():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1BB9)

    def lambda_1BCE():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1BCE)

    def lambda_1BE3():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BE3)
    Sleep(50)

    def lambda_1BF3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BF3)
    Sleep(50)

    def lambda_1C03():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C03)
    Sleep(50)

    def lambda_1C13():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C13)
    Sleep(50)

    def lambda_1C23():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C23)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x3)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x3)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xF, 0x3)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x13, 0, 0, 19)
    BeginChrThread(0x14, 0, 0, 19)
    OP_6F(0x79)
    Sleep(500)

    #N0025
    NpcTalk(
        0x101,
        "琪雅",
        "#5801F#5P被追上了……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#0010F#6P……到此为止了吗………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1854, 255, 100, 0)    #voice#Garcia
    Sleep(800)

    #N0027
    NpcTalk(
        0xD,
        "豪气的声音",
        (
            "#1P哎呀呀……\x01",
            "没想到是你们啊。\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_68(-24000, -3000, -49950, 4000)
    MoveCamera(40, 18, 0, 4000)

    def lambda_1DB6():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1DB6)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)

    #C0028
    ChrTalk(
        0x101,
        "#0001F#6P加尔西亚·罗西……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0029
    AnonymousTalk(
        0xD,
        (
            "支援科的小鬼们……\x01",
            "真是好久不见了啊。\x02\x03",

            "哼哼，难怪我觉得\x01",
            "那两个小鬼有点眼熟。\x02\x03",

            "没想到你们居然能弄到邀请卡，\x01",
            "混到竞拍会里啊。\x02",
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

    #C0030
    ChrTalk(
        0x101,
        (
            "#0004F#6P……不过，你们好像\x01",
            "也没有规定\x01",
            "禁止警察参加吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xD,
        (
            "#3105F#11P嗯，的确没有啊。\x02\x03",

            "#3104F来者不拒……\x01",
            "如果是客户的话，当然热烈欢迎。\x02\x03",

            "#3101F不过呢，说实话，我真是小看你们了。\x02\x03",

            "没想到你们竟然与『黑月』勾结，\x01",
            "引起这么大的骚动啊。\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #N0032
    NpcTalk(
        0x101,
        "琪雅",
        "#5805F#5P黑月？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0011F#6P这、这话从何说起！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_20EE")

    #C0034
    ChrTalk(
        0x102,
        (
            "#0103F#6P……『银』和我们\x01",
            "没有任何关系。\x02\x03",

            "#0101F不相信的话，就问问你那些\x01",
            "昏迷的部下怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BE")

    label("loc_20EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_215B")

    #C0035
    ChrTalk(
        0x103,
        (
            "#0203F#6P『银』和我们\x01",
            "并没有任何关系……\x02\x03",

            "#0211F如果不相信，可以去问问\x01",
            "您那些昏迷的部下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BE")

    label("loc_215B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_21BE")

    #C0036
    ChrTalk(
        0x104,
        (
            "#0306F#6P『银』和我们\x01",
            "可没有任何关系啊。\x02\x03",

            "#0301F不信的话，就问问你那些昏迷的部下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BE")


    #C0037
    ChrTalk(
        0x105,
        (
            "#0406F#5P而且，反倒可以说是我们\x01",
            "赶走了入侵宅邸的他呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xD,
        (
            "#3105F#11P嗯～是这样吗？\x02\x03",

            "#3104F……也罢，事到如今，\x01",
            "那些也都无所谓了。\x02\x03",

            "重要的问题是，\x01",
            "你们这次让我们颜面丢尽……\x02\x03",

            "#3100F这笔账，可一定要\x01",
            "好好算清楚才行啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0006F#6P……看样子，我们就算说投降，\x01",
            "你也不会听了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xD,
        (
            "#3104F#11P哼哼，难得的狩猎，\x01",
            "连猎物的惨叫声都还没听到，\x01",
            "怎么能轻易收场呢……？\x02\x03",

            "#3100F放心吧……\x01",
            "我还没打算取你们的性命。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sleep(150)
    Sound(1857, 255, 100, 0)    #voice#Garcia
    Fade(250)
    Sound(804, 0, 100, 0)
    BeginChrThread(0xD, 0, 0, 10)
    OP_0D()
    Sound(929, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7404", 0)
    Sleep(500)
    SetCameraDistance(18000, 20000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0041
    ChrTalk(
        0xD,
        (
            "#3102F#11P砍断一两条胳膊之后，\x01",
            "便饶过你们好了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0110F#6P……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#0201F#6P好像要来真的……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0301F#6P真是的……\x01",
            "也不考虑一下自己的年纪啊，大叔。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xD,
        (
            "#3104F#11P哼哼……\x01",
            "你们可要让我好好开心一下。\x02\x03",

            "#3107F让我这个好久都没有狩猎，\x01",
            "已经热血沸腾的『杀戮之熊』玩个痛快啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0013F#6P呜……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        "#0407F#5P来了……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16860, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_24(0x1DF)
    OP_C7(0x0, 0x4000)
    Battle("BattleInfo_4B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_C7(0x1, 0x4000)
    EndChrThread(0xD, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)
    Call(0, 38)
    Return()

    # Function_9_A7C end

    def Function_10_254B(): pass

    label("Function_10_254B")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2553")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_256E")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_2553")

    label("loc_256E")

    Return()

    # Function_10_254B end

    def Function_11_256F(): pass

    label("Function_11_256F")

    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)

    label("loc_2582")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_259F")
    OP_A1(0xFE, 0x3E8, 0x4, 0x1, 0x2, 0x3, 0x4)
    Sleep(1000)
    Jump("loc_2582")

    label("loc_259F")

    Return()

    # Function_11_256F end

    def Function_12_25A0(): pass

    label("Function_12_25A0")

    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)

    label("loc_25A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25C7")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_25A8")

    label("loc_25C7")

    Return()

    # Function_12_25A0 end

    def Function_13_25C8(): pass

    label("Function_13_25C8")

    SetChrChipByIndex(0xFE, 0x3B)
    SetChrSubChip(0xFE, 0x0)

    label("loc_25D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25EF")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_25D0")

    label("loc_25EF")

    Return()

    # Function_13_25C8 end

    def Function_14_25F0(): pass

    label("Function_14_25F0")

    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)

    label("loc_25F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2617")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_25F8")

    label("loc_2617")

    Return()

    # Function_14_25F0 end

    def Function_15_2618(): pass

    label("Function_15_2618")

    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_263E")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(1000)
    Jump("loc_2620")

    label("loc_263E")

    Return()

    # Function_15_2618 end

    def Function_16_263F(): pass

    label("Function_16_263F")

    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2647")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26A6")
    OP_A1(0xFE, 0x3E8, 0x1, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 80, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(1000)
    Jump("loc_2647")

    label("loc_26A6")

    Return()

    # Function_16_263F end

    def Function_17_26A7(): pass

    label("Function_17_26A7")

    SetChrChipByIndex(0xFE, 0x3F)
    SetChrSubChip(0xFE, 0x0)

    label("loc_26AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2848")
    Sound(355, 0, 80, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    Sleep(1000)
    Jump("loc_26AF")

    label("loc_2848")

    Return()

    # Function_17_26A7 end

    def Function_18_2849(): pass

    label("Function_18_2849")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_285C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2877")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_285C")

    label("loc_2877")

    Return()

    # Function_18_2849 end

    def Function_19_2878(): pass

    label("Function_19_2878")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_288B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28A9")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_288B")

    label("loc_28A9")

    Return()

    # Function_19_2878 end

    def Function_20_28AA(): pass

    label("Function_20_28AA")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, 13510, -3060, -32119, 90)

    def lambda_28C8():
        OP_95(0xFE, 13210, -4000, -38990, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28C8)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 16)
    WaitChrThread(0xFE, 0)
    Return()

    # Function_20_28AA end

    def Function_21_28EC(): pass

    label("Function_21_28EC")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, 14500, -2080, -30160, 90)

    def lambda_290A():
        OP_95(0xFE, 14810, -4000, -37790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_290A)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 17)
    WaitChrThread(0xFE, 0)
    Return()

    # Function_21_28EC end

    def Function_22_292E(): pass

    label("Function_22_292E")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)

    def lambda_293D():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_293D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_292E end

    def Function_23_2957(): pass

    label("Function_23_2957")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2964():
        OP_95(0xFE, 12970, -4000, -48160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2964)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)
    OP_A1(0xFE, 0x3E8, 0x1, 0x2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x4)
    Sleep(1000)
    OP_A1(0xFE, 0x3E8, 0x1, 0x2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x4)
    Sleep(200)
    OP_A1(0xFE, 0x3E8, 0x2, 0x1, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2A47():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A47)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_2957 end

    def Function_24_2A61(): pass

    label("Function_24_2A61")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2A6E():
        OP_95(0xFE, 14350, -4000, -48920, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A6E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0x0, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 100, 0)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    PlayEffect(0x2, 0x1, 0xFE, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x3, 0xFF, 0xFF, 0x140, 14090, -4000, -40140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2B78():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B78)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_2A61 end

    def Function_25_2B92(): pass

    label("Function_25_2B92")

    OP_93(0xFE, 0x0, 0x12C)
    Sleep(600)

    def lambda_2BA1():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BA1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_2B92 end

    def Function_26_2BBB(): pass

    label("Function_26_2BBB")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_2BC7():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BC7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_2BBB end

    def Function_27_2BE1(): pass

    label("Function_27_2BE1")

    SetChrPos(0xFE, -5750, -4000, -50700, 270)

    def lambda_2BF7():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BF7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_2BE1 end

    def Function_28_2C0C(): pass

    label("Function_28_2C0C")

    SetChrPos(0xFE, -15280, -4000, -52250, 90)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2C25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C88")
    Sleep(850)
    OP_A1(0xFE, 0x3E8, 0x1, 0x2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x4)
    Jump("loc_2C25")

    label("loc_2C88")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2CA3():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CA3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_2C0C end

    def Function_29_2CBD(): pass

    label("Function_29_2CBD")

    SetChrPos(0xFE, -15780, -4000, -48270, 90)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2CD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E7A")
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0x0, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 100, 0)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    PlayEffect(0x2, 0x1, 0xFE, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_2D9C"),
        (1, "loc_2DE2"),
        (2, "loc_2E28"),
        (SWITCH_DEFAULT, "loc_2E6E"),
    )


    label("loc_2D9C")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -6250, -4000, -50610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E6E")

    label("loc_2DE2")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -9950, -4000, -50630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E6E")

    label("loc_2E28")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -3370, -4000, -51680, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E6E")

    label("loc_2E6E")

    SetChrSubChip(0xFE, 0x4)
    Sleep(1200)
    Jump("loc_2CD6")

    label("loc_2E7A")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2E95():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E95)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_2CBD end

    def Function_30_2EAF(): pass

    label("Function_30_2EAF")

    SetChrPos(0xFE, -11920, -4000, -51900, 90)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_2ECA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FA5")
    SetChrChipByIndex(0xFE, 0x3B)
    SetChrSubChip(0xFE, 0x0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)

    def lambda_2EEE():
        OP_9B(0x1, 0xFE, 0x0, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EEE)
    Sound(532, 0, 80, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x2, 0x3, 0x4, 0x5)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0xFE, 0x140, 0, 750, 600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_2F5E():
        OP_A6(0xFE, 0x0, 0x28, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F5E)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    Sound(814, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFD170, 0xFFFFF060, 0xFFFF3544, 0x1F4, 0xFA0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2ECA")

    label("loc_2FA5")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2FCA():
        OP_97(0xFE, 0xFFFFE0C0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FCA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_30_2EAF end

    def Function_31_2FE4(): pass

    label("Function_31_2FE4")

    SetChrPos(0xFE, -9920, -4000, -51900, 270)

    label("loc_2FF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_307C")
    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)
    Sleep(400)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0xFFFFDD28, 0xFFFFF060, 0xFFFF3544, 0x1F4, 0x1770)
    SetChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)

    def lambda_3041():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3041)
    OP_A1(0xFE, 0x5DC, 0x4, 0x2, 0x4, 0x1, 0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3065")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3077")
    Sleep(1)
    Jump("loc_3065")

    label("loc_3077")

    Jump("loc_2FF5")

    label("loc_307C")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_2FE4 end

    def Function_32_3085(): pass

    label("Function_32_3085")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -11560, -4000, -49320, 90)

    label("loc_30A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_312C")
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x3)

    def lambda_30C1():
        OP_9D(0xFE, 0xFFFFD6C0, 0xFFFFF060, 0xFFFF3F58, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30C1)
    WaitChrThread(0xFE, 1)
    Sound(534, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x14, 0x13)
    Sleep(250)
    OP_A1(0xFE, 0x5DC, 0x2, 0xE, 0x3)
    Sleep(100)

    def lambda_30FE():
        OP_9D(0xFE, 0xFFFFD2D8, 0xFFFFF060, 0xFFFF3F58, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30FE)
    WaitChrThread(0xFE, 1)
    Sleep(400)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A5")

    label("loc_312C")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3156():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3156)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_32_3085 end

    def Function_33_3170(): pass

    label("Function_33_3170")

    SetChrPos(0xFE, -8560, -4000, -49320, 270)

    label("loc_3181")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3204")
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x4)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)

    def lambda_31A4():
        OP_9B(0x1, 0xFE, 0xB4, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31A4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x4)
    Sleep(400)

    def lambda_31C4():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31C4)
    OP_A1(0xFE, 0x9C4, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    WaitChrThread(0xFE, 1)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FF")
    Sleep(1)
    Jump("loc_31ED")

    label("loc_31FF")

    Jump("loc_3181")

    label("loc_3204")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_3170 end

    def Function_34_3218(): pass

    label("Function_34_3218")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -1840, -4000, -50740, 270)
    BeginChrThread(0xFE, 0, 0, 16)
    Return()

    # Function_34_3218 end

    def Function_35_3238(): pass

    label("Function_35_3238")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -4610, -4000, -49060, 270)
    BeginChrThread(0xFE, 0, 0, 17)
    Return()

    # Function_35_3238 end

    def Function_36_3258(): pass

    label("Function_36_3258")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -5870, -4000, -51790, 270)
    BeginChrThread(0xFE, 0, 0, 17)
    Return()

    # Function_36_3258 end

    def Function_37_327B(): pass

    label("Function_37_327B")

    OP_25(0x1DF, 0x5A)
    Sleep(300)
    OP_25(0x1DF, 0x50)
    Sleep(300)
    OP_25(0x1DF, 0x46)
    Sleep(300)
    OP_25(0x1DF, 0x3C)
    Sleep(300)
    OP_25(0x1DF, 0x32)
    Sleep(300)
    OP_25(0x1DF, 0x28)
    Sleep(300)
    OP_25(0x1DF, 0x1E)
    Sleep(300)
    OP_25(0x1DF, 0x14)
    Sleep(300)
    OP_25(0x1DF, 0xA)
    Sleep(300)
    OP_24(0x1DF)
    Return()

    # Function_37_327B end

    def Function_38_32BE(): pass

    label("Function_38_32BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31952.itc", 0x27)
    LoadChrToIndex("chr/ch31951.itc", 0x28)
    LoadChrToIndex("chr/ch31953.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00150.itc", 0x2C)
    LoadChrToIndex("chr/ch00151.itc", 0x2D)
    LoadChrToIndex("chr/ch00250.itc", 0x2E)
    LoadChrToIndex("chr/ch00251.itc", 0x2F)
    LoadChrToIndex("chr/ch00350.itc", 0x30)
    LoadChrToIndex("chr/ch00351.itc", 0x31)
    LoadChrToIndex("chr/ch00450.itc", 0x32)
    LoadChrToIndex("chr/ch00451.itc", 0x33)
    LoadChrToIndex("chr/ch02200.itc", 0x34)
    LoadChrToIndex("chr/ch02250.itc", 0x35)
    LoadChrToIndex("monster/ch67150.itc", 0x36)
    LoadChrToIndex("monster/ch67151.itc", 0x37)
    LoadChrToIndex("chr/ch02750.itc", 0x38)
    LoadChrToIndex("apl/ch50542.itc", 0x39)
    LoadChrToIndex("chr/ch02251.itc", 0x3A)
    LoadChrToIndex("chr/ch02252.itc", 0x3B)
    LoadChrToIndex("chr/ch02253.itc", 0x3C)
    LoadChrToIndex("chr/ch02254.itc", 0x3D)
    LoadChrToIndex("apl/ch50122.itc", 0x3E)
    LoadChrToIndex("chr/ch00357.itc", 0x3F)
    LoadChrToIndex("chr/ch02751.itc", 0x40)
    LoadChrToIndex("chr/ch02752.itc", 0x41)
    LoadChrToIndex("chr/ch00352.itc", 0x42)
    LoadChrToIndex("apl/ch50026.itc", 0x43)
    LoadChrToIndex("chr/ch31000.itc", 0x44)
    LoadEffect(0x0, "event\\ev305_00.eff")
    LoadEffect(0x1, "event\\ev306_00.eff")
    LoadEffect(0x2, "battle\\ms00001.eff")
    LoadEffect(0x3, "event\\ev314_00.eff")
    LoadEffect(0x4, "event\\ev315_00.eff")
    LoadEffect(0x5, "battle\\cr003300.eff")
    SoundLoad(930)
    SoundLoad(483)
    SetMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 17000, -5500, -63000, 270)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x400)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2E)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x32)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -26710, -4000, -49230, 90)
    SetChrPos(0x102, -28160, -4000, -48980, 90)
    SetChrPos(0x103, -29510, -4000, -50870, 90)
    SetChrPos(0x104, -26230, -4000, -50670, 90)
    SetChrPos(0x105, -28120, -4000, -51340, 90)
    SetChrPos(0x133, -29910, -4000, -49130, 90)
    SetChrChipByIndex(0x17, 0x40)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x4)
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x3)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x3)
    SetChrChipByIndex(0xE, 0x29)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0xD, 0x3C)
    SetChrSubChip(0xD, 0x3)
    SetChrChipByIndex(0x13, 0x3E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x3E)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x3E)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x11, -20750, -4000, -51500, 270)
    SetChrPos(0x10, -17500, -4000, -48000, 270)
    SetChrPos(0xE, -18750, -4000, -50500, 270)
    SetChrPos(0x13, -19900, -4000, -47200, 270)
    SetChrPos(0x14, -17500, -4000, -52000, 270)
    SetChrPos(0x15, -19000, -4000, -50000, 270)
    SetChrPos(0xD, -21500, -4000, -50000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4613")
    OP_68(-24270, -3000, -50000, 0)
    MoveCamera(51, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18360, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(19860, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0048
    ChrTalk(
        0x101,
        "#0010F#6P呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x105,
        "#0406F#6P真是相当难对付啊……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x11,
        "#11P#40W……副、副头目……！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xE,
        "#11P#40W……您、您没事吧！？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xD,
        (
            "#3104F#11P#40W哼哼哼……哈哈哈哈……\x02\x03",

            "#3100F……本来没对你们抱多大期待，\x01",
            "想不到竟然还有点能耐，真是有趣啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0xD, 0x1)
    Sleep(150)
    OP_68(-23830, -2900, -49830, 1000)
    Fade(250)
    BeginChrThread(0xD, 0, 0, 10)
    OP_0D()
    Sound(929, 0, 100, 0)
    Sleep(500)
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_3984():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3984)

    def lambda_399D():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_399D)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x3)
    SetChrChipByIndex(0x13, 0x36)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 19)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sound(531, 0, 100, 0)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x13, 2)
    Sleep(500)

    def lambda_39EC():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_39EC)

    def lambda_3A05():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3A05)

    def lambda_3A1E():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3A1E)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x3)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0x14, 0x36)
    SetChrSubChip(0x14, 0x0)
    BeginChrThread(0x14, 0, 0, 19)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sound(531, 0, 100, 0)
    WaitChrThread(0x10, 2)
    WaitChrThread(0xE, 2)
    WaitChrThread(0x14, 2)

    #C0053
    ChrTalk(
        0x133,
        (
            "#5805F#5P哇……\x01",
            "复活了。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#0007F#6P不、不可能吧……！？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#0401F#6P#N好像比瓦鲁多\x01",
            "都要耐打很多呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0056
    ChrTalk(
        0x104,
        "#0301F#6P嘁……这怪物。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        (
            "#3104F#11P哼哼，这话说得真可笑啊。\x02\x03",

            "#3102F──兰道夫·奥兰多，\x01",
            "你不也是一样吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0x12C)

    #C0058
    ChrTalk(
        0x104,
        "#0310F#6P……！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#0005F#5P兰迪……？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xD,
        (
            "#3102F#11P哼哼，果然如此啊。\x02\x03",

            "#3104F出身于大陆西部最强的猎兵团之一\x01",
            "——『赤色星座』……\x02\x03",

            "身为团长之子，\x01",
            "从小率领着大部队，\x01",
            "杀敌无数的红色死神……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0061
    ChrTalk(
        0xD,
        (
            "#3107F#11P#4S──『斗神之子』\x01",
            "兰道夫·奥兰多……！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#0311F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#0011F#6P『斗神之子』……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#0208F#6P#N『赤色星座』……\x01",
            "是很有名的猎兵团呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0065
    ChrTalk(
        0x102,
        "#0106F#6P……是这样吗………\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0304F#5P──哈哈。\x01",
            "既然暴露了，那就没办法啦。\x02\x03",

            "#0312F嗯，那大叔的话\x01",
            "基本没错。\x02\x03",

            "只是『斗神之子』这个称号\x01",
            "让我恶心到想要作呕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xD,
        (
            "#3102F#11P哼哼，看样子，你是因为某些特殊原因\x01",
            "而流落到克洛斯贝尔的啊。\x02\x03",

            "#3104F我的老巢『西风旅团』\x01",
            "与『赤色星座』可是多年的宿敌……\x02\x03",

            "正好，我们就在这里\x01",
            "来个宿命的对决吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0068
    ChrTalk(
        0xD,
        "#3107F#11P这次就一对一地决胜负吧！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        "#0311F#6P……满嘴废话……\x02",
    )

    CloseMessageWindow()
    OP_68(-23150, -3000, -49620, 1500)
    MoveCamera(44, 18, 0, 1500)
    SetChrChipByIndex(0x104, 0x31)
    SetChrSubChip(0x104, 0x0)

    def lambda_3EF1():
        OP_95(0xFE, -25200, -4000, -50000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EF1)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0x104, 0x5A, 0x190)
    OP_6F(0x79)

    #C0070
    ChrTalk(
        0x101,
        "#0007F#6P喂，兰迪……！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0303F#5P……这里就交给我。\x02\x03",

            "#0301F只要打倒这个大叔，\x01",
            "应该就能打开突破口了。\x02\x03",

            "#0307F不用管我……\x01",
            "你们赶快逃离这里吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#0010F#6P那怎么行……！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#0107F#6P#N不、不行啊……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0074
    ChrTalk(
        0x103,
        "#0201F#6P#N这、这可不像你啊……！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrChipByIndex(0x104, 0x3F)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)
    Sound(1301, 255, 100, 0)    #voice#Randy
    BeginChrThread(0x101, 3, 0, 40)
    BeginChrThread(0x1A, 1, 0, 72)
    MoveCamera(45, 18, 0, 2500)
    SetCameraDistance(15860, 2500)
    Sleep(200)
    PlayEffect(0x5, 0xFF, 0x104, 0x140, 0, 700, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sleep(2000)
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    Sleep(300)
    Sound(1310, 255, 100, 0)    #voice#Randy
    SetCameraDistance(21360, 800)
    SetChrSubChip(0x104, 0x1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1000)
    PlayEffect(0x0, 0x0, 0x104, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sound(256, 0, 100, 0)
    OP_6F(0x79)
    Sound(325, 0, 100, 0)
    EndChrThread(0x1A, 0x1)
    BeginChrThread(0x101, 3, 0, 40)
    BeginChrThread(0x101, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 58)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 59)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 60)
    Sleep(50)
    BeginChrThread(0x133, 3, 0, 61)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x133, 3)
    Sleep(1300)

    #C0075
    ChrTalk(
        0xD,
        (
            "#3104F#11P『战场咆哮』……\x02\x03",

            "引发出爆发性的斗气，\x01",
            "是猎兵特有的战斗技术……\x02\x03",

            "#3102F哼哼，就是要这样才有趣！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1858, 255, 100, 0)    #voice#Garcia
    OP_68(-21510, -3000, -48550, 2500)
    SetCameraDistance(16860, 2500)
    Sleep(500)
    PlayEffect(0x5, 0xFF, 0xD, 0x140, 0, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    EndChrThread(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x3D)
    SetChrSubChip(0xD, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sleep(2500)
    EndChrThread(0x101, 0x3)
    SetCameraDistance(21360, 800)
    SetChrSubChip(0xD, 0x4)
    BeginChrThread(0xD, 0, 0, 39)
    Sound(1840, 255, 100, 1)    #voice#Garcia
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1000)
    PlayEffect(0x1, 0x1, 0xD, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x258, 0x1770, 0x1F4)
    Sound(256, 0, 100, 0)
    Sound(325, 0, 100, 0)
    OP_6F(0x79)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 40)

    #C0076
    ChrTalk(
        0x11,
        "#11P呜……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xE,
        "#11P退、退后……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 63)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 64)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 65)
    Sleep(50)
    BeginChrThread(0x14, 3, 0, 65)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    Sleep(500)
    OP_68(-25050, -3000, -48760, 1500)
    MoveCamera(45, 16, 0, 1500)
    OP_6E(540, 1500)
    SetCameraDistance(21360, 1500)
    OP_6F(0x79)

    #C0078
    ChrTalk(
        0x105,
        "#0410F#6P呜……好厉害……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x133,
        "#5801F#6P#N噼噼啪啪的呢～……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0080
    ChrTalk(
        0x101,
        "#0010F#6P呜，这样下去的话──\x02",
    )

    CloseMessageWindow()
    Sound(846, 0, 100, 0)
    StopBGM(0x1388)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    CancelBlur(1000)
    BeginChrThread(0x1A, 1, 0, 73)
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x133, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(1500)
    EndChrThread(0x101, 0x3)
    OP_82(0x0, 0x12C, 0x1770, 0x1F4)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    Sleep(750)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(750)
    EndChrThread(0x1A, 0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_456D():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_456D)
    Sleep(50)

    def lambda_457D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_457D)
    Sleep(50)

    def lambda_458D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_458D)
    Sleep(50)

    def lambda_459D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_459D)
    Sleep(50)

    def lambda_45AD():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45AD)
    Sleep(50)

    def lambda_45BD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_45BD)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0xD, 1)

    #C0081
    ChrTalk(
        0x101,
        "#0005F#6P什么……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        "#0202F#6P这声远吠是……！\x02",
    )

    CloseMessageWindow()

    label("loc_4613")

    OP_68(-15500, -3000, -50000, 1500)
    MoveCamera(30, 26, 0, 1500)
    OP_6E(540, 1500)
    SetCameraDistance(19360, 1500)
    Sleep(500)
    SetChrPos(0x17, -5000, -4000, -50000, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    BeginChrThread(0x17, 3, 0, 43)
    WaitChrThread(0x17, 3)
    OP_68(-17000, -3000, -50000, 1000)
    OP_6F(0x79)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)

    def lambda_4689():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_4689)

    def lambda_46A2():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_46A2)
    Sound(847, 0, 100, 0)
    Sleep(250)
    Fade(500)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x3E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x3E)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0x13, 2)
    WaitChrThread(0x14, 2)
    BeginChrThread(0x17, 0, 0, 42)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x10, 0x13, 500)

    #C0083
    ChrTalk(
        0x10,
        "#11P什么……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x14, 500)

    #C0084
    ChrTalk(
        0xE,
        (
            "#5P喂、喂……！\x01",
            "不要退缩……！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x11)
    OP_64(0x10)
    OP_64(0xE)
    #Sound(2047, 255, 100, 0)    #voice#Zeit

    #C0085
    ChrTalk(
        0x17,
        "#1201F嗷噜噜呜呜呜！\x02",
    )

    CloseMessageWindow()
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-17550, -3000, -50000, 1500)
    MoveCamera(45, 18, 0, 2500)
    SetCameraDistance(17860, 1000)
    Sound(2049, 255, 100, 0)    #voice#Zeit
    BeginChrThread(0x17, 3, 0, 44)
    WaitChrThread(0x17, 3)
    OP_6F(0x79)
    OP_68(-18350, -3000, -50000, 1500)
    OP_6F(0x79)
    Fade(250)
    BeginChrThread(0xD, 0, 0, 10)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0086
    ChrTalk(
        0xD,
        "#3110F#6P嘁，区区一条狗……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x1A, 1, 0, 74)
    Fade(1000)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-22770, -3000, -50000, 0)
    OP_68(-24270, -3000, -50000, 1200)
    MoveCamera(30, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19860, 0)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x133, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0087
    ChrTalk(
        0x101,
        "#0002F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        "#0102F#6P那是……！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x1A, 0x1)
    Fade(500)
    BeginChrThread(0x1A, 1, 0, 75)
    Sound(481, 0, 100, 0)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0x104, 0x20)
    SetChrBattleFlags(0x105, 0x20)
    SetChrBattleFlags(0x133, 0x20)
    SetChrBattleFlags(0x16, 0x20)
    SetChrBattleFlags(0x17, 0x20)

    def lambda_49A6():

        label("loc_49A6")

        TurnDirection(0x101, 0x16, 500)
        Yield()
        Jump("loc_49A6")

    QueueWorkItem2(0x101, 1, lambda_49A6)

    def lambda_49B8():

        label("loc_49B8")

        TurnDirection(0x102, 0x16, 500)
        Yield()
        Jump("loc_49B8")

    QueueWorkItem2(0x102, 1, lambda_49B8)

    def lambda_49CA():

        label("loc_49CA")

        TurnDirection(0x103, 0x16, 500)
        Yield()
        Jump("loc_49CA")

    QueueWorkItem2(0x103, 1, lambda_49CA)

    def lambda_49DC():

        label("loc_49DC")

        TurnDirection(0x104, 0x16, 500)
        Yield()
        Jump("loc_49DC")

    QueueWorkItem2(0x104, 1, lambda_49DC)

    def lambda_49EE():

        label("loc_49EE")

        TurnDirection(0x105, 0x16, 500)
        Yield()
        Jump("loc_49EE")

    QueueWorkItem2(0x105, 1, lambda_49EE)

    def lambda_4A00():

        label("loc_4A00")

        TurnDirection(0x133, 0x16, 500)
        Yield()
        Jump("loc_4A00")

    QueueWorkItem2(0x133, 1, lambda_4A00)

    def lambda_4A12():

        label("loc_4A12")

        TurnDirection(0xD, 0x16, 500)
        Yield()
        Jump("loc_4A12")

    QueueWorkItem2(0xD, 1, lambda_4A12)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearMapObjFlags(0x1, 0x4)
    OP_D1(0x16, 0x1, "Null_Sheet")
    OP_68(2550, -2800, -63000, 0)
    MoveCamera(50, 22, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(50000, 0)
    SetCameraDistance(27000, 2700)
    BeginChrThread(0x19, 3, 0, 69)
    SetChrPos(0x19, 35000, -5500, -63000, 270)
    BeginChrThread(0x19, 1, 0, 71)
    Sleep(1150)
    MoveCamera(309, 12, 0, 2700)
    Sleep(2800)
    Fade(500)
    SetChrPos(0x19, -26000, -5500, -63000, 270)
    OP_68(-32460, -2400, -57410, 0)
    MoveCamera(55, 30, 0, 0)
    SetCameraDistance(36000, 0)
    OP_68(-35310, -2400, -51820, 2500)
    MoveCamera(45, 12, 0, 2500)
    SetCameraDistance(19000, 2500)

    def lambda_4B08():
        OP_9E(0xFE, 0xFFFF9A70, 0xFFFF30F8, 0x15F90, 0x2328, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4B08)
    Sleep(1750)

    def lambda_4B26():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4B26)
    Sleep(300)
    EndChrThread(0x19, 0x1)

    def lambda_4B47():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4B47)
    Sleep(350)
    EndChrThread(0x19, 0x1)

    def lambda_4B68():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4B68)
    WaitChrThread(0x19, 1)
    EndChrThread(0x19, 0x3)
    OP_82(0x0, 0x4B, 0x1194, 0x12C)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x133, 0x1)
    EndChrThread(0xD, 0x1)
    OP_93(0xD, 0x10E, 0x0)
    EndChrThread(0x1A, 0x1)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)

    #C0089
    ChrTalk(
        0x16,
        (
            "#1001F#5P……别磨磨蹭蹭的，\x01",
            "赶快上来。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#0000F#11P科长……！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x133,
        "#5810F#11P哇，是小船！\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#0202F#11P时机真是太巧了……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-22000, -3000, -50000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(19000, 1000)
    OP_0D()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0093
    ChrTalk(
        0xD,
        "#3107F#4S#11P休想逃跑啊啊啊！\x02",
    )

    CloseMessageWindow()

    def lambda_4CC3():
        OP_93(0xFE, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4CC3)
    Sleep(50)

    def lambda_4CD3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CD3)
    Sleep(50)

    def lambda_4CE3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4CE3)
    Sleep(50)

    def lambda_4CF3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4CF3)
    Sleep(50)

    def lambda_4D03():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4D03)
    Sleep(50)

    def lambda_4D13():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_4D13)
    OP_68(-23250, -3000, -50000, 500)
    SetCameraDistance(17500, 500)
    Sound(1820, 255, 100, 0)    #voice#Garcia
    BeginChrThread(0xD, 3, 0, 53)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 54)
    OP_6F(0x79)
    SetCameraDistance(16500, 30000)
    Sleep(1000)

    #C0094
    ChrTalk(
        0xD,
        "#3110F#11P唔，你这混账……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#0311F#6P抱歉了，大叔……\x01",
            "看来这次不能陪你玩了。\x02\x03",

            "#0303F话说回来……\x01",
            "你们知道吗……？\x02\x03",

            "#0301F那个竞拍会准备拍卖\x01",
            "『活生生的小孩』……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0xD,
        "#3105F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#0003F#6P……这孩子被装在拍卖品房间\x01",
            "中的皮革箱子里。\x02\x03",

            "#0001F这意味着什么，\x01",
            "你明白吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0098
    ChrTalk(
        0x133,
        "#5805F#2P哎～？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0099
    ChrTalk(
        0xD,
        (
            "#3107F#11P你、你在说什么胡话！\x02\x03",

            "那个箱子里放的明明\x01",
            "是罗赞贝尔克的人偶……！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x105,
        (
            "#0406F#6P#N哈，但这是事实啊。\x02\x03",

            "#0402F视具体情况发展，\x01",
            "后果也许会很严重哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0101
    ChrTalk(
        0x16,
        (
            "#1003F#2P哎呀呀……\x01",
            "似乎发生了奇怪的事情啊。\x02\x03",

            "#1001F──鲁巴彻的家伙，\x01",
            "下次再找你慢慢聊。\x02\x03",

            "你们自己先\x01",
            "整理一下状况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xD,
        "#3110F#11P唔……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x16,
        (
            "#1007F#2P特别任务支援科，撤退！\x01",
            "全都赶快上来！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#0007F#5P是！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_93(0x101, 0x10E, 0x0)
    OP_93(0x102, 0x10E, 0x0)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x105, 0x10E, 0x0)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_68(-33750, -2800, -50000, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19850, 0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x103, 3, 0, 48)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 47)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 50)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 46)
    BeginChrThread(0x17, 3, 0, 51)
    Sleep(300)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1300)
    MoveCamera(30, 14, 0, 2500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x104, 3)
    Sound(484, 0, 100, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Sound(482, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 70)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x17, 3)
    Sleep(1000)
    OP_68(-30800, -2800, -50000, 3000)
    SetChrChipByIndex(0x10, 0x43)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x43)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x10, 0x1)
    SetChrFlags(0x11, 0x1)
    SetChrPos(0x10, -17970, -4000, -48470, 270)
    SetChrPos(0x11, -18820, -4000, -51400, 270)

    def lambda_5185():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5185)

    def lambda_519A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_519A)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x10, 0x44)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x44)
    SetChrSubChip(0x11, 0x0)
    OP_6F(0x79)
    WaitChrThread(0x19, 3)

    #C0105
    ChrTalk(
        0x10,
        "#11P啊啊……！\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x11,
        (
            "#11P呜……\x01",
            "没有其它的船了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-30800, -2800, -50000, 2000)
    MoveCamera(59, 14, 0, 2000)
    OP_6E(540, 2000)
    SetCameraDistance(16350, 2000)

    #C0107
    ChrTalk(
        0xD,
        "#3110F#11P#50W唔唔唔唔唔～～～～……\x02",
    )

    CloseMessageWindow()
    OP_6F(0x1)
    Sleep(500)
    BlurSwitch(0xBB8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(56000, 4000)
    OP_82(0xC8, 0x0, 0x7D0, 0x5DC)

    #C0108
    ChrTalk(
        0xD,
        "#3107F#4S#11P#14A#70W呜噢噢噢噢噢噢噢噢噢！！\x02",
    )
    #Auto

    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    CancelBlur(0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x3A2)
    OP_24(0x1E3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t112B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_32BE end

    def Function_39_5308(): pass

    label("Function_39_5308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5321")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_39_5308")

    label("loc_5321")

    Return()

    # Function_39_5308 end

    def Function_40_5322(): pass

    label("Function_40_5322")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5346")
    OP_82(0x0, 0x28, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_40_5322")

    label("loc_5346")

    Return()

    # Function_40_5322 end

    def Function_41_5347(): pass

    label("Function_41_5347")

    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_535A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_537B")
    Sound(925, 0, 80, 0)
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_535A")

    label("loc_537B")

    Return()

    # Function_41_5347 end

    def Function_42_537C(): pass

    label("Function_42_537C")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_538F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53AD")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_538F")

    label("loc_53AD")

    Return()

    # Function_42_537C end

    def Function_43_53AE(): pass

    label("Function_43_53AE")

    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_53B9():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_53B9)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    Sound(2058, 255, 100, 0)    #voice#Zeit
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Sound(925, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x2D)
    CancelBlur(750)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Return()

    # Function_43_53AE end

    def Function_44_5428(): pass

    label("Function_44_5428")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_544C():
        OP_9D(0xFE, 0xFFFFC0A5, 0xFFFFF060, 0xFFFF4372, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_544C)
    Sleep(300)

    #C0109
    ChrTalk(
        0x10,
        "#6P呀！\x05\x02",
    )

    BeginChrThread(0x10, 3, 0, 66)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    Sound(925, 0, 100, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x1, 0x2)
    TurnDirection(0xFE, 0xE, 500)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_54AC():
        OP_9D(0xFE, 0xFFFFB35C, 0xFFFFF060, 0xFFFF3814, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_54AC)
    Sleep(300)

    #C0110
    ChrTalk(
        0xE,
        "#5P呜哇啊啊！？\x05\x02",
    )

    BeginChrThread(0xE, 3, 0, 67)
    Sleep(100)
    BeginChrThread(0x11, 3, 0, 68)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    Sound(925, 0, 100, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x1, 0x2)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_551D():
        OP_9D(0xFE, 0xFFFFC75C, 0xFFFFF060, 0xFFFF3CB0, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_551D)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    Sound(925, 0, 100, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x1, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    BeginChrThread(0x17, 0, 0, 42)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0xE, 3)
    Return()

    # Function_44_5428 end

    def Function_45_556E(): pass

    label("Function_45_556E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5585")
    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("Function_45_556E")

    label("loc_5585")

    Return()

    # Function_45_556E end

    def Function_46_5586(): pass

    label("Function_46_5586")

    SetChrFlags(0xFE, 0x4)

    def lambda_5590():
        OP_95(0xFE, -30390, -4000, -50000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5590)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_55C0():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55C0)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_55E7():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55E7)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_46_5586 end

    def Function_47_5615(): pass

    label("Function_47_5615")

    SetChrFlags(0xFE, 0x4)

    def lambda_561F():
        OP_95(0xFE, -30390, -4000, -48700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_561F)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)

    def lambda_5642():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5642)
    WaitChrThread(0xFE, 1)

    def lambda_5663():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5663)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_47_5615 end

    def Function_48_5691(): pass

    label("Function_48_5691")

    SetChrFlags(0xFE, 0x4)

    def lambda_569B():
        OP_95(0xFE, -30390, -4000, -51000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_569B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_56CB():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF379C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56CB)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_56F2():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF379C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56F2)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_48_5691 end

    def Function_49_5720(): pass

    label("Function_49_5720")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_5732():
        OP_95(0xFE, -29700, -4000, -50000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5732)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_575B():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_575B)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_5782():
        OP_9D(0xFE, 0xFFFF7388, 0xFFFFEE08, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5782)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_49_5720 end

    def Function_50_57B0(): pass

    label("Function_50_57B0")

    SetChrFlags(0xFE, 0x4)

    def lambda_57BA():
        OP_95(0xFE, -30300, -4000, -50250, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57BA)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)

    def lambda_57DD():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3DDC, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57DD)
    WaitChrThread(0xFE, 1)

    def lambda_57FE():
        OP_9D(0xFE, 0xFFFF7388, 0xFFFFEE08, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57FE)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_50_57B0 end

    def Function_51_582C(): pass

    label("Function_51_582C")

    Sleep(1500)
    EndChrThread(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_5843():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5843)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_588D():
        OP_9D(0xFE, 0xFFFFAC36, 0xFFFFF060, 0xFFFF44EE, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_588D)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_58D1():
        OP_95(0xFE, -25520, -4000, -48010, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_58D1)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_5920():
        OP_9D(0xFE, 0xFFFF92D2, 0xFFFFF380, 0xFFFF4B1A, 0x5DC, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5920)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_596E():
        OP_9D(0xFE, 0xFFFF8454, 0xFFFFF380, 0xFFFF4B6A, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_596E)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_59B5():
        OP_9D(0xFE, 0xFFFF7554, 0xFFFFEE08, 0xFFFF5AC4, 0x7D0, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59B5)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(925, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_51_582C end

    def Function_52_5A0D(): pass

    label("Function_52_5A0D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A3A")

    def lambda_5A1D():
        OP_A6(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A1D)
    WaitChrThread(0xFE, 2)
    Jump("Function_52_5A0D")

    label("loc_5A3A")

    Return()

    # Function_52_5A0D end

    def Function_53_5A3B(): pass

    label("Function_53_5A3B")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x3B)
    SetChrSubChip(0xFE, 0x0)
    Sound(534, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(750)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrFlags(0xFE, 0x20)

    def lambda_5A8E():
        OP_9B(0x0, 0xFE, 0x0, 0x546, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A8E)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    BeginChrThread(0xFE, 1, 0, 52)

    label("loc_5ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ACD")
    Sleep(1)
    Jump("loc_5ABB")

    label("loc_5ACD")

    Sleep(400)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Sound(804, 0, 100, 0)

    def lambda_5AEB():
        OP_9D(0xFE, 0xFFFFAC04, 0xFFFFF060, 0xFFFF3CB0, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AEB)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sleep(1350)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_5B2B():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B2B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_53_5A3B end

    def Function_54_5B48(): pass

    label("Function_54_5B48")

    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)

    def lambda_5B60():
        OP_9B(0x0, 0xFE, 0x0, 0x47E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B60)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x42)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0xFE, 1, 0, 52)
    OP_82(0x1F4, 0x0, 0x1770, 0x12C)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1000, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(830, 0, 100, 0)
    Sound(834, 0, 100, 0)

    label("loc_5BD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE8")
    Sleep(1)
    Jump("loc_5BD6")

    label("loc_5BE8")

    EndChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0x42)
    SetChrSubChip(0xFE, 0x0)
    Sound(532, 0, 100, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -23450, -3000, -50000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(830, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    Call(0, 49)
    Return()

    # Function_54_5B48 end

    def Function_55_5C58(): pass

    label("Function_55_5C58")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5C65():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C65)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_55_5C58 end

    def Function_56_5C82(): pass

    label("Function_56_5C82")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5C8F():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C8F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_5C82 end

    def Function_57_5CAC(): pass

    label("Function_57_5CAC")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5CB9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5CB9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_57_5CAC end

    def Function_58_5CD6(): pass

    label("Function_58_5CD6")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5CE3():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5CE3)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_58_5CD6 end

    def Function_59_5D00(): pass

    label("Function_59_5D00")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5D0D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D0D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_59_5D00 end

    def Function_60_5D2A(): pass

    label("Function_60_5D2A")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5D37():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D37)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_60_5D2A end

    def Function_61_5D54(): pass

    label("Function_61_5D54")


    def lambda_5D59():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D59)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_61_5D54 end

    def Function_62_5D6E(): pass

    label("Function_62_5D6E")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5D8D():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D8D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    OP_64(0xFE)
    Return()

    # Function_62_5D6E end

    def Function_63_5DAD(): pass

    label("Function_63_5DAD")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5DCC():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5DCC)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    OP_64(0xFE)
    Return()

    # Function_63_5DAD end

    def Function_64_5DEC(): pass

    label("Function_64_5DEC")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5E0B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E0B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_64(0xFE)
    Return()

    # Function_64_5DEC end

    def Function_65_5E2B(): pass

    label("Function_65_5E2B")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)

    def lambda_5E54():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E54)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    OP_64(0xFE)
    Return()

    # Function_65_5E2B end

    def Function_66_5E7A(): pass

    label("Function_66_5E7A")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -17000, -3000, -48000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_5EDA():
        OP_9D(0xFE, 0xFFFFB1E0, 0xFFFFE0C0, 0xFFFF63C0, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5EDA)
    Sleep(1000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -19500, -5000, -42000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(927, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_66_5E7A end

    def Function_67_5F3F(): pass

    label("Function_67_5F3F")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -18750, -3000, -50500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_5F9F():
        OP_9D(0xFE, 0xFFFFB636, 0xFFFFF060, 0xFFFF383C, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5F9F)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_67_5F3F end

    def Function_68_5FCA(): pass

    label("Function_68_5FCA")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -20750, -3000, -51500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_602A():
        OP_9D(0xFE, 0xFFFFADF8, 0xFFFFF060, 0xFFFF33F0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_602A)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_68_5FCA end

    def Function_69_6055(): pass

    label("Function_69_6055")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_60B0")
    PlayEffect(0x4, 0xFF, 0xFE, 0x100, 0, 0, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x14, 0x3E8, 0xA6)
    Sleep(166)
    Jump("Function_69_6055")

    label("loc_60B0")

    Return()

    # Function_69_6055 end

    def Function_70_60B1(): pass

    label("Function_70_60B1")

    BeginChrThread(0x19, 2, 0, 69)

    def lambda_60BC():
        OP_98(0xFE, 0x0, 0x0, 0x3A98, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_60BC)
    Sleep(1200)

    def lambda_60D9():
        OP_9E(0xFE, 0xFFFF0880, 0xFFFF7860, 0xFFFEA070, 0x2EE0, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_60D9)
    WaitChrThread(0x19, 1)
    EndChrThread(0x19, 0x2)
    Return()

    # Function_70_60B1 end

    def Function_71_60F8(): pass

    label("Function_71_60F8")

    SetChrPos(0xFE, 35000, -5500, -63000, 270)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 35000, -5500, -63000)
    OP_9F(0x1, -17000, -5500, -63000)
    OP_9F(0x1, -28000, -5500, -63000)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_71_60F8 end

    def Function_72_6141(): pass

    label("Function_72_6141")

    Sound(930, 2, 0, 0)
    Sleep(100)
    OP_25(0x3A2, 0xA)
    Sleep(100)
    OP_25(0x3A2, 0x14)
    Sleep(100)
    OP_25(0x3A2, 0x1E)
    Sleep(100)
    OP_25(0x3A2, 0x28)
    Sleep(100)
    OP_25(0x3A2, 0x32)
    Sleep(200)
    OP_25(0x3A2, 0x3C)
    Sleep(200)
    OP_25(0x3A2, 0x46)
    Sleep(200)
    OP_25(0x3A2, 0x50)
    Sleep(200)
    OP_25(0x3A2, 0x5A)
    Sleep(200)
    OP_25(0x3A2, 0x64)
    Return()

    # Function_72_6141 end

    def Function_73_618E(): pass

    label("Function_73_618E")

    OP_25(0x3A2, 0x5A)
    Sleep(200)
    OP_25(0x3A2, 0x50)
    Sleep(200)
    OP_25(0x3A2, 0x46)
    Sleep(200)
    OP_25(0x3A2, 0x3C)
    Sleep(200)
    OP_25(0x3A2, 0x32)
    Sleep(200)
    OP_25(0x3A2, 0x28)
    Sleep(200)
    OP_25(0x3A2, 0x1E)
    Sleep(200)
    OP_25(0x3A2, 0x14)
    Sleep(200)
    OP_25(0x3A2, 0xA)
    Sleep(200)
    OP_24(0x3A2)
    Return()

    # Function_73_618E end

    def Function_74_61D1(): pass

    label("Function_74_61D1")

    Sound(483, 2, 0, 0)
    Sleep(100)
    OP_25(0x1E3, 0xA)
    Sleep(100)
    OP_25(0x1E3, 0x14)
    Sleep(100)
    OP_25(0x1E3, 0x1E)
    Sleep(100)
    OP_25(0x1E3, 0x28)
    Sleep(100)
    OP_25(0x1E3, 0x32)
    Sleep(100)
    OP_25(0x1E3, 0x3C)
    Sleep(100)
    OP_25(0x1E3, 0x46)
    Sleep(100)
    OP_25(0x1E3, 0x50)
    Sleep(100)
    OP_25(0x1E3, 0x5A)
    Sleep(100)
    OP_25(0x1E3, 0x64)
    Return()

    # Function_74_61D1 end

    def Function_75_621E(): pass

    label("Function_75_621E")

    OP_25(0x1E3, 0x5A)
    Sleep(100)
    OP_25(0x1E3, 0x50)
    Sleep(100)
    OP_25(0x1E3, 0x46)
    Sleep(100)
    OP_25(0x1E3, 0x3C)
    Sleep(100)
    OP_25(0x1E3, 0x32)
    Sleep(100)
    OP_25(0x1E3, 0x28)
    Sleep(100)
    OP_25(0x1E3, 0x1E)
    Sleep(100)
    OP_25(0x1E3, 0x14)
    Sleep(100)
    OP_25(0x1E3, 0xA)
    Sleep(100)
    OP_24(0x1E3)
    Return()

    # Function_75_621E end

    def Function_76_6261(): pass

    label("Function_76_6261")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前往『克洛斯贝尔市』的水上巴士·时刻表\x01\x01",
            "   ※期待着您的\x01",
            "　       下次乘坐！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_76_6261 end

    SaveToFile()

Try(main)
