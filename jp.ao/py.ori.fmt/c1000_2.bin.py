from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1000_2.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [152, 4751, 8974, 12812, 22148, 25732, 26167, 26757, 29230, 0, 32545, 0, 36393, 39440, 39924, 42004, 0, 43963, 0, 176, 180, 0, 0],
    )

    BuildStringList((
        "c1000_2",                # 0
    ))

    ChipFrameInfo(152, 0)                                        # 0

    ScpFunction((
        "Function_0_98",           # 00, 0
        "Function_1_128F",         # 01, 1
        "Function_2_230E",         # 02, 2
        "Function_3_320C",         # 03, 3
        "Function_4_5684",         # 04, 4
        "Function_5_6484",         # 05, 5
        "Function_6_6637",         # 06, 6
        "Function_7_6885",         # 07, 7
        "Function_8_722E",         # 08, 8
        "Function_9_7F21",         # 09, 9
        "Function_10_8E29",        # 0A, 10
        "Function_11_9A10",        # 0B, 11
        "Function_12_9BF4",        # 0C, 12
        "Function_13_A414",        # 0D, 13
        "Function_14_ABBB",        # 0E, 14
        "Function_15_B4B0",        # 0F, 15
        "Function_16_B5CF",        # 10, 16
    ))


    def Function_0_98(): pass

    label("Function_0_98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E7")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x1A2, 500)

    #C0001
    ChrTalk(
        0x8,
        "お、可愛らしいお子さんッスね～。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "どうスか、この風車。\x01",
            "フーフー吹いたら楽しいッスよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x1A2,
        "……それはボクに言ってるのか？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x1A2,
        (
            "フンッ、そんなの東方じゃ\x01",
            "珍しくもなんともないし、\x01",
            "コドモだましもいいトコロだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "ガーン……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_223")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2D0")

    label("loc_223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_27C")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2D0")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2D0")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2D0")

    TalkEnd(0x8)
    SetScenarioFlags(0x1DC, 3)
    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_32A")

    label("loc_2E7")


    #C0006
    ChrTalk(
        0x8,
        (
            "うぅ……\x01",
            "こんなに食い付きの悪い\x01",
            "お子さんは初めてかもッス。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_32A")

    Return()

    label("loc_32B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_393")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3B2")
    OP_AF(0x38)
    Jump("loc_3B4")

    label("loc_3B2")

    OP_AF(0x39)

    label("loc_3B4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1286")

    label("loc_3C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D7")
    Jump("loc_1286")

    label("loc_3D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1286")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_573")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD")

    #C0007
    ChrTalk(
        0xFE,
        (
            "ひとまず、クロスベル市が\x01",
            "日常を取り戻せてよかったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "その代わりにワケの分からない\x01",
            "大樹が現れちまったッスけど……\x01",
            "きっと何とかなるッスよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "気晴らしに、新しい工芸品でも\x01",
            "作ってみるッスかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_56E")

    label("loc_4DD")


    #C0010
    ChrTalk(
        0xFE,
        (
            "ロイくんには、また明日から\x01",
            "バリバリ働いてもらうつもりッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "ワケの分からない\x01",
            "大樹が現れちまったッスけど……\x01",
            "きっと何とかなるッスよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56E")

    Jump("loc_1286")

    label("loc_573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_581")
    Jump("loc_1286")

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FD")

    #C0012
    ChrTalk(
        0xFE,
        (
            "クロスベルがついに\x01",
            "国家として独立するんッスね……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "まさに歴史が変わる瞬間に\x01",
            "立ち会っている気分ッス。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_5FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_695")

    #C0014
    ChrTalk(
        0xFE,
        (
            "旧市街で行われる\x01",
            "炊き出しのために、\x01",
            "木製の食器を沢山作ったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "些細なことだけど、\x01",
            "自分にはこれくらいしか\x01",
            "できないッスからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_714")

    #C0016
    ChrTalk(
        0xFE,
        (
            "マインツが占領されちまった\x01",
            "そうッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "工芸品の材料のこととかで\x01",
            "色々お世話になってるし、\x01",
            "心配ッス……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_79D")

    #C0018
    ChrTalk(
        0xFE,
        (
            "今日はお客さんも\x01",
            "あんまり来なさそうッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "ロイくんにも休みをあげたし、\x01",
            "１人でノンビリと工芸品でも\x01",
            "作ってるッス。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_79D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_80F")

    #C0020
    ChrTalk(
        0xFE,
        (
            "ロイくんの作った風車、\x01",
            "ひっそりと売れていったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "いや～、なんだかオレも\x01",
            "嬉しいッスね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E1")

    #C0022
    ChrTalk(
        0xFE,
        (
            "店頭に出してる風車は\x01",
            "一つ一つ、回転の仕方が\x01",
            "微妙に違うんッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "これぞ、手作りならではの\x01",
            "味ってやつッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "まあ、素人さんには\x01",
            "ほとんど違いなんて\x01",
            "分かんないッスけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_96D")

    label("loc_8E1")


    #C0025
    ChrTalk(
        0xFE,
        (
            "そういえばロイくんの風車、\x01",
            "商品として売れそうなのが\x01",
            "１つだけできたッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "もともと手先が\x01",
            "器用みたいッスからね。\x01",
            "将来有望ッスよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96D")

    Jump("loc_1286")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5A")

    #C0027
    ChrTalk(
        0xFE,
        (
            "コツコツつくってた\x01",
            "オルキスタワーの模型が\x01",
            "昨夜、やっとこさ完成したッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "店先に置いておいたら\x01",
            "観光客がすごく欲しがって\x01",
            "くれたんッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "でも、これは非売品なんッスよね～。\x01",
            "なんだか悪いッス。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AC9")

    label("loc_A5A")


    #C0030
    ChrTalk(
        0xFE,
        (
            "それにしてもロイくん、\x01",
            "根気よく働いてくれて\x01",
            "助かってるッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "やっぱりこれも\x01",
            "会長の血筋なんスかね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC9")

    Jump("loc_1286")

    label("loc_ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B76")

    #C0032
    ChrTalk(
        0xFE,
        (
            "ロイくんにウチで\x01",
            "働いてもらうことになったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "さすが、商工会会長の\x01",
            "お孫さんだけあってマジメッスね～。\x01",
            "なかなか期待できそうッス。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BDA")

    label("loc_B76")


    #C0034
    ChrTalk(
        0xFE,
        (
            "彼にはこの際、色々と\x01",
            "覚えてもらうつもりッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "ふふ、弟子ができたみたいで\x01",
            "楽しいッスね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDA")

    Jump("loc_1286")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C96")

    #C0036
    ChrTalk(
        0xFE,
        (
            "さっきの東方風の美女なら、\x01",
            "露店街で色々と買い物をしてから\x01",
            "中央広場の方に歩いていったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "切れ長で冷ややかな目が\x01",
            "すげえ印象的だったッスよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3E")

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFF")

    #C0038
    ChrTalk(
        0xFE,
        (
            "ついさっき、東方風の美女が\x01",
            "買い物に来てたんッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "切れ長で冷ややかな目が\x01",
            "すげえ印象的だったッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00001F……その人はどちらへ？\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "露店街で色々と買い物をしてから\x01",
            "中央広場の方に歩いていったッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00305F（おいロイド、こいつは\x01",
            "  もしかしてあの人なんじゃ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00001F（……ああ、探してみるとしよう。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1C6, 7)
    Jump("loc_F3E")

    label("loc_DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED2")

    #C0044
    ChrTalk(
        0xFE,
        (
            "いや～、オルキスタワーってのは\x01",
            "すごい迫力ッスね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "う～ん、創作意欲が沸いてきたッス。\x01",
            "タワーの模型を作ってみようかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "以前の記念祭のときも、\x01",
            "市庁舎の模型を作ったんッスよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F3E")

    label("loc_ED2")


    #C0047
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "商工会のモルス会長の\x01",
            "お孫さんが見に来てるッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "ふーむ、珍しい事もあるものッス。\x02",
    )

    CloseMessageWindow()

    label("loc_F3E")

    Jump("loc_1286")

    label("loc_F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_103D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC8")

    #C0049
    ChrTalk(
        0xFE,
        (
            "うちの工芸品は、\x01",
            "全部手作りなんッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "手作りって、やっぱりどこか\x01",
            "温かみがあっていいッスよね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1038")

    label("loc_FC8")


    #C0051
    ChrTalk(
        0xFE,
        (
            "手作りは手間がかかるし、\x01",
            "怪我しちゃうこともあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "やっぱりどこか\x01",
            "温かみがあっていいッスよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1038")

    Jump("loc_1286")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1165")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FC")

    #C0053
    ChrTalk(
        0xFE,
        (
            "折角作った工芸品が\x01",
            "濡れちまうッスねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "……とは言っても、\x01",
            "ウチの工芸品は\x01",
            "バッチリ防水加工ッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "手間ひまかけているだけに\x01",
            "丈夫にできてるんッスよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1160")

    label("loc_10FC")


    #C0056
    ChrTalk(
        0xFE,
        (
            "ウチの工芸品は\x01",
            "バッチリ防水加工ッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "手間ひまかけているだけに\x01",
            "丈夫にできてるんッスよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1160")

    Jump("loc_1286")

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1206")

    #C0058
    ChrTalk(
        0xFE,
        "へい、らっしゃいッス！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "うちは色んな\x01",
            "手作りの工芸品を扱ってるッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "気に入ったのがあったら\x01",
            "是非買っていって欲しいッス！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1286")

    label("loc_1206")


    #C0061
    ChrTalk(
        0xFE,
        (
            "うちの商品の中でも、人気なのは\x01",
            "この『風車#4Rかざぐるま#』ッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "東方で魔除けになるといわれてる\x01",
            "おもちゃなんッスよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1286")

    Jump("loc_335")

    label("loc_128B")

    TalkEnd(0xFE)
    Return()

    # Function_0_98 end

    def Function_1_128F(): pass

    label("Function_1_128F")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_129C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_12FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131A")
    OP_AF(0x35)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2305")

    label("loc_131A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132E")
    Jump("loc_2305")

    label("loc_132E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2305")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1466")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F7")

    #C0063
    ChrTalk(
        0xFE,
        "らっしゃい、らっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "フレッシュ・ディンズは\x01",
            "今日も営業中だよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "新鮮な野菜を食べて、\x01",
            "この異常な事態を\x01",
            "健康に乗り切ってこうぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1461")

    label("loc_13F7")


    #C0066
    ChrTalk(
        0xFE,
        (
            "……さっきからリリィが\x01",
            "チラチラとこっちを\x01",
            "見てくるみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "俺の顔に何かついてるのかねえ。\x02",
    )

    CloseMessageWindow()

    label("loc_1461")

    Jump("loc_2305")

    label("loc_1466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1474")
    Jump("loc_2305")

    label("loc_1474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_157D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1520")

    #C0068
    ChrTalk(
        0xFE,
        (
            "クロスベル独立国かぁ……\x01",
            "いやあ、めでたいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "でもリリィの奴は\x01",
            "なんだか難しそうな顔を\x01",
            "してんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "何か心配事でもあんのかねえ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1578")

    label("loc_1520")


    #C0071
    ChrTalk(
        0xFE,
        (
            "リリィの奴、\x01",
            "なんだか難しそうな顔を\x01",
            "してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "何か心配事でもあんのかねえ？\x02",
    )

    CloseMessageWindow()

    label("loc_1578")

    Jump("loc_2305")

    label("loc_157D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1642")

    #C0073
    ChrTalk(
        0xFE,
        (
            "今日、市民会館で行われる\x01",
            "チャリティイベントの為に、\x01",
            "うちから野菜を贈ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "主催する商工会には\x01",
            "世話になってるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "街の皆にも\x01",
            "元気になって欲しいしな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16CB")

    label("loc_1642")


    #C0076
    ChrTalk(
        0xFE,
        (
            "商工会のじーさま方には、\x01",
            "役員にさそってもらったり\x01",
            "色々世話になってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "街の皆を元気にするために\x01",
            "がんばって欲しいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CB")

    Jump("loc_2305")

    label("loc_16D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_17C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1778")

    #C0078
    ChrTalk(
        0xFE,
        (
            "マインツが占拠されたそうだが……\x01",
            "噂じゃ、身代金なんかの要求は\x01",
            "出ていないって話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "武装集団はなにをしようと\x01",
            "してんだろうな……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17BE")

    label("loc_1778")


    #C0080
    ChrTalk(
        0xFE,
        (
            "武装集団とやらは、\x01",
            "何のためにマインツを\x01",
            "占領したんだろうな……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BE")

    Jump("loc_2305")

    label("loc_17C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A7")

    #C0081
    ChrTalk(
        0xFE,
        (
            "野菜を卸しに来てくれる兄さんが\x01",
            "興奮気味に話してくれたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "昨日、なんかアルモリカ村の方で\x01",
            "大きな騒ぎがあったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "一応、解決はしたみたいだが……\x01",
            "うーん、なにがあったのかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1934")

    label("loc_18A7")


    #C0084
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の方で\x01",
            "昨日、大きな騒ぎがあったらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "トラックの兄さん、興奮してて\x01",
            "しかも訛ってたから\x01",
            "よくわかんなかったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1934")

    Jump("loc_2305")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A12")

    #C0086
    ChrTalk(
        0xFE,
        (
            "実はオレ、子供の頃は\x01",
            "野菜なんて大嫌いだったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "でも、大人になるにつれて\x01",
            "だんだん、美味しいと\x01",
            "思えるようになってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "好き嫌いなんてのは案外\x01",
            "そんなもんなのかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A99")

    label("loc_1A12")


    #C0089
    ChrTalk(
        0xFE,
        (
            "オレは野菜は大嫌いだったけど、\x01",
            "いつのまにか美味しく\x01",
            "食べれるようになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "好き嫌いなんてのは案外\x01",
            "そんなもんなのかもな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A99")

    Jump("loc_2305")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B4B")

    #C0091
    ChrTalk(
        0xFE,
        (
            "実は、うちの店の名前は\x01",
            "リリィが考えてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "商売がやりたいって言ったときから\x01",
            "なにかとサポートしてくれてさ……\x01",
            "へへ、いい幼馴染をもったもんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2305")

    label("loc_1B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFC")

    #C0093
    ChrTalk(
        0xFE,
        (
            "いつも、アルモリカ村から\x01",
            "導力トラックで野菜を卸しに\x01",
            "来てもらってるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "う～ん、言っちゃ悪いが\x01",
            "あんなに小奇麗な\x01",
            "トラックだったかなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C6B")

    label("loc_1BFC")


    #C0095
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の\x01",
            "導力トラック……\x01",
            "新しく買い換えたのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "へへ、景気がよくて\x01",
            "うらやましい限りだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6B")

    Jump("loc_2305")

    label("loc_1C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0C")

    #C0097
    ChrTalk(
        0xFE,
        (
            "通商会議では主に経済について\x01",
            "話し合われるってことだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "……ま、俺には\x01",
            "難しいことはわからねえ。\x01",
            "なるようになれだぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D8B")

    label("loc_1D0C")


    #C0099
    ChrTalk(
        0xFE,
        (
            "ま、経済がどうなろうが、\x01",
            "これからもお客様第一で\x01",
            "商売してくだけだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "オレには、難しいことは\x01",
            "さっぱりわからねえしな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    Jump("loc_2305")

    label("loc_1D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECB")

    #C0101
    ChrTalk(
        0xFE,
        (
            "なんでも今日、リベール王国から\x01",
            "お姫様がきたらしいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "リベール王国といったら、\x01",
            "『にがトマト』の出荷で有名でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "なんでもリベールにある\x01",
            "ＺＣＦっていう導力器メーカーで\x01",
            "生まれたものらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "導力器メーカーなのに\x01",
            "野菜まで作っちまうなんて、\x01",
            "さすがの技術力だよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F5D")

    label("loc_1ECB")


    #C0105
    ChrTalk(
        0xFE,
        (
            "にがトマトってのは、\x01",
            "ちょっと前にＺＣＦで\x01",
            "生み出された野菜でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "導力器メーカーなのに\x01",
            "野菜まで作っちまうなんて、\x01",
            "さすがの技術力だよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5D")

    Jump("loc_2305")

    label("loc_1F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2160")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D6")

    #C0107
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院の先生に\x01",
            "聞いたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "なんでも野菜を食べると、\x01",
            "油の吸収がゆるやかになるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "肉なんかを食べるときは\x01",
            "野菜をいっしょに食べると\x01",
            "太りにくくなるってわけさ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2054")
    Jump("loc_20CE")

    label("loc_2054")


    #C0110
    ChrTalk(
        0x109,
        "#10105Fな、なるほど……！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#00102F勉強になります。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00012F（女性ってこういう話題には\x01",
            "  特に熱心だよな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CE")

    SetScenarioFlags(0x0, 1)
    Jump("loc_215B")

    label("loc_20D6")


    #C0113
    ChrTalk(
        0xFE,
        (
            "野菜、食ってるかい？\x01",
            "ジャンクフードばっかり\x01",
            "食べてちゃあ、体に毒だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "健康に過ごしたいなら、\x01",
            "やっぱり野菜を食べないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215B")

    Jump("loc_2305")

    label("loc_2160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21FF")

    #C0115
    ChrTalk(
        0xFE,
        (
            "……んー、テントから\x01",
            "雨漏りしてるみてえだな。\x01",
            "近いうちに補修しとかねえと。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "……しかし、さっきからリリィは\x01",
            "何をモジモジしてやがるんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2305")

    label("loc_21FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AC")

    #C0117
    ChrTalk(
        0xFE,
        "らっしゃい、らっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "アルモリカ産の新鮮野菜、\x01",
            "今日もたっぷり入ってるよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "やっぱりクロスベル産の野菜は\x01",
            "ピカイチのうまさだぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2305")

    label("loc_22AC")


    #C0120
    ChrTalk(
        0xFE,
        (
            "やっぱりアルモリカ産野菜は\x01",
            "美味くてオススメだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "たっぷり買ってってくれよな！\x02",
    )

    CloseMessageWindow()

    label("loc_2305")

    Jump("loc_129C")

    label("loc_230A")

    TalkEnd(0xFE)
    Return()

    # Function_1_128F end

    def Function_2_230E(): pass

    label("Function_2_230E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2404")

    #C0122
    ChrTalk(
        0xFE,
        (
            "ディンズったら……\x01",
            "野菜を食べて乗り切ろう、なんて\x01",
            "能天気にもほどがあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "でも、そんなディンズだからこそ\x01",
            "みんなに元気を与えられるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "露天商として大事なのは、\x01",
            "案外そういう部分なのかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24A1")

    label("loc_2404")


    #C0125
    ChrTalk(
        0xFE,
        (
            "能天気なディンズだからこそ\x01",
            "みんなに元気を与えられるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "私も街に化物がうろついてたときは\x01",
            "ディンズに元気付けられたの。\x01",
            "ふふ、感謝しなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A1")

    Jump("loc_3208")

    label("loc_24A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_24B4")
    Jump("loc_3208")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F1")

    #C0127
    ChrTalk(
        0xFE,
        (
            "２大国からの物流も\x01",
            "完全にストップしちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "どうも、ディーター大統領は\x01",
            "５年分くらいの備蓄を\x01",
            "蓄えてるって話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "新鮮野菜を売りにしてるウチは\x01",
            "商売のやり方を考えないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "……でもディンズったら、\x01",
            "その辺を全然分かってないみたい。\x01",
            "はあ、しっかりしてほしいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2692")

    label("loc_25F1")


    #C0131
    ChrTalk(
        0xFE,
        (
            "どうも、ディーター大統領は５年分くらいの備蓄を\x01",
            "蓄えてるって話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "今後の商売にも\x01",
            "関わってくることなんだから、\x01",
            "ディンズにもしっかりしてほしいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2692")

    Jump("loc_3208")

    label("loc_2697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_277E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")

    #C0133
    ChrTalk(
        0xFE,
        (
            "不幸中の幸いか、\x01",
            "東通りはほとんど\x01",
            "被害がなかったんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_26EF")


    #C0134
    ChrTalk(
        0xFE,
        (
            "あの大きな鬼が暴れまわったせいで、\x01",
            "旧市街はひどい有様みたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "今、復旧作業をやってるようだけど……\x01",
            "いつごろ目処がつくのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_277E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27EC")

    #C0136
    ChrTalk(
        0xFE,
        "マインツの件、怖いわよね……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "警備隊の人たちが\x01",
            "なんとか解決してくれると\x01",
            "いいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_27EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_288F")

    #C0138
    ChrTalk(
        0xFE,
        (
            "ああもう、この間\x01",
            "テントの穴をふさいだのに、\x01",
            "別のところから雨漏りしてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "まったくディンズったら、\x01",
            "考え事はいいから手伝って欲しいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_288F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298B")

    #C0140
    ChrTalk(
        0xFE,
        (
            "ネギとかニラとかって、\x01",
            "においがあるから嫌いな人は\x01",
            "多いかも知れないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "結構食わず嫌いな人が\x01",
            "ほとんどじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "思い切って食べてみると\x01",
            "案外美味しいかもしれないから\x01",
            "色々とチャレンジしてみてほしいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A0C")

    label("loc_298B")


    #C0143
    ChrTalk(
        0xFE,
        (
            "食わず嫌いって、\x01",
            "やっぱりちょっともったいないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "ニオイの苦手な食べ物でも\x01",
            "食べてみると結構美味しいかも\x01",
            "しれないわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A0C")

    Jump("loc_3208")

    label("loc_2A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE7")

    #C0145
    ChrTalk(
        0xFE,
        (
            "ディンズって、\x01",
            "何の知識もないまま\x01",
            "商売を始めようとしてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "商売の許可をとったり\x01",
            "場所を確保したりは、\x01",
            "私がやってあげたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "なんというか、昔っから\x01",
            "放っておけないのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B77")

    label("loc_2AE7")


    #C0148
    ChrTalk(
        0xFE,
        (
            "ディンズって、\x01",
            "何の知識もないまま\x01",
            "商売を始めようとしてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "だから商売の諸々の準備は\x01",
            "私がしてあげたのよね。\x01",
            "まったく、やれやれだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B77")

    Jump("loc_3208")

    label("loc_2B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C41")

    #C0150
    ChrTalk(
        0xFE,
        (
            "実はこの間、商工会のじーさまが\x01",
            "こっそりディンズの様子を\x01",
            "聞きに来てたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "ディンズは前に役員の誘いを\x01",
            "断っちゃったんだけど、\x01",
            "やっぱり惜しく思ってるみたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CD9")

    label("loc_2C41")


    #C0152
    ChrTalk(
        0xFE,
        (
            "うーん、あの時は私も\x01",
            "誘いを断るのは惜しいって\x01",
            "思ってたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "ディンズって\x01",
            "人の上に立つような柄じゃないし、\x01",
            "これでよかったんだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD9")

    Jump("loc_3208")

    label("loc_2CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D52")

    #C0154
    ChrTalk(
        0xFE,
        (
            "もう、ディンズって\x01",
            "物事を深く考えられないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "幼馴染の私が\x01",
            "しっかりとサポートしないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3208")

    label("loc_2D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3E")

    #C0156
    ChrTalk(
        0xFE,
        (
            "にがトマトって料理につかうと\x01",
            "味にかなり深みがでるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "でも、サラダとかにして\x01",
            "食べたい人には\x01",
            "あまりオススメしないかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "……だって、そのままだと\x01",
            "すっごく苦いんだもの。\x01",
            "私はちょっと苦手かな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EBA")

    label("loc_2E3E")


    #C0159
    ChrTalk(
        0xFE,
        (
            "にがトマトって料理につかうと\x01",
            "味にかなり深みがでるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "そのままだとすっごく苦いけどね。\x01",
            "結構、玄人向けの食材よ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBA")

    Jump("loc_3208")

    label("loc_2EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA3")

    #C0161
    ChrTalk(
        0xFE,
        (
            "ディンズは露天商になるために\x01",
            "野菜のことを一所懸命勉強したのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "ただ経営的なセンスはさっぱりで、\x01",
            "ほとんど人柄の良さだけでやってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "まあ、ある意味それが\x01",
            "ディンズの持ち味なんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_301F")

    label("loc_2FA3")


    #C0164
    ChrTalk(
        0xFE,
        (
            "ディンズの商売は誠実だけど、\x01",
            "経営のセンスはさっぱりなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "まあ、ある意味それが\x01",
            "ディンズの持ち味なんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301F")

    Jump("loc_3208")

    label("loc_3024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_317D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E2")

    #C0166
    ChrTalk(
        0xFE,
        (
            "さっき来てくれたお客さんが、\x01",
            "『あんたたち夫婦みたいだね』って……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "単なる幼馴染だと思ってたから\x01",
            "考えた事もなかったけど……\x01",
            "な、なんだか意識しちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3178")

    label("loc_30E2")


    #C0168
    ChrTalk(
        0xFE,
        (
            "お客さんに、\x01",
            "『あんたたち夫婦みたいだね』\x01",
            "なんて言われちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "……でも、ディンズは\x01",
            "何とも思ってないみたい。\x01",
            "まったく、失礼しちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3178")

    Jump("loc_3208")

    label("loc_317D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3208")

    #C0170
    ChrTalk(
        0xFE,
        (
            "クロスベルでは、\x01",
            "食料品の多くを輸入に頼っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "でも、鉄道で迅速に届けられるから\x01",
            "輸入物でも思った以上に新鮮なのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3208")

    TalkEnd(0xFE)
    Return()

    # Function_2_230E end

    def Function_3_320C(): pass

    label("Function_3_320C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3235")
    Call(0, 29)
    Return()

    label("loc_3235")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_567D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5678")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "話をする")
    MenuCmd(1, 1, "魚を渡す")
    MenuCmd(1, 1, "やめる")
    ClearScenarioFlags(0x2, 3)
    Call(2, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A3")
    MenuCmd(3, 1, 0x1)

    label("loc_32A3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32D5")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_32D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5643")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5634")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3360")
    MenuCmd(1, 1, "ファイタ　　　　　時    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3356")
    Call(2, 6)

    label("loc_3356")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3360")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33B6")
    MenuCmd(1, 1, "スノーシュラブ　　幻    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33AC")
    Call(2, 6)

    label("loc_33AC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_33B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_340C")
    MenuCmd(1, 1, "エーゼル　　　　　液体物×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3402")
    Call(2, 6)

    label("loc_3402")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_340C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3462")
    MenuCmd(1, 1, "カサギン　　　　　空    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3458")
    Call(2, 6)

    label("loc_3458")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3462")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_34B8")
    MenuCmd(1, 1, "アルモリカブナ　　ネギ  ×  2")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34AE")
    Call(2, 6)

    label("loc_34AE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_34B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_350E")
    MenuCmd(1, 1, "トタス　　　　　　粉末物×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3504")
    Call(2, 6)

    label("loc_3504")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_350E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3564")
    MenuCmd(1, 1, "オロショ　　　　　人参  ×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_355A")
    Call(2, 6)

    label("loc_355A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35BA")
    MenuCmd(1, 1, "ロック　　　　　　液体物×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B0")
    Call(2, 6)

    label("loc_35B0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_35BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3610")
    MenuCmd(1, 1, "レインボウ　　　　全    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3606")
    Call(2, 6)

    label("loc_3606")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3610")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3666")
    MenuCmd(1, 1, "ピラーニャ　　　　ハーブ×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365C")
    Call(2, 6)

    label("loc_365C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3666")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36BC")
    MenuCmd(1, 1, "カルプ　　　　　　リーフ×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B2")
    Call(2, 6)

    label("loc_36B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_36BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3712")
    MenuCmd(1, 1, "グラトンバス　　　地    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3708")
    Call(2, 6)

    label("loc_3708")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3768")
    MenuCmd(1, 1, "トラード　　　　　ポテト×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375E")
    Call(2, 6)

    label("loc_375E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3768")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37BE")
    MenuCmd(1, 1, "グラディエタ　　　全    ×  5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37B4")
    Call(2, 6)

    label("loc_37B4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_37BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3814")
    MenuCmd(1, 1, "レイニー　　　　　水    × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380A")
    Call(2, 6)

    label("loc_380A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3814")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_386A")
    MenuCmd(1, 1, "サンショ　　　　　風    × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3860")
    Call(2, 6)

    label("loc_3860")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_386A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38C0")
    MenuCmd(1, 1, "サモーナ　　　　　ベリー×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B6")
    Call(2, 6)

    label("loc_38B6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_38C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3916")
    MenuCmd(1, 1, "アローナ　　　　　火    × 15")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_390C")
    Call(2, 6)

    label("loc_390C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3916")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_396C")
    MenuCmd(1, 1, "イール　　　　　　珍野菜×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3962")
    Call(2, 6)

    label("loc_3962")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_396C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39C2")
    MenuCmd(1, 1, "アダマンタス　　　玄米  ×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B8")
    Call(2, 6)

    label("loc_39B8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_39C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A18")
    MenuCmd(1, 1, "クインシザー　　　珍野菜×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0E")
    Call(2, 6)

    label("loc_3A0E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A6E")
    MenuCmd(1, 1, "パルルク　　　　　味噌  ×  3")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A64")
    Call(2, 6)

    label("loc_3A64")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AC4")
    MenuCmd(1, 1, "タイタン　　　　　酪農品×  4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ABA")
    Call(2, 6)

    label("loc_3ABA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B1A")
    MenuCmd(1, 1, "ゴルドサモーナ　　空    × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B10")
    Call(2, 6)

    label("loc_3B10")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B70")
    MenuCmd(1, 1, "オオザンショ　　　幻    × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B66")
    Call(2, 6)

    label("loc_3B66")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BC6")
    MenuCmd(1, 1, "ノーブルカルプ　　全    × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BBC")
    Call(2, 6)

    label("loc_3BBC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C1C")
    MenuCmd(1, 1, "エメロド　　　　　風    ×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C12")
    Call(2, 6)

    label("loc_3C12")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C72")
    MenuCmd(1, 1, "ティガロック　　　地    ×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C68")
    Call(2, 6)

    label("loc_3C68")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CC8")
    MenuCmd(1, 1, "クリムゾンイータ　火    ×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CBE")
    Call(2, 6)

    label("loc_3CBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3CC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D1E")
    MenuCmd(1, 1, "ブルドラゴン　　　水    ×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D14")
    Call(2, 6)

    label("loc_3D14")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D74")
    MenuCmd(1, 1, "ギガルーク　　　　時空幻×500")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D6A")
    Call(2, 6)

    label("loc_3D6A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D74")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DB5")
    Jump("loc_562F")

    label("loc_3DB5")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E42")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E38")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0172
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス５個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_3E38")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EB2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0173
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス５個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_3EA8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F22")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F18")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0174
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I液体物食材３個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_3F18")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F92")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F88")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0175
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#61I空のセピス５個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_3F88")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FFC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0176
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20Iネギ２個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_3FF2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_406C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4062")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0177
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I粉末物食材４個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4062")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_406C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40D6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40CC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0178
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I人参４個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_40CC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_40D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4146")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0179
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I液体物食材３個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_413C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41BA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41B0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0180
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "全ての属性のセピス５個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_41B0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_41BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4226")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_421C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0181
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20Iハーブ４個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_421C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4226")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4292")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4288")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0182
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20Iリーフ３個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4288")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4302")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0183
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#56I地のセピス５個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_42F8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4302")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_436E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4364")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0184
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20Iポテト４個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4364")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_436E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43E2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0185
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "全ての属性のセピス５個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_43D8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4452")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4448")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0186
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#57I水のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4448")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44C2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44B8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0187
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#59I風のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_44B8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_452E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4524")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0188
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20Iベリー３個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4524")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_452E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_459E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4594")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0189
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#58I火のセピス15個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4594")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_459E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_460A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4600")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0190
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I珍野菜３個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4600")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_460A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4674")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0191
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I玄米３個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_466A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46E0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46D6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0192
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I珍野菜３個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_46D6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_474A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4740")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0193
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I味噌３個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4740")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_474A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47B6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47AC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0194
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#20I酪農品４個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_47AC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4826")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_481C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0195
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#61I空のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_481C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4826")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4896")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0196
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_488C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4896")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x19, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_490A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4900")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0197
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "全ての属性のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4900")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_490A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_497B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4971")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0198
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#59I風のセピス500個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4971")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_497B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0199
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#56I地のセピス500個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_49E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_49EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A5D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A53")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0200
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#58I火のセピス500個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4A53")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4ACE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0201
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#57I水のセピス500個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4AC4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4ACE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B3F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B35")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0202
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "時空幻のセピス500個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4B35")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B3F")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "交換する\x01",      # 0
            "やめる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_562F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C63")

    #C0203
    ChrTalk(
        0xFE,
        (
            "これは特別立派な魚だし\x01",
            "もう釣れないかもしれないけど……\x01",
            "本当に貰っちまっていいかい？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "はい\x01",        # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C63")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5625")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4D54"),
        (1, "loc_4D8B"),
        (2, "loc_4DC2"),
        (3, "loc_4DFE"),
        (4, "loc_4E35"),
        (5, "loc_4E62"),
        (6, "loc_4EA7"),
        (7, "loc_4ED4"),
        (8, "loc_4F10"),
        (9, "loc_4FDE"),
        (10, "loc_500B"),
        (11, "loc_5038"),
        (12, "loc_506F"),
        (13, "loc_509C"),
        (14, "loc_516A"),
        (15, "loc_51A3"),
        (16, "loc_51DC"),
        (17, "loc_5209"),
        (18, "loc_5242"),
        (19, "loc_527E"),
        (20, "loc_52AB"),
        (21, "loc_52E7"),
        (22, "loc_5314"),
        (23, "loc_5359"),
        (24, "loc_5392"),
        (25, "loc_53CB"),
        (26, "loc_54A7"),
        (27, "loc_54E2"),
        (28, "loc_551D"),
        (29, "loc_5558"),
        (30, "loc_5593"),
        (SWITCH_DEFAULT, "loc_5609"),
    )


    label("loc_4D54")


    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×５\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x4, 5)
    SubItemNumber(0x15E, 1)
    Jump("loc_5609")

    label("loc_4D8B")


    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻のセピス×５\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x6, 5)
    SubItemNumber(0x15F, 1)
    Jump("loc_5609")

    label("loc_4DC2")


    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13B),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x136),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x13B, 1)
    AddItemNumber(0x13C, 1)
    AddItemNumber(0x136, 1)
    SubItemNumber(0x160, 1)
    Jump("loc_5609")

    label("loc_4DFE")


    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空のセピス×５\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x5, 5)
    SubItemNumber(0x161, 1)
    Jump("loc_5609")

    label("loc_4E35")


    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x146),
            "×２\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x146, 2)
    SubItemNumber(0x162, 1)
    Jump("loc_5609")

    label("loc_4E62")


    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x139),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13A),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13D),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13E),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x139, 1)
    AddItemNumber(0x13A, 1)
    AddItemNumber(0x13D, 1)
    AddItemNumber(0x13E, 1)
    SubItemNumber(0x163, 1)
    Jump("loc_5609")

    label("loc_4EA7")


    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x147),
            "×４\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x147, 4)
    SubItemNumber(0x164, 1)
    Jump("loc_5609")

    label("loc_4ED4")


    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13B),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x136),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x13B, 1)
    AddItemNumber(0x13C, 1)
    AddItemNumber(0x136, 1)
    SubItemNumber(0x165, 1)
    Jump("loc_5609")

    label("loc_4F10")


    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×５\x01\x07\x02",

            "#57I水のセピス×５\x01\x07\x02",

            "#58I火のセピス×５\x01\x07\x02",

            "#59I風のセピス×５\x01\x07\x02",

            "#60I時のセピス×５\x01\x07\x02",

            "#61I空のセピス×５\x01\x07\x02",

            "#62I幻のセピス×５\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x0, 5)
    AddSepith(0x1, 5)
    AddSepith(0x2, 5)
    AddSepith(0x3, 5)
    AddSepith(0x4, 5)
    AddSepith(0x5, 5)
    AddSepith(0x6, 5)
    SubItemNumber(0x166, 1)
    Jump("loc_5609")

    label("loc_4FDE")


    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x138),
            "×４\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x138, 4)
    SubItemNumber(0x167, 1)
    Jump("loc_5609")

    label("loc_500B")


    #A0214
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x137),
            "×３\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x137, 3)
    SubItemNumber(0x168, 1)
    Jump("loc_5609")

    label("loc_5038")


    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×５\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x0, 5)
    SubItemNumber(0x169, 1)
    Jump("loc_5609")

    label("loc_506F")


    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x145),
            "×４\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x145, 4)
    SubItemNumber(0x16A, 1)
    Jump("loc_5609")

    label("loc_509C")


    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×５\x01\x07\x02",

            "#57I水のセピス×５\x01\x07\x02",

            "#58I火のセピス×５\x01\x07\x02",

            "#59I風のセピス×５\x01\x07\x02",

            "#60I時のセピス×５\x01\x07\x02",

            "#61I空のセピス×５\x01\x07\x02",

            "#62I幻のセピス×５\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x0, 5)
    AddSepith(0x1, 5)
    AddSepith(0x2, 5)
    AddSepith(0x3, 5)
    AddSepith(0x4, 5)
    AddSepith(0x5, 5)
    AddSepith(0x6, 5)
    SubItemNumber(0x16B, 1)
    Jump("loc_5609")

    label("loc_516A")


    #A0218
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水のセピス×１０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x1, 10)
    SubItemNumber(0x16C, 1)
    Jump("loc_5609")

    label("loc_51A3")


    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I風のセピス×１０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x3, 10)
    SubItemNumber(0x16D, 1)
    Jump("loc_5609")

    label("loc_51DC")


    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x142),
            "×３\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x142, 3)
    SubItemNumber(0x16E, 1)
    Jump("loc_5609")

    label("loc_5209")


    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火のセピス×１５\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x2, 15)
    SubItemNumber(0x16F, 1)
    Jump("loc_5609")

    label("loc_5242")


    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x143),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x144),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x148),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x143, 1)
    AddItemNumber(0x144, 1)
    AddItemNumber(0x148, 1)
    SubItemNumber(0x170, 1)
    Jump("loc_5609")

    label("loc_527E")


    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x134),
            "×３\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x134, 3)
    SubItemNumber(0x171, 1)
    Jump("loc_5609")

    label("loc_52AB")


    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x143),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x144),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x148),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x143, 1)
    AddItemNumber(0x144, 1)
    AddItemNumber(0x148, 1)
    SubItemNumber(0x172, 1)
    Jump("loc_5609")

    label("loc_52E7")


    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x135),
            "×３\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x135, 3)
    SubItemNumber(0x173, 1)
    Jump("loc_5609")

    label("loc_5314")


    #A0226
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            scpstr(SCPSTR_CODE_ITEM, 0x13F),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x140),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x141),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_ITEM, 0x149),
            scpstr(SCPSTR_CODE_LINE_FEED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    AddItemNumber(0x13F, 1)
    AddItemNumber(0x140, 1)
    AddItemNumber(0x141, 1)
    AddItemNumber(0x149, 1)
    SubItemNumber(0x174, 1)
    Jump("loc_5609")

    label("loc_5359")


    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空のセピス×５０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x5, 50)
    SubItemNumber(0x175, 1)
    Jump("loc_5609")

    label("loc_5392")


    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻のセピス×２０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x6, 20)
    SubItemNumber(0x176, 1)
    Jump("loc_5609")

    label("loc_53CB")


    #A0229
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×１０\x01\x07\x02",

            "#57I水のセピス×１０\x01\x07\x02",

            "#58I火のセピス×１０\x01\x07\x02",

            "#59I風のセピス×１０\x01\x07\x02",

            "#60I時のセピス×１０\x01\x07\x02",

            "#61I空のセピス×１０\x01\x07\x02",

            "#62I幻のセピス×１０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x0, 10)
    AddSepith(0x1, 10)
    AddSepith(0x2, 10)
    AddSepith(0x3, 10)
    AddSepith(0x4, 10)
    AddSepith(0x5, 10)
    AddSepith(0x6, 10)
    SubItemNumber(0x177, 1)
    Jump("loc_5609")

    label("loc_54A7")


    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I風のセピス×５００\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x3, 500)
    SubItemNumber(0x178, 1)
    Jump("loc_5609")

    label("loc_54E2")


    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×５００\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x0, 500)
    SubItemNumber(0x179, 1)
    Jump("loc_5609")

    label("loc_551D")


    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火のセピス×５００\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x2, 500)
    SubItemNumber(0x17A, 1)
    Jump("loc_5609")

    label("loc_5558")


    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水のセピス×５００\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x1, 500)
    SubItemNumber(0x17B, 1)
    Jump("loc_5609")

    label("loc_5593")


    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×５００\x01\x07\x02",

            "#61I空のセピス×５００\x01\x07\x02",

            "#62I幻のセピス×５００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x4, 500)
    AddSepith(0x5, 500)
    AddSepith(0x6, 500)
    SubItemNumber(0x17C, 1)
    Jump("loc_5609")

    label("loc_5609")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_562F")

    label("loc_5625")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_562F")

    Jump("loc_32EE")

    label("loc_5634")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5673")

    label("loc_5643")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5657")
    Jump("loc_5673")

    label("loc_5657")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5673")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(2, 4)

    label("loc_5673")

    Jump("loc_3251")

    label("loc_5678")

    Jump("loc_5680")

    label("loc_567D")

    Call(2, 4)

    label("loc_5680")

    TalkEnd(0xB)
    Return()

    # Function_3_320C end

    def Function_4_5684(): pass

    label("Function_4_5684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_57AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_573B")

    #C0235
    ChrTalk(
        0xFE,
        (
            "あんなことがあって\x01",
            "心配なのは分かるけど……\x01",
            "亭主が店にまでついてきちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "ふふ、でも確かに安心だよ。\x01",
            "いっそこれからは\x01",
            "夫婦で営業するかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_57A9")

    label("loc_573B")


    #C0237
    ChrTalk(
        0xFE,
        (
            "亭主も外国から魚を仕入れる仕事を\x01",
            "失業しちまったことだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "いっそこれからは\x01",
            "夫婦で営業するかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57A9")

    Jump("loc_6483")

    label("loc_57AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_57BC")
    Jump("loc_6483")

    label("loc_57BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_58DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589D")

    #C0239
    ChrTalk(
        0xFE,
        (
            "外国に仕事に行っている亭主に、\x01",
            "早く戻って来るよう連絡したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "なんせ、今日の鉄道便を最後に\x01",
            "しばらく運行が差し止められるって\x01",
            "いうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "ふう、ちゃんと帰って\x01",
            "これるのかねえ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_58D8")

    label("loc_589D")


    #C0242
    ChrTalk(
        0xFE,
        (
            "ああ、うちの亭主……\x01",
            "はやく戻ってくればいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58D8")

    Jump("loc_6483")

    label("loc_58DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_597E")

    #C0243
    ChrTalk(
        0xFE,
        (
            "以前、この辺りでやんちゃしてた\x01",
            "赤ジャージの子たち、\x01",
            "この間の襲撃で怪我したんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "う～ん、心配ね……\x01",
            "早く元気な姿を見せて欲しいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6483")

    label("loc_597E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_59C8")

    #C0245
    ChrTalk(
        0xFE,
        "こんな事件が起こるなんてね……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "ああ、不安だわ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6483")

    label("loc_59C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A8E")

    #C0247
    ChrTalk(
        0xFE,
        (
            "今朝方、遊撃士さんが\x01",
            "聞き込みに来ていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "何でも、女性の遊撃士さんが\x01",
            "どこかに行っちゃったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "この天気が悪い日に、\x01",
            "どこに行っちゃったんだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5B06")

    label("loc_5A8E")


    #C0250
    ChrTalk(
        0xFE,
        (
            "何でも、女性の遊撃士さんが\x01",
            "どこかに行っちゃったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "この天気が悪い日に、\x01",
            "どこに行っちゃったんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B06")

    Jump("loc_6483")

    label("loc_5B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5B74")

    #C0252
    ChrTalk(
        0xFE,
        (
            "うちの旦那、今は共和国に\x01",
            "海魚の仕入れに行ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "いい魚は手に入ったかしらね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6483")

    label("loc_5B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4D")

    #C0254
    ChrTalk(
        0xFE,
        (
            "淡水魚って、\x01",
            "普通に食べようとしても\x01",
            "泥臭いものが多いのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "だから、牛乳に\x01",
            "漬け込んだりして\x01",
            "一旦臭みを取るといいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "サッと食べられる\x01",
            "海の魚に比べると、\x01",
            "ちょっと面倒なのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CAF")

    label("loc_5C4D")


    #C0257
    ChrTalk(
        0xFE,
        (
            "淡水魚は一旦牛乳に漬けて\x01",
            "臭みを取るといいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "家で調理するときは\x01",
            "試してみるといいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAF")

    Jump("loc_6483")

    label("loc_5CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DCB")

    #C0259
    ChrTalk(
        0xFE,
        (
            "クロスベルの税収のうち、\x01",
            "約１０％は帝国と共和国に収める\x01",
            "決まりになってるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "もしクロスベルが独立すれば\x01",
            "そんな決まりも無くなって、\x01",
            "生活ももっと楽になるだろうねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "もちろん安全保障の面で\x01",
            "心配はあるけど……\x01",
            "できれば実現してほしいねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5E48")

    label("loc_5DCB")


    #C0262
    ChrTalk(
        0xFE,
        (
            "クロスベルの独立には\x01",
            "私も賛成だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "理不尽な税収なんかから\x01",
            "解放されれば、私らの生活も\x01",
            "もっと楽になるだろうしねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E48")

    Jump("loc_6483")

    label("loc_5E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_601D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FAB")

    #C0264
    ChrTalk(
        0xFE,
        (
            "帝国の宰相さんってのは、\x01",
            "相当頭が切れる人物らしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "お魚を食べると、\x01",
            "頭がよくなるって言うし……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "やっぱり魚をいっぱい食べて\x01",
            "育ったのかねえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0267
    ChrTalk(
        0x101,
        (
            "#00000F……なんだか、\x01",
            "いやに庶民的な絵が\x01",
            "浮かんじゃったなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6018")

    label("loc_5FAB")


    #C0268
    ChrTalk(
        0xFE,
        (
            "お魚を食べると、\x01",
            "頭がよくなるって言うしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "帝国の宰相さんも、\x01",
            "魚をいっぱい食べて\x01",
            "育ったのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6018")

    Jump("loc_6483")

    label("loc_601D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6102")

    #C0270
    ChrTalk(
        0xFE,
        (
            "国境門の警備も、\x01",
            "相当厳重になっているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "共和国からの仕入れ業者さんが、\x01",
            "入国手続きにやたらと\x01",
            "時間を食ったってぼやいてたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "各国のＶＩＰが入国するってのは\x01",
            "大変なことなんだねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_618D")

    label("loc_6102")


    #C0273
    ChrTalk(
        0xFE,
        (
            "共和国からの仕入れ業者さんが、\x01",
            "入国手続きにやたらと\x01",
            "時間を食ったってぼやいてたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "国境門の警備も\x01",
            "厳重になっているみたいだねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_618D")

    Jump("loc_6483")

    label("loc_6192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626B")

    #C0275
    ChrTalk(
        0xFE,
        (
            "釣公師団の建物に入った、\x01",
            "《釣皇倶楽部》……だっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "少し前までいた\x01",
            "《釣公師団》みたいなもんだと\x01",
            "思っていたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "近所付き合いもほとんどないし、\x01",
            "なんだか怪しげなんだよねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_62EA")

    label("loc_626B")


    #C0278
    ChrTalk(
        0xFE,
        (
            "《釣皇倶楽部》……\x01",
            "どうにも怪しげなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "釣り好きの集まりみたいだし\x01",
            "悪い人たちってわけじゃ\x01",
            "なさそうなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62EA")

    Jump("loc_6483")

    label("loc_62EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6376")

    #C0280
    ChrTalk(
        0xFE,
        (
            "う～ん、今日は\x01",
            "あいにくの天気だねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "ま、この程度なら\x01",
            "店を閉めるまでもないけどね。\x01",
            "遠慮なく見てっておくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6483")

    label("loc_6376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6413")

    #C0282
    ChrTalk(
        0xFE,
        "新鮮なお魚はいかが～？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "例の釣公師団の人たち、\x01",
            "最近見かけないねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        "……どこに行っちまったんだろう？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6483")

    label("loc_6413")


    #C0285
    ChrTalk(
        0xFE,
        (
            "釣公師団の人たち、\x01",
            "どこに行っちまったんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "面白い人たちだったし、\x01",
            "見かけないと寂しくなるねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6483")

    Return()

    # Function_4_5684 end

    def Function_5_6484(): pass

    label("Function_5_6484")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_6492")
    SetScenarioFlags(0x2, 3)

    label("loc_6492")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_64A0")
    SetScenarioFlags(0x2, 3)

    label("loc_64A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_64AE")
    SetScenarioFlags(0x2, 3)

    label("loc_64AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_64BC")
    SetScenarioFlags(0x2, 3)

    label("loc_64BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_64CA")
    SetScenarioFlags(0x2, 3)

    label("loc_64CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_64D8")
    SetScenarioFlags(0x2, 3)

    label("loc_64D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_64E6")
    SetScenarioFlags(0x2, 3)

    label("loc_64E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_64F4")
    SetScenarioFlags(0x2, 3)

    label("loc_64F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_6502")
    SetScenarioFlags(0x2, 3)

    label("loc_6502")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_6510")
    SetScenarioFlags(0x2, 3)

    label("loc_6510")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_651E")
    SetScenarioFlags(0x2, 3)

    label("loc_651E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_652C")
    SetScenarioFlags(0x2, 3)

    label("loc_652C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_653A")
    SetScenarioFlags(0x2, 3)

    label("loc_653A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_6548")
    SetScenarioFlags(0x2, 3)

    label("loc_6548")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_6556")
    SetScenarioFlags(0x2, 3)

    label("loc_6556")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_6564")
    SetScenarioFlags(0x2, 3)

    label("loc_6564")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_6572")
    SetScenarioFlags(0x2, 3)

    label("loc_6572")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_6580")
    SetScenarioFlags(0x2, 3)

    label("loc_6580")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_658E")
    SetScenarioFlags(0x2, 3)

    label("loc_658E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_659C")
    SetScenarioFlags(0x2, 3)

    label("loc_659C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_65AA")
    SetScenarioFlags(0x2, 3)

    label("loc_65AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_65B8")
    SetScenarioFlags(0x2, 3)

    label("loc_65B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_65C6")
    SetScenarioFlags(0x2, 3)

    label("loc_65C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_65D4")
    SetScenarioFlags(0x2, 3)

    label("loc_65D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_65E2")
    SetScenarioFlags(0x2, 3)

    label("loc_65E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_65F0")
    SetScenarioFlags(0x2, 3)

    label("loc_65F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_65FE")
    SetScenarioFlags(0x2, 3)

    label("loc_65FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_660C")
    SetScenarioFlags(0x2, 3)

    label("loc_660C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_661A")
    SetScenarioFlags(0x2, 3)

    label("loc_661A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_6628")
    SetScenarioFlags(0x2, 3)

    label("loc_6628")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_6636")
    SetScenarioFlags(0x2, 3)

    label("loc_6636")

    Return()

    # Function_5_6484 end

    def Function_6_6637(): pass

    label("Function_6_6637")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_664A")
    MenuCmd(3, 1, 0x0)

    label("loc_664A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_665D")
    MenuCmd(3, 1, 0x1)

    label("loc_665D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6670")
    MenuCmd(3, 1, 0x2)

    label("loc_6670")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6683")
    MenuCmd(3, 1, 0x3)

    label("loc_6683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6696")
    MenuCmd(3, 1, 0x4)

    label("loc_6696")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66A9")
    MenuCmd(3, 1, 0x5)

    label("loc_66A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66BC")
    MenuCmd(3, 1, 0x6)

    label("loc_66BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66CF")
    MenuCmd(3, 1, 0x7)

    label("loc_66CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66E2")
    MenuCmd(3, 1, 0x8)

    label("loc_66E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66F5")
    MenuCmd(3, 1, 0x9)

    label("loc_66F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6708")
    MenuCmd(3, 1, 0xA)

    label("loc_6708")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_671B")
    MenuCmd(3, 1, 0xB)

    label("loc_671B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_672E")
    MenuCmd(3, 1, 0xC)

    label("loc_672E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6741")
    MenuCmd(3, 1, 0xD)

    label("loc_6741")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6754")
    MenuCmd(3, 1, 0xE)

    label("loc_6754")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6767")
    MenuCmd(3, 1, 0xF)

    label("loc_6767")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677A")
    MenuCmd(3, 1, 0x10)

    label("loc_677A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_678D")
    MenuCmd(3, 1, 0x11)

    label("loc_678D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A0")
    MenuCmd(3, 1, 0x12)

    label("loc_67A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B3")
    MenuCmd(3, 1, 0x13)

    label("loc_67B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67C6")
    MenuCmd(3, 1, 0x14)

    label("loc_67C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67D9")
    MenuCmd(3, 1, 0x15)

    label("loc_67D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67EC")
    MenuCmd(3, 1, 0x16)

    label("loc_67EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67FF")
    MenuCmd(3, 1, 0x17)

    label("loc_67FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6812")
    MenuCmd(3, 1, 0x18)

    label("loc_6812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6825")
    MenuCmd(3, 1, 0x19)

    label("loc_6825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6838")
    MenuCmd(3, 1, 0x1A)

    label("loc_6838")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_684B")
    MenuCmd(3, 1, 0x1B)

    label("loc_684B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_685E")
    MenuCmd(3, 1, 0x1C)

    label("loc_685E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6871")
    MenuCmd(3, 1, 0x1D)

    label("loc_6871")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6884")
    MenuCmd(3, 1, 0x1E)

    label("loc_6884")

    Return()

    # Function_6_6637 end

    def Function_7_6885(): pass

    label("Function_7_6885")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_69AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_693A")

    #C0287
    ChrTalk(
        0xFE,
        (
            "ディーター大統領が拘束、\x01",
            "ですって！\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "国のトップが捕まるなんて\x01",
            "前代未聞よねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州はこれから、\x01",
            "どうなってしまうのかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_69A8")

    label("loc_693A")


    #C0290
    ChrTalk(
        0xFE,
        (
            "国のトップが捕まるなんて\x01",
            "前代未聞よねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州はこれから、\x01",
            "どうなってしまうのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69A8")

    Jump("loc_722A")

    label("loc_69AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_69BB")
    Jump("loc_722A")

    label("loc_69BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6A50")

    #C0292
    ChrTalk(
        0xFE,
        (
            "おばさんもディーター市長……\x01",
            "いや、大統領の演説を見ていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "こうなったら、\x01",
            "とことん独立に向けて\x01",
            "がんばってほしいものよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6B01")

    #C0294
    ChrTalk(
        0xFE,
        (
            "中央広場にあった大きな鐘が\x01",
            "盗まれちゃったみたいねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "どうしてあんなものを\x01",
            "盗んでいったのか、\x01",
            "確証のある噂もないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        "はあ、なんだか不気味だわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6B71")

    #C0297
    ChrTalk(
        0xFE,
        "鉱山町のこと、心配よね……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "警備隊が解決に向けて\x01",
            "動いてるみたいだけど、\x01",
            "大丈夫かしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6BE5")

    #C0299
    ChrTalk(
        0xFE,
        (
            "昨日の列車事故には\x01",
            "本当に驚かされたわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "何にしても、とりあえず\x01",
            "早く復旧してよかったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6C70")

    #C0301
    ChrTalk(
        0xFE,
        (
            "共和国の旅客バスが\x01",
            "この通りを通っていったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "変ねえ……\x01",
            "あのバスは東口のバス停までしか\x01",
            "運行してないはずなのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2E")

    #C0303
    ChrTalk(
        0xFE,
        (
            "独立提唱は、市長が温めていた\x01",
            "アイデアだったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "マクダエル議長は、\x01",
            "どう思っているのかしらね？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "是非ともご意見を\x01",
            "お聞きしたいところだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6DAD")

    label("loc_6D2E")


    #C0306
    ChrTalk(
        0xFE,
        (
            "おばさん、まだ\x01",
            "どちらに投票しようか\x01",
            "迷っているところなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "是非とも、マグダエル議長の意見も\x01",
            "聞いてみたいところだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DAD")

    Jump("loc_722A")

    label("loc_6DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7A")

    #C0308
    ChrTalk(
        0xFE,
        (
            "市長の独立提唱には、\x01",
            "さすがのおばさんも驚いたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "でも、私もクロスベルは\x01",
            "もっと大きく出ていいと思うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "なんてったって、大陸屈指の\x01",
            "貿易都市なんですからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6EF0")

    label("loc_6E7A")


    #C0311
    ChrTalk(
        0xFE,
        (
            "クロスベルは外国に対して\x01",
            "もっと大きく出ていいと思うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "なんてったって、大陸屈指の\x01",
            "貿易都市なんですからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF0")

    Jump("loc_722A")

    label("loc_6EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6F7B")

    #C0313
    ChrTalk(
        0xFE,
        "今日はいよいよ通商会議の当日よね。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        (
            "ディーター市長たちには、\x01",
            "クロスベルのために\x01",
            "是非とも頑張ってもらいたいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6FEF")

    #C0315
    ChrTalk(
        0xFE,
        (
            "オルキスタワーのお披露目、\x01",
            "すごかったわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "おばさん、びっくりして\x01",
            "腰をぬかしちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_6FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_705B")

    #C0317
    ChrTalk(
        0xFE,
        (
            "今日はよく警備中の\x01",
            "警察官を見かけるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "なんだか街が\x01",
            "あわただしい感じがするわねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_705B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_70CF")

    #C0319
    ChrTalk(
        0xFE,
        (
            "ふんふんふ～ん♪\x01",
            "おばさん、子供の頃から\x01",
            "雨が大好きなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "……ちょっと大人気ないかしら？\x02",
    )

    CloseMessageWindow()
    Jump("loc_722A")

    label("loc_70CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_722A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B2")

    #C0321
    ChrTalk(
        0xFE,
        (
            "月末に『通商会議』っていうのが\x01",
            "開かれるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "帝国や共和国だけでなく、\x01",
            "リベールとレミフェリアの偉い人を\x01",
            "クロスベルに招致するらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "……なんだか、とても大きな\x01",
            "行事になりそうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_722A")

    label("loc_71B2")


    #C0324
    ChrTalk(
        0xFE,
        (
            "月末に『通商会議』っていうのが\x01",
            "開かれるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "偉い人が沢山来るみたいだし、\x01",
            "とても大きな行事になりそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_722A")

    TalkEnd(0xFE)
    Return()

    # Function_7_6885 end

    def Function_8_722E(): pass

    label("Function_8_722E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C8")

    #C0326
    ChrTalk(
        0xFE,
        (
            "ディーター大統領がいなくなっても\x01",
            "マクダエル議長がおる。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "議長なら、きっとこの状況も\x01",
            "何とか収めてくれるじゃろうて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7311")

    label("loc_72C8")


    #C0328
    ChrTalk(
        0xFE,
        (
            "マクダエル議長なら、きっとこの状況も\x01",
            "何とか収めてくれるじゃろうて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7311")

    Jump("loc_7F1D")

    label("loc_7316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7324")
    Jump("loc_7F1D")

    label("loc_7324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_746D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73E2")

    #C0329
    ChrTalk(
        0xFE,
        (
            "遊撃士のアリオス殿を\x01",
            "国防長官に任命するとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "だが、彼の功績を考えると\x01",
            "妥当な人選かも知れぬのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "ディーター殿の判断は\x01",
            "さすがというべきじゃろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7468")

    label("loc_73E2")


    #C0332
    ChrTalk(
        0xFE,
        (
            "アリオス殿の功績を考えると\x01",
            "国防長官への任命も妥当じゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "なにせ彼は、クロスベルの守護神とも\x01",
            "言うべき存在なのじゃからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7468")

    Jump("loc_7F1D")

    label("loc_746D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_75CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_754E")

    #C0334
    ChrTalk(
        0xFE,
        (
            "まさか、あのような事件が\x01",
            "このクロスベルで\x01",
            "起こってしまうとはのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "旧市街の方から聞こえてきた\x01",
            "巨大な鬼のような化物の叫び声が、\x01",
            "脳裏から離れんわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        "はあ……今日も眠れんじゃろうな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_75CA")

    label("loc_754E")


    #C0337
    ChrTalk(
        0xFE,
        (
            "襲撃事件の時に聞こえてきた\x01",
            "巨大な鬼のような化物の叫び声が、\x01",
            "脳裏から離れんわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        "はあ……今日も眠れんじゃろうな。\x02",
    )

    CloseMessageWindow()

    label("loc_75CA")

    Jump("loc_7F1D")

    label("loc_75CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7719")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76A1")

    #C0339
    ChrTalk(
        0xFE,
        (
            "マインツの占拠か……\x01",
            "大変なことに\x01",
            "なってしまったのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "市長が独立提唱をした手前、\x01",
            "帝国や共和国の助けも\x01",
            "期待できんじゃろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "ううむ、どうなって\x01",
            "しまうのじゃろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7714")

    label("loc_76A1")


    #C0342
    ChrTalk(
        0xFE,
        (
            "独立提唱をした手前、\x01",
            "帝国や共和国の助けも\x01",
            "期待できんじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "ううむ、どうなって\x01",
            "しまうのじゃろうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7714")

    Jump("loc_7F1D")

    label("loc_7719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7727")
    Jump("loc_7F1D")

    label("loc_7727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7797")

    #C0344
    ChrTalk(
        0xFE,
        (
            "中央広場のほうを\x01",
            "救急車が通っていったそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "はて……\x01",
            "どこぞで事故でもあったかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1D")

    label("loc_7797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7912")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7873")

    #C0346
    ChrTalk(
        0xFE,
        (
            "今度の住民投票……\x01",
            "わしの知人たちの間でも\x01",
            "その話でもちきりじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "だが、周りの意見に\x01",
            "流されるようではいかんぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "だれにとっても\x01",
            "他人事ではないのじゃからな。\x01",
            "よおく考えるがええ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_790D")

    label("loc_7873")


    #C0349
    ChrTalk(
        0xFE,
        (
            "一人一人が考えに考え抜き、\x01",
            "己の意思で投じた票でなければ\x01",
            "投票の意味があるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "だれにとっても\x01",
            "他人事ではないのじゃからな。\x01",
            "よおく考えるがええ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790D")

    Jump("loc_7F1D")

    label("loc_7912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A04")

    #C0351
    ChrTalk(
        0xFE,
        (
            "この地の歴史を知る身としては、\x01",
            "是が非にでも独立を\x01",
            "勝ち取って欲しいものじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "じゃが、帝国と共和国の\x01",
            "実質的支配下にあるが故に\x01",
            "平和が保たれておるのも事実……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "ううむ……\x01",
            "よく考える必要がありそうじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7A7E")

    label("loc_7A04")


    #C0354
    ChrTalk(
        0xFE,
        (
            "従属州としての平和を享受するか、\x01",
            "それを手放してでも独立をとるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "ううむ……\x01",
            "よく考える必要がありそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A7E")

    Jump("loc_7F1D")

    label("loc_7A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B48")

    #C0356
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの周辺は\x01",
            "今朝から封鎖されておる\x01",
            "ようじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "わしも各国首脳をこの目で\x01",
            "見たいところじゃったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "安全を考えると\x01",
            "仕方ないのかもしれんのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7BB2")

    label("loc_7B48")


    #C0359
    ChrTalk(
        0xFE,
        (
            "オルキスタワー周辺は\x01",
            "今朝から封鎖されておるようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "わしも各国首脳をこの目で\x01",
            "見たかったのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BB2")

    Jump("loc_7F1D")

    label("loc_7BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C97")

    #C0361
    ChrTalk(
        0xFE,
        (
            "ロックスミス大統領のリムジンが\x01",
            "この道を通っていったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "さすが大統領の車じゃ、\x01",
            "白と金を基調とした\x01",
            "豪華な車体じゃったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "あれほどの車は、\x01",
            "大陸中を探しても\x01",
            "なかなかないじゃろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7D1E")

    label("loc_7C97")


    #C0364
    ChrTalk(
        0xFE,
        (
            "ロックスミス大統領のリムジンは、\x01",
            "それはそれは豪華なものじゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "あれほどの車は、\x01",
            "大陸中を探しても\x01",
            "なかなかないじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D1E")

    Jump("loc_7F1D")

    label("loc_7D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7DBD")

    #C0366
    ChrTalk(
        0xFE,
        (
            "各国の首脳たちは、\x01",
            "明日クロスベル入りするという\x01",
            "話じゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "滅多にない機会じゃ、\x01",
            "この目で彼らを見ることが\x01",
            "できればいいがのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F1D")

    label("loc_7DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7DCB")
    Jump("loc_7F1D")

    label("loc_7DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA0")

    #C0368
    ChrTalk(
        0xFE,
        (
            "ディーター新市長は、\x01",
            "マクダエル議長と上手く協力して\x01",
            " 政 #4Rまつりごと#に励んでいるようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "市長と議長の協力など、\x01",
            "昔では考えられなかったことじゃ。\x01",
            "ほっほ、全く良い事だのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7F1D")

    label("loc_7EA0")


    #C0370
    ChrTalk(
        0xFE,
        (
            "ディーター新市長は、\x01",
            "ずっとＩＢＣの総裁として\x01",
            "その手腕を発揮しておった。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "ほっほ、全くもって\x01",
            "先がたのしみじゃわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F1D")

    TalkEnd(0xFE)
    Return()

    # Function_8_722E end

    def Function_9_7F21(): pass

    label("Function_9_7F21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_80A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8027")
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0372
    ChrTalk(
        0xFE,
        (
            "大統領が拘束されたり、\x01",
            "妙な青白い樹が現れたり……\x01",
            "なんだか色々な事が起こってるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "元の日常に完全に戻るなんて\x01",
            "出来るのかねえ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    #C0374
    ChrTalk(
        0x10,
        "兄たん、どうしたのー？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    #C0375
    ChrTalk(
        0xFE,
        "ハハ、なんでもないさ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0xF, 0x10E, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_809F")

    label("loc_8027")


    #C0376
    ChrTalk(
        0xFE,
        "……ま、なるようになるよな。\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "俺にとって一番大事なのは\x01",
            "メイリンを守ってくこと……\x01",
            "それさえ忘れなきゃ大丈夫だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_809F")

    Jump("loc_8E25")

    label("loc_80A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_80B2")
    Jump("loc_8E25")

    label("loc_80B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8243")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_819E")

    #C0378
    ChrTalk(
        0xFE,
        (
            "帝国と共和国に\x01",
            "目をつけられちまうのは、\x01",
            "確かに怖いけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "でも……クロスベルのためだ、\x01",
            "俺たち市民が腹を括らなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "それに、どんなことがあっても\x01",
            "メイリンだけは絶対に\x01",
            "俺が守ってみせるからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_823E")

    label("loc_819E")


    #C0381
    ChrTalk(
        0xFE,
        (
            "メイリンをそばにおきたいって\x01",
            "クロンクさんに頼みこんだら、\x01",
            "快くＯＫしてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "話が分かる人でよかったよ。\x01",
            "見えるところにいれば\x01",
            "安心できるからさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_823E")

    Jump("loc_8E25")

    label("loc_8243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8251")
    Jump("loc_8E25")

    label("loc_8251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_831F")

    #C0383
    ChrTalk(
        0xFE,
        (
            "マインツのほう、\x01",
            "武装集団が現れたんだってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "町にそんなもんが現れるなんて、\x01",
            "相当恐ろしい思いをしてるだろうな……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "早いとこ、警備隊が\x01",
            "追っ払ってくれたらいいんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8391")

    label("loc_831F")


    #C0386
    ChrTalk(
        0xFE,
        (
            "メイリン、どうしてるかな……\x01",
            "最近物騒だし、心配だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "今日は早めに上がらせてもらって\x01",
            "一緒に帰るかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8391")

    Jump("loc_8E25")

    label("loc_8396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_852A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849B")

    #C0388
    ChrTalk(
        0xFE,
        (
            "バイト先で\x01",
            "作るのに失敗した風車を\x01",
            "メイリンにやったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "そしたら、どうしても\x01",
            "今日はこれで遊びたいって\x01",
            "聞かなくってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "正直、わざわざ雨の日に\x01",
            "出歩きたくないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "……ま、メイリンが\x01",
            "喜んでるからいいけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8525")

    label("loc_849B")


    #C0392
    ChrTalk(
        0xFE,
        (
            "しかしまあ、あんな\x01",
            "ガラクタ同然の失敗作で\x01",
            "喜んでくれるなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "……次はもっと\x01",
            "ちゃんとしたやつを\x01",
            "プレゼントしてやらねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8525")

    Jump("loc_8E25")

    label("loc_852A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_85BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85A8")

    #C0394
    ChrTalk(
        0xFE,
        (
            "うーん……\x01",
            "オレの作った風車、\x01",
            "全然売れねえなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "って、アレ！？\x01",
            "いつの間にか売れてる！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_85BA")

    label("loc_85A8")


    #C0396
    ChrTalk(
        0xFE,
        "ぽかーん……\x02",
    )

    CloseMessageWindow()

    label("loc_85BA")

    Jump("loc_8E25")

    label("loc_85BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8661")

    #C0397
    ChrTalk(
        0xFE,
        (
            "がんばって作った風車を、\x01",
            "やっと１コだけ店に\x01",
            "置いてもらえたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "自分で作ったものが\x01",
            "店に並んでいるのって……\x01",
            "なんていうか、いいモンだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E25")

    label("loc_8661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_87A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8741")

    #C0399
    ChrTalk(
        0xFE,
        (
            "クロンクさん、\x01",
            "あんなスゲエ模型を\x01",
            "作っちまうんだからなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "オレも手先の器用さには\x01",
            "自信はあったけど、いまだに\x01",
            "風車すら失敗ばかりだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "ふう、なんだか自信を\x01",
            "なくしちゃいそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_87A3")

    label("loc_8741")


    #C0402
    ChrTalk(
        0xFE,
        (
            "とりあえず、今日は雑用に\x01",
            "精を出すとするかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "ふう……\x01",
            "働いてミラを稼ぐって大変だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87A3")

    Jump("loc_8E25")

    label("loc_87A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_88B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8859")

    #C0404
    ChrTalk(
        0xFE,
        (
            "クロンクさんにお願いしたら、\x01",
            "意外にあっさりと\x01",
            "働かせてもらえることになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "う、う～ん……\x01",
            "最初から露店で仕事を\x01",
            "探せばよかったかなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_88AE")

    label("loc_8859")


    #C0406
    ChrTalk(
        0xFE,
        (
            "簡単な工芸品の作り方に、\x01",
            "ミラの管理に……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        "ちょっとずつ仕事を覚えないとな。\x02",
    )

    CloseMessageWindow()

    label("loc_88AE")

    Jump("loc_8E25")

    label("loc_88B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_89E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_897C")

    #C0408
    ChrTalk(
        0xFE,
        "ふーむ、工芸品か……\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "オレって結構手先が器用だし、\x01",
            "こういう職人っぽい仕事って\x01",
            "案外向いてるかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "……でも、こんなオレでも\x01",
            "働かせてくれるかなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_89E0")

    label("loc_897C")


    #C0411
    ChrTalk(
        0xFE,
        (
            "こんな風車を作れたら、\x01",
            "メイリンも喜びそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "よ、よーし……\x01",
            "試しに頼んでみようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89E0")

    Jump("loc_8E25")

    label("loc_89E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AFB")
    OP_4B(0x10, 0xFF)

    #C0413
    ChrTalk(
        0xFE,
        (
            "はあ、仕事探しに\x01",
            "行き詰まっちまったなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x10,
        (
            "兄たん、あっちに\x01",
            "いっぱいあるお店には\x01",
            "おねがいしにいかないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "バ、バカ。\x01",
            "露店なんてやってたら\x01",
            "目立って恥ずかしいじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "オレはもっと室内でやれる\x01",
            "楽な仕事がいいんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xF, 0x10)
    Jump("loc_8B6E")

    label("loc_8AFB")


    #C0417
    ChrTalk(
        0xFE,
        (
            "う～ん、露店かぁ……\x01",
            "ガラじゃないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "でも露店以外に\x01",
            "考えられる仕事は\x01",
            "もう、ほとんど当たったし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B6E")

    Jump("loc_8E25")

    label("loc_8B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8BEB")

    #C0419
    ChrTalk(
        0xFE,
        (
            "今日はメイリンと一緒に\x01",
            "買い物がてら散歩に出てたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "子供って雨でも元気だよなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E25")

    label("loc_8BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CE1")

    #C0421
    ChrTalk(
        0xFE,
        (
            "さっき、赤毛の男が\x01",
            "いきなり俺に絡んできたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "『もっと悩め、それが青春だ～！』とか言って\x01",
            "そのまま中央広場へ歩いていったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "……な、なんか俺よりも\x01",
            "チャランポランそうなヤツだったなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8D59")

    label("loc_8CE1")


    #C0424
    ChrTalk(
        0xFE,
        (
            "さっきの赤毛の男なら、\x01",
            "中央広場へ歩いていったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "……な、なんか俺よりも\x01",
            "チャランポランそうなヤツだったなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D59")

    Jump("loc_8E25")

    label("loc_8D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF3")

    #C0426
    ChrTalk(
        0xFE,
        (
            "ちょっと前から\x01",
            "仕事を探し始めたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "はあ、なかなか\x01",
            "雇ってくれるとこなんて\x01",
            "ねーよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        "早くもくじけそうだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8E25")

    label("loc_8DF3")


    #C0429
    ChrTalk(
        0xFE,
        (
            "なかなか\x01",
            "雇ってくれるとこなんて\x01",
            "ねーよなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E25")

    TalkEnd(0xFE)
    Return()

    # Function_9_7F21 end

    def Function_10_8E29(): pass

    label("Function_10_8E29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8E9C")

    #C0430
    ChrTalk(
        0xFE,
        (
            "兄たん、なんだか\x01",
            "もやもや考えてるのー。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "むつかしいことはいいから、\x01",
            "メイリンと遊んでっ☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A0C")

    label("loc_8E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8EAA")
    Jump("loc_9A0C")

    label("loc_8EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F3C")

    #C0432
    ChrTalk(
        0xFE,
        (
            "今日は兄たんが\x01",
            "おてつだいによんでくれたのー。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "えへへ、兄たんの\x01",
            "『くるくる』が３つもあるの。\x01",
            "売れますよーに！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8F96")

    label("loc_8F3C")


    #C0434
    ChrTalk(
        0xFE,
        (
            "メイリンが手伝ったら、\x01",
            "『くるくる』を\x01",
            "もらえるんだってー。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        "えへへ、たのしみー♪\x02",
    )

    CloseMessageWindow()

    label("loc_8F96")

    Jump("loc_9A0C")

    label("loc_8F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_908D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9024")

    #C0436
    ChrTalk(
        0xFE,
        (
            "おじいちゃんも兄たんも\x01",
            "どっかにいっちゃったのー。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "メイリン、今日は\x01",
            "おばあちゃんちであそぼっかな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9088")

    label("loc_9024")


    #C0438
    ChrTalk(
        0xFE,
        (
            "おじいちゃんと兄たん、\x01",
            "ちゃれ……ちゃら……\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "……ちゃりちい？\x01",
            "っていうのをやるらしいのー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9088")

    Jump("loc_9A0C")

    label("loc_908D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9145")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9124")

    #C0440
    ChrTalk(
        0xFE,
        (
            "メイリン、らいねんは、\x01",
            "もう“にちよーがっこー”なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xFE,
        (
            "だから、さみしーけど\x01",
            "兄たんをおうえんするのっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_9140")

    label("loc_9124")


    #C0442
    ChrTalk(
        0xFE,
        "兄たん、がんばるのー！\x02",
    )

    CloseMessageWindow()

    label("loc_9140")

    Jump("loc_9A0C")

    label("loc_9145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_91E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91A3")

    #C0443
    ChrTalk(
        0xFE,
        (
            "これ、兄たんのつくった\x01",
            "くるくるなのー！\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        "まわるまわる～♪\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_91DF")

    label("loc_91A3")


    #C0445
    ChrTalk(
        0xFE,
        (
            "このくるくる、\x01",
            "兄たんが作ったんだよー！\x01",
            "すごいよね～♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91DF")

    Jump("loc_9A0C")

    label("loc_91E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9239")

    #C0446
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、\x01",
            "むつかしー顔をしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        "……つまんないの……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A0C")

    label("loc_9239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9321")
    OP_4B(0x14, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C4")

    #C0448
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、\x01",
            "おひげおひげー☆\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        "ぐい、ぐいーん♪\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x14,
        (
            "あたたた……\x01",
            "これこれ、引っ張っちゃいかん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9318")

    label("loc_92C4")


    #C0451
    ChrTalk(
        0xFE,
        "ぐい、ぐいーん♪\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x14,
        (
            "メ、メイリンや、\x01",
            "意外にパワフルじゃのう……\x01",
            "あたたた……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9318")

    OP_4C(0x14, 0xFF)
    Jump("loc_9A0C")

    label("loc_9321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_93E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93A6")

    #C0453
    ChrTalk(
        0xFE,
        (
            "兄たん、いっしょけんめー\x01",
            "はたらいてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "でも、メイリンとも\x01",
            "遊んでほしーの……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xFE, 0xE1, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_93E2")

    label("loc_93A6")


    #C0455
    ChrTalk(
        0xFE,
        (
            "兄たん、メイリンも\x01",
            "いっしょにいたいのー！\x01",
            "……くすん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93E2")

    Jump("loc_9A0C")

    label("loc_93E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9458")

    #C0456
    ChrTalk(
        0xFE,
        (
            "兄たん、くるくるのお店で\x01",
            "はたらくらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "お仕事みつかって\x01",
            "よかったねー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9490")

    label("loc_9458")


    #C0458
    ChrTalk(
        0xFE,
        (
            "よかったけど……\x01",
            "ちょっとさみしいの。\x01",
            "……くすん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9490")

    Jump("loc_9A0C")

    label("loc_9495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_961F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9589")
    OP_4B(0xF, 0xFF)

    #C0459
    ChrTalk(
        0xFE,
        (
            "くるくる回ってるの、\x01",
            "たのしーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        "くるくるくるくる……♪\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x10)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0x10, 0)

    #C0461
    ChrTalk(
        0xF,
        (
            "わわっ、メイリン！？\x01",
            "おまえ目を回してるじゃねーか！\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        "くるくるくらくら……\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Jump("loc_961A")

    label("loc_9589")

    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x10, 0)
    TurnDirection(0x10, 0xF, 0)

    #C0463
    ChrTalk(
        0xF,
        "だ、大丈夫かメイリン。\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        (
            "（ふらふら……）\x01",
            "だいじょーぶにゃにょ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xF,
        "大丈夫じゃないだろそれは……\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)

    label("loc_961A")

    Jump("loc_9A0C")

    label("loc_961F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96F9")
    OP_4B(0xF, 0xFF)

    #C0466
    ChrTalk(
        0xFE,
        (
            "兄たん、最近あんまり\x01",
            "あそんでくれないの……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "はやくお仕事みつけて\x01",
            "メイリンとあそんでっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0468
    ChrTalk(
        0xF,
        (
            "はあ、そんな簡単だったら\x01",
            "本当いいんだけどな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_975D")

    label("loc_96F9")


    #C0469
    ChrTalk(
        0xFE,
        (
            "メイリンも兄たんの\x01",
            "お仕事さがし、てつだうのっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        (
            "みつかったら、\x01",
            "一緒にあそんでもらうのー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_975D")

    Jump("loc_9A0C")

    label("loc_9762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_988A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9823")
    OP_4B(0xF, 0xFF)

    #C0471
    ChrTalk(
        0xFE,
        (
            "たらんたらん……♪\x01",
            "ん～、いいにおいなのっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xF,
        (
            "おいメイリン、\x01",
            "まだ袋を開けちゃだめだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xF,
        (
            "せっかくの焼きたてパンが\x01",
            "濡れちまうぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xFE,
        "あいっ☆\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_9885")

    label("loc_9823")


    #C0475
    ChrTalk(
        0xFE,
        (
            "兄たんといっしょに\x01",
            "パンやさんまで\x01",
            "おかいものしてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        "ん～、ほっかほっかでいい匂い☆\x02",
    )

    CloseMessageWindow()

    label("loc_9885")

    Jump("loc_9A0C")

    label("loc_988A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_990B")

    #C0477
    ChrTalk(
        0xFE,
        (
            "赤毛のヒトが、\x01",
            "兄たんの肩をもみもみしていったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        "メイリンも兄たんの肩をもみもみするの～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A0C")

    label("loc_990B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99B8")
    OP_4B(0xF, 0xFF)

    #C0479
    ChrTalk(
        0xFE,
        "兄たん、元気出してっ！\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xFE,
        (
            "お仕事なんてみつからなくても、\x01",
            "メイリンがそばにいるのっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xF,
        (
            "メ、メイリ～ン……\x01",
            "お前だけだよ、俺の味方は。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xF, 0xFF)
    Jump("loc_9A0C")

    label("loc_99B8")


    #C0482
    ChrTalk(
        0xFE,
        (
            "兄たん、お仕事なくって\x01",
            "元気ないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        (
            "メイリンがよしよしして\x01",
            "あげなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A0C")

    TalkEnd(0xFE)
    Return()

    # Function_10_8E29 end

    def Function_11_9A10(): pass

    label("Function_11_9A10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9A8F")

    #C0484
    ChrTalk(
        0xFE,
        (
            "どうも先ほどから、\x01",
            "救急車が何台も市内を\x01",
            "行き来している様子なんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xFE,
        "ううむ、嫌な予感がするのう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9BF0")

    label("loc_9A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9BF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B6C")

    #C0486
    ChrTalk(
        0xFE,
        (
            "孫のロイが\x01",
            "ついに働きはじめてな。\x01",
            "それも露店街で……\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xFE,
        (
            "わしも若い頃\x01",
            "露店街で働いていたからの。\x01",
            "なにやら感慨深いわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xFE,
        (
            "まあ、せいぜい\x01",
            "頑張るがよかろうて。\x01",
            "わしも見守っていくからの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9BF0")

    label("loc_9B6C")


    #C0489
    ChrTalk(
        0xFE,
        (
            "今日は休みが取れたから\x01",
            "わしがメイリンのお守りを\x01",
            "引き受けたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "どれ、せっかくだから\x01",
            "力の限り遊んでやると\x01",
            "するかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BF0")

    TalkEnd(0xFE)
    Return()

    # Function_11_9A10 end

    def Function_12_9BF4(): pass

    label("Function_12_9BF4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9D42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CCB")

    #C0491
    ChrTalk(
        0xFE,
        (
            "うちの男どもは、なんだか最近\x01",
            "私に優しくしてくれるようになったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        (
            "ふふ、ジレと一緒に\x01",
            "買い物に来るなんて何年ぶりかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xFE,
        (
            "こんなときになんだけど、\x01",
            "ちょっとだけ楽しいかも。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9D3D")

    label("loc_9CCB")


    #C0494
    ChrTalk(
        0xFE,
        (
            "ふふ、ジレと一緒に\x01",
            "買い物に来るなんて何年ぶりかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xFE,
        (
            "こんなときになんだけど、\x01",
            "ちょっとだけ楽しいかも。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D3D")

    Jump("loc_A410")

    label("loc_9D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_9D50")
    Jump("loc_A410")

    label("loc_9D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9D5E")
    Jump("loc_A410")

    label("loc_9D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E3A")

    #C0496
    ChrTalk(
        0xFE,
        (
            "この間の事件のせいで、\x01",
            "うちの男どもの仕事場が\x01",
            "休みになっちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xFE,
        (
            "みんな家にいたら\x01",
            "家事の大変さも倍増よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        (
            "まあ、前とは違って\x01",
            "手伝ってくれるように\x01",
            "なったのはありがたいけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9E98")

    label("loc_9E3A")


    #C0499
    ChrTalk(
        0xFE,
        (
            "みんな家にいたら\x01",
            "家事の大変さも倍増よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        (
            "はやく男どもの仕事場が\x01",
            "再開しないかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E98")

    Jump("loc_A410")

    label("loc_9E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9EAB")
    Jump("loc_A410")

    label("loc_9EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9EB9")
    Jump("loc_A410")

    label("loc_9EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F5F")

    #C0501
    ChrTalk(
        0xFE,
        (
            "は～、家事をしないと\x01",
            "やっぱり楽チンね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        (
            "……って、あっ！？\x01",
            "お腹にぜいに……く……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        (
            "……さすがに\x01",
            "ゴロゴロしすぎたかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9F96")

    label("loc_9F5F")


    #C0504
    ChrTalk(
        0xFE,
        (
            "やっぱりそろそろ\x01",
            "家事を再開してあげようかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F96")

    Jump("loc_A410")

    label("loc_9F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A0E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A063")

    #C0505
    ChrTalk(
        0xFE,
        (
            "うちの男ども、最近ようやく\x01",
            "家事の大変さを分かったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "私に家事をしてくれないかって、\x01",
            "頼んでくるようになったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xFE,
        (
            "ふふん、\x01",
            "家事ボイコット作戦は大成功ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A0E2")

    label("loc_A063")


    #C0508
    ChrTalk(
        0xFE,
        (
            "うちの男ども、ようやく\x01",
            "家事の大変さを分かったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xFE,
        (
            "ん～でもどうしよっかな。\x01",
            "私も、もうしばらく\x01",
            "楽をしたいし……♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0E2")

    Jump("loc_A410")

    label("loc_A0E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A0F5")
    Jump("loc_A410")

    label("loc_A0F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A201")

    #C0510
    ChrTalk(
        0xFE,
        (
            "私が家事をしなくなってから、\x01",
            "食事のメニューが本当、\x01",
            "簡素になってきたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        (
            "勝手に出前を頼んじゃったりして\x01",
            "余計にミラをかけちゃうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xFE,
        (
            "ウチは大家族なんだから\x01",
            "少しでも節約しないといけないのに……\x01",
            "まったく、男ってのはダメね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A271")

    label("loc_A201")


    #C0513
    ChrTalk(
        0xFE,
        (
            "……ハッ！\x01",
            "なんでまた私ったら、露店街に……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xFE,
        (
            "家事はしないと決めたんだから、\x01",
            "もう来ないようにしないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A271")

    Jump("loc_A410")

    label("loc_A276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A284")
    Jump("loc_A410")

    label("loc_A284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A3F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A34E")

    #C0515
    ChrTalk(
        0xFE,
        (
            "最近、家事をすっかり\x01",
            "やめちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        (
            "そしたらもー、ほんとラクチン☆\x01",
            "家ではずっとゴロゴロしてるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xFE,
        (
            "ふふ、旦那や息子たちのことなんか\x01",
            "知るもんですかっての。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A3F4")

    label("loc_A34E")


    #C0518
    ChrTalk(
        0xFE,
        (
            "私が家事をしなくなって、\x01",
            "ウチの男どもは毎日大慌てよ。\x01",
            "ふふ、ざまあみなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "……でも、散歩に出ると\x01",
            "ついつい露店街に来ちゃうのよね。\x01",
            "やだやだ、職業病だわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F4")

    Jump("loc_A410")

    label("loc_A3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A407")
    Jump("loc_A410")

    label("loc_A407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A410")

    label("loc_A410")

    TalkEnd(0xFE)
    Return()

    # Function_12_9BF4 end

    def Function_13_A414(): pass

    label("Function_13_A414")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A527")

    #C0520
    ChrTalk(
        0xFE,
        (
            "さすがに１人じゃ心配でさ。\x01",
            "親父と兄弟で、母ちゃんの買い物に\x01",
            "交代でついてくことにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        (
            "面倒だけど、仕方ないよな。\x01",
            "もし母ちゃんが怪我なんかしたら\x01",
            "俺たち、やってけないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "母ちゃんの大切さが、\x01",
            "なんだか改めて分かった気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A564")

    label("loc_A527")


    #C0523
    ChrTalk(
        0xFE,
        (
            "母ちゃんの大切さが、\x01",
            "なんだか改めて分かった気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A564")

    Jump("loc_ABB7")

    label("loc_A569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A577")
    Jump("loc_ABB7")

    label("loc_A577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A615")

    #C0524
    ChrTalk(
        0xFE,
        (
            "いやー、興奮したぜ。\x01",
            "よもやクロスベルが独立国に\x01",
            "なるなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "素直にうれしいけど、\x01",
            "これからどうなるのか\x01",
            "俺にはさっぱり分かんねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABB7")

    label("loc_A615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A623")
    Jump("loc_ABB7")

    label("loc_A623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A76A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A706")

    #C0526
    ChrTalk(
        0xFE,
        (
            "母ちゃんがようやく家事を\x01",
            "再開してくれるようになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        (
            "も、もちろん今度からは\x01",
            "親父と俺たち兄弟にも\x01",
            "分担するようにしたけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        (
            "うちは大家族なんだから、\x01",
            "ちゃんと力をあわせないとな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A765")

    label("loc_A706")


    #C0529
    ChrTalk(
        0xFE,
        (
            "母ちゃんが家事をしなかった時は\x01",
            "ほんとうに大変だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xFE,
        "やっぱり、母は偉大だよな……\x02",
    )

    CloseMessageWindow()

    label("loc_A765")

    Jump("loc_ABB7")

    label("loc_A76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A778")
    Jump("loc_ABB7")

    label("loc_A778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A786")
    Jump("loc_ABB7")

    label("loc_A786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A794")
    Jump("loc_ABB7")

    label("loc_A794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A902")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A878")

    #C0531
    ChrTalk(
        0xFE,
        (
            "母ちゃんが家事をしなくなって、\x01",
            "その大変さが身に染みて分かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xFE,
        (
            "毎日謝ってんだけど\x01",
            "なかなか許してくれなくてさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        (
            "街では独立について賑わってるけど、\x01",
            "ウチはウチで大問題を抱えてるよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A8FD")

    label("loc_A878")


    #C0534
    ChrTalk(
        0xFE,
        (
            "今まで家事を手伝ってこなかった\x01",
            "俺たちが明らかに悪かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xFE,
        (
            "とにかく、母ちゃんが\x01",
            "許してくれるまで\x01",
            "根気強く謝んないとな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8FD")

    Jump("loc_ABB7")

    label("loc_A902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A910")
    Jump("loc_ABB7")

    label("loc_A910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AA52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9C2")

    #C0536
    ChrTalk(
        0xFE,
        (
            "母ちゃんが家事をサボるから、\x01",
            "代わりに親父と兄弟たちで\x01",
            "分担して家事をやってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xFE,
        (
            "おれは食事担当になってね。\x01",
            "うーん、何買えばいいのやら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AA4D")

    label("loc_A9C2")


    #C0538
    ChrTalk(
        0xFE,
        (
            "毎日の食事の献立を考えるのが\x01",
            "こんなに大変だったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xFE,
        (
            "母ちゃんはこんなことを\x01",
            "毎日やってたんだよな。\x01",
            "まったく、恐れ入るよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA4D")

    Jump("loc_ABB7")

    label("loc_AA52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AA60")
    Jump("loc_ABB7")

    label("loc_AA60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_AA6E")
    Jump("loc_ABB7")

    label("loc_AA6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_ABB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB48")

    #C0540
    ChrTalk(
        0xFE,
        (
            "うちの母ちゃん、\x01",
            "最近すっかり家事を\x01",
            "しなくなっちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xFE,
        (
            "親父も俺たち兄弟も\x01",
            "ほとんど手伝わなかったから、\x01",
            "ついにキレちまったみたいでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "うーん……\x01",
            "さすがに困っちまうよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ABB7")

    label("loc_AB48")


    #C0543
    ChrTalk(
        0xFE,
        (
            "母ちゃんがぶち切れて、\x01",
            "家事をまるっきり\x01",
            "しなくなっちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        (
            "うーん……\x01",
            "さすがに困っちまうよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABB7")

    TalkEnd(0xFE)
    Return()

    # Function_13_A414 end

    def Function_14_ABBB(): pass

    label("Function_14_ABBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ACF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC7C")

    #C0545
    ChrTalk(
        0xFE,
        (
            "なんだか街が前の活気を\x01",
            "取り戻した気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xFE,
        (
            "僕も買い物をたくさんして、\x01",
            "経済に貢献しなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xFE,
        (
            "よ～し、安い買い物ルートを\x01",
            "もう一度洗いなおすぞ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_ACEC")

    label("loc_AC7C")


    #C0548
    ChrTalk(
        0xFE,
        (
            "僕も買い物をたくさんして、\x01",
            "経済に貢献しなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        (
            "よ～し、安い買い物ルートを\x01",
            "もう一度洗いなおすぞ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACEC")

    Jump("loc_B4AC")

    label("loc_ACF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_ACFF")
    Jump("loc_B4AC")

    label("loc_ACFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AD79")

    #C0550
    ChrTalk(
        0xFE,
        (
            "僕にはまだ難しい事は\x01",
            "よく分からないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xFE,
        (
            "みんなが選んだ結果なら、\x01",
            "正しいことなんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AD79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ADF3")

    #C0552
    ChrTalk(
        0xFE,
        (
            "この前、教会のミサに行って\x01",
            "女神さまにお祈りしてきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        (
            "はやくクロスベルが\x01",
            "平和になるといいね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_ADF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_AE63")

    #C0554
    ChrTalk(
        0xFE,
        "最近、事件ばかりだよね。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xFE,
        (
            "なんだか怖いし、\x01",
            "今日は買い物を切り上げて\x01",
            "早めに帰ろうかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AE63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AEF2")

    #C0556
    ChrTalk(
        0xFE,
        (
            "えへへ、今日はなんと\x01",
            "１０ミラも浮かせることに\x01",
            "成功したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xFE,
        (
            "アイスでも食べて帰るかなー♪\x01",
            "……雨でちょっと肌寒いけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AEF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_AF71")

    #C0558
    ChrTalk(
        0xFE,
        (
            "うん、今日の買い物は\x01",
            "こんなところかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        (
            "ふふ、安い買い物ルートを\x01",
            "回ったおかげで\x01",
            "ミラがかなり浮いたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AF71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AFE0")

    #C0560
    ChrTalk(
        0xFE,
        (
            "だんだんと\x01",
            "新しい買い物ルートが\x01",
            "見えてきた気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xFE,
        (
            "節約するって\x01",
            "本当に大変だね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_AFE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AFEE")
    Jump("loc_B4AC")

    label("loc_AFEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B144")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0B3")

    #C0562
    ChrTalk(
        0xFE,
        (
            "周りの人と競争して\x01",
            "いかに安いものを買えるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        (
            "セールやバーゲンの楽しさって、\x01",
            "そこにあると思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        (
            "欲しいものが\x01",
            "安く買えたときの喜びは\x01",
            "まさに格別だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B13F")

    label("loc_B0B3")


    #C0565
    ChrTalk(
        0xFE,
        (
            "セールやバーゲンで\x01",
            "欲しいものが安く買えたときの\x01",
            "喜びは格別だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        (
            "特に僕の場合、\x01",
            "余ったミラがお小遣いになるから\x01",
            "喜びも倍増なのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B13F")

    Jump("loc_B4AC")

    label("loc_B144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B1E9")

    #C0567
    ChrTalk(
        0xFE,
        (
            "今日はオルキスタワーの除幕式で\x01",
            "かなり盛り上がったよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xFE,
        (
            "……なんだかセールの匂いがするな。\x01",
            "今日は普段行かない\x01",
            "百貨店とかも回ってみようっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_B1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2AA")

    #C0569
    ChrTalk(
        0xFE,
        (
            "節約のコツは、情報収集さ。\x01",
            "タイムセールやバーゲンは\x01",
            "見落とさないようにしないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        (
            "えーっと、今の時間帯だと\x01",
            "露店で買い物すれば\x01",
            "そこそこミラが浮きそうだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B310")

    label("loc_B2AA")


    #C0571
    ChrTalk(
        0xFE,
        (
            "お小遣いのためにも、\x01",
            "節約、節約……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "タイムセールやバーゲンは\x01",
            "見落とさないようにしないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B310")

    Jump("loc_B4AC")

    label("loc_B315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B391")

    #C0573
    ChrTalk(
        0xFE,
        (
            "雨の日は買い物客が少ないから\x01",
            "商品をじっくり見定められるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "ふふ、今日も\x01",
            "いい買い物ができそうだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4AC")

    label("loc_B391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B4AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B431")

    #C0575
    ChrTalk(
        0xFE,
        (
            "ママはお使いを頼むとき、\x01",
            "多めにミラを渡してくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xFE,
        (
            "それで買い物をして、\x01",
            "あまったミラが僕のお小遣いに\x01",
            "なるって寸法さ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B4AC")

    label("loc_B431")


    #C0577
    ChrTalk(
        0xFE,
        (
            "……だけど最近、ママは\x01",
            "買い物総額のギリギリしか\x01",
            "ミラを渡してくれないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "う、うーん……\x01",
            "僕のお小遣い計画が……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4AC")

    TalkEnd(0xFE)
    Return()

    # Function_14_ABBB end

    def Function_15_B4B0(): pass

    label("Function_15_B4B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B548")

    #C0579
    ChrTalk(
        0xFE,
        (
            "こんなときくらい\x01",
            "店を休みにしたっていいのに、\x01",
            "マルテも肝が据わってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xFE,
        (
            "まあ、そこがウチの奥さんの\x01",
            "いい所なんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B5CB")

    label("loc_B548")


    #C0581
    ChrTalk(
        0xFE,
        (
            "こんなときくらい\x01",
            "店を休みにしたっていいのに、\x01",
            "マルテも肝が据わってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "まあ、せっかく来たんだし\x01",
            "今日は店を手伝うかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5CB")

    TalkEnd(0xFE)
    Return()

    # Function_15_B4B0 end

    def Function_16_B5CF(): pass

    label("Function_16_B5CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B67C")

    #C0583
    ChrTalk(
        0xFE,
        (
            "テロリストどもに、\x01",
            "オルキスタワーの図面が\x01",
            "渡った可能性が高いらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "だが、ヤツら一体\x01",
            "どこから攻めるつもりなんだ？\x01",
            "穴はないと信じたい所だが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7EE")

    label("loc_B67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B6E5")

    #C0585
    ChrTalk(
        0xFE,
        (
            "『赤い星座』『黒月』共に\x01",
            "今の所こちらには現れず、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xFE,
        "ふう、警戒も楽じゃねえな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B7EE")

    label("loc_B6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B7EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B784")

    #C0587
    ChrTalk(
        0xFE,
        "ああ、特務支援課か。\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xFE,
        (
            "見ての通りこっちは今、\x01",
            "露店通りを警戒中だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        (
            "アンタらはアンタらの\x01",
            "やれることを尽くしてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_B7EE")

    label("loc_B784")


    #C0590
    ChrTalk(
        0xFE,
        (
            "見ての通りこっちは今、\x01",
            "露店通りを警戒中だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        (
            "アンタらはアンタらの\x01",
            "やれることを尽くしてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7EE")

    TalkEnd(0xFE)
    Return()

    # Function_16_B5CF end

    SaveToFile()

Try(main)
