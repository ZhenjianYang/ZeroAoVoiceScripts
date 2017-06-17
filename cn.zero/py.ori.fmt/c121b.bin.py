from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c121b.bin",                # FileName
        "c121b",                    # MapName
        "c121b",                    # Location
        0x0021,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 0, 0, 1],
    )

    BuildStringList((
        "c121b",                  # 0
        "曹",                     # 1
        "刘",                     # 2
        "银",                     # 3
        "成员",                   # 4
        "成员",                   # 5
        "SE控制",                 # 6
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_1EC",          # 01, 1
        "Function_2_1ED",          # 02, 2
        "Function_3_DF1",          # 03, 3
        "Function_4_19FF",         # 04, 4
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1DC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_1EB")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1EB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 3)

    label("loc_1EB")

    Return()

    # Function_0_1C8 end

    def Function_1_1EC(): pass

    label("Function_1_1EC")

    Return()

    # Function_1_1EC end

    def Function_2_1ED(): pass

    label("Function_2_1ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06302.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch00500.itc", 0x20)
    OP_68(4450, 900, 130, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 2000, 0, 0, 90)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 7300, 0, 3300, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    LoadEffect(0x0, "event\\ev202_00.eff")
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)

    #C0001
    ChrTalk(
        0x9,
        "#5P──以上就是本周的成果。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            "#5P那些家伙投入使用的军犬\x01",
            "确实是有些威胁性……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "#5P但只要有『银』大人在，应该就能弥补\x01",
            "战力方面的不足了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#11P#3203F嗯，明白了。\x02\x03",

            "#3200F市内的体制仍然保持现状。\x02\x03",

            "至于接下来嘛……\x01",
            "请把派遣到阿尔泰尔市的人员\x01",
            "召回一半吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        "#5P明白了。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "#5P那么，曹先生，\x01",
            "请您早点休息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "#11P#3209F嗯，辛苦你了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    OP_68(2790, 900, 630, 2000)

    def lambda_4C9():
        OP_95(0xFE, -4500, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C9)
    Sleep(3000)
    Sound(103, 0, 100, 0)

    def lambda_4EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4EC)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Sleep(200)
    Sound(104, 0, 100, 0)
    Sleep(1300)
    Fade(500)
    OP_68(5030, 900, 220, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20760, 0)
    OP_0D()
    Sleep(500)

    #C0008
    ChrTalk(
        0x8,
        (
            "#11P#3201F呼……真头疼啊。\x02\x03",

            "如果向长老请求支援，\x01",
            "代价应该会很可怕……\x02\x03",

            "#3206F哎呀呀……\x01",
            "如果『银』大人能再\x01",
            "多协助我们一些就好了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1628, 255, 100, 0)    #voice#Yin
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sleep(500)

    #N0009
    NpcTalk(
        0xA,
        "声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#N……可我只打算按照契约上\x01",
            "规定的义务办事。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(5680, 900, 1890, 3000)
    MoveCamera(47, 15, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(18500, 3000)
    PlayEffect(0x0, 0xFF, 0xA, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    ClearChrFlags(0xA, 0x8)
    SetChrChip(0x0, 0xA, 0x1E, 0x12C)

    def lambda_6C2():
        OP_95(0xFE, 5800, 0, 3300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6C2)

    def lambda_6DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6DC)
    Sleep(300)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetChrSubChip(0x8, 0x2)
    OP_93(0xA, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sleep(300)

    #C0010
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3205F噢……\x01",
            "您已经来了啊。\x02\x03",

            "#3204F啊呀，我还真是失言了。\x02",
        )
    )

    CloseMessageWindow()
    #Sound(1627, 255, 100, 0)    #voice#Yin
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("黑衣男子")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30W哼……\x01",
            "你根本就是故意说给我听的吧？\x02\x03",

            "还是和以前一样狡猾。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0012
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3204F哪里哪里，还比不上阁下。\x02\x03",

            "#3200F话说回来，今晚\x01",
            "有何贵干呢？\x02\x03",

            "莫非是改变主意，准备\x01",
            "帮忙对付那些军犬了？\x02",
        )
    )

    CloseMessageWindow()

    #N0013
    NpcTalk(
        0xA,
        "黑衣男子",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0700F那种小角色，\x01",
            "凭你的部下就能解决了吧。\x02\x03",

            "我的对手应该只有\x01",
            "以加尔西亚为首的\x01",
            "鲁巴彻主力……\x02\x03",

            "契约上就是这样写的。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3206F哎呀呀，真是无情啊。\x02\x03",

            "#3201F您还是执著于\x01",
            "『彩虹剧团』那边啊……\x02\x03",

            "这里的警察很优秀呢。\x01",
            "如果将麻烦带到这边，我们可是会头疼的哦。\x02",
        )
    )

    CloseMessageWindow()

    #N0015
    NpcTalk(
        0xA,
        "黑衣男子",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0702F呵呵，不必担心。\x02\x03",

            "比起那个来……\x01",
            "对『特别任务支援科』，你有何感觉？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3205F嗯……原来您来这里\x01",
            "就是为了说他们的事吗。\x02\x03",

            "#3204F这个嘛──\x01",
            "可以说是几个让我很感兴趣的年轻人吧。\x02\x03",

            "#3200F特别是那个看起来像是领队的小子，\x01",
            "是叫罗伊德吧。\x02\x03",

            "虽然深切感到了自己力量不足，\x01",
            "却仍然毫不气馁地勇往直前……\x02\x03",

            "#3209F而且他的直觉似乎也还算敏锐，\x01",
            "可以说是我喜欢的类型呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0017
    NpcTalk(
        0xA,
        "黑衣男子",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0700F我没问你的喜好。\x02\x03",

            "那其他成员呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3204F呵呵，也都令人\x01",
            "很感兴趣啊。\x02\x03",

            "#3200F麦克道尔市长的孙女……\x01",
            "具有相当的政治嗅觉，\x01",
            "可以说是队内的军师吧。\x02\x03",

            "至于爱普斯泰恩财团的小姑娘……\x01",
            "我对她那个魔导杖很感兴趣，\x01",
            "而且她自身似乎也拥有着某种特殊的资质呢。\x02\x03",

            "#3204F至于那个红头发的……\x01",
            "呵呵，虽然只是我的直觉而已，\x01",
            "他身上似乎有种与我们很相似的味道。\x02",
        )
    )

    CloseMessageWindow()

    #N0019
    NpcTalk(
        0xA,
        "黑衣男子",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0700F……原来如此。\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3200F可是……\x01",
            "您为何会对他们感兴趣呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0021
    NpcTalk(
        0xA,
        "黑衣男子",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0702F没什么……\x01",
            "只是想稍微试试他们而已。\x02\x03",

            "试试他们是否有\x01",
            "资格接受我\x01",
            "──接受『银』的委托。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1ED end

    def Function_3_DF1(): pass

    label("Function_3_DF1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch31500.itc", 0x20)
    LoadChrToIndex("apl/ch50237.itc", 0x21)
    LoadChrToIndex("apl/ch50406.itc", 0x22)
    SoundLoad(940)
    SoundLoad(941)
    SoundLoad(942)
    OP_68(5800, 900, 0, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 7300, 0, 0, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6100, 0, -2100, 0)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -4500, 0, 0, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -4500, 0, 0, 90)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("青年的声音")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            "──鲁巴彻的地下贸易\x01",
            "渠道已经恢复了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(7300, 900, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0023
    ChrTalk(
        0x9,
        "#11P……是的。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "#11P这一周中，被我们摧毁的\x01",
            "三条渠道都已经恢复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "#11P我们也尝试过进行阻碍，\x01",
            "但却遭到了预想之外的激烈抵抗……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#3203F#5P嗯……真是奇怪啊。\x02\x03",

            "在这种状况下，我并不认为\x01",
            "他们还有余力去特意\x01",
            "夺回已经失去的渠道……\x02\x03",

            "#3200F那边的营业总部部长\x01",
            "已经亲自出马了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "#11P不，那个……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "#11P『杀戮之熊』并没有出现，\x01",
            "好像只有他的部下成员而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "#11P而且连军犬也没有携带，\x01",
            "只有寥寥数人而已……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0030
    ChrTalk(
        0x8,
        (
            "#3205F嗯，真是越来越奇怪了啊。\x02\x03",

            "#3203F如果要论普通成员的个人战斗力，\x01",
            "应该是我们『黑月』的人比较强才对……\x02\x03",

            "#3201F他们用上莱恩福尔特公司\x01",
            "制造的重型机关枪了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#11P嗯，确实用上了\x01",
            "那种武器，而且……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "#11P根据报告，他们的战斗能力本身\x01",
            "也大幅度增强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "#3203F#5P原来如此……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0034
    ChrTalk(
        0x8,
        (
            "#3204F#5P现在，马尔克尼会长\x01",
            "为了平息议长阁下的愤怒，\x01",
            "似乎都已经忙得焦头烂额了。\x02\x03",

            "没有雇佣了\x01",
            "猎兵团的迹象，\x01",
            "也没有关于大规模战斗训练的报告……\x02\x03",

            "#3210F嗯，真是耐人寻味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#11P……莫非他们还藏有\x01",
            "我们所不知的王牌吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#3200F嗯，应该是那样没错了。\x02\x03",

            "#3204F而且，根据我的判断……\x01",
            "那似乎并不是寻常的王牌。\x02\x03",

            "#3210F说不定是像『银』大人那样，\x01",
            "可以将战况瞬间扭转的\x01",
            "『鬼牌』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        "#11P唔，那到底是……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(940, 2, 80, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x7D0)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(941, 2, 80, 0)

    def lambda_149B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_149B)
    Sleep(50)
    OP_93(0x9, 0x10E, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)

    #C0038
    ChrTalk(
        0x9,
        "#11P刚、刚才的是……！？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        "#11P#3201F说到就到了吗？\x02",
    )

    CloseMessageWindow()
    Sound(942, 2, 80, 0)
    OP_68(6300, 800, 0, 1500)
    MoveCamera(50, 15, 0, 1500)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1540():
        OP_95(0xFE, 2100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1540)

    def lambda_155A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_155A)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    OP_64(0xB)
    OP_6F(0x79)

    #C0040
    ChrTalk(
        0xB,
        "#6P糟、糟糕了！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "#6P有一群身穿黑衣的家伙来袭击了，\x01",
            "似乎是鲁巴彻的人！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "#6P人数大概有十人！\x01",
            "并没有看到『杀戮之熊』！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#11P只不过是十个小卒而已，\x01",
            "马上反击，干掉他们就是了！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "#11P不用担心警察！\x01",
            "这只不过是正当防卫而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        "#6P可、可是……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "#6P袭击者的战斗力非比寻常，\x01",
            "单手就能轻松使用重型机关枪……\x02",
        )
    )

    CloseMessageWindow()
    Sound(834, 0, 100, 0)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    Sleep(1000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_16FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_16FC)

    def lambda_170D():
        OP_95(0xFE, 2200, 0, -1100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_170D)
    WaitChrThread(0xC, 1)
    OP_64(0xC)
    OP_93(0xC, 0x5A, 0x1F4)
    WaitChrThread(0xC, 2)

    #C0047
    ChrTalk(
        0xC,
        "#6P一层已经被突破了！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "#6P杀到这里应该也只是\x01",
            "时间问题而已了！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#11P唔……\x01",
            "如果『银』大人在的话……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(7300, 800, 0, 1500)
    SetCameraDistance(22500, 1500)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(130)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    Sound(882, 0, 100, 0)
    SetChrSubChip(0x8, 0x3)
    Sleep(500)
    OP_6F(0x11)

    #C0050
    ChrTalk(
        0x8,
        (
            "#11P#3204F……呵呵，哎呀呀。\x02\x03",

            "#3200F看来已经不能再假装为\x01",
            "单纯的计谋派了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0x0, 0x1F4)

    #C0051
    ChrTalk(
        0x9,
        "#11P曹先生，难道──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_25(0x3AC, 0x3C)
    OP_25(0x3AD, 0x3C)
    OP_25(0x3AE, 0x3C)
    Sleep(300)
    SetCameraDistance(21500, 800)
    Fade(250)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sound(939, 0, 100, 0)
    OP_6F(0x10)
    OP_25(0x3AC, 0x46)
    OP_25(0x3AD, 0x46)
    OP_25(0x3AE, 0x46)

    #C0052
    ChrTalk(
        0x8,
        (
            "#11P#3203F──轮到我们出场了，刘。\x02\x03",

            "#3210F如果只因这种程度的小事就要依靠『银』大人，\x01",
            "未免有损『黑月』之名了……\x02\x03",

            "支配东方人街的我们到底有何等实力，\x01",
            "就让他们好好体会一下吧。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 1, 0, 4)
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1770)
    WaitBGM()
    WaitChrThread(0xD, 1)
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_CA(0x1, 0xFF, 0x0)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    OP_24(0x3AC)
    OP_24(0x3AD)
    OP_24(0x3AE)
    SetScenarioFlags(0x5D, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_DF1 end

    def Function_4_19FF(): pass

    label("Function_4_19FF")

    OP_25(0x3AC, 0x50)
    OP_25(0x3AD, 0x50)
    OP_25(0x3AE, 0x50)
    Sleep(300)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    Sleep(300)
    OP_25(0x3AC, 0x64)
    OP_25(0x3AD, 0x64)
    OP_25(0x3AE, 0x64)
    Sleep(1500)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    Sleep(300)
    OP_25(0x3AC, 0x50)
    OP_25(0x3AD, 0x50)
    OP_25(0x3AE, 0x50)
    Sleep(300)
    OP_25(0x3AC, 0x46)
    OP_25(0x3AD, 0x46)
    OP_25(0x3AE, 0x46)
    Sleep(300)
    OP_25(0x3AC, 0x3C)
    OP_25(0x3AD, 0x3C)
    OP_25(0x3AE, 0x3C)
    Sleep(300)
    OP_25(0x3AC, 0x32)
    OP_25(0x3AD, 0x32)
    OP_25(0x3AE, 0x32)
    Sleep(300)
    OP_25(0x3AC, 0x28)
    OP_25(0x3AD, 0x28)
    OP_25(0x3AE, 0x28)
    Sleep(300)
    OP_25(0x3AC, 0x1E)
    OP_25(0x3AD, 0x1E)
    OP_25(0x3AE, 0x1E)
    Sleep(300)
    OP_25(0x3AC, 0x14)
    OP_25(0x3AD, 0x14)
    OP_25(0x3AE, 0x14)
    Sleep(300)
    OP_25(0x3AC, 0xA)
    OP_25(0x3AD, 0xA)
    OP_25(0x3AE, 0xA)
    Sleep(300)
    OP_24(0x3AC)
    OP_24(0x3AD)
    OP_24(0x3AE)
    Return()

    # Function_4_19FF end

    SaveToFile()

Try(main)
