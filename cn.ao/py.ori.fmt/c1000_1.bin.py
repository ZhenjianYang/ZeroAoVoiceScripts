from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1000_1.bin",                # FileName
        "map1",                    # MapName
        "map1",                    # Location
        0x0010,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [88, 720921, 0, -16777216, 11796682, 28573696, 256, 16777216, 256, 0, 0, 256, -65280, 1660944639, 1936291423, 12336, 11831, 29801, 112, 202, 1, 0, 0],
    )

    BuildStringList((
        "c1000_1",                # 0
    ))

    ChipFrameInfo(88, 0)                                         # 0

    ScpFunction((
        "Function_0_58",           # 00, 0
    ))


    def Function_0_58(): pass

    label("Function_0_58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis232.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis233.itp")
    SoundLoad(803)
    SoundLoad(2711)
    SoundLoad(2712)
    Sleep(500)
    Sound(803, 2, 100, 0)
    Sleep(1600)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_25(0x80, 0x28)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0001
    AnonymousTalk(
        0x101,
        (
            "#00005F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2711V#30W你好，罗伊德警官～！\x02\x03",

            "#2712V#30W在雨中工作，真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA98)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0003
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002F哦，是芙兰啊。\x02\x03",

            "#00000F怎么了？\x01",
            "有什么紧急任务吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，那个……\x02\x03",

            "各位还记得玛因兹\x01",
            "的比克森镇长吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0005
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F嗯，那当然。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0006
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F……莫非矿山镇\x01",
            "发生了什么情况？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，据说有魔兽\x01",
            "出现在矿山中……\x02\x03",

            "啊，不过那好像是座\x01",
            "位于镇外的\x01",
            "旧矿山。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0008
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F……？\x02\x03",

            "#00001F那种地方就算出现魔兽\x01",
            "也很正常吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是的，矿工们并没有\x01",
            "遭受任何侵害。\x02\x03",

            "但矿山内部的状况\x01",
            "似乎有些奇怪……\x02\x03",

            "谨慎起见，希望各位\x01",
            "前去调查。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0010
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F状况有些奇怪……？\x01",
            "听得不是很明白呢。\x02\x03",

            "#00000F知道了，\x01",
            "市内的紧急支援已经处理完毕了，\x01",
            "我们马上赶往玛因兹。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好的，拜托大家啦。\x02\x03",

            "啊，顺便提醒一下，\x01",
            "玛因兹山道中出现了\x01",
            "一种被通缉的魔兽。\x02\x03",

            "如果各位有余力，\x01",
            "就请将它处理掉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0012
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002F是吗，明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，山道地区的天气情况\x01",
            "和市内不同，好像很晴朗。\x02\x03",

            "机会难得，不如\x01",
            "开导力车过去吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0014
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004F这样啊……知道了。\x02\x03",

            "#00000F谢啦，芙兰，\x01",
            "如果有什么新情况，就再和我们联系吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好的，那我挂断了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 60, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sound(804, 0, 100, 0)
    Sleep(800)
    SetMessageWindowPos(240, 110, -1, -1)

    #A0016
    AnonymousTalk(
        0x109,
        "#10105F是芙兰吧？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 40, -1, -1)

    #A0017
    AnonymousTalk(
        0x102,
        (
            "#00101F玛因兹那边\x01",
            "好像发生了什么事？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0018
    AnonymousTalk(
        0x101,
        (
            "#00006F嗯，据说在旧矿山\x01",
            "出现了奇怪的状况。\x02\x03",

            "#00000F市内的支援请求已经处理完了，\x01",
            "我们准备一下，就前往玛因兹吧。\x02\x03",

            "#00002F听说山道地区的天气很晴朗，\x01",
            "我们不妨开车过去。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 30, -1, -1)

    #A0019
    AnonymousTalk(
        0x105,
        "#10304F明白啦，队长。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 110, -1, -1)

    #A0020
    AnonymousTalk(
        0x109,
        (
            "#10100F如果要开车去矿山镇，\x01",
            "我们就先回支援科的后门吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "调查手册和支援科的终端中\x01",
            "增加了新的通缉魔兽任务。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6D, 0x4, 0x2)
    OP_29(0xA1, 0x1, 0x12)
    OP_CC(0x1, 0xFF, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x128, 7)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_25(0x80, 0x64)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_0_58 end

    SaveToFile()

Try(main)
