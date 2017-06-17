from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3000.bin",                # FileName
        "e3000",                    # MapName
        "e3000",                    # Location
        0x00A1,                     # MapIndex
        "ed7104",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 2, 0, 3],
    )

    BuildStringList((
        "e3000",                  # 0
        "レクター",               # 1
        "男の子",                 # 2
        "男性",                   # 3
        "女性",                   # 4
        "観光客",                 # 5
        "SE制御",                 # 6
    ))

    AddCharChip((
        "chr/ch07400.itc",                   # 00
        "chr/ch20602.itc",                   # 01
        "chr/ch20202.itc",                   # 02
        "chr/ch20302.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "apl/ch50352.itc",                   # 05
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

    DeclNpc(2950,    4099,    -7750,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1169,   4250,    899,     180,  341,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(1029,    4250,    899,     180,  341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(2210,    4250,    899,     180,  341,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       4099,    12760,   0,    257,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_285",          # 01, 1
        "Function_2_2A5",          # 02, 2
        "Function_3_2CB",          # 03, 3
        "Function_4_2E3",          # 04, 4
        "Function_5_2F2",          # 05, 5
        "Function_6_4F0",          # 06, 6
        "Function_7_67B",          # 07, 7
        "Function_8_867",          # 08, 8
        "Function_9_9F5",          # 09, 9
        "Function_10_AA2",         # 0A, 10
        "Function_11_C30",         # 0B, 11
        "Function_12_1EA8",        # 0C, 12
        "Function_13_1EC9",        # 0D, 13
        "Function_14_1EEA",        # 0E, 14
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_213")
    Sleep(600)
    Jump("loc_23C")

    label("loc_213")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22A")
    Sleep(400)
    Jump("loc_23C")

    label("loc_22A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23C")
    Sleep(200)

    label("loc_23C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_284")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Jump("loc_23C")

    label("loc_284")

    Return()

    # Function_0_1F0 end

    def Function_1_285(): pass

    label("Function_1_285")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A4")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1)
    Jump("Function_1_285")

    label("loc_2A4")

    Return()

    # Function_1_285 end

    def Function_2_2A5(): pass

    label("Function_2_2A5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BB")
    Event(0, 14)

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2CA")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_2CA")

    Return()

    # Function_2_2A5 end

    def Function_3_2CB(): pass

    label("Function_3_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    Call(0, 4)

    label("loc_2DC")

    Sound(479, 1, 100, 0)
    Return()

    # Function_3_2CB end

    def Function_4_2E3(): pass

    label("Function_4_2E3")

    SetChrChipByIndex(0x8, 0x5)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 1)
    Return()

    # Function_4_2E3 end

    def Function_5_2F2(): pass

    label("Function_5_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_308")
    Call(0, 11)
    Jump("loc_4EF")

    label("loc_308")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8")

    #C0001
    ChrTalk(
        0x8,
        (
            "#3506Fそれにしてもあのオヤジ、\x01",
            "競売会#6Rパ ー テ ィ#の代理出席のことしか\x01",
            "教えてくれてねーんだもんな。\x02\x03",

            "#3500Fテーマパークなんてモンが\x01",
            "あると知ってりゃ\x01",
            "朝一でクロスベル入りしたのによ～。\x02",
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

    #C0002
    ChrTalk(
        0x101,
        "#0012F根っからの遊び人ですね……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#3504Fうむ、失敬だなキミは。\x01",
            "俺はただ欲望に忠実なだけだぜェ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4EC")

    label("loc_4A8")


    #C0004
    ChrTalk(
        0x8,
        (
            "#3510F到着したら\x01",
            "噂のテーマパークとやらに\x01",
            "直行してみるかなァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EC")

    TalkEnd(0x8)

    label("loc_4EF")

    Return()

    # Function_5_2F2 end

    def Function_6_4F0(): pass

    label("Function_6_4F0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_584")
    Jump("loc_5CE")

    label("loc_584")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CE")

    label("loc_5A4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CE")

    label("loc_5C4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D")

    #C0005
    ChrTalk(
        0xFE,
        (
            "わーいわーい、水上バスだぁ！\x01",
            "速い速～い！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_648")
    SetScenarioFlags(0xB6, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_648")

    Jump("loc_673")

    label("loc_64D")


    #C0006
    ChrTalk(
        0xFE,
        "ミシュラムにはいつ着くのカナ～？\x02",
    )

    CloseMessageWindow()

    label("loc_673")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_4F0 end

    def Function_7_67B(): pass

    label("Function_7_67B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_70F")
    Jump("loc_759")

    label("loc_70F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_72F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_759")

    label("loc_72F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_74F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_759")

    label("loc_74F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_759")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81D")

    #C0007
    ChrTalk(
        0xFE,
        (
            "記念祭中は忙しかったが\x01",
            "ようやく家族との時間が取れたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "今日一日は、家族の団欒を\x01",
            "大いに楽しむつもりだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_818")
    SetScenarioFlags(0xB6, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_818")

    Jump("loc_85F")

    label("loc_81D")


    #C0009
    ChrTalk(
        0xFE,
        (
            "今日一日は仕事を忘れて、\x01",
            "家族との団欒を\x01",
            "満喫するつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_67B end

    def Function_8_867(): pass

    label("Function_8_867")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FB")
    Jump("loc_945")

    label("loc_8FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_91B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_945")

    label("loc_91B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_945")

    label("loc_93B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_945")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0010
    ChrTalk(
        0xFE,
        (
            "夫が息子との時間を作ってくれて\x01",
            "本当にうれしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "この子がいい思い出を\x01",
            "作ってくれるといいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9ED")
    SetScenarioFlags(0xB6, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9ED")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_867 end

    def Function_9_9F5(): pass

    label("Function_9_9F5")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        (
            "ミシュラムには高級レストランが\x01",
            "あるそうじゃないかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "美食を求めてウン十年……\x01",
            "ここクロスベルでも美味い料理に\x01",
            "出会えるといいのう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9E")
    SetScenarioFlags(0xB6, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A9E")

    TalkEnd(0xFE)
    Return()

    # Function_9_9F5 end

    def Function_10_AA2(): pass

    label("Function_10_AA2")

    EventBegin(0x0)
    OP_E5()
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    Call(0, 4)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B68")
    FadeToBright(1000, 0)
    OP_68(80, 2300, -22430, 0)
    MoveCamera(11, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(85880, 0)
    OP_68(570, 2300, 64420, 18000)
    SetCameraDistance(45950, 13500)
    MoveCamera(11, 16, 0, 13500)
    Sleep(12000)
    OP_0D()

    label("loc_B68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBB")
    Fade(2000)
    OP_68(60, 4500, -16129, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25520, 0)
    OP_68(60, 4500, 20650, 15000)
    Sleep(12000)
    OP_0D()

    label("loc_BBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C17")
    Fade(2000)
    OP_68(-5400, 4500, -20850, 0)
    MoveCamera(152, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29350, 0)
    OP_68(-5400, 4500, 49430, 15000)
    SetCameraDistance(69180, 9000)
    Sleep(12000)
    OP_0D()

    label("loc_C17")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("e0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_AA2 end

    def Function_11_C30(): pass

    label("Function_11_C30")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50351.itc", 0x1E)
    SetCameraDistance(18440, 0)
    OP_68(2260, 5800, -6790, 0)
    MoveCamera(136, 20, 0, 0)
    OP_6E(500, 0)
    SetChrPos(0x101, 2350, 4100, -6500, 180)
    SetChrPos(0x102, 3550, 4100, -6500, 180)
    SetChrPos(0x103, 2350, 4100, -5500, 180)
    SetChrPos(0x104, 3550, 4100, -5500, 180)
    SetChrPos(0x8, 2950, 4100, -8150, 0)
    FadeToBright(1000, 0)
    StopBGM(0xBB8)
    BeginChrThread(0xD, 0, 0, 12)
    SetCameraDistance(16940, 3000)
    OP_6F(0x10)
    OP_0D()
    EndChrThread(0xD, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7525", 1)

    #C0014
    ChrTalk(
        0x8,
        (
            "#3509F#11P#0W#67Aボクらの前には、\x01",
            "楽園が、待っている～♪\x02\x03",

            "#67Aさあ、手を取って\x01",
            "波打ち際に走り出そう～♪\x02\x03",

            "#3510F#48A白いボートであの島目指そう～♪\x02\x03",

            "#46A魅惑の日焼け跡～♪\x02\x03",

            "#42Aパラソル、ヤシの木、カキ氷～♪\x02\x03",

            "#3504F#60Aキミがいる場所、\x01",
            "そこが、ボクの楽園～♪\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    BeginChrThread(0xD, 0, 0, 13)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x20)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x3E8)
    EndChrThread(0xD, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7104", 0)

    #C0015
    ChrTalk(
        0x101,
        (
            "#0012F#6Pなんか……\x01",
            "メチャメチャ満喫してますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0306F#6Pしかも妙に上手いってのが\x01",
            "逆にイラッ☆と来るよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#3507F#11Pおう、青春は爆発だからな。\x02\x03",

            "#3509F旅先で歌を奏でるのは\x01",
            "どこぞの皇子の\x01",
            "専売特許じゃないんだぜェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        "#0211F#6P意味不明なんですが……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0100F#5Pえっと、レクターさんは\x01",
            "ミシュラムにどういった用件で？\x02\x03",

            "テーマパーク目当てでは\x01",
            "無いみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#3503F#11Pあー、さっきも言ったように\x01",
            "代理として来ただけなんだよな。\x02\x03",

            "#3501F喰えない中年オヤジの\x01",
            "代わりなんだけどよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0005F#6P喰えない中年オヤジ……？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#3501F#11Pうーん、名前くらいは\x01",
            "知ってるんじゃないか？\x02\x03",

            "ギリアス・オズボーンっていう\x01",
            "喰えないオヤジなんだが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0023
    ChrTalk(
        0x101,
        "#0011F#6P#4Sえ゛。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#3505F#11Pあー、やっぱ知ってるか。\x02\x03",

            "#3506Fあのオヤジ、押し出しだけは\x01",
            "やたらといいからなァ。\x02\x03",

            "丁寧にヒゲの手入れなんざして\x01",
            "薔薇の似合うカリスマ美中年でも\x01",
            "気取ってるつもりかっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#0001F#6Pエレボニア帝国宰相、\x01",
            "ギリアス・オズボーン……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        "#0203F#6P……通称《鉄血宰相》ですね。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#0101F#5Pま、まさか……\x01",
            "帝国政府の方だったんですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#3504F#11Pま、オレはただの二等書記官だけどな。\x02\x03",

            "#3500Fクロスベルのトップの１人で\x01",
            "ハルトマンってオッサンがいるだろ？\x02\x03",

            "去年、そいつとギリアスのオッサンが\x01",
            "極秘裏に──と言ってもバレバレだけど\x01",
            "──会談してパイプを作ったんだが。\x02\x03",

            "そのパイプの繋ぎとして\x01",
            "今回オレが派遣されたってわけだ。\x02\x03",

            "#3506Fいや～、宮仕えは大変だぜェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0003F#6Pそ、そうだったんですか……\x02\x03",

            "#0005Fって、そんな事まで\x01",
            "俺たちに話してもいいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#3500F#11Pま、いいんじゃない？\x02\x03",

            "#3509Fどうせアンタら、\x01",
            "ここで死ぬんだし。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x0, 0x7D0)
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
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        "#0007F#6Pな──\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#0301F#6Pてめぇ……\x02",
    )

    CloseMessageWindow()
    OP_68(2380, 5800, -6400, 1200)

    def lambda_15C3():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15C3)
    Sleep(50)

    def lambda_15DB():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15DB)
    Sleep(100)

    def lambda_15F3():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15F3)
    Sleep(50)

    def lambda_160B():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_160B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0033
    ChrTalk(
        0x8,
        (
            "#3504F#11P今、この水上バスに\x01",
            "オレの部下が何人くらい\x01",
            "乗り込んでると思う……？\x02\x03",

            "#3500F多分、片手の指じゃ\x01",
            "足りないんじゃねーかなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0101F#5Pくっ、何の目的で……！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        "#0208F#6P……罠、ですか。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "#3504F#11Pくくくっ……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    VolumeBGM(0x64, 0xBB8)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0037
    ChrTalk(
        0x8,
        (
            "#3509F#4S#11Pわははははははははッ！\x02\x03",

            "#3504Fくっくっ……\x01",
            "いやぁ～、いい反応だ。\x02\x03",

            "#3502Fこんな手に引っかかるなんて\x01",
            "なかなか純朴だな！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0038
    ChrTalk(
        0x101,
        "#0011F#6Pひょっとして……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#0301F#6P……全部ネタってか？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#3509F#11Pいや～、なんつーか。\x02\x03",

            "クロスベルに来るまでの間、\x01",
            "列車の中で読んだスパイ小説の設定、\x01",
            "まんま持ってきただけなんだけどな。\x02\x03",

            "そんなに反応してくれるとは\x01",
            "オレ様ちょっと予想外だぜ～。\x02\x03",

            "#3502Fもしかして律儀に\x01",
            "ネタに付き合ってくれたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#0012F#6Pえ、ええ、まあ。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#0106F#5P……真に迫っていたので\x01",
            "つい釣られてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#3504F#11Pはは、あまりに反応がいいんで\x01",
            "《競売会#6Rオークション#》の潜入調査に来た\x01",
            "警察の人間とか思ったが……\x02\x03",

            "#3500Fさすがにそんなスパイ小説みたいな\x01",
            "話はそうそう転がってねーよなァ？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0012F#6Pっ……ははは。\x01",
            "そんな訳ないじゃないですか。\x02\x03",

            "#0005Fって、それじゃあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#0201F#6Pそれではあなたも\x01",
            "例の《競売会》に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#3504F#11Pああ、そのつもりだ。\x02\x03",

            "#3505Fちなみにオレが\x01",
            "鉄血宰相の代理ってのはナシね。\x02\x03",

            "#3500Fオレはただの\x01",
            "帝国貴族のボンボン息子。\x02\x03",

            "都合がつかなくなった親父の代理で\x01",
            "《競売会》に出席するつもりなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#0103F#5P……そうでしたか。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F#6P悪ぃけど、その格好といい\x01",
            "帝国貴族の若様には見えねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#3505F#11Pおいおい、失礼な奴だなー。\x02\x03",

            "#3504Fお嬢さんたちはともかく、\x01",
            "アンタら野郎共だって\x01",
            "ボンボンには見えないぜ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0006F#6Pうっ……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#0309F#6Pはは、違いねぇ。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        (
            "#0104F#5P……ですが私たちも一応、\x01",
            "招待カードを持っています。\x02\x03",

            "#0100F改めて会場で、顔を合わせる事も\x01",
            "あるかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#3500F#11P……フフ。\x02\x03",

            "#3504Fま、アンタら面白いし、\x01",
            "そん時は声でもかけてくれ。\x02\x03",

            "オヤジどもの相手をするのに\x01",
            "ウンザリしてそーだしなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0003F#6P……分かりました。\x02\x03",

            "#0000Fそれでは今夜、\x01",
            "機会があったら会場で。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "#3509F#11Pおう、ヨロシク～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetCameraDistance(17190, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x20)
    OP_49()
    OP_D5(0x1E)
    SetChrPos(0x0, 2780, 4100, -6430, 180)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 2950, 4100, -7750, 180)
    SetScenarioFlags(0xA3, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_C30 end

    def Function_12_1EA8(): pass

    label("Function_12_1EA8")

    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Return()

    # Function_12_1EA8 end

    def Function_13_1EC9(): pass

    label("Function_13_1EC9")

    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Return()

    # Function_13_1EC9 end

    def Function_14_1EEA(): pass

    label("Function_14_1EEA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性の声")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──お待たせしました。\x02",
        )
    )

    CloseMessageWindow()

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当水上バスはまもなく\x01",
            "《ミシュラム》に到着いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どなた様もお忘れ物のないよう\x01",
            "お気をつけてお降りになって下さい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1EEA end

    SaveToFile()

Try(main)
