from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c153b.bin",                # FileName
        "c153b",                    # MapName
        "c153b",                    # Location
        0x00AE,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 174, 0, 0, 0, 1],
    )

    BuildStringList((
        "c153b",                  # 0
        "迪塔市长",               # 1
        "麦克道尔议长",           # 2
        "达德利搜查官",           # 3
        "索妮亚司令",             # 4
        "道格拉斯副司令",         # 5
        "赛尔盖科长",             # 6
        "皮埃尔副局长",           # 7
        "局长？",                 # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_190",          # 01, 1
        "Function_2_191",          # 02, 2
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_18F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_18F")

    Return()

    # Function_0_180 end

    def Function_1_190(): pass

    label("Function_1_190")

    Return()

    # Function_1_190 end

    def Function_2_191(): pass

    label("Function_2_191")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05602.itc", 0x1E)
    LoadChrToIndex("chr/ch05802.itc", 0x1F)
    LoadChrToIndex("chr/ch05702.itc", 0x20)
    LoadChrToIndex("chr/ch44902.itc", 0x21)
    LoadChrToIndex("chr/ch06402.itc", 0x22)
    LoadChrToIndex("chr/ch02502.itc", 0x23)
    LoadChrToIndex("chr/ch00902.itc", 0x24)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 272800, 100, 6950, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 272800, 100, 4950, 270)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 269200, 100, 8950, 90)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 269200, 100, 6950, 90)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 269200, 100, 4950, 90)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 269200, 100, 2950, 90)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 269200, 100, 900, 90)
    OP_68(271500, -1100, 5950, 0)
    MoveCamera(90, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21000, 0)
    OP_68(271500, 900, 5950, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(271700, 800, 5950, 0)
    MoveCamera(36, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17630, 0)
    SetCameraDistance(16630, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x9,
        (
            "#02503F#11P真是没想到……\x02\x03",

            "#02501F区区一个猎兵团，\x01",
            "竟然能引起如此严重的事件。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0002
    ChrTalk(
        0x8,
        (
            "#5P#02803F……他们背后\x01",
            "必定有指使者。\x02\x03",

            "#02801F而且和通商会议时一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xD,
        (
            "#6P#01003F埃雷波尼亚帝国政府……\x02\x03",

            "#01001F不，若要锁定一个具体对象，\x01",
            "应该是『帝国军情报局』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xA,
        (
            "#12P#00606F确实很有\x01",
            "可能呢……\x02\x03",

            "#00601F毕竟情报局的军官\x01",
            "在克洛斯贝尔也曾与\x01",
            "『赤色星座』频繁接触。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xE,
        (
            "#6P事、事到如今，\x01",
            "我们也只能哭着去向\x01",
            "帝国政府道歉求情了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xE,
        (
            "#6P或者请求共和国政府\x01",
            "为我们撑腰……！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#5P#02803F不行，我白天就已经\x01",
            "和帝国政府联络过了。\x02\x03",

            "#02801F而他们的回答……\x01",
            "自然是『毫不知情』。\x02\x03",

            "#02806F……既然已经发表了独立提案，\x01",
            "也无法再向共和国政府寻求援助了。\x01",
            "这都是我的责任……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xE,
        "#6P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xE,
        (
            "#6P……不、不对！\x01",
            "这绝不是市长的责任！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "#02503F#11P总之……\x01",
            "虽说我们只是自治州政府，但如果再这样下去，\x01",
            "也只能正式发出抗议声明了。\x02\x03",

            "#02500F……不过，比起这些问题，我更加担心\x01",
            "身在玛因兹的居民们如今是否平安。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "#6P#02003F……我们已经向民间人士发出了委托，\x01",
            "他们驾驶飞艇，总算在上空确认了那边的情况。\x02\x03",

            "#02001F到目前为止，猎兵团并没有\x01",
            "准备做出掠夺等恶行的迹象。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xC,
        (
            "#5P话虽如此，但状况却没有任何改变，\x01",
            "玛因兹的居民仍是他们的人质。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        (
            "#5P另外，不知食材的储备是否充足，\x01",
            "我们不能再磨蹭下去了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    #C0014
    ChrTalk(
        0x8,
        (
            "#11P#02803F当然，我们现在就来商讨接下来的对策吧。\x02\x03",

            "#02801F……警备队遭受的损失\x01",
            "大概在什么程度？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        (
            "#6P#02006F……无论是人力还是物资，\x01",
            "损失都相当惨重。\x02\x03",

            "#02001F目前，我已经把所有预备战力\x01",
            "都派往山道地区了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "#11P#02806F这样啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0017
    ChrTalk(
        0x8,
        (
            "#02801F#5P对手虽然是战斗专家，\x01",
            "但终究也只是拿钱办事的雇佣集团。\x02\x03",

            "如果交涉得当，说不定可以控制住局面，\x01",
            "避免事态进一步恶化下去。\x02\x03",

            "希望警界诸位\x01",
            "在安抚市民的同时，\x01",
            "也寻找一下那方面的可能性。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        "#12P#00601F明白！\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xE,
        "#6P我、我们马上行动！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xD,
        (
            "#6P#01003F也联络一下游击士协会吧，\x01",
            "现在只能尽力而为了……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17130, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_191 end

    SaveToFile()

Try(main)
