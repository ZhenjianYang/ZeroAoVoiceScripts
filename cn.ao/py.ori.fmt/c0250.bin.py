from ScenarioHelper import *

def main():
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
        "雷缇",                   # 1
        "潘莎",                   # 2
        "菲伊",                   # 3
        "寇肯",                   # 4
        "隆",                     # 5
        "琪露露",                 # 6
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
        "Function_5_1AEB",         # 05, 5
        "Function_6_1E50",         # 06, 6
        "Function_7_273C",         # 07, 7
        "Function_8_288C",         # 08, 8
        "Function_9_2FCE",         # 09, 9
        "Function_10_3B02",        # 0A, 10
        "Function_11_3C12",        # 0B, 11
        "Function_12_3CF6",        # 0C, 12
        "Function_13_3DE6",        # 0D, 13
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_735")

    #C0001
    ChrTalk(
        0xFE,
        (
            "我刚才和塞茜尔联系上了，\x01",
            "总算是松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "不过，听她的语气，\x01",
            "似乎心事重重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "我想那应该不是因为\x01",
            "医院忽然忙碌起来才这样的……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "如果你们有时间，\x01",
            "就去医院看看她吧。\x01",
            "她大概有不少话想说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_790")

    label("loc_735")


    #C0005
    ChrTalk(
        0xFE,
        (
            "塞茜尔似乎\x01",
            "心事重重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "如果你们有时间，\x01",
            "就去医院看看她吧。\x01",
            "她大概有不少话想说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790")

    Jump("loc_1AE7")

    label("loc_795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A05")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0007
    ChrTalk(
        0xFE,
        (
            "啊，这不是罗伊德吗……！\x01",
            "你这段时间去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "对了，见到塞茜尔了吗？\x01",
            "我一直都见不到她的面……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00012F阿、阿姨，您先冷静些。\x01",
            "……久别重逢，我实在是很开心。\x02\x03",

            "#00000F塞茜尔姐姐还在医院，\x01",
            "她看上去很有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "是吗，太好了……\x01",
            "罗伊德也回来了，\x01",
            "阿姨真是松了口气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "外面很危险呢，\x01",
            "你们就藏在阿姨这里别出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00004F不、不了，感谢您的好意……\x01",
            "但我们无论如何\x01",
            "也必须要去某个地方。\x02\x03",

            "#00000F阿姨，您就在\x01",
            "这里耐心等着吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "是吗……我明白了。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "不过，路上一定要小心哦！\x01",
            "如果你们有个三长两短，\x01",
            "我、我可就……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00000F嗯，我们会小心的。\x01",
            "……再见。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 7)
    Jump("loc_A60")

    label("loc_A05")


    #C0016
    ChrTalk(
        0xFE,
        (
            "太好了……\x01",
            "罗伊德也回来了，\x01",
            "阿姨真是松了口气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "空之女神啊，\x01",
            "感谢您保佑他们……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A60")

    Jump("loc_1AE7")

    label("loc_A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A73")
    Jump("loc_1AE7")

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B84")

    #C0018
    ChrTalk(
        0xFE,
        (
            "我昨天联络了\x01",
            "医院那边……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "塞茜尔他们\x01",
            "好像相当忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00003F……那也难怪呢。\x02\x03",

            "#00008F受那起袭击事件的影响，\x01",
            "医院里的伤员似乎\x01",
            "已经人满为患了……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "唉，真让人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "塞茜尔的性格太好强，\x01",
            "总爱勉强自己……\x01",
            "希望她不要累坏身体。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BD8")

    label("loc_B84")


    #C0023
    ChrTalk(
        0xFE,
        (
            "受那起袭击事件的影响，\x01",
            "医院现在好像相当繁忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "塞茜尔有没有\x01",
            "好好休息呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD8")

    Jump("loc_1AE7")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C5A")

    #C0025
    ChrTalk(
        0xFE,
        (
            "玛因兹竟然被占领了……\x01",
            "那里的人们肯定会\x01",
            "非常恐慌吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "听说警备队也陷入苦战了，\x01",
            "结果究竟会如何呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE7")

    label("loc_C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1C")

    #C0027
    ChrTalk(
        0xFE,
        (
            "啊，对了，\x01",
            "明天就是彩虹剧团\x01",
            "新版舞剧的公演日呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "听说门票在转瞬之间\x01",
            "就销售一空……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "呵呵，不知不觉间，伊莉娅那孩子\x01",
            "已经变得这么出色了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        "#10105F伊、伊莉娅『那孩子』……？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00005F说起来……\x01",
            "伊莉娅小姐是塞茜尔姐姐的\x01",
            "童年玩伴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "嗯，伊莉娅当时就是个很引人注目的孩子。\x01",
            "她和塞茜尔意外地投缘，\x01",
            "两人总是在一起玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "伊莉娅还曾勇敢地教训过\x01",
            "欺负塞茜尔的男孩，\x01",
            "把对方都揍哭了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，真是符合伊莉娅小姐\x01",
            "风格的童年往事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00306F不过……总觉得\x01",
            "被揍的小鬼很可怜……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，小孩子往往表里不一，\x01",
            "正是因为喜欢对方，才故意去欺负。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#00203F算啦，能被伊莉娅小姐揍，\x01",
            "从某种意义上说，\x01",
            "也算是很珍贵的回忆吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00012F这、这个嘛……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 3)

    label("loc_F1C")


    #C0039
    ChrTalk(
        0xFE,
        (
            "呵呵，当年那个小女孩，\x01",
            "如今已经成长为引领着\x01",
            "整个彩虹剧团的超级明星……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "连自幼看着她长大的阿姨我\x01",
            "都觉得面上有光呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE7")

    label("loc_F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1008")

    #C0041
    ChrTalk(
        0xFE,
        (
            "哎，刚才那不是……\x01",
            "急救车的警笛声吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "好像开过去很多辆……\x01",
            "莫非发生交通事故了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE7")

    label("loc_1008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1016")
    Jump("loc_1AE7")

    label("loc_1016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1118")

    #C0043
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市独立为正式国家……\x01",
            "听说要举办以此为主题\x01",
            "的居民投票活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "这真是个相当难做决定的问题啊。\x01",
            "我必须先和老公好好商量一下，\x01",
            "然后再决定该投什么票。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "究竟哪一方才是正确的呢……\x01",
            "想得到这个问题的答案可没有那么简单。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_119B")

    label("loc_1118")


    #C0046
    ChrTalk(
        0xFE,
        (
            "我准备先和老公\x01",
            "好好商量一下，\x01",
            "然后再决定到时该投什么票。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "究竟哪一方才是正确的呢……\x01",
            "想得到这个问题的答案可没有那么简单。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_119B")

    Jump("loc_1AE7")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1399")

    #C0048
    ChrTalk(
        0xFE,
        (
            "啊，那不是\x01",
            "小缇欧吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        "#00202F久疏问候了。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "呵呵，你好像很有精神啊，这就好。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "如果以后有时间，\x01",
            "大家还要一起来我家吃饭哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        (
            "#00109F阿姨做的料理吗……\x01",
            "呵呵，真期待。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00309F嗯，确实非常美味，\x01",
            "简直可以品味出母亲的味道呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x105,
        "#10305F哎，是吗？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x109,
        (
            "#10109F那可真不错啊……\x01",
            "我可得好好期待一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "自然也会招待\x01",
            "你们二位新成员的。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "呵呵，到时候\x01",
            "我一定会拿出全部本领，\x01",
            "给你们做最棒的料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00000F谢谢了，阿姨。\x01",
            "等我们有空时，\x01",
            "还会再来打扰您的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 1)
    Jump("loc_13F1")

    label("loc_1399")


    #C0059
    ChrTalk(
        0xFE,
        (
            "支援科的成员\x01",
            "终于聚齐了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "呵呵，如果以后有时间，\x01",
            "大家还要一起来我家吃饭哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F1")

    Jump("loc_1AE7")

    label("loc_13F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1452")

    #C0061
    ChrTalk(
        0xFE,
        (
            "啊，不知不觉，\x01",
            "天色已经全黑下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "我老公也快回来了，\x01",
            "得赶快做饭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE7")

    label("loc_1452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1610")

    #C0063
    ChrTalk(
        0x101,
        (
            "#00000F阿姨，我们昨天\x01",
            "去见过塞茜尔姐姐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "啊，是吗？\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "呵呵，那塞茜尔\x01",
            "一定很开心吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00012F哈哈，是啊……\x01",
            "她好像很有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，真是一位比想象中\x01",
            "更加优秀的女性，让我大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        (
            "#10100F是啊，她非常\x01",
            "有包容力……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#00309F对吧对吧～？那可是\x01",
            "直接击中我红心的\x01",
            "大姐姐呀！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00106F我、我说你啊……\x01",
            "在塞茜尔小姐的母亲面前，\x01",
            "这种发言是不是有些……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00006F就、就是说啊，真是的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 0)

    label("loc_1610")


    #C0072
    ChrTalk(
        0xFE,
        (
            "呵呵，塞茜尔\x01",
            "好像很受欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "如果可以，希望大家今后\x01",
            "也和她好好相处吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE7")

    label("loc_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_178F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1754")

    #C0074
    ChrTalk(
        0xFE,
        (
            "我今天出去买东西，\x01",
            "看到外面有\x01",
            "很多警察在巡逻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "你们警察现在肯定\x01",
            "很忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00000F通商会议明天就要召开了，\x01",
            "我们正在处理支援请求的同时\x01",
            "到处巡视。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "虽然很辛苦，\x01",
            "但大家一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_178A")

    label("loc_1754")


    #C0078
    ChrTalk(
        0xFE,
        (
            "虽然你们警察\x01",
            "的工作很辛苦，\x01",
            "但大家一定要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178A")

    Jump("loc_1AE7")

    label("loc_178F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_18E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AA")
    Call(0, 5)
    Jump("loc_18DD")

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186D")

    #C0079
    ChrTalk(
        0xFE,
        (
            "我老公\x01",
            "在图书馆\x01",
            "负责管理图书……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "他和一位记者\x01",
            "有着多年的深交。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "那位记者似乎相当博学，\x01",
            "每次见到他的时候，\x01",
            "老公都会和人家埋头畅谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "呵呵，简直像个小孩子一样。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18DD")

    label("loc_186D")


    #C0083
    ChrTalk(
        0xFE,
        (
            "我老公\x01",
            "和一位记者\x01",
            "有着多年的深交。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "那位记者似乎相当博学，\x01",
            "每次见到他的时候，\x01",
            "老公都会和人家埋头畅谈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DD")

    Jump("loc_1AE7")

    label("loc_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1AE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FD")
    Call(0, 5)
    Jump("loc_1AE7")

    label("loc_18FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7D")

    #C0085
    ChrTalk(
        0xFE,
        (
            "对了，罗伊德，\x01",
            "你已经和塞茜尔联系过了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00000F嗯，用导力通讯联络过了。\x01",
            "等以后有机会，\x01",
            "还会过去见个面的。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "呵呵，你这次回来以后，\x01",
            "好像比以前更加强壮了，\x01",
            "塞茜尔说不定也会大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00012F那、那个，是吗……\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#00111F（总觉得他在害羞呢。\x01",
            "  ……心里到底在想象什么？）\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x105,
        (
            "#10309F（呵呵，我对那位塞茜尔小姐\x01",
            "  真是越来越有兴趣了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AE7")

    label("loc_1A7D")


    #C0091
    ChrTalk(
        0xFE,
        (
            "罗伊德，你这次回来以后，\x01",
            "好像比以前更加强壮了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "呵呵，塞茜尔要是看见你，\x01",
            "说不定也会大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE7")

    TalkEnd(0xFE)
    Return()

    # Function_4_64A end

    def Function_5_1AEB(): pass

    label("Function_5_1AEB")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0xFE,
        (
            "啊，哎呀呀……\x01",
            "这不是罗伊德吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#00000F雷缇阿姨，我回来啦。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "呵呵，你好像很有精神呢，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "支援科的同伴也在一起，\x01",
            "看来一科的研修\x01",
            "终于结束了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00000F嗯，前几天刚刚结束。\x01",
            "不好意思，这么晚才来\x01",
            "见您……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        "#10305F这位夫人是……？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00000F哦，是从我小时候开始\x01",
            "就一直照顾我的阿姨。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#00100F这位是塞茜尔小姐的母亲，\x01",
            "平时也经常关照我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        (
            "#10100F说起塞茜尔小姐，\x01",
            "就是以前在医院见过的那位……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00000F哦，说起来，诺艾尔曾\x01",
            "见过塞茜尔姐姐一面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10303F唔，好像只有我\x01",
            "被大家排除在外啊。\x02\x03",

            "#10302F听起来，那位塞茜尔小姐\x01",
            "与罗伊德之间的关系似乎非同寻常……\x01",
            "一定要好好给我讲讲哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#00012F才、才没有什么\x01",
            "非同寻常的关系啦。\x02\x03",

            "#00000F好啦，反正以后肯定有\x01",
            "见到塞茜尔姐姐的机会，\x01",
            "到时候再介绍给你。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "呵呵，你们支援科\x01",
            "还是这么有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "罗伊德，如果今后\x01",
            "遇到了什么困难，\x01",
            "随时都可以来找阿姨哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 5)
    Return()

    # Function_5_1AEB end

    def Function_6_1E50(): pass

    label("Function_6_1E50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFB")

    #C0107
    ChrTalk(
        0xFE,
        (
            "在铁路停止运营之后，\x01",
            "爸爸有段时间非常沮丧……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "但他很快就重新打起了精神，\x01",
            "开始到各处帮忙援助。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "真是的，机械痴\x01",
            "可真是无可救药。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F45")

    label("loc_1EFB")


    #C0110
    ChrTalk(
        0xFE,
        (
            "真是的，机械痴\x01",
            "可真是无可救药。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "……不过，这也\x01",
            "算是爸爸的优点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F45")

    Jump("loc_2738")

    label("loc_1F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1FA5")

    #C0112
    ChrTalk(
        0xFE,
        "发、发生什么事了……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐和总统\x01",
            "肯定能想办法解决吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_1FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2009")

    #C0114
    ChrTalk(
        0xFE,
        (
            "爸爸今天一大早就去了一趟车站，\x01",
            "好像非常忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "……希望他在家\x01",
            "好好休息一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_2009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2090")

    #C0116
    ChrTalk(
        0xFE,
        (
            "听说在不久前的那场事件中，\x01",
            "彩虹剧团的伊莉娅小姐\x01",
            "身受重伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "难道以后再也看不到那种精彩的表演了吗？\x01",
            "不要啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_2090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_217E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2117")

    #C0118
    ChrTalk(
        0xFE,
        (
            "今天是彩虹剧团\x01",
            "新版舞剧的公演日呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "但爸爸却好像一副\x01",
            "忧心忡忡的表情。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "难道发生什么事了吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2179")

    label("loc_2117")


    #C0121
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的新版舞剧就要公演，\x01",
            "这是个值得庆贺的日子，\x01",
            "但爸爸却……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        "难道发生什么事了吗……\x02",
    )

    CloseMessageWindow()

    label("loc_2179")

    Jump("loc_2738")

    label("loc_217E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21ED")

    #C0123
    ChrTalk(
        0xFE,
        (
            "因为昨天发生了脱轨事故，\x01",
            "爸爸工作得非常\x01",
            "忙碌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "……今天还是安静些，\x01",
            "让他好好休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2260")

    #C0125
    ChrTalk(
        0xFE,
        (
            "爸爸听说发生了\x01",
            "列车事故之后，\x01",
            "立刻就慌慌张张地冲出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "他说要去车站看看，\x01",
            "不会有事吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_2260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_22B7")

    #C0127
    ChrTalk(
        0xFE,
        (
            "爸爸今天\x01",
            "想去看看\x01",
            "姐姐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "难得的假日，\x01",
            "在家里休息一下多好嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_22B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2320")

    #C0129
    ChrTalk(
        0xFE,
        (
            "爸爸出差\x01",
            "回来之后，\x01",
            "马上就扑到床上睡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "真是的，连衣服都不换，\x01",
            "把床单都弄脏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_2320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_23FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2386")

    #C0131
    ChrTalk(
        0xFE,
        (
            "我看了刊登着玛丽亚贝尔小姐\x01",
            "照片的时装杂志。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "啊啊～好憧憬她啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23F7")

    label("loc_2386")


    #C0133
    ChrTalk(
        0xFE,
        (
            "呼，为什么玛丽亚贝尔小姐\x01",
            "如此美丽，头脑又那么聪明呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "所谓的才色兼备，\x01",
            "就是指她这样的人吧？\x01",
            "真棒啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F7")

    Jump("loc_2738")

    label("loc_23FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_24DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2492")

    #C0135
    ChrTalk(
        0xFE,
        (
            "……啊！\x01",
            "我放时装杂志的书架里\x01",
            "混杂着铁路方面的书……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "这一定是爸爸干的。\x01",
            "同样的伎俩，\x01",
            "他到底还想用多少次啊？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_24D9")

    label("loc_2492")


    #C0137
    ChrTalk(
        0xFE,
        (
            "爸爸总是做这种事情，\x01",
            "希望我能喜欢上铁路。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "真是太纠缠不休了。\x02",
    )

    CloseMessageWindow()

    label("loc_24D9")

    Jump("loc_2738")

    label("loc_24DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25EE")
    TurnDirection(0xFE, 0x0, 0)

    #C0139
    ChrTalk(
        0xFE,
        (
            "大家全都像小孩子一样呢。\x01",
            "只不过是看到了一座巨大的建筑物，\x01",
            "就大惊小怪地议论不停。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "……算、算了，\x01",
            "那座建筑确实挺惊人的……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "不过比起建筑物，\x01",
            "还是看时装杂志\x01",
            "更加开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#00006F（这两种东西\x01",
            "  好像并没有可比性呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_264E")

    label("loc_25EE")


    #C0143
    ChrTalk(
        0xFE,
        (
            "（翻书……）\x01",
            "哇，这张照片上的大姐姐\x01",
            "好漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "果然还是这种\x01",
            "腰部纤细的身材\x01",
            "更好看……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264E")

    Jump("loc_2738")

    label("loc_2653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_26B0")

    #C0145
    ChrTalk(
        0xFE,
        (
            "爸爸又要出差\x01",
            "一个月左右，\x01",
            "把我留在了家里。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "看来铁路技师\x01",
            "确实很忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_272F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CB")
    Call(0, 7)
    Jump("loc_272A")

    label("loc_26CB")


    #C0147
    ChrTalk(
        0xFE,
        (
            "我只想成为\x01",
            "玛丽亚贝尔小姐那种\x01",
            "又漂亮又聪明的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "并不想按照爸爸的期望，\x01",
            "当一个技师。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272A")

    Jump("loc_2738")

    label("loc_272F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2738")

    label("loc_2738")

    TalkEnd(0xFE)
    Return()

    # Function_6_1E50 end

    def Function_7_273C(): pass

    label("Function_7_273C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0149
    ChrTalk(
        0x9,
        (
            "听说玛丽亚贝尔小姐\x01",
            "统率着ＩＢＣ的技术部，\x01",
            "很精通导力技术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "嗯……\x01",
            "不然我也学习一下\x01",
            "导力技术方面的知识吧。\x02",
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
            "潘、潘莎～！\x01",
            "你总算也开始对\x01",
            "技师的道路感兴趣了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "好，现在就确定目标吧。\x01",
            "要不要成为像爸爸一样的\x01",
            "铁路技师呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "……不要。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        "#4S（打击！）#3S\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_273C end

    def Function_8_288C(): pass

    label("Function_8_288C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2991")

    #C0155
    ChrTalk(
        0xFE,
        (
            "铁道列车如今已经停止运营，\x01",
            "我这些铁路技师方面的技术\x01",
            "或许已经起不到什么作用了……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "但巴士和导力车也是\x01",
            "依靠导力器而运行的交通工具，\x01",
            "我应该能在维修工作中贡献一些力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "好，这就去市民会馆咨询一下，\x01",
            "看看有没有什么工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A16")

    label("loc_2991")


    #C0158
    ChrTalk(
        0xFE,
        (
            "我这些铁路技师方面的技术\x01",
            "应该也能在维修巴士或导力车\x01",
            "的工作中派上用场。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "好，这就去市民会馆咨询一下，\x01",
            "看看有没有什么工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A16")

    Jump("loc_2FCA")

    label("loc_2A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A7E")

    #C0160
    ChrTalk(
        0xFE,
        (
            "潘莎，千万不要外出哦，\x01",
            "和爸爸一起乖乖待在家里。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "你姐姐也一定不会有事的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FCA")

    label("loc_2A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2B")

    #C0162
    ChrTalk(
        0xFE,
        (
            "我今天早上去\x01",
            "克洛斯贝尔车站帮忙了……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "准备返乡的外国人\x01",
            "把那里围得水泄不通，\x01",
            "场面相当混乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "稍微休息一下之后，\x01",
            "我还得赶快回去帮忙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B8B")

    label("loc_2B2B")


    #C0165
    ChrTalk(
        0xFE,
        (
            "一群外国人把车站围得水泄不通，\x01",
            "场面相当混乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "稍微休息一下之后，\x01",
            "我还得赶快回去帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8B")

    Jump("loc_2FCA")

    label("loc_2B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B9E")
    Jump("loc_2FCA")

    label("loc_2B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2BFE")

    #C0167
    ChrTalk(
        0xFE,
        (
            "怎么会有这种事，\x01",
            "玛因兹竟然被……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "武装集团的那些家伙\x01",
            "究竟有何目的……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCA")

    label("loc_2BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C1C")

    #C0169
    ChrTalk(
        0xFE,
        "嗯、嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FCA")

    label("loc_2C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2C2A")
    Jump("loc_2FCA")

    label("loc_2C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEC")
    OP_4B(0x9, 0xFF)

    #C0170
    ChrTalk(
        0xFE,
        (
            "难得有时间，不然就去\x01",
            "看看温蒂工作时的样子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "潘莎你也看看姐姐是怎么工作的，\x01",
            "学一学怎样当个好技师吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "真是的，\x01",
            "我都说过不想\x01",
            "当什么技师了！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D5C")

    label("loc_2CEC")


    #C0173
    ChrTalk(
        0xFE,
        (
            "潘莎你也看看姐姐是怎么工作的，\x01",
            "学一学怎样当个好技师吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "将来你想当技师时，\x01",
            "这些知识一定会派上用场的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5C")

    Jump("loc_2FCA")

    label("loc_2D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2DC8")

    #C0175
    ChrTalk(
        0xFE,
        (
            "嗯嗯嗯……\x01",
            "啊啊，我家的床\x01",
            "果然是最棒的……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "就让我像烂泥一样\x01",
            "趴在这里不动吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCA")

    label("loc_2DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DD6")
    Jump("loc_2FCA")

    label("loc_2DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2DE4")
    Jump("loc_2FCA")

    label("loc_2DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2DF2")
    Jump("loc_2FCA")

    label("loc_2DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E00")
    Jump("loc_2FCA")

    label("loc_2E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E1B")
    Call(0, 7)
    Jump("loc_2E76")

    label("loc_2E1B")


    #C0177
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "算啦，也不用着急。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "她毕竟继承了我的血脉，\x01",
            "将来一定会成为\x01",
            "一名优秀的技师。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E76")

    Jump("loc_2FCA")

    label("loc_2E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2FCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7B")

    #C0179
    ChrTalk(
        0x101,
        (
            "#00005F啊，是温蒂\x01",
            "的父亲……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x109,
        "#10100F看上去似乎非常疲惫呢。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "嗯嗯嗯……\x01",
            "难得刚刚出差归来，但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "潘莎，不好意思，\x01",
            "你就一个人吃饭吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#00004F……好像根本没醒嘛。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        "#00100F呵呵，还是不要打扰他休息啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FCA")

    label("loc_2F7B")


    #C0185
    ChrTalk(
        0xFE,
        (
            "……哎，潘莎\x01",
            "去哪里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "哦，对了，\x01",
            "主日学校今天有课……\x01",
            "嗯嗯嗯……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCA")

    TalkEnd(0xFE)
    Return()

    # Function_8_288C end

    def Function_9_2FCE(): pass

    label("Function_9_2FCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_312C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A2")

    #C0187
    ChrTalk(
        0xFE,
        (
            "隆那小子，好像正和几个小伙伴\x01",
            "一起在外边巡视，帮助附近的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "今天我本想教他一些\x01",
            "经商方面的知识呢。\x01",
            "唔唔，又被他巧妙地逃掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "……算了，他大概是很想\x01",
            "为大家做点什么吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3127")

    label("loc_30A2")


    #C0190
    ChrTalk(
        0xFE,
        (
            "隆也就罢了……\x01",
            "琪露露还是一样任性，又要出去旅行，\x01",
            "现在已经去了唐古拉姆门那边。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "……真是的，我这两个孩子\x01",
            "都在家里待不住啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3127")

    Jump("loc_3AFE")

    label("loc_312C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_31A0")

    #C0192
    ChrTalk(
        0xFE,
        (
            "两个孩子都在家里，\x01",
            "总算可以暂时安心了……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "但还是很担心外面的情况。\x01",
            "现在究竟变成什么样了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFE")

    label("loc_31A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3252")

    #C0194
    ChrTalk(
        0xFE,
        (
            "看样子，克洛斯贝尔\x01",
            "将要发生什么大事了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "……不管怎么说，琪露露能平安回来，\x01",
            "我也算松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "必须要全家团聚在一起啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32BE")

    label("loc_3252")


    #C0197
    ChrTalk(
        0xFE,
        (
            "看样子，克洛斯贝尔\x01",
            "将要发生什么大事了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "一定要预先做好心理准备，\x01",
            "以应对接下来的任何突发状况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BE")

    Jump("loc_3AFE")

    label("loc_32C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_333C")

    #C0199
    ChrTalk(
        0xFE,
        (
            "虽然那起事件很严重……\x01",
            "但ＩＢＣ很快就\x01",
            "恢复了营业，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "对商人来说，\x01",
            "银行可是最重要的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFE")

    label("loc_333C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3393")

    #C0201
    ChrTalk(
        0xFE,
        (
            "真没想到，竟然会发生\x01",
            "这样的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        "在外旅行的琪露露不要紧吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AFE")

    label("loc_3393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_344D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340E")

    #C0203
    ChrTalk(
        0xFE,
        (
            "我以前也是个\x01",
            "在下雨天会光脚乱跑\x01",
            "的顽皮小鬼。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "从某种意义上说，\x01",
            "隆和小时候的我\x01",
            "很像呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3448")

    label("loc_340E")


    #C0205
    ChrTalk(
        0xFE,
        (
            "隆和小时候的我\x01",
            "很像呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "所以整天都得\x01",
            "让人操心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3448")

    Jump("loc_3AFE")

    label("loc_344D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3491")

    #C0207
    ChrTalk(
        0xFE,
        (
            "怎么回事？我刚才听到了\x01",
            "一阵非常刺耳的\x01",
            "警笛声……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFE")

    label("loc_3491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_35B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3545")

    #C0208
    ChrTalk(
        0xFE,
        (
            "我女儿琪露露终于\x01",
            "结束旅行，回到家里来了。\x01",
            "她现在和朋友出去玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "隆和琪露露\x01",
            "都和朋友相处得\x01",
            "很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "嘿，这可真是一件\x01",
            "值得高兴的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35B4")

    label("loc_3545")


    #C0211
    ChrTalk(
        0xFE,
        (
            "琪露露那孩子很少待在家里，\x01",
            "真亏卡缇莉娜还能\x01",
            "继续跟她交好下去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "嘿，这可真是一件\x01",
            "值得高兴的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B4")

    Jump("loc_3AFE")

    label("loc_35B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_362B")

    #C0213
    ChrTalk(
        0xFE,
        (
            "我今天本想\x01",
            "让隆那小子\x01",
            "帮忙工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "但稍不留神，\x01",
            "他就跑出去了。\x01",
            "真是的，这小子跑得好快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFE")

    label("loc_362B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3698")

    #C0215
    ChrTalk(
        0xFE,
        (
            "隆今天也和\x01",
            "他的朋友们\x01",
            "一起去看兰花塔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "真是的，昨天看了那么半天，\x01",
            "难道还没看够吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFE")

    label("loc_3698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_376F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370E")

    #C0217
    ChrTalk(
        0xFE,
        (
            "我希望隆有朝一日\x01",
            "能继承我的批发生意……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "但这小子整天\x01",
            "就知道玩，\x01",
            "真是让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_376A")

    label("loc_370E")


    #C0219
    ChrTalk(
        0xFE,
        (
            "隆那小子，在主日学校\x01",
            "的考试成绩也是一塌糊涂。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "真希望他能认真学习，\x01",
            "不要只想着玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376A")

    Jump("loc_3AFE")

    label("loc_376F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3893")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3836")

    #C0221
    ChrTalk(
        0xFE,
        (
            "我从大约三年前开始，\x01",
            "在克洛斯贝尔做起了批发生意。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "受揭幕式的影响，\x01",
            "百货店这次向我订了\x01",
            "比平时更多的货。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔这座城市充满活力，\x01",
            "真是个适合经商的好地方。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_388E")

    label("loc_3836")


    #C0224
    ChrTalk(
        0xFE,
        (
            "受揭幕式的影响，\x01",
            "百货店这次向我订了\x01",
            "比平时更多的货。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "呵呵呵，生意真是兴隆啊。\x02",
    )

    CloseMessageWindow()

    label("loc_388E")

    Jump("loc_3AFE")

    label("loc_3893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391D")

    #C0226
    ChrTalk(
        0xFE,
        (
            "隆那小子，\x01",
            "最近总是约塔利兹先生\x01",
            "家的小桃一起玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "他没教人家玩一些危险的游戏吧……\x01",
            "实在是有些担心……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_398E")

    label("loc_391D")


    #C0228
    ChrTalk(
        0xFE,
        (
            "如果隆教小桃玩了\x01",
            "危险的游戏，\x01",
            "我可就太对不起人家的父母了。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "必须要好好提醒隆那小子，\x01",
            "让他多加注意才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_398E")

    Jump("loc_3AFE")

    label("loc_3993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A40")

    #C0230
    ChrTalk(
        0xFE,
        (
            "琪露露很快就要\x01",
            "再次出门旅行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "趁着全家人聚在一起，\x01",
            "我要让他们尝尝\x01",
            "我最拿手的炒饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "我以前住在共和国，\x01",
            "所以很了解那些东方菜式。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AA4")

    label("loc_3A40")


    #C0233
    ChrTalk(
        0xFE,
        (
            "我以前住在共和国，\x01",
            "所以很了解那些东方菜式。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "不过，我的拿手菜式\x01",
            "也只有炒饭之类的简单料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA4")

    Jump("loc_3AFE")

    label("loc_3AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3AFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC4")
    Call(0, 10)
    Jump("loc_3AFE")

    label("loc_3AC4")


    #C0235
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "无论经历了什么危险，\x01",
            "也丝毫不接受教训啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AFE")

    TalkEnd(0xFE)
    Return()

    # Function_9_2FCE end

    def Function_10_3B02(): pass

    label("Function_10_3B02")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0236
    ChrTalk(
        0xB,
        (
            "哦，琪露露，你回来了啊，\x01",
            "这次的旅行可真够久的。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xB,
        (
            "记得你当时说了些\x01",
            "非常莽撞的话，好像是要\x01",
            "征服玛因兹连峰吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xD,
        (
            "嗯……\x01",
            "但在途中遇到了些许险情。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xD,
        (
            "唉，看来我的实力还是不够，\x01",
            "下次有机会时再挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        "你真是不接受教训啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_3B02 end

    def Function_11_3C12(): pass

    label("Function_11_3C12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C23")
    Jump("loc_3CF2")

    label("loc_3C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C99")

    #C0241
    ChrTalk(
        0xFE,
        (
            "戒严令实在是太过无聊了，\x01",
            "我正想偷偷摸摸地溜出去玩，\x01",
            "没想到却发生了这种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "呼，真是搞不懂啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF2")

    label("loc_3C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB4")
    Call(0, 12)
    Jump("loc_3CF2")

    label("loc_3CB4")


    #C0243
    ChrTalk(
        0xFE,
        (
            "我姐姐真是个\x01",
            "怪人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "她总想跑到\x01",
            "一些古怪的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CF2")

    TalkEnd(0xFE)
    Return()

    # Function_11_3C12 end

    def Function_12_3CF6(): pass

    label("Function_12_3CF6")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0245
    ChrTalk(
        0xC,
        (
            "对了，姐姐，\x01",
            "你下次要去哪里旅行了？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xD,
        (
            "嗯……\x01",
            "暂时会在克洛斯贝尔\x01",
            "市内转转吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xD,
        (
            "市内也有很多\x01",
            "没去过的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "嘿，姐姐果然\x01",
            "是个怪人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xC,
        (
            "总想去各种\x01",
            "奇怪的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xD,
        "……我可不想被你这样说啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_3CF6 end

    def Function_13_3DE6(): pass

    label("Function_13_3DE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3DF7")
    Jump("loc_40DB")

    label("loc_3DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3EE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAE")
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0251
    ChrTalk(
        0xFE,
        (
            "现在不能离开市区，\x01",
            "我本来就很烦躁了，还发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "……哼，睡觉。\x01",
            "骚乱平息下来以后再叫醒我。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        "现、现在是睡觉的时候吗～！？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 5)
    Jump("loc_3EDF")

    label("loc_3EAE")


    #C0254
    ChrTalk(
        0xFE,
        (
            "骚乱平息下来以后再叫醒我。\x01",
            "……我要睡觉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EDF")

    Jump("loc_40DB")

    label("loc_3EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5F")

    #C0255
    ChrTalk(
        0xFE,
        (
            "最近这段时间，我感觉\x01",
            "整个克洛斯贝尔都很异常。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "看样子，暂时还是不要\x01",
            "外出旅行为好吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3FB3")

    label("loc_3F5F")


    #C0257
    ChrTalk(
        0xFE,
        (
            "看样子，暂时还是不要\x01",
            "外出旅行为好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "……也没别的事可做，\x01",
            "还是睡觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB3")

    Jump("loc_40DB")

    label("loc_3FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3FC6")
    Jump("loc_40DB")

    label("loc_3FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4072")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE1")
    Call(0, 12)
    Jump("loc_406D")

    label("loc_3FE1")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0259
    ChrTalk(
        0xFE,
        (
            "……你以前擅自钻进地下空间，\x01",
            "最后还哭着被人救出来，\x01",
            "又有什么资格说我。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0260
    ChrTalk(
        0xC,
        "我……我才没哭呢！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)

    label("loc_406D")

    Jump("loc_40DB")

    label("loc_4072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_40DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408D")
    Call(0, 10)
    Jump("loc_40DB")

    label("loc_408D")


    #C0261
    ChrTalk(
        0xFE,
        (
            "我现在还没有\x01",
            "征服玛因兹连峰的实力……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "但下次挑战时\x01",
            "一定要取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DB")

    TalkEnd(0xFE)
    Return()

    # Function_13_3DE6 end

    SaveToFile()

Try(main)
