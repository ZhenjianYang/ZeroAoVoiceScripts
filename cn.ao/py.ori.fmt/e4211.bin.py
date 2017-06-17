from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4211.bin",                # FileName
        "e4211",                    # MapName
        "e4211",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x00',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4211",                  # 0
        "国防军士兵",             # 1
        "国防军士兵",             # 2
        "艾丝蒂尔",               # 3
        "约修亚",                 # 4
        "玲",                     # 5
        "神机３",                 # 6
        "帕蒂尔·玛蒂尔",         # 7
        "显示台词用角色模型",     # 8
        "国防军士兵",             # 9
        "国防军士兵",             # 10
        "国防军士兵",             # 11
        "空",                     # 12
        "路障",                   # 13
        "路障",                   # 14
        "路障",                   # 15
        "防护栏",                 # 16
        "SE控制",                 # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(912, 0)                                        # 0

    ScpFunction((
        "Function_0_390",          # 00, 0
        "Function_1_3A8",          # 01, 1
        "Function_2_3CC",          # 02, 2
        "Function_3_3D2",          # 03, 3
        "Function_4_878",          # 04, 4
        "Function_5_894",          # 05, 5
        "Function_6_8B0",          # 06, 6
        "Function_7_90A",          # 07, 7
        "Function_8_A41",          # 08, 8
        "Function_9_A68",          # 09, 9
        "Function_10_A8F",         # 0A, 10
        "Function_11_BC1",         # 0B, 11
        "Function_12_C1E",         # 0C, 12
        "Function_13_E9A",         # 0D, 13
        "Function_14_25EE",        # 0E, 14
        "Function_15_26AD",        # 0F, 15
        "Function_16_26C1",        # 10, 16
        "Function_17_2720",        # 11, 17
        "Function_18_2754",        # 12, 18
        "Function_19_27F2",        # 13, 19
        "Function_20_28F6",        # 14, 20
        "Function_21_2965",        # 15, 21
        "Function_22_29E4",        # 16, 22
        "Function_23_29FD",        # 17, 23
        "Function_24_2A50",        # 18, 24
        "Function_25_2AB5",        # 19, 25
        "Function_26_2B1A",        # 1A, 26
        "Function_27_2B77",        # 1B, 27
        "Function_28_2BBA",        # 1C, 28
        "Function_29_2C0C",        # 1D, 29
        "Function_30_2C0D",        # 1E, 30
        "Function_31_2C9A",        # 1F, 31
        "Function_32_2CE6",        # 20, 32
        "Function_33_2D89",        # 21, 33
        "Function_34_2E7E",        # 22, 34
        "Function_35_3068",        # 23, 35
        "Function_36_3069",        # 24, 36
        "Function_37_3094",        # 25, 37
        "Function_38_30C8",        # 26, 38
        "Function_39_310E",        # 27, 39
        "Function_40_316E",        # 28, 40
        "Function_41_31BA",        # 29, 41
        "Function_42_3204",        # 2A, 42
        "Function_43_3247",        # 2B, 43
        "Function_44_32C5",        # 2C, 44
        "Function_45_334B",        # 2D, 45
        "Function_46_334C",        # 2E, 46
        "Function_47_33CA",        # 2F, 47
        "Function_48_33E4",        # 30, 48
        "Function_49_33F6",        # 31, 49
        "Function_50_348A",        # 32, 50
        "Function_51_351B",        # 33, 51
        "Function_52_3531",        # 34, 52
        "Function_53_353D",        # 35, 53
        "Function_54_3549",        # 36, 54
        "Function_55_3609",        # 37, 55
        "Function_56_36A9",        # 38, 56
        "Function_57_36E6",        # 39, 57
        "Function_58_37A1",        # 3A, 58
        "Function_59_3925",        # 3B, 59
        "Function_60_39D2",        # 3C, 60
        "Function_61_3EDD",        # 3D, 61
        "Function_62_41A0",        # 3E, 62
        "Function_63_41EB",        # 3F, 63
        "Function_64_424D",        # 40, 64
        "Function_65_42BC",        # 41, 65
        "Function_66_432B",        # 42, 66
        "Function_67_4351",        # 43, 67
        "Function_68_441B",        # 44, 68
        "Function_69_4481",        # 45, 69
        "Function_70_44D4",        # 46, 70
        "Function_71_4523",        # 47, 71
    ))


    def Function_0_390(): pass

    label("Function_0_390")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7")
    SetMapObjFlags(0xA, 0x2000000)

    label("loc_3A7")

    Return()

    # Function_0_390 end

    def Function_1_3A8(): pass

    label("Function_1_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3BC")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_3CB")

    label("loc_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3CB")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_3CB")

    Return()

    # Function_1_3A8 end

    def Function_2_3CC(): pass

    label("Function_2_3CC")

    OP_F3(100000)
    Return()

    # Function_2_3CC end

    def Function_3_3D2(): pass

    label("Function_3_3D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    SoundLoad(993)
    SoundLoad(825)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Call(0, 9)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C")
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    Jump("loc_41F")

    label("loc_41C")

    Call(0, 10)

    label("loc_41F")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -13060, 0, -26480, 270)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -12880, 0, -28330, 270)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2150, 0, -15190, 188)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 5940, 0, 5200, 180)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 1140, 2500, 21380, 180)
    ClearChrFlags(0xF, 0x80)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF, -16000, 4400, -20300, 0)
    OP_70(0x8, 0x1E)
    OP_70(0x9, 0x1E)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    OP_68(10300, 2600, 32500, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(37000, 0)
    FadeToBright(1000, 0)
    OP_68(-11500, 0, -28500, 9000)
    MoveCamera(130, 21, 0, 9000)
    OP_6E(510, 9000)
    SetCameraDistance(38220, 9000)
    OP_0D()
    OP_6F(0x79)
    ClearMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x9, 0x1000)
    OP_68(-13150, 2500, -27500, 0)
    MoveCamera(57, 35, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24000, 0)
    Fade(500)
    OP_68(-13150, 1200, -27500, 3000)
    MoveCamera(57, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(23000, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0001
    ChrTalk(
        0x8,
        (
            "#5P……北出口和东出口\x01",
            "好像已经开战了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    #C0002
    ChrTalk(
        0x9,
        "#11P喂……情况是不是很危险啊？\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "#11P万一索妮亚司令的部队\x01",
            "攻向我们这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#5P应、应该不会的。\x01",
            "她好像说过，在政治问题彻底\x01",
            "确定下来之前，会一直静观其变。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#5P总之，在情况稳定下来之前，\x01",
            "我们只要等待结果就行了。\x02",
        )
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0xF,
        "少女的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1P#N呵呵呵……\x01",
            "采取那种观望的态度\x01",
            "合适吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x18, 1, 0, 6)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x8, 0, 0, 4)
    BeginChrThread(0x9, 0, 0, 5)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    #C0007
    ChrTalk(
        0x9,
        "#5P什、什么……？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "#11P这声音……是从哪里……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_871")
    FadeToDark(1000, 0, -1)
    Sleep(500)
    StopSound(825, 500, 100)
    StopSound(993, 500, 100)
    OP_0D()
    SetScenarioFlags(0x24, 4)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Jump("loc_877")

    label("loc_871")

    Call(0, 7)
    Call(0, 13)

    label("loc_877")

    Return()

    # Function_3_3D2 end

    def Function_4_878(): pass

    label("Function_4_878")

    OP_93(0xFE, 0x140, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x82, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_4_878 end

    def Function_5_894(): pass

    label("Function_5_894")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_5_894 end

    def Function_6_8B0(): pass

    label("Function_6_8B0")

    Sound(825, 2, 30, 0)
    Sound(993, 2, 30, 0)
    Sleep(200)
    OP_25(0x339, 0x28)
    OP_25(0x3E1, 0x28)
    Sleep(200)
    OP_25(0x339, 0x32)
    OP_25(0x3E1, 0x32)
    Sleep(200)
    OP_25(0x339, 0x3C)
    OP_25(0x3E1, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    OP_25(0x3E1, 0x46)
    Sleep(200)
    OP_25(0x339, 0x50)
    OP_25(0x3E1, 0x50)
    Sleep(200)
    OP_25(0x339, 0x5A)
    OP_25(0x3E1, 0x5A)
    Sleep(200)
    OP_25(0x339, 0x64)
    OP_25(0x3E1, 0x64)
    Return()

    # Function_6_8B0 end

    def Function_7_90A(): pass

    label("Function_7_90A")

    Call(0, 8)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    Call(0, 12)
    SetChrPos(0xE, 0, 50000, 0, 0)
    OP_68(0, 48500, 0, 0)
    MoveCamera(180, -45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(57000, 0)
    Fade(500)
    OP_68(0, 55000, 0, 4000)
    MoveCamera(180, -22, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(9250, 4000)
    OP_0D()
    Sound(990, 0, 100, 0)
    Sleep(1000)
    Sound(994, 0, 100, 0)
    Sleep(1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1000)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    Return()

    # Function_7_90A end

    def Function_8_A41(): pass

    label("Function_8_A41")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xC5, 0xEE, 0xFE, 0xC8, 0x514, 0x0)
    Return()

    # Function_8_A41 end

    def Function_9_A68(): pass

    label("Function_9_A68")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xD0, 0xD0, 0xFF, 0x1E, 0x96, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF000000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x190)
    Return()

    # Function_9_A68 end

    def Function_10_A8F(): pass

    label("Function_10_A8F")

    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch09500.itc", 0x20)
    LoadChrToIndex("apl/ch50115.itc", 0x21)
    LoadChrToIndex("apl/ch50547.itc", 0x22)
    LoadChrToIndex("apl/ch50338.itc", 0x23)
    LoadChrToIndex("chr/ch00650.itc", 0x24)
    LoadChrToIndex("chr/ch00651.itc", 0x25)
    LoadChrToIndex("chr/ch00750.itc", 0x26)
    LoadChrToIndex("chr/ch00751.itc", 0x27)
    LoadChrToIndex("chr/ch09556.itc", 0x28)
    LoadChrToIndex("chr/ch00656.itc", 0x29)
    LoadChrToIndex("chr/ch00757.itc", 0x2A)
    LoadEffect(0x8, "event/ev15059.eff")
    LoadEffect(0x2, "event/ev10018.eff")
    LoadEffect(0x0, "event/ev600_00.eff")
    LoadEffect(0x1, "event/ev601_01.eff")
    LoadEffect(0x3, "event/ev14003.eff")
    LoadEffect(0x4, "battle/mgaria0.eff")
    LoadEffect(0x5, "event/ev17064.eff")
    LoadEffect(0x6, "event/ev17063.eff")
    LoadEffect(0x7, "event/eva01_01.eff")
    LoadEffect(0x9, "event/ev17038.eff")
    LoadEffect(0xA, "event/ev17039.eff")
    SoundLoad(979)
    Return()

    # Function_10_A8F end

    def Function_11_BC1(): pass

    label("Function_11_BC1")

    OP_8A(0x0)
    OP_8A(0x1)
    OP_8A(0x3)
    OP_8A(0x8)
    LoadEffect(0x0, "battle/cr006300.eff")
    LoadEffect(0x1, "battle/cr007100.eff")
    LoadEffect(0x3, "event/ev10017.eff")
    LoadEffect(0x8, "event/ev17107.eff")
    Return()

    # Function_11_BC1 end

    def Function_12_C1E(): pass

    label("Function_12_C1E")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 0, 100000, 0, 0)
    OP_78(0xA, 0x13)
    OP_93(0x13, 0x10E, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 0, 0, 0, 0)
    OP_74(0x0, 0xF)
    OP_78(0x0, 0xE)
    OP_93(0xE, 0x0, 0x0)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 0)
    OP_D3(0xC, 0x0, "Null_ren(52)")
    OP_87(0x1, 0x0, 0x0, "Null_S_jet_r0(63)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x1, 0x0, "Null_S_jet_r2(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x2, 0x0, "Null_S_jet_l0(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x3, 0x0, "Null_S_jet_l2(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x4, 0x0, "Null_S_jet_r1(61)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x5, 0x0, "Null_S_jet_l1(62)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x6, 0x0, "Null_kata_jet_r(53)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x7, 0x0, "Null_kata_jet_l(54)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_71(0x0, 0xF1, 0x104, 0x1, 0x20)
    Return()

    # Function_12_C1E end

    def Function_13_E9A(): pass

    label("Function_13_E9A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBA")
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 10)

    label("loc_EBA")

    SoundLoad(979)
    SoundLoad(996)
    SoundLoad(950)
    SoundLoad(579)
    SoundLoad(1038)
    Call(0, 9)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03300.itp")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 0, 100000, 0, 0)
    OP_78(0xA, 0x13)
    OP_93(0x13, 0x10E, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -3000, 5000, -27500, 0)
    OP_74(0x1, 0x1E)
    OP_78(0x1, 0xD)
    OP_93(0xD, 0x10E, 0x0)
    SetChrFlags(0xD, 0x1)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x0, 0xF)
    OP_71(0x1, 0xA, 0x32, 0x0, 0x20)
    Call(0, 12)
    SetChrPos(0xE, -22000, 5000, -27500, 0)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -22500, 0, -36500, 90)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -24370, 100, -31100, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -13060, 0, -26480, 270)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -12880, 0, -28330, 270)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2150, 0, -15190, 180)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -15000, 0, -20330, 0)
    OP_93(0x14, 0x10E, 0x0)
    OP_78(0x2, 0x14)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -15000, 0, -36330, 0)
    OP_93(0x15, 0x10E, 0x0)
    OP_78(0x3, 0x15)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -15000, 0, -43850, 0)
    OP_93(0x16, 0x10E, 0x0)
    OP_78(0x4, 0x16)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -15000, 0, -28750, 0)
    OP_93(0x17, 0x0, 0x0)
    OP_78(0x5, 0x17)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    OP_68(-23500, 5000, -27500, 0)
    MoveCamera(270, 50, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AB")
    Sound(994, 0, 100, 0)
    FadeToBright(1000, 0)
    Jump("loc_11B0")

    label("loc_11AB")

    Fade(500)

    label("loc_11B0")

    OP_68(-23500, 2000, -27500, 1300)
    MoveCamera(270, 30, 0, 1300)
    OP_6E(800, 1300)
    SetCameraDistance(13500, 1300)
    BeginChrThread(0xE, 0, 0, 14)
    BeginChrThread(0xE, 1, 0, 15)
    OP_0D()
    Sleep(500)
    OP_68(-20750, 4100, -29150, 0)
    MoveCamera(312, 28, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9900, 0)
    Fade(500)
    OP_0D()
    CancelBlur(0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0009
    ChrTalk(
        0x9,
        "#5P#4S哇啊啊啊！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0)

    #C0010
    ChrTalk(
        0x8,
        "#5P#4S红色的『神机』……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0xC, 0, 0, 16)
    WaitChrThread(0xC, 0)
    Sleep(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0011
    AnonymousTalk(
        0xC,
        (
            "嘻嘻……贵安。\x02\x03",

            "不过，请不要将『帕蒂尔·玛蒂尔』\x01",
            "和那些智能兵器混为一谈哦。\x02\x03",

            "『帕蒂尔·玛蒂尔』远比它们\x01",
            "帅气、聪明、可靠呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sound(903, 0, 100, 0)
    Sleep(1000)
    OP_68(-18470, 2800, -29000, 0)
    MoveCamera(34, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12380, 0)
    Fade(500)
    OP_0D()

    #C0012
    ChrTalk(
        0x8,
        "#11P难、难道是……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        "#11P敌、敌人吗……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        (
            "#03304F#5P呵呵呵，我可懒得\x01",
            "理会你们这些士兵。\x02\x03",

            "#03300F如果不想被踩成肉饼，\x01",
            "还是退开为好哦。\x02\x03",

            "#03302F看，已经来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "#11P哎……\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1532")
    Call(0, 8)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetChrPos(0xD, 45000, 55000, -27500, 0)
    Sound(979, 2, 100, 0)
    OP_68(-12500, 12400, -27500, 0)
    MoveCamera(90, -26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25000, 0)
    Fade(500)
    Sound(834, 0, 100, 0)
    SetCameraDistance(24000, 2000)
    BeginChrThread(0xD, 0, 0, 17)
    Sleep(1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sound(990, 0, 100, 0)
    WaitChrThread(0xD, 0)

    label("loc_1532")

    Call(0, 9)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrPos(0xD, -5000, 10000, -27500, 0)
    OP_93(0x8, 0x5A, 0x0)
    OP_93(0x9, 0x5A, 0x0)
    OP_68(-4000, 13200, -27500, 0)
    MoveCamera(90, 50, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    OP_68(-4000, 2000, -27500, 1700)
    MoveCamera(90, 30, 0, 1700)
    OP_6E(800, 1700)
    SetCameraDistance(13500, 1700)
    BeginChrThread(0xD, 0, 0, 18)
    BeginChrThread(0xD, 1, 0, 19)
    OP_0D()
    OP_6F(0x79)
    Sleep(700)
    OP_68(-5500, 3900, -27500, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13350, 0)
    Fade(500)
    OP_0D()
    CancelBlur(0)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0016
    ChrTalk(
        0x8,
        "#11P#4S哇啊！？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        "#11P#4S蓝色的『神机』……！\x02",
    )

    CloseMessageWindow()
    OP_68(-15000, 3400, -27500, 0)
    MoveCamera(42, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16000, 0)
    Fade(500)
    OP_0D()
    BeginChrThread(0x8, 0, 0, 20)
    BeginChrThread(0x9, 0, 0, 21)
    Sleep(1000)

    #C0018
    ChrTalk(
        0xC,
        "#03302F#5P呵呵呵……来了啊。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 26)
    Sleep(600)
    OP_68(-15550, -800, -27800, 800)
    MoveCamera(41, 20, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(16350, 800)
    WaitChrThread(0xC, 0)
    BeginChrThread(0xE, 1, 0, 29)
    OP_6F(0x79)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 27)
    BeginChrThread(0xB, 0, 0, 28)
    OP_0D()
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)

    def lambda_1735():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1735)

    def lambda_1742():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1742)
    Sleep(300)

    #C0019
    ChrTalk(
        0xA,
        (
            "#00807F#12P你们几个！\x01",
            "赶快退开吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "#00907F#6P凭你们的战斗力，\x01",
            "根本无法介入这种程度的战斗！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "#5P唔唔……！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        "#11P撤、撤退到铁桥！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x8, 0, 0, 23)
    BeginChrThread(0x9, 0, 0, 24)
    BeginChrThread(0x10, 0, 0, 25)
    WaitChrThread(0xE, 1)
    Sleep(2000)

    def lambda_183B():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_183B)
    Sleep(50)

    def lambda_184B():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_184B)
    SetChrPos(0xE, -22500, 0, -27500, 0)
    OP_93(0xE, 0x5A, 0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x17D, 0x1A4, 0x1, 0x20)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    SetChrPos(0xD, -3000, 0, -27500, 0)
    OP_93(0xD, 0x10E, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x33, 0x5A, 0x0, 0x0)
    OP_D3(0xC, 0xFF, "")
    SetChrChipByIndex(0xC, 0x22)
    SetChrPos(0xC, -20200, 0, -33250, 71)
    TurnDirection(0xC, 0xD, 0)
    SetChrPos(0xA, -18500, 0, -33500, 45)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    TurnDirection(0xA, 0xD, 0)
    SetChrPos(0xB, -19250, 0, -32000, 45)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    TurnDirection(0xB, 0xD, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_FF(0xB, 0x3E8, 0x3E8, 0xFA)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x9, 0x1000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xA, 0x32, 0x0, 0x20)
    OP_68(-19800, 500, -33100, 0)
    MoveCamera(251, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10810, 0)
    Fade(500)
    OP_0D()
    Sleep(150)

    #C0023
    ChrTalk(
        0xA,
        (
            "#00808F#6P玲……不要太硬来。\x02\x03",

            "#00801F我们也会全力援护的。\x02",
        )
    )

    Call(0, 11)
    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "#00903F#12P虽然帕蒂尔·玛蒂尔得到了强化，\x01",
            "但还是对方的力量更强大。\x02\x03",

            "#00901F我们只能在游斗中寻找胜机！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xC,
        (
            "#03303F#5P嗯，知道了。\x02\x03",

            "#03308F休想在\x01",
            "他们居住的地方\x01",
            "继续为所欲为……\x02\x03",

            "#03307F我们上吧！\x01",
            "艾丝蒂尔、约修亚！\x01",
            "还有『帕蒂尔·玛蒂尔』！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-20750, 3300, -28470, 0)
    MoveCamera(224, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10730, 0)
    Fade(500)
    OP_0D()
    Sleep(300)
    BeginChrThread(0xE, 3, 0, 71)
    Sound(903, 0, 100, 0)
    WaitChrThread(0xE, 3)
    Sleep(1000)
    OP_68(-4250, 4100, -27500, 0)
    MoveCamera(144, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    Fade(500)
    BeginChrThread(0xD, 0, 0, 30)
    BeginChrThread(0xE, 0, 0, 36)
    BeginChrThread(0xC, 0, 0, 40)
    BeginChrThread(0xA, 0, 0, 41)
    BeginChrThread(0xB, 0, 0, 42)
    Sleep(500)
    Sound(979, 2, 50, 0)
    Sleep(400)
    OP_68(-4250, 4000, -27501, 800)
    MoveCamera(144, 25, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(20030, 800)
    OP_0D()
    Sound(655, 0, 50, 0)
    OP_87(0x6, 0xFF, 0x1, "Null_eyes(76)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    OP_68(-23770, 4200, -28350, 2600)
    MoveCamera(115, 22, 0, 2600)
    OP_6E(800, 2600)
    SetCameraDistance(20590, 2600)
    Sleep(1000)
    Sleep(1500)
    OP_68(-24750, 3800, -24090, 1000)
    MoveCamera(131, 20, 0, 1000)
    OP_6E(800, 1000)
    SetCameraDistance(20590, 1000)
    BlurSwitch(0x1392, 0x55FFFFFF, 0x0, 0x1, 0xA)
    Sleep(450)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -34980, 7900, -27270, 99, 90, 0, 150, 1250, 150, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    WaitChrThread(0xE, 0)
    BeginChrThread(0xE, 0, 0, 37)
    OP_68(-27050, 3800, -26330, 800)
    MoveCamera(112, 20, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(16480, 800)
    Sleep(700)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_68(-25000, 3100, -26000, 800)
    MoveCamera(114, 22, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(15500, 800)
    OP_6F(0x79)
    WaitChrThread(0xE, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -24660, 5400, -27620, 82, 90, 0, 700, 1500, 700, 0xFF, 0, 0, 0, 0)
    Sound(200, 0, 100, 0)
    Sound(902, 0, 100, 0)

    label("loc_1D60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D77")
    Sleep(50)
    Jump("loc_1D60")

    label("loc_1D77")

    OP_68(-18500, 3700, -29000, 2000)
    MoveCamera(112, 25, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(27350, 2000)
    Sleep(500)
    CancelBlur(500)
    Sleep(500)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    EndChrThread(0xC, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    SetChrPos(0xE, -26000, 0, -26000, 35)
    SetChrPos(0xD, -8500, 0, -33240, 300)
    OP_68(-9800, 4100, -32450, 0)
    MoveCamera(121, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14760, 0)
    Fade(500)
    OP_0D()
    BeginChrThread(0xD, 0, 0, 43)
    Sleep(400)
    OP_68(-9800, 5700, -32450, 3000)
    MoveCamera(121, 23, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(12200, 4000)
    Sleep(1000)
    Sleep(700)
    SetCameraDistance(12200, 1200)
    OP_87(0x9, 0x6, 0x1, "Null_hand_l(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    OP_87(0x9, 0x7, 0x1, "Null_hand_r(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Sound(1039, 0, 100, 0)
    Sleep(2200)
    OP_6F(0x79)
    Fade(500)
    OP_68(-9800, 5200, -32450, 0)
    MoveCamera(75, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xA, 0x32, 0x0, 0x20)
    OP_0D()
    Sound(1038, 2, 100, 0)
    Sound(1014, 0, 100, 0)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    OP_87(0xA, 0x4, 0x1, "Null_hand_l(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x3E8, 0x0)
    OP_87(0xA, 0x5, 0x1, "Null_hand_r(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x3E8, 0x0)
    MoveCamera(64, 23, 0, 1000)
    SetCameraDistance(13000, 1000)
    Sleep(500)
    WaitChrThread(0xD, 0)
    OP_6F(0x79)
    StopSound(579, 500, 70)
    StopSound(1038, 1000, 90)
    SetMapObjFlags(0x1, 0x4)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2016")
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    Call(0, 8)
    SetChrPos(0x13, 0, 0, 0, 0)
    Jump("loc_2016")

    label("loc_2016")

    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    Fade(500)
    OP_68(-23610, 800, -36580, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10350, 0)
    BeginChrThread(0xE, 0, 0, 44)
    BeginChrThread(0xC, 0, 0, 46)
    BeginChrThread(0xA, 0, 0, 49)
    BeginChrThread(0xB, 0, 0, 50)

    label("loc_2067")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_207E")
    Sleep(50)
    Jump("loc_2067")

    label("loc_207E")

    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C5")
    OP_68(-26050, 2300, -30050, 700)
    MoveCamera(323, 1, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(16180, 700)
    Jump("loc_20F3")

    label("loc_20C5")

    OP_68(-24870, 2900, -26210, 700)
    MoveCamera(329, 29, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(13680, 700)

    label("loc_20F3")

    Sleep(400)
    BlurSwitch(0x0, 0x88FFFFFF, 0x0, 0x1, 0xA)
    Sound(1038, 2, 100, 0)
    Sound(1014, 0, 100, 0)
    PlayEffect(0xA, 0x4, 0xFF, 0x0, -2750, 5000, -38400, 297, 2, 0, 1500, 1500, 950, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA, 0x5, 0xFF, 0x0, -1070, 5000, -34550, 289, 5, 0, 1500, 1500, 950, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    CancelBlur(1000)
    Sleep(800)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopSound(1038, 1000, 90)
    Sleep(1000)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xC, 0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D5")
    ClearMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    Call(0, 9)
    Jump("loc_21D5")

    label("loc_21D5")

    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    SetMapObjFlags(0x1, 0x4)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xC, -24000, 0, -37000, 349)
    SetChrPos(0xA, -20020, 0, -37390, 78)
    SetChrPos(0xB, -20020, 0, -35630, 80)
    OP_68(-21400, 400, -36720, 0)
    MoveCamera(260, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    Fade(500)
    BeginChrThread(0xE, 0, 0, 45)
    BeginChrThread(0xC, 0, 0, 51)
    BeginChrThread(0xA, 0, 0, 54)
    BeginChrThread(0xB, 0, 0, 55)
    PlayEffect(0x3, 0x7, 0xA, 0x5, 0, 3000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    CancelBlur(1000)
    OP_68(-8750, 1400, -34450, 1300)
    MoveCamera(260, 20, 0, 1300)
    OP_6E(800, 1300)
    SetCameraDistance(6750, 1300)
    OP_6F(0x79)
    Sleep(600)
    StopEffect(0x7, 0x2)
    Sleep(350)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetChrFlags(0xD, 0x1)
    SetChrPos(0xA, -11800, 0, -37820, 45)
    SetChrFlags(0xA, 0x4)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetChrPos(0xB, -5790, 800, -28380, 225)
    SetChrFlags(0xB, 0x4)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    OP_68(-7830, 1400, -33700, 0)
    MoveCamera(103, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16840, 0)
    Fade(500)
    BeginChrThread(0xD, 0, 0, 56)
    BeginChrThread(0xA, 0, 0, 59)
    BeginChrThread(0xB, 0, 0, 61)
    MoveCamera(116, 30, 0, 3200)
    Sleep(3200)
    SetCameraDistance(9350, 700)
    Sleep(700)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_68(-7830, 1400, -33700, 2500)
    MoveCamera(135, 64, 0, 2500)
    SetCameraDistance(22000, 2500)
    Sleep(2500)
    CancelBlur(500)
    OP_68(-7830, 1300, -33700, 800)
    MoveCamera(135, 39, 0, 800)
    OP_6E(800, 800)
    SetCameraDistance(12500, 800)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xD, 0)
    OP_6F(0x79)
    Sleep(300)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    OP_68(-7830, 2000, -33700, 0)
    MoveCamera(93, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20000, 0)
    Fade(500)
    SetCameraDistance(22000, 2000)
    BeginChrThread(0xD, 0, 0, 63)
    BeginChrThread(0xA, 0, 0, 64)
    BeginChrThread(0xB, 0, 0, 65)
    Sleep(2000)
    OP_0D()
    OP_68(-7830, 2000, -33700, 2500)
    MoveCamera(78, 47, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(22000, 2500)
    Sleep(800)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -20080, 7700, -27960, 122, 90, 0, 250, 2250, 250, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetChrFlags(0xB, 0x1000)
    SetChrFlags(0xA, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_68(-19550, 100, -29800, 0)
    MoveCamera(239, 22, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12310, 0)
    SetChrPos(0xC, -23500, 0, -34750, 0)
    TurnDirection(0xC, 0xD, 0)
    OP_68(-14570, 3600, -30280, 5000)
    MoveCamera(177, 40, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(32910, 5000)
    BeginChrThread(0xD, 0, 0, 66)
    BeginChrThread(0xE, 0, 0, 67)
    BeginChrThread(0xC, 0, 0, 68)
    BeginChrThread(0xA, 0, 0, 69)
    BeginChrThread(0xB, 0, 0, 70)
    Sleep(2000)
    BlurSwitch(0x7D0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    Sleep(2000)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    StopSound(979, 1000, 40)
    StopSound(833, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 4)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_E9A end

    def Function_14_25EE(): pass

    label("Function_14_25EE")

    SetChrPos(0xFE, -23000, 5000, -27500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x5A, 0x0)
    OP_9F(0x1, -22500, 0, -27500)
    OP_9F(0x2, 0xFE, 8000, 0x0)
    StopSound(825, 500, 100)
    StopSound(993, 500, 100)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x17D, 0x1A4, 0x1, 0x20)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x5DC)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Sleep(300)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    Return()

    # Function_14_25EE end

    def Function_15_26AD(): pass

    label("Function_15_26AD")

    Sleep(1150)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x17D, 0x1A4, 0x1, 0x20)
    Return()

    # Function_15_26AD end

    def Function_16_26C1(): pass

    label("Function_16_26C1")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(800)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_16_26C1 end

    def Function_17_2720(): pass

    label("Function_17_2720")

    SetChrPos(0xFE, 45000, 55000, -27500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    OP_9F(0x1, -2000, 10000, -27500)
    OP_9F(0x2, 0xFE, 42000, 0x0)
    Return()

    # Function_17_2720 end

    def Function_18_2754(): pass

    label("Function_18_2754")

    SetChrPos(0xFE, -3000, 10000, -27500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    OP_9F(0x1, -3000, 0, -27500)
    OP_9F(0x2, 0xFE, 10000, 0x0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x33, 0x5A, 0x0, 0x0)
    StopSound(979, 1000, 100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x1F4, 0x1770, 0x6A4)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Return()

    # Function_18_2754 end

    def Function_19_27F2(): pass

    label("Function_19_27F2")

    Sleep(1100)
    OP_FF(0x6, 0x3E8, 0x3E8, 0x3E8)
    Sound(880, 0, 100, 0)
    Sound(876, 0, 100, 0)
    Sleep(50)
    OP_FF(0x6, 0x3E8, 0x3E8, 0x320)
    Sleep(50)
    OP_FF(0x6, 0x3E8, 0x3E8, 0x258)
    Sleep(50)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x6, 0x4)
    Sound(200, 0, 100, 0)
    PlayEffect(0x8, 0x1, 0xFF, 0x0, -4030, 30, -27550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x0, 0xFF, 0x0, -5030, 200, -27550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_FF(0xB, 0x3E8, 0x3E8, 0x190)
    Sleep(50)
    Sound(833, 0, 100, 0)
    OP_FF(0xB, 0x3E8, 0x3E8, 0xFA)
    Sleep(600)
    Sleep(600)
    StopEffect(0x0, 0x2)
    OP_79(0x1)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x172, 0x19A, 0x0, 0x20)
    Return()

    # Function_19_27F2 end

    def Function_20_28F6(): pass

    label("Function_20_28F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2964")
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x87, 0x1F4)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(700)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x13B, 0x1F4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Jump("Function_20_28F6")

    label("loc_2964")

    Return()

    # Function_20_28F6 end

    def Function_21_2965(): pass

    label("Function_21_2965")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29E3")
    Sleep(100)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(400)
    BeginChrThread(0xFE, 3, 0, 22)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x13B, 0x1F4)
    Jump("Function_21_2965")

    label("loc_29E3")

    Return()

    # Function_21_2965 end

    def Function_22_29E4(): pass

    label("Function_22_29E4")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)
    Return()

    # Function_22_29E4 end

    def Function_23_29FD(): pass

    label("Function_23_29FD")

    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x3C8C, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0xFA0, 0x1388, 0x1)

    def lambda_2A2B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A2B)
    OP_9B(0x0, 0xFE, 0x2D, 0xBB8, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_29FD end

    def Function_24_2A50(): pass

    label("Function_24_2A50")

    Sleep(200)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3C8C, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x128E, 0x1388, 0x1)

    def lambda_2A90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A90)
    OP_9B(0x0, 0xFE, 0x2D, 0xBB8, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_2A50 end

    def Function_25_2AB5(): pass

    label("Function_25_2AB5")

    Sleep(400)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x1068, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0xBB8, 0x1388, 0x1)

    def lambda_2AF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AF5)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_2AB5 end

    def Function_26_2B1A(): pass

    label("Function_26_2B1A")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0xFF, "")
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x5A, 0x0)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFB118, 0x0, 0xFFFF7E1E, 0x3E8, 0x7D0)
    Sound(326, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xD, 500)
    Return()

    # Function_26_2B1A end

    def Function_27_2B77(): pass

    label("Function_27_2B77")


    def lambda_2B7C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B7C)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -18500, 0, -33500, 6000, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_27_2B77 end

    def Function_28_2BBA(): pass

    label("Function_28_2BBA")


    def lambda_2BBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BBF)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFB4CE, 0x0, 0xFFFF8300, 0x3E8, 0x5DC)
    Sound(326, 0, 40, 0)
    Sound(540, 0, 40, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_28_2BBA end

    def Function_29_2C0C(): pass

    label("Function_29_2C0C")

    Return()

    # Function_29_2C0C end

    def Function_30_2C0D(): pass

    label("Function_30_2C0D")

    OP_70(0x1, 0x1AE)
    Sleep(500)
    SetChrPos(0xFE, -3000, 0, -27500, 0)
    OP_74(0x1, 0x1E)
    BeginChrThread(0xFE, 1, 0, 32)
    BeginChrThread(0x18, 1, 0, 31)
    OP_71(0x1, 0x1AE, 0x1D6, 0x1, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1AE, 0x1D6, 0x1, 0x0)
    OP_79(0x1)
    OP_74(0x1, 0x1E)
    Sound(1019, 0, 100, 0)
    OP_71(0x1, 0x24E, 0x276, 0x1, 0x0)
    OP_79(0x1)
    Sound(288, 0, 100, 0)
    Sound(833, 0, 80, 0)
    OP_71(0x1, 0x276, 0x28A, 0x1, 0x0)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    OP_71(0x1, 0x28A, 0x2B2, 0x1, 0x0)
    Return()

    # Function_30_2C0D end

    def Function_31_2C9A(): pass

    label("Function_31_2C9A")

    Sleep(500)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(600)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(600)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(600)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Sleep(600)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 50, 0)
    Return()

    # Function_31_2C9A end

    def Function_32_2CE6(): pass

    label("Function_32_2CE6")

    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    OP_9F(0x1, -3500, 0, -27500)
    OP_9F(0x1, -4500, 0, -27500)
    OP_9F(0x1, -5500, 0, -27500)
    OP_9F(0x2, 0xFE, 2000, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1770, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F40, 0x32C8, 0x1)
    BeginChrThread(0xFE, 3, 0, 33)
    OP_9B(0x1, 0xFE, 0x0, 0x1F40, 0x32C8, 0x1)
    WaitChrThread(0xFE, 3)
    Return()

    # Function_32_2CE6 end

    def Function_33_2D89(): pass

    label("Function_33_2D89")

    Sound(114, 0, 100, 0)

    def lambda_2D94():
        OP_96(0xFE, 0xFFFFBD98, 0x15E, 0xFFFF8FB2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2D94)

    def lambda_2DAE():
        OP_D5(0xFE, 0x0, 0x2710, 0x14C08, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2DAE)
    Sleep(100)

    def lambda_2DCA():
        OP_96(0xFE, 0xFFFFC568, 0x32, 0xFFFF75FE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2DCA)

    def lambda_2DE4():
        OP_D5(0xFE, 0x14FF0, 0x41EB0, 0x2710, 0x2BC)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2DE4)
    Sleep(50)
    Sound(1018, 0, 100, 0)

    def lambda_2E06():
        OP_96(0xFE, 0xFFFFC568, 0x64, 0xFFFFAE3E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2E06)

    def lambda_2E20():
        OP_D5(0xFE, 0x14FF0, 0x41EB0, 0xFFFFD8F0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2E20)
    Sleep(50)

    def lambda_2E3C():
        OP_D5(0xFE, 0x80E8, 0x445C0, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2E3C)
    Sleep(150)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x17, 2)
    WaitChrThread(0x14, 1)
    WaitChrThread(0x14, 2)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 2)
    OP_FF(0x5, 0x3B6, 0x15E, 0x2EE)
    Return()

    # Function_33_2D89 end

    def Function_34_2E7E(): pass

    label("Function_34_2E7E")

    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2EA1():
        TurnDirection(0xFE, 0xE, 20)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EA1)
    BeginChrThread(0xFE, 3, 0, 35)
    Sound(996, 2, 50, 0)
    OP_9D(0xFE, 0xFFFFCB44, 0x0, 0xFFFF86E8, 0x3E8, 0x258)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFF830, 0x1388, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0xFA0, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0xBB8, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x7D0, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(996, 1000, 40)
    Return()

    # Function_34_2E7E end

    def Function_35_3068(): pass

    label("Function_35_3068")

    Return()

    # Function_35_3068 end

    def Function_36_3069(): pass

    label("Function_36_3069")

    Sleep(2400)
    BeginChrThread(0xFE, 1, 0, 38)
    Sleep(200)
    OP_96(0xFE, 0xFFFF9A70, 0x0, 0xFFFFB5C8, 0x1B58, 0x1)
    Sleep(500)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    Return()

    # Function_36_3069 end

    def Function_37_3094(): pass

    label("Function_37_3094")

    OP_9D(0xFE, 0xFFFF8AD0, 0x0, 0xFFFF9E58, 0x2EE, 0x3E8)
    Sound(902, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0xFE, 1, 0, 39)
    Sleep(200)
    EndChrThread(0xD, 0x0)
    BeginChrThread(0xD, 0, 0, 34)
    Return()

    # Function_37_3094 end

    def Function_38_30C8(): pass

    label("Function_38_30C8")

    OP_D5(0xFE, 0x0, 0x20F58, 0x0, 0x190)
    OP_74(0x0, 0xC)
    OP_71(0x0, 0xDD, 0xF0, 0x1, 0x0)
    OP_79(0x0)
    OP_D5(0xFE, 0x0, 0x27100, 0x0, 0xC8)
    OP_71(0x0, 0x2EE, 0x302, 0x1, 0x0)
    Return()

    # Function_38_30C8 end

    def Function_39_310E(): pass

    label("Function_39_310E")


    def lambda_3113():
        OP_D5(0xFE, 0x0, 0x15F90, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3113)
    Sound(905, 0, 100, 0)
    Sound(576, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x302, 0x306, 0x1, 0x0)
    OP_79(0x0)

    label("loc_3146")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315D")
    Sleep(50)
    Jump("loc_3146")

    label("loc_315D")

    OP_71(0x0, 0x306, 0x316, 0x1, 0x0)
    WaitChrThread(0xFE, 3)
    Return()

    # Function_39_310E end

    def Function_40_316E(): pass

    label("Function_40_316E")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFA240, 0x64, 0xFFFF6F78, 0x3E8, 0x5DC)
    Sound(326, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)

    def lambda_31AC():

        label("loc_31AC")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_31AC")

    QueueWorkItem2(0xFE, 2, lambda_31AC)
    Return()

    # Function_40_316E end

    def Function_41_31BA(): pass

    label("Function_41_31BA")

    Sleep(3000)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xFFFFAC04, 0x0, 0xFFFF7072, 0x3E8, 0x5DC)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)

    def lambda_31F6():

        label("loc_31F6")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_31F6")

    QueueWorkItem2(0xFE, 2, lambda_31F6)
    Return()

    # Function_41_31BA end

    def Function_42_3204(): pass

    label("Function_42_3204")

    Sleep(3000)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xFFFFA628, 0x0, 0xFFFF7842, 0x3E8, 0x5DC)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)

    def lambda_3239():

        label("loc_3239")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_3239")

    QueueWorkItem2(0xFE, 2, lambda_3239)
    Return()

    # Function_42_3204 end

    def Function_43_3247(): pass

    label("Function_43_3247")

    Sound(905, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x5A, 0x33, 0x1, 0x0)
    OP_79(0x1)
    PlayEffect(0x2, 0xFF, 0xD, 0x5, 0, 0, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(978, 0, 70, 0)
    Sound(579, 2, 80, 0)
    OP_71(0x1, 0xC9, 0xDC, 0x1, 0x0)
    OP_79(0x1)
    Sound(951, 0, 100, 0)
    OP_71(0x1, 0xDD, 0x104, 0x1, 0x20)
    Return()

    # Function_43_3247 end

    def Function_44_32C5(): pass

    label("Function_44_32C5")


    def lambda_32CA():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_32CA)

    label("loc_32D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32E9")
    Sleep(50)
    Jump("loc_32D2")

    label("loc_32E9")

    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(950, 2, 80, 0)
    PlayEffect(0x5, 0xFF, 0xE, 0x5, 0, 3500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sleep(700)
    Sound(202, 0, 100, 0)
    StopSound(950, 1000, 80)
    Sleep(700)
    Return()

    # Function_44_32C5 end

    def Function_45_334B(): pass

    label("Function_45_334B")

    Return()

    # Function_45_334B end

    def Function_46_334C(): pass

    label("Function_46_334C")

    Sleep(150)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    TurnDirection(0xFE, 0xE, 300)
    Sleep(100)
    Sound(357, 0, 70, 0)
    PlayEffect(0x4, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 3, 0, 47)
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xFE, 0x3)
    StopEffect(0x0, 0x2)
    EndChrThread(0xFE, 0x3)
    BeginChrThread(0xFE, 3, 0, 48)
    WaitChrThread(0xFE, 3)
    Return()

    # Function_46_334C end

    def Function_47_33CA(): pass

    label("Function_47_33CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33E3")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_47_33CA")

    label("loc_33E3")

    Return()

    # Function_47_33CA end

    def Function_48_33E4(): pass

    label("Function_48_33E4")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_48_33E4 end

    def Function_49_33F6(): pass

    label("Function_49_33F6")

    Sleep(300)
    TurnDirection(0xFE, 0xD, 500)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFADF8, 0x0, 0xFFFF6D20, 0xFA0, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    label("loc_342A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3441")
    Sleep(50)
    Jump("loc_342A")

    label("loc_3441")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    OP_9B(0x0, 0xFE, 0x4, 0x3E8, 0x1F40, 0x1)
    OP_9D(0xFE, 0xFFFFB87A, 0x1F4, 0xFFFF6F5A, 0x258, 0x3E8)
    OP_9D(0xFE, 0xFFFFCB94, 0x0, 0xFFFF736A, 0xC8, 0x3E8)
    Return()

    # Function_49_33F6 end

    def Function_50_348A(): pass

    label("Function_50_348A")

    Sleep(400)
    TurnDirection(0xFE, 0xD, 500)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFADF8, 0x0, 0xFFFF7428, 0xFA0, 0x0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    label("loc_34BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D5")
    Sleep(50)
    Jump("loc_34BE")

    label("loc_34D5")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x164, 0x3E8, 0x1F40, 0x1)
    OP_9D(0xFE, 0xFFFFB88E, 0x1F4, 0xFFFF7608, 0x258, 0x3E8)
    OP_9D(0xFE, 0xFFFFCBC6, 0x0, 0xFFFF796E, 0xC8, 0x3E8)
    Return()

    # Function_50_348A end

    def Function_51_351B(): pass

    label("Function_51_351B")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    TurnDirection(0xFE, 0xD, 500)
    Return()

    # Function_51_351B end

    def Function_52_3531(): pass

    label("Function_52_3531")

    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_52_3531 end

    def Function_53_353D(): pass

    label("Function_53_353D")

    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_53_353D end

    def Function_54_3549(): pass

    label("Function_54_3549")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x4)
    Sound(809, 0, 50, 0)
    BeginChrThread(0xFE, 3, 0, 52)
    OP_9D(0xFE, 0xFFFFB87A, 0x1F4, 0xFFFF6F5A, 0x258, 0x3E8)
    Sound(326, 0, 50, 0)
    Sound(809, 0, 80, 0)
    BeginChrThread(0xFE, 3, 0, 53)
    OP_9D(0xFE, 0xFFFFCB94, 0x0, 0xFFFF736A, 0xC8, 0x3E8)
    ClearChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sound(326, 0, 80, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x1, 0x7D0, 0x1388, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_93(0xFE, 0x86, 0x0)
    Sound(844, 0, 70, 0)
    Sound(250, 0, 50, 0)
    BeginChrThread(0xFE, 3, 0, 52)
    OP_9D(0xFE, 0xFFFFE624, 0x4B0, 0xFFFF6BAE, 0x4E2, 0x3E8)
    Return()

    # Function_54_3549 end

    def Function_55_3609(): pass

    label("Function_55_3609")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 3, 0, 53)
    OP_9D(0xFE, 0xFFFFB88E, 0x1F4, 0xFFFF7608, 0x258, 0x3E8)
    BeginChrThread(0xFE, 3, 0, 52)
    OP_9D(0xFE, 0xFFFFCBC6, 0x0, 0xFFFF796E, 0xC8, 0x3E8)
    ClearChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x167, 0x7D0, 0x1388, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    OP_93(0xFE, 0x21, 0x0)
    BeginChrThread(0xFE, 3, 0, 53)
    OP_9D(0xFE, 0xFFFFE3A4, 0x4B0, 0xFFFF895E, 0x4E2, 0x3E8)
    Return()

    # Function_55_3609 end

    def Function_56_36A9(): pass

    label("Function_56_36A9")

    Sound(579, 2, 100, 0)
    ClearMapObjFlags(0x1, 0x20)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    StopSound(579, 1000, 90)
    OP_71(0x1, 0x105, 0x118, 0x1, 0x0)
    OP_79(0x1)
    Sound(951, 0, 100, 0)
    OP_71(0x1, 0xA, 0x32, 0x1, 0x20)
    Return()

    # Function_56_36A9 end

    def Function_57_36E6(): pass

    label("Function_57_36E6")

    Sleep(250)
    Sound(534, 0, 100, 0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_57_36E6 end

    def Function_58_37A1(): pass

    label("Function_58_37A1")

    Sleep(900)
    Sound(307, 0, 100, 0)
    Sound(329, 0, 100, 0)
    Sound(264, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -300, 8000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -180, 7200, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -90, 6400, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -30, 5600, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 0, 4800, 750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 0, 4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(329, 0, 100, 0)
    Return()

    # Function_58_37A1 end

    def Function_59_3925(): pass

    label("Function_59_3925")

    OP_95(0xFE, -5740, 100, -36860, 7000, 0x1)
    OP_95(0xFE, -5100, 0, -30220, 7000, 0x1)
    Sound(809, 0, 70, 0)
    OP_9D(0xFE, 0xFFFFEB56, 0x2BC, 0xFFFF91A6, 0x2EE, 0x5DC)
    Sound(326, 0, 60, 0)
    BeginChrThread(0xFE, 3, 0, 57)

    def lambda_397B():
        OP_93(0xFE, 0xF0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_397B)
    Sound(844, 0, 40, 0)
    OP_9D(0xFE, 0xFFFFD198, 0x0, 0xFFFF8A44, 0x3E8, 0x5DC)
    Sound(326, 0, 60, 0)
    BeginChrThread(0xFE, 1, 0, 60)
    OP_95(0xFE, -7950, 100, -33580, 5000, 0x1)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_59_3925 end

    def Function_60_39D2(): pass

    label("Function_60_39D2")

    Sound(562, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x2)
    Sleep(120)
    SetChrSubChip(0xFE, 0x3)
    Sleep(120)
    SetChrSubChip(0xFE, 0x4)
    Sleep(120)
    SetChrSubChip(0xFE, 0x5)
    Sleep(120)
    Sound(321, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1017, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(90)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(60)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(60)
    SetChrSubChip(0xFE, 0x4)
    Sleep(60)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(60)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1100, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1100, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1300, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x4)
    Sleep(30)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1300, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(60)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, 1300, 750, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(60)
    SetChrSubChip(0xFE, 0x4)
    Sleep(60)
    PlayEffect(0x7, 0xFF, 0xD, 0x2, -1300, 750, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(60)
    Sound(501, 0, 100, 0)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(300)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    Return()

    # Function_60_39D2 end

    def Function_61_3EDD(): pass

    label("Function_61_3EDD")

    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD332, 0x32, 0xFFFF7DBA, 0x5DC, 0x7D0)
    Sound(326, 0, 70, 0)

    def lambda_3F05():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F05)
    OP_96(0xFE, 0xFFFFD292, 0x0, 0xFFFF7A90, 0x1B58, 0x1)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD6F2, 0x7D0, 0xFFFF7AEA, 0x802, 0xBB8)
    Sound(326, 0, 70, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, -250, 850, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 250, 650, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3FC6():
        OP_93(0xFE, 0x22, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FC6)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD206, 0x0, 0xFFFF6E60, 0xFA, 0x9C4)
    Sound(326, 0, 70, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFDA8, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x7D0, 0x1)
    Sleep(1300)
    BeginChrThread(0xFE, 1, 0, 62)
    Sleep(500)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_406B():
        OP_93(0xFE, 0x22, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_406B)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFDD46, 0x11F8, 0xFFFF89F4, 0x122A, 0x1194)
    Sound(326, 0, 50, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, -500, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_40E1():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40E1)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD45E, 0x19C8, 0xFFFF7838, 0x802, 0xBB8)
    Sound(326, 0, 70, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 500, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_4157():
        OP_93(0xFE, 0x78, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4157)
    BeginChrThread(0xFE, 3, 0, 58)
    Sound(251, 0, 50, 0)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFDB48, 0x0, 0xFFFF8058, 0xABE, 0x9C4)
    Sound(326, 0, 70, 0)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_61_3EDD end

    def Function_62_41A0(): pass

    label("Function_62_41A0")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    Sound(540, 0, 40, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(80)
    SetChrSubChip(0xFE, 0x1)
    Sleep(80)
    SetChrSubChip(0xFE, 0x2)
    Sleep(80)
    SetChrSubChip(0xFE, 0x3)
    Sleep(80)
    SetChrSubChip(0xFE, 0x4)
    Sleep(80)
    SetChrSubChip(0xFE, 0x5)
    Sleep(80)
    Sound(255, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(80)
    Return()

    # Function_62_41A0 end

    def Function_63_41EB(): pass

    label("Function_63_41EB")

    OP_93(0xFE, 0x14A, 0x3C)
    OP_93(0xFE, 0x10E, 0x3C)

    def lambda_41FE():
        OP_93(0xFE, 0x12C, 0x3C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41FE)
    Sound(1019, 0, 100, 0)
    OP_71(0x1, 0x118, 0x140, 0x1, 0x0)
    OP_79(0x1)
    Sound(288, 0, 100, 0)
    Sound(833, 0, 80, 0)
    OP_71(0x1, 0x141, 0x154, 0x1, 0x0)
    OP_79(0x1)
    Sound(905, 0, 100, 0)
    OP_74(0x1, 0xA)
    OP_71(0x1, 0x155, 0x168, 0x1, 0x0)
    Return()

    # Function_63_41EB end

    def Function_64_424D(): pass

    label("Function_64_424D")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0xFE, 0xFFFFCF54, 0x0, 0xFFFF8A8A, 0x1F4, 0x4B0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFB780, 0x0, 0xFFFF9E1C, 0x1F4, 0x4B0)
    Sound(326, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_64_424D end

    def Function_65_42BC(): pass

    label("Function_65_42BC")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFCC5C, 0x0, 0xFFFF8580, 0x1F4, 0x4B0)
    Sound(326, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFB230, 0x0, 0xFFFF8EA4, 0x5DC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_65_42BC end

    def Function_66_432B(): pass

    label("Function_66_432B")

    TurnDirection(0xFE, 0xE, 500)
    Sleep(1500)
    OP_71(0x1, 0xA, 0x32, 0x1, 0x20)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x3E8, 0x1)
    Return()

    # Function_66_432B end

    def Function_67_4351(): pass

    label("Function_67_4351")

    TurnDirection(0xFE, 0xD, 500)
    OP_74(0x0, 0x1E)

    def lambda_4361():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4361)

    label("loc_4371")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_441A")
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x3C, 0x44, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    Sound(902, 0, 50, 0)
    Sound(833, 0, 50, 0)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x45, 0x49, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x4A, 0x58, 0x1, 0x0)
    OP_79(0x0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    Sound(902, 0, 50, 0)
    Sound(833, 0, 50, 0)
    OP_4B(0xFE, 0x1)
    OP_71(0x0, 0x59, 0x5D, 0x1, 0x0)
    OP_79(0x0)
    OP_4C(0xFE, 0x1)
    OP_71(0x0, 0x5E, 0x64, 0x1, 0x0)
    OP_79(0x0)
    Jump("loc_4371")

    label("loc_441A")

    Return()

    # Function_67_4351 end

    def Function_68_441B(): pass

    label("Function_68_441B")

    TurnDirection(0xFE, 0xD, 500)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(357, 0, 80, 0)
    PlayEffect(0x4, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 3, 0, 47)
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_68_441B end

    def Function_69_4481(): pass

    label("Function_69_4481")

    TurnDirection(0xFE, 0xD, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -19550, 100, -29800, 5000, 0x1)

    def lambda_44A9():
        TurnDirection(0xFE, 0xD, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44A9)
    OP_96(0xFE, 0xFFFFA9AC, 0x64, 0xFFFF7B30, 0xFA0, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_69_4481 end

    def Function_70_44D4(): pass

    label("Function_70_44D4")

    TurnDirection(0xFE, 0xD, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 30, 0)
    OP_9D(0xFE, 0xFFFFAE98, 0x64, 0xFFFF80D0, 0x1F4, 0x5DC)
    OP_96(0xFE, 0xFFFFACFE, 0x64, 0xFFFF78E2, 0xFA0, 0x0)
    Sound(540, 0, 30, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_70_44D4 end

    def Function_71_4523(): pass

    label("Function_71_4523")

    Sound(655, 0, 50, 0)
    OP_87(0x6, 0xFF, 0x0, "Null_eyes(74)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    Return()

    # Function_71_4523 end

    SaveToFile()

Try(main)
