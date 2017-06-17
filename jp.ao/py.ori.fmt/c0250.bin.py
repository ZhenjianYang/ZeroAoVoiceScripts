from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0250.bin",                # FileName
        "c0250",                    # MapName
        "c0250",                    # Location
        0x000E,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 14, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0250",                  # 0
        "レイテ",                 # 1
        "パンセ",                 # 2
        "フェイ",                 # 3
        "コウケン",               # 4
        "リュウ",                 # 5
        "チルル",                 # 6
    ))

    AddCharChip((
        "chr/ch10300.itc",                   # 00
        "chr/ch22300.itc",                   # 01
        "chr/ch22302.itc",                   # 02
        "chr/ch32700.itc",                   # 03
        "chr/ch32702.itc",                   # 04
        "apl/ch50148.itc",                   # 05
        "chr/ch21000.itc",                   # 06
        "chr/ch21002.itc",                   # 07
        "chr/ch20600.itc",                   # 08
        "chr/ch20500.itc",                   # 09
    ))

    DeclNpc(51830,   0,       115930,  0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-54310,  0,       52840,   90,   261,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(-53380,  0,       52599,   270,  261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-51919,  0,       108370,  90,   261,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-58000,  0,       107489,  0,    389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-57729,  0,       106739,  180,  389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)

    ChipFrameInfo(412, 0)                                        # 0

    ScpFunction((
        "Function_0_19C",          # 00, 0
        "Function_1_24C",          # 01, 1
        "Function_2_277",          # 02, 2
        "Function_3_5E2",          # 03, 3
        "Function_4_64A",          # 04, 4
        "Function_5_1ED7",         # 05, 5
        "Function_6_22B8",         # 06, 6
        "Function_7_2DDC",         # 07, 7
        "Function_8_2F66",         # 08, 8
        "Function_9_37D2",         # 09, 9
        "Function_10_459A",        # 0A, 10
        "Function_11_46BE",        # 0B, 11
        "Function_12_47EA",        # 0C, 12
        "Function_13_4930",        # 0D, 13
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
    OP_94(0xFE, 0xFFFF28BA, 0xC9A4, 0xFFFF30C6, 0xD2C8, 0x3E8)
    Sleep(300)
    Jump("Function_1_24C")

    label("loc_276")

    Return()

    # Function_1_24C end

    def Function_2_277(): pass

    label("Function_2_277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_296")
    SetChrPos(0xA, -58130, 0, 58620, 0)
    Jump("loc_5E1")

    label("loc_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2E0")
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -54030, 0, 104830, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -53850, 0, 106300, 180)
    SetChrFlags(0xD, 0x10)
    Jump("loc_5E1")

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32B")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -51060, 400, 56380, 180)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -56700, 0, 110990, 225)
    Jump("loc_5E1")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_33E")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5E1")

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_369")
    SetChrPos(0x9, -58130, 0, 58620, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_5E1")

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39E")
    SetChrPos(0xA, -51250, 500, 57180, 315)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x40)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    Jump("loc_5E1")

    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3B1")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5E1")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3CF")
    SetChrFlags(0x8, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_5E1")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_426")
    SetChrPos(0xA, -51250, 500, 57180, 315)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x40)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x7)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, -51780, 150, 112520, 90)
    Jump("loc_5E1")

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_45B")
    SetChrPos(0x9, -57750, 400, 52200, 180)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x80)
    Jump("loc_5E1")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_494")
    SetChrPos(0x9, -58130, 0, 58620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484")
    SetChrFlags(0x9, 0x10)

    label("loc_484")

    SetChrFlags(0xA, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_5E1")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E5")
    SetChrPos(0x9, -58130, 0, 58620, 0)
    SetChrFlags(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 0x7)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, -51780, 150, 112520, 90)
    Jump("loc_5E1")

    label("loc_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4F8")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5E1")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_567")
    SetChrPos(0x8, 57650, 0, 108310, 270)
    SetChrFlags(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xC, -54030, 0, 104830, 0)
    SetChrPos(0xD, -53850, 0, 106300, 180)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_558")
    SetChrFlags(0xC, 0x10)

    label("loc_558")

    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_5E1")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5E1")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, -51250, 500, 57180, 315)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x40)
    EndChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xB, -53760, 0, 107910, 180)
    SetChrPos(0xD, -53850, 0, 106300, 0)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2")
    SetChrFlags(0xB, 0x10)

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1")
    SetChrFlags(0xD, 0x10)

    label("loc_5E1")

    Return()

    # Function_2_277 end

    def Function_3_5E2(): pass

    label("Function_3_5E2")

    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_620")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_649")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)

    label("loc_649")

    Return()

    # Function_3_5E2 end

    def Function_4_64A(): pass

    label("Function_4_64A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_757")

    #C0001
    ChrTalk(
        0xFE,
        (
            "さっきセシルと連絡してね。\x01",
            "ひとまず安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "ただ、何だか物思いに\x01",
            "耽ってるみたいなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "病院が急に忙しくなったからじゃ\x01",
            "ないとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "もし時間があったら、\x01",
            "病院に立ち寄ってあげてね。\x01",
            "色々話したいだろうから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7DA")

    label("loc_757")


    #C0005
    ChrTalk(
        0xFE,
        (
            "セシル、何だか物思いに\x01",
            "耽ってるみたいなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "もし時間があったら、\x01",
            "病院に立ち寄ってあげてね。\x01",
            "色々話したいだろうから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DA")

    Jump("loc_1ED3")

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABB")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0007
    ChrTalk(
        0xFE,
        (
            "まあ、ロイド君じゃない……！\x01",
            "今までどこに行っていたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "そうだ、セシルには会った？\x01",
            "私、あの子ともなかなか会えてなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00012Fお、おばさん、落ち着いて。\x01",
            "……久しぶりに会えてうれしいよ。\x02\x03",

            "#00000Fセシル姉なら、今は病院だ。\x01",
            "元気そうにしてるみたいだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "そう、よかった……\x01",
            "ロイド君も帰ってきてくれたし、\x01",
            "おばさん、本当に安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "外は危ないわ、おばさんちに\x01",
            "隠れていなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00004Fいや、ありがたいけど……\x01",
            "どうしても行かなきゃ\x01",
            "ならないところがあるんだ。\x02\x03",

            "#00000Fおばさんは、\x01",
            "ここで待っていてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "そう……分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "でも、気をつけて行くのよ？\x01",
            "あなたたちに何かあったら、\x01",
            "私、もう……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00000Fああ、もちろんだよ。\x01",
            "……また後でね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 7)
    Jump("loc_B40")

    label("loc_ABB")


    #C0016
    ChrTalk(
        0xFE,
        (
            "よかった……\x01",
            "ロイド君も帰ってきてくれたし、\x01",
            "おばさん、本当に安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "空の女神よ、どうか彼らに\x01",
            "ご加護があらんことを……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B40")

    Jump("loc_1ED3")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B53")
    Jump("loc_1ED3")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9A")

    #C0018
    ChrTalk(
        0xFE,
        (
            "昨日、病院の方に\x01",
            "連絡をいれてみたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "セシルたちは\x01",
            "随分と忙しくしているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00003F……そうだろうね。\x02\x03",

            "#00008Fあの襲撃事件のせいで、\x01",
            "病院にも沢山の患者が\x01",
            "入院したみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "はあ、心配だわ。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "セシルはちょっと、\x01",
            "がんばりすぎる性分だから……\x01",
            "体を壊さないといいけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CFE")

    label("loc_C9A")


    #C0023
    ChrTalk(
        0xFE,
        (
            "あの襲撃事件の影響で、\x01",
            "病院も随分と忙しいみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "セシル、ちゃんと\x01",
            "休めているのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFE")

    Jump("loc_1ED3")

    label("loc_D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DA8")

    #C0025
    ChrTalk(
        0xFE,
        (
            "占領事件だなんて、\x01",
            "マインツにいる人たちは\x01",
            "恐ろしい思いをしているでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "警備隊も苦戦しているって聞くし、\x01",
            "どうなってしまうのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1174")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EA")

    #C0027
    ChrTalk(
        0xFE,
        (
            "ああ、そういえば明日は\x01",
            "アルカンシェルの\x01",
            "リニューアル公演だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "チケットもあっという間に\x01",
            "完売したそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "ふふ、イリアちゃんもいつの間にか\x01",
            "すごい人になっちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        "#10105Fイ、イリア“ちゃん”……？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00005Fそういえば……\x01",
            "セシル姉とイリアさんは\x01",
            "幼なじみだったっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ええ、当時から目立つ子でね。\x01",
            "セシルとは不思議と気が合って、\x01",
            "よく２人で遊んでいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "セシルに意地悪をしてた男の子に\x01",
            "思いっきり殴りかかって、\x01",
            "泣かせちゃったこともあったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、イリアさんらしい\x01",
            "エピソードですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00306Fつーか、相手のガキんちょが\x01",
            "何となく可哀想なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、子供の意地悪って\x01",
            "好意の裏返しだったりするからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#00203Fまあ、イリアさんに殴られたなんて、\x01",
            "ある意味貴重な思い出が\x01",
            "出来たんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00012Fそ、それはどうだろう……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 3)

    label("loc_10EA")


    #C0039
    ChrTalk(
        0xFE,
        (
            "ふふ、そんなイリアちゃんも\x01",
            "今やアルカンシェルを引っ張る\x01",
            "スーパー・スター……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "子供の頃から知ってる\x01",
            "おばさんも、鼻が高いわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_1174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11F6")

    #C0041
    ChrTalk(
        0xFE,
        (
            "あら、今のって……\x01",
            "救急車の音じゃないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "何台も通っていったみたいだけど……\x01",
            "交通事故でもあったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1204")
    Jump("loc_1ED3")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_139E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1314")

    #C0043
    ChrTalk(
        0xFE,
        (
            "クロスベル市の国家独立……\x01",
            "その是非を問うための、\x01",
            "住民投票が行われるらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "これって、かなり難しい問題よね。\x01",
            "お父さんともよく相談して、\x01",
            "どっちに投票するか決めないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "どちらが正しいかなんて、\x01",
            "簡単に出せる答えじゃないものね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1399")

    label("loc_1314")


    #C0046
    ChrTalk(
        0xFE,
        (
            "投票については、\x01",
            "お父さんともよく相談して\x01",
            "決めようと思ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "どちらが正しいかなんて、\x01",
            "簡単に出せる答えじゃないものね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1399")

    Jump("loc_1ED3")

    label("loc_139E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1605")

    #C0048
    ChrTalk(
        0xFE,
        (
            "あら、そちらは……\x01",
            "確かティオちゃんだったわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        "#00202Fどうも、ご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "ふふ、お元気そうでなによりだわ。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "また時間が空いたら\x01",
            "みんなでお食事でもしましょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        (
            "#00109Fおばさまの料理……\x01",
            "ふふ、楽しみです。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00309Fああ、まさにお袋の味って感じで\x01",
            "本当に美味いんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x105,
        "#10305Fへえ、そうなんだ？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x109,
        (
            "#10109Fそれはいいですねぇ……\x01",
            "楽しみにしておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "もちろん新メンバーの\x01",
            "あなたたちもご招待するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "ふふ、その時は\x01",
            "腕によりをかけて\x01",
            "作らせてもらうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、おばさん。\x01",
            "また時間が空いたら\x01",
            "お邪魔させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 1)
    Jump("loc_167D")

    label("loc_1605")


    #C0059
    ChrTalk(
        0xFE,
        (
            "これで支援課のメンバーが\x01",
            "全員揃ったことになるのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "ふふ、また時間が空いたら\x01",
            "みんなでお食事でもしましょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167D")

    Jump("loc_1ED3")

    label("loc_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1700")

    #C0061
    ChrTalk(
        0xFE,
        (
            "あら、いつの間にか\x01",
            "空がすっかり暗くなったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "お父さんも帰ってくるし、\x01",
            "急いで食事の支度をしないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_1700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1902")

    #C0063
    ChrTalk(
        0x101,
        (
            "#00000Fおばさん、昨日セシル姉に\x01",
            "挨拶してきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "あら、そうだったの。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "ふふ、それはセシルも\x01",
            "喜んでたんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00012Fはは、まあ……\x01",
            "元気そうにしてたみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、想像してた以上に\x01",
            "素敵な女性で驚いたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        (
            "#10100Fそうですね、とても\x01",
            "包容力があって……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#00309Fだろだろ～？　何しろ、\x01",
            "俺のど真ん中ストライクな\x01",
            "お姉さんだからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00106Fあ、あなたねえ……\x01",
            "セシルさんのお母様を前にして\x01",
            "その表現はどうなのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00006Fほ、ほんとだよまったく……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 0)

    label("loc_1902")


    #C0072
    ChrTalk(
        0xFE,
        (
            "ふふ、セシルったら\x01",
            "なかなか人気者みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "よかったら、これからも\x01",
            "仲良くしてあげてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED3")

    label("loc_1971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9C")

    #C0074
    ChrTalk(
        0xFE,
        (
            "今日お買い物に出たら、\x01",
            "巡回している警察の人を\x01",
            "何人も見かけたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "やっぱり警察も、\x01",
            "忙しくしてるみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00000F明日から通商会議だからね。\x01",
            "俺たちも支援要請をこなしながら\x01",
            "見回っているところだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "あらあら……\x01",
            "大変だと思うけど、\x01",
            "がんばってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AE0")

    label("loc_1A9C")


    #C0078
    ChrTalk(
        0xFE,
        (
            "あなたたち警察は\x01",
            "大変だとおもうけど、\x01",
            "がんばってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE0")

    Jump("loc_1ED3")

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B00")
    Call(0, 5)
    Jump("loc_1C87")

    label("loc_1B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF5")

    #C0079
    ChrTalk(
        0xFE,
        (
            "うちのお父さんは、\x01",
            "図書館で司書として\x01",
            "働いているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "以前からある記者さんと\x01",
            "親交があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "とても博識な方らしくて、\x01",
            "その人が来ているときは\x01",
            "つい話し込んじゃうんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "ふふ、まるで子供みたいね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C87")

    label("loc_1BF5")


    #C0083
    ChrTalk(
        0xFE,
        (
            "うちのお父さん、\x01",
            "以前からある記者さんと\x01",
            "親交があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "とても博識な方らしくて、\x01",
            "その人が来ているときは\x01",
            "つい話し込んじゃうんですって。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C87")

    Jump("loc_1ED3")

    label("loc_1C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA7")
    Call(0, 5)
    Jump("loc_1ED3")

    label("loc_1CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5F")

    #C0085
    ChrTalk(
        0xFE,
        (
            "そういえばロイド君、\x01",
            "セシルにはもう連絡したのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00000Fああ、一応導力通信でね。\x01",
            "また今度、別の機会に\x01",
            "改めて行かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "ふふ、帰ってきてから\x01",
            "更に逞#2Rたくま#しくなったみたいだし、\x01",
            "セシルもびっくりするかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00012Fえ、えっと、そうかな。\x01",
            "ハハハ……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#00111F（なんだか照れてるわね。\x01",
            "  ……何を想像したのかしら。）\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x105,
        (
            "#10309F（フフ、セシルさんとやらに\x01",
            "  ますます興味がわいてきたよ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ED3")

    label("loc_1E5F")


    #C0091
    ChrTalk(
        0xFE,
        (
            "ロイド君、帰ってきてから\x01",
            "更に逞しくなったみたいだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "ふふ、セシルが見たら\x01",
            "びっくりするかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED3")

    TalkEnd(0xFE)
    Return()

    # Function_4_64A end

    def Function_5_1ED7(): pass

    label("Function_5_1ED7")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0xFE,
        (
            "あら、あらあら……\x01",
            "ロイド君じゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#00000Fレイテおばさん、ただいま。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "うふふ、\x01",
            "元気そうでなによりだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "支援課の方も一緒みたいだし、\x01",
            "一課の研修っていうのが\x01",
            "ようやく終わったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00000Fああ、つい先日ね。\x01",
            "ちょっと顔を出すのが\x01",
            "遅れちゃったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        "#10305Fこちらのマダムはどなただい？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00000Fああ、子供の頃から何かと\x01",
            "面倒を見てくれてる人なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#00100F私たちもお世話になってる、\x01",
            "セシルさんのお母様なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        (
            "#10100Fセシルさんっていうと、\x01",
            "以前病院でお会いした……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そういえばノエルは\x01",
            "面識があったんだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10303Fふむ、僕だけ\x01",
            "仲間はずれってわけかい？\x02\x03",

            "#10302Fなんだかロイドと\x01",
            "ただならぬ間柄みたいだし……\x01",
            "是非とも話を聞きたいところだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#00012Fた、ただならぬ間柄とか、\x01",
            "そういうんじゃないから。\x02\x03",

            "#00000Fまあセシル姉には\x01",
            "後々会う機会もあるだろうし、\x01",
            "そのときにでも紹介するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "ふふ、支援課って\x01",
            "相変わらず楽しそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "ロイド君、また何か\x01",
            "困った事があったら\x01",
            "いつでもいらっしゃいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 5)
    Return()

    # Function_5_1ED7 end

    def Function_6_22B8(): pass

    label("Function_6_22B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238D")

    #C0107
    ChrTalk(
        0xFE,
        (
            "おとーさんったら、鉄道が止まってから\x01",
            "しばらくは元気なかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "すぐに思い直して色んなところに\x01",
            "首を突っ込んでるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "まったく、メカオタクって\x01",
            "懲りないんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23F5")

    label("loc_238D")


    #C0110
    ChrTalk(
        0xFE,
        (
            "まったく、メカオタクって\x01",
            "懲りないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "……まあそれがおとーさんの\x01",
            "いい所でもあるけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F5")

    Jump("loc_2DD8")

    label("loc_23FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2469")

    #C0112
    ChrTalk(
        0xFE,
        "な、何が起こってるのかしら……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "マリアベルさんや大統領が\x01",
            "どうにかしてくれるわよね……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24EB")

    #C0114
    ChrTalk(
        0xFE,
        (
            "おとーさん、今日は朝から\x01",
            "駅に行っててすっごく忙しそうなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "……せめて家にいる間は\x01",
            "ゆっくりしてほしいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_24EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2582")

    #C0116
    ChrTalk(
        0xFE,
        (
            "この間の事件で、\x01",
            "アルカンシェルのイリアさんが\x01",
            "大怪我しちゃったって……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "もう、あのすごい劇は見れないのかな。\x01",
            "そんなのヤダな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262B")

    #C0118
    ChrTalk(
        0xFE,
        (
            "今日って、アルカンシェルの\x01",
            "リニューアル公演がある日よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "なのに、なんだかおとーさん\x01",
            "心配そうにしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "何かあったのかな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2689")

    label("loc_262B")


    #C0121
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの\x01",
            "リニューアル公演がある\x01",
            "おめでたい日なのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        "何かあったのかな……\x02",
    )

    CloseMessageWindow()

    label("loc_2689")

    Jump("loc_2DD8")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2709")

    #C0123
    ChrTalk(
        0xFE,
        (
            "おとーさん、昨日は\x01",
            "脱線事故のことで\x01",
            "随分忙しくしてたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "……今日は静かにしてて\x01",
            "あげよっかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_279E")

    #C0125
    ChrTalk(
        0xFE,
        (
            "おとーさん、\x01",
            "列車が事故を起こしたって聞いて\x01",
            "大慌てで飛び出していったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "駅に行ってくるって聞いたけど、\x01",
            "大丈夫なのかなあ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_279E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2839")

    #C0127
    ChrTalk(
        0xFE,
        (
            "おとーさんったら、\x01",
            "今日はお姉ちゃんの様子を\x01",
            "見にいきたいなんていうの。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "せっかくのお休みなんだから\x01",
            "お家でゆっくりすればいいのにね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28C6")

    #C0129
    ChrTalk(
        0xFE,
        (
            "おとーさんったら、\x01",
            "出張から帰るなり\x01",
            "ベッドに突入しちゃうの。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "もー、服ぐらい着替えないと\x01",
            "シーツが汚れちゃうじゃない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_28C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2946")

    #C0131
    ChrTalk(
        0xFE,
        (
            "マリアベルさんの写真が載った\x01",
            "ファッション誌を読んでるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "あ～ん、あこがれちゃうなあ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29C9")

    label("loc_2946")


    #C0133
    ChrTalk(
        0xFE,
        (
            "はあ、何でマリアベルさんって\x01",
            "あんなにキレイで頭もいいのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "彼女みたいなひとを\x01",
            "才色兼備って言うのよね。\x01",
            "いいなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C9")

    Jump("loc_2DD8")

    label("loc_29CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2AE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7A")

    #C0135
    ChrTalk(
        0xFE,
        (
            "……あっ！\x01",
            "あたしのファッション誌の棚に\x01",
            "鉄道の本が混ざってる……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "絶対おとーさんの仕業ね。\x01",
            "何度おんなじ手を\x01",
            "使うつもりなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_2AE1")

    label("loc_2A7A")


    #C0137
    ChrTalk(
        0xFE,
        (
            "おとーさん、時々こうやって\x01",
            "あたしを鉄道好きにしようとするの。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "まったく、コシャクなんだから。\x02",
    )

    CloseMessageWindow()

    label("loc_2AE1")

    Jump("loc_2DD8")

    label("loc_2AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C12")
    TurnDirection(0xFE, 0x0, 0)

    #C0139
    ChrTalk(
        0xFE,
        (
            "みんなコドモよねー。\x01",
            "あんなおっきな建物くらいで\x01",
            "キャーキャー騒いじゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "……ま、まあ、\x01",
            "確かに少しはすごかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "建物なんかより、\x01",
            "ファッション誌を見たほうが\x01",
            "楽しいしタメになるもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#00006F（比べるもんじゃ\x01",
            "  ないと思うけどな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_2C94")

    label("loc_2C12")


    #C0143
    ChrTalk(
        0xFE,
        (
            "（ぺらぺら……）\x01",
            "わあ、この写真のお姉さん、\x01",
            "とってもステキね。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "やっぱりこう、\x01",
            "くびれがあったほうが\x01",
            "かっこいいのかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C94")

    Jump("loc_2DD8")

    label("loc_2C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D1E")

    #C0145
    ChrTalk(
        0xFE,
        (
            "おとーさん、\x01",
            "また出張で１ヶ月くらい\x01",
            "家を空けるんだってー。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "やっぱり鉄道技師だから、\x01",
            "色々いそがしーみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD8")

    label("loc_2D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D39")
    Call(0, 7)
    Jump("loc_2DCA")

    label("loc_2D39")


    #C0147
    ChrTalk(
        0xFE,
        (
            "私はただ、マリアベルさんみたいな\x01",
            "かっこよくて頭のいいヒトに\x01",
            "なりたいだけだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "おとーさんの思惑通りに\x01",
            "技師になんかならないんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCA")

    Jump("loc_2DD8")

    label("loc_2DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2DD8")

    label("loc_2DD8")

    TalkEnd(0xFE)
    Return()

    # Function_6_22B8 end

    def Function_7_2DDC(): pass

    label("Function_7_2DDC")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0149
    ChrTalk(
        0x9,
        (
            "マリアベルさんって、\x01",
            "ＩＢＣの技術部を率いてて\x01",
            "導力技術にも詳しいらしいのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "うーん……\x01",
            "あたしも導力技術の事、\x01",
            "勉強したほうがいいのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0151
    ChrTalk(
        0xA,
        (
            "パ、パンセ～！\x01",
            "ようやくお前も技師の道に\x01",
            "興味を持ってくれたんだなあ！\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "よし、この際だ。\x01",
            "お父さんと同じ鉄道技師を\x01",
            "目指してみないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "……それはイヤ。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        "#4Sがーん！#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_2DDC end

    def Function_8_2F66(): pass

    label("Function_8_2F66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306D")

    #C0155
    ChrTalk(
        0xFE,
        (
            "僕の鉄道技師としての技術は、\x01",
            "大陸横断鉄道が止まっている今、\x01",
            "役に立たないかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "同じ導力器の乗り物である\x01",
            "バスや導力車の整備では\x01",
            "何か力になれるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "よし、市民会館にかけあって\x01",
            "何か仕事を探してくるかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30F8")

    label("loc_306D")


    #C0158
    ChrTalk(
        0xFE,
        (
            "僕の鉄道技師としての技術は、\x01",
            "バスや導力車の整備でも\x01",
            "何か力になれるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "よし、市民会館にかけあって\x01",
            "何か仕事を探してくるかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F8")

    Jump("loc_37CE")

    label("loc_30FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3176")

    #C0160
    ChrTalk(
        0xFE,
        (
            "パンセ、外に出ちゃダメだぞ。\x01",
            "お父さんと家でじっとしてような。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "お姉ちゃんもきっと無事なはずだ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37CE")

    label("loc_3176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324D")

    #C0162
    ChrTalk(
        0xFE,
        (
            "今朝からクロスベル駅に\x01",
            "手伝いに行ってたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "故郷に帰ろうとする\x01",
            "外国人たちが大勢詰め掛けて、\x01",
            "かなりの混乱状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "僕も早めに休憩を切り上げて\x01",
            "手伝いに戻らないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32BD")

    label("loc_324D")


    #C0165
    ChrTalk(
        0xFE,
        (
            "駅に外国人たちが詰め掛けて\x01",
            "かなりの混乱状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "僕も早めに休憩を切り上げて\x01",
            "手伝いに戻らないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BD")

    Jump("loc_37CE")

    label("loc_32C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32D0")
    Jump("loc_37CE")

    label("loc_32D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3338")

    #C0167
    ChrTalk(
        0xFE,
        (
            "なんてことだ、\x01",
            "まさかマインツが……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "武装集団とやらは、\x01",
            "一体何が目的なんだ……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CE")

    label("loc_3338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_335A")

    #C0169
    ChrTalk(
        0xFE,
        "ぐう、ぐう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37CE")

    label("loc_335A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3368")
    Jump("loc_37CE")

    label("loc_3368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3456")
    OP_4B(0x9, 0xFF)

    #C0170
    ChrTalk(
        0xFE,
        (
            "せっかくだから、ウェンディの\x01",
            "働いている姿が見たいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "パンセもお姉ちゃんの姿を見て、\x01",
            "技師の勉強をするといいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "もー、だからあたしは\x01",
            "技師にはならないって\x01",
            "言ってるでしょ！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_34CE")

    label("loc_3456")


    #C0173
    ChrTalk(
        0xFE,
        (
            "パンセもお姉ちゃんの姿を見て、\x01",
            "技師の勉強をするといいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "将来、技師になるために\x01",
            "きっと役立つだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34CE")

    Jump("loc_37CE")

    label("loc_34D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_354E")

    #C0175
    ChrTalk(
        0xFE,
        (
            "むにゃむにゃ……\x01",
            "ああ、我が家のベッドは\x01",
            "最高だなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "このまま泥のように\x01",
            "ねむりこけるとしよう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CE")

    label("loc_354E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_355C")
    Jump("loc_37CE")

    label("loc_355C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_356A")
    Jump("loc_37CE")

    label("loc_356A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3578")
    Jump("loc_37CE")

    label("loc_3578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3586")
    Jump("loc_37CE")

    label("loc_3586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3627")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A1")
    Call(0, 7)
    Jump("loc_3622")

    label("loc_35A1")


    #C0177
    ChrTalk(
        0xFE,
        (
            "うーん……\x01",
            "まあ、焦ることでもないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "僕の血をひいているんだから、\x01",
            "将来はきっと立派な技師に\x01",
            "なってくれるに違いないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3622")

    Jump("loc_37CE")

    label("loc_3627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_37CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3757")

    #C0179
    ChrTalk(
        0x101,
        (
            "#00005Fあ、ウェンディの\x01",
            "お父さんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x109,
        "#10100Fなんだかお疲れみたいですね。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "むにゃむにゃ……\x01",
            "出張から戻ったばかりなんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "パンセ、悪いけど\x01",
            "ご飯は一人で食べといてくれ……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#00004F……寝ぼけてるみたいだ。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        "#00100Fふふ、そっとしておいてあげましょう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37CE")

    label("loc_3757")


    #C0185
    ChrTalk(
        0xFE,
        (
            "……あれ、パンセは\x01",
            "どこにいったんだろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "ああ、そういえば\x01",
            "今日は日曜学校の日だったな……\x01",
            "むにゃむにゃ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CE")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F66 end

    def Function_9_37D2(): pass

    label("Function_9_37D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_396E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38DC")

    #C0187
    ChrTalk(
        0xFE,
        (
            "リュウのやつ、何やら子供たちだけで\x01",
            "近所の手伝いをして回るつもりらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "今日は商人としての勉強を\x01",
            "教えてやるつもりだったんじゃがな。\x01",
            "ううむ、体よく逃げられたわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "……まあ、何かしていないと\x01",
            "落ち着かんのかもしれんがのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3969")

    label("loc_38DC")


    #C0190
    ChrTalk(
        0xFE,
        (
            "リュウはまあいいが……\x01",
            "チルルはチルルで、旅を再開して\x01",
            "タングラム門のほうに行きおった。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "……まったく、\x01",
            "ウチの子は家に居つかんのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3969")

    Jump("loc_4596")

    label("loc_396E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_39F2")

    #C0192
    ChrTalk(
        0xFE,
        (
            "うちの子たちは家にいてくれて\x01",
            "とりあえずは安心じゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "外の様子が気になるのう。\x01",
            "どんな状況なんじゃろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_39F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB8")

    #C0194
    ChrTalk(
        0xFE,
        (
            "なにやらクロスベルで\x01",
            "大変なことが起こりそうじゃな……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "……ともかく、チルルが無事に\x01",
            "帰ってきて安心したわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "こういうときは、\x01",
            "家族みんなで一緒におらねばな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B30")

    label("loc_3AB8")


    #C0197
    ChrTalk(
        0xFE,
        (
            "なにやらクロスベルで\x01",
            "大変なことが起こりそうじゃな……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "何が起きてもいいように、\x01",
            "心の準備だけはしておかねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B30")

    Jump("loc_4596")

    label("loc_3B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BC6")

    #C0199
    ChrTalk(
        0xFE,
        (
            "事件は大変じゃったが……\x01",
            "ＩＢＣの業務が早いうちに\x01",
            "復旧してよかったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "銀行は商売人にとって\x01",
            "最も重要なものじゃからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_3BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3C3D")

    #C0201
    ChrTalk(
        0xFE,
        (
            "まさかこのような事件が起きるとは\x01",
            "思いもよらんかったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        "旅に出ておるチルルは大丈夫かのう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_3C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE0")

    #C0203
    ChrTalk(
        0xFE,
        (
            "わしも昔は、雨の中\x01",
            "裸足で走り回るような\x01",
            "やんちゃ坊主じゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "そういう意味では、\x01",
            "リュウはわしの子供のころに\x01",
            "よく似ておるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D42")

    label("loc_3CE0")


    #C0205
    ChrTalk(
        0xFE,
        (
            "リュウはわしの子供のころに\x01",
            "よく似ておるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "それだけに、\x01",
            "余計に手がかかるわけじゃがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D42")

    Jump("loc_4596")

    label("loc_3D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D9D")

    #C0207
    ChrTalk(
        0xFE,
        (
            "ふむ、なにやら\x01",
            "けたたましいサイレンの音が\x01",
            "聞こえてきおったが……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_3D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3EFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E77")

    #C0208
    ChrTalk(
        0xFE,
        (
            "娘のチルルが、\x01",
            "旅から戻ってきてな。\x01",
            "今は友達と出かけておるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "リュウにしろチルルにしろ、\x01",
            "友人関係にはずいぶんと\x01",
            "恵まれておるようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "いや、まったく\x01",
            "ありがたいことじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EF8")

    label("loc_3E77")


    #C0211
    ChrTalk(
        0xFE,
        (
            "チルルはほとんど家におらんのに、\x01",
            "カテリーナちゃんは\x01",
            "よう付き合ってくれておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "いや、まったく\x01",
            "ありがたいことじゃわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF8")

    Jump("loc_4596")

    label("loc_3EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F9B")

    #C0213
    ChrTalk(
        0xFE,
        (
            "今日はリュウのやつに\x01",
            "仕事を手伝わせようと\x01",
            "思うとったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "いつの間にやら\x01",
            "出かけておったようじゃな。\x01",
            "まったく、逃げ足の速い奴じゃよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_3F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4028")

    #C0215
    ChrTalk(
        0xFE,
        (
            "今日もリュウたちは\x01",
            "オルキスタワーを見に\x01",
            "出かけて行ったようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "まったく、昨日も見たろうに\x01",
            "よく飽きんもんじゃのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4596")

    label("loc_4028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CA")

    #C0217
    ChrTalk(
        0xFE,
        (
            "リュウにはいつか問屋の仕事を\x01",
            "継がせたいと思っておるのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "こやつときたら\x01",
            "遊ぶ事ばかり覚えおってな。\x01",
            "やれやれじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_413E")

    label("loc_40CA")


    #C0219
    ChrTalk(
        0xFE,
        (
            "リュウの奴は日曜学校の成績も\x01",
            "さっぱりなのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "遊ばせるばかりじゃなくて、\x01",
            "少しは勉強させなければのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_413E")

    Jump("loc_4596")

    label("loc_4143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4285")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_421E")

    #C0221
    ChrTalk(
        0xFE,
        (
            "わしは３年ほど前から\x01",
            "クロスベルで問屋業をしておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "今回は除幕式にあわせて、\x01",
            "百貨店から多めに\x01",
            "発注があったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "やはりクロスベルは活気があって、\x01",
            "商売をやるにはいい所じゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4280")

    label("loc_421E")


    #C0224
    ChrTalk(
        0xFE,
        (
            "今回は除幕式にあわせて、\x01",
            "百貨店から多めに\x01",
            "発注があったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "むほほ、大繁盛じゃわい。\x02",
    )

    CloseMessageWindow()

    label("loc_4280")

    Jump("loc_4596")

    label("loc_4285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4339")

    #C0226
    ChrTalk(
        0xFE,
        (
            "リュウのやつ、最近は\x01",
            "タリーズさんところのモモちゃんを\x01",
            "よく遊びに誘っておるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "危険な遊びなど教えておらんか、\x01",
            "ちょっと心配じゃのう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43BA")

    label("loc_4339")


    #C0228
    ChrTalk(
        0xFE,
        (
            "モモちゃんに\x01",
            "危険な遊びを教えたとあっては、\x01",
            "親御さんに申し訳が立たん。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "リュウのやつには\x01",
            "きちんと注意しておかねばのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43BA")

    Jump("loc_4596")

    label("loc_43BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A6")

    #C0230
    ChrTalk(
        0xFE,
        (
            "チルルもすぐ旅に出て\x01",
            "しまうじゃろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "家族が揃っておるうちに、\x01",
            "わしの得意なチャーハンでも\x01",
            "食わしてやるとするかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "わしはもともと共和国にいたんでな。\x01",
            "東方料理には馴染み深いんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_452C")

    label("loc_44A6")


    #C0233
    ChrTalk(
        0xFE,
        (
            "わしはもともと共和国にいたんでな。\x01",
            "東方料理には馴染み深いんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "ま、上手く作れるのは\x01",
            "チャーハンくらいのもんじゃがのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_452C")

    Jump("loc_4596")

    label("loc_4531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_454C")
    Call(0, 10)
    Jump("loc_4596")

    label("loc_454C")


    #C0235
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "どんな危ない目にあっても\x01",
            "まったく懲りる気配がないのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4596")

    TalkEnd(0xFE)
    Return()

    # Function_9_37D2 end

    def Function_10_459A(): pass

    label("Function_10_459A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0236
    ChrTalk(
        0xB,
        (
            "おうチルル、戻ったか。\x01",
            "今回の旅は随分長かったのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xB,
        (
            "確か、マインツ連峰を\x01",
            "踏破するなどと\x01",
            "無茶を言っておったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xD,
        (
            "うん……\x01",
            "途中でちょっと遭難しちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xD,
        (
            "ふう、まだまだ力不足みたい。\x01",
            "また次の機会に挑戦するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        "お前も懲りん奴じゃのう……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_459A end

    def Function_11_46BE(): pass

    label("Function_11_46BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_46CF")
    Jump("loc_47E6")

    label("loc_46CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_475D")

    #C0241
    ChrTalk(
        0xFE,
        (
            "戒厳令なんてつまんねーから\x01",
            "こっそり外に遊びに行こうとしてたら、\x01",
            "こんな事になっちゃってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "はあ、ワケがわかんないよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E6")

    label("loc_475D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4778")
    Call(0, 12)
    Jump("loc_47E6")

    label("loc_4778")


    #C0243
    ChrTalk(
        0xFE,
        (
            "うちの姉ちゃん、なんだか\x01",
            "変わってるんだよなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "よく自分からヘンな場所に\x01",
            "入ってみようと思うよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E6")

    TalkEnd(0xFE)
    Return()

    # Function_11_46BE end

    def Function_12_47EA(): pass

    label("Function_12_47EA")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0245
    ChrTalk(
        0xC,
        (
            "そういや姉ちゃん、\x01",
            "次はどこに旅に出るんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xD,
        (
            "んー……\x01",
            "当分は、クロスベル内を\x01",
            "歩き回るつもりかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xD,
        (
            "まだまだ行ったことのない\x01",
            "ところも多いし。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "うへー、姉ちゃんって\x01",
            "やっぱ変わりモンだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xC,
        (
            "よく自分からヘンな場所に\x01",
            "入ってみようと思うよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xD,
        "……あんたに言われたくないから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_47EA end

    def Function_13_4930(): pass

    label("Function_13_4930")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4941")
    Jump("loc_4C6F")

    label("loc_4941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4A28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F0")
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0251
    ChrTalk(
        0xFE,
        (
            "ただでさえ街から出れなくて\x01",
            "イライラしてるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "……ふん、寝る。\x01",
            "騒ぎが収まったら起こして。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        "ね、寝てる場合かよ～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4A23")

    label("loc_49F0")


    #C0254
    ChrTalk(
        0xFE,
        (
            "騒ぎが収まったら起こして。\x01",
            "……私、寝るから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A23")

    Jump("loc_4C6F")

    label("loc_4A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB5")

    #C0255
    ChrTalk(
        0xFE,
        (
            "最近、クロスベル全体が\x01",
            "おかしなことになってる気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "しばらく、旅をするのは\x01",
            "控えた方がいいのかも……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4B15")

    label("loc_4AB5")


    #C0257
    ChrTalk(
        0xFE,
        (
            "しばらく、旅をするのは\x01",
            "控えた方がいいのかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "……他にやる事ないし、\x01",
            "寝てようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B15")

    Jump("loc_4C6F")

    label("loc_4B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B28")
    Jump("loc_4C6F")

    label("loc_4B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B43")
    Call(0, 12)
    Jump("loc_4BE5")

    label("loc_4B43")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0259
    ChrTalk(
        0xFE,
        (
            "……前にジオフロントに入り込んで、\x01",
            "泣きながら救出されたあんたには\x01",
            "言われたくないから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0260
    ChrTalk(
        0xC,
        "なっ……泣いてねーしっ！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)

    label("loc_4BE5")

    Jump("loc_4C6F")

    label("loc_4BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C05")
    Call(0, 10)
    Jump("loc_4C6F")

    label("loc_4C05")


    #C0261
    ChrTalk(
        0xFE,
        (
            "マインツ連峰の踏破は、\x01",
            "私にはまだムリだった……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "次に挑戦したときは、\x01",
            "絶対に成し遂げてみせるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C6F")

    TalkEnd(0xFE)
    Return()

    # Function_13_4930 end

    SaveToFile()

Try(main)
