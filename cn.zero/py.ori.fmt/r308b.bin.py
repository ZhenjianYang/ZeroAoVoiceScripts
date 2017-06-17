from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r308b.bin",                # FileName
        "r308b",                    # MapName
        "r308b",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -74000, 0, -2000, 0, 0, 1, 101, 0, 1, 0, 2],
    )

    BuildStringList((
        "r308b",                  # 0
        "赛尔盖科长",             # 1
        "蔡特",                   # 2
        "车１",                   # 3
        "阿尔摩利卡古道",         # 4
        "太阳堡垒",               # 5
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-94.0, 0.0, -5.0, 0x0000, 0x0000, "阿尔摩利卡古道")
    PlaceName(68.0, 0.0, -1.0, 0x0000, 0x0000, "太阳堡垒")

    ScpFunction((
        "Function_0_290",          # 00, 0
        "Function_1_2AD",          # 01, 1
        "Function_2_2BD",          # 02, 2
        "Function_3_2CD",          # 03, 3
        "Function_4_162C",         # 04, 4
        "Function_5_16AD",         # 05, 5
    ))


    def Function_0_290(): pass

    label("Function_0_290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2AC")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_0_290")

    label("loc_2AC")

    Return()

    # Function_0_290 end

    def Function_1_2AD(): pass

    label("Function_1_2AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2BC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)

    label("loc_2BC")

    Return()

    # Function_1_2AD end

    def Function_2_2BD(): pass

    label("Function_2_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_2CC")

    Return()

    # Function_2_2BD end

    def Function_3_2CD(): pass

    label("Function_3_2CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02700.itc", 0x1E)
    LoadChrToIndex("chr/ch02702.itc", 0x1F)
    LoadChrToIndex("apl/ch50520.itc", 0x20)
    LoadChrToIndex("apl/ch50521.itc", 0x21)
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_32(0x6, 0x0, 0x26)
    RemoveCraft(0x6, 0xFFFF)
    OP_38(0x6, 0x80, 0x2)
    OP_38(0x6, 0x81, 0x2)
    OP_38(0x6, 0x82, 0x2)
    OP_38(0x6, 0x83, 0x2)
    OP_38(0x6, 0x84, 0x2)
    OP_38(0x6, 0x85, 0x2)
    OP_38(0x6, 0x86, 0x2)
    OP_42(0x6, 0x442, 0xFF)
    OP_42(0x6, 0x5EC, 0xFF)
    OP_42(0x6, 0x650, 0xFF)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    AddCraft(0x6, 0xD5)
    AddCraft(0x6, 0xD6)
    AddCraft(0x6, 0x118)
    SetChrChipPat(0x6, 0x6, 0x118)
    AddCraft(0x6, 0x13E)
    AddCraft(0x6, 0x150)
    OP_42(0x6, 0x87, 0x0)
    OP_42(0x6, 0x6C, 0x1)
    OP_42(0x6, 0x8D, 0x2)
    OP_42(0x6, 0x7E, 0x3)
    OP_42(0x6, 0x66, 0x4)
    OP_42(0x6, 0x6F, 0x5)
    OP_42(0x6, 0x81, 0x6)
    OP_32(0x7, 0x0, 0x26)
    RemoveCraft(0x7, 0xFFFF)
    OP_38(0x7, 0x80, 0x2)
    OP_38(0x7, 0x81, 0x2)
    OP_38(0x7, 0x82, 0x2)
    OP_38(0x7, 0x83, 0x2)
    OP_38(0x7, 0x84, 0x2)
    OP_38(0x7, 0x85, 0x2)
    OP_38(0x7, 0x86, 0x2)
    OP_42(0x7, 0x447, 0xFF)
    OP_42(0x7, 0x5EC, 0xFF)
    OP_42(0x7, 0x650, 0xFF)
    AddCraft(0x7, 0xDC)
    AddCraft(0x7, 0xDD)
    AddCraft(0x7, 0xDE)
    AddCraft(0x7, 0xDF)
    AddCraft(0x7, 0xE0)
    AddCraft(0x7, 0x11D)
    SetChrChipPat(0x7, 0x6, 0x11D)
    AddCraft(0x7, 0x141)
    AddCraft(0x7, 0x150)
    OP_42(0x7, 0x81, 0x0)
    OP_42(0x7, 0x6C, 0x1)
    OP_42(0x7, 0x99, 0x2)
    OP_42(0x7, 0xA3, 0x3)
    OP_42(0x7, 0x7E, 0x4)
    OP_42(0x7, 0x8B, 0x5)
    OP_42(0x7, 0x7B, 0x6)
    OP_68(-70000, 900, 1000, 0)
    MoveCamera(67, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(29000, 0)
    SetChrPos(0x101, -51300, 0, -2500, 90)
    SetChrPos(0x102, -51800, 0, -1500, 90)
    SetChrPos(0x103, -52800, 0, -3300, 90)
    SetChrPos(0x104, -53300, 0, -2300, 90)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrPos(0x107, -29000, 0, -3100, 270)
    SetChrPos(0x108, -28700, 0, -1900, 270)
    SetChrFlags(0x107, 0x80)
    SetChrBattleFlags(0x107, 0x8000)
    SetChrFlags(0x108, 0x80)
    SetChrBattleFlags(0x108, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, -55000, 0, -2900, 90)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, -54000, 250, 1400, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x5, 0xA)
    OP_49()
    SetChrPos(0xA, -84000, 100, 1000, 0)
    OP_D3(0xA, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB5, 0xF0, 0x0, 0x20)
    SetMapObjFlags(0x4, 0x4)
    Sound(485, 0, 100, 0)
    Sleep(300)
    OP_68(-59000, 900, 1000, 5000)
    MoveCamera(67, 17, 0, 5000)
    SetCameraDistance(21000, 5000)

    def lambda_5A7():
        OP_96(0xFE, 0xFFFF2D10, 0x64, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5A7)
    FadeToBright(2000, 0)
    WaitChrThread(0xA, 1)
    ClearMapObjFlags(0x5, 0x20)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    Sleep(500)
    OP_71(0x5, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_79(0x5)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_68(-52000, 1000, -2300, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0xA, -54000, 100, 1500, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    #C0001
    ChrTalk(
        0x101,
        (
            "#0013F#5P古战场……\x01",
            "……莫非这里就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        (
            "#0101F#5P『教团』残党所潜伏的\x01",
            "据点……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x107, 0x80)
    ClearChrBattleFlags(0x107, 0x8000)
    Sleep(300)
    #Sound(1708, 255, 100, 0)    #voice#Estelle
    Sleep(150)

    #N0003
    NpcTalk(
        0x107,
        "女孩的声音",
        "#8A你们来了啊……！\x02",
    )
    #Auto

    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_68(-50200, 900, -2300, 3500)
    MoveCamera(40, 23, 0, 3500)
    SetCameraDistance(17000, 3500)
    ClearChrFlags(0x108, 0x80)
    ClearChrBattleFlags(0x108, 0x8000)

    def lambda_7A2():
        OP_96(0xFE, 0xFFFF3FD0, 0x0, 0xFFFFF3E4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7A2)
    Sleep(200)

    def lambda_7BF():
        OP_96(0xFE, 0xFFFF40FC, 0x0, 0xFFFFF894, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7BF)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    OP_6F(0x79)

    #C0004
    ChrTalk(
        0x101,
        "#6P#0002F艾丝蒂尔、约修亚！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#6P#0300F哟……！\x01",
            "辛苦了！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x108,
        (
            "#0903F#11P你们才是……\x01",
            "好像经历了一番苦战呢。\x02\x03",

            "#0900F事情的详细情况，我们刚才已经在与\x01",
            "亚里欧斯先生的通讯中得知了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x107,
        (
            "#11P#0800F我们也是刚刚才\x01",
            "打开那里的入口的。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#6P#0205F啊……\x02",
    )

    CloseMessageWindow()
    OP_68(-24000, 3000, -2000, 3000)
    MoveCamera(75, 5, 0, 3000)
    SetCameraDistance(26500, 3000)

    def lambda_907():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_907)
    Sleep(100)

    def lambda_917():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_917)
    OP_6F(0x79)

    #C0009
    ChrTalk(
        0x103,
        "#0201F原本紧紧关闭的门……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0010
    ChrTalk(
        0x107,
        (
            "#0806F这道门设置了奇怪的机关，\x01",
            "我们费了好一番周折才把它打开。\x02\x03",

            "#0800F这样一来，就能潜入\x01",
            "那些家伙的据点了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-50200, 900, -2300, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Sleep(300)

    #C0011
    ChrTalk(
        0x101,
        (
            "#6P#0004F……真是帮大忙了。\x02\x03",

            "#0001F我们准备继续前进，\x01",
            "直接去逮捕主谋……\x02\x03",

            "你们有何打算？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A4F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A4F)
    Sleep(50)

    def lambda_A5F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A5F)
    Sleep(300)

    #C0012
    ChrTalk(
        0x107,
        (
            "#11P#0809F当然是帮忙了！\x02\x03",

            "#0800F我们就是为了这个才等在这里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x108,
        (
            "#0900F#11P而且还需要救出失踪者，\x01",
            "我们当然要帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#6P#0004F……谢谢。有你们相助的话，\x01",
            "真是胜过百人之力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    StopBGM(0xFA0)

    #C0015
    ChrTalk(
        0x101,
        (
            "#6P#0001F──对了，\x01",
            "有条传言是给你们的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将玲在医院研究楼所说的话转告给了两人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7001", 0)

    #C0017
    ChrTalk(
        0x108,
        "#0908F#11P是吗……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x107,
        "#11P#0808F……果然……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0103F#6P给你们捉住玲的\x01",
            "最后机会……\x02\x03",

            "#0101F到底，是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x107,
        (
            "#11P#0804F嗯……\x02\x03",

            "#0800F──我觉得，玲大概是在\x01",
            "试探我们能不能接受\x01",
            "她的全部吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x108,
        (
            "#0903F#11P因此，我们也\x01",
            "必须向发生在那个孩子身上的\x01",
            "悲剧的始作俑者之一……\x02\x03",

            "#0901F向『他』问出\x01",
            "全部真相。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#6P#0001F是吗……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#6P#0206F……我也想\x01",
            "正式询问一下那个人。\x02\x03",

            "#0208F为什么……要进行那种实验……\x02\x03",

            "为什么要逃到这座城市来\x01",
            "完成『真知』……\x02\x03",

            "#0201F还有琪雅的真正身份，\x01",
            "以及他打算对她做些什么……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DFC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DFC)
    Sleep(100)

    def lambda_E0C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E0C)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0024
    ChrTalk(
        0x102,
        "#0101F#5P是啊……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#5P#0303F看样子，无论如何，\x01",
            "我们也必须要把那家伙抓住啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#11P#0003F是啊……一定要将他逮捕。\x02\x03",

            "#0013F这也是为了解放被操纵的警备队，\x01",
            "以及保证琪雅的安全。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0027
    NpcTalk(
        0x8,
        "男性的声音",
        "#40W……要走了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F77():

        label("loc_F77")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F77")

    QueueWorkItem2(0x101, 2, lambda_F77)
    Sleep(50)

    def lambda_F8C():

        label("loc_F8C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F8C")

    QueueWorkItem2(0x102, 2, lambda_F8C)
    Sleep(50)

    def lambda_FA1():

        label("loc_FA1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FA1")

    QueueWorkItem2(0x103, 2, lambda_FA1)
    Sleep(50)

    def lambda_FB6():

        label("loc_FB6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FB6")

    QueueWorkItem2(0x104, 2, lambda_FB6)

    def lambda_FC8():

        label("loc_FC8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FC8")

    QueueWorkItem2(0x9, 2, lambda_FC8)
    OP_68(-52700, 1000, -1000, 2500)
    MoveCamera(47, 25, 0, 2500)
    SetCameraDistance(16500, 2500)
    BeginChrThread(0x8, 3, 0, 4)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)

    #C0028
    ChrTalk(
        0x101,
        "#0005F#11P科长……！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#11P#0101F您刚刚才接受过止血包扎，\x01",
            "请不要乱动……！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#5P#1002F#30W呵呵，我可没打算拖着\x01",
            "这条伤腿跟你们去啊……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 5)
    WaitChrThread(0x8, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x9, 0x2)

    #C0031
    ChrTalk(
        0x8,
        (
            "#1004F#5P#30W……但是，至少让我\x01",
            "在这里目送你们吧。\x02\x03",

            "就让我目送一下……\x01",
            "就要变得能够独当一面的部下们吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0008F#11P科长……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#12P#0306F真是的……\x01",
            "耍帅耍过头了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#1002F#5P#30W呵呵……这可是\x01",
            "大叔的特权啊。\x02\x03",

            "#1003F──罗伊德、艾莉、\x01",
            "缇欧、兰迪……\x02\x03",

            "上任四个月多一点……\x01",
            "你们也成长了不少。\x02\x03",

            "如果你们能顺利了结这件案子，\x01",
            "我就正式承认你们已经能独当一面了。\x02\x03",

            "#1001F所以……\x01",
            "绝对要平安无事地回来！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#0001F#11P是……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#11P#0100F知道了！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        "#12P#0202F……了解……！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#12P#0309F是！长官！\x02",
    )

    CloseMessageWindow()
    OP_E5()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    OP_6F(0x10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)
    ReplaceBGM("ed7510", "ed7305")
    Sleep(1600)
    OP_68(-29000, 1000, -2000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20000, 0)
    OP_90(0x101, -40000, 0, -2000, 90)
    OP_90(0x102, -41300, 0, -2900, 90)
    OP_90(0x103, -41700, 0, -1500, 90)
    OP_90(0x104, -40600, 0, -900, 90)
    OP_90(0x107, -43500, 0, -2500, 90)
    OP_90(0x108, -44000, 0, -1500, 90)
    OP_90(0x9, -53400, 0, -2300, 90)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x8, 0x1)

    def lambda_13A9():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A9)
    Sleep(50)

    def lambda_13C1():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13C1)
    Sleep(50)

    def lambda_13D9():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13D9)
    Sleep(50)

    def lambda_13F1():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13F1)
    Sleep(50)

    def lambda_1409():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1409)
    Sleep(50)

    def lambda_1421():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1421)
    SetCameraDistance(17000, 4000)
    FadeToBright(2000, 0)
    OP_6F(0x10)
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x103, 0xFF)
    OP_4B(0x104, 0xFF)
    OP_4B(0x107, 0xFF)
    OP_4B(0x108, 0xFF)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x107, 0x80)
    SetChrBattleFlags(0x107, 0x8000)
    SetChrFlags(0x108, 0x80)
    SetChrBattleFlags(0x108, 0x8000)
    Fade(500)
    OP_68(-53500, 2000, -1800, 0)
    MoveCamera(63, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    OP_68(-53500, 1300, -1800, 5000)
    OP_6F(0x1)
    OP_4C(0x101, 0xFF)
    OP_4C(0x102, 0xFF)
    OP_4C(0x103, 0xFF)
    OP_4C(0x104, 0xFF)
    OP_4C(0x107, 0xFF)
    OP_4C(0x108, 0xFF)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x107, 0x80)
    ClearChrBattleFlags(0x107, 0x8000)
    ClearChrFlags(0x108, 0x80)
    ClearChrBattleFlags(0x108, 0x8000)
    PlaceName2(340, 200, "c_plac30", 0x0, 2500)
    Fade(500)
    OP_68(-7500, 6200, -2000, 0)
    MoveCamera(50, 40, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(12500, 17200, -2000, 6000)
    MoveCamera(60, 15, 0, 6000)
    SetCameraDistance(25000, 6000)
    OP_6F(0x79)
    Sleep(2000)
    Fade(500)
    OP_68(38500, 21000, -2000, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(30000, 0)
    OP_68(51500, 21000, -2000, 4000)
    MoveCamera(60, 27, 0, 4000)
    SetCameraDistance(17000, 4000)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x107, 0xFF)
    EndChrThread(0x108, 0xFF)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("m3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2CD end

    def Function_4_162C(): pass

    label("Function_4_162C")

    BeginChrThread(0x8, 0, 0, 0)

    def lambda_1637():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1637)

    def lambda_1648():
        OP_96(0xFE, 0xFFFF2D10, 0xFA, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1648)
    WaitChrThread(0x8, 1)

    def lambda_1666():
        OP_96(0xFE, 0xFFFF2D10, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1666)
    WaitChrThread(0x8, 1)

    def lambda_1684():
        OP_96(0xFE, 0xFFFF2D10, 0x0, 0xFFFFFCE0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1684)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x8, 0x101, 500)
    Return()

    # Function_4_162C end

    def Function_5_16AD(): pass

    label("Function_5_16AD")

    OP_92(0x8, 0xFFFF3224, 0xFFFFFCE0, 0x1F4)
    BeginChrThread(0x8, 0, 0, 0)

    def lambda_16C5():
        OP_96(0xFE, 0xFFFF3224, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16C5)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    Return()

    # Function_5_16AD end

    SaveToFile()

Try(main)
