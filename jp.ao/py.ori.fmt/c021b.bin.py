from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c021b.bin",                # FileName
        "c021b",                    # MapName
        "c021b",                    # Location
        0x000B,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c021b",                  # 0
        "オスカー",               # 1
        "モルジュ",               # 2
        "ベネット",               # 3
        "タリーズ",               # 4
        "エルサ",                 # 5
        "モモ",                   # 6
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(119120,  0,       -660,    275,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  4,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  9,  0x0000)
    DeclActor(-72380,  0,       8250,    1200,    -72380,  2450,    8250,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(516, 0)                                        # 0

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2F0",          # 02, 2
        "Function_3_2F1",          # 03, 3
        "Function_4_3A4",          # 04, 4
        "Function_5_3A8",          # 05, 5
        "Function_6_46C",          # 06, 6
        "Function_7_624",          # 07, 7
        "Function_8_6AA",          # 08, 8
        "Function_9_70D",          # 09, 9
        "Function_10_711",         # 0A, 10
        "Function_11_83D",         # 0B, 11
        "Function_12_88D",         # 0C, 12
        "Function_13_99C",         # 0D, 13
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_23C"),
        (1, "loc_248"),
        (2, "loc_254"),
        (3, "loc_260"),
        (4, "loc_26C"),
        (5, "loc_278"),
        (6, "loc_284"),
        (SWITCH_DEFAULT, "loc_290"),
    )


    label("loc_23C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_248")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_254")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_260")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_26C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_278")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_2B3")

    Return()

    # Function_0_204 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    SetChrFlags(0xA, 0x10)
    SetChrPos(0xC, -68850, 0, -980, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9")
    SetChrFlags(0xC, 0x10)

    label("loc_2D9")

    SetChrPos(0xD, -68700, 0, 340, 180)
    SetChrFlags(0xD, 0x10)
    Return()

    # Function_1_2B4 end

    def Function_2_2F0(): pass

    label("Function_2_2F0")

    Return()

    # Function_2_2F0 end

    def Function_3_2F1(): pass

    label("Function_3_2F1")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『お菓子の王国　第一巻』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_3A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ミックスジェラート』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3A0")

    TalkEnd(0xFF)
    Return()

    # Function_3_2F1 end

    def Function_4_3A4(): pass

    label("Function_4_3A4")

    Call(0, 5)
    Return()

    # Function_4_3A4 end

    def Function_5_3A8(): pass

    label("Function_5_3A8")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_468")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_413")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_433")
    OP_AF(0xC9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_463")

    label("loc_433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_447")
    Jump("loc_463")

    label("loc_447")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_463")

    Jump("loc_3B5")

    label("loc_468")

    TalkEnd(0x8)
    Return()

    # Function_5_3A8 end

    def Function_6_46C(): pass

    label("Function_6_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BF")

    #C0003
    ChrTalk(
        0x8,
        (
            "こんな時間に\x01",
            "ウロウロしてるなんて\x01",
            "珍しいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "一応、閉店時間は\x01",
            "過ぎちまってんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "ま、おまえらならいいだろ。\x01",
            "遠慮せず見てってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00000Fサンキュー、オスカー。\x01",
            "是非そうさせてもら……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x10A,
        "#00603F…………………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00006F（か、買い物するにしても\x01",
            "  早く済ませた方がよさそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_623")

    label("loc_5BF")


    #C0009
    ChrTalk(
        0x8,
        (
            "一応、閉店時間は\x01",
            "過ぎちまってんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "ま、おまえらならいいだろ。\x01",
            "遠慮せず見てってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_623")

    Return()

    # Function_6_46C end

    def Function_7_624(): pass

    label("Function_7_624")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        (
            "さーて、そろそろ\x01",
            "後片付けに入るとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "パン屋の仕込みは、\x01",
            "早朝３時からなんでな。\x01",
            "明日に備えてさっさと休まねえと。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_624 end

    def Function_8_6AA(): pass

    label("Function_8_6AA")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xFE,
        (
            "私の作ったパン、\x01",
            "オスカーのに\x01",
            "売り上げで負けてる……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "ぐぬぬ、明日こそは……！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_6AA end

    def Function_9_70D(): pass

    label("Function_9_70D")

    Call(0, 10)
    Return()

    # Function_9_70D end

    def Function_10_711(): pass

    label("Function_10_711")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_839")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_77C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79C")
    OP_AF(0x29)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_834")

    label("loc_79C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B0")
    Jump("loc_834")

    label("loc_7B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0015
    ChrTalk(
        0xB,
        (
            "おやいらっしゃい、\x01",
            "何か入用かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "店はもう少し\x01",
            "開けてるつもりだから、\x01",
            "ゆっくりしてていいからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_834")

    Jump("loc_71E")

    label("loc_839")

    TalkEnd(0xB)
    Return()

    # Function_10_711 end

    def Function_11_83D(): pass

    label("Function_11_83D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_852")
    Call(0, 12)
    Jump("loc_889")

    label("loc_852")


    #C0017
    ChrTalk(
        0xFE,
        (
            "ふふ、モモったらよっぽど\x01",
            "楽しかったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_889")

    TalkEnd(0xFE)
    Return()

    # Function_11_83D end

    def Function_12_88D(): pass

    label("Function_12_88D")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0018
    ChrTalk(
        0xD,
        (
            "……それでね、それでね。\x01",
            "リュウ君、オルキスタワーに\x01",
            "かってに入ろうとしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        (
            "そしたら、モモとアンリちゃんまで\x01",
            "警察の人におこられちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xC,
        (
            "あらあら……\x01",
            "それは大変だったわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xD,
        (
            "でもね、でもね。\x01",
            "とっても楽しかったの……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_88D end

    def Function_13_99C(): pass

    label("Function_13_99C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B1")
    Call(0, 12)
    Jump("loc_A4B")

    label("loc_9B1")


    #C0022
    ChrTalk(
        0xFE,
        (
            "でもリュウ君、面白かったの。\x01",
            "ぜんぶアンリちゃんのせいに\x01",
            "しようとしちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "でも、すぐにばれちゃって、\x01",
            "もっと叱られちゃったの。\x01",
            "くすくす……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4B")

    TalkEnd(0xFE)
    Return()

    # Function_13_99C end

    SaveToFile()

Try(main)
