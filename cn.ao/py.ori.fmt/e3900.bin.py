from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3900.bin",                # FileName
        "e3900",                    # MapName
        "e3900",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3900",                  # 0
        "战鬼西格蒙德",           # 1
        "飞艇",                   # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(220, 0)                                        # 0

    ScpFunction((
        "Function_0_DC",           # 00, 0
        "Function_1_EC",           # 01, 1
        "Function_2_ED",           # 02, 2
        "Function_3_658",          # 03, 3
    ))


    def Function_0_DC(): pass

    label("Function_0_DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_EB")

    Return()

    # Function_0_DC end

    def Function_1_EC(): pass

    label("Function_1_EC")

    Return()

    # Function_1_EC end

    def Function_2_ED(): pass

    label("Function_2_ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03350.itc", 0x1E)
    LoadChrToIndex("chr/ch00056.itc", 0x1F)
    LoadChrToIndex("chr/ch00156.itc", 0x20)
    LoadChrToIndex("chr/ch00256.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch0295F.itc", 0x23)
    LoadChrToIndex("chr/ch0305F.itc", 0x24)
    LoadChrToIndex("chr/ch03351.itc", 0x25)
    LoadEffect(0x0, "event/ev17087.eff")
    SoundLoad(825)
    SoundLoad(868)
    SoundLoad(489)
    SoundLoad(3839)
    SoundLoad(4114)
    SoundLoad(2755)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -200, -25000, 180)
    SetChrFlags(0x8, 0x800)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x0)
    OP_90(0x101, 1100, -1000, -33000, 0)
    OP_90(0x102, -1100, -1000, -33000, 0)
    OP_90(0x103, 2000, -1000, -34000, 0)
    OP_90(0x104, 0, -1000, -31700, 0)
    OP_90(0x109, -2000, -1000, -34000, 0)
    OP_90(0x105, 0, -1000, -34500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x14)
    SetMapObjFlags(0x1, 0x1000)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x2, 0x9)
    OP_49()
    SetChrPos(0x9, 120000, 20000, 10000, 0)
    OP_D5(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_71(0x2, 0x65, 0x82, 0x0, 0x20)
    OP_68(0, 5900, -27700, 0)
    MoveCamera(0, -13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    Sound(825, 2, 100, 0)
    Sound(868, 2, 100, 0)
    OP_68(0, 2000, -27700, 6000)
    MoveCamera(0, -8, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(9600, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2000)
    OP_C9(0x0, 0x80000000)
    #Sound(2182, 255, 100, 0)    #voice#Elie

    #C0001
    ChrTalk(
        0x102,
        "#6P#N#00106F#12A呀啊啊啊……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    #Sound(2223, 255, 100, 0)    #voice#Tio

    #C0002
    ChrTalk(
        0x103,
        "#12P#N#00210F#12A唔……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    #Sound(3322, 255, 100, 0)    #voice#Lloyd

    #C0003
    ChrTalk(
        0x101,
        "#12P#N#00010F#16A竟、竟然做出这种事……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    Sleep(500)
    OP_82(0xC8, 0xC8, 0xBB8, 0x1F4)

    #C0004
    ChrTalk(
        0x104,
        "#6P#00307F#4S#N#2755V#30W#17A叔叔！！！！！！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #C0005
    ChrTalk(
        0x8,
        "#04502F#3839V#15A哼哼哼……\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(800)
    OP_82(0x12C, 0x12C, 0xBB8, 0x3E8)

    #C0006
    ChrTalk(
        0x8,
        "#04509F#4114V#5S#40A哈──哈哈哈哈哈哈哈哈！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(30000, 7900, -25000, 0)
    MoveCamera(70, -10, 10, 0)
    OP_6E(850, 0)
    SetCameraDistance(20000, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x8, 0, 0, -25000, 180)
    ClearChrFlags(0x8, 0x800)
    OP_68(0, 4900, -25000, 5500)
    MoveCamera(30, -10, 0, 5500)
    SetCameraDistance(30000, 5500)
    BlurSwitch(0x157C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(489, 0, 100, 0)
    OP_87(0x0, 0x0, 0x2, "Null_burn_l", 0x7, 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    OP_87(0x0, 0x1, 0x2, "Null_burn_r", 0x7, 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(2700)
    Sound(499, 0, 100, 0)
    SetChrChip(0x0, 0x8, 0x1E, 0xC8)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_5B6():
        OP_9D(0xFE, 0x0, 0xFA0, 0xFFFF9E58, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B6)
    WaitChrThread(0x8, 1)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    SetChrFlags(0x8, 0x8)

    def lambda_5E4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E4)
    OP_6F(0x79)
    StopSound(825, 1000, 100)
    StopSound(868, 1000, 100)
    CancelBlur(0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_03b.pmf", 0x227, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    SetScenarioFlags(0x22, 2)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_ED end

    def Function_3_658(): pass

    label("Function_3_658")

    OP_9F(0x0, 0x9)
    OP_9F(0x1, 0, 2000, -30000)
    OP_9F(0x1, -120000, 20000, 10000)
    OP_9F(0x2, 0x9, 35000, 0x6)
    Return()

    # Function_3_658 end

    SaveToFile()

Try(main)
