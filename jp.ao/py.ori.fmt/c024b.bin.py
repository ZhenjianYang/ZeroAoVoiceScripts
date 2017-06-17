from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c024b.bin",                # FileName
        "c024b",                    # MapName
        "c024b",                    # Location
        0x000F,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c024b",                  # 0
        "サミィ",                 # 1
        "キンドール",             # 2
        "ブリジッタ",             # 3
        "ルーヴィック老人",       # 4
        "オリガ夫人",             # 5
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch21802.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "chr/ch21602.itc",                   # 05
        "chr/ch20100.itc",                   # 06
        "chr/ch20102.itc",                   # 07
        "chr/ch05102.itc",                   # 08
        "chr/ch10000.itc",                   # 09
    ))

    DeclNpc(9060,    10000,   18000,   45,   261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-2009,   1149,    60479,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(8470,    1019,    62380,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-45650,  1019,    60169,   180,  261,  0x0, 0,   4,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(7030,    150,     6969,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)

    DeclActor(-340,    10000,   20320,   1200,    -340,    11500,   20320,   0x007C, 0,  11, 0x0000)

    ChipFrameInfo(412, 0)                                        # 0

    ScpFunction((
        "Function_0_19C",          # 00, 0
        "Function_1_24C",          # 01, 1
        "Function_2_277",          # 02, 2
        "Function_3_2A2",          # 03, 3
        "Function_4_302",          # 04, 4
        "Function_5_309",          # 05, 5
        "Function_6_40E",          # 06, 6
        "Function_7_575",          # 07, 7
        "Function_8_605",          # 08, 8
        "Function_9_694",          # 09, 9
        "Function_10_7B2",         # 0A, 10
        "Function_11_7FC",         # 0B, 11
    ))


    def Function_0_19C(): pass

    label("Function_0_19C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1D4"),
        (1, "loc_1E0"),
        (2, "loc_1EC"),
        (3, "loc_1F8"),
        (4, "loc_204"),
        (5, "loc_210"),
        (6, "loc_21C"),
        (SWITCH_DEFAULT, "loc_228"),
    )


    label("loc_1D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_204")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_210")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_21C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_228")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_24B")

    Return()

    # Function_0_19C end

    def Function_1_24C(): pass

    label("Function_1_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_276")
    OP_94(0xFE, 0xFFFFF858, 0x2A44, 0x866, 0x311A, 0x3E8)
    Sleep(300)
    Jump("Function_1_24C")

    label("loc_276")

    Return()

    # Function_1_24C end

    def Function_2_277(): pass

    label("Function_2_277")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A1")
    OP_94(0xFE, 0xFFFF4C46, 0xE4C0, 0xFFFF592A, 0xF078, 0x3E8)
    Sleep(300)
    Jump("Function_2_277")

    label("loc_2A1")

    Return()

    # Function_2_277 end

    def Function_3_2A2(): pass

    label("Function_3_2A2")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xB, 0x5)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, -48700, 1200, 60400, 270)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -51460, 1200, 60400, 90)
    Return()

    # Function_3_2A2 end

    def Function_4_302(): pass

    label("Function_4_302")

    ClearMapObjFlags(0x2, 0x10)
    Return()

    # Function_4_302 end

    def Function_5_309(): pass

    label("Function_5_309")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B3")

    #C0001
    ChrTalk(
        0xFE,
        (
            "今日は各国の首脳が\x01",
            "アルカンシェルを観劇している\x01",
            "らしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "うーん、さぞ、いい席で\x01",
            "楽しんでるんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "くう～、うらやましいわ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_40A")

    label("loc_3B3")


    #C0004
    ChrTalk(
        0xFE,
        (
            "結局、今度のリニューアル公演の\x01",
            "チケットは買い逃しちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "はーあ……\x02",
    )

    CloseMessageWindow()

    label("loc_40A")

    TalkEnd(0xFE)
    Return()

    # Function_5_309 end

    def Function_6_40E(): pass

    label("Function_6_40E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB")

    #C0006
    ChrTalk(
        0xFE,
        (
            "オルキスタワーは、夜になると\x01",
            "美しくライトアップされるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "青と白を基調としたタワーが\x01",
            "夜の闇に爛々#4Rらんらん#と輝く美しさに、\x01",
            "息を呑むこと請け合いだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "フフ、機会があれば是非とも\x01",
            "見てほしいものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_571")

    label("loc_4FB")


    #C0009
    ChrTalk(
        0xFE,
        (
            "オルキスタワーは、夜になると\x01",
            "美しくライトアップされるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "フフ、機会があれば是非とも\x01",
            "見てほしいものだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_571")

    TalkEnd(0xFE)
    Return()

    # Function_6_40E end

    def Function_7_575(): pass

    label("Function_7_575")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        (
            "主人ったら聞いてもないのに\x01",
            "オルキスタワーのことを\x01",
            "色々と教えてくれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "ふふ、昼間の除幕式の\x01",
            "興奮が冷めきらないみたいね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_575 end

    def Function_8_605(): pass

    label("Function_8_605")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A")
    Call(0, 9)
    Jump("loc_690")

    label("loc_61A")


    #C0013
    ChrTalk(
        0xFE,
        (
            "せっかく一緒に飲もうと思って\x01",
            "いいワインを買ってきたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "ふん、もういいわい。\x01",
            "一人で飲んでしまうからの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_690")

    TalkEnd(0xFE)
    Return()

    # Function_8_605 end

    def Function_9_694(): pass

    label("Function_9_694")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0015
    ChrTalk(
        0xB,
        (
            "あーあ、やっぱり\x01",
            "このワインは美味いのーう。\x01",
            "買ってよかったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "婆さんは要らんようじゃし、\x01",
            "わしが一人で飲むかのーう。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        "……ええ、お好きにどうぞ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xC,
        (
            "そのために高いミラを支払って\x01",
            "買ったんでしょうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "……ふん！\x01",
            "ぐびぐびぐびぐび。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_9_694 end

    def Function_10_7B2(): pass

    label("Function_10_7B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C7")
    Call(0, 9)
    Jump("loc_7F8")

    label("loc_7C7")


    #C0020
    ChrTalk(
        0xFE,
        (
            "……ふん、主人のことなんて\x01",
            "知るもんですか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F8")

    TalkEnd(0xFE)
    Return()

    # Function_10_7B2 end

    def Function_11_7FC(): pass

    label("Function_11_7FC")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_11_7FC end

    SaveToFile()

Try(main)
