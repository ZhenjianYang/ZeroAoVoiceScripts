from ScenarioHelper import *

def main():
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
        "萨米",                   # 1
        "金德尔",                 # 2
        "布里吉塔",               # 3
        "卢威克老人",             # 4
        "奥丽加夫人",             # 5
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
        "Function_6_3C2",          # 06, 6
        "Function_7_4E3",          # 07, 7
        "Function_8_579",          # 08, 8
        "Function_9_5E8",          # 09, 9
        "Function_10_6C8",         # 0A, 10
        "Function_11_706",         # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_389")

    #C0001
    ChrTalk(
        0xFE,
        (
            "各国首脑\x01",
            "好像正在彩虹剧团\x01",
            "观剧呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "嗯……他们想必可以\x01",
            "坐在最好的席位观赏吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "呜～好羡慕啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3BE")

    label("loc_389")


    #C0004
    ChrTalk(
        0xFE,
        (
            "我到最后也没能买到\x01",
            "新版演出的门票。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()

    label("loc_3BE")

    TalkEnd(0xFE)
    Return()

    # Function_5_309 end

    def Function_6_3C2(): pass

    label("Function_6_3C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485")

    #C0006
    ChrTalk(
        0xFE,
        (
            "每到夜晚，兰花塔\x01",
            "就会点亮美丽的灯光。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "以蓝色和白色为基调的高塔\x01",
            "在夜幕中闪耀着炫丽的光芒，\x01",
            "那美景绝对能让人震撼窒息。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "呵呵，如果以后有机会，\x01",
            "希望你们也去看看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4DF")

    label("loc_485")


    #C0009
    ChrTalk(
        0xFE,
        (
            "每到夜晚，兰花塔\x01",
            "就会点亮美丽的灯光。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "呵呵，如果以后有机会，\x01",
            "希望你们也去看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF")

    TalkEnd(0xFE)
    Return()

    # Function_6_3C2 end

    def Function_7_4E3(): pass

    label("Function_7_4E3")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        (
            "我老公啊，即使我什么都没问，\x01",
            "他也会兴致勃勃地\x01",
            "给我讲很多兰花塔方面的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "呵呵，看样子是白天参加揭幕式时的\x01",
            "兴奋劲还没有平静下来呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_4E3 end

    def Function_8_579(): pass

    label("Function_8_579")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58E")
    Call(0, 9)
    Jump("loc_5E4")

    label("loc_58E")


    #C0013
    ChrTalk(
        0xFE,
        (
            "我特意买了上等葡萄酒，\x01",
            "本想和老伴一起享用……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "哼，算了。\x01",
            "我一个人喝就是了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E4")

    TalkEnd(0xFE)
    Return()

    # Function_8_579 end

    def Function_9_5E8(): pass

    label("Function_9_5E8")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0015
    ChrTalk(
        0xB,
        (
            "啊啊，这种葡萄酒\x01",
            "果然美味呢。\x01",
            "真是买对了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "既然老婆子不喝，\x01",
            "那我就一个人享用好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        "……嗯，随你高兴吧。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xC,
        (
            "你不就是想自己喝，\x01",
            "才会花那么多钱买吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "……哼！\x01",
            "（咕嘟咕嘟）\x02",
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

    # Function_9_5E8 end

    def Function_10_6C8(): pass

    label("Function_10_6C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DD")
    Call(0, 9)
    Jump("loc_702")

    label("loc_6DD")


    #C0020
    ChrTalk(
        0xFE,
        (
            "……哼，我还不了解\x01",
            "那老头子吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_702")

    TalkEnd(0xFE)
    Return()

    # Function_10_6C8 end

    def Function_11_706(): pass

    label("Function_11_706")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_11_706 end

    SaveToFile()

Try(main)
