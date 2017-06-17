from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0220.bin",                # FileName
        "c0220",                    # MapName
        "c0220",                    # Location
        0x000D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 13, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0220",                  # 0
        "イアン弁護士",           # 1
        "ピート",                 # 2
        "サラリーマン",           # 3
        "エマ捜査官",             # 4
        "警官",                   # 5
        "捜査官",                 # 6
        "捜査官",                 # 7
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch05902.itc",                   # 01
        "chr/ch22200.itc",                   # 02
        "chr/ch27802.itc",                   # 03
        "chr/ch30500.itc",                   # 04
        "chr/ch30000.itc",                   # 05
        "chr/ch27600.itc",                   # 06
        "chr/ch27800.itc",                   # 07
    ))

    DeclNpc(4510,    1169,    15779,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(12869,   1000,    4809,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(2259,    140,     5500,    90,   453,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(5289,    1019,    16959,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1370,    29,      1990,    180,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-8510,   0,       45979,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-569,    29,      39380,   90,   389,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(14350,   1000,    -70,     2000,    14350,   2500,    -70,     0x007C, 0,  20, 0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_4F7",          # 02, 2
        "Function_3_599",          # 03, 3
        "Function_4_20D3",         # 04, 4
        "Function_5_359D",         # 05, 5
        "Function_6_36D9",         # 06, 6
        "Function_7_387E",         # 07, 7
        "Function_8_392C",         # 08, 8
        "Function_9_3AB7",         # 09, 9
        "Function_10_3C09",        # 0A, 10
        "Function_11_49CD",        # 0B, 11
        "Function_12_4C92",        # 0C, 12
        "Function_13_5315",        # 0D, 13
        "Function_14_7186",        # 0E, 14
        "Function_15_71D1",        # 0F, 15
        "Function_16_721C",        # 10, 16
        "Function_17_7267",        # 11, 17
        "Function_18_72B2",        # 12, 18
        "Function_19_72FD",        # 13, 19
        "Function_20_7348",        # 14, 20
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D8")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 5510, 1020, 16030, 225)
    Jump("loc_4C9")

    label("loc_2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_4C9")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30F")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_349")
    SetChrPos(0x8, 3150, 1020, 12920, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4C9")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_368")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_387")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_4C9")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_408")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DA")
    SetChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_3FE")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3FE")

    SetChrFlags(0x8, 0x80)

    label("loc_403")

    Jump("loc_4C9")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4C9")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4C9")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_452")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x10)
    Jump("loc_4C9")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_471")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_490")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4AF")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C9")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_4C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F6")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_4F6")

    Return()

    # Function_1_2A0 end

    def Function_2_4F7(): pass

    label("Function_2_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_540")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_57F")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_598")
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x0, 0x10)

    label("loc_598")

    Return()

    # Function_2_4F7 end

    def Function_3_599(): pass

    label("Function_3_599")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B3")
    Call(0, 12)
    Jump("loc_20CF")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_944")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#02200F君たちか……\x01",
            "ディーター氏の演説は見たかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        "#00001Fええ、ですが……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "#02200F事態の急激な変化に\x01",
            "戸惑いを感じている……\x01",
            "と言ったところかな？\x02\x03",

            "#02203F市民の大半もそんな気持ちを\x01",
            "抱えていることだろう。\x02\x03",

            "#02201Fだが、２大国の『暗闘』が\x01",
            "実際にあったことも事実なのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#00108F……おじさまが言っていた、\x01",
            "不可解な『事故』のことですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "#02203Fうむ……\x02\x03",

            "#02201Fだが、私たちはそういった事実に\x01",
            "気づかないフリをしながら、\x01",
            "目の前の幸せを享受してきた……\x02\x03",

            "これは、ディーター君の言うように\x01",
            "我々クロスベルに住む者全ての\x01",
            "罪なのだろう。\x02\x03",

            "#02203F国家としての独立は、\x01",
            "それらと向き合うためにも\x01",
            "必要な事だと私は思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#00005Fイアン先生……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "#02203F……すまない、\x01",
            "あの演説にあてられてか、\x01",
            "つい熱が入ってしまったようだ。\x02\x03",

            "#02200Fどちらにせよ……\x01",
            "すでに賽#2Rさい#は投げられてしまった。\x02\x03",

            "#02203Fこれからどうするか……\x01",
            "それは住民の一人一人が\x01",
            "考えていくべき問題だろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 1)
    Jump("loc_9CA")

    label("loc_944")


    #C0008
    ChrTalk(
        0xFE,
        (
            "#02203Fすでに賽#2Rさい#は投げられてしまった。\x02\x03",

            "#02200Fこれからどうするか……\x01",
            "それは住民の一人一人が\x01",
            "考えていくべき問題だろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CA")

    Jump("loc_20CF")

    label("loc_9CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E98")

    #C0009
    ChrTalk(
        0xFE,
        (
            "#02203Fふう……\x01",
            "あのお客さんの会社の\x01",
            "資料はと……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00000Fイアン先生……\x01",
            "お忙しそうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0011
    ChrTalk(
        0xFE,
        (
            "#02205Fああ、君たちか……\x02\x03",

            "#02203F例の襲撃事件で多くの企業が\x01",
            "損害を被ったようでね。\x02\x03",

            "#02200Fここ一週間ほど、\x01",
            "彼らの相談を受けていて\x01",
            "休む間もなかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#00303F……大変そうッスね。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "#02203Fうむ……\x01",
            "だが仕方のないことだ。\x02\x03",

            "#02200FＩＢＣが破壊された事で、\x01",
            "取引き先や職場そのものを\x01",
            "失った者も多いからね。\x02\x03",

            "私も弁護士として、\x01",
            "できる限りのことは\x01",
            "してあげなければ……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、さすがは\x01",
            "熊ヒゲ先生といったところだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00105Fで、でも……\x01",
            "憲法草案の作成も\x01",
            "抱えてらっしゃいましたよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "#02200Fああ、それに関しては\x01",
            "なんとか完成に至ってね、\x01",
            "自治州政府に提出したばかりだよ。\x02\x03",

            "#02202Fいや、人間やればできるものだね。\x01",
            "おかげで最近は寝る間もなかったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        "#00200F不眠不休というわけですか……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x109,
        (
            "#10100Fえっと、あまり無理は\x01",
            "なさらないで下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "#02202Fふふ、お心遣い痛み入るよ。\x02\x03",

            "#02203F今日の分の相談で\x01",
            "ある程度予定に区切りはつくから、\x01",
            "今夜はしっかり休むつもりだ。\x02\x03",

            "#02200F……それでは、お客さんを\x01",
            "待たせているから失礼するよ。\x02\x03",

            "君たちも沢山の要請が\x01",
            "来ているだろうが、\x01",
            "がんばってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_F1B")

    label("loc_E98")


    #C0021
    ChrTalk(
        0xFE,
        (
            "#02200F私は市民のために\x01",
            "弁護士という立場で\x01",
            "尽力するつもりだ。\x02\x03",

            "君たちも沢山の要請が\x01",
            "来ているだろうが、\x01",
            "がんばってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1B")

    Jump("loc_20CF")

    label("loc_F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1035")

    #C0022
    ChrTalk(
        0xFE,
        (
            "#02200F住民投票を控える\x01",
            "このタイミングで起きた\x01",
            "マインツの占拠……\x02\x03",

            "独立提唱を撤回させるために\x01",
            "帝国、あるいは共和国が仕組んだ、\x01",
            "などと考える市民もいるようだ。\x02\x03",

            "#02203F……まさか、\x01",
            "ここまでの事態を引き起こすとは、\x01",
            "私も予想だにしていなかったがね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10EF")

    label("loc_1035")


    #C0023
    ChrTalk(
        0xFE,
        (
            "#02200F今回の事件は、帝国や共和国が\x01",
            "独立提唱を撤回させるために\x01",
            "仕組んだのだと考えられている。\x02\x03",

            "#02203F……まさか、\x01",
            "ここまでの事態を引き起こすとは、\x01",
            "私も予想だにしていなかったがね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EF")

    Jump("loc_20CF")

    label("loc_10F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_16E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F6")

    #C0024
    ChrTalk(
        0xFE,
        "#02200Fああ、君たち……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12B4")

    #C0025
    ChrTalk(
        0x101,
        (
            "#00004Fイアン先生……\x01",
            "昨日はどうもありがとう\x01",
            "ございました。\x02\x03",

            "#00000F先生が見つけてくれた証拠、\x01",
            "役に立ちましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "#02203Fああ、ピート君から顛末は聞いたよ。\x01",
            "ミンネスという男、なんとか\x01",
            "指名手配にはこぎつけたそうだね。\x02\x03",

            "#02202Fはは、とはいっても私はあくまで\x01",
            "手伝いをしたにすぎないが。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00004Fいえ、本当に助かりました。\x02\x03",

            "#00000F憲法草案のほうにも\x01",
            "忙しくされているのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1307")

    label("loc_12B4")


    #C0028
    ChrTalk(
        0x101,
        (
            "#00000Fイアン先生……\x01",
            "お久しぶりです。\x02\x03",

            "憲法草案の作成、\x01",
            "忙しいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1307")


    #C0029
    ChrTalk(
        0xFE,
        (
            "#02200Fああ、それでも少しは\x01",
            "まとまってきたところでね。\x02\x03",

            "コーヒーでも淹れて休憩しようと\x01",
            "思っていたところなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#00105Fあ……\x01",
            "休憩時間を邪魔して\x01",
            "しまったでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "#02202Fいや、そんなことはないさ。\x01",
            "君たちとおしゃべりするのも\x01",
            "いい気分転換になるだろうしね。\x02\x03",

            "#02205F……ところで、君たち。\x01",
            "昨日の脱線事故の調査に\x01",
            "あたったようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00000Fええ、ひとまず原因は\x01",
            "解明できました。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#00203F詳しい説明は省きますが……\x01",
            "人為的に引き起こされた\x01",
            "事故と見て間違いありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "#02205Fふむ、そうだったのか……\x02\x03",

            "#02203F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00305Fイアン先生……\x01",
            "どうしたんッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "#02203F……いや、死者などが出なくて\x01",
            "本当によかったと思ってね。\x02\x03",

            "#02200Fとにかく、最近は何かと物騒だ。\x01",
            "君たちも充分に気をつけたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 0)
    Jump("loc_16E3")

    label("loc_15F6")


    #C0037
    ChrTalk(
        0xFE,
        (
            "#02200F憲法草案も少しはまとまってきたが……\x01",
            "まだまだ改良の余地はありそうでね。\x02\x03",

            "#02203F体力的に厳しいところもあるが、\x01",
            "クロスベルの未来のためにも\x01",
            "弱音を吐くわけにもいくまい。\x02\x03",

            "#02200F必ずや、この上ない憲法草案を\x01",
            "作りあげてみせるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E3")

    Jump("loc_20CF")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1784")

    #C0038
    ChrTalk(
        0x8,
        (
            "#02200F今回の事件……\x01",
            "時間の許す限りは\x01",
            "手伝わせてもらうよ。\x02\x03",

            "#02202Fふふ、あとで顔を出すから\x01",
            "君たちも捜査のほうを\x01",
            "がんばってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CF")

    label("loc_1784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1820")

    #C0039
    ChrTalk(
        0x8,
        (
            "#02200F今回の事件……\x01",
            "時間の許す限りは\x01",
            "手伝わせてもらうよ。\x02\x03",

            "#02202Fふふ、あとで顔を出すから\x01",
            "君たちも捜査のほうを\x01",
            "がんばってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CF")

    label("loc_1820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_182E")
    Jump("loc_20CF")

    label("loc_182E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_183C")
    Jump("loc_20CF")

    label("loc_183C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E9")

    #C0040
    ChrTalk(
        0xFE,
        (
            "#02205Fおや、君たち。\x01",
            "こんな夜に来るとは珍しいね。\x02\x03",

            "#02200Fダドリー君も一緒とは……\x01",
            "明日の会議本番に関わるような\x01",
            "問題でも発生したかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x10A,
        (
            "#00603F今から、それを確かめに\x01",
            "行くところです。\x02\x03",

            "#00600F万全を期すためには、\x01",
            "不確定な要素は潰しておくに\x01",
            "越した事はありませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "#02203Fうむ、用心しすぎるという\x01",
            "ことはないだろうな。\x02\x03",

            "#02200F詳しい事情は知らないが……\x01",
            "是非ともがんばってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A57")

    label("loc_19E9")


    #C0043
    ChrTalk(
        0xFE,
        (
            "#02200Fさて……\x01",
            "準備はこのあたりで充分だな。\x02\x03",

            "#02203Fひとまず明日に備えて、\x01",
            "今日は早めに休むとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A57")

    Jump("loc_20CF")

    label("loc_1A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B47")

    #C0044
    ChrTalk(
        0xFE,
        (
            "#02200F首脳たちがクロスベルを\x01",
            "訪れたようだね。\x02\x03",

            "#02203F通商会議初日にして\x01",
            "街の警戒が更に高まったのを\x01",
            "感じているよ。\x02\x03",

            "#02200Fトラブルというものは\x01",
            "こういう時に起きるもの……\x01",
            "君たちも気をつけてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BEF")

    label("loc_1B47")


    #C0045
    ChrTalk(
        0xFE,
        (
            "#02203F首脳たちが訪れた今、\x01",
            "クロスベル市内の警戒は\x01",
            "さらに増したことだろう。\x02\x03",

            "#02200Fトラブルというものは\x01",
            "こういう時に起きるもの……\x01",
            "君たちも気をつけてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEF")

    Jump("loc_20CF")

    label("loc_1BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CEE")

    #C0046
    ChrTalk(
        0xFE,
        (
            "#02200F通商会議がいよいよ明日、\x01",
            "開催されるね。\x02\x03",

            "除幕式には、各国の首脳たちが\x01",
            "やってくる予定だが……\x02\x03",

            "万が一、彼らの身に何かあれば\x01",
            "国際問題に発展してしまうだろう。\x02\x03",

            "君たち警察には、より一層\x01",
            "がんばってもらわなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D60")

    label("loc_1CEE")


    #C0047
    ChrTalk(
        0xFE,
        (
            "#02200F何か心配事があるなら\x01",
            "いつでも相談してくれたまえ。\x02\x03",

            "私でよければ\x01",
            "いくらでも力にならせて\x01",
            "もらうからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D60")

    Jump("loc_20CF")

    label("loc_1D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED8")

    #C0048
    ChrTalk(
        0xFE,
        (
            "#02203F《黒月》がルバーチェ跡の買収を\x01",
            "着々と進めているようだね。\x02\x03",

            "#02201Fあの場所が黒月のものになるなど、\x01",
            "あまり考えたくない話だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00008Fそうですね……\x01",
            "厄介なことになりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "#02203F……とはいえ、手立てもない。\x01",
            "おそらく現実の話に\x01",
            "なってしまうだろうな……\x02\x03",

            "#02200Fやれやれ……\x01",
            "クロスベルの抱える問題は\x01",
            "まだまだ山積みだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F5D")

    label("loc_1ED8")


    #C0051
    ChrTalk(
        0xFE,
        (
            "#02200Fルバーチェ跡を黒月が\x01",
            "手に入れてしまうのは\x01",
            "時間の問題だろう。\x02\x03",

            "やれやれ……\x01",
            "クロスベルの抱える問題は\x01",
            "まだまだ山積みだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5D")

    Jump("loc_20CF")

    label("loc_1F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205F")

    #C0052
    ChrTalk(
        0xFE,
        (
            "#02203F特務支援課には\x01",
            "市民たちから大きな期待が\x01",
            "かかっているはずだ。\x02\x03",

            "#02202F前以上に頼られる事も\x01",
            "多くなるだろうが、是非とも\x01",
            "がんばってくれたまえ。\x02\x03",

            "その一つ一つの積み重ねが、\x01",
            "きっとクロスベルの希望に\x01",
            "なるのだろうからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20CF")

    label("loc_205F")


    #C0053
    ChrTalk(
        0xFE,
        (
            "#02200F特務支援課の働きには、\x01",
            "私も期待しているよ。\x02\x03",

            "#02202F是非とも、市民の期待に\x01",
            "応えてやってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CF")

    TalkEnd(0xFE)
    Return()

    # Function_3_599 end

    def Function_4_20D3(): pass

    label("Function_4_20D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F5")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_20F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21FE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話す\x01",                      # 0
            "イアンの書置きを読む\x01",      # 1
            "やめる\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2173")
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21F9")

    label("loc_2173")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2187")
    Jump("loc_21F9")

    label("loc_2187")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0054
    ChrTalk(
        0xFE,
        "皆さん……ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "どうか……\x01",
            "イアン先生をよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F9")

    Jump("loc_20FF")

    label("loc_21FE")

    Jump("loc_3599")

    label("loc_2203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2211")
    Jump("loc_3599")

    label("loc_2211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_22A9")

    #C0056
    ChrTalk(
        0xFE,
        (
            "クロスベルの独立のため、\x01",
            "憲法草案を作成したのは\x01",
            "イアン先生です。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "独立の立役者の一人として、\x01",
            "色々と思う所が\x01",
            "あるんでしょうね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_22A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233F")

    #C0058
    ChrTalk(
        0xFE,
        (
            "イアン先生、とても\x01",
            "忙しそうにしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "僕が一人前だったら、\x01",
            "イアン先生の代わりに\x01",
            "相談を受けられたんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23B9")

    label("loc_233F")


    #C0060
    ChrTalk(
        0xFE,
        (
            "……とにかく今は、\x01",
            "イアン先生を全力でお手伝いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "休んでもらうためにも、\x01",
            "早く仕事を片付けていただかないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B9")

    Jump("loc_3599")

    label("loc_23BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_24F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247A")

    #C0062
    ChrTalk(
        0xFE,
        (
            "マインツが武装集団に\x01",
            "占拠されるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "住民たちには何の罪もないのに、\x01",
            "ひどい話ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "僕たち市民にはどうすることも\x01",
            "できないんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24F2")

    label("loc_247A")


    #C0065
    ChrTalk(
        0xFE,
        (
            "イアン先生も今回の事件には\x01",
            "胸を痛めておられるようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "僕たち市民にはどうすることも\x01",
            "できないんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F2")

    Jump("loc_3599")

    label("loc_24F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D7")

    #C0067
    ChrTalk(
        0xFE,
        (
            "昨日のアルモリカでの事件は\x01",
            "僕がまとめておかないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "先生に任せていたら、\x01",
            "また書類の山の奥に大事な資料が\x01",
            "埋もれてしまいますからね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2656")

    #C0069
    ChrTalk(
        0x101,
        (
            "#00000Fはは……でも、\x01",
            "本当に解決できてよかった。\x02\x03",

            "色々と手伝ってくれて\x01",
            "ありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "いいえ、とんでもないです。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "支援課の皆さんこそ、\x01",
            "本当にお疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27CF")

    label("loc_2656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_26F4")

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F（アルモリカの事件……\x01",
            "  例のミンネスって男に\x01",
            "  関係する件のことかな？）\x02\x03",

            "（……やっぱり、ちゃんと\x01",
            "  最後までやるべきだったな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27CF")

    label("loc_26F4")


    #C0073
    ChrTalk(
        0x101,
        (
            "#00005Fアルモリカの事件……\x01",
            "何かあったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "ええ、実は悪徳商人が……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "……あっ、すみません。\x01",
            "僕としたことが……\x01",
            "守秘義務があったんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00000Fそ、そうか……\x01",
            "でもまあ、解決したなら\x01",
            "よかったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CF")

    SetScenarioFlags(0x16C, 2)
    Jump("loc_281B")

    label("loc_27D7")


    #C0077
    ChrTalk(
        0xFE,
        (
            "なにはともあれ……\x01",
            "アルモリカ村が救われて\x01",
            "本当によかったです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281B")

    Jump("loc_3599")

    label("loc_2820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283B")
    SetScenarioFlags(0x0, 1)
    Jump("loc_283B")

    label("loc_283B")

    Jump("loc_3599")

    label("loc_2840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2929")

    #C0078
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の事件について、\x01",
            "過去の似たケースを洗い出してるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "思わぬところから解決の糸口が\x01",
            "見つかったりしますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "イアン先生なら、ハロルドさんの\x01",
            "お宅に行っていますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29AD")

    label("loc_2929")


    #C0081
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の事件について、\x01",
            "過去の似たケースを洗い出してるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "イアン先生なら、ハロルドさんの\x01",
            "お宅に行っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AD")

    Jump("loc_2B9D")

    label("loc_29B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_END)), "loc_2B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A88")

    #C0083
    ChrTalk(
        0xFE,
        (
            "イアン先生も憲法草案の作成に\x01",
            "大変忙しい身の上なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "だからといって、こうした事件を\x01",
            "見過ごすわけにはいけませんよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "僕も、出来る限り\x01",
            "お手伝いさせていただきますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B06")

    label("loc_2A88")


    #C0086
    ChrTalk(
        0xFE,
        (
            "忙しいからといって、こうした事件を\x01",
            "見過ごすわけにはいけませんよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "僕も、出来る限り\x01",
            "お手伝いさせていただきますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B06")

    Jump("loc_2B9D")

    label("loc_2B0B")


    #C0088
    ChrTalk(
        0xFE,
        (
            "イアン先生なら、２階にこもって\x01",
            "憲法草案の作成に勤しんでいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "今日も随分と忙しくされていますし、\x01",
            "僕もしっかり支えないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9D")

    Jump("loc_3599")

    label("loc_2BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3023")

    #C0090
    ChrTalk(
        0xFE,
        "あ、皆さんは特務支援課の……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "イアン先生なら、\x01",
            "今はお仕事で２階に\x01",
            "こもっておられますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#00104Fなんだか最近、相当お忙しく\x01",
            "されてらっしゃるみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00005Fそうなのか？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "ええ、実は……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "例の国家独立に関する\x01",
            "憲法草案の作成を市長に\x01",
            "頼まれたそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CF2")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2CF2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D18")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2D18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D3E")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2D3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D64")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2D64")

    Sleep(1000)

    #C0096
    ChrTalk(
        0x101,
        "#00007Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x109,
        (
            "#10101F《憲法》……\x01",
            "自治州法ではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00104F《憲法》というのは\x01",
            "国家存立の基本条件を定めた\x01",
            "根本的な法律になるの。\x02\x03",

            "#00100F国の統治権や仕組み、\x01",
            "大原則を定めた最高法規で\x01",
            "他国の干渉を許さないものよ。\x02\x03",

            "国家としての体裁を持つためには\x01",
            "絶対欠かせないものになるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00305Fは～……\x01",
            "また難しげなシロモンだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#00204Fしかしイアン先生ならば\x01",
            "まさに適任ではないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、周辺諸国でも活躍する\x01",
            "熊ヒゲ先生なら、\x01",
            "うまくやってくれるだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "ええ、きっと素晴らしい憲法草案を\x01",
            "作ってくれるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "イアン先生によろしく\x01",
            "言っておいてもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "ええ、ありがとうございます。\x01",
            "先生も励みになると思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 1)
    Jump("loc_30A9")

    label("loc_3023")


    #C0105
    ChrTalk(
        0xFE,
        (
            "イアン先生は、\x01",
            "憲法草案の作成を\x01",
            "市長に頼まれたそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "きっとイアン先生なら\x01",
            "素晴らしい憲法草案を\x01",
            "作ってくれるはずですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A9")

    Jump("loc_3599")

    label("loc_30AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3128")

    #C0107
    ChrTalk(
        0xFE,
        (
            "イアン先生なら、\x01",
            "今日はお仕事に出られました。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "なにか伝言があれば、\x01",
            "後で僕がお伝えしておきますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_3128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_31B2")

    #C0109
    ChrTalk(
        0xFE,
        (
            "あれ、このファイル……\x01",
            "収納する場所が間違ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "まったくイアン先生ったら、\x01",
            "こういうところはズボラなんだから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3296")

    #C0111
    ChrTalk(
        0xFE,
        (
            "あれ、さっきのお客様の相談料……\x01",
            "随分少ないような。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "……イアン先生ったら、\x01",
            "また勝手に料金を\x01",
            "まけちゃったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "法律家なんですから、\x01",
            "こういうところはしっかりして\x01",
            "いただかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32FE")

    label("loc_3296")


    #C0114
    ChrTalk(
        0xFE,
        (
            "……イアン先生ったら、\x01",
            "また勝手に料金を\x01",
            "まけちゃったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "まったくもう、ぶつぶつ……\x02",
    )

    CloseMessageWindow()

    label("loc_32FE")

    Jump("loc_3599")

    label("loc_3303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C3")

    #C0116
    ChrTalk(
        0xFE,
        (
            "最近は、イアン先生も\x01",
            "特に忙しくしてらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "通商会議が近づいた関係で\x01",
            "さらに相談が増えているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "僕も可能な限り、\x01",
            "先生をサポートしないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3431")

    label("loc_33C3")


    #C0119
    ChrTalk(
        0xFE,
        (
            "通商会議が近づいた関係で、\x01",
            "最近は相談が増えているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "僕も可能な限り、\x01",
            "先生をサポートしないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3431")

    Jump("loc_3599")

    label("loc_3436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34BD")

    #C0121
    ChrTalk(
        0xFE,
        (
            "最近はなんだか\x01",
            "相談に来るお客さんが\x01",
            "増えてきているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "先生も働きづめですし、\x01",
            "どこかで休んで頂かないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3599")

    label("loc_34BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3556")

    #C0123
    ChrTalk(
        0xFE,
        (
            "あっ、特務支援課の皆さん……\x01",
            "お久しぶりですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "イアン先生ならデスクにいますよ。\x01",
            "何かご用でしたら、そちらへどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3599")

    label("loc_3556")


    #C0125
    ChrTalk(
        0xFE,
        (
            "イアン先生ならデスクです。\x01",
            "何かご用でしたら、そちらへどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3599")

    TalkEnd(0xFE)
    Return()

    # Function_4_20D3 end

    def Function_5_359D(): pass

    label("Function_5_359D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365A")

    #C0126
    ChrTalk(
        0xFE,
        (
            "私の勤務する会社は\x01",
            "破壊されたＩＢＣに\x01",
            "入っていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "職場が無くなってしまって、\x01",
            "完全に業務停止状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "はあ……これから\x01",
            "どうすればいいだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36D5")

    label("loc_365A")


    #C0129
    ChrTalk(
        0xFE,
        (
            "ＩＢＣに入っていた\x01",
            "職場が無くなってしまって、\x01",
            "完全に業務停止状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "はあ……これから\x01",
            "どうすればいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D5")

    TalkEnd(0xFE)
    Return()

    # Function_5_359D end

    def Function_6_36D9(): pass

    label("Function_6_36D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F2")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3804")

    #C0131
    ChrTalk(
        0xFE,
        (
            "彼の考案した《計画》……\x01",
            "かなり前から練られていたと見て\x01",
            "間違いなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "引き続き、私たち捜査一課は\x01",
            "グリムウッド法律事務所の\x01",
            "家宅捜索を続けます。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "……皆さんもお気をつけて。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37FC")

    #C0134
    ChrTalk(
        0x10A,
        (
            "#00600Fうむ……\x01",
            "ここは頼んだぞ、エマ君。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FC")

    SetScenarioFlags(0x0, 3)
    Jump("loc_387A")

    label("loc_3804")


    #C0135
    ChrTalk(
        0xFE,
        (
            "引き続き、私たち捜査一課は\x01",
            "イアン・グリムウッド法律事務所の\x01",
            "家宅捜索を続けます。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "……皆さんもお気をつけて。\x02",
    )

    CloseMessageWindow()

    label("loc_387A")

    TalkEnd(0xFE)
    Return()

    # Function_6_36D9 end

    def Function_7_387E(): pass

    label("Function_7_387E")

    TalkBegin(0xFE)

    #C0137
    ChrTalk(
        0xFE,
        (
            "現在、捜査一課によって\x01",
            "グリムウッド法律事務所の\x01",
            "家宅捜索が進められています。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "２階に続く扉の鍵も開錠に成功したとか。\x01",
            "……何か手がかりが見つかればいいですね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_387E end

    def Function_8_392C(): pass

    label("Function_8_392C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1E")

    #C0139
    ChrTalk(
        0xFE,
        (
            "どれも、中世の錬金術や\x01",
            "ゼムリア文明について扱った\x01",
            "資料のようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "相当に古い資料だが……\x01",
            "これほど集めるのには\x01",
            "かなりの年月を要するはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "一体イアン容疑者は、いつから\x01",
            "《計画》とやらを企んでいたんだ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3AB3")

    label("loc_3A1E")


    #C0142
    ChrTalk(
        0xFE,
        (
            "相当に古い資料だが……\x01",
            "これほど集めるのには\x01",
            "かなりの年月を要するはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "一体イアン容疑者は、いつから\x01",
            "《計画》とやらを企んでいたんだ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB3")

    TalkEnd(0xFE)
    Return()

    # Function_8_392C end

    def Function_9_3AB7(): pass

    label("Function_9_3AB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B87")

    #C0144
    ChrTalk(
        0xFE,
        (
            "端末からは、ＩＢＣやオルキスタワーと\x01",
            "頻繁に交信した形跡が見つかっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "おそらく、この場所から黒幕として\x01",
            "大統領……いや、クロイス容疑者たちに\x01",
            "指示を行っていたのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3C05")

    label("loc_3B87")


    #C0146
    ChrTalk(
        0xFE,
        (
            "おそらく、この場所から黒幕として\x01",
            "クロイス容疑者たちに\x01",
            "指示を行っていたのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "慎重に捜査をすすめなければ……\x02",
    )

    CloseMessageWindow()

    label("loc_3C05")

    TalkEnd(0xFE)
    Return()

    # Function_9_3AB7 end

    def Function_10_3C09(): pass

    label("Function_10_3C09")

    EventBegin(0x0)
    Fade(500)
    OP_68(6060, 2320, 15510, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18770, 0)
    SetChrPos(0x101, 7120, 1020, 15230, 270)
    SetChrPos(0x102, 7010, 1020, 16640, 270)
    SetChrPos(0x103, 7000, 1020, 13880, 315)
    SetChrPos(0x104, 8300, 1000, 14190, 270)
    SetChrPos(0xF4, 8600, 1000, 15690, 270)
    SetChrPos(0xF5, 8400, 1000, 17000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0xB, 0x5A, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_0D()

    #C0148
    ChrTalk(
        0x9,
        "#11Pひっく、うう……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        "#11Pイアン先生……どうして……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#11P#00005Fピート君……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x1F4)

    #C0151
    ChrTalk(
        0x9,
        "#6Pみ、皆さん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DCC")

    #C0152
    ChrTalk(
        0xB,
        (
            "#5Pダドリーさん……\x01",
            "それに特務支援課も、\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x10A,
        "#11P#00603F……ああ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DF4")

    label("loc_3DCC")


    #C0154
    ChrTalk(
        0xB,
        (
            "#5P特務支援課の……\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF4")


    #C0155
    ChrTalk(
        0x101,
        (
            "#11P#00001Fエマ捜査官も、お疲れ様です。\x01",
            "……イアン先生の家宅捜索ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "#5Pええ……重要参考人として、\x01",
            "捜査一課で調べを進めていた所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "#5P酷とは思いましたが……\x01",
            "グリムウッド氏の関係者として\x01",
            "彼にも立ち会ってもらっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        (
            "#6Pグスッ……\x01",
            "いえ、僕の方からお願いしたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "#6Pイアン先生……いなくなる前に、\x01",
            "気になることを言っていましたから\x01",
            "どうしても確かめたくって。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_END)), "loc_402B")

    #C0160
    ChrTalk(
        0x104,
        (
            "#11P#00308Fああ……机の掃除を\x01",
            "頼まれていたとかいうアレか。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#11P#00106F確かに、あのタイミングで\x01",
            "何で急にそんなことを言ったのか\x01",
            "気になっていたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_426D")

    label("loc_402B")


    #C0162
    ChrTalk(
        0x102,
        "#11P#00105F気になること……？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        "#6P……はい。\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        (
            "#6Pあの《魔導兵》がうろついていた\x01",
            "非常事態が落ち着いたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        (
            "#6P事務所に戻って先生の机を\x01",
            "掃除しておいてくれって。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#11P#00005F掃除……？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "#6Pええ、最初は急いで出て行くからと\x01",
            "思ってたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "#6P普段、掃除は僕任せの先生も\x01",
            "机だけは出来るだけ触らないように\x01",
            "普段から言っていたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "#6P仕事上、助手の僕にも\x01",
            "見せられないものも多いからって\x01",
            "そのままにしてたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#11P#00108Fイアン先生が……\x01",
            "確かに気になるわね……\x02\x03",

            "#00106Fそんなタイミングで\x01",
            "掃除を頼むというのも、\x01",
            "よく分からないし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426D")


    #C0171
    ChrTalk(
        0x9,
        (
            "#6Pその答えがさっき……\x01",
            "イアン先生の机から出てきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        "#6P……これです。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ピートは開封された封筒を差し出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_42FA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_42FA)
    Sleep(50)

    def lambda_430A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_430A)
    Sleep(50)

    def lambda_431A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_431A)
    Sleep(50)

    def lambda_432A():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_432A)
    Sleep(50)

    def lambda_433A():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_433A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4409")

    #C0174
    ChrTalk(
        0x105,
        "#11P#10401Fこれは……置き手紙かい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_447E")

    label("loc_4409")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4443")

    #C0175
    ChrTalk(
        0x109,
        "#11P#10101Fこれは……置き手紙？\x02",
    )

    CloseMessageWindow()
    Jump("loc_447E")

    label("loc_4443")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_447E")

    #C0176
    ChrTalk(
        0x106,
        "#11P#10701Fこれは……置き手紙ですか？\x02",
    )

    CloseMessageWindow()

    label("loc_447E")


    #C0177
    ChrTalk(
        0x101,
        "#11P#00001F……読んでもいいかい？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x9,
        "#6P………………（こくん）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    Call(0, 11)

    #C0179
    ChrTalk(
        0x101,
        "#11P#00006F……イアン先生……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4547")

    #C0180
    ChrTalk(
        0x101,
        "#11P#00008F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_45C6")

    label("loc_4547")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4589")

    #C0181
    ChrTalk(
        0x109,
        "#11P#10108F……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_45C6")

    label("loc_4589")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45C6")

    #C0182
    ChrTalk(
        0x105,
        "#11P#10408F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_45C6")


    #C0183
    ChrTalk(
        0xB,
        (
            "#5P……彼の机には、\x01",
            "他にもいくつもの書類が\x01",
            "保管されていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xB,
        (
            "#5P現在、事務所に相談をしている\x01",
            "依頼者への今後の対応が記された\x01",
            "膨大なメモ……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xB,
        (
            "#5Pそして、ピート少年の\x01",
            "後見人を手配するための、\x01",
            "親権関係の手続き書類などです。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "#6P……ううっ、イアン先生……\x01",
            "どうしてこんな……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_46EE():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_46EE)
    Sleep(50)

    def lambda_46FE():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_46FE)
    Sleep(50)

    def lambda_470E():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_470E)
    Sleep(50)

    def lambda_471E():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_471E)
    Sleep(50)

    def lambda_472E():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_472E)
    Sleep(50)

    def lambda_473E():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_473E)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)

    #C0187
    ChrTalk(
        0x9,
        (
            "#6Pお世話になった先生の事を忘れて、\x01",
            "幸せになんてなれるわけ\x01",
            "ないじゃないですかっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        "#11P#00106Fピート君……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        "#11P#00208F……イアン先生は大馬鹿です。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#11P#00306Fああ、俺も人のことは言えねえが……\x01",
            "残された方はこんな手紙なんかじゃ\x01",
            "絶対に納得できねえだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#11P#00003F……その通りだ。\x02\x03",

            "#00008Fピート君、俺たちはこれから\x01",
            "イアン先生のところに向かうつもりだ。\x02\x03",

            "#00001F俺たちはそこで、必ず真実を掴んで……\x01",
            "先生たちを連れ戻してみせるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "#6Pみ、皆さん……\x01",
            "……ぐすっ、ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "#6Pどうか……\x01",
            "イアン先生をよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    SetScenarioFlags(0x1BD, 6)
    EventEnd(0x5)
    Return()

    # Function_10_3C09 end

    def Function_11_49CD(): pass

    label("Function_11_49CD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(18, 0, 40, 0)
    SetChrName("")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ピート君へ。\x01",
            "まずは、こんな手紙を残して君の元を\x01",
            "突然去ってしまった事を謝らせてほしい。\x02\x01",

            "かつて後見人として君を引き取り、\x01",
            "事務所で働いてもらうようになってから\x01",
            "私は輝くような毎日を過ごさせてもらった。\x02\x01",

            "運命のあの日から、嘆きと哀しみに支配され、\x01",
            "計画を達成するためだけにあるはずだった\x01",
            "私の人生を……本当に感謝してもし足りない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 40, 0)

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "君のこともあるから、\x01",
            "しばらくの間、私も悩んでいたが……\x02\x01",

            "やはり計画を中止することはできない。\x01",
            "私に後戻りすることは許されないのだ。\x02\x01",

            "ピート君、どうか……\x01",
            "私のことは忘れて幸せに過ごしてほしい。\x02\x01",

            "聡明な君が立派な大人になってくれるのを\x01",
            "遠い場所から女神に祈っている。\x02\x01",

            "　　　　　　　──イアン・グリムウッド\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_49CD end

    def Function_12_4C92(): pass

    label("Function_12_4C92")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_68(4790, 1920, 14330, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20480, 0)
    SetChrPos(0x101, 4830, 1020, 12570, 0)
    SetChrPos(0x102, 3990, 1020, 12720, 0)
    SetChrPos(0x109, 5650, 1000, 11990, 0)
    SetChrPos(0x105, 2910, 1000, 11990, 0)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0196
    ChrTalk(
        0x8,
        "#5P#02205Fおお、君たちは……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#00000Fお久しぶりです、イアン先生。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#5P#02200Fはは、久しぶりだね。\x01",
            "一旦、活動を休止したと\x01",
            "聞いていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#00000Fええ、業務を再開しました。\x01",
            "またよろしくおねがいします。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x8,
        (
            "#5P#02200Fふふ、なるほど。\x01",
            "新メンバーも入って、\x01",
            "心機一転と言ったところかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x105,
        (
            "#12P#10300F確か、有名な\x01",
            "『熊ヒゲ先生』だったかな？\x02\x03",

            "#10304Fフフ、これからよろしくたのむよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(150)

    #C0202
    ChrTalk(
        0x8,
        (
            "#5P#02205Fおお、これはご丁寧にどうも。\x02\x03",

            "#02203F……ええと、\x01",
            "名刺はどこにやったか……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F74")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4F74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F9A")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4F9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FC0")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4FC0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FE6")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4FE6")

    Sleep(1000)
    TurnDirection(0x109, 0x105, 500)
    Sleep(500)

    #C0203
    ChrTalk(
        0x109,
        (
            "#10106Fワ、ワジ君……\x01",
            "目上の人に対する\x01",
            "礼儀ってものがあるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        (
            "#12P#00100Fもう、イアン先生も\x01",
            "ノリが良すぎです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    #C0205
    ChrTalk(
        0x8,
        (
            "#5P#02202Fはは、いやいや……\x01",
            "人と人との付き合いにおいて、\x01",
            "自己紹介はとても大切だよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0206
    AnonymousTalk(
        0x8,
        (
            "──コホン、それでは\x01",
            "改めて名乗らせていただこうか。\x02\x03",

            "私の名前はイアン・グリムウッド。\x01",
            "この法律事務所の所長を\x01",
            "させてもらっている弁護士だ。\x02\x03",

            "特務支援課の諸君、\x01",
            "改めてよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0207
    ChrTalk(
        0x109,
        (
            "#10100Fこちらこそ、\x01",
            "よろしくお願いします！\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#00000Fまた色々と相談に来る事も\x01",
            "あるかもしれません。\x02\x03",

            "#00004Fその時はぜひ、俺たちに\x01",
            "力を貸してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "#5P#02200Fああ、いつでも\x01",
            "来てくれたまえ。\x02\x03",

            "私でよければいくらでも\x01",
            "相談に乗らせてもらうからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x12C, 4)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_4C92 end

    def Function_13_5315(): pass

    label("Function_13_5315")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 6600, 140, 5500, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    OP_68(-940, 1300, -180, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, -2710, 0, -490, 90)
    SetChrPos(0x102, -2710, 0, -490, 90)
    SetChrPos(0x103, -2710, 0, -490, 90)
    SetChrPos(0x104, -2710, 0, -490, 90)
    SetChrPos(0x109, -2710, 0, -490, 90)
    SetChrPos(0x105, -2710, 0, -490, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(700)
    OP_68(2570, 1300, 1440, 5000)
    MoveCamera(65, 23, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20900, 5000)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 19)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)

    #C0210
    ChrTalk(
        0x8,
        "#02205Fおや……？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        "#00000Fイアン先生！\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        (
            "#00204Fよかった……\x01",
            "事務所にいてくれましたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "#02200Fああ、今はちょうど\x01",
            "休憩している所なのだが……\x02\x03",

            "#02201F……ふむ、なにか私に\x01",
            "相談事でもあるのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#00100F分かりますか……\x01",
            "さすが先生ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        (
            "#02203Fふふ、依頼がある人の顔は\x01",
            "それこそ何百何千と\x01",
            "見てきているからね。\x02\x03",

            "#02200Fどれ、そっちに腰かけなさい。\x01",
            "私も忙しい身の上だが、\x01",
            "話を聞こうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        "#00004Fすみません……助かります。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは、前日に調べた\x01",
            "ミンネスのプロフィールと行動……\x02\x03",

            "そして、本日判明した\x01",
            "土地の権利書を集めていたという事実を\x01",
            "イアンに伝えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x8, 0x0)
    OP_68(5320, 500, 6810, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21670, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 2310, 200, 5400, 90)
    SetChrPos(0x102, 2310, 200, 4570, 90)
    SetChrPos(0x103, 2260, 200, 6070, 90)
    SetChrPos(0x104, 4530, 200, 7520, 180)
    SetChrPos(0x109, 3780, 200, 7520, 180)
    SetChrPos(0x105, 5160, 200, 7520, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0218
    ChrTalk(
        0x8,
        (
            "#02200Fふむ……なるほどね。\x01",
            "大方の事情は分かったよ。\x02\x03",

            "本来なら私がこの件を\x01",
            "引き受けたいところなのだが……\x02\x03",

            "#02203F君たちも知っての通り、\x01",
            "今の私は憲法草案の作成という\x01",
            "重要な仕事があってね。\x02\x03",

            "#02203F申し訳ないが、私が引き受けて\x01",
            "調査をする時間は作れそうにない。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x103,
        "#00203F残念ですが……仕方ないかと。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x102,
        (
            "#00102Fこうして相談に\x01",
            "乗っていただけただけでも\x01",
            "助かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x8,
        (
            "#02203Fすまないな……\x01",
            "代わりに今、出来る限りの\x01",
            "アドバイスをさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#00004Fありがとうございます。\x02\x03",

            "#00001Fそれで……どうでしょうか？\x02\x03",

            "これまでのミンネス氏の行動……\x01",
            "そこから、何らかの犯罪の兆候を\x01",
            "読み取ることはできるでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0223
    ChrTalk(
        0x8,
        "#02203F一つだけ、思い当たるフシがある。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0224
    ChrTalk(
        0x104,
        "#00309Fヒュウ、マジっすか！？\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "#02200Fああ……帝国の知り合いから\x01",
            "参考資料としてもらったケースに\x01",
            "よく似たものがあるんだ。\x02\x03",

            "とはいえ、全く同様の事件だと\x01",
            "断定する事はできないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#00003F……今はとにかく、\x01",
            "捜査の取っ掛かりが\x01",
            "ほしい状況なんです。\x02\x03",

            "#00003Fその思い当たるフシについて、\x01",
            "お話していただけないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#02200F……うむ、いいだろう。\x01",
            "他でもない君たちの頼みだ。\x02\x03",

            "#02203Fこほん、では……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0228
    ChrTalk(
        0x8,
        (
            "#02203F──数年前……\x01",
            "エレボニア帝国のある男爵家に、\x01",
            "１人の男が訪れた。\x02\x03",

            "#02201F男の名は『リドナー』……\x01",
            "ある有名な酒造会社に勤める\x01",
            "凄腕のビジネスマンを名乗る男だ。\x02\x03",

            "そしてリドナーは、\x01",
            "男爵にある儲け話を持ちかけた。\x02\x03",

            "代々、男爵家の領地に\x01",
            "受け継がれてきた広大な麦畑……\x01",
            "それを利用した酒造会社の起業だ。\x02\x03",

            "#02203Fビール工場を領内に建造し、\x01",
            "その経営を男爵家に任せる……\x01",
            "概ねそういった内容だったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#00005F……！　この話って……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x105,
        (
            "#10300Fフフ……\x01",
            "どこかで聞いた話に\x01",
            "よく似ているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "#02203F──男爵はその儲け話に快諾し、\x01",
            "リドナーが持ってきた\x01",
            "契約書にサインをした。\x02\x03",

            "#02200Fそして、管理の名目で麦畑全域が、\x01",
            "そして工場建造の名目で一部の土地が\x01",
            "リドナーに一時、譲渡された。\x02\x03",

            "また、会社の資本金として\x01",
            "男爵家の資産の一部が回され、\x01",
            "起業の準備は着々と整っていった……\x02\x03",

            "#02203Fだが……リドナーは、\x01",
            "土地の権利書と資産の一部、\x01",
            "それらを持ったまま姿をくらました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0232
    ChrTalk(
        0x104,
        "#00305Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "#02203F突然リドナーとの連絡が途絶え、\x01",
            "男爵家の者たちは焦ったらしいが……\x02\x03",

            "そのとき重大な事態が\x01",
            "進行している事に気づいていなかった。\x02\x03",

            "#02201Fあろうことか、リドナーは\x01",
            "預かり受けた土地の権利書を\x01",
            "第三者に売り渡してしまっていたのだ。\x02\x03",

            "高級別荘地に最適な土地としてな。\x02\x03",

            "#02203F──結局、男爵家には\x01",
            "莫大な借金だけが残ってしまい……\x01",
            "程なく領地全てを手放す羽目になる。\x02\x03",

            "領地を失ったことで爵位も剥奪され……\x01",
            "以後、彼らは行方知れずとなってしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#00306Fなんっつう……\x01",
            "とんでもねえ話だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x109,
        (
            "#10101F勝手に他人の土地を売り払うなんて……\x02\x03",

            "いくらなんでもひどすぎます！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "#02203F──これが、君たちの話を聞いて\x01",
            "真っ先に思い浮かんだ事件だ。\x02\x03",

            "身分を偽って信用を勝ち取り、\x01",
            "最終的に莫大な財産を騙し取る……\x02\x03",

            "#02201Fいわゆる『詐欺』の\x01",
            "手口の一つといえるだろうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0237
    ChrTalk(
        0x102,
        "#00105F詐欺……！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        (
            "#00203Fつまり、あのミンネスという人は\x01",
            "クインシー社の役員などではなく……\x02\x03",

            "#00200Fただの詐欺師である可能性があると？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x8,
        (
            "#02203Fうむ……断定はできないが\x01",
            "可能性は高いと言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00003F実際、共通する部分は\x01",
            "いくつも確認できた……\x02\x03",

            "#00001Fひとまずこの件を\x01",
            "詐欺事件として捜査するのが\x01",
            "いいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        (
            "#10103Fだとすると……\x01",
            "おのずと、調査すべき部分が\x01",
            "見えてきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そうだな。\x01",
            "ミンネスという男には大きく分けて２つ、\x01",
            "疑わしい部分がある。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    #C0243
    ChrTalk(
        0x101,
        (
            "#00001Fまずは、その計画……\x01",
            "『アルモリカ・ハニーカンパニー』が\x01",
            "本当に存在するのかどうか、という点だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x105,
        (
            "#10303Fそれに関しては、\x01",
            "ミラの動きが分かれば\x01",
            "つかめるかもしれないね。\x02\x03",

            "#10300Fクロスベルで起業する以上、\x01",
            "ＩＢＣで融資を受ける必要性が\x01",
            "あるはずだ。\x02\x03",

            "もし、計画にウソがあるなら\x01",
            "ＩＢＣに証拠が残っている\x01",
            "可能性は高いんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#00003Fそれともう一つ、当然確認したいのが\x01",
            "ミンネスが本当に『クインシー社』の\x01",
            "役員なのかどうかだ。\x02\x03",

            "#00001F……これに関しては外国の会社だし、\x01",
            "裏を取るのは苦労しそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0246
    ChrTalk(
        0x102,
        (
            "#00103Fあまり役に立たないかも\x01",
            "しれないけど……\x02\x03",

            "#00100F私の家になら、もしかしたら\x01",
            "参考になるものがあるかも。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)

    #C0247
    ChrTalk(
        0x103,
        "#00205F参考になるもの……？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#00100F実は、私の家にクインシー社の\x01",
            "パンフレットがあるの。\x02\x03",

            "あれになら、会社の概要とかが\x01",
            "書かれていたから、もしかしたら\x01",
            "参考になるかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        (
            "#00300Fクインシー社のパンフレット……\x01",
            "なんでお嬢がンなもんを持ってんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0250
    ChrTalk(
        0x102,
        (
            "#00113Fえっと、実は私……\x01",
            "お菓子作りとか結構好きなんだけど……\x02\x03",

            "#00100Fこの前、クインシー社について\x01",
            "すごく興味がわいてしまって、\x01",
            "ついパンフレットを取り寄せたのよね。\x02\x03",

            "実家の私の部屋の\x01",
            "本棚に置いてあるはずだけど……\x02\x03",

            "#00106F……って、ダメよね。\x01",
            "流石にそんなパンフレットなんかじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#02203Fいや、もしかしたらと言うこともありうる。\x02\x03",

            "#02200F会社の正式な資料となれば、\x01",
            "何かしら、ミンネスという男の言葉と\x01",
            "矛盾する内容が見つかるかもしれない。\x02\x03",

            "念の為調べてみるといいんじゃないかね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0252
    ChrTalk(
        0x101,
        (
            "#00003Fそうですね……\x01",
            "一応エリィの家にも行ってみます。\x02\x03",

            "#00000F……イアン先生、貴重なお話を\x01",
            "ありがとうございました。\x02\x03",

            "おかげで捜査方針が\x01",
            "まとまりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "#02200Fうむ、少しは\x01",
            "役に立てたようで何よりだ。\x02\x03",

            "……確か、君たちは今\x01",
            "ハロルド君の家を拠点に\x01",
            "捜査をしているんだったね？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        "#00005Fええ、そうですけど……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "#02200Fなに、今回の事件……\x01",
            "時間の許す限りは\x01",
            "手伝わせてもらおうと思ってね。\x02\x03",

            "#02203Fなにぶん忙しい身なので、\x01",
            "そこまで役には立てないだろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x102,
        (
            "#00109Fいいえ、そんな……\x01",
            "とっても心強いです！\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x105,
        (
            "#10302Fプロフェッショナルがいるなら\x01",
            "百人力だねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "#02202Fふふ、あとで顔を出すから\x01",
            "君たちも捜査のほうを\x01",
            "がんばってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#00000Fええ、ありがとうございます。\x02\x03",

            "#00003F……それじゃあ、\x01",
            "早速捜査に当たるとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    #C0260
    ChrTalk(
        0x101,
        (
            "#00001FＩＢＣで資金繰りを調べ、\x01",
            "ミンネスの計画の裏を取る……\x02\x03",

            "そして、参考程度に\x01",
            "マクダエル邸にある資料を調べて、\x01",
            "彼の言葉との齟齬を探してみる……\x02\x03",

            "調査するのは以上の２つのポイントだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x109,
        (
            "#10102F了解です……\x01",
            "なんとしても証拠を挙げましょう！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x87, 0x1, 0x1)
    SetScenarioFlags(0x177, 3)
    ClearMapFlags(0x10000000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    SetChrPos(0x0, 2400, 30, 1120, 225)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_13_5315 end

    def Function_14_7186(): pass

    label("Function_14_7186")


    def lambda_718B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_718B)

    def lambda_719C():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_719C)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3290, 30, 900, 2000, 0x0)
    TurnDirection(0x101, 0x8, 500)
    Return()

    # Function_14_7186 end

    def Function_15_71D1(): pass

    label("Function_15_71D1")


    def lambda_71D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_71D6)

    def lambda_71E7():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71E7)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 2330, 30, 1420, 2000, 0x0)
    TurnDirection(0x102, 0x8, 500)
    Return()

    # Function_15_71D1 end

    def Function_16_721C(): pass

    label("Function_16_721C")


    def lambda_7221():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7221)

    def lambda_7232():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7232)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 3210, 30, -360, 2000, 0x0)
    TurnDirection(0x103, 0x8, 500)
    Return()

    # Function_16_721C end

    def Function_17_7267(): pass

    label("Function_17_7267")


    def lambda_726C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_726C)

    def lambda_727D():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_727D)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2300, 30, 80, 2000, 0x0)
    TurnDirection(0x104, 0x8, 500)
    Return()

    # Function_17_7267 end

    def Function_18_72B2(): pass

    label("Function_18_72B2")


    def lambda_72B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_72B7)

    def lambda_72C8():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_72C8)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 1960, 30, -1080, 2000, 0x0)
    TurnDirection(0x109, 0x8, 500)
    Return()

    # Function_18_72B2 end

    def Function_19_72FD(): pass

    label("Function_19_72FD")


    def lambda_7302():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7302)

    def lambda_7313():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7313)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1200, 0, 350, 2000, 0x0)
    TurnDirection(0x105, 0x8, 500)
    Return()

    # Function_19_72FD end

    def Function_20_7348(): pass

    label("Function_20_7348")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0262
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_20_7348 end

    SaveToFile()

Try(main)
