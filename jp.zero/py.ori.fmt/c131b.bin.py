from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c131b.bin",                # FileName
        "c131b",                    # MapName
        "c131b",                    # Location
        0x001C,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c131b",                  # 0
        "受付嬢ランフィ",         # 1
        "警備員ビルス",           # 2
        "受付嬢コリンナ",         # 3
        "ツァイト",               # 4
        "ランディ",               # 5
        "ギヨーム親方",           # 6
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch27900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch02708.itc",                   # 03
        "chr/ch00302.itc",                   # 04
        "chr/ch26400.itc",                   # 05
        "chr/ch02702.itc",                   # 06
    ))

    DeclNpc(0,       300,     31700,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(1190,    300,     4789,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7110,    300,     32759,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7300,   0,       23299,   180,  277,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5710,   0,       23809,   180,  277,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(7150,    0,       20149,   270,  261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)

    DeclEvent(0x0000, 0, 15,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  6,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  8,  0x0000)
    DeclActor(7670,    0,       13360,   1500,    7670,    1400,    13360,   0x007C, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_264",          # 00, 0
        "Function_1_31C",          # 01, 1
        "Function_2_3E4",          # 02, 2
        "Function_3_3EB",          # 03, 3
        "Function_4_463",          # 04, 4
        "Function_5_56E",          # 05, 5
        "Function_6_71C",          # 06, 6
        "Function_7_720",          # 07, 7
        "Function_8_A9C",          # 08, 8
        "Function_9_AA0",          # 09, 9
        "Function_10_E48",         # 0A, 10
        "Function_11_F7C",         # 0B, 11
        "Function_12_157C",        # 0C, 12
        "Function_13_2977",        # 0D, 13
        "Function_14_2E8E",        # 0E, 14
        "Function_15_2F09",        # 0F, 15
    ))


    def Function_0_264(): pass

    label("Function_0_264")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2A4"),
        (1, "loc_2B0"),
        (2, "loc_2BC"),
        (3, "loc_2C8"),
        (4, "loc_2D4"),
        (5, "loc_2E0"),
        (6, "loc_2EC"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_2A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_31B")

    Return()

    # Function_0_264 end

    def Function_1_31C(): pass

    label("Function_1_31C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_378")
    ClearScenarioFlags(0x5F, 1)
    SetChrPos(0x0, 7670, 0, 16000, 270)
    SetChrPos(0x1, 7670, 0, 16000, 270)
    SetChrPos(0x2, 7670, 0, 16000, 270)
    SetChrPos(0x3, 7670, 0, 16000, 270)
    Event(0, 2)

    label("loc_378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0xC, 0x80)

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_3D2")
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xB, -1330, 300, 17250, 135)
    SetChrPos(0xD, 1180, 300, 11650, 270)
    SetChrPos(0x9, -1440, 300, 5330, 180)

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_3E3")
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)

    label("loc_3E3")

    Return()

    # Function_1_31C end

    def Function_2_3E4(): pass

    label("Function_2_3E4")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_3E4 end

    def Function_3_3EB(): pass

    label("Function_3_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B")
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_431")

    label("loc_41B")

    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_431")

    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44E")
    OP_1B(0x0, 0x0, 0xE)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_462")
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_462")

    Return()

    # Function_3_3EB end

    def Function_4_463(): pass

    label("Function_4_463")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x1, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_550")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_56C")

    Return()

    # Function_4_463 end

    def Function_5_56E(): pass

    label("Function_5_56E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_628")

    #C0002
    ChrTalk(
        0xFE,
        (
            "門の前に来ている連中が\x01",
            "導力爆弾らしき物を設置しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "君たちが連中を撃退した後、\x01",
            "我々が爆弾を回収する！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "……くれぐれも気をつけてな。\x01",
            "女神の加護を！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_718")

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C0")

    #C0005
    ChrTalk(
        0xFE,
        "君たちも大変だったらしいな……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "ここは我々\x01",
            "保安部の者に任せてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ＩＢＣにいる限り、君たちには\x01",
            "指一本触れさせないさ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_718")

    label("loc_6C0")


    #C0008
    ChrTalk(
        0xFE,
        (
            "外は保安部の者が\x01",
            "万全の警備を敷いている。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "心配はいらない、\x01",
            "ここは任せてくれ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_718")

    TalkEnd(0xFE)
    Return()

    # Function_5_56E end

    def Function_6_71C(): pass

    label("Function_6_71C")

    Call(0, 7)
    Return()

    # Function_6_71C end

    def Function_7_720(): pass

    label("Function_7_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_895")
    TalkBegin(0x8)

    #C0010
    ChrTalk(
        0x8,
        (
            "これはロイド様……\x01",
            "総裁からすべて伺っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "本日は大変な事に\x01",
            "なってしまいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#0006Fすみません、ここの人たちまで\x01",
            "巻き込んでしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "いえいえ、私たちの事は\x01",
            "お気になさらないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "それにクロイス総裁なら\x01",
            "この事態を黙って見過ごされる\x01",
            "わけがありませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "どうか私たちにも\x01",
            "協力させてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Jump("loc_A9B")

    label("loc_895")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A98")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                    # 0
            "買い物をする（装備品）\x01",      # 1
            "買い物をする（消耗品）\x01",      # 2
            "やめる\x01",                      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_92B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94B")
    OP_AF(0xB8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A93")

    label("loc_94B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96B")
    OP_AF(0xB9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A93")

    label("loc_96B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97F")
    Jump("loc_A93")

    label("loc_97F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A93")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_A12")

    #C0016
    ChrTalk(
        0x8,
        (
            "まさかこのような事に\x01",
            "なってしまうとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "皆様、くれぐれもお気をつけて。\x01",
            "ご武運を祈っていますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A93")

    label("loc_A12")


    #C0018
    ChrTalk(
        0x8,
        (
            "クロイス総裁なら\x01",
            "この事態を黙って見過ごされる\x01",
            "わけがありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "どうか私たち職員にも\x01",
            "できるだけの協力をさせて下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A93")

    Jump("loc_8A2")

    label("loc_A98")

    TalkEnd(0x8)

    label("loc_A9B")

    Return()

    # Function_7_720 end

    def Function_8_A9C(): pass

    label("Function_8_A9C")

    Call(0, 9)
    Return()

    # Function_8_A9C end

    def Function_9_AA0(): pass

    label("Function_9_AA0")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE9")

    #C0020
    ChrTalk(
        0xA,
        (
            "警備隊を操るとは\x01",
            "不気味なお話ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        "ですがきっと、皆様は幸運ですよ。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xA,
        (
            "ここは天下の\x01",
            "ＩＢＣビルでございますからー。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0002Fはは、そうですね。\x02\x03",

            "#0004F（確かにＩＢＣに\x01",
            "  匿ってもらえたのは\x01",
            "  ラッキーだったな。）\x02\x03",

            "#0008F（……今のうちに\x01",
            "  装備はできるだけ\x01",
            "  整えておかないと。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E44")

    label("loc_BE9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E44")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                  # 0
            "交換する（装備品）\x01",        # 1
            "交換する（クオーツ）\x01",      # 2
            "交換する（その他）\x01",        # 3
            "やめる\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C89")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA9")
    OP_AF(0xBA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3F")

    label("loc_CA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC9")
    OP_AF(0xBB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3F")

    label("loc_CC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE9")
    OP_AF(0xBC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3F")

    label("loc_CE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFD")
    Jump("loc_E3F")

    label("loc_CFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_DBB")

    #C0024
    ChrTalk(
        0xA,
        (
            "このＩＢＣビルまで\x01",
            "攻めてくるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "申し訳ありませんが\x01",
            "わたくしたちの命運、\x01",
            "皆様に預けさせていただきますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3F")

    label("loc_DBB")


    #C0027
    ChrTalk(
        0xA,
        (
            "警備隊を操るとは\x01",
            "不気味なお話ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        "ですがきっと、皆様は幸運ですよ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "ここは天下の\x01",
            "ＩＢＣビルでございますからー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3F")

    Jump("loc_BF3")

    label("loc_E44")

    TalkEnd(0xA)
    Return()

    # Function_9_AA0 end

    def Function_10_E48(): pass

    label("Function_10_E48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_EC8")

    #C0030
    ChrTalk(
        0xB,
        "#1201Fグルルルル………！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#0002Fツァイト……\x01",
            "このビルの守りは任せたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        "#1200Fグルル……ウォン！\x02",
    )

    CloseMessageWindow()
    Jump("loc_F78")

    label("loc_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_END)), "loc_F33")

    #C0033
    ChrTalk(
        0xB,
        "#1201Fグルルルルルルルル……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0005F（ツァイト……？\x01",
            "  気が立ってるみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F78")

    label("loc_F33")


    #C0035
    ChrTalk(
        0xB,
        "#1200Fグルルルルル……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0000Fツァイト……\x01",
            "ここは頼んだぞ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F78")

    TalkEnd(0xFE)
    Return()

    # Function_10_E48 end

    def Function_11_F7C(): pass

    label("Function_11_F7C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1010")
    Jump("loc_105A")

    label("loc_1010")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1030")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_105A")

    label("loc_1030")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1050")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_105A")

    label("loc_1050")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_105A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_END)), "loc_1369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12DE")
    OP_4B(0xB, 0xFF)

    #C0037
    ChrTalk(
        0x101,
        "#0001Fランディ、外の様子は？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xC,
        (
            "#0306Fああ、今のところ動きはねぇ。\x02\x03",

            "#0301Fとはいえ、そろそろ\x01",
            "嗅ぎ付かれても不思議じゃねぇな。\x02\x03",

            "あの派手なリムジンが、\x01",
            "ここの大将の愛車だってのは\x01",
            "さすがに判るだろうしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0003F……確かに。\x02\x03",

            "#0000Fツァイトも悪いな。\x01",
            "こっちの方はよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        "#1200Fウォン。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        (
            "#0309Fハハ……\x01",
            "相変わらず偉そうなヤツだぜ。\x02\x03",

            "#0304F──ま、ここまで来たら\x01",
            "腹を括るっきゃねえだろ。\x02\x03",

            "#0300F警備隊がここを攻めるとしたら\x01",
            "多分、波状攻撃を仕掛けるはずだ。\x02\x03",

            "連戦になるかもしれねぇから\x01",
            "今のうちに補給は頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        "#0000Fああ、了解。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE4, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1364")

    label("loc_12DE")


    #C0043
    ChrTalk(
        0xC,
        (
            "#0303F警備隊がここを攻めるとしたら\x01",
            "多分、波状攻撃を仕掛けるはずだ。\x02\x03",

            "#0300F連戦になるかもしれねぇから\x01",
            "今のうちに補給は頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1364")

    Jump("loc_1574")

    label("loc_1369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F6")
    OP_4B(0xB, 0xFF)

    #C0044
    ChrTalk(
        0x101,
        "#0001Fランディ、外の様子は？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        (
            "#0304Fああ、今の所は問題ねえよ。\x02\x03",

            "#0300Fさすがにリムジンの速度だ。\x01",
            "連中も完璧に撒けたみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0002Fそうか……ツァイトもいるし\x01",
            "こっちは安心だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xB,
        "#1200Fウォン。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "#0306Fま、ここまで来たら\x01",
            "何があってもおかしくねえ\x01",
            "状況だけどな。\x02\x03",

            "#0300F……ロイド。\x01",
            "補充だけは済ませとけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#0000Fああ、分かってる。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0xB, 0xFF)
    Jump("loc_1574")

    label("loc_14F6")


    #C0050
    ChrTalk(
        0xC,
        (
            "#0303F外はここの警備員連中が\x01",
            "見張りをしてるらしい。\x02\x03",

            "#0300F一休みしたら、俺らは腰を据えて\x01",
            "今後の対策を考えるとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1574")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_F7C end

    def Function_12_157C(): pass

    label("Function_12_157C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1623")

    #C0051
    ChrTalk(
        0xFE,
        (
            "おう、ハナシは聞いたぜ。\x01",
            "お前ぇらで打って出るそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "……準備は万全か？\x01",
            "装備や隊列も見直しとけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "しっかりな、特務支援課！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 4)
    Jump("loc_1C11")

    label("loc_1623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C11")

    #C0054
    ChrTalk(
        0xD,
        (
            "いよう……\x01",
            "何だかとんでもねえ事に\x01",
            "なってやがんな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 4)), scpexpr(EXPR_END)), "loc_1796")

    #C0055
    ChrTalk(
        0x101,
        (
            "#0005F修理屋の親方さん……\x02\x03",

            "#0000Fそういえば、今日は\x01",
            "財団支部に顔を出すって\x01",
            "仰ってましたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xD,
        (
            "おう、そうなのよ。\x01",
            "あれからここの\x01",
            "５階にある支部を訪ねててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        (
            "ロバーツの奴と発明のアイデアを\x01",
            "話し込んでたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xD,
        (
            "まさか、こんな事に\x01",
            "なっちまうとはな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188A")

    label("loc_1796")


    #C0059
    ChrTalk(
        0x101,
        (
            "#0005F旧市街にいた修理屋の……\x02\x03",

            "#0005F親方さん、どうしてこちらに？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xD,
        (
            "いやなに、今日は\x01",
            "財団の支部を訪ねてたとこでよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xD,
        (
            "ロバーツの奴と\x01",
            "発明のアイデアを話し込んでたら\x01",
            "遅くなっちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xD,
        (
            "だがまさか\x01",
            "こんな事になっちまうとはな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188A")


    #C0063
    ChrTalk(
        0x101,
        (
            "#0003Fすみません、俺たちのせいで\x01",
            "巻き込んでしまいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xD,
        (
            "なはは、気にすんな！\x01",
            "別にお前ぇらのせいじゃねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xD,
        (
            "それよりこんなオヤジでも\x01",
            "役に立つ事がありそうだ。\x01",
            "全力で協力させてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xD,
        "工房道具は一式用意してきてる。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xD,
        (
            "オーブメントの改造から\x01",
            "武器の強化まで、\x01",
            "何でも言いつけてくれや！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#0000Fありがとうございます。\x01",
            "ありがたく利用させて頂きます。\x02\x03",

            "#0003F（そうだな……装備と合わせて\x01",
            "  オーブメントも確認しておこう。）\x02\x03",

            "（これから何があるか\x01",
            "  分からないからな。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFE")
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ギヨーム親方に話しかけて『改造を頼む』を選択すると、\x01",
            "  改造可能な商品が一覧表示されます。\x01",
            "  必要な素材を持っていれば、改造を行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※改造によってできた武器・防具は\x01",
            "  武器商会などでは入手出来ない強力なもので、\x01",
            "  特に武器には特殊な効果がついていることがあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※改造に必要な『素材』は、\x01",
            "  主に魔獣が落とすことがあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    label("loc_1BFE")

    SetScenarioFlags(0xEE, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xD)
    Return()

    label("loc_1C11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F38")

    #C0072
    ChrTalk(
        0xFE,
        (
            "ところでそいつは……\x01",
            "『ゼムリアストーン』じゃねえか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "お前ぇすげえ物もってやがるな！\x01",
            "一体どこで手に入れたんだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0005Fええと、これって\x01",
            "そんなに貴重な物なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "おうよ、その石っころは\x01",
            "古代文明の遺物って言われててな、\x01",
            "とんでもなく硬ぇのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "だが……つい昨年辺りに\x01",
            "ようやく加工法が見つかったって噂だぜ。\x01",
            "俺も財団の方面から聞いた事がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "こいつを使って武器が作れれば……\x01",
            "きっと最強の威力を持つはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#0005Fそ、そんな代物だったんですか。\x02\x03",

            "#0003Fでも最強の武器、か……\x01",
            "状況が状況だけに\x01",
            "あれば欲しい所だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "へへっ、俺も丁度\x01",
            "新しい武器の設計図を\x01",
            "引いている所なんでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "お前ぇさんさえよけりゃあ\x01",
            "そのゼムリアストーンで\x01",
            "作ってやってもいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……その石１個を使えば\x01",
            "１人分の武器が作れると思うが……\x01",
            "どうだ、試してみるか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 7)
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_1F38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_255C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2557")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "話をする")
    MenuCmd(1, 0, "改造・合成する（オーブメント）")
    MenuCmd(1, 0, "改造を頼む（装備品）")
    MenuCmd(1, 0, "アップデートを頼む")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2016")
    MenuCmd(1, 0, "最強武器を頼む")

    label("loc_2016")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_204A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_204A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2070")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2070")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21DD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    #C0082
    ChrTalk(
        0xD,
        (
            "そういやお前ぇ、\x01",
            "『スロットの強化』ってのは知ってるかい？\x02",
        )
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※スロットの強化について。\x02",
        )
    )

    CloseMessageWindow()

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※[SLOT]を選んで\x01",
            "  開封済みのスロットを選択すると\x01",
            "  スロットレベルを強化する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※上位クオーツのセットが可能になるほか、\x01",
            "  最大ＥＰもこれまで以上に\x01",
            "  引き上げる事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)

    label("loc_21DD")

    OP_AF(0xAF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2552")

    label("loc_21EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_220E")
    OP_AF(0xAE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2552")

    label("loc_220E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23DF")

    #C0086
    ChrTalk(
        0xD,
        "おっ、例の魔導杖の改造か。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xD,
        (
            "準備は一通り揃えてるぜ。\x01",
            "材料を使って\x01",
            "改造しちまうかよ？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【頼む】\x01",            # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2371")

    #C0088
    ChrTalk(
        0x101,
        "#0000Fええ、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xD,
        (
            "うっし、んじゃあ\x01",
            "ロバーツの奴に\x01",
            "声を掛けてくるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0000Fそうですね。\x01",
            "ついでにティオにも\x01",
            "話をしてきましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 1)
    NewScene("c1320", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_2371")


    #C0091
    ChrTalk(
        0xD,
        (
            "そうかい、またアップデートを\x01",
            "したくなったら言ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xD,
        "準備だけは整えてあるからよ。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2552")

    label("loc_23DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_240A")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2405")
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_2405")

    Jump("loc_2552")

    label("loc_240A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241E")
    Jump("loc_2552")

    label("loc_241E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2552")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_24B4")

    #C0093
    ChrTalk(
        0xFE,
        (
            "ハナシは聞いたぜ。\x01",
            "お前ぇらで打って出るそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "……準備は万全かよ？\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        "しっかりな、特務支援課！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2552")

    label("loc_24B4")


    #C0096
    ChrTalk(
        0xD,
        (
            "このビルにはエプスタイン財団の\x01",
            "支部も入ってっからな。\x01",
            "設備は申し分ねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "何か用事がありゃあ\x01",
            "遠慮なく言いつけてくれ。\x01",
            "ガッツリ対応してやるからよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2552")

    Jump("loc_1F7C")

    label("loc_2557")

    Jump("loc_2973")

    label("loc_255C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2566")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2973")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "話をする")
    MenuCmd(1, 0, "改造・合成する（オーブメント）")
    MenuCmd(1, 0, "改造を頼む（装備品）")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25EA")
    MenuCmd(1, 0, "最強武器を頼む")

    label("loc_25EA")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_261E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_261E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2644")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2644")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    #C0098
    ChrTalk(
        0xD,
        (
            "そういやお前ぇ、\x01",
            "『スロットの強化』ってのは知ってるかい？\x02",
        )
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※スロットの強化について。\x02",
        )
    )

    CloseMessageWindow()

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※[SLOT]を選んで\x01",
            "  開封済みのスロットを選択すると\x01",
            "  スロットレベルを強化する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※上位クオーツのセットが可能になるほか、\x01",
            "  最大ＥＰもこれまで以上に\x01",
            "  引き上げる事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)

    label("loc_27B1")

    OP_AF(0xAF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_296E")

    label("loc_27C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E2")
    OP_AF(0xAE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_296E")

    label("loc_27E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280D")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2808")
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_2808")

    Jump("loc_296E")

    label("loc_280D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2821")
    Jump("loc_296E")

    label("loc_2821")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_28D0")

    #C0102
    ChrTalk(
        0xFE,
        (
            "ハナシは聞いたぜ。\x01",
            "お前ぇらで打って出るそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "……準備は万全か？\x01",
            "装備や隊列も見直しとけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "しっかりな、特務支援課！\x02",
    )

    CloseMessageWindow()
    Jump("loc_296E")

    label("loc_28D0")


    #C0105
    ChrTalk(
        0xD,
        (
            "このビルにはエプスタイン財団の\x01",
            "支部も入ってっからな。\x01",
            "設備は申し分ねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xD,
        (
            "何か用事がありゃあ\x01",
            "遠慮なく言いつけてくれ。\x01",
            "ガッツリ対応してやるからよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296E")

    Jump("loc_2566")

    label("loc_2973")

    TalkEnd(0xD)
    Return()

    # Function_12_157C end

    def Function_13_2977(): pass

    label("Function_13_2977")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【ロイドの武器を頼む】\x01",        # 0
            "【エリィの武器を頼む】\x01",        # 1
            "【ティオの武器を頼む】\x01",        # 2
            "【ランディの武器を頼む】\x01",      # 3
            "【やめる】\x01",                    # 4
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA5")

    #C0107
    ChrTalk(
        0xFE,
        (
            "よしきた、一丁腕を\x01",
            "振るってやろうじゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "かのゼムリアストーンから\x01",
            "俺の最高傑作を造ってやるぜい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACE")

    label("loc_2AA5")


    #C0109
    ChrTalk(
        0xFE,
        (
            "よしきた、ちょいと\x01",
            "待っててくれや！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4B(0xD, 0xFF)
    OP_68(6020, 1500, 19170, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(17100, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0x101, 5670, 0, 19810, 90)
    OP_93(0xD, 0x10E, 0x0)
    Sleep(1500)
    FadeToBright(2000, 0)
    OP_0D()

    #C0110
    ChrTalk(
        0xFE,
        "#2P#40Wウム、調整はこんな所かねぇ……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "#2P……よし、できだぜ。\x01",
            "受け取んな！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD9")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x3F4, 1)
    Jump("loc_2C6A")

    label("loc_2BD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C0B")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x408),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x408, 1)
    Jump("loc_2C6A")

    label("loc_2C0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3D")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x41C, 1)
    Jump("loc_2C6A")

    label("loc_2C3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6A")

    #A0115
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x430),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x430, 1)

    label("loc_2C6A")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x396, 1)
    OP_DE(0x18, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D87")

    #C0116
    ChrTalk(
        0x101,
        (
            "#0005F本当にできた……\x02\x03",

            "#0005F親方さん、ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "#2Pいいってことよ。\x01",
            "こんな素材が扱えるなんて\x01",
            "俺も技師冥利に尽きるってモンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "#2Pまた用事があったら\x01",
            "遠慮なく声をかけなよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#0000Fはい、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E11")

    label("loc_2D87")


    #C0120
    ChrTalk(
        0xFE,
        (
            "#2Pこんな時だからこそ\x01",
            "こいつも役に立つはずだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "#2Pつうわけで、しっかりやれよ！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#0000Fはい、大切に\x01",
            "使わせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E11")

    OP_5A()
    SetScenarioFlags(0xF0, 0)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xA, 0x8000)
    EventEnd(0x5)
    Jump("loc_2E8D")

    label("loc_2E25")


    #C0123
    ChrTalk(
        0xFE,
        (
            "そうかい、また\x01",
            "用事があったら声をかけな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "俺にできる事なら何でも\x01",
            "ガッツリ対応してやるからよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E8D")

    Return()

    # Function_13_2977 end

    def Function_14_2E8E(): pass

    label("Function_14_2E8E")

    EventBegin(0x1)

    #C0125
    ChrTalk(
        0x101,
        (
            "#0003F外は警備員の人たちが\x01",
            "見張ってくれている……\x02\x03",

            "#0001F俺たちは補充と\x01",
            "休息を取っておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -460, 300, 4950, 0)
    EventEnd(0x4)
    Return()

    # Function_14_2E8E end

    def Function_15_2F09(): pass

    label("Function_15_2F09")

    EventBegin(0x1)

    #C0126
    ChrTalk(
        0x101,
        (
            "#0003Fゲート前の導力爆弾を撤去して、\x01",
            "警備隊員たちの突入を阻止しないと。\x02\x03",

            "#0001F……猶予はない。\x01",
            "正面から打って出よう！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    EventEnd(0x4)
    Return()

    # Function_15_2F09 end

    SaveToFile()

Try(main)
