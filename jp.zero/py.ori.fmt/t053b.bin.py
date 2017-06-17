from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t053b.bin",                # FileName
        "t053b",                    # MapName
        "t053b",                    # Location
        0x0040,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t053b",                  # 0
        "ベッカライ",             # 1
        "キミィ",                 # 2
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch22700.itc",                   # 02
    ))

    DeclNpc(-129,    0,       3640,    225,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-2009,   0,       2130,    45,   261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)

    DeclActor(-40,     0,       2120,    1000,    -130,    1500,    3640,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_118",          # 00, 0
        "Function_1_1D0",          # 01, 1
        "Function_2_1D1",          # 02, 2
        "Function_3_1D2",          # 03, 3
        "Function_4_1D6",          # 04, 4
        "Function_5_3CC",          # 05, 5
        "Function_6_4FC",          # 06, 6
    ))


    def Function_0_118(): pass

    label("Function_0_118")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_158"),
        (1, "loc_164"),
        (2, "loc_170"),
        (3, "loc_17C"),
        (4, "loc_188"),
        (5, "loc_194"),
        (6, "loc_1A0"),
        (SWITCH_DEFAULT, "loc_1AC"),
    )


    label("loc_158")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_164")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_170")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_17C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_188")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_194")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1CF")

    Return()

    # Function_0_118 end

    def Function_1_1D0(): pass

    label("Function_1_1D0")

    Return()

    # Function_1_1D0 end

    def Function_2_1D1(): pass

    label("Function_2_1D1")

    Return()

    # Function_2_1D1 end

    def Function_3_1D2(): pass

    label("Function_3_1D2")

    Call(0, 4)
    Return()

    # Function_3_1D2 end

    def Function_4_1D6(): pass

    label("Function_4_1D6")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_241")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_260")
    OP_AF(0x56)
    Jump("loc_282")

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_270")
    OP_AF(0x55)
    Jump("loc_282")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_280")
    OP_AF(0x57)
    Jump("loc_282")

    label("loc_280")

    OP_AF(0x55)

    label("loc_282")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C3")

    label("loc_291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A5")
    Jump("loc_3C3")

    label("loc_2A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E")

    #C0001
    ChrTalk(
        0x8,
        (
            "……おう、こんな夜中に来るたぁ\x01",
            "いい度胸じゃねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "ほれ、欲しいモンを言いな。\x01",
            "冷やかしだったらタダじゃおかねえぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3C3")

    label("loc_34E")


    #C0003
    ChrTalk(
        0x8,
        "ほれ、欲しいモンを言え、すぐ言え。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "娘との時間に水を差しやがったんだ、\x01",
            "冷やかしだったらタダじゃおかねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C3")

    Jump("loc_1E3")

    label("loc_3C8")

    TalkEnd(0x8)
    Return()

    # Function_4_1D6 end

    def Function_5_3CC(): pass

    label("Function_5_3CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6")
    OP_93(0xFE, 0x2D, 0x0)
    OP_4B(0x8, 0xFF)

    #C0005
    ChrTalk(
        0xFE,
        (
            "お父ちゃん、\x01",
            "すっかり遅くなっちゃったねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "今日の晩御飯は何にするの～？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "おう、今日はキミィの好きな\x01",
            "ハンバーグを作るぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "わ～い！　お父ちゃんのハンバーグ大好き！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_4F8")

    label("loc_4A6")

    TurnDirection(0xFE, 0x0, 0)

    #C0009
    ChrTalk(
        0xFE,
        (
            "お父ちゃん、町のみんなには厳しいけど\x01",
            "キミィにはとっても優しいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F8")

    TalkEnd(0xFE)
    Return()

    # Function_5_3CC end

    def Function_6_4FC(): pass

    label("Function_6_4FC")

    Return()

    # Function_6_4FC end

    SaveToFile()

Try(main)
