from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2020.bin",                # FileName
        "t2020",                    # MapName
        "t2020",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2020",                  # 0
        "ミレイユ准尉",           # 1
        "ミレイユ三尉",           # 2
        "ソーニャ司令",           # 3
        "兵士ロメオ",             # 4
        "ノエル少尉",             # 5
        "ダグラス副司令",         # 6
    ))

    AddCharChip((
        "chr/ch32600.itc",                   # 00
        "chr/ch05702.itc",                   # 01
        "chr/ch41400.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-250,    0,       1409,    0,    389,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(48900,   0,       -27260,  1200,    48900,   850,     -27260,  0x007C, 0,  4,  0x0000)
    DeclActor(-2000,   0,       -4520,   1200,    -2000,   1000,    -4520,   0x007C, 0,  14, 0x0000)
    DeclActor(-38750,  0,       0,       1200,    -40300,  1500,    0,       0x007E, 0,  7,  0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_301",          # 02, 2
        "Function_3_511",          # 03, 3
        "Function_4_629",          # 04, 4
        "Function_5_6E2",          # 05, 5
        "Function_6_BD6",          # 06, 6
        "Function_7_1566",         # 07, 7
        "Function_8_156A",         # 08, 8
        "Function_9_2342",         # 09, 9
        "Function_10_24EB",        # 0A, 10
        "Function_11_3859",        # 0B, 11
        "Function_12_4418",        # 0C, 12
        "Function_13_4E41",        # 0D, 13
        "Function_14_53F6",        # 0E, 14
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_300")
    OP_95(0xFE, -250, 0, 4390, 2000, 0x0)
    OP_95(0xFE, 19540, 0, 4390, 2000, 0x0)
    OP_95(0xFE, -250, 0, 4390, 2000, 0x0)
    OP_95(0xFE, -250, 0, -11650, 2000, 0x0)
    Jump("Function_1_2A0")

    label("loc_300")

    Return()

    # Function_1_2A0 end

    def Function_2_301(): pass

    label("Function_2_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_314")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4FE")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_349")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_37E")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B3")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3FE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_449")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_494")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B8")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36160, 0, 3980, 0)
    Jump("loc_4FE")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_510")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 10)

    label("loc_510")

    Return()

    # Function_2_301 end

    def Function_3_511(): pass

    label("Function_3_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_52B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_559")

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_547")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_559")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_559")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_559")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_578")
    OP_10(0xB, 0x0)
    OP_10(0xD, 0x1)
    OP_10(0xC, 0x0)
    OP_10(0xE, 0x1)
    Jump("loc_584")

    label("loc_578")

    OP_10(0xB, 0x1)
    OP_10(0xD, 0x0)
    OP_10(0xC, 0x1)
    OP_10(0xE, 0x0)

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_5AA")

    SetMapObjFrame(0xFF, "cgf1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cda1", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5E8")
    SetMapObjFrame(0xFF, "cgf1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cda1", 0x1, 0x1)

    label("loc_5E8")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_604")
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_616")
    OP_65(0x2, 0x1)
    Jump("loc_628")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_628")
    OP_65(0x2, 0x1)

    label("loc_628")

    Return()

    # Function_3_511 end

    def Function_4_629(): pass

    label("Function_4_629")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『おうちで作ろう！　スープ特集』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_6DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ミルクポタージュ』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6DE")

    TalkEnd(0xFF)
    Return()

    # Function_4_629 end

    def Function_5_6E2(): pass

    label("Function_5_6E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_77A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_700")
    Call(0, 12)
    Jump("loc_775")

    label("loc_700")


    #C0003
    ChrTalk(
        0xFE,
        (
            "#07900F今、ソーニャ司令とダグラス副司令が\x01",
            "テロ対策の打ち合わせをしてるの。\x02\x03",

            "#07903Fあまり邪魔をしないようにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_775")

    Jump("loc_BD2")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795")
    Call(0, 12)
    Jump("loc_A66")

    label("loc_795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E1")

    #C0004
    ChrTalk(
        0xFE,
        (
            "#07900Fソーニャ司令なら、\x01",
            "今日は保養地ミシュラムで\x01",
            "警備の指揮をとっているわ。\x02\x03",

            "#07903F国賓たちが迎賓館に\x01",
            "招待されているから、\x01",
            "最も重要な警備地点なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00305Fっつーことは\x01",
            "今日はお前が司令の代わりに\x01",
            "ベルガード門の連中を纏めるわけか。\x02\x03",

            "#00306Fはあ、ミレイユなんかに\x01",
            "あのソーニャ司令の\x01",
            "代理が務まるんですかねえ～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0006
    ChrTalk(
        0xFE,
        (
            "#07901Fし、失礼なッ……\x02\x03",

            "#07903F……ふん、あなたの心配なんか結構。\x01",
            "前司令がいたころは似たような事を\x01",
            "よくやらされてたもの。\x02\x03",

            "#07907Fソーニャ司令のお留守は、\x01",
            "絶対に守ってみせるんだから！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        "#00309Fはは、その意気なら大丈夫そうだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A66")

    label("loc_9E1")


    #C0008
    ChrTalk(
        0xFE,
        (
            "#07903F前司令がいたころは\x01",
            "よく代理で門の指揮を\x01",
            "任されていたもの。\x02\x03",

            "#07901Fソーニャ司令のお留守は、\x01",
            "絶対に守ってみせるんだから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A66")

    Jump("loc_BD2")

    label("loc_A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A86")
    Call(0, 12)
    Jump("loc_BD2")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4C")

    #C0009
    ChrTalk(
        0xFE,
        (
            "#07904Fま、まあ、\x01",
            "私の昇進の話はさておき……\x02\x03",

            "#07900F通商会議に向けて、\x01",
            "国境門でも警戒を強めているわ。\x02\x03",

            "旅行者なんかとトラブルを\x01",
            "起こしたりしないよう、\x01",
            "注意してちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BD2")

    label("loc_B4C")


    #C0010
    ChrTalk(
        0xFE,
        (
            "#07900F通商会議に向けて、\x01",
            "国境門でも警戒を強めているわ。\x02\x03",

            "旅行者なんかとトラブルを\x01",
            "起こしたりしないよう、\x01",
            "注意してちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD2")

    TalkEnd(0xFE)
    Return()

    # Function_5_6E2 end

    def Function_6_BD6(): pass

    label("Function_6_BD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE7")
    Jump("loc_1562")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BF5")
    Jump("loc_1562")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C03")
    Jump("loc_1562")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E79")

    #C0011
    ChrTalk(
        0xFE,
        (
            "#07900Fああ、あなたたち……\x02\x03",

            "ベルガード門に来る途中に、\x01",
            "何か危ない目に合わなかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00005Fえっ……？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#00305F別段いつもと変わった様子は\x01",
            "なかったみてえだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "#07900Fそう……\x02\x03",

            "#07903F……どうやら今日は\x01",
            "現れる気配はないみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0015
    ChrTalk(
        0xFE,
        (
            "#07900Fいえ、気にしないで。\x01",
            "こちらの仕事の話だから。\x02\x03",

            "#07903Fもしかしたら近い内に、\x01",
            "あなたたちに相談するかも\x01",
            "しれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00303Fふーむ、よくわからねえが……\x01",
            "助けが必要ならいつでも呼んでくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "#07902Fええ、その時はお願いするわね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EFF")

    label("loc_E79")


    #C0018
    ChrTalk(
        0xFE,
        (
            "#07903F……どうやら今日は\x01",
            "現れる気配はないみたいだし……\x02\x03",

            "#07901F今はとにかく、２大国との緊張状態に\x01",
            "全力であたっていかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFF")

    Jump("loc_1562")

    label("loc_F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1562")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120C")

    #C0019
    ChrTalk(
        0x104,
        (
            "#00309Fいよっ、ミレイユ准尉殿。\x01",
            "元気にしてたかよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0020
    ChrTalk(
        0xFE,
        (
            "#07901F……あなた、\x01",
            "わざとやってるでしょ？\x02\x03",

            "#07906Fこの間三尉に昇進したって\x01",
            "言ったばかりじゃない……\x01",
            "まったくもう。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        (
            "#10109Fあはは……何はともあれ、\x01",
            "昇進、おめでとうございます。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    #C0022
    ChrTalk(
        0xFE,
        (
            "#07909Fふふ、ありがとう曹長。\x02\x03",

            "#07903F昇進はありがたいことだけど……\x01",
            "背負う責任もだんだんと\x01",
            "大きくなってくるでしょう。\x02\x03",

            "#07901Fこれからも一層、\x01",
            "精進を重ねていかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#00306Fやれやれ、あいかわらず\x01",
            "クソマジメなやつだなあ。\x02\x03",

            "#00302Fガンバるばかりじゃ疲れちまうぜ。\x01",
            "テケトーにやっとけ、テケトーに。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)
    OP_63(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0024
    ChrTalk(
        0xFE,
        (
            "#07901F人が折角いい話を\x01",
            "してるっていうのに……\x01",
            "この、ぼけなすランディ！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#10112Fあ、あはは……\x01",
            "（昇進しても相変わらずですね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 4)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_1562")

    label("loc_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C3")

    #C0026
    ChrTalk(
        0x104,
        (
            "#00300Fおっと、そういや……\x01",
            "昇進祝いにプレゼントしたアレ、\x01",
            "つけてるか？\x02\x03",

            "ミシュラムの宝飾店で\x01",
            "買ってきたアレだよ、アレ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D5")

    #C0027
    ChrTalk(
        0x101,
        (
            "#00005Fへえ……\x01",
            "プレゼントなんてしてたのか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1313")

    label("loc_12D5")


    #C0028
    ChrTalk(
        0x101,
        (
            "#00002Fああ……そういえば、\x01",
            "ブローチを買ってたんだっけ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1313")

    TurnDirection(0xFE, 0x104, 500)

    #C0029
    ChrTalk(
        0xFE,
        (
            "#07906Fあのねえ……\x01",
            "つけてるわけないでしょ。\x02\x03",

            "#07900F警備隊の士官ともあろうものが\x01",
            "そんなチャラチャラできないし、\x01",
            "アレは大事にしまって……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0030
    ChrTalk(
        0xFE,
        (
            "#07911Fちっ、ちがっ……ちがうからね！\x01",
            "大事になんてしてないから！\x02\x03",

            "#07909Fそ、そう！　タンスのすみ～の方に\x01",
            "ぞんざいに投げ入れてて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#00309Fわはは、照れるなっつの。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#00204F（……ほほえましいです。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 5)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_1562")

    label("loc_14C3")


    #C0033
    ChrTalk(
        0xFE,
        (
            "#07902Fコ、コホン、とにかく……\x01",
            "昇進したからには、\x01",
            "前以上に頑張っていくつもりよ。\x02\x03",

            "#07903F少しでも司令の力になれるよう、\x01",
            "より一層精進していかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1562")

    TalkEnd(0xFE)
    Return()

    # Function_6_BD6 end

    def Function_7_1566(): pass

    label("Function_7_1566")

    Call(0, 8)
    Return()

    # Function_7_1566 end

    def Function_8_156A(): pass

    label("Function_8_156A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B2C")
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x109, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1607")
    Jump("loc_1651")

    label("loc_1607")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1627")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1651")

    label("loc_1627")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1647")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1651")

    label("loc_1647")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1651")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6C")

    #C0034
    ChrTalk(
        0xA,
        "#02008F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00001Fソーニャ司令……\x01",
            "何か悩み事でもあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "#02003F……警備隊の再編について少しね。\x02\x03",

            "#02000Fマインツ山道で受けた甚大な被害から\x01",
            "元の状態まで立ち直るには、\x01",
            "やはり時間がかかるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#00108Fやはりそうですか……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        "#10108F…………………………\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "#02000F……ノエル曹長。\x01",
            "浮かない顔をしているわね。\x02\x03",

            "#02003F警備隊への復帰を決めたこと、\x01",
            "後悔しているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#10103F……いえ、そんなことは。\x02\x03",

            "#10108Fただ、支援課も忙しいのに\x01",
            "私だけ抜けてしまうのが\x01",
            "少し忍びない気持ちですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00003Fノエル……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "#02003F……警備隊の建て直しに\x01",
            "あなたの力は是非とも欲しいけど……\x02\x03",

            "#02000Fやはり、復帰は止めておくのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x109,
        (
            "#10103Fいえ……\x01",
            "やっぱり決めたことですから。\x02\x03",

            "#10101Fノエル・シーカー、\x01",
            "今日一日の業務が終わり次第、\x01",
            "警備隊に復帰させていただきます！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "#02004F結構。\x02\x03",

            "#02000Fでももちろん、今の貴女はまだ\x01",
            "支援課の出向員よ。\x02\x03",

            "悔いのないよう、残った仕事は\x01",
            "全て片付けてきなさい。\x01",
            "……いいわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x109,
        "#10100Fハッ、了解です！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B22")

    label("loc_1A6C")


    #C0046
    ChrTalk(
        0xA,
        (
            "#02000F警備隊の建て直しに\x01",
            "ノエルの力は是非とも欲しいわ。\x02\x03",

            "#02004F今日一日、悔いのないように\x01",
            "支援課の業務を片付けて、\x01",
            "それから戻ってきてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x109,
        "#10100Fハッ、了解です！\x02",
    )

    CloseMessageWindow()

    label("loc_1B22")

    ClearChrFlags(0xA, 0x10)
    Jump("loc_233E")

    label("loc_1B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1E1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D90")

    #C0048
    ChrTalk(
        0xA,
        (
            "#02002Fロイド君、\x01",
            "昨日はお手柄だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#00005Fえっ……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#00100F昨日の事故現場での\x01",
            "調査の事ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "#02003F……もしあの時、\x01",
            "私が復旧を急がせていたら\x01",
            "脱線事故の原因は不明のままだった。\x02\x03",

            "#02008F真実に辿り着く証拠をこの手で\x01",
            "潰そうとしていたなんて……\x01",
            "私も焦りすぎていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#00203F警備隊の立場を考えたら\x01",
            "仕方ないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00300Fああ、それにあの後\x01",
            "復旧は迅速に進んだんッスよね。\x02\x03",

            "#00302F別に落ち込むことは\x01",
            "ないんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x109,
        "#10100Fそ、そうですよ！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "#02004F……ふふ、そう言って\x01",
            "もらえると私も救われるわ。\x02\x03",

            "#02002F改めて礼を言わせてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 0)
    Jump("loc_1E16")

    label("loc_1D90")


    #C0056
    ChrTalk(
        0xA,
        (
            "#02004Fともかく、おかげで\x01",
            "脱線事故の原因は判明したわ。\x02\x03",

            "#02002F大型魔獣のことは気になるけど……\x01",
            "それはこちらに任せてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E16")

    Jump("loc_233E")

    label("loc_1E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202C")

    #C0057
    ChrTalk(
        0xA,
        (
            "#02000Fあなたたちの調査報告書を\x01",
            "読ませてもらったわ。\x02\x03",

            "#02003F《プレロマ草》……まさか、\x01",
            "教団事件で出てきたという名前が\x01",
            "再び現れるなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00003Fええ……\x01",
            "俺たちも正直驚きました。\x02\x03",

            "#00001F今後の調査はどうなって\x01",
            "行くんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xA,
        (
            "#02003Fそうね、警備隊が\x01",
            "動く事ができないのは\x01",
            "依然変わらないけれど……\x02\x03",

            "#02000Fひとまず、《幻獣》が現れる\x01",
            "原因が判明しただけでも\x01",
            "大きな進歩だといえるわ。\x02\x03",

            "あなたたちは、このまま\x01",
            "できる範囲での調査を\x01",
            "続けてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        "#00302Fあいよ、任せてくださいッス。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 7)
    Jump("loc_20C3")

    label("loc_202C")


    #C0061
    ChrTalk(
        0xA,
        (
            "#02000Fひとまず、《幻獣》が現れる\x01",
            "原因が判明しただけでも\x01",
            "大きな進歩だといえるわ。\x02\x03",

            "あなたたちは、このまま\x01",
            "できる範囲での調査を\x01",
            "続けてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C3")

    Jump("loc_233E")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EA")

    #C0062
    ChrTalk(
        0xA,
        (
            "#02001F不可解な《幻獣》の発生……\x01",
            "クロスベル自治州にとって\x01",
            "決して無視できない問題だわ。\x02\x03",

            "#02003Fとはいえ、私たち警備隊は\x01",
            "国境の緊張状態に\x01",
            "集中する必要がある……\x02\x03",

            "#02000F幻獣の発生原因の調査、\x01",
            "どうかよろしくお願いするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00000Fええ、お任せください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_226B")

    label("loc_21EA")


    #C0064
    ChrTalk(
        0xA,
        (
            "#02003F私たち警備隊は\x01",
            "国境の緊張状態に\x01",
            "集中する必要がある……\x02\x03",

            "#02000F幻獣の発生原因の調査、\x01",
            "どうかよろしくお願いするわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_226B")

    Jump("loc_233E")

    label("loc_2270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_227E")
    Jump("loc_233E")

    label("loc_227E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_228C")
    Jump("loc_233E")

    label("loc_228C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_233E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A7")
    Call(0, 11)
    Jump("loc_233E")

    label("loc_22A7")


    #C0065
    ChrTalk(
        0xA,
        (
            "#02003F猟兵団である『赤い星座』は、\x01",
            "通商会議の警備においても\x01",
            "要注意だと言わざるを得ない。\x02\x03",

            "#02000F何か分かったら、\x01",
            "警備隊にも連絡してちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233E")

    TalkEnd(0xA)
    Return()

    # Function_8_156A end

    def Function_9_2342(): pass

    label("Function_9_2342")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2471")

    #C0066
    ChrTalk(
        0xB,
        (
            "国防軍を受け入れた司令、\x01",
            "レジスタンス活動を始めた\x01",
            "ミレイユ三尉たち……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xB,
        (
            "あの人たちは、考えに考えた末に\x01",
            "それぞれの道を選んだんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "だが、国防軍になれた事で\x01",
            "隊員のほとんどは浮かれちまって、\x01",
            "ただ流されるままになっていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        "……はあ、自分で自分が情けないな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_24E7")

    label("loc_2471")


    #C0070
    ChrTalk(
        0xB,
        (
            "ソーニャ司令もミレイユ三尉たちも、\x01",
            "考えに考えた末に\x01",
            "それぞれの道を選んだんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xB,
        "……俺たちも頑張らないとな。\x02",
    )

    CloseMessageWindow()

    label("loc_24E7")

    TalkEnd(0xFE)
    Return()

    # Function_9_2342 end

    def Function_10_24EB(): pass

    label("Function_10_24EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("chr/ch12202.itc", 0x1F)
    LoadChrToIndex("apl/ch51533.itc", 0x20)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -36600, 0, 0, 270)
    SetChrPos(0x106, -35830, 0, 870, 270)
    SetChrPos(0x103, -35240, 0, -680, 270)
    SetChrPos(0x104, -35430, 0, -1680, 270)
    SetChrPos(0x107, -34080, 0, 1450, 270)
    SetChrPos(0x105, -34350, 0, -80, 270)
    SetChrSubChip(0x107, 0x5)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -40000, 0, 2000, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -40150, 100, 0, 90)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "人目に付かぬように司令室まで案内され……\x02\x03",

            "今までの事情や経緯を含め、\x01",
            "《零の至宝》に関わる話まで\x01",
            "全てを司令たちに打ち明けた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7566", 0)
    OP_68(-40000, 1100, 1000, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    OP_68(-38000, 1100, 1000, 4000)
    OP_6F(0x79)
    OP_0D()

    #C0073
    ChrTalk(
        0xC,
        "#10206F#5Pそ、そんな事が……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "#10603F#5P……なるほどね。\x02\x03",

            "#10601F大統領側の不可解な行動も\x01",
            "ようやく見えて来たわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        "#00305F#12Pって事は、ひょっとして？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00002F#12P……こちらにある程度\x01",
            "協力していただけるとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#10603F#5P残念ながらそれは無理ね。\x02\x03",

            "警備隊にせよ、国防軍にせよ、\x01",
            "《文民統制#8Rシビリアンコントロール#》の原則は変わらない。\x02\x03",

            "#10608F問題があるとはいえ、\x01",
            "『クロスベル独立国』が成立して\x01",
            "大統領という国家元首がいる以上……\x02\x03",

            "#10601F私たち軍人は、勝手な判断で\x01",
            "武力を行使することは許されない。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#00006F#12P……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        "#10208F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00306F#12Pハア、正規軍ってのは\x01",
            "そのあたりが厳格ッスよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10401F#12Pそれじゃあやっぱり\x01",
            "歩み寄るのは無理そうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "#10603F#5Pええ、そうなるわね。\x02\x03",

            "#10608F──そうでなくても、\x01",
            "アリオス国防長官は優秀よ。\x02\x03",

            "仮にベルガード門の部隊が\x01",
            "そちらに協力したとしても……\x02\x03",

            "#10601F彼の率いる主力部隊に\x01",
            "“反乱軍”としてあっという間に\x01",
            "鎮圧されてしまうでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        "#00201F#12Pそうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#00301F#12Pあのオッサン、\x01",
            "指揮官としても優秀なのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "#10606F#5Pええ、セルゲイの元部下だけど\x01",
            "さすが『剣聖』と呼ばれるだけ\x01",
            "《理#2Rことわり#》に通じているみたいね。\x02\x03",

            "#10601Fその戦略の巧みさ……\x01",
            "兄弟子であるリベール王国軍司令、\x01",
            "カシウス准将に通じる物があるわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    #C0086
    ChrTalk(
        0xC,
        (
            "#10206F#11Pで、でも……！\x02\x03",

            "#10201Fたとえアリオス長官相手でも\x01",
            "タングラム門のダグラス副司令と\x01",
            "協力できれば……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    #C0087
    ChrTalk(
        0xA,
        (
            "#10605F#5Pあら、ノエル。\x02\x03",

            "#10604Fなぜ彼らに協力する事が\x01",
            "前提になっているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xC,
        "#10208F#11P……っ………\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        "#00202F#12Pノエルさん……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x105,
        (
            "#10409F#12Pはは、さっきの一騎打ちが\x01",
            "効いちゃってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0091
    ChrTalk(
        0x101,
        (
            "#00003F#12P──ソーニャ司令。\x02\x03",

            "#00008Fもし仮に、ディーター大統領と\x01",
            "クロスベル独立国の“正当性”が\x01",
            "揺らいだ場合……\x02\x03",

            "#00001F国防軍の対応はどうなりますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)

    #C0092
    ChrTalk(
        0xC,
        "#10205F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x106,
        "#10712F#12Pそれって……\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "#10604F#5Pふふ、そうね……\x02\x03",

            "どの程度かによるけど\x01",
            "事の真偽がはっきりするまで\x01",
            "“慎重に状況を見極める”……\x02\x03",

            "#10602Fその必要はあるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xC,
        "#10202F#5P……！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10404F#12Pフフ、なるほどね。\x02\x03",

            "#10402Fとなると、どうやってその\x01",
            "“正当性”を揺るがせるかが\x01",
            "鍵になってくるわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0097
    ChrTalk(
        0x101,
        (
            "#00004F#5Pああ……\x02\x03",

            "こういう事はエリィの判断が\x01",
            "一番頼りになりそうだけど……\x02\x03",

            "#00000Fたぶん鍵は、マクダエル議長じゃ\x01",
            "ないかと思う。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3022():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3022)
    Sleep(50)

    def lambda_3032():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3032)
    Sleep(50)

    def lambda_3042():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3042)
    Sleep(50)

    def lambda_3052():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3052)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    #C0098
    ChrTalk(
        0x103,
        "#00205F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        "#00300F#6Pお嬢のジーサマか……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x106,
        (
            "#10702F#12P確か、クロスベル自治州の\x01",
            "代表の一人になるんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ、もう一人は他ならぬ\x01",
            "ディーター市長だったけど。\x02\x03",

            "#00008F独立国の宣言にあたって\x01",
            "マクダエル議長の意見は\x01",
            "完全に封じられたと聞いている。\x02\x03",

            "#00013Fその彼の意見が、何らかの形で\x01",
            "国内外に発表されたら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#00203F#12P大統領や独立国の正当性が\x01",
            "わずかに揺らぐかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xC,
        "#10201F#5Pそうなったら国防軍も……！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "#10602F#5Pふふ……\x01",
            "いい所に気付いたわね。\x02\x03",

            "#10604Fどうやらヒントを\x01",
            "出すまでも無かったか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_329C():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_329C)
    Sleep(50)

    def lambda_32AC():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_32AC)
    Sleep(50)

    def lambda_32BC():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_32BC)
    Sleep(50)

    def lambda_32CC():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_32CC)
    Sleep(50)

    def lambda_32DC():
        OP_93(0x106, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_32DC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0105
    ChrTalk(
        0xA,
        (
            "#10603F#5P──ノエル少尉。\x02\x03",

            "#10601Fマクダエル元議長は、\x01",
            "ミシュラムだったかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    #C0106
    ChrTalk(
        0xC,
        (
            "#10211F#11Pえ……あ、はいっ！\x02\x03",

            "#10203Fお孫さんのエリィ嬢と共に\x01",
            "迎賓館内に軟禁されています！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0107
    ChrTalk(
        0xA,
        (
            "#10608F#5Pふむ、ミシュラムの警備は\x01",
            "確か《赤い星座》の部隊……\x02\x03",

            "#10601F国防軍の部隊は\x01",
            "常駐していなかったわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        "#10201F#11Pは、その通りであります。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0109
    ChrTalk(
        0x101,
        "#00002F#12Pソーニャ司令……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    #C0110
    ChrTalk(
        0xA,
        (
            "#10605F#5Pあら、私としたことが\x01",
            "うっかり部外者の前で……\x02\x03",

            "#10604F何でもないわ。\x01",
            "今のはすぐに忘れなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        "#00209F#12Pふふっ……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00309F#12Pハハ……\x01",
            "さすがソーニャ司令。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x105,
        (
            "#10402F#12P気持ちがいいほどの\x01",
            "しらばっくれぶりだねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(200)

    #C0114
    ChrTalk(
        0xA,
        (
            "#10603F#5P──それとノエル少尉。\x02\x03",

            "#10601F先ほどの一騎打ちだけど、\x01",
            "甘いと言われても仕方ないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        "#10206F#11P……はい。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "#10603F#5P罰として、しばらくの間、\x01",
            "無期限の謹慎処分とし──\x02\x03",

            "#10602F代わりに、クロスベル警察、\x01",
            "特務支援課への再出向を命じます。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0117
    ChrTalk(
        0xC,
        "#10202F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "#10604F#5P自分に何が足りなかったか……\x02\x03",

            "そして、クロスベルの将来のため\x01",
            "自分が何をすべきなのか。\x02\x03",

            "#10602Fしっかりと見極めて来なさい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetCameraDistance(25200, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0119
    ChrTalk(
        0xC,
        "#10212F#11P了解しました#12Rイ エ ス ・ マ ム#！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(25000, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 6)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_24EB end

    def Function_11_3859(): pass

    label("Function_11_3859")

    EventBegin(0x0)
    Fade(500)
    OP_68(-38900, 900, 260, 0)
    MoveCamera(314, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25180, 0)
    SetChrPos(0x101, -37250, 0, 0, 270)
    SetChrPos(0x102, -37250, 0, 980, 270)
    SetChrPos(0x109, -37250, 0, -1020, 270)
    SetChrPos(0x104, -36050, 0, -720, 270)
    SetChrPos(0x105, -35700, 0, 680, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    #C0120
    ChrTalk(
        0x109,
        "#12P#10100Fお疲れ様です、ソーニャ司令！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "#5P#02000Fお疲れ様、ノエル曹長。\x02\x03",

            "#02004F特務支援課への出向、\x01",
            "頑張っているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        "#12P#10104Fはい、本当に学ぶことが多くて……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x105,
        (
            "#12P#10300Fなるほど、警備隊司令の\x01",
            "ソーニャ・ベルツ殿か。\x02\x03",

            "#10302F警備隊を纏める有能な司令官……\x01",
            "フフ、なかなかの女傑みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#00004Fああ、俺たちも前々から\x01",
            "お世話になってる人なんだ。\x02\x03",

            "#00000F──お久しぶりです、司令。\x01",
            "それと……今更になりましたが\x01",
            "昇進、おめでとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "#5P#02002Fフフ、どういたしまして。\x01",
            "そういえば久しぶりだったわね。\x02\x03",

            "#02002F最近は通商会議の警備もあって\x01",
            "なかなか顔を合わせる機会が\x01",
            "なかったけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#00100Fやっぱりお忙しく\x01",
            "されているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "#5P#02000Fそうね、最近は連日、\x01",
            "部隊と一緒に警備範囲周辺を\x01",
            "チェックさせてもらっているわ。\x02\x03",

            "#02003F万が一のことがないように、\x01",
            "入念な準備をして\x01",
            "おかなければならないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#12P#00306Fまあ、明日は各国のＶＩＰ達が\x01",
            "来るっつー話だからなぁ。\x01",
            "当然といえば当然か。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00003Fすみません、司令。\x01",
            "なんだかお忙しいところに\x01",
            "お邪魔してしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "#5P#02003Fいえ、むしろ丁度よかったわ。\x02\x03",

            "#02001Fあなたたちに、どうしても\x01",
            "伝えておくべき事もあったから。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x109,
        "#12P#10105Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "#5P#02003F──先日、このベルガード門に\x01",
            "ある一団が訪れたわ。\x02\x03",

            "#02001F『赤い星座』……\x01",
            "ゼムリア大陸西部において\x01",
            "最強と言われる猟兵たちがね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x101,
        "#00011Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        "#00101Fこんな所にまで……！？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        (
            "#5P#02000F赤い星座は、ランディ……\x01",
            "あなたと密接に関わっている\x01",
            "という話だったわね。\x02\x03",

            "#02003Fだから、その目撃情報は\x01",
            "直接あなた達に伝えるべきだと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        "#12P#00301F……奴らは、ここで何を？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "#5P#02000F目撃した警備隊員の話では、\x01",
            "特別に目立ったことは\x01",
            "していなかったらしいわ。\x02\x03",

            "#02003F到着してからしばらく、\x01",
            "食堂でくつろいだあと……\x02\x03",

            "#02000F帝国から来た商人を出迎えて、\x01",
            "そのまま一緒に門を去ったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x105,
        (
            "#12P#10304Fふうん、帝国商人の出迎えねえ。\x02\x03",

            "#10302Fさしずめ、例の\x01",
            "『クリムゾン商会』とやらの\x01",
            "関係者か何かってトコかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        (
            "#00100Fああ、赤い星座の資金調達用の\x01",
            "ダミー会社っていう……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x109,
        (
            "#12P#10106F可能性は高そうですけど……\x01",
            "そ、それにしても、あまりに大胆です。\x02\x03",

            "#10101F治安維持組織である警備隊……\x01",
            "それも、帝国方面を守る精鋭たちの\x01",
            "真っ只中に来るなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#00003F……連中はこのクロスベルでは、\x01",
            "まだ何も事を起こしてはいないからな。\x02\x03",

            "#00001Fこの間の旧鉱山での一件も\x01",
            "証拠があるわけじゃないし、\x01",
            "コソコソすることもないだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        (
            "#12P#00303F……それくらい面の皮が厚くねえと、\x01",
            "堂々と高級クラブなんて経営しねえさ。\x02\x03",

            "#00300Fソーニャ司令、情報どうもッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#5P#02003F……礼には及ばないわ。\x02\x03",

            "#02001F猟兵団である『赤い星座』は、\x01",
            "通商会議の警備においても\x01",
            "要注意だと言わざるを得ない。\x02\x03",

            "何か分かったら、\x01",
            "警備隊にも連絡してちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00001F……分かりました。\x01",
            "こちらでも気をつけてみます。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 5)
    OP_29(0xA3, 0x1, 0x2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -37250, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_3859 end

    def Function_12_4418(): pass

    label("Function_12_4418")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4583")
    OP_68(-1550, 910, 41080, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44EA")
    SetChrPos(0x101, -1850, 10, 40450, 0)
    SetChrPos(0x104, -590, 10, 40320, 0)
    SetChrPos(0x102, -2060, 10, 39240, 0)
    SetChrPos(0x103, -720, 10, 39190, 0)
    SetChrPos(0x109, -2140, 10, 38080, 0)
    SetChrPos(0x105, -540, 10, 37980, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_4577")

    label("loc_44EA")

    OP_68(-1940, 910, 41470, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -1850, 10, 40450, 0)
    SetChrPos(0x104, -590, 10, 40320, 0)
    SetChrPos(0x102, -2060, 10, 39240, 0)
    SetChrPos(0x109, -720, 10, 39190, 0)
    SetChrPos(0x105, -1740, 10, 38080, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4577")

    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_4625")

    label("loc_4583")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4625")
    OP_68(-37130, 700, 3380, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -36980, 0, 2200, 0)
    SetChrPos(0x104, -35490, 0, 2200, 0)
    SetChrPos(0x102, -36980, 0, 1200, 0)
    SetChrPos(0x109, -35490, 0, 1200, 0)
    SetChrPos(0x105, -36250, 0, 600, 0)
    OP_93(0x8, 0xB4, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4625")

    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0145
    ChrTalk(
        0x8,
        (
            "#07902Fあら、支援課の皆さん。\x01",
            "お久しぶりね。\x02\x03",

            "#07909Fそれと、そこの馬鹿──\x02\x03",

            "#07903F……コホン。\x01",
            "ランディ、調子はどう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46FF")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_46FF")

    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0146
    ChrTalk(
        0x104,
        (
            "#6P#00304Fフフ、ミレイユ。\x01",
            "言うようになったみてえだが……\x01",
            "お前の気持ちは分かってるぜ。\x02\x03",

            "#00302F俺様が支援課に復帰しちまって、\x01",
            "さぞ寂しい思いをしてんだろ。\x02\x03",

            "#00309F『──行かないで、ランディ！\x01",
            "  これからも私と一緒にいて！（裏声）』\x01",
            "……な～んて言ってたもんな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0147
    ChrTalk(
        0x8,
        (
            "#07907Fい、いつ私がそんな事を言いました！？\x01",
            "……この、大馬鹿ランディ！\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x109,
        (
            "#6P#10100F（クスクス……\x01",
            "  相変わらず仲がいいですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00000Fはは……ミレイユ准尉、\x01",
            "お元気そうで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#00100Fそういえば、\x01",
            "昇進の話が出ているそうですね。\x01",
            "ふふ、おめでとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#07902Fコ、コホン、ええ……\x01",
            "正直、身に余る気持ちですけど。\x02\x03",

            "#07908F教団事件の時は、あろうことか\x01",
            "ＩＢＣの襲撃を先導するなんて\x01",
            "重大な過ちを犯しましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x105,
        (
            "#6P#10300Fま、あの時は妙な薬を盛られて\x01",
            "操られてたって話なんだし、\x01",
            "気にしなくてもいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#07903F……ええ、頭では\x01",
            "分かってるんですけど、\x01",
            "自分が許せないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#6P#00306Fやれやれ、相変わらず\x01",
            "固ぇヤツだなあ、お前は。\x02\x03",

            "#00300F今回のは、前のアホ司令の下でも\x01",
            "最善の指揮をとってきたことが、\x01",
            "正当に評価された結果だろ？\x02\x03",

            "#00302F謹んで受けるのが、\x01",
            "司令への礼儀ってもんだろうが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BF7")
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_4BF7")

    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C49")
    OP_64(0x103)

    label("loc_4C49")

    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CA0")

    #C0155
    ChrTalk(
        0x103,
        (
            "#6P#00205Fランディさんが\x01",
            "いきなりマトモな意見を……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE0")

    label("loc_4CA0")


    #C0156
    ChrTalk(
        0x101,
        (
            "#00006Fな、なんていうか……\x01",
            "急にマトモな意見を言うんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE0")


    #C0157
    ChrTalk(
        0x104,
        (
            "#6P#00309Fハハ、俺はいつだって\x01",
            "マトモだろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "#07902F……うん、そうよね。\x01",
            "謹んで受けることにする。\x02\x03",

            "#07906F#1S……ありがとう、ランディ。#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        "#6P#00305F……へ？　何か言ったか？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        "#07903Fな、なんでもないっ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF0")
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -1310, 10, 40450, 0)
    Jump("loc_4E16")

    label("loc_4DF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E16")
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x0, -36300, 0, 2009, 0)

    label("loc_4E16")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E3A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_4E3A")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_4418 end

    def Function_13_4E41(): pass

    label("Function_13_4E41")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch44900.itc", 0x1E)
    OP_68(-39050, 900, 70, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -37300, 0, 0, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0161
    ChrTalk(
        0xA,
        (
            "#5P#02001F──以上が、\x01",
            "警察の確かな筋からの情報よ。\x02\x03",

            "#02003Fおそらく、テロリストが\x01",
            "なんらかの方法で侵入を試みるのは\x01",
            "間違いないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xD,
        "#12Pふむ……厄介な連中ですな。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xD,
        (
            "#12P了解です。\x01",
            "タングラム門でも引き続き\x01",
            "警戒を強めていくとしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "#5P#02003Fええ、それと……\x01",
            "飛行艇を用いて侵入する可能性も\x01",
            "ゼロとはいえないわ。\x02\x03",

            "#02000Fついては、国境門付近に配備されている\x01",
            "レーダー施設を有効活用するように。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xD,
        "#12Pふむ、あの対空レーダーですな？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xD,
        (
            "#12P重ねて了解しました。\x01",
            "早速担当者に連絡を入れて……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    OP_68(-1850, 900, -4540, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -1050, 0, -4470, 270)
    SetChrPos(0x102, -650, 0, -3490, 270)
    SetChrPos(0x103, -550, 0, -5500, 270)
    SetChrPos(0x104, 950, 0, -4470, 270)
    SetChrPos(0x109, 650, 0, -5500, 270)
    SetChrPos(0x105, 1050, 0, -3200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00000Fどうやら、今日の警備体制を\x01",
            "話し合っているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        (
            "#00100Fええ、どうやらテロ対策が\x01",
            "主軸におかれてるようだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#12P#00303Fにしても、レーダー施設か……\x01",
            "門の近くにそんなもんがあったんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        (
            "#12P#10100F確か両国境門の付近に\x01",
            "配備されているはずです。\x02\x03",

            "#10103F私は扱ったことはないですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#6P#00203F以前、財団がそういったものを\x01",
            "クロスベルに設置したと\x01",
            "聞いたことがあります。\x02\x03",

            "#00200F自治州領空に入る飛行船を\x01",
            "かなり広範囲で補足できる\x01",
            "高性能なものだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#00005Fへえ……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x105,
        (
            "#12P#10300Fまあ、そんなものがあるなら\x01",
            "ある程度安心できるかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 6)
    OP_D7(0x1E)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1050, 0, -4470, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_13_4E41 end

    def Function_14_53F6(): pass

    label("Function_14_53F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5408")
    Call(0, 13)
    Jump("loc_547D")

    label("loc_5408")

    TalkBegin(0xFF)

    #C0174
    ChrTalk(
        0x101,
        (
            "#00000Fソーニャ司令とダグラス副司令が\x01",
            "テロ対策について話しているみたいだ。\x01",
            "……中に入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_547D")

    Return()

    # Function_14_53F6 end

    SaveToFile()

Try(main)
