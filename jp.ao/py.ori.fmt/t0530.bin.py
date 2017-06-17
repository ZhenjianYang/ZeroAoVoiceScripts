from ScenarioHelper import *

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
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0530",                  # 0
        "ベッカライ",             # 1
        "キミィ",                 # 2
        "ハロルド",               # 3
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch09300.itc",                   # 02
    ))

    DeclNpc(-129,    0,       3640,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-4530,   0,       4500,    320,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-3400,   0,       3559,    315,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(-40,     0,       2120,    1000,    -130,    1500,    3640,    0x007E, 0,  3,  0x0000)

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_309",          # 02, 2
        "Function_3_342",          # 03, 3
        "Function_4_346",          # 04, 4
        "Function_5_1422",         # 05, 5
        "Function_6_1B22",         # 06, 6
        "Function_7_1C29",         # 07, 7
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_138 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FE")
    Jump("loc_308")

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_20C")
    Jump("loc_308")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_21A")
    Jump("loc_308")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_245")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1000, 0, 1600, 315)
    TurnDirection(0x8, 0xA, 0)
    Jump("loc_308")

    label("loc_245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_253")
    Jump("loc_308")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_261")
    Jump("loc_308")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_26F")
    Jump("loc_308")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_282")
    SetChrFlags(0x9, 0x80)
    Jump("loc_308")

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_290")
    Jump("loc_308")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A3")
    SetChrFlags(0x9, 0x80)
    Jump("loc_308")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2B1")
    Jump("loc_308")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D5")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    TurnDirection(0x9, 0xA, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_308")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E3")
    Jump("loc_308")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_308")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FF")
    Jump("loc_308")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_308")

    label("loc_308")

    Return()

    # Function_1_1F0 end

    def Function_2_309(): pass

    label("Function_2_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_31B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_341")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_341")

    Return()

    # Function_2_309 end

    def Function_3_342(): pass

    label("Function_3_342")

    Call(0, 4)
    Return()

    # Function_3_342 end

    def Function_4_346(): pass

    label("Function_4_346")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3D0")
    OP_AF(0x58)
    Jump("loc_3F2")

    label("loc_3D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E0")
    OP_AF(0x57)
    Jump("loc_3F2")

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F0")
    OP_AF(0x56)
    Jump("loc_3F2")

    label("loc_3F0")

    OP_AF(0x55)

    label("loc_3F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1419")

    label("loc_401")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415")
    Jump("loc_1419")

    label("loc_415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42D")
    TalkEnd(0x8)
    Return()

    label("loc_42D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1419")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A")

    #C0001
    ChrTalk(
        0x8,
        (
            "鉱山はマインツ住民の\x01",
            "譲れない誇りそのものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "どんな異常事態でも、\x01",
            "誇りを忘れない限りは\x01",
            "きっと乗り越えていける。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "譲れない何かが、\x01",
            "お前等にもきっとあるはずだ。\x01",
            "絶対に忘れるんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5C0")

    label("loc_52A")


    #C0004
    ChrTalk(
        0x8,
        (
            "どんな異常事態でも、\x01",
            "誇りを忘れない限りは\x01",
            "きっと乗り越えていける。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "譲れない何かが、\x01",
            "お前等にもきっとあるはずだ。\x01",
            "絶対に忘れるんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C0")

    Jump("loc_1419")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D4")

    #C0006
    ChrTalk(
        0x8,
        (
            "俺はあまり学がねえから、\x01",
            "無効宣言だのなんだのは\x01",
            "よく分かんねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "早いところキミィやガキどもが\x01",
            "安心して暮らせる世の中に\x01",
            "なってほしいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "……そのためにレジスタンスに\x01",
            "危険な事を任せちまってるのは、\x01",
            "情けねえ話なんだがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_76D")

    label("loc_6D4")


    #C0009
    ChrTalk(
        0x8,
        (
            "レジスタンスに危険な事を\x01",
            "任せちまってるのは情けねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "キミィやガキどもが\x01",
            "安心して暮らせる世の中のためにも、\x01",
            "なんとか頑張って欲しいもんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76D")

    Jump("loc_1419")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D8")

    #C0011
    ChrTalk(
        0x8,
        (
            "レジスタンス狩りを始める前に、\x01",
            "猟兵どもが町長の家まで\x01",
            "挨拶に来やがったそうでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "何様のつもりか、ぬけぬけと\x01",
            "『町から出ないよう注意して下さい』\x01",
            "なんて言いやがったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "レジスタンスに協力してる俺達への\x01",
            "牽制のつもりだったんだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "ちっ、その場に居合わせてたら\x01",
            "占領事件のお返しに\x01",
            "ブン殴ってやったんだがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_95C")

    label("loc_8D8")


    #C0015
    ChrTalk(
        0x8,
        (
            "聞けば、猟兵どもは山道のトンネルに\x01",
            "地雷まで仕掛けやがったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "ちっ、居合わせてたら\x01",
            "絶対にブン殴ってやったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95C")

    Jump("loc_1419")

    label("loc_961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7C")

    #C0017
    ChrTalk(
        0x8,
        (
            "マインツのやつらはよ、\x01",
            "例の猟兵どもの占拠のせいで\x01",
            "まだ沈んでやがる。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "俺も当事者だから\x01",
            "そうなる気持ちは分かるが……\x01",
            "いつまでも沈んでても始まらねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "とにかく、俺や鉱員どもみたいな\x01",
            "元気だけが取り柄のやつらが、\x01",
            "みんなを盛り上げていかねえとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B11")

    label("loc_A7C")


    #C0020
    ChrTalk(
        0x8,
        (
            "あの猟兵どもは恐ろしかったが……\x01",
            "沈んでても始まらねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "俺や鉱員どもみたいな\x01",
            "元気だけが取り柄のやつらが、\x01",
            "みんなを盛り上げていかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B11")

    Jump("loc_1419")

    label("loc_B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B86")

    #C0022
    ChrTalk(
        0x8,
        (
            "俺が足に怪我を負って、\x01",
            "鉱員を引退したのも\x01",
            "こんな雨の日だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        "……古傷が痛みやがるぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1419")

    label("loc_B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5C")

    #C0024
    ChrTalk(
        0x8,
        (
            "キミィは今日、ホフマンとこの\x01",
            "坊主と遊んでるみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "……同じ年代のヤツも少ねえし、\x01",
            "仲良くなるのは別にいいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "将来、付き合いだすとかいう\x01",
            "展開になんねえだろうな……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CF5")

    label("loc_C5C")


    #C0027
    ChrTalk(
        0x8,
        (
            "キミィがホフマンとこの坊主と\x01",
            "将来、まかり間違うようなことが\x01",
            "ないとは言い切れねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "……ホフマンのやつには、\x01",
            "キッチリ釘をさしておかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF5")

    Jump("loc_1419")

    label("loc_CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEE")

    #C0029
    ChrTalk(
        0x8,
        (
            "なんでも、この間の通商会議で\x01",
            "国家独立の話が持ち上がった\x01",
            "そうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "新しい市長サンも、\x01",
            "なかなか粋な事考えやがる。\x01",
            "へへ、大いに結構だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "帝国と共和国にペコペコするのも、\x01",
            "ここらで止めにしなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E5C")

    label("loc_DEE")


    #C0032
    ChrTalk(
        0x8,
        "国家独立、大いに結構だぜ。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "俺たちクロスベルの住民も、\x01",
            "これからはもっと誇り高く\x01",
            "生きていかなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5C")

    Jump("loc_1419")

    label("loc_E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_102F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F82")

    #C0034
    ChrTalk(
        0x8,
        (
            "少し前、キミィを心配しすぎて\x01",
            "ついつい日曜学校の授業に\x01",
            "乱入しちまった事がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "あん時は迷惑をかけちまった。\x01",
            "おれの強面#4Rこわもて#で他の子供も\x01",
            "ビビらせたみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "キミィにこれ以上\x01",
            "恥をかかせるわけにはいかねえ。\x01",
            "もうやんないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_102A")

    label("loc_F82")


    #C0037
    ChrTalk(
        0x8,
        (
            "少し前、キミィを心配しすぎて\x01",
            "ついつい日曜学校の授業に\x01",
            "乱入しちまった事がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "キミィにこれ以上\x01",
            "恥をかかせるわけにはいかねえ。\x01",
            "もうやんないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102A")

    Jump("loc_1419")

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_113B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C9")

    #C0039
    ChrTalk(
        0x8,
        (
            "おっと、ハロルドのヤツが\x01",
            "来やがったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "前回仕入れた食材なんかが\x01",
            "そろそろなくなる頃だ。\x01",
            "へへ、丁度よかったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1136")

    label("loc_10C9")


    #C0041
    ChrTalk(
        0x8,
        (
            "ハロルドのヤツ、\x01",
            "なかなかいいタイミングで\x01",
            "来てくれるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "よし、今回は仕入れ値に\x01",
            "色つけてやるかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1136")

    Jump("loc_1419")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1231")

    #C0043
    ChrTalk(
        0x8,
        (
            "俺はあんま学がねえからよ。\x01",
            "難しいことは分かんねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "通商会議ってやつは要するに、\x01",
            "頭のいい奴らが集まって\x01",
            "色々と話し合う場なんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "若え奴らの未来の為にも\x01",
            "是非とも、いい話し合いを\x01",
            "して欲しいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12CF")

    label("loc_1231")


    #C0046
    ChrTalk(
        0x8,
        (
            "通商会議ってやつは要するに、\x01",
            "頭のいい奴らが集まって\x01",
            "色々と話し合う場なんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "若え奴らの未来の為にも\x01",
            "是非とも、いい話し合いを\x01",
            "して欲しいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CF")

    Jump("loc_1419")

    label("loc_12D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1394")

    #C0048
    ChrTalk(
        0x8,
        (
            "最近、若い鉱員どもの\x01",
            "顔つきが良くなってきてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "この先やってけるのか、\x01",
            "ちっとばかり心配してたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "へへ、どうやら\x01",
            "余計なお世話だったみてえだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1419")

    label("loc_1394")


    #C0051
    ChrTalk(
        0x8,
        (
            "あの教団事件にガンツが\x01",
            "巻き込まれちまったときは、\x01",
            "どうなる事かと思ってたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "へへ、俺なんぞが\x01",
            "心配するまでもなかったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1419")

    Jump("loc_353")

    label("loc_141E")

    TalkEnd(0x8)
    Return()

    # Function_4_346 end

    def Function_5_1422(): pass

    label("Function_5_1422")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_155C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E7")

    #C0053
    ChrTalk(
        0x9,
        (
            "お外にはなんだかヘンな\x01",
            "木が生えてるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "お父ちゃん、それよりも\x01",
            "鉱山が再開したのが\x01",
            "すっごく嬉しいみたいなんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        "えへへ、キミィも嬉しいっ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1557")

    label("loc_14E7")


    #C0056
    ChrTalk(
        0x9,
        (
            "お外にはなんだかヘンな\x01",
            "木が生えてるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "お父ちゃんが嬉しそうだから\x01",
            "キミィ、気にしな～い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1557")

    Jump("loc_1B1E")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_15C4")

    #C0058
    ChrTalk(
        0x9,
        (
            "日曜学校の授業も、\x01",
            "しばらくうけてないな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "シスターさん、\x01",
            "元気だといいけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1E")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1661")

    #C0060
    ChrTalk(
        0x9,
        (
            "お父ちゃん、ドクリツしてから\x01",
            "いっつも怒ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "前はドクリツはいいことだって\x01",
            "言ってたんだけど……\x01",
            "やっぱりよくなかったのかな～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1E")

    label("loc_1661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_175D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F7")

    #C0062
    ChrTalk(
        0x9,
        (
            "キミィはいつでも\x01",
            "スマイル、スマイル♪\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "どんなときでも笑顔でいれば\x01",
            "元気でいられるって、\x01",
            "お父ちゃんが言ってたもん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1758")

    label("loc_16F7")


    #C0064
    ChrTalk(
        0x9,
        (
            "キミィはいつでも\x01",
            "スマイル、スマイル♪\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "町のみんなが\x01",
            "はやく元気になって\x01",
            "くれるといいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1758")

    Jump("loc_1B1E")

    label("loc_175D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_186A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180D")

    #C0066
    ChrTalk(
        0x9,
        (
            "お父ちゃん、雨の日は\x01",
            "なんだか寂しそうなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "やっぱり鉱員のお仕事は\x01",
            "ずっと続けたかったんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "でもキミィ、\x01",
            "今のお父ちゃんも大好き！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1865")

    label("loc_180D")


    #C0069
    ChrTalk(
        0x9,
        (
            "お父ちゃん、雨の日は\x01",
            "なんだか寂しそうなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "キミィが元気付けて\x01",
            "あげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1865")

    Jump("loc_1B1E")

    label("loc_186A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1878")
    Jump("loc_1B1E")

    label("loc_1878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_190A")

    #C0071
    ChrTalk(
        0x9,
        (
            "キミィはまだ、\x01",
            "ドクリツってなんのことか\x01",
            "わかんないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "お父ちゃんはドクリツは\x01",
            "いいことだっていうし、\x01",
            "キミィも賛成～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1E")

    label("loc_190A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1918")
    Jump("loc_1B1E")

    label("loc_1918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1933")
    Call(0, 6)
    Jump("loc_195B")

    label("loc_1933")


    #C0073
    ChrTalk(
        0x9,
        "わーい、みっしぃのぬいぐるみだあ！\x02",
    )

    CloseMessageWindow()

    label("loc_195B")

    Jump("loc_1B1E")

    label("loc_1960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E9")

    #C0074
    ChrTalk(
        0x9,
        (
            "キミィ、大きくなったら\x01",
            "お父ちゃんと一緒にお店をやるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "今のうちにいっぱい\x01",
            "お仕事おぼえないとね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A05")

    label("loc_19E9")


    #C0076
    ChrTalk(
        0x9,
        "お手伝い、お手伝い～♪\x02",
    )

    CloseMessageWindow()

    label("loc_1A05")

    Jump("loc_1B1E")

    label("loc_1A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB4")

    #C0077
    ChrTalk(
        0x9,
        (
            "お父ちゃん、\x01",
            "昔は町一番の鉱員だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "だから、鉱員のみんなには\x01",
            "キビシくしちゃう事も多いけど、\x01",
            "本当はとっても気にかけてるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B1E")

    label("loc_1AB4")


    #C0079
    ChrTalk(
        0x9,
        (
            "お父ちゃん、\x01",
            "昔は町一番の鉱員だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "いつもはキビシいけど、\x01",
            "本当はとっても優しいんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1E")

    TalkEnd(0xFE)
    Return()

    # Function_5_1422 end

    def Function_6_1B22(): pass

    label("Function_6_1B22")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0081
    ChrTalk(
        0x9,
        "あ、ハロルドおいちゃんだー。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        "今日はお父ちゃんと商談？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#03600Fああ、そんなところさ。\x01",
            "色々と商品を持ってきた所でね。\x02\x03",

            "#03609Fふふ、前に君が欲しがってた\x01",
            "みっしぃぐるみも持ってきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "わあ、ほんとにー！？\x01",
            "やったあ！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_6_1B22 end

    def Function_7_1C29(): pass

    label("Function_7_1C29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D70")

    #C0085
    ChrTalk(
        0x101,
        (
            "#00000Fハロルドさん……\x01",
            "マインツに来てたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        (
            "#03600Fええ、アルモリカから\x01",
            "仕入れてきた作物を\x01",
            "届けに来たところです。\x02\x03",

            "#03603F……町の方々はここ最近、\x01",
            "襲撃の悪夢に怯える日々を\x01",
            "過ごされているようです。\x02\x03",

            "#03608F犠牲者が出なかったとはいえ、\x01",
            "確実に襲撃の爪痕は\x01",
            "残されているようですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DDE")

    label("loc_1D70")


    #C0087
    ChrTalk(
        0xA,
        (
            "#03603F私のような商人には\x01",
            "大したことはできませんが……\x02\x03",

            "#03600Fなんとか元気を取り戻して\x01",
            "欲しいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDE")

    Jump("loc_1E33")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DFE")
    Call(0, 6)
    Jump("loc_1E33")

    label("loc_1DFE")


    #C0088
    ChrTalk(
        0xA,
        (
            "#03609Fはは……\x01",
            "やはり子供は\x01",
            "元気が一番ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E33")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C29 end

    SaveToFile()

Try(main)
