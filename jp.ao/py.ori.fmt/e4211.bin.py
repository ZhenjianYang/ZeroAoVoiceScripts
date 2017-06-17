from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "国防軍兵士",             # 1
        "国防軍兵士",             # 2
        "エステル",               # 3
        "ヨシュア",               # 4
        "レン",                   # 5
        "アイオーン３",           # 6
        "パテルマテル",           # 7
        "台詞表示用ダミーキャラ", # 8
        "国防軍兵士",             # 9
        "国防軍兵士",             # 10
        "国防軍兵士",             # 11
        "空",                     # 12
        "フェンス",               # 13
        "フェンス",               # 14
        "フェンス",               # 15
        "バリケード",             # 16
        "SE制御",                 # 17
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
        "Function_4_89A",          # 04, 4
        "Function_5_8B6",          # 05, 5
        "Function_6_8D2",          # 06, 6
        "Function_7_92C",          # 07, 7
        "Function_8_A63",          # 08, 8
        "Function_9_A8A",          # 09, 9
        "Function_10_AB1",         # 0A, 10
        "Function_11_BE3",         # 0B, 11
        "Function_12_C40",         # 0C, 12
        "Function_13_EBC",         # 0D, 13
        "Function_14_26B0",        # 0E, 14
        "Function_15_276F",        # 0F, 15
        "Function_16_2783",        # 10, 16
        "Function_17_27E2",        # 11, 17
        "Function_18_2816",        # 12, 18
        "Function_19_28B4",        # 13, 19
        "Function_20_29B8",        # 14, 20
        "Function_21_2A27",        # 15, 21
        "Function_22_2AA6",        # 16, 22
        "Function_23_2ABF",        # 17, 23
        "Function_24_2B12",        # 18, 24
        "Function_25_2B77",        # 19, 25
        "Function_26_2BDC",        # 1A, 26
        "Function_27_2C39",        # 1B, 27
        "Function_28_2C7C",        # 1C, 28
        "Function_29_2CCE",        # 1D, 29
        "Function_30_2CCF",        # 1E, 30
        "Function_31_2D5C",        # 1F, 31
        "Function_32_2DA8",        # 20, 32
        "Function_33_2E4B",        # 21, 33
        "Function_34_2F40",        # 22, 34
        "Function_35_312A",        # 23, 35
        "Function_36_312B",        # 24, 36
        "Function_37_3156",        # 25, 37
        "Function_38_318A",        # 26, 38
        "Function_39_31D0",        # 27, 39
        "Function_40_3230",        # 28, 40
        "Function_41_327C",        # 29, 41
        "Function_42_32C6",        # 2A, 42
        "Function_43_3309",        # 2B, 43
        "Function_44_3387",        # 2C, 44
        "Function_45_340D",        # 2D, 45
        "Function_46_340E",        # 2E, 46
        "Function_47_348C",        # 2F, 47
        "Function_48_34A6",        # 30, 48
        "Function_49_34B8",        # 31, 49
        "Function_50_354C",        # 32, 50
        "Function_51_35DD",        # 33, 51
        "Function_52_35F3",        # 34, 52
        "Function_53_35FF",        # 35, 53
        "Function_54_360B",        # 36, 54
        "Function_55_36CB",        # 37, 55
        "Function_56_376B",        # 38, 56
        "Function_57_37A8",        # 39, 57
        "Function_58_3863",        # 3A, 58
        "Function_59_39E7",        # 3B, 59
        "Function_60_3A94",        # 3C, 60
        "Function_61_3F9F",        # 3D, 61
        "Function_62_4262",        # 3E, 62
        "Function_63_42AD",        # 3F, 63
        "Function_64_430F",        # 40, 64
        "Function_65_437E",        # 41, 65
        "Function_66_43ED",        # 42, 66
        "Function_67_4413",        # 43, 67
        "Function_68_44DD",        # 44, 68
        "Function_69_4543",        # 45, 69
        "Function_70_4596",        # 46, 70
        "Function_71_45E5",        # 47, 71
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
            "#5P……北口と東口では\x01",
            "戦闘が始まったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    #C0002
    ChrTalk(
        0x9,
        "#11Pなあ……ヤバくないか？\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "#11Pこれでソーニャ司令の部隊が\x01",
            "こっちに攻めてきたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#5Pだ、大丈夫だろう。\x01",
            "政治的な問題が決着するまで\x01",
            "静観するって話みたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#5Pとにかく、ケリが付くまで\x01",
            "俺たちはただ待ってりゃいいさ。\x02",
        )
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0xF,
        "少女の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1P#Nうふふ……\x01",
            "そんな日和見さんな考えで\x01",
            "いいのかしら？\x07\x00\x02",
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
        "#5Pな、なんだ……？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "#11Pこの音……どこかで……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_893")
    FadeToDark(1000, 0, -1)
    Sleep(500)
    StopSound(825, 500, 100)
    StopSound(993, 500, 100)
    OP_0D()
    SetScenarioFlags(0x24, 4)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Jump("loc_899")

    label("loc_893")

    Call(0, 7)
    Call(0, 13)

    label("loc_899")

    Return()

    # Function_3_3D2 end

    def Function_4_89A(): pass

    label("Function_4_89A")

    OP_93(0xFE, 0x140, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x82, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_4_89A end

    def Function_5_8B6(): pass

    label("Function_5_8B6")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_5_8B6 end

    def Function_6_8D2(): pass

    label("Function_6_8D2")

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

    # Function_6_8D2 end

    def Function_7_92C(): pass

    label("Function_7_92C")

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

    # Function_7_92C end

    def Function_8_A63(): pass

    label("Function_8_A63")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xC5, 0xEE, 0xFE, 0xC8, 0x514, 0x0)
    Return()

    # Function_8_A63 end

    def Function_9_A8A(): pass

    label("Function_9_A8A")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0xD0, 0xD0, 0xFF, 0x1E, 0x96, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF000000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x190)
    Return()

    # Function_9_A8A end

    def Function_10_AB1(): pass

    label("Function_10_AB1")

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

    # Function_10_AB1 end

    def Function_11_BE3(): pass

    label("Function_11_BE3")

    OP_8A(0x0)
    OP_8A(0x1)
    OP_8A(0x3)
    OP_8A(0x8)
    LoadEffect(0x0, "battle/cr006300.eff")
    LoadEffect(0x1, "battle/cr007100.eff")
    LoadEffect(0x3, "event/ev10017.eff")
    LoadEffect(0x8, "event/ev17107.eff")
    Return()

    # Function_11_BE3 end

    def Function_12_C40(): pass

    label("Function_12_C40")

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

    # Function_12_C40 end

    def Function_13_EBC(): pass

    label("Function_13_EBC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDC")
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 10)

    label("loc_EDC")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CD")
    Sound(994, 0, 100, 0)
    FadeToBright(1000, 0)
    Jump("loc_11D2")

    label("loc_11CD")

    Fade(500)

    label("loc_11D2")

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
        "#5P#4Sなああああっ！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0)

    #C0010
    ChrTalk(
        0x8,
        "#5P#4S赤い《神機#4Rアイオーン#》……！？\x02",
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
            "クスクス……御機嫌よう。\x02\x03",

            "でも、この《パテル＝マテル》を\x01",
            "あんな人形さんたちと一緒にしないで。\x02\x03",

            "遥かに格好よくって、アタマがよくて、\x01",
            "頼りになるんだから。\x02",
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
        "#11Pま、まさか……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        "#11Pて、敵なのか……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        (
            "#03304F#5Pうふふ、兵士さんたちは\x01",
            "どうでもいいけど。\x02\x03",

            "#03300F踏み潰されたくなかったら\x01",
            "下がっているといいわ。\x02\x03",

            "#03302F──ほら、来たわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "#11Pえ……\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1598")
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

    label("loc_1598")

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
        "#11P#4Sうわあっ！？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        "#11P#4S青色の《神機#4Rアイオーン#》……！\x02",
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
        "#03302F#5Pうふふ……来たわね。\x02",
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

    def lambda_17AF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17AF)

    def lambda_17BC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_17BC)
    Sleep(300)

    #C0019
    ChrTalk(
        0xA,
        (
            "#00807F#12Pあなたたち！\x01",
            "いいから下がりなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "#00907F#6Pその程度の戦力で\x01",
            "介入できる勝負じゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "#5Pううっ……！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        "#11Pて、鉄橋まで下がるぞ！\x02",
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

    def lambda_18C5():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_18C5)
    Sleep(50)

    def lambda_18D5():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18D5)
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
            "#00808F#6Pレン……無茶しないで。\x02\x03",

            "#00801Fあたしたちも全力で援護するから。\x02",
        )
    )

    Call(0, 11)
    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "#00903F#12Pパテル＝マテルも強化されたけど\x01",
            "それでもパワーはあちらが上だ。\x02\x03",

            "#00901F翻弄しつつ勝機を見出すしかない！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xC,
        (
            "#03303F#5Pうん、分かってる。\x02\x03",

            "#03308F──これ以上、\x01",
            "あの人たちが暮らす地を\x01",
            "勝手にはさせない……\x02\x03",

            "#03307F行きましょう！\x01",
            "エステル、ヨシュア！\x01",
            "《パテル＝マテル》！\x02",
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

    label("loc_1E22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E39")
    Sleep(50)
    Jump("loc_1E22")

    label("loc_1E39")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D8")
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    Call(0, 8)
    SetChrPos(0x13, 0, 0, 0, 0)
    Jump("loc_20D8")

    label("loc_20D8")

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

    label("loc_2129")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2140")
    Sleep(50)
    Jump("loc_2129")

    label("loc_2140")

    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2187")
    OP_68(-26050, 2300, -30050, 700)
    MoveCamera(323, 1, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(16180, 700)
    Jump("loc_21B5")

    label("loc_2187")

    OP_68(-24870, 2900, -26210, 700)
    MoveCamera(329, 29, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(13680, 700)

    label("loc_21B5")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2297")
    ClearMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    Call(0, 9)
    Jump("loc_2297")

    label("loc_2297")

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

    # Function_13_EBC end

    def Function_14_26B0(): pass

    label("Function_14_26B0")

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

    # Function_14_26B0 end

    def Function_15_276F(): pass

    label("Function_15_276F")

    Sleep(1150)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x17D, 0x1A4, 0x1, 0x20)
    Return()

    # Function_15_276F end

    def Function_16_2783(): pass

    label("Function_16_2783")

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

    # Function_16_2783 end

    def Function_17_27E2(): pass

    label("Function_17_27E2")

    SetChrPos(0xFE, 45000, 55000, -27500, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    OP_9F(0x1, -2000, 10000, -27500)
    OP_9F(0x2, 0xFE, 42000, 0x0)
    Return()

    # Function_17_27E2 end

    def Function_18_2816(): pass

    label("Function_18_2816")

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

    # Function_18_2816 end

    def Function_19_28B4(): pass

    label("Function_19_28B4")

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

    # Function_19_28B4 end

    def Function_20_29B8(): pass

    label("Function_20_29B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A26")
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
    Jump("Function_20_29B8")

    label("loc_2A26")

    Return()

    # Function_20_29B8 end

    def Function_21_2A27(): pass

    label("Function_21_2A27")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2AA5")
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
    Jump("Function_21_2A27")

    label("loc_2AA5")

    Return()

    # Function_21_2A27 end

    def Function_22_2AA6(): pass

    label("Function_22_2AA6")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)
    Return()

    # Function_22_2AA6 end

    def Function_23_2ABF(): pass

    label("Function_23_2ABF")

    OP_93(0xFE, 0x2D, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x3C8C, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0xFA0, 0x1388, 0x1)

    def lambda_2AED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AED)
    OP_9B(0x0, 0xFE, 0x2D, 0xBB8, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_2ABF end

    def Function_24_2B12(): pass

    label("Function_24_2B12")

    Sleep(200)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x3C8C, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x128E, 0x1388, 0x1)

    def lambda_2B52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B52)
    OP_9B(0x0, 0xFE, 0x2D, 0xBB8, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_2B12 end

    def Function_25_2B77(): pass

    label("Function_25_2B77")

    Sleep(400)
    OP_93(0xFE, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x1068, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0xBB8, 0x1388, 0x1)

    def lambda_2BB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BB7)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1388, 0x1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_2B77 end

    def Function_26_2BDC(): pass

    label("Function_26_2BDC")

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

    # Function_26_2BDC end

    def Function_27_2C39(): pass

    label("Function_27_2C39")


    def lambda_2C3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C3E)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -18500, 0, -33500, 6000, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_27_2C39 end

    def Function_28_2C7C(): pass

    label("Function_28_2C7C")


    def lambda_2C81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C81)
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

    # Function_28_2C7C end

    def Function_29_2CCE(): pass

    label("Function_29_2CCE")

    Return()

    # Function_29_2CCE end

    def Function_30_2CCF(): pass

    label("Function_30_2CCF")

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

    # Function_30_2CCF end

    def Function_31_2D5C(): pass

    label("Function_31_2D5C")

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

    # Function_31_2D5C end

    def Function_32_2DA8(): pass

    label("Function_32_2DA8")

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

    # Function_32_2DA8 end

    def Function_33_2E4B(): pass

    label("Function_33_2E4B")

    Sound(114, 0, 100, 0)

    def lambda_2E56():
        OP_96(0xFE, 0xFFFFBD98, 0x15E, 0xFFFF8FB2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2E56)

    def lambda_2E70():
        OP_D5(0xFE, 0x0, 0x2710, 0x14C08, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2E70)
    Sleep(100)

    def lambda_2E8C():
        OP_96(0xFE, 0xFFFFC568, 0x32, 0xFFFF75FE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E8C)

    def lambda_2EA6():
        OP_D5(0xFE, 0x14FF0, 0x41EB0, 0x2710, 0x2BC)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2EA6)
    Sleep(50)
    Sound(1018, 0, 100, 0)

    def lambda_2EC8():
        OP_96(0xFE, 0xFFFFC568, 0x64, 0xFFFFAE3E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2EC8)

    def lambda_2EE2():
        OP_D5(0xFE, 0x14FF0, 0x41EB0, 0xFFFFD8F0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2EE2)
    Sleep(50)

    def lambda_2EFE():
        OP_D5(0xFE, 0x80E8, 0x445C0, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2EFE)
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

    # Function_33_2E4B end

    def Function_34_2F40(): pass

    label("Function_34_2F40")

    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2F63():
        TurnDirection(0xFE, 0xE, 20)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F63)
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

    # Function_34_2F40 end

    def Function_35_312A(): pass

    label("Function_35_312A")

    Return()

    # Function_35_312A end

    def Function_36_312B(): pass

    label("Function_36_312B")

    Sleep(2400)
    BeginChrThread(0xFE, 1, 0, 38)
    Sleep(200)
    OP_96(0xFE, 0xFFFF9A70, 0x0, 0xFFFFB5C8, 0x1B58, 0x1)
    Sleep(500)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    Return()

    # Function_36_312B end

    def Function_37_3156(): pass

    label("Function_37_3156")

    OP_9D(0xFE, 0xFFFF8AD0, 0x0, 0xFFFF9E58, 0x2EE, 0x3E8)
    Sound(902, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0xFE, 1, 0, 39)
    Sleep(200)
    EndChrThread(0xD, 0x0)
    BeginChrThread(0xD, 0, 0, 34)
    Return()

    # Function_37_3156 end

    def Function_38_318A(): pass

    label("Function_38_318A")

    OP_D5(0xFE, 0x0, 0x20F58, 0x0, 0x190)
    OP_74(0x0, 0xC)
    OP_71(0x0, 0xDD, 0xF0, 0x1, 0x0)
    OP_79(0x0)
    OP_D5(0xFE, 0x0, 0x27100, 0x0, 0xC8)
    OP_71(0x0, 0x2EE, 0x302, 0x1, 0x0)
    Return()

    # Function_38_318A end

    def Function_39_31D0(): pass

    label("Function_39_31D0")


    def lambda_31D5():
        OP_D5(0xFE, 0x0, 0x15F90, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31D5)
    Sound(905, 0, 100, 0)
    Sound(576, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x302, 0x306, 0x1, 0x0)
    OP_79(0x0)

    label("loc_3208")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_321F")
    Sleep(50)
    Jump("loc_3208")

    label("loc_321F")

    OP_71(0x0, 0x306, 0x316, 0x1, 0x0)
    WaitChrThread(0xFE, 3)
    Return()

    # Function_39_31D0 end

    def Function_40_3230(): pass

    label("Function_40_3230")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFA240, 0x64, 0xFFFF6F78, 0x3E8, 0x5DC)
    Sound(326, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)

    def lambda_326E():

        label("loc_326E")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_326E")

    QueueWorkItem2(0xFE, 2, lambda_326E)
    Return()

    # Function_40_3230 end

    def Function_41_327C(): pass

    label("Function_41_327C")

    Sleep(3000)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xFFFFAC04, 0x0, 0xFFFF7072, 0x3E8, 0x5DC)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)

    def lambda_32B8():

        label("loc_32B8")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_32B8")

    QueueWorkItem2(0xFE, 2, lambda_32B8)
    Return()

    # Function_41_327C end

    def Function_42_32C6(): pass

    label("Function_42_32C6")

    Sleep(3000)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xFFFFA628, 0x0, 0xFFFF7842, 0x3E8, 0x5DC)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)

    def lambda_32FB():

        label("loc_32FB")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_32FB")

    QueueWorkItem2(0xFE, 2, lambda_32FB)
    Return()

    # Function_42_32C6 end

    def Function_43_3309(): pass

    label("Function_43_3309")

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

    # Function_43_3309 end

    def Function_44_3387(): pass

    label("Function_44_3387")


    def lambda_338C():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_338C)

    label("loc_3394")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33AB")
    Sleep(50)
    Jump("loc_3394")

    label("loc_33AB")

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

    # Function_44_3387 end

    def Function_45_340D(): pass

    label("Function_45_340D")

    Return()

    # Function_45_340D end

    def Function_46_340E(): pass

    label("Function_46_340E")

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

    # Function_46_340E end

    def Function_47_348C(): pass

    label("Function_47_348C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34A5")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_47_348C")

    label("loc_34A5")

    Return()

    # Function_47_348C end

    def Function_48_34A6(): pass

    label("Function_48_34A6")

    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(802, 0, 100, 0)
    Return()

    # Function_48_34A6 end

    def Function_49_34B8(): pass

    label("Function_49_34B8")

    Sleep(300)
    TurnDirection(0xFE, 0xD, 500)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFADF8, 0x0, 0xFFFF6D20, 0xFA0, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    label("loc_34EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3503")
    Sleep(50)
    Jump("loc_34EC")

    label("loc_3503")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    OP_9B(0x0, 0xFE, 0x4, 0x3E8, 0x1F40, 0x1)
    OP_9D(0xFE, 0xFFFFB87A, 0x1F4, 0xFFFF6F5A, 0x258, 0x3E8)
    OP_9D(0xFE, 0xFFFFCB94, 0x0, 0xFFFF736A, 0xC8, 0x3E8)
    Return()

    # Function_49_34B8 end

    def Function_50_354C(): pass

    label("Function_50_354C")

    Sleep(400)
    TurnDirection(0xFE, 0xD, 500)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFADF8, 0x0, 0xFFFF7428, 0xFA0, 0x0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    label("loc_3580")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3597")
    Sleep(50)
    Jump("loc_3580")

    label("loc_3597")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x164, 0x3E8, 0x1F40, 0x1)
    OP_9D(0xFE, 0xFFFFB88E, 0x1F4, 0xFFFF7608, 0x258, 0x3E8)
    OP_9D(0xFE, 0xFFFFCBC6, 0x0, 0xFFFF796E, 0xC8, 0x3E8)
    Return()

    # Function_50_354C end

    def Function_51_35DD(): pass

    label("Function_51_35DD")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    TurnDirection(0xFE, 0xD, 500)
    Return()

    # Function_51_35DD end

    def Function_52_35F3(): pass

    label("Function_52_35F3")

    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_52_35F3 end

    def Function_53_35FF(): pass

    label("Function_53_35FF")

    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_53_35FF end

    def Function_54_360B(): pass

    label("Function_54_360B")

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

    # Function_54_360B end

    def Function_55_36CB(): pass

    label("Function_55_36CB")

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

    # Function_55_36CB end

    def Function_56_376B(): pass

    label("Function_56_376B")

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

    # Function_56_376B end

    def Function_57_37A8(): pass

    label("Function_57_37A8")

    Sleep(250)
    Sound(534, 0, 100, 0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_57_37A8 end

    def Function_58_3863(): pass

    label("Function_58_3863")

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

    # Function_58_3863 end

    def Function_59_39E7(): pass

    label("Function_59_39E7")

    OP_95(0xFE, -5740, 100, -36860, 7000, 0x1)
    OP_95(0xFE, -5100, 0, -30220, 7000, 0x1)
    Sound(809, 0, 70, 0)
    OP_9D(0xFE, 0xFFFFEB56, 0x2BC, 0xFFFF91A6, 0x2EE, 0x5DC)
    Sound(326, 0, 60, 0)
    BeginChrThread(0xFE, 3, 0, 57)

    def lambda_3A3D():
        OP_93(0xFE, 0xF0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A3D)
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

    # Function_59_39E7 end

    def Function_60_3A94(): pass

    label("Function_60_3A94")

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

    # Function_60_3A94 end

    def Function_61_3F9F(): pass

    label("Function_61_3F9F")

    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD332, 0x32, 0xFFFF7DBA, 0x5DC, 0x7D0)
    Sound(326, 0, 70, 0)

    def lambda_3FC7():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FC7)
    OP_96(0xFE, 0xFFFFD292, 0x0, 0xFFFF7A90, 0x1B58, 0x1)
    Sound(844, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD6F2, 0x7D0, 0xFFFF7AEA, 0x802, 0xBB8)
    Sound(326, 0, 70, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, -250, 850, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 250, 650, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_4088():
        OP_93(0xFE, 0x22, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4088)
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

    def lambda_412D():
        OP_93(0xFE, 0x22, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_412D)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFDD46, 0x11F8, 0xFFFF89F4, 0x122A, 0x1194)
    Sound(326, 0, 50, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, -500, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_41A3():
        OP_93(0xFE, 0xD7, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41A3)
    Sound(250, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFD45E, 0x19C8, 0xFFFF7838, 0x802, 0xBB8)
    Sound(326, 0, 70, 0)
    Sound(501, 0, 100, 0)
    Sound(511, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x2, 500, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)

    def lambda_4219():
        OP_93(0xFE, 0x78, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4219)
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

    # Function_61_3F9F end

    def Function_62_4262(): pass

    label("Function_62_4262")

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

    # Function_62_4262 end

    def Function_63_42AD(): pass

    label("Function_63_42AD")

    OP_93(0xFE, 0x14A, 0x3C)
    OP_93(0xFE, 0x10E, 0x3C)

    def lambda_42C0():
        OP_93(0xFE, 0x12C, 0x3C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_42C0)
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

    # Function_63_42AD end

    def Function_64_430F(): pass

    label("Function_64_430F")

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

    # Function_64_430F end

    def Function_65_437E(): pass

    label("Function_65_437E")

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

    # Function_65_437E end

    def Function_66_43ED(): pass

    label("Function_66_43ED")

    TurnDirection(0xFE, 0xE, 500)
    Sleep(1500)
    OP_71(0x1, 0xA, 0x32, 0x1, 0x20)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x3E8, 0x1)
    Return()

    # Function_66_43ED end

    def Function_67_4413(): pass

    label("Function_67_4413")

    TurnDirection(0xFE, 0xD, 500)
    OP_74(0x0, 0x1E)

    def lambda_4423():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4423)

    label("loc_4433")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44DC")
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
    Jump("loc_4433")

    label("loc_44DC")

    Return()

    # Function_67_4413 end

    def Function_68_44DD(): pass

    label("Function_68_44DD")

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

    # Function_68_44DD end

    def Function_69_4543(): pass

    label("Function_69_4543")

    TurnDirection(0xFE, 0xD, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -19550, 100, -29800, 5000, 0x1)

    def lambda_456B():
        TurnDirection(0xFE, 0xD, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_456B)
    OP_96(0xFE, 0xFFFFA9AC, 0x64, 0xFFFF7B30, 0xFA0, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_69_4543 end

    def Function_70_4596(): pass

    label("Function_70_4596")

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

    # Function_70_4596 end

    def Function_71_45E5(): pass

    label("Function_71_45E5")

    Sound(655, 0, 50, 0)
    OP_87(0x6, 0xFF, 0x0, "Null_eyes(74)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    Return()

    # Function_71_45E5 end

    SaveToFile()

Try(main)
