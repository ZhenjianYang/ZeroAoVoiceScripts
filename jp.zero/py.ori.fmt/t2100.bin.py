from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2100.bin",                # FileName
        "t2100",                    # MapName
        "t2100",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2100",                  # 0
        "ブルード隊員",           # 1
        "ダリア隊員",             # 2
        "エステル",               # 3
        "ヨシュア",               # 4
        "観光客ディーン",         # 5
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch34100.itc",                   # 01
        "chr/ch00600.itc",                   # 02
        "chr/ch00700.itc",                   # 03
        "chr/ch26700.itc",                   # 04
    ))

    DeclNpc(-13829,  10000,   -2960,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-14060,  10000,   2900,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-15819,  5000,    -16600,  265,  405,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-16780,  5000,    -17700,  315,  405,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-17709,  5000,    -18780,  220,  385,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(-100,    10000,   -260,    1000,    -100,    10000,   -260,    0x007C, 0,  11, 0x0000)
    DeclActor(-1690,   10000,   -9200,   1000,    -1690,   10000,   -9200,   0x007C, 0,  12, 0x0000)
    DeclActor(8710,    10000,   -11130,  1000,    8710,    10000,   -11130,  0x007C, 0,  13, 0x0000)
    DeclActor(-16000,  10000,   0,       2000,    -16000,  10000,   0,       0x007C, 0,  14, 0x0000)
    DeclActor(15480,   10000,   4880,    1000,    19930,   7500,    5800,    0x007C, 0,  16, 0x0000)
    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_369",          # 02, 2
        "Function_3_40D",          # 03, 3
        "Function_4_4D2",          # 04, 4
        "Function_5_61F",          # 05, 5
        "Function_6_BC0",          # 06, 6
        "Function_7_1902",         # 07, 7
        "Function_8_1B65",         # 08, 8
        "Function_9_1BF1",         # 09, 9
        "Function_10_1CE7",        # 0A, 10
        "Function_11_1F04",        # 0B, 11
        "Function_12_2114",        # 0C, 12
        "Function_13_232C",        # 0D, 13
        "Function_14_24F8",        # 0E, 14
        "Function_15_2E29",        # 0F, 15
        "Function_16_2FDC",        # 10, 16
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_368")
    OP_95(0xFE, -13830, 10000, -2960, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -14060, 10000, 2900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    Jump("Function_1_308")

    label("loc_368")

    Return()

    # Function_1_308 end

    def Function_2_369(): pass

    label("Function_2_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_381")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_399")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_39F")

    label("loc_399")

    BeginChrThread(0x9, 0, 0, 1)

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    SetChrPos(0x8, -8560, 5000, -19100, 175)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_3F9")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    Event(0, 10)

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C")
    ClearChrFlags(0xC, 0x80)

    label("loc_40C")

    Return()

    # Function_2_369 end

    def Function_3_40D(): pass

    label("Function_3_40D")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    OP_66(0x4, 0x1)
    Jump("loc_4BA")

    label("loc_465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_4BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484")
    OP_66(0x0, 0x1)

    label("loc_484")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496")
    OP_66(0x1, 0x1)

    label("loc_496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8")
    OP_66(0x2, 0x1)

    label("loc_4A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA")
    OP_66(0x3, 0x1)

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD")
    OP_70(0x2, 0x0)
    Jump("loc_4D1")

    label("loc_4CD")

    OP_70(0x2, 0x1E)

    label("loc_4D1")

    Return()

    # Function_3_40D end

    def Function_4_4D2(): pass

    label("Function_4_4D2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CE")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x646, 1)"), scpexpr(EXPR_END)), "loc_557")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_5C9")

    label("loc_557")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_5C9")

    Jump("loc_613")

    label("loc_5CE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
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

    label("loc_613")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4D2 end

    def Function_5_61F(): pass

    label("Function_5_61F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5")

    #C0004
    ChrTalk(
        0xFE,
        (
            "今日は珍しく、ダリア君の方から\x01",
            "話しかけてくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……話がコアすぎて\x01",
            "ついてけなかったけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6EB")

    label("loc_6A5")


    #C0006
    ChrTalk(
        0xFE,
        (
            "うーん、親睦を深める\x01",
            "チャンスだったのにな。\x01",
            "自分の無知が憎いよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EB")

    Jump("loc_BBC")

    label("loc_6F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_84B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5")

    #C0007
    ChrTalk(
        0xFE,
        (
            "二人だけでこんなとこ\x01",
            "突っ立ってるって気恥ずかしいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "ダリア君は人一倍\x01",
            "礼儀正しくしてるから\x01",
            "世間話もしづらいし……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "はぁ、一人になりたいよ。\x01",
            "また休憩させてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_846")

    label("loc_7C5")


    #C0010
    ChrTalk(
        0xFE,
        (
            "タングラム門に勤めてるバレルとなら\x01",
            "付き合いも長いし\x01",
            "気にならないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "女性と二人っきりってのは\x01",
            "どうも苦手だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_846")

    Jump("loc_BBC")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_924")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BB")

    #C0012
    ChrTalk(
        0xFE,
        (
            "ふぅ……\x01",
            "やっぱりこの場所は落ち着くね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "もう少ししたら国境監視に戻るか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_91F")

    label("loc_8BB")


    #C0014
    ChrTalk(
        0xFE,
        (
            "ちゃんとダリア君に\x01",
            "了承を取って休憩してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "……サボッてるわけじゃ\x01",
            "決してないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91F")

    Jump("loc_BBC")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BBC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A17")

    #C0016
    ChrTalk(
        0xFE,
        "え、例の起動キーが屋上にあるはずだって？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "うーん、僕とダリアくんも\x01",
            "念のため隅々まで探したんだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……でも、もしかしたら\x01",
            "見落としてるだけかもしれない。\x01",
            "捜索はよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A82")

    label("loc_A17")


    #C0019
    ChrTalk(
        0xFE,
        (
            "起動キーは僕たちも探したんだが……\x01",
            "見落としてるだけかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "すまないが、調べてみてくれ。\x02",
    )

    CloseMessageWindow()

    label("loc_A82")

    Jump("loc_BBC")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4E")

    #C0021
    ChrTalk(
        0xFE,
        (
            "タングラム門の方には\x01",
            "バレルっていう友人が勤めてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "正直、アイツがうらやましいよ……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "ここじゃイザというときに\x01",
            "司令がいないかもしれないから\x01",
            "すごい不安なんだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BBC")

    label("loc_B4E")


    #C0024
    ChrTalk(
        0xFE,
        (
            "タングラム門に勤めてる\x01",
            "バレルのヤツがうらやましいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "こっちに配属されるなんて\x01",
            "運が悪かったなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBC")

    TalkEnd(0xFE)
    Return()

    # Function_5_61F end

    def Function_6_BC0(): pass

    label("Function_6_BC0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFC")

    #C0026
    ChrTalk(
        0xFE,
        (
            "数年前、帝国のギルドが\x01",
            "猟兵団によって同時多発的に\x01",
            "襲撃される事件がありました。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "高名な遊撃士によって\x01",
            "事態は収束したそうですが……\x01",
            "未だに色々ないわくが残っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "実は襲撃事件自体が、\x01",
            "大規模な陽動作戦であったなどとも\x01",
            "言われていますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "……何か、裏を感じますね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D4B")

    label("loc_CFC")


    #C0030
    ChrTalk(
        0xFE,
        (
            "数年前に起きた\x01",
            "帝国のギルドの襲撃事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "……何か、裏を感じますね。\x02",
    )

    CloseMessageWindow()

    label("loc_D4B")

    Jump("loc_18FE")

    label("loc_D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DE3")

    #C0032
    ChrTalk(
        0xFE,
        (
            "あの帝国の堅牢ぶりを見ると……\x01",
            "この門がいかに無防備なものかを\x01",
            "痛感させられます。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "帝国が本気を出したら\x01",
            "きっとこんな門は……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18FE")

    label("loc_DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_EAD")

    #C0034
    ChrTalk(
        0xFE,
        (
            "以前リベールで起こった\x01",
            "導力停止現象……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "そのとき、帝国のオズボーン宰相閣下は\x01",
            "廃れたはずの蒸気機関の戦車を\x01",
            "大胆にも出動させたとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "あの準備のよさ……\x01",
            "本当に恐ろしい男です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18FE")

    label("loc_EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_102D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8E")

    #C0037
    ChrTalk(
        0xFE,
        (
            "せっかく同じ場所を警備しているので\x01",
            "なんとか親睦を深めようと\x01",
            "話題を振ってみたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "少し前のリベールの異変について\x01",
            "どう思ったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "なんて突然聞くようなことじゃ\x01",
            "なかったですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1028")

    label("loc_F8E")


    #C0040
    ChrTalk(
        0xFE,
        (
            "ふぅ……人見知りは辛いです。\x01",
            "一度話題が途切れると\x01",
            "どうも気まずいというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "仕方ありません、\x01",
            "今日はもう黙って\x01",
            "仕事に集中したほうがいいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1028")

    Jump("loc_18FE")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_11AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1112")

    #C0042
    ChrTalk(
        0xFE,
        (
            "ブルードさんとは\x01",
            "話し始めてもなかなか長続きしません。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "女性隊員となら\x01",
            "そうでもないんですが……\x01",
            "自分は人見知りですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "同じ国境監視の任についてるのだし\x01",
            "もう少し親しくしたいところです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11A6")

    label("loc_1112")


    #C0045
    ChrTalk(
        0xFE,
        (
            "ミレイユ准尉となら\x01",
            "親しみやすいですし、\x01",
            "結構よく話すのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "男性の方と二人というのは\x01",
            "どうにも慣れません。\x01",
            "自分は人見知りですから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A6")

    Jump("loc_18FE")

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_12F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1286")

    #C0047
    ChrTalk(
        0xFE,
        (
            "ブルードさんが\x01",
            "一服したいというので\x01",
            "少しの間一人警備です。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "ほんとはダメなんですけど……\x01",
            "司令もいないので、こっそり。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "同じ景色を見張っているのは\x01",
            "仕事といえどやはり飽きますしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12EE")

    label("loc_1286")


    #C0050
    ChrTalk(
        0xFE,
        (
            "……自分も後で\x01",
            "休憩させてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "仕事をサボる気持ちを味わうのも\x01",
            "一興かもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EE")

    Jump("loc_18FE")

    label("loc_12F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1582")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_138C")

    #C0052
    ChrTalk(
        0xFE,
        "……ふぅ……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "昨夜、この屋上で司令が\x01",
            "大声で歌を歌っていて……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "忙しいのに満足な睡眠が\x01",
            "取れませんでした。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157D")

    label("loc_138C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AC")

    #C0055
    ChrTalk(
        0xFE,
        (
            "警備隊の女性隊員数は\x01",
            "あまり多くはありませんから\x01",
            "好奇の目で見られることもあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "タングラム門のソーニャ副司令や\x01",
            "ノエル曹長は美人ですから\x01",
            "特に大変だと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "『あの美人隊員にインタビュー！』\x01",
            "なんて紙面で騒がれた日には……\x01",
            "ああ、想像したくないです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_157D")

    label("loc_14AC")


    #C0058
    ChrTalk(
        0xFE,
        (
            "そういえば、\x01",
            "リベールで起こった\x01",
            "例の異変の後……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "王室親衛隊隊長のユリアという方も\x01",
            "随分騒ぎ立てられていましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "写真を見たことがありますが、\x01",
            "あの方も凛々しい方でしたし……\x01",
            "苦労したでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157D")

    Jump("loc_18FE")

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A9")

    #C0061
    ChrTalk(
        0xFE,
        (
            "一昨年までは、\x01",
            "あちらに見えるガレリア要塞から\x01",
            "巨大な列車砲が向けられていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "まさに一触即発の雰囲気で……\x01",
            "再び大きな紛争が起きるのではと\x01",
            "厳戒態勢だったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "不戦条約が締結したおかげで\x01",
            "最近では平和そのものですが……\x01",
            "あの恐ろしさは忘れられません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_174B")

    label("loc_16A9")


    #C0064
    ChrTalk(
        0xFE,
        (
            "一昨年に締結された不戦条約のお陰で、\x01",
            "クロスベルは極度の緊張状態から開放されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "条約を提案したリベールのアリシア女王には\x01",
            "ただ頭が下がるばかりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174B")

    Jump("loc_18FE")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_18FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187A")

    #C0066
    ChrTalk(
        0xFE,
        (
            "あの岩壁に見えるのが、帝国の誇る\x01",
            "《ガレリア要塞》の一角です。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "帝国の軍事力は脅威ですから\x01",
            "いつだって気が抜けません。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#0300Fん～、気を張りすぎてもソンだぜ？\x02\x03",

            "#0304Fマジメなのはいいが、\x01",
            "適度に抜くのも大事だと俺は思うな。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "……ランディ先輩は抜きすぎです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18FE")

    label("loc_187A")


    #C0070
    ChrTalk(
        0xFE,
        (
            "……でも確かに、\x01",
            "緊張しすぎはよくないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "あとでブルードさんと\x01",
            "交代してもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        "#0306F（マジメな奴……）\x02",
    )

    CloseMessageWindow()

    label("loc_18FE")

    TalkEnd(0xFE)
    Return()

    # Function_6_BC0 end

    def Function_7_1902(): pass

    label("Function_7_1902")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1B61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB3")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0073
    ChrTalk(
        0xA,
        (
            "#0805Fうわ～、威圧的……\x02\x03",

            "#0801Fあれが帝国側の国境ね。\x01",
            "今までちゃんと見る機会が\x01",
            "無かったかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "#0901F帝国側の施設は\x01",
            "《ガレリア要塞》だね。\x02\x03",

            "帝国でも最重要軍事拠点の\x01",
            "１つとして配備されてる要塞だよ。\x02\x03",

            "#0903F何といっても……\x01",
            "一番共和国に近い場所だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        (
            "#0806Fそっか、帝国と共和国は\x01",
            "犬猿の仲だもんね。\x02\x03",

            "#0808F……クロスベルってやっぱり\x01",
            "色々抱えちゃってるわね～。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B61")

    label("loc_1AB3")


    #C0076
    ChrTalk(
        0xA,
        (
            "#0805Fあ、ロイド君たちも来てたんだ。\x02\x03",

            "#0806Fこういうのを見ると\x01",
            "改めて帝国の威圧を感じちゃうわね。\x02\x03",

            "#0802F……あたしが知ってる帝国人には\x01",
            "良い人や変な人もいるんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B61")

    TalkEnd(0xFE)
    Return()

    # Function_7_1902 end

    def Function_8_1B65(): pass

    label("Function_8_1B65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B83")
    Call(0, 7)
    Jump("loc_1BED")

    label("loc_1B83")


    #C0077
    ChrTalk(
        0xB,
        (
            "#0904Fはは……\x01",
            "挨拶ついでに、ちょっとね。\x02\x03",

            "#0900Fクロスベルを理解するためには\x01",
            "色々と見ておかないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BED")

    TalkEnd(0xFE)
    Return()

    # Function_8_1B65 end

    def Function_9_1BF1(): pass

    label("Function_9_1BF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7B")

    #C0078
    ChrTalk(
        0xFE,
        (
            "うおーっ！！　高ぇなぁ。\x01",
            "ちょっと足を踏み外したら\x01",
            "谷底にまっさかさまじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xDC, 0x1F4)

    #C0079
    ChrTalk(
        0xFE,
        "……怖ぇえー！！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1CE3")

    label("loc_1C7B")


    #C0080
    ChrTalk(
        0xFE,
        (
            "落ちたら確実に死ぬな。\x01",
            "どれどれ、もう一回見てみよう……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xDC, 0x1F4)

    #C0081
    ChrTalk(
        0xFE,
        "…………やっぱり怖ぇえー！！！\x02",
    )

    CloseMessageWindow()

    label("loc_1CE3")

    TalkEnd(0xFE)
    Return()

    # Function_9_1BF1 end

    def Function_10_1CE7(): pass

    label("Function_10_1CE7")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6670, 11000, 3120, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18620, 0)
    SetChrPos(0x101, 7300, 10000, 2500, 180)
    SetChrPos(0x102, 6000, 10000, 2500, 180)
    SetChrPos(0x103, 7300, 10000, 3800, 180)
    SetChrPos(0x104, 6000, 10000, 3800, 180)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#0000Fさて……\x01",
            "屋上に着いたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#12P#0200Fミレイユ准尉の話では、\x01",
            "ここで思うさま歌ったりしていたとか。\x02\x03",

            "酒の回りがピークに達していた\x01",
            "時間だったと思われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#5P#0106Fどこで失くしたか\x01",
            "覚えていないっていうのが\x01",
            "大きな問題だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#11P#0300Fま、鍵をなくしたとすれば\x01",
            "ここが一番可能性が高そうだ。\x02\x03",

            "一通り調べてみるとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 7300, 10000, 2500, 180)
    OP_29(0x19, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_1CE7 end

    def Function_11_1F04(): pass

    label("Function_11_1F04")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F7E")

    #C0086
    ChrTalk(
        0x101,
        (
            "#0005Fん……\x01",
            "この光るものはもしかして……\x02\x03",

            "#0006F……１０ミラ硬貨だ。\x01",
            "司令が落としたのかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DA")

    label("loc_1F7E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF9")

    #C0087
    ChrTalk(
        0x102,
        (
            "#0105Fあら……\x01",
            "この光るものはもしかして……\x02\x03",

            "#0106F……１０ミラ硬貨ね。\x01",
            "司令が落としたのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DA")

    label("loc_1FF9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206A")

    #C0088
    ChrTalk(
        0x103,
        (
            "#0205Fあ……\x01",
            "この光る物体は……\x02\x03",

            "#0211F……１０ミラ硬貨ですね。\x01",
            "司令の落し物でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DA")

    label("loc_206A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DA")

    #C0089
    ChrTalk(
        0x104,
        (
            "#0305Fん……\x01",
            "この光るモンは……\x02\x03",

            "#0306F……１０ミラ硬貨じゃねえか。\x01",
            "なんだよ、紛らわしいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DA")

    OP_65(0x0, 0x1)
    OP_29(0x19, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2110")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_2110")

    TalkEnd(0xFF)
    Return()

    # Function_11_1F04 end

    def Function_12_2114(): pass

    label("Function_12_2114")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218D")

    #C0090
    ChrTalk(
        0x101,
        (
            "#0005Fおっ……何かあるぞ。\x02\x03",

            "#0006F……缶ジュースのプルトップだ。\x01",
            "あとでゴミ箱に捨てとこう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F2")

    label("loc_218D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2209")

    #C0091
    ChrTalk(
        0x102,
        (
            "#0105Fあっ……何かあるわ。\x02\x03",

            "#0106F……缶ジュースのプルトップね。\x01",
            "あとでゴミ箱に捨てておかないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F2")

    label("loc_2209")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2285")

    #C0092
    ChrTalk(
        0x103,
        (
            "#0205Fあっ……何かあります。\x02\x03",

            "#0203F……缶ジュースのプルトップですね。\x01",
            "あとでゴミ箱に捨てないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F2")

    label("loc_2285")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F2")

    #C0093
    ChrTalk(
        0x104,
        (
            "#0305Fおっ……何かあるぞ。\x02\x03",

            "#0306F……缶ジュースのプルトップかよ。\x01",
            "ガッカリさせんなよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F2")

    OP_29(0x19, 0x1, 0x7)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2328")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_2328")

    TalkEnd(0xFF)
    Return()

    # Function_12_2114 end

    def Function_13_232C(): pass

    label("Function_13_232C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2391")

    #C0094
    ChrTalk(
        0x101,
        (
            "#0005Fこれは……\x02\x03",

            "#0006F……ただの針金か。\x01",
            "うーん、キーは見当たらない……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BE")

    label("loc_2391")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23F5")

    #C0095
    ChrTalk(
        0x102,
        (
            "#0105Fこれは……\x02\x03",

            "#0106F……ただの針金ね。\x01",
            "うーん、キーは見当たらないわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BE")

    label("loc_23F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245D")

    #C0096
    ChrTalk(
        0x103,
        (
            "#0205Fこれは……\x02\x03",

            "#0203F……ただの針金ですか。\x01",
            "キーは見当たらないようですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BE")

    label("loc_245D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24BE")

    #C0097
    ChrTalk(
        0x104,
        (
            "#0305Fお、これは……\x02\x03",

            "#0301F……ただの針金か。\x01",
            "チッ、キーは見当たらねえな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24BE")

    OP_29(0x19, 0x1, 0x8)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24F4")
    Call(0, 15)
    OP_66(0x4, 0x1)

    label("loc_24F4")

    TalkEnd(0xFF)
    Return()

    # Function_13_232C end

    def Function_14_24F8(): pass

    label("Function_14_24F8")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -10400, 10000, -650, 270)
    SetChrPos(0x102, -10400, 10000, 650, 270)
    SetChrPos(0x103, -9400, 10000, -1300, 270)
    SetChrPos(0x104, -9400, 10000, 1300, 270)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(-29750, 13600, 710, 0)
    MoveCamera(256, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(35900, 0)
    SetCameraDistance(45900, 5000)
    OP_6F(0x10)

    #C0098
    ChrTalk(
        0x101,
        "#5P#0005Fあれは……帝国方面の国境トンネルか。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#11P#0103Fええ、そうよ。\x02\x03",

            "#0101F正確には、あのトンネルを含めた\x01",
            "岩壁と一体化した要塞都市を\x01",
            "《ガレリア要塞》というのだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        (
            "#5P#0208F帝国最東端の要塞にして\x01",
            "共和国を牽制するための防波堤……\x02\x03",

            "#0206Fこうして眺めていると……\x01",
            "何故か物凄い威圧感を感じます。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-9200, 11500, -580, 0)
    MoveCamera(294, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19210, 0)
    OP_68(-9200, 11500, -580, 0)
    MoveCamera(294, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17710, 0)
    OP_0D()

    def lambda_2724():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2724)
    Sleep(300)

    #C0101
    ChrTalk(
        0x104,
        (
            "#11P#0304Fハハ、ティオすけが\x01",
            "そう感じるのも無理はねぇ。\x02\x03",

            "#0301Fあの壁にはな、『列車砲』っていう\x01",
            "とんでもねぇものが隠れてやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_27BE():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27BE)

    def lambda_27CB():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27CB)

    def lambda_27D8():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27D8)
    Sleep(300)

    #C0102
    ChrTalk(
        0x101,
        (
            "#5P#0005F列車砲……\x01",
            "どこかで聞いたことがあるような。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#11P#0303F帝国軍の誇る最強兵器のひとつだ。\x02\x03",

            "#0301F８０リジュ砲弾を撃ち出す\x01",
            "化物じみた大砲だって話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        (
            "#6P#0201Fなるほど……\x01",
            "ラインフォルト社の戦略兵器ですか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28CD():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28CD)
    Sleep(300)

    #C0105
    ChrTalk(
        0x102,
        (
            "#11P#0103F２年ほど前……\x01",
            "帝国・共和国間の緊張は\x01",
            "ピークに達していたわ。\x02\x03",

            "#0101F両国が大規模な演習をする中、\x01",
            "向こうに見えるゲートは開放され、\x01",
            "２門の巨大な列車砲が現れていたの。\x02\x03",

            "#0108Fクロスベル市までも射程に捉えた\x01",
            "兵器がもし使われていたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#6P#0006F……大惨事は免れない所だったわけか。\x02\x03",

            "#0008F（取り寄せてたクロスベルタイムズには\x01",
            "  そこまで書かれていなかった……）\x02\x03",

            "#0013F（でもまさか、そこまで\x01",
            "  危機的な状況だったなんて……）\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#11P#0304Fま、列車砲も\x01",
            "今じゃ見ての通り収められてる。\x02\x03",

            "#0300F《不戦条約》を締結させた\x01",
            "リベールの女王サマのおかげかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ……\x01",
            "立派な方だとは聞いていたけど\x01",
            "正直、認識を改めたよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    #C0109
    ChrTalk(
        0x101,
        (
            "#6P#0005F……っと、つい話し込んじゃったな。\x01",
            "起動キーの捜索を再開しないと。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x9)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E0C")

    #C0110
    ChrTalk(
        0x102,
        (
            "#11P#0105Fうーん、でも……\x01",
            "もう屋上の怪しい場所は\x01",
            "大体探しちゃったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x104,
        (
            "#11P#0306F司令がここにいたのは\x01",
            "間違いないハズなんだがなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        (
            "#6P#0203F屋上に落ちている、という前提が\x01",
            "間違っているのかもしれません。\x02\x03",

            "#0200Fもしそうなら\x01",
            "きっとすでに警備隊員が\x01",
            "見つけているでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#6P#0003Fさっきディーター総裁に言われたように、\x01",
            "視点を変えたほうがよさそうだな。\x02\x03",

            "#0001Fもしかしたら……普通に拾える場所には\x01",
            "落ちていないのかもしれない。\x02\x03",

            "もう一度隅々まで調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_66(0x4, 0x1)
    OP_29(0x19, 0x1, 0x1F)

    label("loc_2E0C")

    OP_5A()
    SetChrPos(0x0, -10400, 10000, -650, 270)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_14_24F8 end

    def Function_15_2E29(): pass

    label("Function_15_2E29")


    #C0114
    ChrTalk(
        0x102,
        "#0105Fうーん、見つからないわね……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        (
            "#0306F司令がここにいたのは\x01",
            "間違いないハズなんだがなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        (
            "#0203F屋上に落ちている、という前提が\x01",
            "間違っているのかもしれません。\x02\x03",

            "#0200Fもしそうなら\x01",
            "きっとすでに警備隊員が\x01",
            "見つけているでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0003Fさっきディーター総裁に言われたように、\x01",
            "視点を変えたほうがよさそうだな。\x02\x03",

            "#0001Fもしかしたら……普通に拾える場所には\x01",
            "落ちていないのかもしれない。\x02\x03",

            "もう一度隅々まで調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x1F)
    Return()

    # Function_15_2E29 end

    def Function_16_2FDC(): pass

    label("Function_16_2FDC")

    EventBegin(0x0)
    LoadEffect(0x9, "event\\eva00_00.eff")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15330, 11000, 4890, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 15000, 10000, 4700, 90)
    SetChrPos(0x102, 15000, 10000, 3400, 90)
    SetChrPos(0x103, 15000, 10000, 2100, 90)
    SetChrPos(0x104, 15000, 10000, 800, 90)
    SetCameraDistance(19000, 2000)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0118
    ChrTalk(
        0x101,
        "#5P#0001F…………ん？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0119
    ChrTalk(
        0x103,
        "#5P#0205F……ロイドさん？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#5P#0105Fなに、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#5P#0005F……あった……！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(24460, 11000, 1930, 3000)
    MoveCamera(310, 33, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(15440, 3000)
    OP_6F(0x79)
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 19510, 7000, 5830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(860, 0, 100, 0)
    Sleep(3000)

    #C0122
    ChrTalk(
        0x104,
        (
            "#5P#0306F#Nおいおい、マジかよ……\x01",
            "あんなところに引っかかってるとは。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0123
    ChrTalk(
        0x103,
        (
            "#5P#0206F#N道理で、門の内部を探しても\x01",
            "見つからない訳ですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0124
    ChrTalk(
        0x101,
        (
            "#5P#0000F#Nと、とにかく准尉に報告しよう。\x02\x03",

            "梯子か何かを借りてくれば\x01",
            "回収できるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0125
    ChrTalk(
        0x102,
        "#5P#0100F#Nそうね、行きましょう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2FDC end

    SaveToFile()

Try(main)
