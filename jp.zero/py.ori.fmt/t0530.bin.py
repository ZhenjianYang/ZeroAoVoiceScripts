from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0530.bin",                # FileName
        "t0530",                    # MapName
        "t0530",                    # Location
        0x0040,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0530",                  # 0
        "ベッカライ",             # 1
        "キミィ",                 # 2
        "ハロルド",               # 3
        "エステル",               # 4
        "ヨシュア",               # 5
        "観光客ルティーナ",       # 6
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch22700.itc",                   # 02
        "chr/ch09300.itc",                   # 03
        "chr/ch00600.itc",                   # 04
        "chr/ch00700.itc",                   # 05
        "chr/ch34300.itc",                   # 06
    ))

    DeclNpc(-129,    0,       3640,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-4530,   0,       4500,    320,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4670,    0,       1279,    135,  405,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4409,    0,       -839,    0,    405,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(5500,    0,       -180,    315,  405,  0x0, 0,   5,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(5539,    0,       750,     45,   389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(-40,     0,       2120,    1000,    -130,    1500,    3640,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_1A4",          # 00, 0
        "Function_1_25C",          # 01, 1
        "Function_2_2A4",          # 02, 2
        "Function_3_2D8",          # 03, 3
        "Function_4_2DC",          # 04, 4
        "Function_5_10AC",         # 05, 5
        "Function_6_181A",         # 06, 6
        "Function_7_18F5",         # 07, 7
        "Function_8_19C4",         # 08, 8
        "Function_9_1C4D",         # 09, 9
    ))


    def Function_0_1A4(): pass

    label("Function_0_1A4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1E4"),
        (1, "loc_1F0"),
        (2, "loc_1FC"),
        (3, "loc_208"),
        (4, "loc_214"),
        (5, "loc_220"),
        (6, "loc_22C"),
        (SWITCH_DEFAULT, "loc_238"),
    )


    label("loc_1E4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1F0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1FC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_208")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_214")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_220")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_22C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_238")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_25B")

    Return()

    # Function_0_1A4 end

    def Function_1_25C(): pass

    label("Function_1_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_290")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_290")
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xC, 0xB, 0)

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A3")
    ClearChrFlags(0xD, 0x80)

    label("loc_2A3")

    Return()

    # Function_1_25C end

    def Function_2_2A4(): pass

    label("Function_2_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_2D7")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D7")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_2D7")

    Return()

    # Function_2_2A4 end

    def Function_3_2D8(): pass

    label("Function_3_2D8")

    Call(0, 4)
    Return()

    # Function_3_2D8 end

    def Function_4_2DC(): pass

    label("Function_4_2DC")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_347")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_366")
    OP_AF(0x56)
    Jump("loc_388")

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_376")
    OP_AF(0x55)
    Jump("loc_388")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_386")
    OP_AF(0x57)
    Jump("loc_388")

    label("loc_386")

    OP_AF(0x55)

    label("loc_388")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A3")

    label("loc_397")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AB")
    Jump("loc_10A3")

    label("loc_3AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493")

    #C0001
    ChrTalk(
        0x8,
        (
            "魔獣に襲われたり、失踪したり……\x01",
            "鉱員にやたらと不運が降りかかってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "ホフマンの奴は、こういうときこそ\x01",
            "ドンと構えてなくちゃならねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "鉱山長としての腕の見せ所だな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_52C")

    label("loc_493")


    #C0004
    ChrTalk(
        0x8,
        (
            "……俺も、脚をケガしてなきゃ\x01",
            "鉱員どもを手伝ってやれるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "いや、鉱山長はホフマンだ。\x01",
            "きっと自分たちでどうにか上手く\x01",
            "やっていくだろうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52C")

    Jump("loc_10A3")

    label("loc_531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5CA")

    #C0006
    ChrTalk(
        0x8,
        (
            "ガンツの野郎、わざわざ町長に\x01",
            "出向かせるとはふてぇヤツだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "どうやら博打に勝って\x01",
            "気が大きくなっちまってるらしいな。\x01",
            "ったくよぉ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A3")

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_669")

    #C0008
    ChrTalk(
        0x8,
        (
            "ガンツの野郎は、博打に\x01",
            "給料の殆どを使っちまってたから\x01",
            "随分ツケが溜まってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "あの野郎、無事に戻ってこねぇと\x01",
            "ただじゃすまさないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A3")

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C")
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x9, 500)

    #C0010
    ChrTalk(
        0x8,
        (
            "……キミィ！\x01",
            "すまんが棚からアレ、とってくれるか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0011
    ChrTalk(
        0x9,
        "はーい♪　アレね～。\x02",
    )

    CloseMessageWindow()

    def lambda_6E4():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6E4)

    def lambda_6F1():
        OP_93(0xFE, 0x140, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6F1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    #C0012
    ChrTalk(
        0x8,
        (
            "……立て込んでてすまねぇな。\x01",
            "何か入用か？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_7AA")

    label("loc_73C")


    #C0013
    ChrTalk(
        0x8,
        (
            "ウチの娘はよく気がつく\x01",
            "頭のいい子に育ってくれたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "俺に似なくてよかったってとこだな。\x01",
            "わっはっは。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AA")

    Jump("loc_10A3")

    label("loc_7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_85A")

    #C0015
    ChrTalk(
        0x8,
        (
            "妙に鉱員どものサボリが\x01",
            "目立つ気がするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "俺が鉱員の頃は、\x01",
            "それこそ寝る間も惜しんで……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "……いかんいかん、\x01",
            "赤の他人に説教するところだったぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A3")

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8C7")

    #C0018
    ChrTalk(
        0x8,
        (
            "……あとで《赤レンガ亭》にでも\x01",
            "行くとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "俺にだってハメを外したい時はあるのさ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A3")

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_966")

    #C0020
    ChrTalk(
        0x8,
        (
            "魔獣は総じて七耀石が大好物でな。\x01",
            "倒すとセピスを落とすのは\x01",
            "そういうことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "この町の鉱山に魔獣が集まるのも\x01",
            "七耀石の産地だからだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A3")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_ABD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A83")

    #C0022
    ChrTalk(
        0x8,
        (
            "おめぇら、\x01",
            "クロスベル市の警察なんだろ？\x01",
            "こんなトコまで見回りとはご苦労だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "……誰にでも下積みの時代はある。\x01",
            "俺も昔はマトックかついで\x01",
            "鉱山で働かされたもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "そこで腐らずやれるかどうかが\x01",
            "将来デカいことやれるかどうかに\x01",
            "繋がってくると思うぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AB8")

    label("loc_A83")


    #C0025
    ChrTalk(
        0x8,
        (
            "誰にでも下積みの時代はある。\x01",
            "せいぜい頑張りな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB8")

    Jump("loc_10A3")

    label("loc_ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B22")

    #C0026
    ChrTalk(
        0x8,
        "おうおう、何か入用かァ？！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "景気よくバーンと買っていけや、おう！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B85")

    label("loc_B22")


    #C0028
    ChrTalk(
        0x8,
        (
            "どうした、何か必要だから\x01",
            "店に入ってきたんだろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "景気よくバーンと買っていけや、おう！\x02",
    )

    CloseMessageWindow()

    label("loc_B85")

    Jump("loc_10A3")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C50")

    #C0030
    ChrTalk(
        0x8,
        (
            "都会のモヤシっ子にしちゃあ\x01",
            "ハロルドはよく出来たヤツだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "ちっと謙虚すぎるのが\x01",
            "たまにキズだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "商人としてやってくなら、\x01",
            "やっぱどんと構えてないとよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CBF")

    label("loc_C50")


    #C0033
    ChrTalk(
        0x8,
        (
            "ハロルドのヤツは\x01",
            "ちっと謙虚すぎるのが\x01",
            "たまにキズだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "もっと儲けを追求しようとは\x01",
            "思わねぇのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBF")

    Jump("loc_10A3")

    label("loc_CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D60")

    #C0035
    ChrTalk(
        0x8,
        (
            "ちっ、記念祭が近いからって\x01",
            "どいつもこいつも\x01",
            "浮かれやがってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "祭りが楽しみなのは分かるが、\x01",
            "浮ついてちゃ怪我の元だぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DEE")

    label("loc_D60")


    #C0037
    ChrTalk(
        0x8,
        (
            "記念祭が楽しみなのは分かるが、\x01",
            "どいつもこいつも\x01",
            "浮かれやがってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "怪我して記念祭に\x01",
            "行けなくならないように、\x01",
            "気合入れてろってんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEE")

    Jump("loc_10A3")

    label("loc_DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_E01")
    Jump("loc_10A3")

    label("loc_E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_F3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC3")

    #C0039
    ChrTalk(
        0x8,
        (
            "しかし、最近は鉱員の質も\x01",
            "下がったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "イヌだかオオカミだか知らねぇが\x01",
            "そんなもんにビクビクしやがってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "この町の鉱員なら\x01",
            "ドンと構えてろってんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F39")

    label("loc_EC3")


    #C0042
    ChrTalk(
        0x8,
        (
            "イヌだかオオカミだか知らねぇが\x01",
            "そんなもんにビクビクしやがってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "この町の鉱員なら\x01",
            "ドンと構えてろってんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F39")

    Jump("loc_10A3")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_10A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F60")
    SetScenarioFlags(0x66, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102D")

    #C0044
    ChrTalk(
        0x8,
        (
            "近頃、魔獣だのなんだのが\x01",
            "町をウロチョロしててイライラしてんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "魔獣に襲われて、\x01",
            "怪我するヤツまで出ちまってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "この上うちのキミィに何かあったら\x01",
            "絶対にただじゃおかねぇぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10A3")

    label("loc_102D")


    #C0047
    ChrTalk(
        0x8,
        (
            "魔獣に襲われて、\x01",
            "怪我するヤツまで出ちまってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "この上うちのキミィに何かあったら\x01",
            "絶対にただじゃおかねぇぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A3")

    Jump("loc_2E9")

    label("loc_10A8")

    TalkEnd(0x8)
    Return()

    # Function_4_2DC end

    def Function_5_10AC(): pass

    label("Function_5_10AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1187")

    #C0049
    ChrTalk(
        0xFE,
        (
            "キミィねぇ、後で鉱員さんたちに\x01",
            "差し入れしてあげるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "キミィが持って行った方が\x01",
            "みんながよろこぶからって、\x01",
            "お父ちゃんにまかされたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "えへへ、お父ちゃんって\x01",
            "恥ずかしがり屋さんだよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_1187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1214")

    #C0052
    ChrTalk(
        0xFE,
        (
            "鉱員のみんなはねー、\x01",
            "キミィにとっても優しくしてくれるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "みんな、お父ちゃんを\x01",
            "そんけいしてるんだって！\x01",
            "えへへー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1244")

    #C0054
    ChrTalk(
        0xFE,
        "今日のごはんは、なーにかな♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_1244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1287")

    #C0055
    ChrTalk(
        0xFE,
        (
            "キミィ、お父ちゃんの\x01",
            "お手伝いするの大好きだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_1287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1325")

    #C0056
    ChrTalk(
        0xFE,
        (
            "お父ちゃんねー、昔は鉱員だったから\x01",
            "今の鉱員さんのことがきになるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "たまにミラが無い鉱員さんに\x01",
            "食材をおまけしたりしてあげてるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_1325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_13B1")

    #C0058
    ChrTalk(
        0xFE,
        (
            "お父ちゃん、今日の夜は\x01",
            "お店を閉めて遊びに行くんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "記念祭の間はずっと忙しかったから、\x01",
            "楽しんできてほしいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_13B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_141C")

    #C0060
    ChrTalk(
        0xFE,
        (
            "セピスっていうのは、\x01",
            "七耀石のカケラのことなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "よく知ってるでしょ、えっへん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_141C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1459")

    #C0062
    ChrTalk(
        0xFE,
        (
            "お父ちゃんの鉱員姿、\x01",
            "見てみたかったなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_1459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_152C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E7")

    #C0063
    ChrTalk(
        0xFE,
        (
            "お父ちゃん、\x01",
            "なんだか機嫌悪かったけど\x01",
            "今日なおったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "えへへ、\x01",
            "やっぱりキミィが応援したおかげかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1527")

    label("loc_14E7")


    #C0065
    ChrTalk(
        0xFE,
        (
            "お父ちゃん、\x01",
            "なんだか機嫌悪かったけど\x01",
            "元気になったみたい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1527")

    Jump("loc_1816")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_159E")

    #C0066
    ChrTalk(
        0xFE,
        (
            "ハロルドおいちゃんねー、\x01",
            "キミィを見るときなんだか\x01",
            "寂しそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "何かあったのかな……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1816")

    label("loc_159E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1621")

    #C0068
    ChrTalk(
        0xFE,
        (
            "記念祭が近いのに、\x01",
            "お父ちゃんったら\x01",
            "なんだが機嫌が悪いみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "キミィ、何かしちゃったかなぁ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_165E")

    label("loc_1621")


    #C0070
    ChrTalk(
        0xFE,
        (
            "お父ちゃん、記念祭の話になると\x01",
            "機嫌が悪くなっちゃうの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165E")

    Jump("loc_1816")

    label("loc_1663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1671")
    Jump("loc_1816")

    label("loc_1671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_173E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F7")

    #C0071
    ChrTalk(
        0xFE,
        (
            "お父ちゃんも、\x01",
            "昔は鉱員だったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "体も大きくて、\x01",
            "町一番の鉱員だったんだって。\x01",
            "すごいでしょ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1739")

    label("loc_16F7")


    #C0073
    ChrTalk(
        0xFE,
        (
            "お父ちゃん、\x01",
            "昔は町一番の鉱員だったんだって。\x01",
            "すごいでしょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1739")

    Jump("loc_1816")

    label("loc_173E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1816")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1760")
    SetScenarioFlags(0x66, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D4")

    #C0074
    ChrTalk(
        0xFE,
        "お手伝い、お手伝い♪\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "お父ちゃんは\x01",
            "町の人には怖がられてるけど、\x01",
            "あたしには優しいんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1816")

    label("loc_17D4")


    #C0076
    ChrTalk(
        0xFE,
        (
            "お父ちゃん、\x01",
            "あたしには優しいんだよ。\x01",
            "怖がらないであげてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1816")

    TalkEnd(0xFE)
    Return()

    # Function_5_10AC end

    def Function_6_181A(): pass

    label("Function_6_181A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18F1")
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_18D1")

    #C0077
    ChrTalk(
        0xC,
        (
            "#0908F（エステル……気持ちは判るけど\x01",
            "  もっとさり気なく行こう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xB,
        "#0806F（ううっ……判ってるけど……）\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "#3605F…………………？？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_18E5")

    label("loc_18D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 2)), scpexpr(EXPR_END)), "loc_18E2")
    Call(0, 9)
    Jump("loc_18E5")

    label("loc_18E2")

    Call(0, 8)

    label("loc_18E5")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)

    label("loc_18F1")

    TalkEnd(0xFE)
    Return()

    # Function_6_181A end

    def Function_7_18F5(): pass

    label("Function_7_18F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1974")

    #C0080
    ChrTalk(
        0xFE,
        (
            "あら、これって……\x01",
            "鉱員用のヘルメットかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "こんなものまで売ってるなんて、\x01",
            "さすが鉱山の町……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19C0")

    label("loc_1974")


    #C0082
    ChrTalk(
        0xFE,
        "このヘルメット、お土産になるかしら。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "……さすがにかさばるわねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_19C0")

    TalkEnd(0xFE)
    Return()

    # Function_7_18F5 end

    def Function_8_19C4(): pass

    label("Function_8_19C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(4730, 1500, 0, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(26660, 0)
    SetChrPos(0x101, 2750, 0, -1250, 45)
    SetChrPos(0x102, 2100, 0, -600, 45)
    SetChrPos(0x103, 1750, 0, -2250, 45)
    SetChrPos(0x104, 1100, 0, -1600, 45)
    OP_0D()

    #C0084
    ChrTalk(
        0xC,
        (
            "#0905Fそれじゃあ、ハロルドさんは\x01",
            "７年前から今の貿易会社を……？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "#3609Fはは、貿易会社なんて\x01",
            "大層なものではありませんが……\x02\x03",

            "#3600Fお付き合いさせてもらっている\x01",
            "全ての方々が笑顔でいられるような\x01",
            "取引を心がけています。\x02\x03",

            "#3604Fクロスベルの貿易商としては\x01",
            "失格かもしれませんけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        (
            "#0904Fいえ……\x01",
            "とても意義のあるお仕事を\x01",
            "されていると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xB,
        "#0801F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#0005F（エステルたちとハロルドさん……\x01",
            "  何だか取り込み中みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#0104F（邪魔したら悪そうね。）\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2750, 0, -1250, 45)
    SetScenarioFlags(0x94, 2)
    EventEnd(0x5)
    Return()

    # Function_8_19C4 end

    def Function_9_1C4D(): pass

    label("Function_9_1C4D")

    EventBegin(0x0)
    Fade(500)
    OP_68(4730, 1500, 0, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(26660, 0)
    SetChrPos(0x101, 2750, 0, -1250, 45)
    SetChrPos(0x102, 2100, 0, -600, 45)
    SetChrPos(0x103, 1750, 0, -2250, 45)
    SetChrPos(0x104, 1100, 0, -1600, 45)
    OP_0D()
    TurnDirection(0xA, 0xB, 300)

    #C0090
    ChrTalk(
        0xA,
        (
            "#3605Fあの……\x01",
            "エステルさんと仰いましたか？\x02\x03",

            "#3600Fそのう、どこかで\x01",
            "お会いした事がありましたか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_1D54():
        TurnDirection(0xC, 0xB, 300)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1D54)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    WaitChrThread(0xC, 1)

    #C0091
    ChrTalk(
        0xB,
        (
            "#0805Fい、いえっ！\x01",
            "ちょっと知っている人に\x01",
            "似てるなぁって思っただけで！\x02\x03",

            "#0806F（……まさかここまで\x01",
            "  ソックリだったなんて……）\x02\x03",

            "#0808F（本物の人間よね……この人？）\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)
    SetChrPos(0x0, 2750, 0, -1250, 45)
    SetScenarioFlags(0x94, 3)
    EventEnd(0x5)
    Return()

    # Function_9_1C4D end

    SaveToFile()

Try(main)
