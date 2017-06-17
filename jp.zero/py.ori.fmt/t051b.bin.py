from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t051b.bin",                # FileName
        "t051b",                    # MapName
        "t051b",                    # Location
        0x003D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 61, 0, 1, 0, 2],
    )

    BuildStringList((
        "t051b",                  # 0
        "ビクセン町長",           # 1
        "アンナ夫人",             # 2
        "ビルマ婆さん",           # 3
        "アミー",                 # 4
        "鉱員ロージー",           # 5
        "ミランダ",               # 6
        "アレク",                 # 7
        "鉱山長ホフマン",         # 8
        "鉱員マックス",           # 9
        "ルリエダ",               # 10
    ))

    AddCharChip((
        "chr/ch23202.itc",                   # 00
        "chr/ch20100.itc",                   # 01
        "chr/ch23700.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch23300.itc",                   # 04
        "chr/ch23000.itc",                   # 05
        "chr/ch26302.itc",                   # 06
        "chr/ch22702.itc",                   # 07
        "apl/ch50130.itc",                   # 08
        "chr/ch24300.itc",                   # 09
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

    DeclNpc(-889,    949,     2640,    90,   341,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-6530,   750,     59,      270,  261,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(49209,   0,       4369,    0,    261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(50959,   0,       1389,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(49689,   0,       1389,    90,   389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(97519,   150,     2130,    180,  469,  0x0, 0,   7,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(98349,   0,       -1129,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(97459,   150,     -1169,   0,    469,  0x0, 0,   6,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(154710,  300,     2500,    315,  471,  0x0, 0,   8,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(147369,  0,       4179,    333,  261,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)

    ScpFunction((
        "Function_0_264",          # 00, 0
        "Function_1_31C",          # 01, 1
        "Function_2_421",          # 02, 2
        "Function_3_42D",          # 03, 3
        "Function_4_6DF",          # 04, 4
        "Function_5_743",          # 05, 5
        "Function_6_787",          # 06, 6
        "Function_7_83B",          # 07, 7
        "Function_8_941",          # 08, 8
        "Function_9_9A4",          # 09, 9
        "Function_10_A5D",         # 0A, 10
        "Function_11_BC6",         # 0B, 11
        "Function_12_D27",         # 0C, 12
        "Function_13_EA6",         # 0D, 13
        "Function_14_F72",         # 0E, 14
        "Function_15_1050",        # 0F, 15
    ))


    def Function_0_264(): pass

    label("Function_0_264")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_32A")
    Jump("loc_420")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_420")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_346")
    Jump("loc_420")

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_354")
    Jump("loc_420")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_362")
    Jump("loc_420")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_370")
    Jump("loc_420")

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_37E")
    Jump("loc_420")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_38C")
    Jump("loc_420")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_39A")
    Jump("loc_420")

    label("loc_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A8")
    Jump("loc_420")

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B6")
    Jump("loc_420")

    label("loc_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_409")
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_3FD")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_404")

    label("loc_3FD")

    TurnDirection(0xE, 0xD, 0)

    label("loc_404")

    Jump("loc_420")

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_417")
    Jump("loc_420")

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_420")

    label("loc_420")

    Return()

    # Function_1_31C end

    def Function_2_421(): pass

    label("Function_2_421")

    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_421 end

    def Function_3_42D(): pass

    label("Function_3_42D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_50B")

    label("loc_4C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50B")

    label("loc_4E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_501")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50B")

    label("loc_501")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_657")
    SetChrSubChip(0xFE, 0x0)

    #C0001
    ChrTalk(
        0xFE,
        "七耀石の取引を独占……か。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "確かに、鉱員の安全には\x01",
            "代えられない……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "今取り引き中の商人もいるのだ。\x01",
            "彼らの信用を失う訳には……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#0003F（町長さん……\x01",
            "  随分悩んでいるみたいだ。）\x02\x03",

            "#0001F（……今夜、奴らはきっと現れる。\x01",
            "  準備が済んだら宿で待機しよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6C5")

    label("loc_657")


    #C0005
    ChrTalk(
        0xFE,
        (
            "おや、君たちか……\x01",
            "今日はこの町に泊まるのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "鉱員に怪我人も出ているんだ。\x01",
            "君たちも気をつけてな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C5")

    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_42D end

    def Function_4_6DF(): pass

    label("Function_4_6DF")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        "あの人……とても悩んでいるみたい。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "何か元気のでる食べ物でも\x01",
            "作ってあげようかしら。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_6DF end

    def Function_5_743(): pass

    label("Function_5_743")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "まったく孫たちときたら、\x01",
            "こんな夜中に騒がしいんだから。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_743 end

    def Function_6_787(): pass

    label("Function_6_787")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79C")
    Call(0, 7)
    Jump("loc_837")

    label("loc_79C")


    #C0010
    ChrTalk(
        0xFE,
        (
            "全くお兄ちゃんったら、\x01",
            "鉱員仲間と飲んでくればよかったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "……ま、こないだマックスさんが\x01",
            "襲われたばっかりだし、\x01",
            "安心っていえば安心だけどさ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_837")

    TalkEnd(0xFE)
    Return()

    # Function_6_787 end

    def Function_7_83B(): pass

    label("Function_7_83B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)

    #C0012
    ChrTalk(
        0xB,
        (
            "お兄ちゃん、\x01",
            "今日も飲み会行かなかったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        (
            "町長から早く家に帰るように\x01",
            "言われてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        "まっすぐ帰って何が悪いんだよ。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        "……強いて言うなら……そうね。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        "……『付き合いが悪い』？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        "う、うるせぇっつーの。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_7_83B end

    def Function_8_941(): pass

    label("Function_8_941")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_956")
    Call(0, 7)
    Jump("loc_9A0")

    label("loc_956")


    #C0018
    ChrTalk(
        0xFE,
        "ちっ、余計なお世話だってんだよ。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "……俺、あんまり酒飲めないし。\x02",
    )

    CloseMessageWindow()

    label("loc_9A0")

    TalkEnd(0xFE)
    Return()

    # Function_8_941 end

    def Function_9_9A4(): pass

    label("Function_9_9A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_9ED")
    TurnDirection(0xFE, 0xF, 0)

    #C0020
    ChrTalk(
        0xFE,
        (
            "ねーねー早く食べようよ。\x01",
            "僕、おなか減った。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A59")

    label("loc_9ED")


    #C0021
    ChrTalk(
        0xFE,
        (
            "お父さんが帰ってくるまで\x01",
            "晩ごはんは我慢するんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……おなか減ったなぁ。\x01",
            "早く帰ってこないかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A59")

    TalkEnd(0xFE)
    Return()

    # Function_9_9A4 end

    def Function_10_A5D(): pass

    label("Function_10_A5D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AF1")
    Jump("loc_B3B")

    label("loc_AF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B11")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B3B")

    label("loc_B11")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B31")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B3B")

    label("loc_B31")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B3B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B72")
    Call(0, 11)
    Jump("loc_BBE")

    label("loc_B72")


    #C0023
    ChrTalk(
        0xFE,
        (
            "ああ、お前らか。\x01",
            "鉱山に入るのはいいが、\x01",
            "怪我しないように気を付けろよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_A5D end

    def Function_11_BC6(): pass

    label("Function_11_BC6")

    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    #C0024
    ChrTalk(
        0xD,
        (
            "魔獣に襲われたマックスさん……\x01",
            "まだ怪我はよくならないって？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xF,
        (
            "ああ……\x01",
            "傷自体はそこまで深いものじゃ\x01",
            "ないそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xF,
        (
            "何せ、足を噛まれちまってるからな。\x01",
            "無理はさせないほうがいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        "そう……心配ねぇ。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xD,
        "……あなたも気をつけてよね？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xF,
        (
            "はは、大丈夫だ。\x01",
            "なんせ俺は鉱山長だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xD,
        "根拠のあることを言ってよね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_11_BC6 end

    def Function_12_D27(): pass

    label("Function_12_D27")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DBB")
    Jump("loc_E05")

    label("loc_DBB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DDB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E05")

    label("loc_DDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E05")

    label("loc_DFB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E05")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E45")
    Call(0, 11)
    Jump("loc_E72")

    label("loc_E45")


    #C0031
    ChrTalk(
        0xFE,
        (
            "この人、命知らずだから\x01",
            "心配なのよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E72")

    Jump("loc_E9E")

    label("loc_E77")


    #C0032
    ChrTalk(
        0xFE,
        (
            "はぁ、あの人ったら\x01",
            "遅いわねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_D27 end

    def Function_13_EA6(): pass

    label("Function_13_EA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBB")
    Call(0, 14)
    Jump("loc_F6E")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3C")

    #C0033
    ChrTalk(
        0xFE,
        (
            "俺は鉱山に入ってないと\x01",
            "夜は寝付けないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "……くそっ。\x01",
            "魔獣に襲われたりなんか\x01",
            "しなけりゃなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_F6E")

    label("loc_F3C")


    #C0035
    ChrTalk(
        0xFE,
        (
            "あー……\x01",
            "こんな生活じゃ\x01",
            "体がなまっちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6E")

    TalkEnd(0xFE)
    Return()

    # Function_13_EA6 end

    def Function_14_F72(): pass

    label("Function_14_F72")


    #C0036
    ChrTalk(
        0xFE,
        "あー……夜が長ぇなぁ……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "買ってきてもらった本も\x01",
            "読んじまったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……よかったらこの本、読むか？\x01",
            "なんだったらくれてやるよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C8, 1)
    SetScenarioFlags(0x9C, 2)
    Return()

    # Function_14_F72 end

    def Function_15_1050(): pass

    label("Function_15_1050")

    TalkBegin(0xFE)

    #C0040
    ChrTalk(
        0xFE,
        (
            "うちの旦那、\x01",
            "昼間っからしょげちゃっててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "……怪我、早く治るといいわね……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1050 end

    SaveToFile()

Try(main)
