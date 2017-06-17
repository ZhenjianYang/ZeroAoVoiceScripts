from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "乗組員サルサ",           # 1
        "観光客",                 # 2
        "貴族の青年",             # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "ガルシア",               # 6
        "マフィア",               # 7
        "マフィア",               # 8
        "マフィア",               # 9
        "マフィア",               # 10
        "マフィア",               # 11
        "犬１",                   # 12
        "犬２",                   # 13
        "犬３",                   # 14
        "セルゲイ課長",           # 15
        "ツァイト",               # 16
        "水上バス",               # 17
        "ボート",                 # 18
        "SE制御",                 # 19
        "bt100b",                 # 20
        "テーマパーク方面",       # 21
        "邸宅方面",               # 22
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

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "テーマパーク方面")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "邸宅方面")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ScpFunction((
        "Function_0_62C",          # 00, 0
        "Function_1_6E4",          # 01, 1
        "Function_2_71E",          # 02, 2
        "Function_3_7C4",          # 03, 3
        "Function_4_886",          # 04, 4
        "Function_5_909",          # 05, 5
        "Function_6_969",          # 06, 6
        "Function_7_9DA",          # 07, 7
        "Function_8_A14",          # 08, 8
        "Function_9_AE8",          # 09, 9
        "Function_10_26DB",        # 0A, 10
        "Function_11_26FF",        # 0B, 11
        "Function_12_2730",        # 0C, 12
        "Function_13_2758",        # 0D, 13
        "Function_14_2780",        # 0E, 14
        "Function_15_27A8",        # 0F, 15
        "Function_16_27CF",        # 10, 16
        "Function_17_2837",        # 11, 17
        "Function_18_29D9",        # 12, 18
        "Function_19_2A08",        # 13, 19
        "Function_20_2A3A",        # 14, 20
        "Function_21_2A7C",        # 15, 21
        "Function_22_2ABE",        # 16, 22
        "Function_23_2AE7",        # 17, 23
        "Function_24_2BF1",        # 18, 24
        "Function_25_2D22",        # 19, 25
        "Function_26_2D4B",        # 1A, 26
        "Function_27_2D71",        # 1B, 27
        "Function_28_2D9C",        # 1C, 28
        "Function_29_2E4D",        # 1D, 29
        "Function_30_303F",        # 1E, 30
        "Function_31_3174",        # 1F, 31
        "Function_32_3215",        # 20, 32
        "Function_33_3300",        # 21, 33
        "Function_34_33A8",        # 22, 34
        "Function_35_33C8",        # 23, 35
        "Function_36_33E8",        # 24, 36
        "Function_37_340B",        # 25, 37
        "Function_38_344E",        # 26, 38
        "Function_39_564A",        # 27, 39
        "Function_40_5664",        # 28, 40
        "Function_41_5689",        # 29, 41
        "Function_42_56BE",        # 2A, 42
        "Function_43_56F0",        # 2B, 43
        "Function_44_576A",        # 2C, 44
        "Function_45_58B6",        # 2D, 45
        "Function_46_58CE",        # 2E, 46
        "Function_47_595D",        # 2F, 47
        "Function_48_59D9",        # 30, 48
        "Function_49_5A68",        # 31, 49
        "Function_50_5AF8",        # 32, 50
        "Function_51_5B74",        # 33, 51
        "Function_52_5D55",        # 34, 52
        "Function_53_5D83",        # 35, 53
        "Function_54_5E90",        # 36, 54
        "Function_55_5FA0",        # 37, 55
        "Function_56_5FCA",        # 38, 56
        "Function_57_5FF4",        # 39, 57
        "Function_58_601E",        # 3A, 58
        "Function_59_6048",        # 3B, 59
        "Function_60_6072",        # 3C, 60
        "Function_61_609C",        # 3D, 61
        "Function_62_60B6",        # 3E, 62
        "Function_63_60F5",        # 3F, 63
        "Function_64_6134",        # 40, 64
        "Function_65_6173",        # 41, 65
        "Function_66_61C2",        # 42, 66
        "Function_67_6287",        # 43, 67
        "Function_68_6312",        # 44, 68
        "Function_69_639D",        # 45, 69
        "Function_70_63F9",        # 46, 70
        "Function_71_6440",        # 47, 71
        "Function_72_6489",        # 48, 72
        "Function_73_64D6",        # 49, 73
        "Function_74_6519",        # 4A, 74
        "Function_75_6566",        # 4B, 75
        "Function_76_65A9",        # 4C, 76
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_843")

    #C0001
    ChrTalk(
        0xFE,
        (
            "クロスベル市への便が\x01",
            "ただいま到着いたしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "お戻りの方はこちらで\x01",
            "少々お待ちくださいませー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_882")

    label("loc_843")


    #C0003
    ChrTalk(
        0xFE,
        (
            "クロスベル市へお帰りの方は\x01",
            "こちらにお並びくださいませー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_882")

    TalkEnd(0xFE)
    Return()

    # Function_3_7C4 end

    def Function_4_886(): pass

    label("Function_4_886")

    TalkBegin(0xFE)

    #C0004
    ChrTalk(
        0xFE,
        (
            "せっかくセレブな彼女を\x01",
            "見つけようと思って来たんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ここの女は俺には荷が重い。\x01",
            "それだけを思い知らされたぜ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_886 end

    def Function_5_909(): pass

    label("Function_5_909")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xFE,
        "フン……ようやく着いたか。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "競売までそんなに時間がないな……\x01",
            "少し急ぐとするか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_909 end

    def Function_6_969(): pass

    label("Function_6_969")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        (
            "友達と一日中、\x01",
            "テーマパークで遊んでたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "気づいたら夜になってるんだから\x01",
            "ビックリしちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_969 end

    def Function_7_9DA(): pass

    label("Function_7_9DA")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "いけない、そろそろ出発ですって！\x01",
            "急ぎましょ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_9DA end

    def Function_8_A14(): pass

    label("Function_8_A14")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0011
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE3")
    OP_E0(0x2)
    MiniGame(0x6, 0x3, 0xFFFFA04C, 0xFFFFF060, 0xFFFF4912, 0x0, 0xFFFFA056, 0xFFFFE890, 0xFFFF6852)

    label("loc_AE3")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_8_A14 end

    def Function_9_AE8(): pass

    label("Function_9_AE8")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_FA1")
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_1608")

    label("loc_FA1")

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
        "#0007F#11Pしまった……！\x02",
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

    def lambda_10C4():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10C4)

    def lambda_10D9():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10D9)

    def lambda_10EE():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10EE)

    def lambda_1103():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1103)

    def lambda_1118():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1118)
    Sound(477, 0, 100, 0)
    Sound(479, 2, 100, 0)

    def lambda_1139():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1139)
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

    def lambda_11FB():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11FB)

    def lambda_1210():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1210)

    def lambda_1225():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1225)

    def lambda_123A():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_123A)

    def lambda_124F():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_124F)
    EndChrThread(0x18, 0x1)
    SetChrPos(0x18, -5000, -5500, -38200, 0)

    def lambda_1279():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1279)
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
        "キーア",
        "#5805F#5Pお船、行っちゃったね～。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        (
            "#0201F#11Pそんな……\x01",
            "まだ出航時刻では……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0103F#11P騒ぎを聞いて出航を\x01",
            "早めたのかもしれないわ……\x02\x03",

            "#0108F正しい判断といえば\x01",
            "そうかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x105,
        (
            "#0401F#11P僕たちにとっては\x01",
            "最悪の判断だったみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x10,
        "男の声",
        "#3Pいたぞ……！\x02",
    )

    CloseMessageWindow()

    #N0019
    NpcTalk(
        0x10,
        "男の声",
        "#3P追い詰めろ……！\x02",
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

    def lambda_1481():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1481)

    def lambda_148E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_148E)
    Sleep(100)

    def lambda_149E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_149E)

    def lambda_14AB():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14AB)
    Sleep(100)

    def lambda_14BB():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14BB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    #C0020
    ChrTalk(
        0x101,
        "#0013F#6Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        (
            "#0307F#5P逃げるだけ逃げるぞ！\x02\x03",

            "ボートかなんか波止場に\x01",
            "泊まってるかもしれねえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0007F#6Pああ……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22570, 3000)

    def lambda_1569():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1569)
    Sleep(100)

    def lambda_1586():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1586)
    Sleep(100)

    def lambda_15A3():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15A3)
    Sleep(100)

    def lambda_15C0():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15C0)
    Sleep(100)

    def lambda_15DD():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15DD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    label("loc_1608")

    EndChrThread(0x1A, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18D4")
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

    def lambda_16C9():
        OP_95(0xFE, 14020, -4000, -52980, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16C9)

    def lambda_16E3():
        OP_95(0xFE, 13510, -4000, -49680, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16E3)

    def lambda_16FD():
        OP_95(0xFE, 14570, -4000, -50590, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16FD)

    def lambda_1717():
        OP_95(0xFE, 15240, -4000, -52410, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1717)

    def lambda_1731():
        OP_95(0xFE, 12940, -4000, -51750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1731)
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
            "#0310F#11Pチッ……\x01",
            "何にもねえのかよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0008F#5Pくっ、このままじゃ……\x02",
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

    label("loc_18D4")

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

    label("loc_1990")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19A7")
    Sleep(1)
    Jump("loc_1990")

    label("loc_19A7")

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

    def lambda_1B64():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B64)

    def lambda_1B79():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B79)

    def lambda_1B8E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B8E)

    def lambda_1BA3():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BA3)

    def lambda_1BB8():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1BB8)
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

    def lambda_1C01():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1C01)

    def lambda_1C16():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1C16)

    def lambda_1C2B():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1C2B)

    def lambda_1C40():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C40)

    def lambda_1C55():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1C55)

    def lambda_1C6A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1C6A)

    def lambda_1C7F():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C7F)
    Sleep(50)

    def lambda_1C8F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C8F)
    Sleep(50)

    def lambda_1C9F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C9F)
    Sleep(50)

    def lambda_1CAF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CAF)
    Sleep(50)

    def lambda_1CBF():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1CBF)
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
        "キーア",
        "#5801F#5P囲まれちゃった……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#0010F#6P……ここまでか………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1854, 255, 100, 0)    #voice#Garcia
    Sleep(800)

    #N0027
    NpcTalk(
        0xD,
        "豪胆な声",
        (
            "#1Pやれやれ……\x01",
            "テメェらだったとはな。\x02",
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

    def lambda_1E5E():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1E5E)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)

    #C0028
    ChrTalk(
        0x101,
        "#0001F#6Pガルシア・ロッシ……\x02",
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
            "支援課のガキども……\x01",
            "ずいぶん久しぶりじゃねえか。\x02\x03",

            "クク、道理で見たことのある\x01",
            "ガキどもだと思ったわけだ。\x02\x03",

            "まさか招待カードを手に入れて\x01",
            "競売会に潜入するとはなァ。\x02",
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
            "#0004F#6P……別に警察の人間が\x01",
            "参加しちゃいけないという決まりは\x01",
            "無かったみたいですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xD,
        (
            "#3105F#11Pああ、別に構わないぜ？\x02\x03",

            "#3104F来る者は拒まず……\x01",
            "お得意様だったら大歓迎だ。\x02\x03",

            "#3101Fしかしまあ、正直侮ってたぜ。\x02\x03",

            "まさか《黒月#4Rヘイユエ#》と結託して\x01",
            "ここまでの騒ぎを起こすとはなァ。\x02",
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
        "キーア",
        "#5805F#5Pへいゆえ？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0011F#6Pな、なんでそうなる！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2216")

    #C0034
    ChrTalk(
        0x102,
        (
            "#0103F#6P……《銀#2Rイン#》と私たちは\x01",
            "何の関わりもありません。\x02\x03",

            "#0101F気絶した部下の方たちに\x01",
            "聞いてみたらどうですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2316")

    label("loc_2216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_22A3")

    #C0035
    ChrTalk(
        0x103,
        (
            "#0203F#6P《銀#2Rイン#》とわたしたちは\x01",
            "何の関わりもないですけど……\x02\x03",

            "#0211F気絶した手下の人たちに\x01",
            "聞いてみればいいいかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2316")

    label("loc_22A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2316")

    #C0036
    ChrTalk(
        0x104,
        (
            "#0306F#6P《銀#2Rイン#》と俺たちは\x01",
            "何の関わりもねぇんだがな。\x02\x03",

            "#0301F気絶した手下どもに聞いてみろや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2316")


    #C0037
    ChrTalk(
        0x105,
        (
            "#0406F#5Pむしろ侵入していた彼を\x01",
            "追い払ったようなもんだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xD,
        (
            "#3105F#11Pんー、そうなのか？\x02\x03",

            "#3104F……ま、そんなのは\x01",
            "今更どうでもいいんだよ。\x02\x03",

            "問題はテメェらが\x01",
            "俺たちの面子を潰したこと……\x02\x03",

            "#3100Fその落とし前だけはキッチリと\x01",
            "付けさせてもらわねえとなあ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0006F#6P……投降すると言っても\x01",
            "聞いてくれなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xD,
        (
            "#3104F#11Pクク、せっかくの狩りに\x01",
            "獲物の悲鳴を聞かないってのも\x01",
            "締まらねぇ話だろ……？\x02\x03",

            "#3100F安心しろ……\x01",
            "命までは取るつもりはねえ。\x02",
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
            "#3102F#11P腕の１本か２本で\x01",
            "勘弁してやるからよ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0110F#6Pっ……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#0201F#6P本気みたいです……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0301F#6Pったく……\x01",
            "トシを考えろよ、オッサン。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xD,
        (
            "#3104F#11Pクク……\x01",
            "せいぜい楽しませてくれよ？\x02\x03",

            "#3107F久々の狩りで血が滾#2Rたぎ#っている\x01",
            "この《キリングベア》をなァ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0013F#6Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        "#0407F#5P来る……！\x02",
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

    # Function_9_AE8 end

    def Function_10_26DB(): pass

    label("Function_10_26DB")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    label("loc_26E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26FE")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_26E3")

    label("loc_26FE")

    Return()

    # Function_10_26DB end

    def Function_11_26FF(): pass

    label("Function_11_26FF")

    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)

    label("loc_2712")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_272F")
    OP_A1(0xFE, 0x3E8, 0x4, 0x1, 0x2, 0x3, 0x4)
    Sleep(1000)
    Jump("loc_2712")

    label("loc_272F")

    Return()

    # Function_11_26FF end

    def Function_12_2730(): pass

    label("Function_12_2730")

    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2738")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2757")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_2738")

    label("loc_2757")

    Return()

    # Function_12_2730 end

    def Function_13_2758(): pass

    label("Function_13_2758")

    SetChrChipByIndex(0xFE, 0x3B)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2760")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277F")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_2760")

    label("loc_277F")

    Return()

    # Function_13_2758 end

    def Function_14_2780(): pass

    label("Function_14_2780")

    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2788")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27A7")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_2788")

    label("loc_27A7")

    Return()

    # Function_14_2780 end

    def Function_15_27A8(): pass

    label("Function_15_27A8")

    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)

    label("loc_27B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27CE")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(1000)
    Jump("loc_27B0")

    label("loc_27CE")

    Return()

    # Function_15_27A8 end

    def Function_16_27CF(): pass

    label("Function_16_27CF")

    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)

    label("loc_27D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2836")
    OP_A1(0xFE, 0x3E8, 0x1, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 80, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(1000)
    Jump("loc_27D7")

    label("loc_2836")

    Return()

    # Function_16_27CF end

    def Function_17_2837(): pass

    label("Function_17_2837")

    SetChrChipByIndex(0xFE, 0x3F)
    SetChrSubChip(0xFE, 0x0)

    label("loc_283F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29D8")
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
    Jump("loc_283F")

    label("loc_29D8")

    Return()

    # Function_17_2837 end

    def Function_18_29D9(): pass

    label("Function_18_29D9")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A07")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_29EC")

    label("loc_2A07")

    Return()

    # Function_18_29D9 end

    def Function_19_2A08(): pass

    label("Function_19_2A08")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A1B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A39")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_2A1B")

    label("loc_2A39")

    Return()

    # Function_19_2A08 end

    def Function_20_2A3A(): pass

    label("Function_20_2A3A")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, 13510, -3060, -32119, 90)

    def lambda_2A58():
        OP_95(0xFE, 13210, -4000, -38990, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A58)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 16)
    WaitChrThread(0xFE, 0)
    Return()

    # Function_20_2A3A end

    def Function_21_2A7C(): pass

    label("Function_21_2A7C")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, 14500, -2080, -30160, 90)

    def lambda_2A9A():
        OP_95(0xFE, 14810, -4000, -37790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A9A)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 17)
    WaitChrThread(0xFE, 0)
    Return()

    # Function_21_2A7C end

    def Function_22_2ABE(): pass

    label("Function_22_2ABE")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)

    def lambda_2ACD():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ACD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_2ABE end

    def Function_23_2AE7(): pass

    label("Function_23_2AE7")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2AF4():
        OP_95(0xFE, 12970, -4000, -48160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AF4)
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

    def lambda_2BD7():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BD7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_2AE7 end

    def Function_24_2BF1(): pass

    label("Function_24_2BF1")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2BFE():
        OP_95(0xFE, 14350, -4000, -48920, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2BFE)
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

    def lambda_2D08():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D08)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_2BF1 end

    def Function_25_2D22(): pass

    label("Function_25_2D22")

    OP_93(0xFE, 0x0, 0x12C)
    Sleep(600)

    def lambda_2D31():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D31)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_2D22 end

    def Function_26_2D4B(): pass

    label("Function_26_2D4B")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_2D57():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D57)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_2D4B end

    def Function_27_2D71(): pass

    label("Function_27_2D71")

    SetChrPos(0xFE, -5750, -4000, -50700, 270)

    def lambda_2D87():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D87)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_2D71 end

    def Function_28_2D9C(): pass

    label("Function_28_2D9C")

    SetChrPos(0xFE, -15280, -4000, -52250, 90)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2DB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E18")
    Sleep(850)
    OP_A1(0xFE, 0x3E8, 0x1, 0x2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x4)
    Jump("loc_2DB5")

    label("loc_2E18")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2E33():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E33)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_2D9C end

    def Function_29_2E4D(): pass

    label("Function_29_2E4D")

    SetChrPos(0xFE, -15780, -4000, -48270, 90)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2E66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_300A")
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
        (0, "loc_2F2C"),
        (1, "loc_2F72"),
        (2, "loc_2FB8"),
        (SWITCH_DEFAULT, "loc_2FFE"),
    )


    label("loc_2F2C")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -6250, -4000, -50610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FFE")

    label("loc_2F72")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -9950, -4000, -50630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FFE")

    label("loc_2FB8")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -3370, -4000, -51680, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FFE")

    label("loc_2FFE")

    SetChrSubChip(0xFE, 0x4)
    Sleep(1200)
    Jump("loc_2E66")

    label("loc_300A")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3025():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3025)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_2E4D end

    def Function_30_303F(): pass

    label("Function_30_303F")

    SetChrPos(0xFE, -11920, -4000, -51900, 90)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_305A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3135")
    SetChrChipByIndex(0xFE, 0x3B)
    SetChrSubChip(0xFE, 0x0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)

    def lambda_307E():
        OP_9B(0x1, 0xFE, 0x0, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_307E)
    Sound(532, 0, 80, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x2, 0x3, 0x4, 0x5)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0xFE, 0x140, 0, 750, 600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_30EE():
        OP_A6(0xFE, 0x0, 0x28, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30EE)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    Sound(814, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFD170, 0xFFFFF060, 0xFFFF3544, 0x1F4, 0xFA0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_305A")

    label("loc_3135")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)

    def lambda_315A():
        OP_97(0xFE, 0xFFFFE0C0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_315A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_30_303F end

    def Function_31_3174(): pass

    label("Function_31_3174")

    SetChrPos(0xFE, -9920, -4000, -51900, 270)

    label("loc_3185")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_320C")
    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)
    Sleep(400)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0xFFFFDD28, 0xFFFFF060, 0xFFFF3544, 0x1F4, 0x1770)
    SetChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)

    def lambda_31D1():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31D1)
    OP_A1(0xFE, 0x5DC, 0x4, 0x2, 0x4, 0x1, 0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3207")
    Sleep(1)
    Jump("loc_31F5")

    label("loc_3207")

    Jump("loc_3185")

    label("loc_320C")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_3174 end

    def Function_32_3215(): pass

    label("Function_32_3215")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -11560, -4000, -49320, 90)

    label("loc_3235")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32BC")
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x3)

    def lambda_3251():
        OP_9D(0xFE, 0xFFFFD6C0, 0xFFFFF060, 0xFFFF3F58, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3251)
    WaitChrThread(0xFE, 1)
    Sound(534, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x14, 0x13)
    Sleep(250)
    OP_A1(0xFE, 0x5DC, 0x2, 0xE, 0x3)
    Sleep(100)

    def lambda_328E():
        OP_9D(0xFE, 0xFFFFD2D8, 0xFFFFF060, 0xFFFF3F58, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_328E)
    WaitChrThread(0xFE, 1)
    Sleep(400)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3235")

    label("loc_32BC")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)

    def lambda_32E6():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32E6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_32_3215 end

    def Function_33_3300(): pass

    label("Function_33_3300")

    SetChrPos(0xFE, -8560, -4000, -49320, 270)

    label("loc_3311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3394")
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x4)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3334():
        OP_9B(0x1, 0xFE, 0xB4, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3334)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x4)
    Sleep(400)

    def lambda_3354():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3354)
    OP_A1(0xFE, 0x9C4, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    WaitChrThread(0xFE, 1)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_337D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338F")
    Sleep(1)
    Jump("loc_337D")

    label("loc_338F")

    Jump("loc_3311")

    label("loc_3394")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_3300 end

    def Function_34_33A8(): pass

    label("Function_34_33A8")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -1840, -4000, -50740, 270)
    BeginChrThread(0xFE, 0, 0, 16)
    Return()

    # Function_34_33A8 end

    def Function_35_33C8(): pass

    label("Function_35_33C8")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -4610, -4000, -49060, 270)
    BeginChrThread(0xFE, 0, 0, 17)
    Return()

    # Function_35_33C8 end

    def Function_36_33E8(): pass

    label("Function_36_33E8")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -5870, -4000, -51790, 270)
    BeginChrThread(0xFE, 0, 0, 17)
    Return()

    # Function_36_33E8 end

    def Function_37_340B(): pass

    label("Function_37_340B")

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

    # Function_37_340B end

    def Function_38_344E(): pass

    label("Function_38_344E")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_487D")
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
        "#0010F#6Pはあはあ……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x105,
        "#0406F#6P手こずらせてくれたね……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x11,
        "#11P#40W……わ、若頭……！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xE,
        "#11P#40W……だ、大丈夫ですか！？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xD,
        (
            "#3104F#11P#40Wククク……ハハハハ……\x02\x03",

            "#3100F……味見だけのつもりだったが\x01",
            "楽しませてくれるじゃねえか。\x02",
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

    def lambda_3B16():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3B16)

    def lambda_3B2F():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3B2F)
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

    def lambda_3B7E():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3B7E)

    def lambda_3B97():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3B97)

    def lambda_3BB0():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3BB0)
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
            "#5805F#5Pわっ……\x01",
            "生き返っちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#0007F#6Pば、馬鹿な……！？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#0401F#6P#Nあのヴァルドよりも\x01",
            "遥かにタフみたいだね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0056
    ChrTalk(
        0x104,
        "#0301F#6Pチッ……化物が。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        (
            "#3104F#11Pクク、何を抜かしてやがる。\x02\x03",

            "#3102F──ランドルフ・オルランド。\x01",
            "テメェだって同じだろうが？\x02",
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
        "#0310F#6Pッ……！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#0005F#5Pランディ……？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xD,
        (
            "#3102F#11Pクク、やっぱりそうだったか。\x02\x03",

            "#3104F大陸西部最強の猟兵団の一つ、\x01",
            "《赤い星座》……\x02\x03",

            "その団長の息子にして、\x01",
            "ガキの頃から大部隊を率いて\x01",
            "敵を殺しまくった赤き死神……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0061
    ChrTalk(
        0xD,
        (
            "#3107F#11P#4S──《闘神の息子》\x01",
            "ランドルフ・オルランド……！\x02",
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
        "#0011F#6P《闘神の息子》……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#0208F#6P#N《赤い星座》……\x01",
            "有名な猟兵団ですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0065
    ChrTalk(
        0x102,
        "#0106F#6P……そうだったの………\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0304F#5P──ハハ。\x01",
            "バレちまったら仕方ねぇか。\x02\x03",

            "#0312Fま、そのオッサンの話は\x01",
            "だいたい間違っちゃいねぇぜ。\x02\x03",

            "《闘神の息子》って呼び名は\x01",
            "ヘドが出るほど気に喰わねぇがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xD,
        (
            "#3102F#11Pクク、どうやら訳アリで\x01",
            "クロスベルに流れてきたらしいな。\x02\x03",

            "#3104F俺の古巣《西風の旅団》と\x01",
            "《赤い星座》は昔からの宿敵……\x02\x03",

            "丁度いい、ここらで因縁の対決と\x01",
            "行ってみようじゃねえか……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0068
    ChrTalk(
        0xD,
        "#3107F#11P今度はタイマン勝負でなァ！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        "#0311F#6P……ぬかせ……\x02",
    )

    CloseMessageWindow()
    OP_68(-23150, -3000, -49620, 1500)
    MoveCamera(44, 18, 0, 1500)
    SetChrChipByIndex(0x104, 0x31)
    SetChrSubChip(0x104, 0x0)

    def lambda_4115():
        OP_95(0xFE, -25200, -4000, -50000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4115)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0x104, 0x5A, 0x190)
    OP_6F(0x79)

    #C0070
    ChrTalk(
        0x101,
        "#0007F#6Pおい、ランディ……！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0303F#5P……ここは任せろ。\x02\x03",

            "#0301Fこのオッサンを倒せたら\x01",
            "何とか突破口が開けるはずだ。\x02\x03",

            "#0307F俺のことはいい……\x01",
            "とにかくこの場を切り抜けろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#0010F#6Pそんな……！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#0107F#6P#Nだ、駄目よ……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0074
    ChrTalk(
        0x103,
        "#0201F#6P#Nら、らしくないです……！\x02",
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
            "#3104F#11P《戦場の叫び#10Rウ ォ ー ク ラ イ#》……\x02\x03",

            "爆発的な闘気を引き出す\x01",
            "猟兵ならではの戦闘技術……\x02\x03",

            "#3102Fクク、そう来なくっちゃなァ！\x02",
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
        "#11Pひっ……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xE,
        "#11Pさ、下がれ……\x02",
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
        "#0410F#6Pくっ……凄いね……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x133,
        "#5801F#6P#Nびりびりする～……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0080
    ChrTalk(
        0x101,
        "#0010F#6Pくっ、このままじゃ──\x02",
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

    def lambda_47D7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_47D7)
    Sleep(50)

    def lambda_47E7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_47E7)
    Sleep(50)

    def lambda_47F7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_47F7)
    Sleep(50)

    def lambda_4807():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4807)
    Sleep(50)

    def lambda_4817():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4817)
    Sleep(50)

    def lambda_4827():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4827)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0xD, 1)

    #C0081
    ChrTalk(
        0x101,
        "#0005F#6Pな……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        "#0202F#6Pこの遠吠えは……！\x02",
    )

    CloseMessageWindow()

    label("loc_487D")

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

    def lambda_48F3():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_48F3)

    def lambda_490C():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_490C)
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
        "#11Pなっ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x14, 500)

    #C0084
    ChrTalk(
        0xE,
        (
            "#5Pこ、こら……！\x01",
            "怯えてんじゃねえ……！\x02",
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
        "#1201Fガルルウウウッ！\x02",
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
        "#3110F#6Pチッ、犬コロが……！\x02",
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
        "#0002F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        "#0102F#6Pあれは……！\x02",
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

    def lambda_4C1E():

        label("loc_4C1E")

        TurnDirection(0x101, 0x16, 500)
        Yield()
        Jump("loc_4C1E")

    QueueWorkItem2(0x101, 1, lambda_4C1E)

    def lambda_4C30():

        label("loc_4C30")

        TurnDirection(0x102, 0x16, 500)
        Yield()
        Jump("loc_4C30")

    QueueWorkItem2(0x102, 1, lambda_4C30)

    def lambda_4C42():

        label("loc_4C42")

        TurnDirection(0x103, 0x16, 500)
        Yield()
        Jump("loc_4C42")

    QueueWorkItem2(0x103, 1, lambda_4C42)

    def lambda_4C54():

        label("loc_4C54")

        TurnDirection(0x104, 0x16, 500)
        Yield()
        Jump("loc_4C54")

    QueueWorkItem2(0x104, 1, lambda_4C54)

    def lambda_4C66():

        label("loc_4C66")

        TurnDirection(0x105, 0x16, 500)
        Yield()
        Jump("loc_4C66")

    QueueWorkItem2(0x105, 1, lambda_4C66)

    def lambda_4C78():

        label("loc_4C78")

        TurnDirection(0x133, 0x16, 500)
        Yield()
        Jump("loc_4C78")

    QueueWorkItem2(0x133, 1, lambda_4C78)

    def lambda_4C8A():

        label("loc_4C8A")

        TurnDirection(0xD, 0x16, 500)
        Yield()
        Jump("loc_4C8A")

    QueueWorkItem2(0xD, 1, lambda_4C8A)
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

    def lambda_4D80():
        OP_9E(0xFE, 0xFFFF9A70, 0xFFFF30F8, 0x15F90, 0x2328, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4D80)
    Sleep(1750)

    def lambda_4D9E():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4D9E)
    Sleep(300)
    EndChrThread(0x19, 0x1)

    def lambda_4DBF():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4DBF)
    Sleep(350)
    EndChrThread(0x19, 0x1)

    def lambda_4DE0():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4DE0)
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
            "#1001F#5P……グズグズすんな。\x01",
            "とっとと乗りやがれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#0000F#11P課長……！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x133,
        "#5810F#11Pわぁ、ぼーとだぁ！\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#0202F#11Pナイスタイミングです……！\x02",
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
        "#3107F#4S#11P行かせるかあああッ！\x02",
    )

    CloseMessageWindow()

    def lambda_4F57():
        OP_93(0xFE, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F57)
    Sleep(50)

    def lambda_4F67():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F67)
    Sleep(50)

    def lambda_4F77():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F77)
    Sleep(50)

    def lambda_4F87():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F87)
    Sleep(50)

    def lambda_4F97():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F97)
    Sleep(50)

    def lambda_4FA7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_4FA7)
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
        "#3110F#11Pくっ、テメエ……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#0311F#6P悪いな、オッサン……\x01",
            "今回は付き合えなさそうだ。\x02\x03",

            "#0303Fそれより……\x01",
            "アンタら知ってたのか……？\x02\x03",

            "#0301F“人間の子供”を競売会に\x01",
            "出品しようとしてたのを……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0xD,
        "#3105F#11Pなにィ……！？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#0003F#6P……この子は、出品物の部屋にあった\x01",
            "革張りのトランクに閉じ込められていた。\x02\x03",

            "#0001Fそれが何を意味するのか\x01",
            "あんたには判っているのか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0098
    ChrTalk(
        0x133,
        "#5805F#2Pふえ～？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0099
    ChrTalk(
        0xD,
        (
            "#3107F#11Pな、何をフカシこいてやがる！\x02\x03",

            "あのトランクには\x01",
            "ローゼンベルクの人形が……！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x105,
        (
            "#0406F#6P#Nまあ、でも事実だからねぇ。\x02\x03",

            "#0402F事と次第によっては\x01",
            "タダじゃ済まないんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0101
    ChrTalk(
        0x16,
        (
            "#1003F#2Pやれやれ……\x01",
            "妙な事になってるみたいだな。\x02\x03",

            "#1001F──ルバーチェの。\x01",
            "改めて話は付けさせてもらう。\x02\x03",

            "そっちはそっちで\x01",
            "状況を整理しておくんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xD,
        "#3110F#11Pグッ……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x16,
        (
            "#1007F#2P特務支援課、撤収！\x01",
            "とっとと全員乗りやがれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#0007F#5Pはいっ！\x02",
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

    def lambda_54B9():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_54B9)

    def lambda_54CE():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_54CE)
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
        "#11Pああっ……！\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x11,
        (
            "#11Pくっ……\x01",
            "他にボートはないのか！？\x02",
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
        "#3110F#11P#50Wぐうううう～～～～ッ……\x02",
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
        "#3107F#4S#11P#14A#70Wうおおおおおおおおおおッ！！\x02",
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

    # Function_38_344E end

    def Function_39_564A(): pass

    label("Function_39_564A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5663")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_39_564A")

    label("loc_5663")

    Return()

    # Function_39_564A end

    def Function_40_5664(): pass

    label("Function_40_5664")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5688")
    OP_82(0x0, 0x28, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_40_5664")

    label("loc_5688")

    Return()

    # Function_40_5664 end

    def Function_41_5689(): pass

    label("Function_41_5689")

    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_569C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56BD")
    Sound(925, 0, 80, 0)
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_569C")

    label("loc_56BD")

    Return()

    # Function_41_5689 end

    def Function_42_56BE(): pass

    label("Function_42_56BE")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56EF")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_56D1")

    label("loc_56EF")

    Return()

    # Function_42_56BE end

    def Function_43_56F0(): pass

    label("Function_43_56F0")

    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_56FB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56FB)
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

    # Function_43_56F0 end

    def Function_44_576A(): pass

    label("Function_44_576A")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_578E():
        OP_9D(0xFE, 0xFFFFC0A5, 0xFFFFF060, 0xFFFF4372, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_578E)
    Sleep(300)

    #C0109
    ChrTalk(
        0x10,
        "#6Pぎゃっ！\x05\x02",
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

    def lambda_57F2():
        OP_9D(0xFE, 0xFFFFB35C, 0xFFFFF060, 0xFFFF3814, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57F2)
    Sleep(300)

    #C0110
    ChrTalk(
        0xE,
        "#5Pうわああっ！？\x05\x02",
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

    def lambda_5865():
        OP_9D(0xFE, 0xFFFFC75C, 0xFFFFF060, 0xFFFF3CB0, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5865)
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

    # Function_44_576A end

    def Function_45_58B6(): pass

    label("Function_45_58B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58CD")
    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("Function_45_58B6")

    label("loc_58CD")

    Return()

    # Function_45_58B6 end

    def Function_46_58CE(): pass

    label("Function_46_58CE")

    SetChrFlags(0xFE, 0x4)

    def lambda_58D8():
        OP_95(0xFE, -30390, -4000, -50000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_58D8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_5908():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5908)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_592F():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_592F)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_46_58CE end

    def Function_47_595D(): pass

    label("Function_47_595D")

    SetChrFlags(0xFE, 0x4)

    def lambda_5967():
        OP_95(0xFE, -30390, -4000, -48700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5967)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)

    def lambda_598A():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_598A)
    WaitChrThread(0xFE, 1)

    def lambda_59AB():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59AB)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_47_595D end

    def Function_48_59D9(): pass

    label("Function_48_59D9")

    SetChrFlags(0xFE, 0x4)

    def lambda_59E3():
        OP_95(0xFE, -30390, -4000, -51000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_59E3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_5A13():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF379C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A13)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_5A3A():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF379C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A3A)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_48_59D9 end

    def Function_49_5A68(): pass

    label("Function_49_5A68")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_5A7A():
        OP_95(0xFE, -29700, -4000, -50000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A7A)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_5AA3():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AA3)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_5ACA():
        OP_9D(0xFE, 0xFFFF7388, 0xFFFFEE08, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5ACA)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_49_5A68 end

    def Function_50_5AF8(): pass

    label("Function_50_5AF8")

    SetChrFlags(0xFE, 0x4)

    def lambda_5B02():
        OP_95(0xFE, -30300, -4000, -50250, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B02)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)

    def lambda_5B25():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3DDC, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B25)
    WaitChrThread(0xFE, 1)

    def lambda_5B46():
        OP_9D(0xFE, 0xFFFF7388, 0xFFFFEE08, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B46)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_50_5AF8 end

    def Function_51_5B74(): pass

    label("Function_51_5B74")

    Sleep(1500)
    EndChrThread(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_5B8B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B8B)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_5BD5():
        OP_9D(0xFE, 0xFFFFAC36, 0xFFFFF060, 0xFFFF44EE, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BD5)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_5C19():
        OP_95(0xFE, -25520, -4000, -48010, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C19)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_5C68():
        OP_9D(0xFE, 0xFFFF92D2, 0xFFFFF380, 0xFFFF4B1A, 0x5DC, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C68)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_5CB6():
        OP_9D(0xFE, 0xFFFF8454, 0xFFFFF380, 0xFFFF4B6A, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5CB6)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_5CFD():
        OP_9D(0xFE, 0xFFFF7554, 0xFFFFEE08, 0xFFFF5AC4, 0x7D0, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5CFD)
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

    # Function_51_5B74 end

    def Function_52_5D55(): pass

    label("Function_52_5D55")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D82")

    def lambda_5D65():
        OP_A6(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D65)
    WaitChrThread(0xFE, 2)
    Jump("Function_52_5D55")

    label("loc_5D82")

    Return()

    # Function_52_5D55 end

    def Function_53_5D83(): pass

    label("Function_53_5D83")

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

    def lambda_5DD6():
        OP_9B(0x0, 0xFE, 0x0, 0x546, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5DD6)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    BeginChrThread(0xFE, 1, 0, 52)

    label("loc_5E03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E15")
    Sleep(1)
    Jump("loc_5E03")

    label("loc_5E15")

    Sleep(400)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Sound(804, 0, 100, 0)

    def lambda_5E33():
        OP_9D(0xFE, 0xFFFFAC04, 0xFFFFF060, 0xFFFF3CB0, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E33)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sleep(1350)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_5E73():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E73)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_53_5D83 end

    def Function_54_5E90(): pass

    label("Function_54_5E90")

    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)

    def lambda_5EA8():
        OP_9B(0x0, 0xFE, 0x0, 0x47E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5EA8)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x42)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0xFE, 1, 0, 52)
    OP_82(0x1F4, 0x0, 0x1770, 0x12C)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1000, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(830, 0, 100, 0)
    Sound(834, 0, 100, 0)

    label("loc_5F1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F30")
    Sleep(1)
    Jump("loc_5F1E")

    label("loc_5F30")

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

    # Function_54_5E90 end

    def Function_55_5FA0(): pass

    label("Function_55_5FA0")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5FAD():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FAD)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_55_5FA0 end

    def Function_56_5FCA(): pass

    label("Function_56_5FCA")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_5FD7():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5FD7)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_5FCA end

    def Function_57_5FF4(): pass

    label("Function_57_5FF4")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6001():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6001)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_57_5FF4 end

    def Function_58_601E(): pass

    label("Function_58_601E")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_602B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_602B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_58_601E end

    def Function_59_6048(): pass

    label("Function_59_6048")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6055():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6055)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_59_6048 end

    def Function_60_6072(): pass

    label("Function_60_6072")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)

    def lambda_607F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_607F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_60_6072 end

    def Function_61_609C(): pass

    label("Function_61_609C")


    def lambda_60A1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60A1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_61_609C end

    def Function_62_60B6(): pass

    label("Function_62_60B6")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_60D5():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60D5)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    OP_64(0xFE)
    Return()

    # Function_62_60B6 end

    def Function_63_60F5(): pass

    label("Function_63_60F5")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6114():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6114)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    OP_64(0xFE)
    Return()

    # Function_63_60F5 end

    def Function_64_6134(): pass

    label("Function_64_6134")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6153():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6153)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_64(0xFE)
    Return()

    # Function_64_6134 end

    def Function_65_6173(): pass

    label("Function_65_6173")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)

    def lambda_619C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_619C)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    OP_64(0xFE)
    Return()

    # Function_65_6173 end

    def Function_66_61C2(): pass

    label("Function_66_61C2")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -17000, -3000, -48000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_6222():
        OP_9D(0xFE, 0xFFFFB1E0, 0xFFFFE0C0, 0xFFFF63C0, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6222)
    Sleep(1000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -19500, -5000, -42000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(927, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_66_61C2 end

    def Function_67_6287(): pass

    label("Function_67_6287")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -18750, -3000, -50500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_62E7():
        OP_9D(0xFE, 0xFFFFB636, 0xFFFFF060, 0xFFFF383C, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_62E7)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_67_6287 end

    def Function_68_6312(): pass

    label("Function_68_6312")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -20750, -3000, -51500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_6372():
        OP_9D(0xFE, 0xFFFFADF8, 0xFFFFF060, 0xFFFF33F0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6372)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_68_6312 end

    def Function_69_639D(): pass

    label("Function_69_639D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63F8")
    PlayEffect(0x4, 0xFF, 0xFE, 0x100, 0, 0, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x14, 0x3E8, 0xA6)
    Sleep(166)
    Jump("Function_69_639D")

    label("loc_63F8")

    Return()

    # Function_69_639D end

    def Function_70_63F9(): pass

    label("Function_70_63F9")

    BeginChrThread(0x19, 2, 0, 69)

    def lambda_6404():
        OP_98(0xFE, 0x0, 0x0, 0x3A98, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6404)
    Sleep(1200)

    def lambda_6421():
        OP_9E(0xFE, 0xFFFF0880, 0xFFFF7860, 0xFFFEA070, 0x2EE0, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6421)
    WaitChrThread(0x19, 1)
    EndChrThread(0x19, 0x2)
    Return()

    # Function_70_63F9 end

    def Function_71_6440(): pass

    label("Function_71_6440")

    SetChrPos(0xFE, 35000, -5500, -63000, 270)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 35000, -5500, -63000)
    OP_9F(0x1, -17000, -5500, -63000)
    OP_9F(0x1, -28000, -5500, -63000)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_71_6440 end

    def Function_72_6489(): pass

    label("Function_72_6489")

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

    # Function_72_6489 end

    def Function_73_64D6(): pass

    label("Function_73_64D6")

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

    # Function_73_64D6 end

    def Function_74_6519(): pass

    label("Function_74_6519")

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

    # Function_74_6519 end

    def Function_75_6566(): pass

    label("Function_75_6566")

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

    # Function_75_6566 end

    def Function_76_65A9(): pass

    label("Function_76_65A9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《クロスベル市》行き水上バス・時刻表\x01\x01",
            "   ※またのお越しを\x01",
            "　       お待ちしております！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_76_65A9 end

    SaveToFile()

Try(main)
