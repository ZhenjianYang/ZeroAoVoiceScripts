from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0600.bin",                # FileName
        "t0600",                    # MapName
        "t0600",                    # Location
        0x0069,                     # MapIndex
        "ed7301",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x20,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 105, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0600",                  # 0
        "鉱山長ホフマン",         # 1
        "鉱員マルロ",             # 2
        "鉱員ガンツ",             # 3
        "鉱員ロージー",           # 4
        "鉱員マックス",           # 5
        "アレク",                 # 6
    ))

    AddCharChip((
        "chr/ch26300.itc",                   # 00
        "chr/ch26200.itc",                   # 01
        "chr/ch30700.itc",                   # 02
        "chr/ch23000.itc",                   # 03
    ))

    DeclNpc(-31850,  0,       32080,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4139,    0,       6690,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-11470,  0,       15090,   19,   261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-17250,  50,      30370,   180,  261,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(-28860,  0,       56150,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclActor(132500,  0,       18000,   1200,    132500,  1750,    18000,   0x007C, 0,  4,  0x0000)
    DeclActor(-22540,  0,       54760,   1200,    -22540,  1500,    54760,   0x007C, 0,  11, 0x0000)

    ChipFrameInfo(452, 0)                                        # 0

    ScpFunction((
        "Function_0_1C4",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_2A7",          # 02, 2
        "Function_3_38F",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_457",          # 05, 5
        "Function_6_E65",          # 06, 6
        "Function_7_181B",         # 07, 7
        "Function_8_1DCD",         # 08, 8
        "Function_9_2792",         # 09, 9
        "Function_10_2FA3",        # 0A, 10
        "Function_11_3134",        # 0B, 11
    ))


    def Function_0_1C4(): pass

    label("Function_0_1C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_210"),
        (2, "loc_21C"),
        (3, "loc_228"),
        (4, "loc_234"),
        (5, "loc_240"),
        (6, "loc_24C"),
        (SWITCH_DEFAULT, "loc_258"),
    )


    label("loc_204")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_210")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_21C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_228")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_234")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_240")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_24C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_27B")

    Return()

    # Function_0_1C4 end

    def Function_1_27C(): pass

    label("Function_1_27C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A6")
    OP_94(0xFE, 0xFFFFA7FE, 0x7F4E, 0xFFFFC3B0, 0x6AA4, 0x3E8)
    Sleep(300)
    Jump("Function_1_27C")

    label("loc_2A6")

    Return()

    # Function_1_27C end

    def Function_2_2A7(): pass

    label("Function_2_2A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B5")
    Jump("loc_38E")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2C3")
    Jump("loc_38E")

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2D1")
    Jump("loc_38E")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DF")
    Jump("loc_38E")

    label("loc_2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2ED")
    Jump("loc_38E")

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FB")
    Jump("loc_38E")

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30E")
    SetChrFlags(0xA, 0x80)
    Jump("loc_38E")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31C")
    Jump("loc_38E")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_343")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_38E")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36C")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -400, 50, 3770, 0)
    Jump("loc_38E")

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_38E")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E")
    SetChrFlags(0xC, 0x10)

    label("loc_38E")

    Return()

    # Function_2_2A7 end

    def Function_3_38F(): pass

    label("Function_3_38F")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -22700, 0, 54850, 10000, 2000, 45000)
    Return()

    # Function_3_38F end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『導力車フリークvol.1』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36E, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_453")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『チャームカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36E, 1)

    label("loc_453")

    TalkEnd(0xFF)
    Return()

    # Function_4_3AD end

    def Function_5_457(): pass

    label("Function_5_457")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_537")

    #C0003
    ChrTalk(
        0xFE,
        (
            "町長と相談して、\x01",
            "鉱山を再開することにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "マインツって町が前に進むには、\x01",
            "やっぱり鉱山の存在は欠かせねえ……\x01",
            "そう思ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……へへ、久しぶりの穴掘りだ。\x01",
            "気合入れてくぞ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_564")

    label("loc_537")


    #C0006
    ChrTalk(
        0xFE,
        (
            "久しぶりの穴掘りだ、\x01",
            "気合入れてくぞ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_564")

    Jump("loc_E61")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_577")
    Jump("loc_E61")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_585")
    Jump("loc_E61")

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_690")

    #C0007
    ChrTalk(
        0xFE,
        (
            "マインツが占領されたとき、\x01",
            "俺らで猟兵のヤツらを\x01",
            "追い出そうとしたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "立ち向かったら\x01",
            "簡単にぶっ飛ばされて、\x01",
            "ちっと腰を痛めちまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "大したケガじゃなかったが、\x01",
            "ムチャしすぎだってミランダに\x01",
            "こっぴどく怒られちまったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_724")

    label("loc_690")


    #C0010
    ChrTalk(
        0xFE,
        (
            "ちっと腰を痛めちまったが、\x01",
            "立ち向かったこと自体は\x01",
            "何にも後悔してねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "とにかく、他の鉱員や\x01",
            "町のやつらがケガしなくて\x01",
            "本当によかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_724")

    Jump("loc_E61")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_90D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87D")

    #C0012
    ChrTalk(
        0xFE,
        (
            "落盤なんかの事故や\x01",
            "魔獣が発生する鉱山では、\x01",
            "鉱員の仕事は命がけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "そんな仕事を続けるにゃあ、\x01",
            "互いの信頼やこの仕事への誇りが\x01",
            "一番重要になってくんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "最近、鉱員たちが良い感じに\x01",
            "まとまってるのは、その辺が\x01",
            "分かってきたって事だろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "へへ、こんな仲間に囲まれて、\x01",
            "鉱山長冥利に尽きるってもんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_908")

    label("loc_87D")


    #C0016
    ChrTalk(
        0xFE,
        (
            "鉱員ってのはある意味\x01",
            "命がけの仕事だからな。\x01",
            "互いの信頼が重要なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "へへ、こんな仲間に囲まれて、\x01",
            "鉱山長冥利に尽きるってもんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_908")

    Jump("loc_E61")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C7")

    #C0018
    ChrTalk(
        0xFE,
        (
            "マルロのやつ、\x01",
            "今日は妙に元気があるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "昨日までは世界の終わりみたいな\x01",
            "顔してやがったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "まあ、ちゃんと働いてるうちは\x01",
            "なにも文句はねえがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A52")

    label("loc_9C7")


    #C0021
    ChrTalk(
        0xFE,
        (
            "マルロのやつ、昨日までとは\x01",
            "打って変わって俄然やる気だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "うーむ、よく分からんが……\x01",
            "ちゃんと働いてるうちは\x01",
            "なにも文句はねえよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A52")

    Jump("loc_E61")

    label("loc_A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFA")

    #C0023
    ChrTalk(
        0xFE,
        (
            "最近、マルロのやつが\x01",
            "どうも仕事に集中できない\x01",
            "らしくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "気分転換に飲みに誘っても\x01",
            "断りやがるし……\x01",
            "いったいなんだってんだ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B5E")

    label("loc_AFA")


    #C0025
    ChrTalk(
        0xFE,
        (
            "そういえばガンツのやつ、\x01",
            "やけに休憩が長いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "ったく、どいつもこいつも\x01",
            "タルんでやがるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5E")

    Jump("loc_E61")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7")

    #C0027
    ChrTalk(
        0xFE,
        (
            "確か、今日はアレクが\x01",
            "日曜学校の日だったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "ベッカライさんとこの\x01",
            "キミィと一緒に、\x01",
            "よく勉強してほしいもんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C59")

    label("loc_BF7")


    #C0029
    ChrTalk(
        0xFE,
        (
            "俺ら鉱員ときたら\x01",
            "学がねえヤツばっかだからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "アレクたちには\x01",
            "よく勉強してほしいもんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C59")

    Jump("loc_E61")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C6C")
    Jump("loc_E61")

    label("loc_C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1A")

    #C0031
    ChrTalk(
        0xFE,
        "（グウウウ……）\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……ああ、いけねえ。\x01",
            "そういや弁当を持ってくるのを\x01",
            "忘れちまってたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "キリのいいとこまで\x01",
            "仕事したら取りにいくか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D82")

    label("loc_D1A")


    #C0034
    ChrTalk(
        0xFE,
        (
            "弁当を持ってくるのを\x01",
            "うっかり忘れちまってたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "キリのいいとこまで\x01",
            "仕事したら取りにいくか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D82")

    Jump("loc_E61")

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E20")

    #C0036
    ChrTalk(
        0xFE,
        (
            "旧鉱山の事は気になるが……\x01",
            "鉱員は穴掘ってなんぼだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "あっちはガンツと町長に任せたし、\x01",
            "俺たちは仕事に専念しねえとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E61")

    label("loc_E20")


    #C0038
    ChrTalk(
        0xFE,
        (
            "鉱員は穴掘ってなんぼだ。\x01",
            "何があろうと仕事に専念しねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E61")

    TalkEnd(0xFE)
    Return()

    # Function_5_457 end

    def Function_6_E65(): pass

    label("Function_6_E65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")

    #C0039
    ChrTalk(
        0xFE,
        (
            "異常事態で大変なときだけど……\x01",
            "俺たちが精一杯頑張って、\x01",
            "マインツを盛り上げないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "はは、そしたらいつか\x01",
            "リュッカちゃんが振り向いて\x01",
            "くれる日も来るかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F81")

    label("loc_F27")


    #C0041
    ChrTalk(
        0xFE,
        (
            "異常事態で大変なときだけど……\x01",
            "俺たちが精一杯頑張って、\x01",
            "マインツを盛り上げないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F81")

    Jump("loc_1817")

    label("loc_F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_F94")
    Jump("loc_1817")

    label("loc_F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_FA2")
    Jump("loc_1817")

    label("loc_FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_111C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1083")

    #C0042
    ChrTalk(
        0xFE,
        (
            "やっと昨日から、マインツ鉱山も\x01",
            "穴掘りを再開したとこだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "クロスベルのこれからについて\x01",
            "色々と考えちまうけど……\x01",
            "とにかく体を動かすだけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "俺たち鉱員は穴掘りくらいしか\x01",
            "できねえからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1117")

    label("loc_1083")


    #C0045
    ChrTalk(
        0xFE,
        (
            "酒場のリュッカちゃんも、\x01",
            "町が占領されたときは\x01",
            "相当怖がってたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "俺には穴掘りくらいしか\x01",
            "できないけど……\x01",
            "早く元気になってほしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1117")

    Jump("loc_1817")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11A4")

    #C0047
    ChrTalk(
        0xFE,
        (
            "ガンツのおかげで\x01",
            "仕事に集中できるように\x01",
            "なったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "お礼代わりに、\x01",
            "今夜の飲み代くらいは\x01",
            "俺がおごってやるかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1817")

    label("loc_11A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1311")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1288")

    #C0049
    ChrTalk(
        0xFE,
        (
            "昨日、ガンツが無理やり俺を\x01",
            "酒場に引っ張っていってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "そしたら、リュッカちゃんが\x01",
            "最近元気のない俺を\x01",
            "励ましてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "はあ、どうやら嫌われて\x01",
            "なかったみたいだな……\x01",
            "ほんとよかったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_130C")

    label("loc_1288")


    #C0052
    ChrTalk(
        0xFE,
        (
            "リュッカちゃんが\x01",
            "最近元気のない俺を\x01",
            "励ましてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "はあ、どうやら嫌われて\x01",
            "なかったみたいだな……\x01",
            "ほんとよかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130C")

    Jump("loc_1817")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1457")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DE")

    #C0054
    ChrTalk(
        0xFE,
        (
            "はあ……\x01",
            "なんだか何にもやる気が出ないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "リュッカちゃんに\x01",
            "嫌われちまってるだろうから\x01",
            "酒場にも顔を出しづらいし……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "今日はもうさっさと\x01",
            "上がらしてもらおうかなあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1452")

    label("loc_13DE")


    #C0057
    ChrTalk(
        0xFE,
        (
            "リュッカちゃんに\x01",
            "嫌われちまってるだろうから\x01",
            "酒場にも顔を出しづらいし……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "はあ……仕事にも身が入らないぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_1452")

    Jump("loc_1817")

    label("loc_1457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1548")

    #C0059
    ChrTalk(
        0xFE,
        (
            "宴会の時、なんでリュッカちゃんに\x01",
            "あんなこと言っちまったんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "ガン無視されちまったし、\x01",
            "そもそも酒に任せて言った感じが\x01",
            "余計にかっこ悪いっつーか……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "あ～……昨夜の俺を\x01",
            "百発くらい殴ってやりたい……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15B6")

    label("loc_1548")


    #C0062
    ChrTalk(
        0xFE,
        (
            "あの様子じゃリュッカちゃんに\x01",
            "嫌われちまったかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "あ～……昨夜の俺を\x01",
            "百発くらい殴ってやりたい……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B6")

    Jump("loc_1817")

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15C9")
    Jump("loc_1817")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168C")

    #C0064
    ChrTalk(
        0xFE,
        (
            "ん、ガンツなら今\x01",
            "町長んとこに行ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "……はあ、それにしても\x01",
            "昨日のリュッカちゃん\x01",
            "かわいかったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "あの笑顔のためだったら、\x01",
            "何でもできちゃうかも。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16EA")

    label("loc_168C")


    #C0067
    ChrTalk(
        0xFE,
        (
            "……あれ、あの子……\x01",
            "鉱山長の息子じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "こんなトコに一人で\x01",
            "なにしにきたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EA")

    Jump("loc_1817")

    label("loc_16EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A2")

    #C0069
    ChrTalk(
        0xFE,
        (
            "最近、ガンツが前向きでな。\x01",
            "愚痴ばっか言ってた頃とは\x01",
            "えらい違いだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "例の教団事件に巻き込まれて、\x01",
            "俺たちに心配かけてたのが\x01",
            "効いたみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1817")

    label("loc_17A2")


    #C0071
    ChrTalk(
        0xFE,
        (
            "酒とギャンブルに\x01",
            "付き合わされるのは\x01",
            "相変わらずだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "幼馴染だし、そのくらいは\x01",
            "大目に見てやんなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1817")

    TalkEnd(0xFE)
    Return()

    # Function_6_E65 end

    def Function_7_181B(): pass

    label("Function_7_181B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D0")

    #C0073
    ChrTalk(
        0xFE,
        (
            "街に行けるようになったし\x01",
            "カジノに繰り出すのも\x01",
            "悪くないと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "やっぱり今は仕事を\x01",
            "がんばらなくっちゃあな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "おーし、やってやるぜ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_191D")

    label("loc_18D0")


    #C0076
    ChrTalk(
        0xFE,
        (
            "仕事が終わったら、\x01",
            "思う存分カジノで遊ぶぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "おーし、やってやるぜ！\x02",
    )

    CloseMessageWindow()

    label("loc_191D")

    Jump("loc_1DC9")

    label("loc_1922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1930")
    Jump("loc_1DC9")

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_193E")
    Jump("loc_1DC9")

    label("loc_193E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5F")

    #C0078
    ChrTalk(
        0xFE,
        (
            "マインツを占領した猟兵どもの\x01",
            "リーダー格の娘、なんだか見覚えが\x01",
            "あると思ってたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "以前マインツで大粒の七耀石を\x01",
            "大量に仕入れてった連中の\x01",
            "中にいた女の子だったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "あんな女の子が警備隊を\x01",
            "ボロボロにしちまうなんて……\x01",
            "今でも信じられねえよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1ACF")

    label("loc_1A5F")


    #C0081
    ChrTalk(
        0xFE,
        (
            "あんな女の子が警備隊を\x01",
            "ボロボロにしちまうなんて……\x01",
            "今でも信じられねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "まさに、悪夢ってやつだぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_1ACF")

    Jump("loc_1DC9")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9E")

    #C0083
    ChrTalk(
        0xFE,
        (
            "今朝、こーんなでっけえ\x01",
            "蒼耀石の結晶を掘り当てたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "へへ、なんだか最近は\x01",
            "仕事も絶好調な感じだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "この調子でギャンブルのツキも\x01",
            "向いてきたらいいんだけどよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C12")

    label("loc_1B9E")


    #C0086
    ChrTalk(
        0xFE,
        (
            "へへ、なんだか最近は\x01",
            "仕事も絶好調な感じだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "この調子でギャンブルのツキも\x01",
            "向いてきたらいいんだけどよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C12")

    Jump("loc_1DC9")

    label("loc_1C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C82")

    #C0088
    ChrTalk(
        0xFE,
        (
            "どうやらマルロのやつも\x01",
            "元気をとりもどしたみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "へへ、世話の焼けるヤツだよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DC9")

    label("loc_1C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C90")
    Jump("loc_1DC9")

    label("loc_1C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D31")

    #C0090
    ChrTalk(
        0xFE,
        (
            "マルロのやつ、\x01",
            "昨日の宴会が終わってから\x01",
            "元気がねえんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "……よっしゃ。\x01",
            "ここは幼馴染のオレが\x01",
            "一肌脱いでやるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D9F")

    label("loc_1D31")


    #C0092
    ChrTalk(
        0xFE,
        (
            "マルロには、教団事件のときに\x01",
            "大分心配かけたからな……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "ここは幼馴染のオレが\x01",
            "一肌脱いでやるとすっか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9F")

    Jump("loc_1DC9")

    label("loc_1DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1DB2")
    Jump("loc_1DC9")

    label("loc_1DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DC0")
    Jump("loc_1DC9")

    label("loc_1DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1DC9")

    label("loc_1DC9")

    TalkEnd(0xFE)
    Return()

    # Function_7_181B end

    def Function_8_1DCD(): pass

    label("Function_8_1DCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA4")

    #C0094
    ChrTalk(
        0xFE,
        (
            "再開したら再開したで、\x01",
            "めんどいのは違いないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "やっぱり、鉱山で働いてないと\x01",
            "どうにも気持ち悪かったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "はは、俺の体にも鉱員って仕事が\x01",
            "染み付いちゃったんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1F24")

    label("loc_1EA4")


    #C0097
    ChrTalk(
        0xFE,
        (
            "やっぱり、鉱山で働いてないと\x01",
            "どうにも気持ち悪かったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "はは、俺の体にも鉱員って仕事が\x01",
            "染み付いちゃったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F24")

    Jump("loc_278E")

    label("loc_1F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1F37")
    Jump("loc_278E")

    label("loc_1F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F45")
    Jump("loc_278E")

    label("loc_1F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_209F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202A")

    #C0099
    ChrTalk(
        0xFE,
        (
            "占領事件が解決したかと思ったら、\x01",
            "今度は街の襲撃事件なんてのが\x01",
            "起こっちまうなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "マインツやクロスベル市のために\x01",
            "できる事をしてかねえと……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "……でも、オレなんかに\x01",
            "何ができるってんだ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_209A")

    label("loc_202A")


    #C0102
    ChrTalk(
        0xFE,
        (
            "マインツやクロスベル市のために\x01",
            "できる事をしてかねえと……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "……でも、オレなんかに\x01",
            "何ができるってんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209A")

    Jump("loc_278E")

    label("loc_209F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2137")

    #C0104
    ChrTalk(
        0xFE,
        (
            "雨が降ると、\x01",
            "坑道の中も寒くなって\x01",
            "ヤなかんじだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "まー、体動かしてたら\x01",
            "あったまってくるんだけどな。\x01",
            "めんどくせえったらないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278E")

    label("loc_2137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_22B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223C")

    #C0106
    ChrTalk(
        0xFE,
        (
            "最近、婆ちゃんが\x01",
            "嫁を連れてこいとか\x01",
            "言うようになってさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "オレがサボらなくなって\x01",
            "喜んでくれるのはいいんだけど、\x01",
            "正直めんどくさいんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "鉱山長やマックス先輩みたいな\x01",
            "甲斐性はないし、\x01",
            "１人の方が気楽でいいんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22B0")

    label("loc_223C")


    #C0109
    ChrTalk(
        0xFE,
        (
            "嫁を連れてこいだなんて、\x01",
            "婆ちゃんも面倒なこと言うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "１人の方が気楽だし、\x01",
            "そういうのはアミーに任せるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B0")

    Jump("loc_278E")

    label("loc_22B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2405")

    #C0111
    ChrTalk(
        0xFE,
        (
            "さっき外で休憩してたら、\x01",
            "鉱山長の息子が話しかけてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "『鉱員の仕事は楽しい？』なんて\x01",
            "聞いてきたけど、めんどいから\x01",
            "適当にあしらっちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "……そういえば前に、\x01",
            "同じようなことをして\x01",
            "落ち込ませちゃったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "はあ、悪い癖だな。\x01",
            "ちっとは夢のあることを\x01",
            "言ってやればよかったかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_247C")

    label("loc_2405")


    #C0115
    ChrTalk(
        0xFE,
        (
            "鉱山長の息子って、\x01",
            "鉱員を目指してるみたい\x01",
            "なんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "ちっとは夢のあることを\x01",
            "言ってやればよかったかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247C")

    Jump("loc_278E")

    label("loc_2481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_260B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2581")

    #C0117
    ChrTalk(
        0xFE,
        (
            "一日休んだだけなのに、\x01",
            "どうも休みボケしちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "サボり生活も長かったからなー。\x01",
            "どうも体がついていかないっつーか、\x01",
            "めんどくせえっつーか……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "まあ、ちゃんと働くけどね。\x01",
            "前みたいなサボリ魔に\x01",
            "戻っちまうのもなんだし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2606")

    label("loc_2581")


    #C0120
    ChrTalk(
        0xFE,
        (
            "一日休んだだけなのに、\x01",
            "どうも休みボケしちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "まあ、ちゃんと働くけどね。\x01",
            "前みたいなサボリ魔に\x01",
            "戻っちまうのもなんだし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2606")

    Jump("loc_278E")

    label("loc_260B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2619")
    Jump("loc_278E")

    label("loc_2619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")

    #C0122
    ChrTalk(
        0xFE,
        (
            "最近、仕事の後の麦酒のウマさが\x01",
            "分かっちゃってさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "正直いって面倒くさいんだけど、\x01",
            "サボらずに働くことが多くなったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "……まあ、婆ちゃんも\x01",
            "喜んでくれるし、いいんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2780")

    label("loc_26EF")


    #C0125
    ChrTalk(
        0xFE,
        (
            "最近、仕事の後の麦酒のウマさが\x01",
            "分かっちゃってさ……\x01",
            "あんまりサボらなくなったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "……まあ、婆ちゃんも\x01",
            "喜んでくれるし、いいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2780")

    Jump("loc_278E")

    label("loc_2785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_278E")

    label("loc_278E")

    TalkEnd(0xFE)
    Return()

    # Function_8_1DCD end

    def Function_9_2792(): pass

    label("Function_9_2792")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_28B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2858")

    #C0127
    ChrTalk(
        0xFE,
        (
            "はは、久しぶりの鉱山で\x01",
            "みんなノリにノッてるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "……うおー、俺もみなぎってきた！\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "掘って掘って、掘りまくって……\x01",
            "それこそが俺たち鉱員ってもんだぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_28AF")

    label("loc_2858")


    #C0130
    ChrTalk(
        0xFE,
        (
            "ひっさびさの穴掘りだ。\x01",
            "張り切っていくとするぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        "うおー、みなぎってきたあー！\x02",
    )

    CloseMessageWindow()

    label("loc_28AF")

    Jump("loc_2F9F")

    label("loc_28B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_28C2")
    Jump("loc_2F9F")

    label("loc_28C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_28D0")
    Jump("loc_2F9F")

    label("loc_28D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2977")

    #C0132
    ChrTalk(
        0xFE,
        (
            "町をあんな奴らに\x01",
            "占拠されちまうなんて……\x01",
            "鉱員の名折れだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "ちくしょう、猟兵のやつら\x01",
            "次に来やがったら\x01",
            "絶対にただじゃおかねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A0A")

    label("loc_2977")


    #C0134
    ChrTalk(
        0xFE,
        (
            "マインツを占領しただけじゃなく、\x01",
            "クロスベル市までめちゃくちゃに\x01",
            "しやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "猟兵のやつら、次に来やがったら\x01",
            "絶対にただじゃおかねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A0A")

    Jump("loc_2F9F")

    label("loc_2A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A95")

    #C0136
    ChrTalk(
        0xFE,
        (
            "もうそろそろ目標の地層まで\x01",
            "掘り進められそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "へへ、七耀石の山は目の前だ。\x01",
            "気合入れて掘りまくるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9F")

    label("loc_2A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B1D")

    #C0138
    ChrTalk(
        0xFE,
        (
            "よーし、今日も\x01",
            "ガンガン採掘していかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "へへ、どーせだから明日のノルマまで\x01",
            "一気に達成しちまうとするか！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9F")

    label("loc_2B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C36")

    #C0140
    ChrTalk(
        0xFE,
        (
            "最近出るっつう\x01",
            "得体の知れない大型魔獣とやらに、\x01",
            "カミさんがえらく心配しててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "俺たちは鉱山に湧く魔獣で\x01",
            "慣れてるんだ、そんなに\x01",
            "心配する事もないと思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……とはいえ、俺は大分前に\x01",
            "軍用犬に襲われてケガしたし、\x01",
            "エラそうには言えねえか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CA6")

    label("loc_2C36")


    #C0143
    ChrTalk(
        0xFE,
        (
            "まあ、得体の知れない魔獣には\x01",
            "気をつけとくとするさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "万が一でも、カミさんを\x01",
            "悲しませたくはないからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA6")

    Jump("loc_2F9F")

    label("loc_2CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB2")

    #C0145
    ChrTalk(
        0xFE,
        (
            "昨日は、俺と鉱山長で\x01",
            "昼間からダラダラ\x01",
            "飲んでたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "夜からはカジノ帰りの\x01",
            "ガンツたちも参加してな。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "せっかくだからロージーも\x01",
            "呼び出して、ちょっとした\x01",
            "大宴会になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "やっぱ仲間同士で飲む酒は\x01",
            "サイコーだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E12")

    label("loc_2DB2")


    #C0149
    ChrTalk(
        0xFE,
        (
            "昨日は、鉱員連中総出の\x01",
            "大宴会になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "やっぱ仲間同士で飲む酒は\x01",
            "サイコーだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E12")

    Jump("loc_2F9F")

    label("loc_2E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E25")
    Jump("loc_2F9F")

    label("loc_2E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2EB6")

    #C0151
    ChrTalk(
        0xFE,
        (
            "ロージーのやつ、\x01",
            "やる気が出てきたのはいいんだが\x01",
            "仕事の技量はまだまだだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "ここは先輩として、\x01",
            "しっかり教えてやんねえとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9F")

    label("loc_2EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2F9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F60")

    #C0153
    ChrTalk(
        0xFE,
        (
            "カミさんのためなら\x01",
            "え～んやこ～ら♪\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "マインツのためなら\x01",
            "え～んやこ～ら♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    #C0155
    ChrTalk(
        0xFE,
        (
            "へへ、今日も一日\x01",
            "がんばって採掘しねえとな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_2F9F")

    label("loc_2F60")


    #C0156
    ChrTalk(
        0xFE,
        (
            "カミさんとこの町のために\x01",
            "今日もがんばって採掘しねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2792 end

    def Function_10_2FA3(): pass

    label("Function_10_2FA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FB4")
    Jump("loc_3130")

    label("loc_2FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FC2")
    Jump("loc_3130")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FD0")
    Jump("loc_3130")

    label("loc_2FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FDE")
    Jump("loc_3130")

    label("loc_2FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FEC")
    Jump("loc_3130")

    label("loc_2FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FFA")
    Jump("loc_3130")

    label("loc_2FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3127")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B0")

    #C0157
    ChrTalk(
        0xFE,
        (
            "わあ、鉱山の中って\x01",
            "こんなふうになってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "暗くて広くて……\x01",
            "オバケとかでてきそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "さてと、お父さんはどこかな。\x01",
            "探検してみようっと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3122")

    label("loc_30B0")


    #C0160
    ChrTalk(
        0xFE,
        (
            "お父さんが働いているのを\x01",
            "一回見てみたかったんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "さーて、どこにいるのかな～。\x01",
            "探検してみようっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3122")

    Jump("loc_3130")

    label("loc_3127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3130")

    label("loc_3130")

    TalkEnd(0xFE)
    Return()

    # Function_10_2FA3 end

    def Function_11_3134(): pass

    label("Function_11_3134")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は頑丈な鎖で閉じられている。\x01",
            "どうやら向こうは廃坑のようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_11_3134 end

    SaveToFile()

Try(main)
