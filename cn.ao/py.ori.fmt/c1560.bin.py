from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1560.bin",                # FileName
        "c1560",                    # MapName
        "c1560",                    # Location
        0x00AC,                     # MapIndex
        "ed7151",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 172, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1560",                  # 0
        "迪塔总统",               # 1
        "战鬼西格蒙德",           # 2
        "谢莉",                   # 3
        "瓦鲁多",                 # 4
        "玛丽亚贝尔",             # 5
        "亚里欧斯长官",           # 6
        "警备员",                 # 7
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(372, 0)                                        # 0

    ScpFunction((
        "Function_0_174",          # 00, 0
        "Function_1_1AC",          # 01, 1
        "Function_2_24B",          # 02, 2
        "Function_3_1514",         # 03, 3
        "Function_4_155E",         # 04, 4
        "Function_5_15A8",         # 05, 5
        "Function_6_1842",         # 06, 6
    ))


    def Function_0_174(): pass

    label("Function_0_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_188")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_1AB")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_19C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)
    Jump("loc_1AB")

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1AB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 6)

    label("loc_1AB")

    Return()

    # Function_0_174 end

    def Function_1_1AC(): pass

    label("Function_1_1AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_200")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_24A")

    Return()

    # Function_1_1AC end

    def Function_2_24B(): pass

    label("Function_2_24B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51716.itc", 0x1E)
    LoadChrToIndex("chr/ch03300.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    LoadChrToIndex("chr/ch03800.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 18000, 150, 116200, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 16800, 0, 111600, 90)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 18000, 0, 111300, 90)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 19600, 0, 111800, 90)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    VolumeBGM(0x46, 0x7D0)
    OP_68(19500, 2000, 111500, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(250, 90, -1, -1)
    SetChrName("格蕾丝")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "接下来，\x01",
            "我想请大家了解\x01",
            "一组消息。\x02\x03",

            "首先是两个月之前发生在\x01",
            "克洛斯贝尔市的袭击事件……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(18000, 1200, 113500, 2000)
    MoveCamera(39, 18, 0, 2000)
    SetCameraDistance(15000, 2000)
    OP_6F(0x79)
    SetChrSubChip(0x8, 0x2)

    #C0002
    ChrTalk(
        0x8,
        (
            "#11301F#5P……这令人不快的影像\x01",
            "究竟还要播放多久？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A4():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_4A4)
    Sleep(100)

    def lambda_4B4():
        OP_93(0xD, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_4B4)
    Sleep(100)

    def lambda_4C4():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_4C4)
    Sleep(100)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0x9, 0)

    #C0003
    ChrTalk(
        0xC,
        (
            "#12P#02913F已经掌握了\x01",
            "入侵线路，正在进行\x01",
            "物理屏蔽。\x02\x03",

            "#02912F大概还需要两分钟左右吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xD,
        (
            "#10503F已经派人去撤收\x01",
            "街头的显示屏了。\x02\x03",

            "#10500F市民们很快就会散去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "#5P#11303F嗯……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "#12P#04500F呵呵，真是精彩的突然袭击啊。\x02\x03",

            "#04504F虚实交错，真乃妙招……\x01",
            "不愧是经验丰富的老将啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#11306F#5P不要一副事不关己的口气……\x02\x03",

            "#11310F都是因为你们没有看好议长，\x01",
            "才会让他搞出这种事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#12P#04504F唔，关于这件事，\x01",
            "我也只能道歉了。\x02\x03",

            "#04502F但话又说回来，如果你当初\x01",
            "接受我的建议，直接斩草除根，\x01",
            "也就不会有这么多麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#5P#11303F……必须要考虑到圣子的心情。\x02\x03",

            "#11301F所以不能对支援科\x01",
            "及其相关人等做得太绝。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xC,
        (
            "#12P#02913F呵呵，虽然很让人不耐烦，\x01",
            "但这件事倒也没什么办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xD,
        (
            "#10503F……市外的国防军士兵\x01",
            "恐怕也受到了不小的影响。\x02\x03",

            "#10500F我会想办法稳定军心。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        "#5P#11303F嗯，拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)
    MoveCamera(39, 18, 0, 4000)
    OP_68(18000, 1200, 108500, 4000)

    def lambda_823():
        OP_96(0xFE, 0x4650, 0x0, 0x182B8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_823)
    Sleep(500)

    def lambda_840():

        label("loc_840")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_840")

    QueueWorkItem2(0x9, 2, lambda_840)
    Sleep(100)

    def lambda_855():

        label("loc_855")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_855")

    QueueWorkItem2(0xC, 2, lambda_855)
    WaitChrThread(0xD, 1)
    Sound(103, 0, 100, 0)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0xD, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(18000, 1200, 113500, 0)
    MoveCamera(49, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sound(104, 0, 100, 0)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8C8():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_8C8)
    Sleep(100)

    def lambda_8D8():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8D8)
    Sleep(100)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    #C0013
    ChrTalk(
        0x9,
        (
            "#12P#04503F那么，我们也去\x01",
            "干些正事吧。\x02\x03",

            "#04504F接下来，要拿出全力……\x02\x03",

            "#04502F剿灭『黑月』与反抗军的那些家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        (
            "#12P#02912F我去联络\x01",
            "『结社』的各位。\x02\x03",

            "#02913F必须要想办法应对\x01",
            "教会的飞艇和支援科的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "#5P#11301F嗯，去吧。\x02",
    )

    CloseMessageWindow()

    def lambda_9DA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9DA)
    WaitChrThread(0xC, 2)
    SetCameraDistance(16000, 3000)

    def lambda_9F4():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9F4)
    Sleep(100)

    def lambda_A11():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A11)
    WaitChrThread(0x9, 2)

    def lambda_A22():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A22)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, 13000, 0, 3000, 180)
    SetChrPos(0xC, 13000, 0, 3000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    OP_68(13000, 1300, -1100, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    MoveCamera(41, 21, 0, 4000)
    SetCameraDistance(16000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_AFB():
        OP_96(0xFE, 0x32C8, 0x0, 0xFFFFF8F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AFB)

    def lambda_B15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B15)
    Sleep(1000)

    def lambda_B29():
        OP_96(0xFE, 0x32C8, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B29)

    def lambda_B43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B43)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(300)

    #C0016
    ChrTalk(
        0x9,
        (
            "#5P#04504F哎呀呀。\x02\x03",

            "#04500F令尊的性格似乎\x01",
            "有些优柔寡断呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)

    #C0017
    ChrTalk(
        0xC,
        (
            "#12P#02906F唉，你就往好的方面想想，\x01",
            "理解为深谋远虑吧。\x02\x03",

            "#02913F这毕竟是一项要将整个大陆的秩序\x01",
            "推翻重建的庞大计划……\x02\x03",

            "#02902F如果光靠父亲一个人的力量，\x01",
            "终究是不够的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#5P#04504F所以才需要各种优秀的帮手\x01",
            "来协助他吧？\x02\x03",

            "#04500F比如剑圣，还有那位先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        "#12P#02913F呵呵，正是如此。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27500, 0, -600, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28400, 0, -1500, 270)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #N0020
    NpcTalk(
        0xA,
        "少女的声音",
        "爸爸，你们聊完了吗？\x02",
    )

    CloseMessageWindow()

    def lambda_D52():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFFDA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D52)
    Sleep(50)

    def lambda_D6F():
        OP_96(0xFE, 0x4010, 0x0, 0xFFFFFA24, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D6F)

    def lambda_D89():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_D89)
    Sleep(50)

    def lambda_D99():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_D99)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    Fade(500)
    OP_68(24500, 1100, -1100, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    OP_68(14500, 1100, -1100, 4500)
    SetCameraDistance(16500, 4500)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0021
    ChrTalk(
        0xA,
        (
            "#11P#04609F啊，贝尔小姐！\x01",
            "呀哈！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        "#01608F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        (
            "#6P#02909F呵呵，谢莉小姐总是\x01",
            "这么精神呢。\x02\x03",

            "#02902F那件事情\x01",
            "考虑得如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xA,
        (
            "#11P#04605F哦，是指让我担当\x01",
            "大小姐私人部队队长的提议吧？\x02\x03",

            "#04606F唔，虽然听起来很有趣，\x01",
            "但我对现在的状态已经很满意了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xC, 500)
    Sleep(100)

    #C0025
    ChrTalk(
        0x9,
        (
            "#5P#04501F哎呀呀，\x01",
            "请不要在我面前\x01",
            "公然挖角啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)

    #C0026
    ChrTalk(
        0xC,
        (
            "#12P#02904F哎呀，失礼了。\x02\x03",

            "#02912F那么，西格蒙德先生，\x01",
            "就按照之前商定的方案\x01",
            "来执行今后的计划吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "#5P#04504F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    #C0028
    ChrTalk(
        0x9,
        (
            "#04500F#5P小鬼，\x01",
            "你接下来有什么打算？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1030():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1030)

    #C0029
    ChrTalk(
        0xB,
        (
            "#01603F#11P……我可不记得自己\x01",
            "加入了你们一伙。\x02\x03",

            "#01600F想干什么是我自己的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        "#04504F呵……也好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0031
    ChrTalk(
        0xA,
        (
            "#5P#04602F瓦鲁多，如果你愿意，\x01",
            "随时都可以来找我哦，\x01",
            "我一定会好好锻炼你的～\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        "#01601F#11P哼……\x02",
    )

    CloseMessageWindow()
    OP_68(19500, 1200, -1100, 4000)
    MoveCamera(51, 17, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0xA, 3, 0, 4)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(500)

    def lambda_1150():

        label("loc_1150")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1150")

    QueueWorkItem2(0xB, 2, lambda_1150)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(14700, 1200, -1650, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    EndChrThread(0xB, 0x2)

    #C0033
    ChrTalk(
        0xC,
        (
            "#6P#02913F呵呵……\x01",
            "他们真是很可靠呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "#5P#01603F……不就是一对怪物父女吗？\x02\x03",

            "#01602F能与他们对等合作的你，\x01",
            "必然也是个相当的人物……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        (
            "#6P#02909F呵呵……\x02\x03",

            "#02912F你后悔接受\x01",
            "我的邀请了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    #C0036
    ChrTalk(
        0xB,
        (
            "#11P#01604F哼……怎么可能。\x02\x03",

            "#01603F多亏你给我的药，\x01",
            "使我获得了真正的力量……\x02\x03",

            "#01602F除我之外，任何人都无法\x01",
            "完美控制的压倒性力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "#6P#02913F呵呵，是啊。\x02\x03",

            "如果单论膂力，魔人化的\x01",
            "瓦鲁多先生可谓人类中的最强者……\x02\x03",

            "#02902F对于我们而言，\x01",
            "你真是可遇而不可求的绝佳实验体呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "#11P#01604F哼哼，我很愿意\x01",
            "继续当你们的小白鼠。\x02\x03",

            "#01601F为了击败那个混蛋……\x01",
            "证明谁才是最强的。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(500)
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，独立无效宣言\x01",
            "造成了巨大影响，因此而引发的\x01",
            "余波慢慢扩散至国内外。\x02\x03",

            "虽然无法了解笼罩在结界之内的\x01",
            "克洛斯贝尔市的情况……\x02\x03",

            "但已经有不少国防军士兵开始慌乱，\x01",
            "贝尔加德门与唐古拉姆门的\x01",
            "指挥系统也开始出现混乱。\x02\x03",

            "就在此时，\x01",
            "乘坐在梅尔卡瓦中的罗伊德等人\x01",
            "接到了某人的联络。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x23, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_24B end

    def Function_3_1514(): pass

    label("Function_3_1514")


    def lambda_1519():
        OP_95(0xFE, 35000, 0, -100, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1519)
    WaitChrThread(0x9, 1)

    def lambda_1537():
        OP_95(0xFE, 40000, 0, -100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1537)

    def lambda_1551():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1551)
    Return()

    # Function_3_1514 end

    def Function_4_155E(): pass

    label("Function_4_155E")


    def lambda_1563():
        OP_95(0xFE, 35000, 0, -700, 2800, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1563)
    WaitChrThread(0xA, 1)

    def lambda_1581():
        OP_95(0xFE, 40000, 0, -700, 2800, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1581)

    def lambda_159B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_159B)
    Return()

    # Function_4_155E end

    def Function_5_15A8(): pass

    label("Function_5_15A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51716.itc", 0x1E)
    LoadChrToIndex("chr/ch28600.itc", 0x1F)
    OP_68(18000, 1300, 104100, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 18000, 100, 116250, 180)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 18000, 0, 90000, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x4)
    Sound(103, 0, 100, 0)
    OP_68(18000, 1300, 114100, 7000)
    SetCameraDistance(14500, 7000)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1695():
        OP_96(0xFE, 0x4650, 0x0, 0x1B580, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1695)
    WaitChrThread(0xE, 1)
    OP_64(0xE)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)

    def lambda_16E4():
        OP_96(0xFE, 0x4650, 0x96, 0x1C520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16E4)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    SetChrSubChip(0x8, 0x1)
    Sound(886, 0, 100, 0)
    Sleep(500)

    #C0040
    ChrTalk(
        0x8,
        (
            "#5P#11307F#4S『结界』已经消失！？\x02\x03",

            "#11310F可恶……\x01",
            "『结社』的那帮家伙真是没用。\x02\x03",

            "#11303F既然如此，是否应该把所有『神机』召回，\x01",
            "用来防卫都市呢……\x02\x03",

            "#11307F给我把国防长官叫来！\x01",
            "还有贝尔和西格蒙德他们！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xE,
        "#12P知、知道了！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_93(0xE, 0xB4, 0x1F4)

    def lambda_1819():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1819)
    OP_0D()
    EndChrThread(0xE, 0xFF)
    OP_6F(0x79)
    SetScenarioFlags(0x23, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_15A8 end

    def Function_6_1842(): pass

    label("Function_6_1842")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05602.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 18000, 200, 116400, 180)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    OP_68(18000, 1200, 115600, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_6_1842 end

    SaveToFile()

Try(main)
