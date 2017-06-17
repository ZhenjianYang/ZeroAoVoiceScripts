from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "e0111.bin",                # FileName
        "e0111",                    # MapName
        "e0111",                    # Location
        0x0001,                     # MapIndex
        "ed7516",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0111",                  # 0
        "蔡特",                   # 1
        "迪塔总裁",               # 2
        "玛丽亚贝尔",             # 3
        "赛尔盖科长",             # 4
        "SE控制",                 # 5
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1C4",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_2A0",          # 02, 2
        "Function_3_2A1",          # 03, 3
        "Function_4_CDE",          # 04, 4
        "Function_5_D03",          # 05, 5
        "Function_6_D28",          # 06, 6
        "Function_7_D59",          # 07, 7
        "Function_8_1C48",         # 08, 8
        "Function_9_1CA0",         # 09, 9
        "Function_10_1E8C",        # 0A, 10
    ))


    def Function_0_1C4(): pass

    label("Function_0_1C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_210"),
        (2, "loc_21C"),
        (3, "loc_228"),
        (4, "loc_234"),
        (5, "loc_240"),
        (6, "loc_24C"),
        (SWITCH_DEFAULT, "loc_258"),
    )


    label("loc_204")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_210")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_21C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_228")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_234")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_240")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_24C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_27B")

    Return()

    # Function_0_1C4 end

    def Function_1_27C(): pass

    label("Function_1_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_290")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)
    Jump("loc_29F")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_29F")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 7)

    label("loc_29F")

    Return()

    # Function_1_27C end

    def Function_2_2A0(): pass

    label("Function_2_2A0")

    Return()

    # Function_2_2A0 end

    def Function_3_2A1(): pass

    label("Function_3_2A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02708.itc", 0x1E)
    LoadChrToIndex("apl/ch50511.itc", 0x1F)
    LoadChrToIndex("chr/ch05502.itc", 0x20)
    LoadChrToIndex("chr/ch00002.itc", 0x21)
    LoadChrToIndex("chr/ch00102.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("chr/ch00302.itc", 0x24)
    LoadChrToIndex("chr/ch08202.itc", 0x25)
    LoadChrToIndex("chr/ch08702.itc", 0x26)
    SoundLoad(460)
    OP_68(0, 1100, -5000, 0)
    MoveCamera(305, 15, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x153, 0x25)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x158, 0x26)
    SetChrSubChip(0x158, 0x0)
    SetChrFlags(0x158, 0x4)
    SetChrPos(0x101, -400, 100, 600, 90)
    SetChrPos(0x102, -400, 100, 2000, 90)
    SetChrPos(0x103, -100, 100, 2600, 135)
    SetChrPos(0x104, 1300, 100, 3000, 180)
    SetChrPos(0x153, -400, 100, 1300, 90)
    SetChrPos(0x158, 500, 100, 3000, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 900, 100, -600, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -700, 100, -1900, 180)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 900, 100, -1900, 180)
    BeginChrThread(0x101, 3, 0, 5)
    Sound(460, 2, 80, 0)
    OP_68(0, 1100, 0, 5000)
    SetCameraDistance(26500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x11)
    Sleep(500)

    #C0001
    ChrTalk(
        0x9,
        (
            "#2803F#5P不仅是鲁巴彻，\x01",
            "连警备队也……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "#12P#2906F……该怎么说……\x01",
            "这状况真是不得了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#11P#0006F……是啊。\x01",
            "说实话，简直就像在做噩梦一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#11P#0105F说起来，叔叔，你们\x01",
            "为什么正好在那个时机……？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "#2800F#5P啊，之前在共和国谈生意，\x01",
            "正在回来的路上……\x02\x03",

            "#2803F然后，在经过唐古拉姆门的时候，\x01",
            "遭到了那些黑手党的袭击。\x02\x03",

            "#2801F好不容易突出重围，逃到那一带，\x01",
            "正好遇见你们遭受袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        "#11P#0101F原来是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#11P#0304F哎呀～\x01",
            "不过，真是帮了大忙了。\x02\x03",

            "#0305F这辆车难道是防弹的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#2809F#5P嗯，是特别定做的。\x02\x03",

            "#2800F因为装设了防弹玻璃，\x01",
            "应该不会被轻易击碎。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#0202F#11P莱恩福尔特公司制造的\x01",
            "最新型高级防弹轿车啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        "#11P#0300F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        (
            "#12P#2903F不过，再怎么说，恐怕也不可能\x01",
            "连炮击都扛得住吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    #C0012
    ChrTalk(
        0xA,
        (
            "#12P#2901F──父亲，\x01",
            "接下来是要直接回ＩＢＣ吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "#2804F#5P嗯，正有此意。\x02\x03",

            "#2800F他们想必也很累了，\x01",
            "就让他们好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x101,
        (
            "#11P#0011F这怎么行，我们不能\x01",
            "再给您添麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#11P#0108F那个……您的好意\x01",
            "我们就心领了，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "#12P#2904F艾莉，\x01",
            "别再说这么见外的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#2800F#5PＩＢＣ的大门是用特殊合金制造的，\x01",
            "应该没那么容易被突破。\x02\x03",

            "#2803F而且，作为ＩＢＣ的总裁，\x01",
            "对克洛斯贝尔的治安\x01",
            "怎能毫不关心……\x02\x03",

            "#2801F所以，可以的话，希望你们\x01",
            "把事情的详细经过告诉我。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#11P#0102F迪塔叔叔……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#11P#0002F……明白了，\x01",
            "那就麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        "#12P#2902F呵呵，那就这么决定了。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x153,
        "#5P#1108F#60W…………………………\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x158,
        "#11P#6008F#60W…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0023
    ChrTalk(
        0x101,
        (
            "#0000F#5P你们两个……\x01",
            "好像很困吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x153, 0x2)
    Sleep(300)

    #C0024
    ChrTalk(
        0x153,
        (
            "#11P#1101F#40W哎……？\x01",
            "琪雅才不困呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x158,
        "#11P#6000F#40W我、我没事……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#11P#0106F不必勉强哦，\x01",
            "都已经快十点了……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#11P#0300F之前一直都让你们陪着\x01",
            "我们经历激战呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        (
            "#12P#2909F呵呵，到了ＩＢＣ以后，\x01",
            "就给你们安排床铺吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "#2800F#5P好，既然决定了，\x01",
            "就全力飞车前往ＩＢＣ吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1100, 5000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    BeginChrThread(0xC, 1, 0, 6)
    OP_6F(0x1)
    EndChrThread(0x101, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x158, 0x4)
    SetChrChipByIndex(0x158, 0xFF)
    SetChrSubChip(0x158, 0x0)
    RemoveParty(0x52, 0x0)
    RemoveParty(0x57, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    WaitChrThread(0xC, 1)
    OP_24(0x1CC)
    SetScenarioFlags(0x5C, 0)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2A1 end

    def Function_4_CDE(): pass

    label("Function_4_CDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D02")
    OP_82(0x14, 0x14, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_4_CDE")

    label("loc_D02")

    Return()

    # Function_4_CDE end

    def Function_5_D03(): pass

    label("Function_5_D03")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D27")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_5_D03")

    label("loc_D27")

    Return()

    # Function_5_D03 end

    def Function_6_D28(): pass

    label("Function_6_D28")

    Sleep(200)
    OP_25(0x1CC, 0x3C)
    Sleep(200)
    OP_25(0x1CC, 0x32)
    Sleep(200)
    OP_25(0x1CC, 0x28)
    Sleep(200)
    OP_25(0x1CC, 0x1E)
    Sleep(200)
    OP_25(0x1CC, 0x14)
    Sleep(200)
    OP_25(0x1CC, 0xA)
    Sleep(200)
    OP_24(0x1CC)
    Return()

    # Function_6_D28 end

    def Function_7_D59(): pass

    label("Function_7_D59")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50518.itc", 0x1E)
    LoadChrToIndex("apl/ch50519.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch00202.itc", 0x22)
    LoadChrToIndex("chr/ch00302.itc", 0x23)
    SoundLoad(492)
    OP_68(100000, 900, 5000, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30500, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 99600, 100, -300, 90)
    SetChrPos(0x102, 99600, 100, -1200, 90)
    SetChrPos(0x104, 99600, 100, -2200, 90)
    SetChrPos(0x103, 100900, 100, -3000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 101300, -100, 900, 270)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 101000, 100, 2250, 0)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0xFF, "wine", 0x0, 0x1)
    SetMapObjFlags(0x9, 0x4)
    LoadEffect(0x0, "battle\\cr008101.eff")
    LoadEffect(0x1, "event\\ev608_01.eff ")
    LoadEffect(0x2, "event\\eva01_00.eff")
    LoadEffect(0x3, "event\\eva03_00.eff")
    BeginChrThread(0x101, 3, 0, 4)
    Sound(492, 2, 100, 0)
    OP_68(100000, 900, 0, 5000)
    SetCameraDistance(28500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_0D()
    OP_6F(0x11)

    #C0030
    ChrTalk(
        0x104,
        "#0309F呀呼！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0002F#5P科长……真的做到了啊！\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#0109F#5P竟然能如此轻易地\x01",
            "成功突破……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#6P#0202F……有点意外呢。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "#1004F#5P呼，都已经有半年左右没驾驶了，\x01",
            "好在还能顺利搞定啊。\x02\x03",

            "#1001F好，就这样一口气\x01",
            "冲入阿尔摩利卡古道吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#0000F#5P拜托您了……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)
    #Sound(2047, 255, 100, 0)    #voice#Zeit

    #C0036
    ChrTalk(
        0x8,
        "#11P#1201F……呜噜噜噜……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    #C0037
    ChrTalk(
        0x101,
        "#0005F#5P蔡特……？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#0301F怎么了，发生了什么事？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0039
    ChrTalk(
        0x103,
        (
            "#6P#0207F后方有车辆接近……！\x02\x03",

            "是警备队的新型车辆……！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        "#1005F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    OP_68(100000, 900, -2000, 2000)
    FadeToDark(2000, 0, -1)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x101, 0x3)
    OP_24(0x1EC)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev03.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    SoundLoad(492)
    OP_68(100000, 900, 0, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    Sound(492, 2, 100, 0)
    FadeToBright(1000, 0)
    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x102, 3, 0, 8)
    Sleep(1000)

    #C0041
    ChrTalk(
        0x101,
        "#0010F#5P唔……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0106F#5P呀……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#6P#0208F……不妙……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0310F他们好像用上了\x01",
            "不得了的家伙啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        (
            "#1007F#5P总之，只能想办法甩掉他们……！\x02\x03",

            "各位，抓稳了──\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x0)
    EndChrThread(0x101, 0x3)
    BeginChrThread(0x102, 3, 0, 9)
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xB, 0x0, -200, 300, 300, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_136C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_136C)
    SetChrSubChip(0xB, 0x1)

    #C0046
    ChrTalk(
        0xB,
        "#1010F#4S啊……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    OP_68(100000, 900, 1000, 1500)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    OP_6F(0x1)

    #C0047
    ChrTalk(
        0x101,
        "#0011F#5P科、科长！？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        "#0101F#5P您还好吗……！？\x02",
    )

    CloseMessageWindow()

    def lambda_140A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_140A)
    SetChrSubChip(0xB, 0x2)
    Sleep(800)

    #C0049
    ChrTalk(
        0xB,
        (
            "#1003F#5P#40W不、不用担心……\x01",
            "……只是小擦伤……！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0013F#5P但、但是……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#0307F不赶快止血的话就危险了吧！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0052
    ChrTalk(
        0x103,
        (
            "#6P#0201F后面还有一辆车\x01",
            "正在接近……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    #C0053
    ChrTalk(
        0x102,
        "#0108F#11P怎、怎么会这样……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0054
    ChrTalk(
        0x101,
        (
            "#0007F#5P科长……\x01",
            "请立刻停车！\x02\x03",

            "必须要赶快包扎一下……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0055
    ChrTalk(
        0xB,
        (
            "#1010F#5P#30W不要啰嗦，\x01",
            "给我抓稳了……！\x02\x03",

            "为你们这群年轻人开路，\x01",
            "是我们这些大叔的任务……\x02\x03",

            "#1007F绝对会把你们安全送到的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#0005F#5P科、科长……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#0306F真是个深藏不露的热血大叔……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0058
    ChrTalk(
        0x103,
        (
            "#6P#0205F啊……\x02\x03",

            "#0214F──另外一辆车\x01",
            "并不是新型车辆！\x02\x03",

            "是诺艾尔小姐驾驶的警备队车辆！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0059
    ChrTalk(
        0x101,
        "#0002F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_68(100000, 900, -2000, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_24(0x1EC)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev04.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    SoundLoad(492)
    OP_68(100000, 900, 0, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    Sound(492, 2, 100, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0xC, 1, 0, 10)
    Sleep(2500)

    #C0060
    ChrTalk(
        0x101,
        "#0000F#5P诺艾尔上士……！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0102F#5P来帮我们了呢……！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        (
            "#0309F不愧是警备队新一代的\x01",
            "希望之星……！\x02",
        )
    )

    CloseMessageWindow()
    Sound(962, 0, 100, 0)
    Sleep(1800)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("女孩的声音")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──听得到吗！\x02\x03",

            "我是诺艾尔·希卡！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    #C0064
    ChrTalk(
        0x101,
        "#0002F#6P啊，听得到！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xB,
        (
            "#1004F#6P#30W索妮亚的王牌部下吗……\x01",
            "……说实话，真是帮了大忙了……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("诺艾尔的声音")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，不必客气。\x02\x03",

            "──另外一辆车\x01",
            "也由我来对付吧！\x02\x03",

            "诸位，请尽快前进吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0067
    ChrTalk(
        0xB,
        "#1007F#6P哦哦……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0007F#6P你也务必要小心啊！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xC, 0x1)
    EndChrThread(0x101, 0x3)
    OP_82(0x96, 0x0, 0xBB8, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 4)
    Fade(100)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    PlayEffect(0x3, 0x0, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_68(100000, 900, -10000, 4000)
    MoveCamera(330, 13, 0, 4000)
    SetCameraDistance(32000, 4000)
    FadeToDark(4000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    OP_24(0x1EC)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev05.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1EC)
    SetScenarioFlags(0x5C, 0)
    NewScene("r307B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_D59 end

    def Function_8_1C48(): pass

    label("Function_8_1C48")

    OP_82(0x0, 0x190, 0xBB8, 0x320)
    Sound(196, 0, 100, 0)
    Sleep(1000)
    OP_82(0x12C, 0x0, 0xBB8, 0x3E8)
    Sound(200, 0, 100, 0)
    Sleep(1200)
    OP_82(0x0, 0x190, 0xBB8, 0x320)
    Sound(834, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    BeginChrThread(0x101, 3, 0, 4)
    Return()

    # Function_8_1C48 end

    def Function_9_1CA0(): pass

    label("Function_9_1CA0")

    Sound(960, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 98500, -500, 2200, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(99000, 900, 0, 100)
    OP_82(0x320, 0x0, 0x1388, 0x2BC)
    Sleep(100)
    ClearMapObjFlags(0x2, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 2200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x3, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1400, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x4, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1700, 1800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x5, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 1300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x6, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1400, 2900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x7, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 2000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x101, 3, 0, 4)
    Return()

    # Function_9_1CA0 end

    def Function_10_1E8C(): pass

    label("Function_10_1E8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EB7")
    Sound(961, 0, 100, 0)
    Sleep(1500)
    Sound(961, 0, 100, 0)
    Sleep(2500)
    Sound(961, 0, 100, 0)
    Sleep(2000)
    Jump("Function_10_1E8C")

    label("loc_1EB7")

    Return()

    # Function_10_1E8C end

    SaveToFile()

Try(main)
