from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0510.bin",                # FileName
        "t0510",                    # MapName
        "t0510",                    # Location
        0x003D,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 61, 0, 3, 0, 4],
    )

    BuildStringList((
        "t0510",                  # 0
        "ビクセン町長",           # 1
        "アンナ夫人",             # 2
        "ミランダ",               # 3
        "ビルマ婆さん",           # 4
        "ルリエダ",               # 5
        "アミー",                 # 6
        "アレク",                 # 7
        "鉱員ガンツ",             # 8
        "鉱員ロージー",           # 9
        "鉱山長ホフマン",         # 10
        "鉱員マックス",           # 11
        "ミレイユ三尉",           # 12
        "警備隊員",               # 13
    ))

    AddCharChip((
        "chr/ch23200.itc",                   # 00
        "chr/ch23202.itc",                   # 01
        "chr/ch20100.itc",                   # 02
        "chr/ch20102.itc",                   # 03
        "chr/ch22700.itc",                   # 04
        "chr/ch23300.itc",                   # 05
        "chr/ch24300.itc",                   # 06
        "chr/ch23700.itc",                   # 07
        "chr/ch23000.itc",                   # 08
        "chr/ch30700.itc",                   # 09
        "chr/ch26202.itc",                   # 0A
        "chr/ch26302.itc",                   # 0B
        "chr/ch26202.itc",                   # 0C
        "chr/ch32600.itc",                   # 0D
        "chr/ch31200.itc",                   # 0E
        "chr/ch24302.itc",                   # 0F
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

    DeclNpc(-889,    949,     3319,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-6530,   750,     59,      270,  261,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(96099,   0,       4219,    0,    261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(49209,   0,       4369,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(147369,  0,       4179,    333,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(47450,   0,       -1500,   0,    389,  0x0, 0,   7,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(101800,  0,       500,     225,  389,  0x0, 0,   8,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(47450,   300,     0,       180,  389,  0x0, 0,   10,  0,   255, 255, 0,   11,  255,  0)
    DeclNpc(97459,   150,     -1169,   0,    453,  0x0, 0,   11,  0,   255, 255, 0,   7,   255,  0)
    DeclNpc(150729,  250,     100,     270,  453,  0x0, 0,   12,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(1200,    750,     -1000,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2200,    750,     -270,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   21,  255,  0)

    ChipFrameInfo(732, 0)                                        # 0

    ScpFunction((
        "Function_0_2DC",          # 00, 0
        "Function_1_38C",          # 01, 1
        "Function_2_3B7",          # 02, 2
        "Function_3_3E2",          # 03, 3
        "Function_4_62F",          # 04, 4
        "Function_5_668",          # 05, 5
        "Function_6_131F",         # 06, 6
        "Function_7_13F9",         # 07, 7
        "Function_8_166C",         # 08, 8
        "Function_9_2409",         # 09, 9
        "Function_10_25E3",        # 0A, 10
        "Function_11_26F1",        # 0B, 11
        "Function_12_27E1",        # 0C, 12
        "Function_13_3469",        # 0D, 13
        "Function_14_3586",        # 0E, 14
        "Function_15_3689",        # 0F, 15
        "Function_16_4767",        # 10, 16
        "Function_17_496B",        # 11, 17
        "Function_18_4C76",        # 12, 18
        "Function_19_5D33",        # 13, 19
        "Function_20_5E49",        # 14, 20
        "Function_21_608B",        # 15, 21
        "Function_22_622A",        # 16, 22
        "Function_23_6275",        # 17, 23
        "Function_24_72C4",        # 18, 24
    ))


    def Function_0_2DC(): pass

    label("Function_0_2DC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_314"),
        (1, "loc_320"),
        (2, "loc_32C"),
        (3, "loc_338"),
        (4, "loc_344"),
        (5, "loc_350"),
        (6, "loc_35C"),
        (SWITCH_DEFAULT, "loc_368"),
    )


    label("loc_314")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_320")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_32C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_338")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_344")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_350")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_368")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_374")

    label("loc_38B")

    Return()

    # Function_0_2DC end

    def Function_1_38C(): pass

    label("Function_1_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B6")
    OP_94(0xFE, 0xBD74, 0xA8C, 0xC92C, 0xFFFFFD44, 0x3E8)
    Sleep(250)
    Jump("Function_1_38C")

    label("loc_3B6")

    Return()

    # Function_1_38C end

    def Function_2_3B7(): pass

    label("Function_2_3B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E1")
    OP_94(0xFE, 0x192EE, 0x7F8, 0x1863C, 0xFFFFFB82, 0x3E8)
    Sleep(250)
    Jump("Function_2_3B7")

    label("loc_3E1")

    Return()

    # Function_2_3B7 end

    def Function_3_3E2(): pass

    label("Function_3_3E2")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x11, 0xB)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0xC)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_423")
    Jump("loc_60F")

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_60F")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4C2")
    SetChrPos(0xC, 147900, 250, 100, 90)
    SetChrChipByIndex(0xC, 0xF)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrChipByIndex(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x40)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 0, 750, -1000, 90)
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A9")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x13, 0x10)

    label("loc_4A9")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_60F")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D0")
    Jump("loc_60F")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4DE")
    Jump("loc_60F")

    label("loc_4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_518")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 101600, 0, 500, 225)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 50000, 0, 1000, 315)
    Jump("loc_60F")

    label("loc_518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_526")
    Jump("loc_60F")

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_534")
    Jump("loc_60F")

    label("loc_534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_542")
    Jump("loc_60F")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_550")
    Jump("loc_60F")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_55E")
    Jump("loc_60F")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_592")
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_60F")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5EA")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 1200, 750, -1000, 270)
    SetChrChipByIndex(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, 650, -1000, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E5")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_5E5")

    Jump("loc_60F")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_60F")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_606")
    Jump("loc_60F")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_60F")

    label("loc_60F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_62E")

    Return()

    # Function_3_3E2 end

    def Function_4_62F(): pass

    label("Function_4_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_641")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_667")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_667")

    Return()

    # Function_4_62F end

    def Function_5_668(): pass

    label("Function_5_668")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_740")

    #C0001
    ChrTalk(
        0xA,
        (
            "鉱山の再開はまだ早いような\x01",
            "気がするけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "町のみんなの気持ちを\x01",
            "ひとつにするには、\x01",
            "やっぱりこれしかないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xA,
        (
            "こうなったら旦那たちには\x01",
            "精一杯働いていてもらいたいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7BC")

    label("loc_740")


    #C0004
    ChrTalk(
        0xA,
        (
            "こうなったら旦那たちには\x01",
            "精一杯働いていてもらいたいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "私も美味しいお弁当を作って、\x01",
            "旦那を応援していかなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BC")

    Jump("loc_131B")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_86C")

    #C0006
    ChrTalk(
        0xA,
        (
            "アレクったら、町の近くにいた狼に\x01",
            "平気で近づいて撫でてたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        (
            "レジスタンスに協力してる\x01",
            "賢い動物だからよかったけど……\x01",
            "もう少し気をつけてほしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131B")

    label("loc_86C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_968")

    #C0008
    ChrTalk(
        0xA,
        (
            "ただでさえ物騒な状況だし、\x01",
            "旦那が鉱山に入らないで済むのは\x01",
            "ある意味安心だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "だけど、このままじゃ\x01",
            "マインツは寂れる一方でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "大統領も市外には\x01",
            "ほとんど手を入れてこないし、\x01",
            "この先どうなってしまうのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9FB")

    label("loc_968")


    #C0011
    ChrTalk(
        0xA,
        (
            "鉱山を閉鎖したままじゃ、\x01",
            "マインツは寂れる一方でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "大統領も市外には\x01",
            "ほとんど手を入れてこないし、\x01",
            "この先どうなってしまうのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FB")

    Jump("loc_131B")

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA6")

    #C0013
    ChrTalk(
        0xA,
        (
            "うちの旦那、この間の占領事件で\x01",
            "ちょっとケガしちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xA,
        (
            "大したことなかったから\x01",
            "よかったものの……\x01",
            "本当に心配したんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B2A")

    label("loc_AA6")


    #C0015
    ChrTalk(
        0xA,
        (
            "旦那はもう鉱山に復帰してるけど……\x01",
            "あの時はどうなる事かと思ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "勇敢なのはいいけど、\x01",
            "あまり無茶をしないでほしいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2A")

    Jump("loc_131B")

    label("loc_B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD9")

    #C0017
    ChrTalk(
        0xA,
        (
            "雨の日は鉱山の中も\x01",
            "結構冷えるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "でも、鉱員たちはみんな\x01",
            "薄着でも平気みたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xA,
        (
            "やれやれ、カゼなんか\x01",
            "引かなきゃいいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C54")

    label("loc_BD9")


    #C0020
    ChrTalk(
        0xA,
        (
            "雨の日は鉱山の中も\x01",
            "結構冷えるんだけど、\x01",
            "鉱員たちはみんな薄着なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "やれやれ、カゼなんか\x01",
            "引かなきゃいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C54")

    Jump("loc_131B")

    label("loc_C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CC9")

    #C0022
    ChrTalk(
        0xA,
        (
            "アレクったら何をあんな\x01",
            "大声で叫んでるのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xA,
        (
            "うるさいったら\x01",
            "ありゃしないんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131B")

    label("loc_CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD5")

    #C0024
    ChrTalk(
        0xA,
        (
            "鉱山長である旦那の影響もあって、\x01",
            "アレクは鉱員を目指してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        (
            "本当は反対したいけど……\x01",
            "子供のやりたいことに親が\x01",
            "口出しするのもよくないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "せめて大きな怪我をしないように、\x01",
            "大人になるまでは\x01",
            "ちゃんと見守ってあげないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E6E")

    label("loc_DD5")


    #C0027
    ChrTalk(
        0xA,
        (
            "鉱山長である旦那の影響もあって、\x01",
            "アレクは鉱員を目指してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        (
            "本当は反対したいけど……\x01",
            "あの子も真剣に考えてるし、\x01",
            "見守ってあげるべきよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6E")

    Jump("loc_131B")

    label("loc_E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19")

    #C0029
    ChrTalk(
        0xA,
        (
            "毎日、アレクが危険な場所に\x01",
            "足を踏み入れてないか心配だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "日曜学校の日は、\x01",
            "シスターが見ててくれるから\x01",
            "少しは安心できるわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F88")

    label("loc_F19")


    #C0031
    ChrTalk(
        0xA,
        (
            "日曜学校に行ってる間は\x01",
            "子供の心配をしなくて\x01",
            "よさそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "せっかくだから\x01",
            "くつろいでましょうかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F88")

    Jump("loc_131B")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1160")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E2")

    #C0033
    ChrTalk(
        0xA,
        (
            "昨日、鉱山で働いてる旦那に\x01",
            "お弁当を届けに行ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        (
            "そこで、アレクが勝手に\x01",
            "鉱山に入り込んでいたのを見つけてね。\x01",
            "それはもう叱り付けてやったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "あそこは危険だから入るなって\x01",
            "いつも言い聞かせてるのに、\x01",
            "あの子ときたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "旦那だけでも手一杯なんだから、\x01",
            "余計な心配をかけさせないで欲しいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_115B")

    label("loc_10E2")


    #C0037
    ChrTalk(
        0xA,
        (
            "鉱山は危険だから入るなって\x01",
            "いつも言い聞かせてるのに、\x01",
            "あの子ときたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "もっと私の言うことを\x01",
            "聞いてほしいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115B")

    Jump("loc_131B")

    label("loc_1160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11EE")

    #C0039
    ChrTalk(
        0xA,
        (
            "ホフマンったら、鉱山に行くのに\x01",
            "お弁当を忘れていっちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        (
            "お腹を空かしてるでしょうし、\x01",
            "届けにいってあげないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131B")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_131B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B4")

    #C0041
    ChrTalk(
        0xA,
        (
            "うちの子供、危ない所に\x01",
            "入りたがるから困ってるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "今朝もガンツさんが止めなきゃ\x01",
            "どうなったことか……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "そのうち大怪我しちゃうんじゃ\x01",
            "ないかしら、まったく。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_131B")

    label("loc_12B4")


    #C0044
    ChrTalk(
        0xA,
        (
            "うちの子供、どうも好奇心旺盛でね。\x01",
            "危ない所に入りたがるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xA,
        "旦那に似ちゃったのね、きっと。\x02",
    )

    CloseMessageWindow()

    label("loc_131B")

    TalkEnd(0xFE)
    Return()

    # Function_5_668 end

    def Function_6_131F(): pass

    label("Function_6_131F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1330")
    Jump("loc_13F5")

    label("loc_1330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13A6")

    #C0046
    ChrTalk(
        0xE,
        (
            "あーあ、雨だと\x01",
            "外で遊べないからつまんないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xE,
        (
            "お父さん、早く帰ってきて\x01",
            "遊んでくれないかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_13A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_13B4")
    Jump("loc_13F5")

    label("loc_13B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13C2")
    Jump("loc_13F5")

    label("loc_13C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13D0")
    Jump("loc_13F5")

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_13DE")
    Jump("loc_13F5")

    label("loc_13DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_13EC")
    Jump("loc_13F5")

    label("loc_13EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_13F5")

    label("loc_13F5")

    TalkEnd(0xFE)
    Return()

    # Function_6_131F end

    def Function_7_13F9(): pass

    label("Function_7_13F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_140A")
    Jump("loc_1668")

    label("loc_140A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_14F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AF")

    #C0048
    ChrTalk(
        0x11,
        (
            "クロスベル市のほうで\x01",
            "何やら大きな動きが\x01",
            "あったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x11,
        (
            "……やはり、俺達鉱員も\x01",
            "このままじゃいけねえ。\x01",
            "町長に相談してみるか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_14EE")

    label("loc_14AF")


    #C0050
    ChrTalk(
        0x11,
        (
            "俺達鉱員もこのままじゃいけねえ。\x01",
            "町長に相談してみるか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EE")

    Jump("loc_1668")

    label("loc_14F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DA")

    #C0051
    ChrTalk(
        0x11,
        (
            "独立国になって、\x01",
            "七耀石の取引きが激減したから\x01",
            "一旦鉱山が閉鎖されたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x11,
        (
            "他国との貿易が完全に\x01",
            "ストップしちまったから\x01",
            "仕方がねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x11,
        (
            "正直締まらねえが……\x01",
            "今の所は様子を見るしか\x01",
            "ねえだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1668")

    label("loc_15DA")


    #C0054
    ChrTalk(
        0x11,
        (
            "独立国になって、\x01",
            "七耀石の取引きが激減したから\x01",
            "一旦鉱山が閉鎖されたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x11,
        (
            "正直締まらねえが……\x01",
            "今の所は様子を見るしか\x01",
            "ねえだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1668")

    TalkEnd(0xFE)
    Return()

    # Function_7_13F9 end

    def Function_8_166C(): pass

    label("Function_8_166C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_17C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1745")

    #C0056
    ChrTalk(
        0xB,
        (
            "ロージーが鉱山に戻れて、\x01",
            "私も安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "クロスベルが\x01",
            "この先どうなるかは\x01",
            "まだ分からないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xB,
        (
            "若者達がしっかりと\x01",
            "地に足をつけてさえいれば、\x01",
            "きっと未来は拓かれるわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17C4")

    label("loc_1745")


    #C0059
    ChrTalk(
        0xB,
        (
            "ロージーが鉱山に戻れて、\x01",
            "私も安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xB,
        (
            "若者達がしっかりと\x01",
            "地に足をつけてさえいれば、\x01",
            "きっと未来は拓かれるわよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C4")

    Jump("loc_2405")

    label("loc_17C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_18BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186E")

    #C0061
    ChrTalk(
        0xB,
        (
            "独立国の無効宣言で、\x01",
            "大統領という存在の\x01",
            "正当性も挫かれた……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xB,
        (
            "私たちは今、歴史の\x01",
            "大きな岐路に立たされている\x01",
            "のかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18B6")

    label("loc_186E")


    #C0063
    ChrTalk(
        0xB,
        (
            "私たちは今、歴史の\x01",
            "大きな岐路に立たされている\x01",
            "のかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B6")

    Jump("loc_2405")

    label("loc_18BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198E")

    #C0064
    ChrTalk(
        0xB,
        (
            "クロスベルの独立が\x01",
            "ここまでの事態に発展するとは\x01",
            "思いも寄らなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xB,
        (
            "鉱山が封鎖されたことで\x01",
            "ロージーも気力を失って\x01",
            "しまったみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        "はあ、どうすればいいかしら。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19F8")

    label("loc_198E")


    #C0067
    ChrTalk(
        0xB,
        (
            "せっかくロージーが\x01",
            "鉱山の仕事にやる気を見出して\x01",
            "くれていたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        "はあ、どうすればいいかしら。\x02",
    )

    CloseMessageWindow()

    label("loc_19F8")

    Jump("loc_2405")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A96")

    #C0069
    ChrTalk(
        0xB,
        (
            "紛争の時代のように、\x01",
            "マインツの占拠なんてことが\x01",
            "また起こってしまうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "ああ、クロスベルは一体\x01",
            "どうなってしまったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2405")

    label("loc_1A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6C")

    #C0071
    ChrTalk(
        0xB,
        (
            "最近は街に出て行く人も\x01",
            "増えているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xB,
        (
            "ロージーたち若者は、\x01",
            "マインツの町を誇りに\x01",
            "思ってくれている。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xB,
        (
            "長くこの町に暮らしてきた\x01",
            "私にとって、これ以上\x01",
            "うれしい事はないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BF8")

    label("loc_1B6C")


    #C0074
    ChrTalk(
        0xB,
        (
            "ロージーたち若者は、\x01",
            "マインツの町を誇りに\x01",
            "思ってくれている。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "長くこの町に暮らしてきた\x01",
            "私にとって、これ以上\x01",
            "うれしい事はないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF8")

    Jump("loc_2405")

    label("loc_1BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCD")

    #C0076
    ChrTalk(
        0xB,
        (
            "ロージーはちゃんと\x01",
            "働くようになって、\x01",
            "毎日が充実してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xB,
        (
            "ふふ、あとはお嫁さんでも\x01",
            "連れてきてくれれば\x01",
            "私も安心できるのだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xB,
        (
            "まあ、まだまだ\x01",
            "先のことかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D3C")

    label("loc_1CCD")


    #C0079
    ChrTalk(
        0xB,
        (
            "ロージーがお嫁さんでも\x01",
            "連れてきてくれれば\x01",
            "私も安心できるのだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xB,
        (
            "まあ、まだまだ\x01",
            "先のことかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3C")

    Jump("loc_2405")

    label("loc_1D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3C")

    #C0081
    ChrTalk(
        0xB,
        "クロスベルの国家独立……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xB,
        (
            "今までこの地で暮らしてきた\x01",
            "私には現実味がない話だけど、\x01",
            "実現すればとても素敵だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "ただ、帝国も共和国も\x01",
            "決してよしとはしないはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "新たな争いの火種に\x01",
            "ならなければいいのだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EB7")

    label("loc_1E3C")


    #C0085
    ChrTalk(
        0xB,
        (
            "独立を提唱されて、\x01",
            "帝国と共和国が黙っているとは\x01",
            "到底思えないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "新たな争いの火種に\x01",
            "ならなければいいのだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB7")

    Jump("loc_2405")

    label("loc_1EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB8")

    #C0087
    ChrTalk(
        0xB,
        (
            "昔は、高山で落盤事故や\x01",
            "土砂崩れなんかが\x01",
            "よく起こっていたものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "でも、導力革命以降は\x01",
            "掘削技術も確立されてきて、\x01",
            "事故は滅多に起こらなくなった。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "技術の進歩は確実に人を救ってる。\x01",
            "とてもいい時代になったものだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_204D")

    label("loc_1FB8")


    #C0090
    ChrTalk(
        0xB,
        (
            "昔は落盤事故や土砂崩れが\x01",
            "よく起こっていたけど……\x01",
            "最近では殆どないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        (
            "技術の進歩は確実に人を救ってる。\x01",
            "とてもいい時代になったものだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204D")

    Jump("loc_2405")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_213D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DE")

    #C0092
    ChrTalk(
        0xB,
        (
            "アミーとロージーは、\x01",
            "二人揃うと騒がしくて\x01",
            "しょうがないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xB,
        (
            "ふふ、まあ兄妹仲が\x01",
            "よくてなによりだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2138")

    label("loc_20DE")


    #C0094
    ChrTalk(
        0xB,
        "それにしても……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xB,
        (
            "２人でじゃれてないで、\x01",
            "家事の手伝いでも\x01",
            "してくれたらいいのに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2138")

    Jump("loc_2405")

    label("loc_213D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EB")

    #C0096
    ChrTalk(
        0xB,
        (
            "近頃、孫のロージーが\x01",
            "仕事をサボらずにちゃんと\x01",
            "働くようになってくれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xB,
        (
            "ああ、これほど嬉しいことはないわ。\x01",
            "……空の女神よ、感謝します。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_228D")

    label("loc_21EB")


    #C0098
    ChrTalk(
        0xB,
        (
            "孫たちが一人前の人間に\x01",
            "なってくれることは、\x01",
            "私にとって何より嬉しいことよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xB,
        (
            "……空の女神よ、感謝します。\x01",
            "これからもあの子たちを\x01",
            "見守っていてくださいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228D")

    Jump("loc_2405")

    label("loc_2292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2380")

    #C0100
    ChrTalk(
        0xB,
        (
            "町を出てすぐの旧鉱山は、\x01",
            "数十年前の主要な坑道なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        (
            "全盛期は、大粒の結晶が\x01",
            "ザクザクと採掘されていた\x01",
            "宝の山だったんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xB,
        (
            "大昔、帝国と共和国が\x01",
            "紛争を繰り返して争った\x01",
            "理由の一つと言える場所ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2405")

    label("loc_2380")


    #C0103
    ChrTalk(
        0xB,
        (
            "旧鉱山は、採掘されつくして\x01",
            "廃坑になってしまったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "大昔のクロスベルにおいて、\x01",
            "間違いなく重要な\x01",
            "場所だったのは確かよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2405")

    TalkEnd(0xFE)
    Return()

    # Function_8_166C end

    def Function_9_2409(): pass

    label("Function_9_2409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_241A")
    Jump("loc_25DF")

    label("loc_241A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_251E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D9")

    #C0105
    ChrTalk(
        0xD,
        (
            "あら、あなたたち\x01",
            "雨の中カサもささずに\x01",
            "歩き回ってたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xD,
        "ふ～ん、なるほどなるほど……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        (
            "……これぞまさしく、\x01",
            "『水もしたたるイイ男』\x01",
            "ってところかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2519")

    label("loc_24D9")


    #C0108
    ChrTalk(
        0xD,
        (
            "あなたたち、まさしく\x01",
            "『水もしたたるイイ男』\x01",
            "ってところね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2519")

    Jump("loc_25DF")

    label("loc_251E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_252C")
    Jump("loc_25DF")

    label("loc_252C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_253A")
    Jump("loc_25DF")

    label("loc_253A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2548")
    Jump("loc_25DF")

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2563")
    Call(0, 10)
    Jump("loc_25C3")

    label("loc_2563")


    #C0109
    ChrTalk(
        0xD,
        (
            "お兄ちゃん、\x01",
            "浮いた話とかないから\x01",
            "つまんないのよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xD,
        "ま、私も似たようなもんだけど。\x02",
    )

    CloseMessageWindow()

    label("loc_25C3")

    Jump("loc_25DF")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25D6")
    Jump("loc_25DF")

    label("loc_25D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_25DF")

    label("loc_25DF")

    TalkEnd(0xFE)
    Return()

    # Function_9_2409 end

    def Function_10_25E3(): pass

    label("Function_10_25E3")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0111
    ChrTalk(
        0xD,
        (
            "ねえねえ、お兄ちゃん。\x01",
            "なんか浮いた話とかないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x10,
        (
            "そんなもんねーよ。\x01",
            "女とかめんどくせえだけだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xD,
        "なによ、つまんないの～。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        (
            "あ、ならガンツさんとかは？\x01",
            "カジノで綺麗なバニーガールと\x01",
            "ウハウハしてたりして……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x10,
        "知るかっ！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_10_25E3 end

    def Function_11_26F1(): pass

    label("Function_11_26F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2702")
    Jump("loc_27DD")

    label("loc_2702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2710")
    Jump("loc_27DD")

    label("loc_2710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_271E")
    Jump("loc_27DD")

    label("loc_271E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_272C")
    Jump("loc_27DD")

    label("loc_272C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_273A")
    Jump("loc_27DD")

    label("loc_273A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2755")
    Call(0, 10)
    Jump("loc_27C1")

    label("loc_2755")


    #C0116
    ChrTalk(
        0x10,
        (
            "ったく、アミーと話すのは\x01",
            "ほんとめんどくせえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x10,
        (
            "せっかくの休みなんだから\x01",
            "ダラダラさせてくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C1")

    Jump("loc_27DD")

    label("loc_27C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27D4")
    Jump("loc_27DD")

    label("loc_27D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_27DD")

    label("loc_27DD")

    TalkEnd(0xFE)
    Return()

    # Function_11_26F1 end

    def Function_12_27E1(): pass

    label("Function_12_27E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AC")

    #C0118
    ChrTalk(
        0xC,
        (
            "マックスが元気を取り戻して\x01",
            "あたしもほっとしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        (
            "鉱員たちは仕事に打ち込む姿が\x01",
            "やっぱり一番だねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "あたしもマインツの女として、\x01",
            "彼らを支えていかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_292B")

    label("loc_28AC")


    #C0121
    ChrTalk(
        0xC,
        (
            "マックスたち鉱員は\x01",
            "仕事に打ち込む姿が\x01",
            "やっぱり一番だねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xC,
        (
            "あたしもマインツの女として、\x01",
            "彼らを支えていかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292B")

    Jump("loc_3465")

    label("loc_2930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0C")

    #C0123
    ChrTalk(
        0xC,
        (
            "レジスタンスの人たちが\x01",
            "何か準備を進めてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        (
            "……あの占領事件のときみたいに、\x01",
            "警備隊の人たちが傷ついたりしたら\x01",
            "あたし達もやりきれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xC,
        "本当に気をつけてほしいものだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A92")

    label("loc_2A0C")


    #C0126
    ChrTalk(
        0xC,
        (
            "……あの占領事件のときみたいに、\x01",
            "警備隊の人たちが傷ついたりしたら\x01",
            "あたし達もやりきれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xC,
        "本当に気をつけてほしいものだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_2A92")

    Jump("loc_3465")

    label("loc_2A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB2")
    Call(0, 13)
    Jump("loc_2B4A")

    label("loc_2AB2")


    #C0128
    ChrTalk(
        0xC,
        (
            "マックスが\x01",
            "好きな仕事をできないのは\x01",
            "あたしも心苦しいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xC,
        (
            "なんとか無理にでも\x01",
            "元気を出してもらわなくちゃ、\x01",
            "この調子じゃ病気になっちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B4A")

    Jump("loc_3465")

    label("loc_2B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF7")

    #C0130
    ChrTalk(
        0xC,
        (
            "あたしたちを助けるために、\x01",
            "警備隊の人たちが何人も\x01",
            "犠牲になったんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "彼らにも待っている人たちが\x01",
            "いたろうに……言葉もないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C48")

    label("loc_2BF7")


    #C0132
    ChrTalk(
        0xC,
        (
            "警備隊の人たちにも、\x01",
            "待っている人たちがいたろうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        "……言葉もないよ。\x02",
    )

    CloseMessageWindow()

    label("loc_2C48")

    Jump("loc_3465")

    label("loc_2C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D34")

    #C0134
    ChrTalk(
        0xC,
        (
            "あんたたち、雨の日のマインツは\x01",
            "気をつけないといけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "足でも滑らせたら、\x01",
            "崖の下にまっさかさま……\x01",
            "なんてことになりかねないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xC,
        (
            "あたしもマックスも、\x01",
            "小さい頃はよく注意されたもんさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DAE")

    label("loc_2D34")


    #C0137
    ChrTalk(
        0xC,
        (
            "あんたたち、雨の日のマインツは\x01",
            "気をつけないといけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        (
            "あたしもマックスも、\x01",
            "小さい頃はよく注意されたもんさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DAE")

    Jump("loc_3465")

    label("loc_2DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EAD")

    #C0139
    ChrTalk(
        0xC,
        (
            "最近、旦那が異様に\x01",
            "仕事にハリキリだしてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        (
            "ガンツさんやロージーさんが\x01",
            "やる気を出してきたから、\x01",
            "旦那にも火がついたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        (
            "毎朝出かけるのが早くなって、\x01",
            "弁当を準備するあたしも\x01",
            "なかなかタイヘンになったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F5B")

    label("loc_2EAD")


    #C0142
    ChrTalk(
        0xC,
        (
            "ガンツさんやロージーさんが\x01",
            "やる気を出してきたから、\x01",
            "旦那にも火がついたみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        (
            "毎朝出かけるのが早くなって、\x01",
            "弁当を準備するあたしも\x01",
            "なかなかタイヘンになったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5B")

    Jump("loc_3465")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3036")

    #C0144
    ChrTalk(
        0xC,
        (
            "なんでも、北の山岳地帯で\x01",
            "大きな魔獣が出たんだってねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xC,
        (
            "町からもそう遠くない場所だし、\x01",
            "鉱山にも湧いて出ないか心配だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        (
            "大型魔獣となると鉱員だけじゃ\x01",
            "対処できないからねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30C3")

    label("loc_3036")


    #C0147
    ChrTalk(
        0xC,
        (
            "北の山岳地帯に\x01",
            "大きな魔獣が出たんだってねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xC,
        (
            "鉱山にも湧いて出ないか心配だよ。\x01",
            "大型魔獣となると鉱員だけじゃ\x01",
            "対処できないからねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C3")

    Jump("loc_3465")

    label("loc_30C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_315E")

    #C0149
    ChrTalk(
        0xC,
        (
            "クロスベル市では\x01",
            "通商会議なんてものが\x01",
            "開かれてるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xC,
        (
            "会議の内容によっちゃ、\x01",
            "マインツのこれからにも\x01",
            "影響があるのかねえ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3465")

    label("loc_315E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31F9")

    #C0151
    ChrTalk(
        0xC,
        (
            "マックスは、今日は\x01",
            "鉱山長と飲みにいっちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "いつもは人一倍働いてるんだ、\x01",
            "休みの日はしっかりと\x01",
            "気分転換してもらわなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3465")

    label("loc_31F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E0")

    #C0153
    ChrTalk(
        0xC,
        (
            "埋まっている七耀石に惹かれて、\x01",
            "鉱山には魔獣が湧いちまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "普通なら危険なんだが、\x01",
            "マインツの鉱員は\x01",
            "そりゃあ屈強な男揃いでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xC,
        (
            "ちょっとやそっとの魔獣なら\x01",
            "自分たちでなんとかしちまうのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3350")

    label("loc_32E0")


    #C0156
    ChrTalk(
        0xC,
        (
            "マインツの鉱員は\x01",
            "そりゃあ屈強な男揃いでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "鉱山に湧いた魔獣程度なら\x01",
            "自分たちでなんとかしちまうのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3350")

    Jump("loc_3465")

    label("loc_3355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3402")

    #C0158
    ChrTalk(
        0xC,
        (
            "あたしの旦那は、\x01",
            "鉱員をやっていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        (
            "今の若手の中じゃ\x01",
            "一番の稼ぎ頭なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        (
            "さて、今日も\x01",
            "夕飯をたっぷり用意して\x01",
            "待ってなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3465")

    label("loc_3402")


    #C0161
    ChrTalk(
        0xC,
        (
            "さ、今日も旦那が\x01",
            "腹を空かして\x01",
            "帰ってくるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        (
            "夕飯をたっぷり用意して\x01",
            "待ってなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3465")

    TalkEnd(0xFE)
    Return()

    # Function_12_27E1 end

    def Function_13_3469(): pass

    label("Function_13_3469")

    OP_4B(0xC, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0163
    ChrTalk(
        0x12,
        (
            "はあ……俺には穴掘りしか\x01",
            "取り柄がないってのに、\x01",
            "鉱山の仕事ができないなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xC,
        (
            "マックス、落ち込むのも\x01",
            "いい加減にしなさいって。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "少ししたらまた鉱山にも\x01",
            "入れるようになるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x12,
        (
            "だといいんだけど……\x01",
            "……………はあ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        "……まったく。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_3469 end

    def Function_14_3586(): pass

    label("Function_14_3586")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3597")
    Jump("loc_3685")

    label("loc_3597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3633")

    #C0168
    ChrTalk(
        0x12,
        (
            "鉱山の仕事が出来ない分、\x01",
            "町内の力仕事とかを\x01",
            "色々やってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x12,
        (
            "だけどやっぱり、\x01",
            "鉱山に入ってないとなあ……\x01",
            "イマイチ調子が出ないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3685")

    label("loc_3633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_364E")
    Call(0, 13)
    Jump("loc_3685")

    label("loc_364E")


    #C0170
    ChrTalk(
        0x12,
        (
            "はあ……俺には穴掘りしか\x01",
            "取り柄がないってのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3685")

    TalkEnd(0xFE)
    Return()

    # Function_14_3586 end

    def Function_15_3689(): pass

    label("Function_15_3689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A0")
    Call(0, 24)
    Return()

    label("loc_36A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36BF")
    Call(0, 16)
    Return()

    label("loc_36BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_383B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C6")

    #C0171
    ChrTalk(
        0x8,
        (
            "レジスタンスとなっていた\x01",
            "警備隊の諸君は、無事に\x01",
            "国防軍と合流出来たらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "大統領が拘束された今……\x01",
            "もはや彼らと敵対する理由も\x01",
            "なくなったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "ミレイユ君たちの抵抗活動も、\x01",
            "ようやく功を奏したわけだ。\x01",
            "……私も安心したよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3836")

    label("loc_37C6")


    #C0174
    ChrTalk(
        0x8,
        (
            "マインツも鉱山を再開し、\x01",
            "活気を取り戻し始めた。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "だが、まだまだこれからが\x01",
            "本当の戦いというところだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3836")

    Jump("loc_4763")

    label("loc_383B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3A00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3947")

    #C0176
    ChrTalk(
        0x8,
        (
            "大統領の正当性が揺らぎ、\x01",
            "国防軍も様子見になったと聞く。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "ミレイユ君たちは、\x01",
            "クロスベル市の解放を視野に入れて\x01",
            "着々と準備を整えているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "……レジスタンスの諸君が\x01",
            "無事に使命を成し遂げんことを、\x01",
            "女神に祈らせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39FB")

    label("loc_3947")


    #C0179
    ChrTalk(
        0x8,
        (
            "ミレイユ君たちは、\x01",
            "クロスベル市の解放を視野に入れて\x01",
            "着々と準備を整えているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "……レジスタンスの諸君が\x01",
            "無事に使命を成し遂げんことを、\x01",
            "女神に祈らせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FB")

    Jump("loc_4763")

    label("loc_3A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3AD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1B")
    Call(0, 17)
    Jump("loc_3ACD")

    label("loc_3A1B")


    #C0181
    ChrTalk(
        0x8,
        (
            "もともとマインツでは、\x01",
            "あの猟兵たちを平然と運用する\x01",
            "大統領には不信感しかなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "今の体制をなんとかしようと足掻く\x01",
            "レジスタンスの諸君は、\x01",
            "私達にとっての希望なのだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ACD")

    Jump("loc_4763")

    label("loc_3AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB9")

    #C0183
    ChrTalk(
        0x8,
        "君たちか……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#00003Fビクセン町長……\x01",
            "マインツも大変でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "ああ……\x01",
            "深刻な被害は殆ど無かったが\x01",
            "さすがに皆、ショックを受けてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "遊撃士殿にも協力してもらって、\x01",
            "しばらくはそれを癒すのに\x01",
            "専念していたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00108F事件の衝撃は相当なもの\x01",
            "だったでしょうしね……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "ああ……今では大分、\x01",
            "落ち着いてきたようだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "とにかく、私は町長として\x01",
            "できるかぎりの事を\x01",
            "やっていくつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x8,
        (
            "君たちも、色々大変だろうが\x01",
            "頑張ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 2)
    Jump("loc_3D34")

    label("loc_3CB9")


    #C0191
    ChrTalk(
        0x8,
        (
            "とにかく、私は町長として\x01",
            "できるかぎりの事を\x01",
            "やっていくつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "君たちも、色々大変だろうが\x01",
            "頑張ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D34")

    Jump("loc_4763")

    label("loc_3D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7D")

    #C0193
    ChrTalk(
        0x8,
        (
            "近頃、得体のしれない大型の魔獣を\x01",
            "見かけたと言う話をよく聞くな。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        (
            "昨日起こったという脱線事故でも、\x01",
            "巨大な化物が目撃されたそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "これらは以前、旧鉱山で\x01",
            "現れたという大型の魔獣と\x01",
            "何か関係があるのだろうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "……なんにせよ、皆の安全の為にも\x01",
            "注意しておいた方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F0B")

    label("loc_3E7D")


    #C0197
    ChrTalk(
        0x8,
        (
            "近頃、得体のしれない大型の魔獣を\x01",
            "見かけたと言う話をよく聞くが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "……なんにせよ、皆の安全の為にも\x01",
            "注意しておいた方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0B")

    Jump("loc_4763")

    label("loc_3F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_40CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4047")

    #C0199
    ChrTalk(
        0x8,
        (
            "最近、遊撃士たちが\x01",
            "以前より忙しくしているようでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x8,
        (
            "よほど緊急性の高い依頼でないと\x01",
            "頼みにくくなってしまったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "どうやら最近出ると言う\x01",
            "大型で得体の知れない魔獣を\x01",
            "調査しているようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "ふむ、嫌な予感がするよ。\x01",
            "クロスベルで何かが\x01",
            "起こりつつあるのだろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40CA")

    label("loc_4047")


    #C0203
    ChrTalk(
        0x8,
        (
            "遊撃士の忙しさが、\x01",
            "ここ最近増しているようでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        (
            "ふむ、嫌な予感がするよ。\x01",
            "クロスベルで何かが\x01",
            "起こりつつあるのだろうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40CA")

    Jump("loc_4763")

    label("loc_40CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E0")

    #C0205
    ChrTalk(
        0x8,
        (
            "クロスベルの国家独立……\x01",
            "まさかそんなことが\x01",
            "提唱される日が来るとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        (
            "鉱山資源のため帝国と共和国に\x01",
            "争われた歴史を持つこの町でも、\x01",
            "真剣に論じるべき問題だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "その是非については、\x01",
            "マインツの住民一人一人に\x01",
            "考えてもらわなくてはな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_426B")

    label("loc_41E0")


    #C0208
    ChrTalk(
        0x8,
        (
            "国家独立の是非は\x01",
            "マインツの住民にも一人一人\x01",
            "考えてもらわなくてはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "投票日までは私も一住民として、\x01",
            "考えを巡らせているとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426B")

    Jump("loc_4763")

    label("loc_4270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_43D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4352")

    #C0210
    ChrTalk(
        0x8,
        "ガンツは、あれで気前のいい男でな。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "ごく稀にカジノで勝ってきても、\x01",
            "景品を配ったり酒をおごったりして\x01",
            "すぐに使ってしまうのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "むしろ、スッて帰るより\x01",
            "ミラが飛んでいっている気もするな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43D2")

    label("loc_4352")


    #C0213
    ChrTalk(
        0x8,
        (
            "ガンツは、スッて帰るより\x01",
            "勝って帰ったときの方が\x01",
            "ミラが飛んでいっている気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        "まあ、彼らしいといえばらしいがね。\x02",
    )

    CloseMessageWindow()

    label("loc_43D2")

    Jump("loc_4763")

    label("loc_43D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F1")

    #C0215
    ChrTalk(
        0x8,
        (
            "超高層ビルディング、\x01",
            "オルキスタワーか……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "技術の進歩は大いに\x01",
            "歓迎したいところなのだが、\x01",
            "なんだか複雑な気分だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "マインツという町がまた一歩\x01",
            "時代に取り残された気がしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x8,
        (
            "……ハハ、まあ気にしないでくれ。\x01",
            "ただの年寄りの独り言だからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_457C")

    label("loc_44F1")


    #C0219
    ChrTalk(
        0x8,
        (
            "ともあれ、通商会議の開催には\x01",
            "大きな意義があると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "自治州の未来のため、\x01",
            "ディーター市長たちには\x01",
            "是非頑張ってほしいものだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_457C")

    Jump("loc_4763")

    label("loc_4581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_460F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4599")
    Jump("loc_460A")

    label("loc_4599")


    #C0221
    ChrTalk(
        0x8,
        (
            "その旧鉱山の合鍵は、\x01",
            "念のために君達に\x01",
            "渡しておくとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "時々そっちでも\x01",
            "様子を見てくれると助かるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460A")

    Jump("loc_4763")

    label("loc_460F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_4763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E3")

    #C0223
    ChrTalk(
        0x8,
        (
            "旧鉱山は町を出て、\x01",
            "少し下ってから\x01",
            "北西に登った先にある。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "何故扉が壊されていたのか、\x01",
            "坑道で何が起こっているのか、\x01",
            "私たちにも判らない。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "どうか、\x01",
            "くれぐれも気を付けてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4763")

    label("loc_46E3")


    #C0226
    ChrTalk(
        0x8,
        (
            "旧鉱山は町を出て、\x01",
            "少し下ってから\x01",
            "北西に登った先にある。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "ガンツが入口を\x01",
            "開けてくれているから、\x01",
            "そちらに向かってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4763")

    TalkEnd(0xFE)
    Return()

    # Function_15_3689 end

    def Function_16_4767(): pass

    label("Function_16_4767")


    #C0228
    ChrTalk(
        0x8,
        (
            "つい先日、壊れた旧鉱山の扉を\x01",
            "新しい頑丈なものに取り変えてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "そうだ、念のために\x01",
            "これを預かっておいてくれるかね？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x323),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x323, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0231
    ChrTalk(
        0x102,
        (
            "#00105Fえっと、いいんですか？\x01",
            "一応私たちは部外者なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        "ああ、君たちなら信用できるからね。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "何か調べたいことがあったら\x01",
            "自由に入ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "念のため、奥との行き来もしやすいよう\x01",
            "ハシゴもかけなおしておいたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#00000Fありがとうございます。\x01",
            "大切に保管させていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 3)
    TalkEnd(0x8)
    Return()

    # Function_16_4767 end

    def Function_17_496B(): pass

    label("Function_17_496B")

    OP_4B(0x8, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0236
    ChrTalk(
        0x8,
        (
            "ふむ、それでは食糧の方は\x01",
            "こちらに任せてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "それと、装備をメンテナンスするための\x01",
            "オイルなども必要ではないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        (
            "そちらはベッカライ君の店に\x01",
            "備蓄があるだろうから確認してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x13,
        (
            "#07902Fええ、よろしくお願いします。\x02\x03",

            "#07908F……マインツの皆さんには\x01",
            "本当に感謝してもしきれません。\x02\x03",

            "#07903Fもし私達に協力しているのが\x01",
            "国防軍にばれたら、\x01",
            "その危険を考えると……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "はは、なんの……\x01",
            "気にしないでくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "もともとマインツでは、\x01",
            "あの猟兵たちを平然と運用する\x01",
            "大統領には不信感しかなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        (
            "そんな中……現状に異を唱える\x01",
            "レジスタンスの諸君が現れたことは、\x01",
            "私達にとっての希望に他ならない。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x8,
        (
            "これからも出来る限り、\x01",
            "君達の活動には協力させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x13,
        (
            "#07904F……ありがとうございます。\x01",
            "このご恩は決して忘れません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AE, 7)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x13, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_17_496B end

    def Function_18_4C76(): pass

    label("Function_18_4C76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D90")

    #C0245
    ChrTalk(
        0x9,
        (
            "長いレジスタンス活動、\x01",
            "ミレイユさんたち警備隊は\x01",
            "本当によく頑張ってくれたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x9,
        (
            "町を発つときに、何度も何度も\x01",
            "お礼を言ってくれたけど……\x01",
            "私達こそお礼を言いたいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x9,
        (
            "全てが終わって落ち着いたら、\x01",
            "きっとまた彼女達を\x01",
            "マインツに招待したいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E32")

    label("loc_4D90")


    #C0248
    ChrTalk(
        0x9,
        (
            "長いレジスタンス活動、\x01",
            "ミレイユさんたち警備隊は\x01",
            "本当によく頑張ってくれたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        (
            "全てが終わって落ち着いたら、\x01",
            "きっとまた彼女達を\x01",
            "マインツに招待したいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E32")

    Jump("loc_5D2F")

    label("loc_4E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F03")

    #C0250
    ChrTalk(
        0x9,
        (
            "ミレイユさんたちは今、\x01",
            "宿の方で休息をとっているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x9,
        (
            "近いうちに更に忙しくなるって\x01",
            "言っていた事だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "この機会に、きちんと休みを\x01",
            "取ってもらいたいものだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F7D")

    label("loc_4F03")


    #C0253
    ChrTalk(
        0x9,
        (
            "ミレイユさんたちは今、\x01",
            "宿の方で休息をとっているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x9,
        (
            "この機会に、きちんと休みを\x01",
            "取ってもらいたいものだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F7D")

    Jump("loc_5D2F")

    label("loc_4F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_50CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5082")

    #C0255
    ChrTalk(
        0x9,
        (
            "レジスタンスの皆さんは\x01",
            "山岳地帯の入り組んだ地点に\x01",
            "キャンプを組んでいるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "いくら野外活動に慣れてるとはいえ、\x01",
            "この状態が長引くのは苦しいはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x9,
        (
            "国防軍や猟兵の捜索が、\x01",
            "少しは落ち着いてくれれば\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_50C8")

    label("loc_5082")


    #C0258
    ChrTalk(
        0x9,
        (
            "国防軍や猟兵の捜索が、\x01",
            "少しは落ち着いてくれれば\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C8")

    Jump("loc_5D2F")

    label("loc_50CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_523D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A6")

    #C0259
    ChrTalk(
        0x9,
        (
            "この間エオリアさんに、\x01",
            "心が落ち着くハーブティ－を\x01",
            "分けてもらってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x9,
        (
            "おかげで私もこの一週間で、\x01",
            "かなり気持ちに整理がついたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x9,
        (
            "エオリアさんたちには\x01",
            "感謝しないといけないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5238")

    label("loc_51A6")


    #C0262
    ChrTalk(
        0x9,
        (
            "エオリアさんたち、\x01",
            "今日は廃坑に出た魔獣を\x01",
            "退治しに来てくれたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x9,
        (
            "色々と助けてもらって、\x01",
            "彼女たちには本当に\x01",
            "感謝しないといけないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5238")

    Jump("loc_5D2F")

    label("loc_523D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5312")

    #C0264
    ChrTalk(
        0x9,
        "山の天気は崩れやすいのよね。\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        (
            "あまりひどいと、バスの運行すら\x01",
            "止まってしまうことだってあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x9,
        (
            "今日はそこまで土砂降りじゃないけど、\x01",
            "行き来するなら充分気をつけるといいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53A8")

    label("loc_5312")


    #C0267
    ChrTalk(
        0x9,
        (
            "雨がひどいと、バスの運行すら\x01",
            "止まってしまうことだってあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x9,
        (
            "今日はそこまで土砂降りじゃないけど、\x01",
            "行き来するなら充分気をつけるといいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53A8")

    Jump("loc_5D2F")

    label("loc_53AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5496")

    #C0269
    ChrTalk(
        0x9,
        (
            "鉱員さんたちの見合い相手、\x01",
            "なかなか見つからないわねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x9,
        (
            "ガンツさんもマルロさんも\x01",
            "ロージーさんも、見合いの話には\x01",
            "乗り気じゃないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x9,
        (
            "若い子はあまり結婚とかに\x01",
            "憧れがないのかしら……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5521")

    label("loc_5496")


    #C0272
    ChrTalk(
        0x9,
        (
            "ガンツさんもマルロさんも\x01",
            "ロージーさんも、見合いの話には\x01",
            "乗り気じゃないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        (
            "若い子はあまり結婚とかに\x01",
            "憧れがないのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5521")

    Jump("loc_5D2F")

    label("loc_5526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_56DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5630")

    #C0274
    ChrTalk(
        0x9,
        (
            "クロスベルは、帝国と共和国に\x01",
            "あわせて１０％もの税収を\x01",
            "収める決まりになっているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        (
            "経済の発展しているクロスベルで\x01",
            "税収の１０％といえば物凄い額よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        (
            "この自治州が２大国に\x01",
            "従属されているという、\x01",
            "象徴ともいえる取り決めなのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_56DA")

    label("loc_5630")


    #C0277
    ChrTalk(
        0x9,
        (
            "クロスベルは、帝国と共和国に\x01",
            "あわせて１０％もの税収を\x01",
            "収める決まりになっているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x9,
        (
            "この自治州が２大国に\x01",
            "従属されているという、\x01",
            "象徴ともいえる取り決めなのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56DA")

    Jump("loc_5D2F")

    label("loc_56DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_58ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_586F")

    #C0279
    ChrTalk(
        0x9,
        "あら、あなた……\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x9,
        (
            "もしよかったら\x01",
            "マインツの鉱員さんと\x01",
            "お見合いしてみないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#00205F……もしかして、私に\x01",
            "聞いているんでしょうか。\x02\x03",

            "まだ私は結婚できる年齢では\x01",
            "ありませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x9,
        (
            "ふふ、だってとっても\x01",
            "美人さんなんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x9,
        (
            "大きくなって相手がいなかったら、\x01",
            "是非話に乗ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x103,
        "#00211F（……微妙に失礼ですね。）\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        "#00012F（は、はは……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_58E8")

    label("loc_586F")


    #C0286
    ChrTalk(
        0x9,
        (
            "ふふ、大きくなって\x01",
            "相手がいなかったら、\x01",
            "是非話に乗ってちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x9,
        (
            "あなた見たいな可愛い子なら\x01",
            "大歓迎だから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E8")

    Jump("loc_5D2F")

    label("loc_58ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_597D")

    #C0288
    ChrTalk(
        0x9,
        "今日は鉱山はお休みにしているの。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x9,
        (
            "あなたたちなら大丈夫だと思うけど、\x01",
            "もし入るつもりなら\x01",
            "魔獣には気をつけてちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D2F")

    label("loc_597D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B47")

    #C0290
    ChrTalk(
        0x9,
        "そうだ……あなたたち。\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x9,
        (
            "マインツにいる鉱員たちと\x01",
            "お見合いしてみないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        "#00105Fお、お見合いですか？\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x9,
        (
            "ええ、ガンツさんたちも\x01",
            "帰りを待ってくれる人がいれば\x01",
            "もっと仕事を頑張れると思うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x9,
        "どうかしら、お嬢さんたち？\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        (
            "#00106Fえ、えっと……すみません。\x01",
            "まだ結婚とかは考えてなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x109,
        (
            "#10106Fじ、自分も今は\x01",
            "仕事が大事なので……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        "そう……残念ねえ。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x9,
        (
            "まあ、気が向いたら\x01",
            "考えておいてちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BB9")

    label("loc_5B47")


    #C0299
    ChrTalk(
        0x9,
        (
            "お見合いのことは、気が向いたら\x01",
            "考えておいてちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "私がはりきって\x01",
            "セッティングさせてもらうから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB9")

    Jump("loc_5D2F")

    label("loc_5BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_5D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAE")

    #C0301
    ChrTalk(
        0x9,
        (
            "あの旧鉱山は、数十年前\x01",
            "まだ紛争が起こっていた時代に\x01",
            "使われていた坑道なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x9,
        (
            "入り組んでいて危険だから、\x01",
            "先代が厳重に閉じたと\x01",
            "聞いているのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x9,
        (
            "一体誰が鍵を壊したのかしら。\x01",
            "なんだか不気味ね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D2F")

    label("loc_5CAE")


    #C0304
    ChrTalk(
        0x9,
        (
            "あの旧鉱山は、\x01",
            "入り組んでいて危険だから\x01",
            "厳重に閉じられたのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x9,
        (
            "一体誰が鍵を壊したのかしら。\x01",
            "なんだか不気味ね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D2F")

    TalkEnd(0xFE)
    Return()

    # Function_18_4C76 end

    def Function_19_5D33(): pass

    label("Function_19_5D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D4A")
    Call(0, 24)
    Return()

    label("loc_5D4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D5B")
    Jump("loc_5E45")

    label("loc_5D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5D69")
    Jump("loc_5E45")

    label("loc_5D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5D77")
    Jump("loc_5E45")

    label("loc_5D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5D85")
    Jump("loc_5E45")

    label("loc_5D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5D93")
    Jump("loc_5E45")

    label("loc_5D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5DA1")
    Jump("loc_5E45")

    label("loc_5DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DB9")
    Jump("loc_5E37")

    label("loc_5DB9")


    #C0306
    ChrTalk(
        0xF,
        (
            "あんな大粒の七耀石を\x01",
            "大量に仕入れていくなんて、\x01",
            "そこらの商人じゃマネできないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xF,
        "……本当に何モンだったんだろうな。\x02",
    )

    CloseMessageWindow()

    label("loc_5E37")

    Jump("loc_5E45")

    label("loc_5E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_5E45")

    label("loc_5E45")

    TalkEnd(0xFE)
    Return()

    # Function_19_5D33 end

    def Function_20_5E49(): pass

    label("Function_20_5E49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5E5A")
    Jump("loc_6087")

    label("loc_5E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5E68")
    Jump("loc_6087")

    label("loc_5E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6087")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E83")
    Call(0, 17)
    Jump("loc_6087")

    label("loc_5E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF6")

    #C0308
    ChrTalk(
        0x13,
        (
            "#07903F苦しい状況は変わりないけど、\x01",
            "しばらくは山岳地帯で\x01",
            "がんばってみるつもりよ。\x02\x03",

            "#07901Fランディ、支援課の皆さん……\x01",
            "こっちは任せてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x104,
        (
            "#00303Fああ、わかった。\x02\x03",

            "#00301F……猟兵や国防軍に\x01",
            "負けるんじゃねえぞ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)

    #C0310
    ChrTalk(
        0x13,
        (
            "#07902Fふふ、誰に言ってるの。\x02\x03",

            "#07904Fそれにマインツの皆さんが\x01",
            "協力してくれてるんだし、\x01",
            "きっと私たちは大丈夫よ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6087")

    label("loc_5FF6")


    #C0311
    ChrTalk(
        0x13,
        (
            "#07900Fランディ、支援課の皆さん……\x01",
            "こっちは任せてちょうだい。\x02\x03",

            "#07904Fマインツの皆さんが\x01",
            "協力してくれてるし、\x01",
            "きっと私たちは大丈夫だから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6087")

    TalkEnd(0xFE)
    Return()

    # Function_20_5E49 end

    def Function_21_608B(): pass

    label("Function_21_608B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6185")

    #C0312
    ChrTalk(
        0x14,
        (
            "神狼の助けが得られたことで、\x01",
            "自分達も動きやすくなりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x14,
        (
            "山道の見張りや山岳地帯の警戒……\x01",
            "それらを任せるだけでも\x01",
            "相当に負担を減らせますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x14,
        (
            "ミレイユ三尉には、この機に\x01",
            "出来るだけ休んで欲しいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6226")

    label("loc_6185")


    #C0315
    ChrTalk(
        0x14,
        (
            "山道の見張りや山岳地帯の警戒……\x01",
            "それらを神狼たちに任せるだけでも\x01",
            "相当に負担を減らせます。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x14,
        (
            "ミレイユ三尉には、この機に\x01",
            "出来るだけ休んで欲しいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6226")

    TalkEnd(0xFE)
    Return()

    # Function_21_608B end

    def Function_22_622A(): pass

    label("Function_22_622A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6274")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x1555), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_624A")
    Sleep(1500)
    Jump("loc_625F")

    label("loc_624A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2500)

    label("loc_625F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_626F")
    Sleep(333)

    label("loc_626F")

    Jump("Function_22_622A")

    label("loc_6274")

    Return()

    # Function_22_622A end

    def Function_23_6275(): pass

    label("Function_23_6275")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30700.itc", 0x1E)
    LoadChrToIndex("chr/ch30702.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    OP_68(560, 2250, -1210, 0)
    MoveCamera(312, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x101, 700, 750, -8600, 0)
    SetChrPos(0x102, -500, 750, -8600, 0)
    SetChrPos(0x109, 700, 750, -10000, 0)
    SetChrPos(0x105, -500, 750, -10000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -250, 650, -1000, 90)
    SetChrChipByIndex(0x8, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 600, 750, -500, 135)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2000, 750, -1000, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(34000, 1500)
    BeginChrThread(0x9, 1, 0, 22)
    Sleep(300)
    BeginChrThread(0xF, 1, 0, 22)
    Sleep(300)
    BeginChrThread(0x8, 1, 0, 22)
    OP_0D()
    Sleep(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    Sound(103, 0, 100, 0)
    Sleep(300)

    #C0317
    ChrTalk(
        0x101,
        (
            "#2P──失礼します。\x01",
            "クロスベル警察、特務支援課です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(34000, 4000)
    MoveCamera(315, 30, 0, 4000)
    OP_68(-1500, 250, 0, 4000)

    def lambda_648B():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_648B)
    Sleep(50)

    def lambda_649B():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_649B)
    Sleep(50)

    def lambda_64AB():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_64AB)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xF, 0)
    Sleep(500)

    def lambda_64CA():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64CA)

    def lambda_64E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_64E4)
    Sleep(100)

    def lambda_64F8():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64F8)

    def lambda_6512():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6512)
    Sleep(50)

    def lambda_6526():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6526)

    def lambda_6540():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6540)
    Sleep(80)

    def lambda_6554():
        OP_97(0xFE, 0x0, 0x0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6554)

    def lambda_656E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_656E)
    Sleep(2000)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    #C0318
    ChrTalk(
        0x8,
        (
            "#11Pやあ、君たち。\x01",
            "わざわざ済まなかったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xF,
        "#2Pよう、しばらくぶりだな！\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#00002F#6P皆さん、ご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        (
            "#00100F#6Pガンツさんの方は……\x01",
            "身体の調子の方はどうですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xF,
        (
            "#2Pああ、特に後遺症とかもなく\x01",
            "元気でやってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xF,
        (
            "#2P本当にありがとう。\x01",
            "改めて礼を言わせてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        "#00109F#6Pふふ、元気そうで何よりです。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#00001F#6Pそれで……\x01",
            "『旧鉱山』というところで\x01",
            "魔獣が発生したとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "#11Pああ、町の近くにある\x01",
            "数十年前に廃坑になった\x01",
            "大昔の坑道なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x9,
        (
            "#11Pまあ、立ち話もなんですし、\x01",
            "そちらに座ってくださいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x9,
        "#11P今、お茶を淹れますから。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_68(1260, 2200, 3060, 0)
    MoveCamera(322, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33750, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 2450, 950, 2780, 270)
    SetChrPos(0x102, 2450, 950, 3780, 270)
    SetChrPos(0x109, 1250, 950, 1500, 0)
    SetChrPos(0x105, 250, 950, 1500, 0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x1)
    SetChrPos(0xF, 800, 950, 5100, 180)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -800, 950, 2780, 90)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -800, 950, 3780, 90)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0329
    AnonymousTalk(
        0x101,
        (
            "#00005F──封鎖されていた\x01",
            "入口の扉が破壊されていた？\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(1260, 1950, 3070, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0330
    ChrTalk(
        0x8,
        (
            "#5Pああ、数十年前のものだが\x01",
            "とても頑丈な扉だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        (
            "#5Pそれが何者かに壊されているのを\x01",
            "町の人間が発見してね……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xF,
        (
            "#5P２日前には異常がなかったから\x01",
            "多分、壊されたのは昨日だと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xF,
        (
            "#5Pまったく、ふざけた事を\x01",
            "しでかす野郎がいたもんだぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#00003F#12P……気になりますね。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x109,
        (
            "#10108F#6Pそれで、中を覗いてみると\x01",
            "魔獣が徘徊していたと……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x105,
        (
            "#10305F#6Pでもまあ、昔の坑道跡とかなら\x01",
            "魔獣がいてもおかしくないよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        "#5Pいや、そうじゃないんだ。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#5Pおかしいと思ったのは\x01",
            "坑道そのもの#12R㈲　㈲　㈲　㈲　㈲　㈲#でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        "#00105F#12P坑道そのもの……？\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xF,
        (
            "#5Pなんつーか……\x01",
            "ぼうっと光ってるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xF,
        (
            "#5P壁そのものが、赤紫色の光に\x01",
            "染まっているというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x102,
        (
            "#00106F#12Pそ、それは……\x01",
            "確かに不気味ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#00008F#12P数十年前の坑道となると\x01",
            "導力灯もなかったはずだ。\x02\x03",

            "#00001F何が原因で光っているのか\x01",
            "確かに気になりますね……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "#5Pああ、町に実害は無いんだが\x01",
            "さすがにちょっと気になってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x9,
        (
            "#5Pお忙しいかとは思ったんだけど\x01",
            "連絡させていただいたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        "#00003F#12P事情は分かりました。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(200)

    #C0347
    ChrTalk(
        0x101,
        (
            "#00001F#12P扉が破壊されたという事は\x01",
            "事件性があると見ていいだろう。\x02\x03",

            "早速、様子を見てこよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x102,
        "#00101F#11Pええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x109,
        "#10101F#6P了解しました！\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x105,
        (
            "#10302F#6Pフフ……\x01",
            "興味深そうな事件だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x8,
        (
            "#5Pありがとう。\x01",
            "よろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(250)

    #C0352
    ChrTalk(
        0x8,
        (
            "#5Pガンツ、皆さんのために\x01",
            "道を開けておいてくれ。\x02",
        )
    )

    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xF,
        "#5Pああ、分かったぜ。\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xF,
        (
            "#5Pそんじゃ、先に行ってるから\x01",
            "準備が済んだら来てくれよな！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -630, 750, 5180, 270)
    Sleep(500)
    OP_95(0xF, -2150, 750, 4460, 2500, 0x0)

    def lambda_6F73():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD6FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6F73)
    OP_68(80, 1950, 2060, 3000)
    Sleep(600)
    SetChrSubChip(0x8, 0x2)
    Sleep(100)
    SetChrSubChip(0x9, 0x2)
    Sleep(200)
    SetChrSubChip(0x109, 0x1)
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(2500)
    Sound(103, 0, 100, 0)
    Sleep(600)
    Sound(104, 0, 100, 0)
    OP_68(1080, 1950, 3060, 1200)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x9, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(150)
    OP_6F(0x1)
    WaitChrThread(0xF, 1)
    SetChrFlags(0xF, 0x80)

    #C0355
    ChrTalk(
        0x101,
        (
            "#00002F#12P……よかった。\x01",
            "本当に元気そうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        "#5Pああ、君たちのおかげさ。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x8,
        (
            "#5Pただまあ、ギャンブル好きは\x01",
            "全然変わっていなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#5P相変わらず休みの日には\x01",
            "カジノでスって帰ってくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x102,
        "#00109F#12Pふふ、そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x101,
        (
            "#00004F#12Pまあ、身を持ち崩さなければ\x01",
            "問題はないと思いますけど……\x02\x03",

            "#00005Fそうだ、旧鉱山というのは\x01",
            "町を出てすぐの所なんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x9,
        (
            "#5Pええ、少し下ってから\x01",
            "北西に登った先にあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#5P何が原因か判らない。\x01",
            "くれぐれも気を付けてくれ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x8, -890, 950, 3320, 90)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -6530, 750, 60, 270)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, -250, 750, -750, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x12A, 0)
    OP_29(0xA2, 0x4, 0x2)
    OP_29(0xA2, 0x1, 0x0)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_23_6275 end

    def Function_24_72C4(): pass

    label("Function_24_72C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1850, 750, -1060, 0)
    MoveCamera(316, 22, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(37200, 0)
    SetChrPos(0x101, 700, 750, -3300, 0)
    SetChrPos(0x102, -500, 750, -3300, 0)
    SetChrPos(0x104, 700, 750, -4500, 0)
    SetChrPos(0x109, -500, 750, -4500, 0)
    SetChrPos(0x105, 100, 750, -5700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_0D()

    #C0363
    ChrTalk(
        0x8,
        (
            "#5Pふむ……\x01",
            "あの者たちは一体……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "まあ、深く考えなくても\x01",
            "いいんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xF,
        "おかげで儲けたんだし。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x8,
        (
            "#5Pいや、この間の犯人も\x01",
            "分かっていないんだ。\x01",
            "用心に越したことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#6P#00000Fえっと……\x01",
            "町長、ガンツさん、\x01",
            "こんにちは。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7488():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7488)
    Sleep(50)
    OP_93(0xF, 0xB4, 0x1F4)

    #C0368
    ChrTalk(
        0x8,
        "#11Pおお、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xF,
        (
            "悪い悪い、今ちょっと\x01",
            "話してたところでよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x102,
        (
            "#00105Fもしかして……\x01",
            "この間の旧鉱山の件ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x8,
        (
            "#11Pああいや、この間の件に関しては\x01",
            "あれから警備隊も何度か\x01",
            "巡回に来てくれたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        (
            "#11P爆薬を仕掛けた犯人や\x01",
            "坑道の異常の謎も\x01",
            "いまだに分からないままでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xF,
        (
            "#11P一応、壊れた扉の代わりに\x01",
            "新しく頑丈な扉を取り付けて、\x01",
            "しっかり封鎖しておいたんだけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x109,
        (
            "#6P#10104Fそれなら当面は、\x01",
            "間違って人が入り込む心配も\x01",
            "なさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "#11P……ただ、それとは別に\x01",
            "気になる事があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x8,
        (
            "#11P実はこの間、マインツに\x01",
            "風変わりな一団が現れたのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#11Pその者たちが大粒の七耀石の結晶を\x01",
            "高額で買い取っていったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x109,
        "#6P#10105F風変わりな一団……？\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#11Pなんというか、とにかく\x01",
            "独特な雰囲気があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "#11P大柄な赤毛の中年男性が\x01",
            "率いていたようなのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11Pおや、そういえばあの赤毛、\x01",
            "ランディ君の髪の色に\x01",
            "ソックリだったような。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0382
    ChrTalk(
        0x102,
        "#00105F（そ、それって……）\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#00005F#6P（《赤い星座》……！？）\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x104,
        (
            "#6P#00303F……そいつらは\x01",
            "七耀石を買い取った以外に\x01",
            "何かしてたんッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "#11Pいや、特別怪しい行動を\x01",
            "とったわけじゃないのだが……\x01",
            "貿易商のようにも見えなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x8,
        (
            "#11P旧鉱山の扉を破壊した者たちも\x01",
            "判明してない状況だから、\x01",
            "気にかけていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x109,
        (
            "#6P#10105F（ランディ先輩の話だと、\x01",
            "  爆薬を仕掛けた犯人はまさに\x01",
            "  彼らだったそうですが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x105,
        (
            "#6P#10303F（ま、明確な証拠もないし\x01",
            "  伏せておいたほうがいいだろうね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x102,
        (
            "#00108F（でも、猟兵団が\x01",
            "  七耀石の結晶なんて仕入れて\x01",
            "  どうするつもりなのかしら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x104,
        (
            "#6P#00301F（……ヤツらの《クリムゾン商会》は、\x01",
            "  ロクでもない商人どもに通じる\x01",
            "  多くのコネクションを持ってる。）\x02\x03",

            "#00303F（大粒の七耀石だったら、\x01",
            "  そいつらに闇ルートで捌かせれば\x01",
            "  いい小遣い稼ぎになるだろうな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        "#11P#00001F（な、なるほど……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0392
    ChrTalk(
        0x8,
        "#11P……ふむ、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        (
            "#11Pやはりアレは君たちに\x01",
            "預けておいたほうがよさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)

    #C0394
    ChrTalk(
        0x8,
        "#5Pガンツ、渡してやってくれ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    #C0395
    ChrTalk(
        0xF,
        "ああ、分かったぜ。\x02",
    )

    CloseMessageWindow()

    def lambda_7C91():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7C91)
    Sleep(50)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0396
    ChrTalk(
        0xF,
        "ほら、受け取ってくんな。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0397
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x323),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x323, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0398
    ChrTalk(
        0x101,
        "#00005F#6Pこれは旧鉱山の……？\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xF,
        "ああ、いわゆるスペアキーだな。\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x102,
        (
            "#00105Fえっと、いいんですか？\x01",
            "一応私たちは部外者なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x8,
        "ああ、君たちなら信用できるからね。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x8,
        (
            "今後、何か調べたいことがあったら\x01",
            "自由に入ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x8,
        (
            "念のため、奥との行き来もしやすいよう\x01",
            "ハシゴもかけなおしておいたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#6P#00000Fありがとうございます。\x01",
            "大切に使わせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0x8, 0xF, 0)
    TurnDirection(0xF, 0x8, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x14F, 2)
    OP_29(0xA3, 0x1, 0x3)
    SetChrPos(0x0, 0, 750, -3500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_72C4 end

    SaveToFile()

Try(main)
