from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e2010.bin",                # FileName
        "e2010",                    # MapName
        "e2010",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e2010",                  # 0
        "赛尔盖科长",             # 1
        "背景",                   # 2
        "尤利",                   # 3
        "塞克斯",                 # 4
        "瑞吉",                   # 5
        "敏涅斯",                 # 6
        "黑衣人",                 # 7
        "黑衣人",                 # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(440, 0)                                        # 0

    ScpFunction((
        "Function_0_1B8",          # 00, 0
        "Function_1_2C1",          # 01, 1
        "Function_2_327",          # 02, 2
        "Function_3_34C",          # 03, 3
        "Function_4_76F",          # 04, 4
        "Function_5_B61",          # 05, 5
        "Function_6_1075",         # 06, 6
        "Function_7_16BD",         # 07, 7
        "Function_8_2493",         # 08, 8
        "Function_9_2F95",         # 09, 9
        "Function_10_33A7",        # 0A, 10
        "Function_11_373D",        # 0B, 11
        "Function_12_4315",        # 0C, 12
        "Function_13_5FBF",        # 0D, 13
        "Function_14_6290",        # 0E, 14
        "Function_15_63FD",        # 0F, 15
        "Function_16_6536",        # 10, 16
    ))


    def Function_0_1B8(): pass

    label("Function_0_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1CF")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 3)
    Jump("loc_2C0")

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1E3")
    ClearScenarioFlags(0x22, 1)
    Event(0, 4)
    Jump("loc_2C0")

    label("loc_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1F7")
    ClearScenarioFlags(0x22, 2)
    Event(0, 5)
    Jump("loc_2C0")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_20B")
    ClearScenarioFlags(0x22, 3)
    Event(0, 6)
    Jump("loc_2C0")

    label("loc_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_21F")
    ClearScenarioFlags(0x22, 4)
    Event(0, 7)
    Jump("loc_2C0")

    label("loc_21F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_233")
    ClearScenarioFlags(0x22, 5)
    Event(0, 8)
    Jump("loc_2C0")

    label("loc_233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_24A")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 2)
    Event(0, 9)
    Jump("loc_2C0")

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_261")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x0, 3)
    Event(0, 10)
    Jump("loc_2C0")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_275")
    ClearScenarioFlags(0x23, 0)
    Event(0, 11)
    Jump("loc_2C0")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_289")
    ClearScenarioFlags(0x23, 1)
    Event(0, 12)
    Jump("loc_2C0")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_29D")
    ClearScenarioFlags(0x23, 3)
    Event(0, 13)
    Jump("loc_2C0")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_2B1")
    ClearScenarioFlags(0x23, 4)
    Event(0, 14)
    Jump("loc_2C0")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_2C0")
    ClearScenarioFlags(0x23, 6)
    Event(0, 16)

    label("loc_2C0")

    Return()

    # Function_0_1B8 end

    def Function_1_2C1(): pass

    label("Function_1_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_326")

    label("loc_2DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 2)
    Jump("loc_326")

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)
    Jump("loc_326")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_326")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_326")

    Return()

    # Function_1_2C1 end

    def Function_2_327(): pass

    label("Function_2_327")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_2_327")

    label("loc_34B")

    Return()

    # Function_2_327 end

    def Function_3_34C(): pass

    label("Function_3_34C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x8000000)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(-1110, 500, 3290, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14280, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 1200, 100, -1900, 180)
    SetChrPos(0x102, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x105, 1200, 100, -400, 180)
    SetChrPos(0x8, 200, 100, 1000, 180)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x3C, 0x3E8)
    FadeToBright(1000, 0)
    OP_68(-570, 500, 500, 3000)
    MoveCamera(323, 22, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14280, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0001
    ChrTalk(
        0x109,
        (
            "#10109F#11P啊……有新车特有的味道呢……\x02\x03",

            "#10102F方向盘周围设计得也很便利，\x01",
            "这真是辆非常棒的导力车啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x105,
        (
            "#10304F#11P座椅很舒服，\x01",
            "内部装潢也十分不错。\x02\x03",

            "#10302F呵呵，我很中意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00012F#12P哈哈……\x01",
            "确实是一辆好车啊。\x02\x03",

            "#00002F而且车内空间很大，\x01",
            "就算坐八个人也绰绰有余。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#00109F#5P呵呵，等缇欧和兰迪回来，\x01",
            "应该也可以坐下。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#01004F#11P赶快试开一下吧。\x02\x03",

            "#01002F车辆的好坏，\x01",
            "只有上路之后才能知道。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x109,
        "#10100F#11P好的，我这就试试！\x02",
    )

    CloseMessageWindow()
    Sound(470, 0, 100, 0)
    OP_82(0xF, 0x23, 0xBB8, 0x1F4)
    Sleep(500)
    Sound(460, 2, 80, 0)
    BeginChrThread(0x101, 3, 0, 2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
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
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    StopSound(460, 1000, 80)
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("t6000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_34C end

    def Function_4_76F(): pass

    label("Function_4_76F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(-720, 500, 200, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 1200, 100, -1900, 180)
    SetChrPos(0x102, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x105, 1200, 100, -400, 180)
    SetChrPos(0x8, 200, 100, 1000, 180)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0007
    ChrTalk(
        0x109,
        "#10109F#5P～～～～¤\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00002F#12P这辆车真的非常好啊……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#00104F#11P是啊，在这么快的速度下，\x01",
            "车身却保持得如此平稳……\x02\x03",

            "#00102F而且引擎也没有什么声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10309F#12P微微传到身上的\x01",
            "震动感也让人很舒服。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#01004F#11P真不愧是著名的蔡斯中央工房啊。\x02\x03",

            "#01002F我甚至都想弄一辆这样的车\x01",
            "来当作私人座驾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        (
            "#10108F#5P唉，我一直都很喜欢\x01",
            "警备队的装甲车……\x02\x03",

            "#10106F现在的感觉就像见异思迁一样，\x01",
            "总觉得有些内疚……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0013
    ChrTalk(
        0x101,
        "#00012F#12P哈哈，有这么夸张吗？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x105,
        (
            "#10302F#12P这就是导力车狂热者\x01",
            "特有的感触吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
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
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r4000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_76F end

    def Function_5_B61(): pass

    label("Function_5_B61")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(99290, 600, 1470, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14280, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 98950, 150, 1900, 0)
    SetChrPos(0x102, 101000, 150, 250, 0)
    SetChrPos(0x109, 101000, 150, 1800, 0)
    SetChrPos(0x105, 98950, 150, 250, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 300, 100, 1100, 180)
    SetChrPos(0x8, 100000, 150, -1350, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13280, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    Sleep(300)

    #C0015
    ChrTalk(
        0x8,
        "#01003F#6P……独眼红发的魁梧男子吗？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00008F#5P是的……\x01",
            "我们已经向一科汇报过此事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x105,
        (
            "#10306F#5P虽然不清楚他的身份，\x01",
            "但怎么看都不是等闲之辈。\x02\x03",

            "#10301F而且他并没有刻意隐藏自己\x01",
            "那强大到异常的战斗力。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#01001F#6P……这就是问题所在。\x02\x03",

            "#01003F如果是恐怖分子或者猎兵，\x01",
            "都应该会隐藏自己的战斗力。\x02\x03",

            "#01000F就算克洛斯贝尔并不具备足以制裁\x01",
            "他们的法律，他们也不会如此张扬。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x109,
        "#10108F#5P确实呢……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#00106F#12P黑月与帝国政府\x01",
            "也有一些可疑的举动……\x02\x03",

            "#00101F看来鲁巴彻覆灭之后，各方势力\x01",
            "开始在暗中搞小动作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#01006F#6P若说是暗中搞小动作，\x01",
            "未免太露骨了一点。\x02\x03",

            "#01000F这个月底还要召开通商会议。\x02\x03",

            "你们到时候应该也会相当忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00003F#5P嗯，我们明白。\x02\x03",

            "#00001F……总之，很有必要查清\x01",
            "那个男人的真正身份。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#00108F#12P是啊……\x01",
            "不知他现在身在何处。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(12780, 2000)
    OP_6F(0x79)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
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
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B61 end

    def Function_6_1075(): pass

    label("Function_6_1075")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(-720, 500, 200, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, 1200, 100, -1900, 180)
    SetChrPos(0x101, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x104, 1200, 100, -400, 180)
    SetChrPos(0x105, 0, 100, 1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sound(2367, 255, 80, 0)    #voice#Randy
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 4)), scpexpr(EXPR_END)), "loc_1297")

    #C0024
    ChrTalk(
        0x104,
        (
            "#00309F#11P过来的路上我就在想，\x01",
            "这辆导力车可真不错啊。\x02\x03",

            "#00302F要是能私人拥有一辆这样的车，\x01",
            "搭讪美女什么的肯定不在话下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1308")

    label("loc_1297")


    #C0025
    ChrTalk(
        0x104,
        (
            "#00309F#11P话说，这辆导力车可真不错啊。\x02\x03",

            "#00302F要是能私人拥有一辆这样的车，\x01",
            "搭讪美女什么的肯定不在话下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1308")

    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0026
    ChrTalk(
        0x101,
        "#00012F#5P我说你啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0027
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，如果依靠物质条件才能成功搭讪，\x01",
            "那你的水准还差得远呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F#11P唔……\x01",
            "你这个后辈也太嚣张了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0029
    ChrTalk(
        0x102,
        (
            "#00109F#6P呵呵……\x01",
            "完全被人家比下去了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#10102F#5P兰迪前辈引以为傲的受欢迎度，\x01",
            "在瓦吉面前根本就不值一提啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#00305F#11P喂喂，诺艾尔！\x01",
            "你我同是警备队出身，这也太薄情了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#10112F#5P呵呵，对不起啦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 4)), scpexpr(EXPR_END)), "loc_1601")

    #C0033
    ChrTalk(
        0x101,
        (
            "#00005F#5P对了，兰迪。\x02\x03",

            "#00000F你是向科长要来了备用钥匙，\x01",
            "开车赶来的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#00100F#6P你什么时候学会\x01",
            "驾驶导力车了？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00304F#11P哦，是利用训练中的\x01",
            "闲暇时间学会的。\x02\x03",

            "#00300F你们最好也抽空学一下，\x01",
            "还挺方便的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00002F#5P哈哈，说的也是。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#00104F#6P为日后着想，\x01",
            "学会驾驶也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x105,
        (
            "#10306F#5P嗯……可我还是比较\x01",
            "喜欢坐别人开的车。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1601")

    Sleep(150)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0039
    ChrTalk(
        0x109,
        "#10101F#11P啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)
    SetCameraDistance(15000, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1075 end

    def Function_7_16BD(): pass

    label("Function_7_16BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(150500, 700, 250, 0)
    MoveCamera(307, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14270, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 150400, 100, -1100, 90)
    SetChrPos(0x102, 151900, 100, 900, 90)
    SetChrPos(0x109, 151900, 100, -1100, 90)
    SetChrPos(0x105, 148800, 100, -100, 90)
    SetChrPos(0x104, 150400, 100, 900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    SetCameraDistance(13770, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00008F#5P……到底是\x01",
            "什么人干的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#00106F#11P完全不清楚对方这样做的目的，\x01",
            "反而更让人感到可怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        (
            "#10108F#6P还有那些炸药……\x01",
            "究竟是从哪里弄到的？\x02\x03",

            "那种东西连警备队\x01",
            "都已经不怎么使用了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#10306F#5P多半是利用了以前留在\x01",
            "那旧矿山里的炸药吧？\x02\x03",

            "#10300F不过我对火药这种东西\x01",
            "并不是很了解……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        "#00303F#5P不，不是那样的。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0045
    ChrTalk(
        0x105,
        "#10305F#5P哦？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#00105F#12P你发现什么了吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0047
    ChrTalk(
        0x104,
        (
            "#00301F#11P漂浮在入口附近的\x01",
            "那些硝烟……\x02\x03",

            "有在近一两年合成的\x01",
            "新炸药的气味。\x02\x03",

            "而且还是威力相当大的类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00001F#6P是、是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        "#10105F#6P不过，你居然能闻出来啊？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#00300F#11P使用火药的重火器\x01",
            "现在并没有被完全淘汰。\x02\x03",

            "虽然正规军几乎不再使用那种类型，\x01",
            "但还是有特别偏好它的家伙。\x02\x03",

            "#00303F……尤其是猎兵团之类。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x101,
        "#00013F#6P难道说……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        "#00101F#12P也、也就是说……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00306F#11P当然了，只是有这个可能性而已。\x02\x03",

            "#00300F顺带一提，现在最常使用\x01",
            "火药式重火器的是埃雷波尼亚。\x02\x03",

            "直到现在，莱恩福尔特公司还保留着\x01",
            "火药式的系列产品。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x109,
        "#10101F#6P这样啊……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，你果然很了解这些啊。\x02\x03",

            "#10303F不过，说到埃雷波尼亚……\x01",
            "出现了讨厌的巧合呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#00008F#6P是啊……\x01",
            "毕竟昨天还发生了那种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#00305F#11P怎么，发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        "#00108F#12P嗯，其实是这样的──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向兰迪说明了与雷克特特务大尉再会的经过。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    #C0060
    ChrTalk(
        0x104,
        (
            "#00301F#11P……那个散漫的家伙\x01",
            "居然是埃雷波尼亚的间谍啊。\x02\x03",

            "我早就觉得他不是\x01",
            "等闲之辈了……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00003F#6P与其说是间谍，\x01",
            "或许更该称为情报军官。\x02\x03",

            "他可能只是想赶在通商会议\x01",
            "召开之前，来这里收集\x01",
            "一些情报吧……\x02\x03",

            "#00008F……另外，和他在一起的\x01",
            "那个红发女孩实在是很令人在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#00106F#12P……唉，那孩子啊……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#10309F#5P呵呵，对你来说，\x01",
            "可谓身心受创吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00302F#11P怎么了？怎么了？\x01",
            "难道发生了什么美妙的事？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        "#10112F#6P其实是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向兰迪说明了与雷克特\x01",
            "一起的红发少女的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    #C0067
    ChrTalk(
        0x104,
        (
            "#00305F#11P……啊…………\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#00112F#12P哎，还是别再提那孩子了吧。\x02\x03",

            "#00113F真是的，我似乎可以体会到\x01",
            "莉夏小姐被伊莉娅小姐\x01",
            "骚扰时的心情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈，很有说服力呢。\x02\x03",

            "#00008F……说起来，她在瞬息之间\x01",
            "就窜到了我的怀中……\x02\x03",

            "#00001F从那种身手来看，\x01",
            "恐怕绝不是普通的民间人士。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        (
            "#10106F#6P对了……\x01",
            "在西克洛斯贝尔街道遇到的\x01",
            "那个人也是从帝国方向来的。\x02\x03",

            "#10105F啊，说起来，\x01",
            "那个人也是一头红发……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0071
    ChrTalk(
        0x105,
        "#10305F#5P哦，听你一说，的确如此呢。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F#5P雷克特大尉和那孩子虽然都是红发，\x01",
            "但在颜色上倒是有些不同……\x02\x03",

            "#00001F可是仔细想想，那孩子的发色\x01",
            "和独眼男人好像一模一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0073
    ChrTalk(
        0x101,
        "#00011F#6P咦……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#00108F#12P难、难道说……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    #Sound(2374, 255, 100, 0)    #voice#Randy

    #C0075
    ChrTalk(
        0x104,
        (
            "#00304F#11P#30W哈哈……\x02\x03",

            "#00311F#30W也就是说，我的红发\x01",
            "也和那两个人十分相似吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        "#10111F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x105,
        (
            "#10301F#5P……看来你好像\x01",
            "有什么头绪？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)
    Sound(2375, 255, 100, 0)    #voice#Randy
    Sleep(1300)

    #C0078
    ChrTalk(
        0x104,
        (
            "#00304F#5P#40W……真服了他们。\x02\x03",

            "#00312F#40W居然来这一手。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(13520, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_16BD end

    def Function_8_2493(): pass

    label("Function_8_2493")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xBE, 0xBE, 0xBE, 0x0, 0x0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("apl/ch50011.itc", 0x23)
    SoundLoad(460)
    SoundLoad(803)
    SoundLoad(3451)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(150500, 700, 250, 0)
    MoveCamera(307, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14270, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 150400, 100, -1100, 90)
    SetChrPos(0x102, 151900, 100, 900, 90)
    SetChrPos(0x109, 151900, 100, -1100, 90)
    SetChrPos(0x105, 148800, 100, -100, 90)
    SetChrPos(0x104, 150400, 100, 900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    PlayBGM("ed7516", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13770, 1000)
    OP_0D()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0079
    ChrTalk(
        0x101,
        "#00001F#6P我说，兰迪……\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    #C0080
    ChrTalk(
        0x101,
        "#00006F#5P啊，怎么在这种时候……\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x9)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0081
    AnonymousTalk(
        0x101,
        (
            "#00001F#3P您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男人的声音")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3451V#40W班宁斯，是我。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD7B)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0083
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F啊，达德利搜查官。\x02\x03",

            "#00000F我听说您出差去了，\x01",
            "现在已经回到克洛斯贝尔了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是的，下午刚回来。\x02\x03",

            "我听艾玛说了，\x01",
            "看来她受到你们不少照顾。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0085
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004F没什么，请不要客气。\x02\x03",

            "#00001F对了……\x01",
            "请问发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是的，我觉得也\x01",
            "告诉你们一下比较好。\x02\x03",

            "鲁巴彻旧址的\x01",
            "新所有者已经定了下来。\x02\x03",

            "是一家名为『深红商会』的公司。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0087
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F『深红商会』……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0088
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F咦！？\x01",
            "不是『黑月』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "听说这家公司瞒过黑月，\x01",
            "抢先签订了买卖合同。\x02\x03",

            "看样子，帝国似乎也在\x01",
            "暗中提供了协助。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0090
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F帝国吗……\x02\x03",

            "#00013F那到底是一家什么样的公司？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那家公司在帝都经营着一家\x01",
            "名为『诺艾·布朗』的高级俱乐部。\x02\x03",

            "大约一年前，在克洛斯贝尔市内\x01",
            "也开设了一间分店。\x02\x03",

            "也就是说，那家公司已经\x01",
            "正式进军克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0092
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F那绝对不会是家\x01",
            "普通的公司吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯……\x02\x03",

            "……奥兰多和你在一起吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0094
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F您说兰迪吗？\x01",
            "嗯，他刚和我们会合……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "关于『深红商会』的事情，\x01",
            "你们可以问他。\x02\x03",

            "晚上我会再联系你们的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 80, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0096
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(804, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)

    #C0097
    ChrTalk(
        0x102,
        "#00108F#11P怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        (
            "#10301F#5P这次通话听起来\x01",
            "有种危险的味道啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00306F#5P原来如此，\x01",
            "他们盯上了鲁巴彻旧址啊。\x02\x03",

            "#00300F#11P诺艾尔，回到市里后，\x01",
            "可以去一趟欢乐街吗？\x02\x03",

            "在后巷前停车就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x109,
        "#10108F#6P当、当然没问题……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x105, 0x0)

    #C0101
    ChrTalk(
        0x101,
        (
            "#00003F#6P……兰迪。\x02\x03",

            "#00013F『深红商会』是一家\x01",
            "什么样的公司？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0102
    ChrTalk(
        0x104,
        (
            "#00306F#5P#30W这个啊……\x02\x03",

            "#00303F它是一家经营高级俱乐部\x01",
            "『诺艾·布朗』的帝国公司……\x02\x03",

            "#00311F不过其真身是──\x01",
            "猎兵团『赤色星座』用于周转资金\x01",
            "而建立的空头公司。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14270, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_24(0x323)
    SetScenarioFlags(0x22, 0)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2493 end

    def Function_9_2F95(): pass

    label("Function_9_2F95")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 151950, 100, 950, 90)
    SetChrPos(0x102, 150400, 100, -1050, 90)
    SetChrPos(0x109, 151750, 170, -1150, 90)
    SetChrPos(0x103, 150400, 100, 950, 90)
    SetChrPos(0x104, 148850, 100, -950, 90)
    SetChrPos(0x105, 148850, 100, 750, 90)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x1, 0x9)
    OP_49()
    SetChrPos(0x9, 150000, 0, 0, 270)
    OP_D5(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0x1, "main", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x46, 0x3E8)
    OP_68(150000, 750, 0, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00008F#5P刚刚那是……\x01",
            "前往医院的急救车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        (
            "#00201F#5P是的，那是乌尔斯拉\x01",
            "医院的车辆。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        "#00303F#5P居然出动了三辆……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        (
            "#00108F#5P应该是在运送\x01",
            "脱轨事故中的负伤者吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x105,
        (
            "#10306F#5P嗯，既然在这种时候出车，\x01",
            "应该不会有错。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00006F#5P……看来塞茜尔姐姐她们\x01",
            "也要开始忙了。\x02\x03",

            "#00001F我们赶快去现场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x109,
        "#10101F#5P好的！\x02",
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
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetScenarioFlags(0x162, 6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21410100), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335B")
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    SetScenarioFlags(0x22, 1)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_33A6")

    label("loc_335B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21302000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3380")
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_33A6")

    label("loc_3380")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21410000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A6")
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    NewScene("r1000", 99, 0, 0)
    IdleLoop()

    label("loc_33A6")

    Return()

    # Function_9_2F95 end

    def Function_10_33A7(): pass

    label("Function_10_33A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    OP_68(-440, 750, 140, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, 1100, 180)
    SetChrPos(0x105, 1300, 100, 1100, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x4, 0x9)
    OP_49()
    SetChrPos(0x9, -8000, 0, 4000, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFrame(0x4, "main", 0x2, "stop")
    SetMapObjFrame(0x4, "obj00", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x46, 0x3E8)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0110
    ChrTalk(
        0x101,
        "#00001F#12P那些巴士是……？\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x109,
        (
            "#10108F#11P那是在共和国与克洛斯贝尔\x01",
            "之间往返的旅游巴士。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#00103F#11P估计正在分批运送\x01",
            "那列事故列车上的乘客吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#00306F#11P哎呀呀，真是不得了啊。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#00208F#12P……那起事故的规模\x01",
            "到底有多大啊？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetChrFlags(0x104, 0x1)
    SetChrFlags(0x103, 0x1)
    SetScenarioFlags(0x162, 7)
    SetScenarioFlags(0x22, 0)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_33A7 end

    def Function_11_373D(): pass

    label("Function_11_373D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SoundLoad(468)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    OP_68(100040, 950, 320, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15750, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 98800, 100, 1700, 0)
    SetChrPos(0x102, 98800, 100, 100, 0)
    SetChrPos(0x109, 101000, 100, 1700, 0)
    SetChrPos(0x105, 101000, 100, -1400, 0)
    SetChrPos(0x104, 98800, 100, -1400, 0)
    SetChrPos(0x103, 101000, 100, 100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    VolumeBGM(0x46, 0x3E8)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0115
    ChrTalk(
        0x109,
        "#5P#10110F这、这是……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#00106F#5P太过分了……居然做出了这种事……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        "#00311F#5P…………………………\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#5P#00010F啧，总之，我们要想办法\x01",
            "确认一下具体事态……\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 60, 0)
    Sleep(300)
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("男人的声音")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我是赛尔盖，能听见吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x2)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x101,
        "#5P#00007F科长……！？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        "#5P#00101F您还好吗！？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，目前还算平安。\x02\x03",

            "警察总部遭到了袭击，\x01",
            "我正在支援科大楼内\x01",
            "处理各方面的联络。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0123
    ChrTalk(
        0x101,
        "#5P#00013F警察总部遭到袭击……！？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x109,
        "#6P#10107F必、必须要尽快赶过去……！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不用了，索妮亚的部队\x01",
            "已经赶往那边了。\x02\x03",

            "如果可以，我希望你们\x01",
            "现在到港湾区去。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0126
    ChrTalk(
        0x101,
        "#5P#00005F港湾区吗……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "据说有一队猎兵刚刚炸毁了\x01",
            "黑月的分公司。\x02\x03",

            "他们随后又冲进了\x01",
            "ＩＢＣ大楼。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "敌人的主力部队\x01",
            "正在向兰花塔发起进攻。\x02\x03",

            "亚里欧斯和达德利他们\x01",
            "一直在奋力抵抗，\x01",
            "但似乎还是需要警备队的支援。\x02\x03",

            "其他的游击士……\x01",
            "如今正在忙着处理那些在市区\x01",
            "肆虐的军用魔兽，无暇分身。\x02\x03",

            "现在也只有你们几个\x01",
            "可以赶到ＩＢＣ了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0129
    ChrTalk(
        0x102,
        "#5P#00108F可、可是……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        (
            "#6P#00201F……支援科那边\x01",
            "没有问题吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我已经尽可能地让路人\x01",
            "来支援科大楼内避难了。\x02\x03",

            "有蔡特负责守门，\x01",
            "军用魔兽也不敢靠近。\x02\x03",

            "琪雅在这里很安全，\x01",
            "所以你们就不用担心了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0132
    ChrTalk(
        0x103,
        "#6P#00206F……这样啊。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x105,
        "#6P#10301F看来应该不会有问题。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#5P#00013F我明白了，\x01",
            "我们这就赶往港湾区。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯……\x01",
            "一定要多加小心。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    #C0136
    ChrTalk(
        0x105,
        (
            "#6P#10308FＩＢＣ大楼……\x01",
            "难道他们的目的是钱吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#5P#00003F目前还不清楚……\x01",
            "总之，我们还是尽快赶去为好。\x02\x03",

            "#00008F虽然很担心遭到袭击的\x01",
            "警察总部……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x109,
        (
            "#6P#10106F……是啊………\x01",
            "但还是赶快去港湾区吧。\x02\x03",

            "#10101F我记得ＩＢＣ大楼里\x01",
            "也有各位的朋友吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        (
            "#5P#00106F嗯……\x01",
            "贝尔很可能在里面。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#6P#00208F约纳和主任……\x01",
            "应该也在财团的事务所里。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#00303F#5P……我先提醒一句，\x01",
            "最好在抵达港湾区之后\x01",
            "就把导力车停下来。\x02\x03",

            "#00301F如果贸然驾车接近，\x01",
            "对方有可能会使用\x01",
            "反战车导弹。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#5P#00011F还有这种危险啊……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x109,
        (
            "#6P#10101F明白了，\x01",
            "这就赶往港湾区入口。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    StopSound(468, 2000, 100)
    OP_68(100000, 850, -3500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrName("")

    #A0144
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人和准备前往\x01",
            "行政区的警备队车辆分开之后……\x02\x03",

            "驾驶导力车不断回避战斗，\x01",
            "并经由东街\x01",
            "来到了港湾区。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7150", "ed7544")
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 2)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_373D end

    def Function_12_4315(): pass

    label("Function_12_4315")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03102.itc", 0x23)
    LoadChrToIndex("chr/ch03202.itc", 0x24)
    LoadChrToIndex("chr/ch00902.itc", 0x25)
    OP_68(-610, 700, 50, 0)
    MoveCamera(321, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14400, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43C5")
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)

    label("loc_43C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43DD")
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)

    label("loc_43DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43F5")
    SetChrChipByIndex(0x106, 0x24)
    SetChrSubChip(0x106, 0x0)

    label("loc_43F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_440D")
    SetChrChipByIndex(0x10A, 0x25)
    SetChrSubChip(0x10A, 0x0)

    label("loc_440D")

    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0xF4, 0x4)
    SetChrFlags(0xF5, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x103, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0xF4, 0x1)
    ClearChrFlags(0xF5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4538")
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x104, -700, 100, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44D4")
    SetChrPos(0x105, 300, 100, 1100, 180)
    Jump("loc_451B")

    label("loc_44D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44FA")
    SetChrPos(0x106, 200, 100, 1100, 180)
    Jump("loc_451B")

    label("loc_44FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_451B")
    SetChrPos(0x10A, 300, 100, 1100, 180)

    label("loc_451B")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x101, 0x2)
    Jump("loc_461D")

    label("loc_4538")

    SetChrPos(0x101, -800, 100, -1700, 180)
    SetChrPos(0x102, 1300, 100, -1900, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, -400, 180)
    ClearScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45A3")
    SetChrPos(0x10A, -700, 100, 1100, 180)
    SetScenarioFlags(0x0, 0)

    label("loc_45A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D3")
    SetChrPos(0x105, -700, 100, 1100, 180)
    Jump("loc_45E4")

    label("loc_45D3")

    SetChrPos(0x105, 300, 100, 1100, 180)

    label("loc_45E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4605")
    SetChrPos(0x106, 200, 100, 1100, 180)

    label("loc_4605")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x102, 0x2)

    label("loc_461D")

    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    VolumeBGM(0x3C, 0x3E8)
    FadeToBright(1000, 0)
    SetCameraDistance(13800, 2000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52C5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4745")

    #C0145
    ChrTalk(
        0x106,
        (
            "#10702F#11P哇……我还是第一次乘坐\x01",
            "这辆导力车，车内的装潢真漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#12P#00009F哈哈，多谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x103,
        (
            "#12P#00202F琪雅也很喜欢\x01",
            "这辆车呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4745")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_481B")

    #C0148
    ChrTalk(
        0x10A,
        (
            "#00605F#11P嗯……这就是蔡斯中央工房的最新型导力车啊。\x02\x03",

            "#00603F确实设计得十分便利，\x01",
            "真想给一科也配备这个型号……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        (
            "#11P#00106F但考虑到大陆目前的状况，\x01",
            "要从利贝尔进口这种导力车\x01",
            "应该很困难……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_481B")

    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    #C0150
    ChrTalk(
        0x109,
        (
            "#10104F#5P嗯，整备情况良好，\x01",
            "导力车随时都可以发动。\x02\x03",

            "#10100F凭借它的性能，\x01",
            "强行突破战区应该不是什么难事。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#12P#00000F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#12P#00203F我们已经成功取回了\x01",
            "用于突破的车辆……\x02\x03",

            "#00200F接下来，不如回科长\x01",
            "他们那里一趟吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        (
            "#11P#00103F说的也是，我也想了解一下\x01",
            "最终定下的计划……\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0154
    ChrTalk(
        0x101,
        "#12P#00013F这是……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A6F")

    #C0155
    ChrTalk(
        0x10A,
        (
            "#00601F#11P是车载式通讯器，\x01",
            "看来是收到了来自某处的联络。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AAD")

    label("loc_4A6F")


    #C0156
    ChrTalk(
        0x104,
        (
            "#11P#00301F是车载式通讯器，\x01",
            "看来是收到了来自某处的联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AAD")


    #C0157
    ChrTalk(
        0x109,
        (
            "#10113F#5P罗、罗伊德警官，\x01",
            "该怎么办……？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯……\x01",
            "接通吧。\x02\x03",

            "#00001F各位，谨慎起见，\x01",
            "请保持安静。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(500)
    Sound(853, 0, 100, 0)
    Sleep(300)
    Sound(899, 0, 50, 0)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("女性的声音")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好久不见了呢，\x01",
            "特别任务支援科的各位。\x02\x03",

            "我是雾香，\x01",
            "雾香·楼兰。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0160
    ChrTalk(
        0x101,
        "#12P#00011F咦……！？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x104,
        "#11P#00307F居然是雾香小姐！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CBE")

    #C0162
    ChrTalk(
        0x106,
        "#10701F#11P（泰斗流的『飞燕红儿』……）\x02",
    )

    CloseMessageWindow()

    label("loc_4CBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D11")

    #C0163
    ChrTalk(
        0x10A,
        (
            "#00601F#11P洛克史密斯机关的主任……\x01",
            "她还在克洛斯贝尔啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7C")

    label("loc_4D11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D7C")

    #C0164
    ChrTalk(
        0x105,
        (
            "#10403F#11P就是卡尔瓦德谍报机关的\x01",
            "那位大姐姐吗……\x02\x03",

            "#10400F没想到她还在克洛斯贝尔啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D7C")


    #C0165
    ChrTalk(
        0x109,
        (
            "#10101F#5P为、为什么能向\x01",
            "这里发出通讯……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#11P#00101F……您完全掌握了\x01",
            "我们的行踪吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("雾香的声音")

    #A0167
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我只是对你们在这种状况下\x01",
            "会采取什么行动做了一番预测。\x02\x03",

            "各位应该很忙吧，在这种时候\x01",
            "本不该打扰你们……\x02\x03",

            "不过，你们有兴趣\x01",
            "跟我『交换情报』吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0168
    ChrTalk(
        0x101,
        "#12P#00008F这……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F6E")

    #C0169
    ChrTalk(
        0x10A,
        (
            "#00603F#11P（……班宁斯，\x01",
            "  由你来做决定吧。）\x02\x03",

            "#00601F（我们一科一直都未能和她\x01",
            "  建立有效的联系渠道。）\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#12P#00003F#11P（……我明白了。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jump("loc_4F86")

    label("loc_4F6E")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    label("loc_4F86")


    #C0171
    ChrTalk(
        0x101,
        (
            "#12P#00006F没问题，雾香小姐。\x02\x03",

            "#00001F我们该到哪里去找您呢？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("雾香的声音")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔车站，停在三号站台的\x01",
            "那辆列车的二号车厢内。\x02\x03",

            "车站内现在空无一人，\x01",
            "你们可以放心过来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0173
    ChrTalk(
        0x101,
        (
            "#12P#00004F我明白了。\x01",
            "是三号站台那辆列车的\x01",
            "二号车厢，没错吧？\x02\x03",

            "#00013F另外……\x01",
            "雷克特先生也在那里吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("雾香的声音")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，猜得没错。\x01",
            "那么，我们恭候各位。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    #C0175
    ChrTalk(
        0x103,
        (
            "#12P#00211F……她还是老样子，\x01",
            "就像有一双千里眼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        (
            "#11P#00108F而且，雷克特大尉\x01",
            "也在那里……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        "#11P#00306F我们也只能去看看了。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#12P#00001F是啊……\x01",
            "这就前往克洛斯贝尔车站吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x109,
        "#10101F#5P明白了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5237")

    #C0180
    ChrTalk(
        0x106,
        (
            "#10701F#11P……以防万一，\x01",
            "我们还是先做好准备吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52C0")

    label("loc_5237")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5280")

    #C0181
    ChrTalk(
        0x105,
        (
            "#10404F#11P以防万一，我们最好\x01",
            "还是做一下准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52C0")

    label("loc_5280")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52C0")

    #C0182
    ChrTalk(
        0x10A,
        (
            "#00603F#11P以防万一，最好还是\x01",
            "先做好准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52C0")

    Jump("loc_5F1A")

    label("loc_52C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5365")

    #C0183
    ChrTalk(
        0x106,
        (
            "#10702F#11P哇……我还是第一次乘坐\x01",
            "这辆导力车，车内的装潢真漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#00009F#5P哈哈，多谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#12P#00202F琪雅也很喜欢\x01",
            "这辆车呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5365")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5464")

    #C0186
    ChrTalk(
        0x10A,
        (
            "#11P#00605F唔，这就是蔡斯中央工房的最新型导力车啊。\x02\x03",

            "#00603F确实设计得十分便利，\x01",
            "真想给一科也配备这个型号……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#12P#00106F但考虑到大陆目前的状况，\x01",
            "要从利贝尔进口这种导力车\x01",
            "应该很困难……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5464")

    #C0188
    ChrTalk(
        0x105,
        "#10403F嗯，确实如此。\x02",
    )

    CloseMessageWindow()

    label("loc_5464")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0189
    ChrTalk(
        0x101,
        (
            "#00004F#5P……整备情况良好，\x01",
            "导力车随时都可以发动。\x02\x03",

            "#00000F但在强行突破的时候，\x01",
            "还是由诺艾尔\x01",
            "来驾驶为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        "#11P#00302F也对，毕竟她才是专业人员。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x103,
        (
            "#12P#00203F我们已经成功取回了\x01",
            "用于突破的车辆……\x02\x03",

            "#00200F接下来，不如回科长\x01",
            "他们那里一趟吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x102,
        (
            "#12P#00103F说的也是，我也想了解一下\x01",
            "最终定下的计划……\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0193
    ChrTalk(
        0x101,
        "#00005F#5P这是……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56CA")

    #C0194
    ChrTalk(
        0x10A,
        (
            "#11P#00601F这是车载式通讯器，\x01",
            "看来是收到了来自某处的联络。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5708")

    label("loc_56CA")


    #C0195
    ChrTalk(
        0x104,
        (
            "#11P#00301F是车载式通讯器，\x01",
            "看来是收到了来自某处的联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5708")


    #C0196
    ChrTalk(
        0x102,
        "#12P#00108F……罗伊德，怎么办？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯……\x01",
            "接通吧。\x02\x03",

            "#00013F各位，谨慎起见，\x01",
            "请保持安静。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(500)
    Sound(853, 0, 100, 0)
    Sleep(300)
    Sound(899, 0, 50, 0)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("女性的声音")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好久不见了呢，\x01",
            "特别任务支援科的各位。\x02\x03",

            "我是雾香，\x01",
            "雾香·楼兰。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0199
    ChrTalk(
        0x101,
        "#00011F#5P咦……！？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        "#11P#00307F居然是雾香小姐！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_590D")

    #C0201
    ChrTalk(
        0x106,
        "#10701F#11P（泰斗流的『飞燕红儿』……）\x02",
    )

    CloseMessageWindow()

    label("loc_590D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5960")

    #C0202
    ChrTalk(
        0x10A,
        (
            "#11P#00601F洛克史密斯机关的主任……\x01",
            "她还在克洛斯贝尔啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59CB")

    label("loc_5960")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59CB")

    #C0203
    ChrTalk(
        0x105,
        (
            "#11P#10403F就是卡尔瓦德谍报机关的\x01",
            "那位大姐姐吗……\x02\x03",

            "#10400F没想到她还在克洛斯贝尔啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59CB")


    #C0204
    ChrTalk(
        0x102,
        (
            "#12P#00101F……您完全掌握了\x01",
            "我们的行踪吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("雾香的声音")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我只是对你们在这种状况下\x01",
            "会采取什么行动做了一番预测。\x02\x03",

            "各位应该很忙吧，在这种时候\x01",
            "本不该打扰你们……\x02\x03",

            "不过，你们有兴趣\x01",
            "跟我『交换情报』吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0206
    ChrTalk(
        0x101,
        "#00008F#5P这……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B84")

    #C0207
    ChrTalk(
        0x10A,
        (
            "#11P#00603F（……班宁斯，\x01",
            "  由你来做决定吧。）\x02\x03",

            "#00601F（我们一科一直都未能和她\x01",
            "  建立有效的联系渠道。）\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#00003F#5P（……我明白了。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jump("loc_5B9C")

    label("loc_5B84")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    label("loc_5B9C")


    #C0209
    ChrTalk(
        0x101,
        (
            "#00006F#5P没问题，雾香小姐。\x02\x03",

            "#00001F我们该到哪里去找您呢？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("雾香的声音")

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔车站，停在三号站台的\x01",
            "那辆列车的二号车厢内。\x02\x03",

            "车站内现在空无一人，\x01",
            "你们可以放心过来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0211
    ChrTalk(
        0x101,
        (
            "#00004F#5P我明白了。\x01",
            "是三号站台那辆列车的\x01",
            "二号车厢，没错吧？\x02\x03",

            "#00013F另外……\x01",
            "雷克特先生也在那里吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("雾香的声音")

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，猜得没错。\x01",
            "那么，我们恭候各位。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    #C0213
    ChrTalk(
        0x103,
        (
            "#12P#00211F……她还是老样子，\x01",
            "就像有一双千里眼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#12P#00108F而且，雷克特大尉\x01",
            "好像也在那里……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x104,
        "#11P#00306F我们也只能去看看了。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#00001F#5P是啊……\x01",
            "这就前往克洛斯贝尔车站吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E19")

    #C0217
    ChrTalk(
        0x10A,
        "#11P#00603F知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E46")

    label("loc_5E19")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E46")

    #C0218
    ChrTalk(
        0x105,
        "#11P#10404F呵呵，好的。\x02",
    )

    CloseMessageWindow()

    label("loc_5E46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E91")

    #C0219
    ChrTalk(
        0x106,
        (
            "#10701F#11P……以防万一，\x01",
            "我们还是先做好准备吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1A")

    label("loc_5E91")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EDA")

    #C0220
    ChrTalk(
        0x105,
        (
            "#10402F#11P以防万一，我们最好\x01",
            "还是做一下准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1A")

    label("loc_5EDA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F1A")

    #C0221
    ChrTalk(
        0x10A,
        (
            "#00601F#11P以防万一，最好还是\x01",
            "先做好准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F1A")

    FadeToDark(1000, 0, -1)
    SetCameraDistance(14300, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0xF4, 0x4)
    ClearChrFlags(0xF5, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x103, 0x1)
    SetChrFlags(0x104, 0x1)
    SetChrFlags(0xF4, 0x1)
    SetChrFlags(0xF5, 0x1)
    OP_37()
    SetScenarioFlags(0x1A5, 5)
    OP_29(0xB1, 0x1, 0x8)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    EventEnd(0x5)
    NewScene("c0200", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_12_4315 end

    def Function_13_5FBF(): pass

    label("Function_13_5FBF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    BeginChrThread(0x101, 3, 0, 2)
    SoundLoad(468)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6100")

    #C0222
    ChrTalk(
        0x103,
        "#00211F被远远抛下了……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        (
            "#00106F算、算了……\x01",
            "毕竟安全驾驶\x01",
            "才是最重要的……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x109,
        "#10106F（唔…………）\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00003F（是我判断失误了吗……？）\x02\x03",

            "#00007F……总、总之，我们继续追赶吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6214")

    label("loc_6100")


    #C0226
    ChrTalk(
        0x103,
        (
            "#00205F下雨天道路湿滑，\x01",
            "居然还能用这种速度转弯……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x102,
        (
            "#00109F但、但这未免也\x01",
            "太危险了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x109,
        (
            "#10102F呵呵，这种程度\x01",
            "根本就不算什么！\x02\x03",

            "#10107F飙车族……\x01",
            "我绝不会让你们逃脱的！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0229
    ChrTalk(
        0x101,
        "#00012F她、她好像兴奋起来了……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0230
    ChrTalk(
        0x101,
        (
            "#00001F……总、总之，\x01",
            "我们继续追赶吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6214")

    Sound(494, 0, 70, 0)
    OP_68(101440, 650, -16510, 3000)
    MoveCamera(311, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11280, 3000)
    Sleep(1000)
    StopSound(468, 1000, 100)
    StopSound(494, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearScenarioFlags(0x178, 5)
    SetScenarioFlags(0x22, 5)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_5FBF end

    def Function_14_6290(): pass

    label("Function_14_6290")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    BeginChrThread(0x101, 3, 0, 2)
    SoundLoad(468)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0231
    ChrTalk(
        0x109,
        (
            "#10110F唔……\x01",
            "他们也挺有一手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x02\x03",

            "#00000F不过，这样下去，\x01",
            "就能和正在西出口待命的\x01",
            "公共安全科两面夹击他们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)

    #C0233
    ChrTalk(
        0x105,
        (
            "#10305F嗯……？\x02\x03",

            "那辆车的样子是不是\x01",
            "有些奇怪啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        "#00005F咦……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopSound(468, 500, 100)
    SetScenarioFlags(0x22, 6)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_6290 end

    def Function_15_63FD(): pass

    label("Function_15_63FD")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(100490, 650, -450, 0)
    MoveCamera(311, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13160, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 99000, 100, 1600, 0)
    SetChrPos(0x102, 99000, 100, 40, 0)
    SetChrPos(0x109, 101100, 100, 1600, 0)
    SetChrPos(0x105, 101100, 100, 40, 0)
    SetChrPos(0x104, 99000, 100, -1420, 0)
    SetChrPos(0x103, 101100, 100, -1420, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Return()

    # Function_15_63FD end

    def Function_16_6536(): pass

    label("Function_16_6536")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SoundLoad(468)
    SoundLoad(469)
    OP_68(-500, 650, 500, 0)
    MoveCamera(324, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13750, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x101, 0x0)
    SetChrBattleFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x102, 0x0)
    SetChrBattleFlags(0x102, 0x4)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    EndChrThread(0x109, 0x0)
    SetChrBattleFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    EndChrThread(0x105, 0x0)
    SetChrBattleFlags(0x105, 0x4)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0x104, 0x0)
    SetChrBattleFlags(0x104, 0x4)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x103, 0x0)
    SetChrBattleFlags(0x103, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x105, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, 1100, 180)
    SetChrPos(0x103, 1300, 100, 1100, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    Sound(469, 2, 60, 0)
    BeginChrThread(0x101, 3, 0, 2)
    FadeToBright(1000, 0)
    OP_0D()

    #C0235
    ChrTalk(
        0x101,
        (
            "#00010F可恶，被手榴弹牵制，\x01",
            "我们无法接近……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x109,
        (
            "#10106F唔……要比车辆性能，\x01",
            "我们是不会输的……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x103,
        (
            "#00201F……但再这样下去，一旦进入\x01",
            "共和国的阿尔泰尔市，事情可就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#00103F那样的话，\x01",
            "恐怕就很难将犯人\x01",
            "抓捕归案了……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        "#00310F啧……真不妙啊。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00001F总之……\x01",
            "不要放弃，继续追吧！\x02\x03",

            "#00007F拜托你了，诺艾尔！\x01",
            "别被甩开，\x01",
            "要牢牢咬紧它！\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        "#10107F是！队长！\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x105,
        "#10305F……嗯……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(468, 300, 90)
    StopSound(469, 300, 50)
    SetScenarioFlags(0x22, 3)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_6536 end

    SaveToFile()

Try(main)
