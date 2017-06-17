from ScenarioHelper import *

def main():
    CreateScenaFile(
        "a0002.bin",                # FileName
        "a0002",                    # MapName
        "a0002",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 23000, 500, 20, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "a0002",                  # 0
        "ダミー",                 # 1
        "ダミー",                 # 2
        "ダミー",                 # 3
        "ダミー",                 # 4
        "ダミー",                 # 5
        "パーティーキャラ",       # 6
        "ＮＰＣ１",               # 7
        "ＮＰＣ２",               # 8
        "別バージョン１",         # 9
        "別バージョン２",         # 10
        "ダミー",                 # 11
        "ダミー",                 # 12
        "後編パーティ",           # 13
        "後編サブキャラ",         # 14
        "後編サブキャラ２",       # 15
        "後編別バージョン１",     # 16
        "後編別バージョン２",     # 17
        "ダミー",                 # 18
        "ダミー",                 # 19
        "font",                   # 20
        "コンシェル",             # 21
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch20100.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch20400.itc",                   # 04
        "chr/ch20500.itc",                   # 05
        "chr/ch20600.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch20800.itc",                   # 08
        "chr/ch20900.itc",                   # 09
        "chr/ch21000.itc",                   # 0A
        "chr/ch21100.itc",                   # 0B
        "chr/ch21200.itc",                   # 0C
        "chr/ch21300.itc",                   # 0D
        "chr/ch21400.itc",                   # 0E
        "chr/ch21500.itc",                   # 0F
        "chr/ch21600.itc",                   # 10
        "chr/ch21700.itc",                   # 11
        "chr/ch21800.itc",                   # 12
        "chr/ch21900.itc",                   # 13
        "monster/ch60050.itc",               # 14
    ))

    DeclNpc(4000,    0,       4000,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(8000,    0,       4000,    180,  257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(12000,   0,       4000,    180,  257,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(16000,   0,       4000,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4000,    0,       8000,    180,  257,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(8000,    0,       8000,    180,  257,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(12000,   0,       8000,    180,  257,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(16000,   0,       8000,    180,  257,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4000,    0,       12000,   180,  257,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(8000,    0,       12000,   180,  257,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(12000,   0,       12000,   180,  257,  0x0, 0,   10,  0,   0,   0,   0,   4,   255,  0)
    DeclNpc(16000,   0,       12000,   180,  257,  0x0, 0,   11,  0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4000,    0,       16000,   180,  257,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(8000,    0,       16000,   180,  257,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(12000,   0,       16000,   180,  257,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(16000,   0,       16000,   180,  257,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4000,    0,       20000,   180,  257,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8000,    0,       20000,   180,  257,  0x0, 0,   17,  0,   0,   0,   0,   4,   255,  0)
    DeclNpc(12000,   0,       20000,   180,  257,  0x0, 0,   18,  0,   0,   0,   0,   4,   255,  0)
    DeclNpc(16000,   0,       20000,   180,  257,  0x0, 0,   19,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(1000,    0,       4000,    180,  257,  0x0, 0,   20,  0,   255, 255, 0,   3,   255,  0)

    ChipFrameInfo(904, 0)                                        # 0

    ScpFunction((
        "Function_0_388",          # 00, 0
        "Function_1_438",          # 01, 1
        "Function_2_439",          # 02, 2
        "Function_3_43A",          # 03, 3
        "Function_4_1D12",         # 04, 4
        "Function_5_1D21",         # 05, 5
        "Function_6_1DF0",         # 06, 6
        "Function_7_1F15",         # 07, 7
        "Function_8_2032",         # 08, 8
        "Function_9_20F9",         # 09, 9
        "Function_10_2310",        # 0A, 10
        "Function_11_331D",        # 0B, 11
        "Function_12_4674",        # 0C, 12
        "Function_13_5833",        # 0D, 13
        "Function_14_5FB7",        # 0E, 14
        "Function_15_678B",        # 0F, 15
        "Function_16_6FDD",        # 10, 16
        "Function_17_81AB",        # 11, 17
        "Function_18_8EBC",        # 12, 18
        "Function_19_A589",        # 13, 19
        "Function_20_B8FE",        # 14, 20
    ))


    def Function_0_388(): pass

    label("Function_0_388")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3C0"),
        (1, "loc_3CC"),
        (2, "loc_3D8"),
        (3, "loc_3E4"),
        (4, "loc_3F0"),
        (5, "loc_3FC"),
        (6, "loc_408"),
        (SWITCH_DEFAULT, "loc_414"),
    )


    label("loc_3C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_3CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_3D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_3E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_3F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_3FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_408")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_414")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_420")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_437")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_420")

    label("loc_437")

    Return()

    # Function_0_388 end

    def Function_1_438(): pass

    label("Function_1_438")

    Return()

    # Function_1_438 end

    def Function_2_439(): pass

    label("Function_2_439")

    Return()

    # Function_2_439 end

    def Function_3_43A(): pass

    label("Function_3_43A")

    TalkBegin(0xFE)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrFlags(0x4, 0x8)
    SetChrFlags(0x5, 0x8)
    SetChrFlags(0x6, 0x8)
    SetChrFlags(0x7, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    OP_49()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ch00000 - ch01500\x01",        # 0
            "ch05000 - ch06900\x01",        # 1
            "ch07000 - ch08900\x01",        # 2
            "ch09000 - ch10900\x01",        # 3
            "×ch11000 - ch12900\x01",      # 4
            "ch20000 - ch21900\x01",        # 5
            "ch22000 - ch23900\x01",        # 6
            "ch24000 - ch25900\x01",        # 7
            "ch26000 - ch27900\x01",        # 8
            "ch28000 - ch29900\x01",        # 9
            "ch30000 - ch31900\x01",        # 10
            "ch32000 - ch33900\x01",        # 11
            "ch34000 - ch35900\x01",        # 12
            "ch36000 - ch39900\x01",        # 13
            "キャンセル\x01",               # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_647"),
        (1, "loc_76A"),
        (2, "loc_971"),
        (3, "loc_B5E"),
        (4, "loc_D57"),
        (5, "loc_F3C"),
        (6, "loc_1199"),
        (7, "loc_12FC"),
        (8, "loc_1455"),
        (9, "loc_15AE"),
        (10, "loc_1707"),
        (11, "loc_1860"),
        (12, "loc_19B9"),
        (13, "loc_1B12"),
        (SWITCH_DEFAULT, "loc_1C6B"),
    )


    label("loc_647")

    LoadChrToIndex("chr/ch00000.itc", 0x0)
    LoadChrToIndex("chr/ch00100.itc", 0x1)
    LoadChrToIndex("chr/ch00200.itc", 0x2)
    LoadChrToIndex("chr/ch00300.itc", 0x3)
    LoadChrToIndex("chr/ch00500.itc", 0x5)
    LoadChrToIndex("chr/ch00600.itc", 0x6)
    LoadChrToIndex("chr/ch00700.itc", 0x7)
    LoadChrToIndex("chr/ch00900.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH00000 ロイド")
    OP_8E(0x9, "CH00100 エリィ")
    OP_8E(0xA, "CH00200 ティオ")
    OP_8E(0xB, "CH00300 ランディ")
    OP_8E(0xC, "CH00400 ワジ")
    OP_8E(0xD, "CH00500 イン")
    OP_8E(0xE, "CH00600 エス")
    OP_8E(0xF, "CH00700 ヨシャ")
    OP_8E(0x10, "CH00800 ノエル")
    OP_8E(0x11, "CH00900 ダドリー")
    Jump("loc_1C7A")

    label("loc_76A")

    LoadChrToIndex("chr/ch40018.itc", 0x0)
    LoadChrToIndex("chr/ch05100.itc", 0x1)
    LoadChrToIndex("chr/ch05200.itc", 0x2)
    LoadChrToIndex("chr/ch05300.itc", 0x3)
    LoadChrToIndex("chr/ch05400.itc", 0x4)
    LoadChrToIndex("chr/ch05500.itc", 0x5)
    LoadChrToIndex("chr/ch05600.itc", 0x6)
    LoadChrToIndex("chr/ch05700.itc", 0x7)
    LoadChrToIndex("chr/ch05800.itc", 0x8)
    LoadChrToIndex("chr/ch05900.itc", 0x9)
    LoadChrToIndex("chr/ch06000.itc", 0xA)
    LoadChrToIndex("chr/ch06100.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch06400.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch06700.itc", 0x11)
    LoadChrToIndex("chr/ch06800.itc", 0x12)
    LoadChrToIndex("chr/ch06900.itc", 0x13)
    OP_8E(0x8, "CH05000 キーア")
    OP_8E(0x9, "CH05100 イリア")
    OP_8E(0xA, "CH05200 リーシャ")
    OP_8E(0xB, "CH05300 セシル")
    OP_8E(0xC, "CH05400 シズク")
    OP_8E(0xD, "CH05500 マリアベル")
    OP_8E(0xE, "CH05600 ディーター")
    OP_8E(0xF, "CH05700 ソーニャ")
    OP_8E(0x10, "CH05800 マクダエル")
    OP_8E(0x11, "CH05900 イアン")
    OP_8E(0x12, "CH06000 グレイス")
    OP_8E(0x13, "CH06100 ヨナ")
    OP_8E(0x14, "CH06200 マルコーニ")
    OP_8E(0x15, "CH06300 ツァオ")
    OP_8E(0x16, "CH06400 ピエール")
    OP_8E(0x17, "CH06500 ハルトマン")
    OP_8E(0x18, "CH06600 ヨルグ")
    OP_8E(0x19, "CH06700 ドーミトリィ")
    OP_8E(0x1A, "CH06800 ディーノ")
    OP_8E(0x1B, "CH06900 フラン")
    Jump("loc_1C7A")

    label("loc_971")

    LoadChrToIndex("chr/ch07000.itc", 0x0)
    LoadChrToIndex("chr/ch40018.itc", 0x1)
    LoadChrToIndex("chr/ch07200.itc", 0x2)
    LoadChrToIndex("chr/ch07300.itc", 0x3)
    LoadChrToIndex("chr/ch07400.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    LoadChrToIndex("chr/ch40018.itc", 0x6)
    LoadChrToIndex("chr/ch40018.itc", 0x7)
    LoadChrToIndex("chr/ch40018.itc", 0x8)
    LoadChrToIndex("chr/ch40018.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch08200.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch08700.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH07000 オスカー")
    OP_8E(0x9, "CH07100 ウェンディ")
    OP_8E(0xA, "CH07200 コリン")
    OP_8E(0xB, "CH07300 キリカ")
    OP_8E(0xC, "CH07400 レクター")
    OP_8E(0xD, "CH07500 セシル")
    OP_8E(0xE, "CH07600 ダミー")
    OP_8E(0xF, "CH07700 ダミー")
    OP_8E(0x10, "CH07800 ダミー")
    OP_8E(0x11, "CH07900 ダミー")
    OP_8E(0x12, "CH08000 ダミー")
    OP_8E(0x13, "CH08100 ダミー")
    OP_8E(0x14, "CH08200 キーア")
    OP_8E(0x15, "CH08300 ダミー")
    OP_8E(0x16, "CH08400 ダミー")
    OP_8E(0x17, "CH08500 ダミー")
    OP_8E(0x18, "CH08600 ダミー")
    OP_8E(0x19, "CH08700 シズク")
    OP_8E(0x1A, "CH08800 ダミー")
    OP_8E(0x1B, "CH08900 ダミー")
    Jump("loc_1C7A")

    label("loc_B5E")

    LoadChrToIndex("chr/ch09000.itc", 0x0)
    LoadChrToIndex("chr/ch09100.itc", 0x1)
    LoadChrToIndex("chr/ch09200.itc", 0x2)
    LoadChrToIndex("chr/ch09300.itc", 0x3)
    LoadChrToIndex("chr/ch09400.itc", 0x4)
    LoadChrToIndex("chr/ch09500.itc", 0x5)
    LoadChrToIndex("chr/ch40018.itc", 0x6)
    LoadChrToIndex("chr/ch40018.itc", 0x7)
    LoadChrToIndex("chr/ch40018.itc", 0x8)
    LoadChrToIndex("chr/ch40018.itc", 0x9)
    LoadChrToIndex("chr/ch10000.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch10300.itc", 0xD)
    LoadChrToIndex("chr/ch10400.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH09000 イメルダ夫人")
    OP_8E(0x9, "CH09100 受付ミシェル")
    OP_8E(0xA, "CH09200 アシュリー")
    OP_8E(0xB, "CH09300 ハロルド")
    OP_8E(0xC, "CH09400 ソフィア")
    OP_8E(0xD, "CH09500 レン")
    OP_8E(0xE, "CH09600 ダミー")
    OP_8E(0xF, "CH09700 ダミー")
    OP_8E(0x10, "CH09800 ダミー")
    OP_8E(0x11, "CH09900 ダミー")
    OP_8E(0x12, "CH10000 シュリ")
    OP_8E(0x13, "CH10100 ダミー")
    OP_8E(0x14, "CH10200 ダミー")
    OP_8E(0x15, "CH10300 レイテ")
    OP_8E(0x16, "CH10400 クラリス")
    OP_8E(0x17, "CH10500 ダミー")
    OP_8E(0x18, "CH10600 ダミー")
    OP_8E(0x19, "CH10700 シズク")
    OP_8E(0x1A, "CH10800 ダミー")
    OP_8E(0x1B, "CH10900 ダミー")
    Jump("loc_1C7A")

    label("loc_D57")

    LoadChrToIndex("chr/ch40018.itc", 0x0)
    LoadChrToIndex("chr/ch40018.itc", 0x1)
    LoadChrToIndex("chr/ch40018.itc", 0x2)
    LoadChrToIndex("chr/ch40018.itc", 0x3)
    LoadChrToIndex("chr/ch40018.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    LoadChrToIndex("chr/ch40018.itc", 0x6)
    LoadChrToIndex("chr/ch40018.itc", 0x7)
    LoadChrToIndex("chr/ch40018.itc", 0x8)
    LoadChrToIndex("chr/ch40018.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH11000 ダミー")
    OP_8E(0x9, "CH11100 ダミー")
    OP_8E(0xA, "CH11100 ダミー")
    OP_8E(0xB, "CH11300 ダミー")
    OP_8E(0xC, "CH11400 ダミー")
    OP_8E(0xD, "CH11500 ダミー")
    OP_8E(0xE, "CH11600 ダミー")
    OP_8E(0xF, "CH11100 ダミー")
    OP_8E(0x10, "CH11800 ダミー")
    OP_8E(0x11, "CH11900 ダミー")
    OP_8E(0x12, "CH12000 ダミー")
    OP_8E(0x13, "CH12100 ダミー")
    OP_8E(0x14, "CH12100 ダミー")
    OP_8E(0x15, "CH12300 ダミー")
    OP_8E(0x16, "CH12400 ダミー")
    OP_8E(0x17, "CH12500 ダミー")
    OP_8E(0x18, "CH12600 ダミー")
    OP_8E(0x19, "CH12100 ダミー")
    OP_8E(0x1A, "CH12800 ダミー")
    OP_8E(0x1B, "CH12900 ダミー")
    Jump("loc_1C7A")

    label("loc_F3C")

    LoadChrToIndex("chr/ch20000.itc", 0x0)
    LoadChrToIndex("chr/ch20100.itc", 0x1)
    LoadChrToIndex("chr/ch20200.itc", 0x2)
    LoadChrToIndex("chr/ch20300.itc", 0x3)
    LoadChrToIndex("chr/ch20400.itc", 0x4)
    LoadChrToIndex("chr/ch20500.itc", 0x5)
    LoadChrToIndex("chr/ch20600.itc", 0x6)
    LoadChrToIndex("chr/ch20700.itc", 0x7)
    LoadChrToIndex("chr/ch20800.itc", 0x8)
    LoadChrToIndex("chr/ch20900.itc", 0x9)
    LoadChrToIndex("chr/ch21000.itc", 0xA)
    LoadChrToIndex("chr/ch21100.itc", 0xB)
    LoadChrToIndex("chr/ch21200.itc", 0xC)
    LoadChrToIndex("chr/ch21300.itc", 0xD)
    LoadChrToIndex("chr/ch21400.itc", 0xE)
    LoadChrToIndex("chr/ch21500.itc", 0xF)
    LoadChrToIndex("chr/ch21600.itc", 0x10)
    LoadChrToIndex("chr/ch21700.itc", 0x11)
    LoadChrToIndex("chr/ch21800.itc", 0x12)
    LoadChrToIndex("chr/ch21900.itc", 0x13)
    OP_8E(0x8, "CH20000 西通り?老人")
    OP_8E(0x9, "CH20100 西通り?老婆")
    OP_8E(0xA, "CH20200 西通り?中年男性")
    OP_8E(0xB, "CH20300 西通り?中年女性")
    OP_8E(0xC, "CH20400 西通り?若者")
    OP_8E(0xD, "CH20500 西通り?娘")
    OP_8E(0xE, "CH20600 西通り?男の子")
    OP_8E(0xF, "CH20700 西通り?女の子")
    OP_8E(0x10, "CH20800 東通り?老人")
    OP_8E(0x11, "CH20900 東通り?老婆")
    OP_8E(0x12, "CH21000 東通り?中年男性")
    OP_8E(0x13, "CH21100 東通り?中年女性")
    OP_8E(0x14, "CH21200 東通り?若者")
    OP_8E(0x15, "CH21300 東通り?娘")
    OP_8E(0x16, "CH21400 東通り?男の子")
    OP_8E(0x17, "CH21500 東通り?女の子")
    OP_8E(0x18, "CH21600 上流?老人")
    OP_8E(0x19, "CH21700 上流?老婆")
    OP_8E(0x1A, "CH21800 上流?中年男性")
    OP_8E(0x1B, "CH21900 上流?中年女性")
    Jump("loc_1C7A")

    label("loc_1199")

    LoadChrToIndex("chr/ch22000.itc", 0x0)
    LoadChrToIndex("chr/ch22100.itc", 0x1)
    LoadChrToIndex("chr/ch22200.itc", 0x2)
    LoadChrToIndex("chr/ch22300.itc", 0x3)
    LoadChrToIndex("chr/ch40018.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    LoadChrToIndex("chr/ch40018.itc", 0x6)
    LoadChrToIndex("chr/ch22700.itc", 0x7)
    LoadChrToIndex("chr/ch22800.itc", 0x8)
    LoadChrToIndex("chr/ch40018.itc", 0x9)
    LoadChrToIndex("chr/ch23000.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch23200.itc", 0xC)
    LoadChrToIndex("chr/ch23300.itc", 0xD)
    LoadChrToIndex("chr/ch23400.itc", 0xE)
    LoadChrToIndex("chr/ch23500.itc", 0xF)
    LoadChrToIndex("chr/ch23600.itc", 0x10)
    LoadChrToIndex("chr/ch23700.itc", 0x11)
    LoadChrToIndex("chr/ch23800.itc", 0x12)
    LoadChrToIndex("chr/ch23900.itc", 0x13)
    OP_8E(0x8, "CH22000 上流?若者")
    OP_8E(0x9, "CH22100")
    OP_8E(0xA, "CH22200")
    OP_8E(0xB, "CH22300")
    OP_8E(0xC, "CH22400")
    OP_8E(0xD, "CH22500")
    OP_8E(0xE, "CH22600")
    OP_8E(0xF, "CH22700")
    OP_8E(0x10, "CH22800")
    OP_8E(0x11, "CH22900")
    OP_8E(0x12, "CH23000")
    OP_8E(0x13, "CH23100")
    OP_8E(0x14, "CH23200")
    OP_8E(0x15, "CH23300")
    OP_8E(0x16, "CH23400")
    OP_8E(0x17, "CH23500")
    OP_8E(0x18, "CH23600")
    OP_8E(0x19, "CH23700")
    OP_8E(0x1A, "CH23800")
    OP_8E(0x1B, "CH23900")
    Jump("loc_1C7A")

    label("loc_12FC")

    LoadChrToIndex("chr/ch24000.itc", 0x0)
    LoadChrToIndex("chr/ch24100.itc", 0x1)
    LoadChrToIndex("chr/ch24200.itc", 0x2)
    LoadChrToIndex("chr/ch24300.itc", 0x3)
    LoadChrToIndex("chr/ch24400.itc", 0x4)
    LoadChrToIndex("chr/ch24500.itc", 0x5)
    LoadChrToIndex("chr/ch24600.itc", 0x6)
    LoadChrToIndex("chr/ch24700.itc", 0x7)
    LoadChrToIndex("chr/ch24800.itc", 0x8)
    LoadChrToIndex("chr/ch24900.itc", 0x9)
    LoadChrToIndex("chr/ch25000.itc", 0xA)
    LoadChrToIndex("chr/ch25100.itc", 0xB)
    LoadChrToIndex("chr/ch25200.itc", 0xC)
    LoadChrToIndex("chr/ch25300.itc", 0xD)
    LoadChrToIndex("chr/ch25400.itc", 0xE)
    LoadChrToIndex("chr/ch25500.itc", 0xF)
    LoadChrToIndex("chr/ch25600.itc", 0x10)
    LoadChrToIndex("chr/ch25700.itc", 0x11)
    LoadChrToIndex("chr/ch25800.itc", 0x12)
    LoadChrToIndex("chr/ch25900.itc", 0x13)
    OP_8E(0x8, "CH24000")
    OP_8E(0x9, "CH24100")
    OP_8E(0xA, "CH24200")
    OP_8E(0xB, "CH24300")
    OP_8E(0xC, "CH24400")
    OP_8E(0xD, "CH24500")
    OP_8E(0xE, "CH24600")
    OP_8E(0xF, "CH24700")
    OP_8E(0x10, "CH24800")
    OP_8E(0x11, "CH24900")
    OP_8E(0x12, "CH25000")
    OP_8E(0x13, "CH25100")
    OP_8E(0x14, "CH25200")
    OP_8E(0x15, "CH25300")
    OP_8E(0x16, "CH25400")
    OP_8E(0x17, "CH25500")
    OP_8E(0x18, "CH25600")
    OP_8E(0x19, "CH25700")
    OP_8E(0x1A, "CH25800")
    OP_8E(0x1B, "CH25900")
    Jump("loc_1C7A")

    label("loc_1455")

    LoadChrToIndex("chr/ch26000.itc", 0x0)
    LoadChrToIndex("chr/ch26100.itc", 0x1)
    LoadChrToIndex("chr/ch26200.itc", 0x2)
    LoadChrToIndex("chr/ch26300.itc", 0x3)
    LoadChrToIndex("chr/ch26400.itc", 0x4)
    LoadChrToIndex("chr/ch26500.itc", 0x5)
    LoadChrToIndex("chr/ch26600.itc", 0x6)
    LoadChrToIndex("chr/ch26700.itc", 0x7)
    LoadChrToIndex("chr/ch26800.itc", 0x8)
    LoadChrToIndex("chr/ch26900.itc", 0x9)
    LoadChrToIndex("chr/ch27000.itc", 0xA)
    LoadChrToIndex("chr/ch27100.itc", 0xB)
    LoadChrToIndex("chr/ch27200.itc", 0xC)
    LoadChrToIndex("chr/ch27300.itc", 0xD)
    LoadChrToIndex("chr/ch27400.itc", 0xE)
    LoadChrToIndex("chr/ch27500.itc", 0xF)
    LoadChrToIndex("chr/ch27600.itc", 0x10)
    LoadChrToIndex("chr/ch27700.itc", 0x11)
    LoadChrToIndex("chr/ch27800.itc", 0x12)
    LoadChrToIndex("chr/ch27900.itc", 0x13)
    OP_8E(0x8, "CH26000")
    OP_8E(0x9, "CH26100")
    OP_8E(0xA, "CH26200")
    OP_8E(0xB, "CH26300")
    OP_8E(0xC, "CH26400")
    OP_8E(0xD, "CH26500")
    OP_8E(0xE, "CH26600")
    OP_8E(0xF, "CH26700")
    OP_8E(0x10, "CH26800")
    OP_8E(0x11, "CH26900")
    OP_8E(0x12, "CH27000")
    OP_8E(0x13, "CH27100")
    OP_8E(0x14, "CH27200")
    OP_8E(0x15, "CH27300")
    OP_8E(0x16, "CH27400")
    OP_8E(0x17, "CH27500")
    OP_8E(0x18, "CH27600")
    OP_8E(0x19, "CH27700")
    OP_8E(0x1A, "CH27800")
    OP_8E(0x1B, "CH27900")
    Jump("loc_1C7A")

    label("loc_15AE")

    LoadChrToIndex("chr/ch28000.itc", 0x0)
    LoadChrToIndex("chr/ch28100.itc", 0x1)
    LoadChrToIndex("chr/ch28200.itc", 0x2)
    LoadChrToIndex("chr/ch28300.itc", 0x3)
    LoadChrToIndex("chr/ch28400.itc", 0x4)
    LoadChrToIndex("chr/ch28500.itc", 0x5)
    LoadChrToIndex("chr/ch28600.itc", 0x6)
    LoadChrToIndex("chr/ch28700.itc", 0x7)
    LoadChrToIndex("chr/ch28800.itc", 0x8)
    LoadChrToIndex("chr/ch28900.itc", 0x9)
    LoadChrToIndex("chr/ch29000.itc", 0xA)
    LoadChrToIndex("chr/ch29100.itc", 0xB)
    LoadChrToIndex("chr/ch29200.itc", 0xC)
    LoadChrToIndex("chr/ch29300.itc", 0xD)
    LoadChrToIndex("chr/ch29400.itc", 0xE)
    LoadChrToIndex("chr/ch29500.itc", 0xF)
    LoadChrToIndex("chr/ch29600.itc", 0x10)
    LoadChrToIndex("chr/ch29700.itc", 0x11)
    LoadChrToIndex("chr/ch29800.itc", 0x12)
    LoadChrToIndex("chr/ch29900.itc", 0x13)
    OP_8E(0x8, "CH28000")
    OP_8E(0x9, "CH28100")
    OP_8E(0xA, "CH28200")
    OP_8E(0xB, "CH28300")
    OP_8E(0xC, "CH28400")
    OP_8E(0xD, "CH28500")
    OP_8E(0xE, "CH28600")
    OP_8E(0xF, "CH28700")
    OP_8E(0x10, "CH28800")
    OP_8E(0x11, "CH28900")
    OP_8E(0x12, "CH29000")
    OP_8E(0x13, "CH29100")
    OP_8E(0x14, "CH29200")
    OP_8E(0x15, "CH29300")
    OP_8E(0x16, "CH29400")
    OP_8E(0x17, "CH29500")
    OP_8E(0x18, "CH29600")
    OP_8E(0x19, "CH29700")
    OP_8E(0x1B, "CH29800")
    OP_8E(0x1B, "CH29900")
    Jump("loc_1C7A")

    label("loc_1707")

    LoadChrToIndex("chr/ch30000.itc", 0x0)
    LoadChrToIndex("chr/ch30100.itc", 0x1)
    LoadChrToIndex("chr/ch30200.itc", 0x2)
    LoadChrToIndex("chr/ch30300.itc", 0x3)
    LoadChrToIndex("chr/ch30400.itc", 0x4)
    LoadChrToIndex("chr/ch30500.itc", 0x5)
    LoadChrToIndex("chr/ch30600.itc", 0x6)
    LoadChrToIndex("chr/ch40018.itc", 0x7)
    LoadChrToIndex("chr/ch30800.itc", 0x8)
    LoadChrToIndex("chr/ch30900.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch31200.itc", 0xC)
    LoadChrToIndex("chr/ch31300.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch31600.itc", 0x10)
    LoadChrToIndex("chr/ch31700.itc", 0x11)
    LoadChrToIndex("chr/ch31800.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH30000")
    OP_8E(0x9, "CH30100")
    OP_8E(0xA, "CH30200")
    OP_8E(0xB, "CH30300")
    OP_8E(0xC, "CH30400")
    OP_8E(0xD, "CH30500")
    OP_8E(0xE, "CH30600")
    OP_8E(0xF, "CH30700")
    OP_8E(0x10, "CH30800")
    OP_8E(0x11, "CH30900")
    OP_8E(0x12, "CH31000")
    OP_8E(0x13, "CH31100")
    OP_8E(0x14, "CH31200")
    OP_8E(0x15, "CH31300")
    OP_8E(0x16, "CH31400")
    OP_8E(0x17, "CH31500")
    OP_8E(0x18, "CH31600")
    OP_8E(0x19, "CH31700")
    OP_8E(0x1A, "CH31800")
    OP_8E(0x1B, "CH31900")
    Jump("loc_1C7A")

    label("loc_1860")

    LoadChrToIndex("chr/ch32000.itc", 0x0)
    LoadChrToIndex("chr/ch32100.itc", 0x1)
    LoadChrToIndex("chr/ch32200.itc", 0x2)
    LoadChrToIndex("chr/ch40018.itc", 0x3)
    LoadChrToIndex("chr/ch32400.itc", 0x4)
    LoadChrToIndex("chr/ch32500.itc", 0x5)
    LoadChrToIndex("chr/ch32600.itc", 0x6)
    LoadChrToIndex("chr/ch32700.itc", 0x7)
    LoadChrToIndex("chr/ch32800.itc", 0x8)
    LoadChrToIndex("chr/ch32900.itc", 0x9)
    LoadChrToIndex("chr/ch33000.itc", 0xA)
    LoadChrToIndex("chr/ch33100.itc", 0xB)
    LoadChrToIndex("chr/ch33200.itc", 0xC)
    LoadChrToIndex("chr/ch33300.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch33600.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH32000")
    OP_8E(0x9, "CH32100")
    OP_8E(0xA, "CH32200")
    OP_8E(0xB, "CH32300")
    OP_8E(0xC, "CH32400")
    OP_8E(0xD, "CH32500")
    OP_8E(0xE, "CH32600")
    OP_8E(0xF, "CH32700")
    OP_8E(0x10, "CH32800")
    OP_8E(0x11, "CH32900")
    OP_8E(0x12, "CH33000")
    OP_8E(0x13, "CH33100")
    OP_8E(0x14, "CH33200")
    OP_8E(0x15, "CH33300")
    OP_8E(0x16, "CH33400")
    OP_8E(0x17, "CH33500")
    OP_8E(0x18, "CH33600")
    OP_8E(0x19, "CH33700")
    OP_8E(0x1A, "CH33800")
    OP_8E(0x1B, "CH33900")
    Jump("loc_1C7A")

    label("loc_19B9")

    LoadChrToIndex("chr/ch34000.itc", 0x0)
    LoadChrToIndex("chr/ch34100.itc", 0x1)
    LoadChrToIndex("chr/ch34200.itc", 0x2)
    LoadChrToIndex("chr/ch34300.itc", 0x3)
    LoadChrToIndex("chr/ch34400.itc", 0x4)
    LoadChrToIndex("chr/ch34500.itc", 0x5)
    LoadChrToIndex("chr/ch34600.itc", 0x6)
    LoadChrToIndex("chr/ch40018.itc", 0x7)
    LoadChrToIndex("chr/ch40018.itc", 0x8)
    LoadChrToIndex("chr/ch40018.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH34000")
    OP_8E(0x9, "CH34100")
    OP_8E(0xA, "CH34200")
    OP_8E(0xB, "CH34300")
    OP_8E(0xC, "CH34400")
    OP_8E(0xD, "CH34500")
    OP_8E(0xE, "CH34600")
    OP_8E(0xF, "CH34700")
    OP_8E(0x10, "CH34800")
    OP_8E(0x11, "CH34900")
    OP_8E(0x12, "CH35000")
    OP_8E(0x13, "CH35100")
    OP_8E(0x14, "CH35200")
    OP_8E(0x15, "CH35300")
    OP_8E(0x16, "CH35400")
    OP_8E(0x17, "CH35500")
    OP_8E(0x18, "CH35600")
    OP_8E(0x19, "CH35700")
    OP_8E(0x1A, "CH35800")
    OP_8E(0x1B, "CH35900")
    Jump("loc_1C7A")

    label("loc_1B12")

    LoadChrToIndex("chr/ch36300.itc", 0x0)
    LoadChrToIndex("chr/ch36600.itc", 0x1)
    LoadChrToIndex("chr/ch36700.itc", 0x2)
    LoadChrToIndex("chr/ch36800.itc", 0x3)
    LoadChrToIndex("chr/ch36900.itc", 0x4)
    LoadChrToIndex("chr/ch37000.itc", 0x5)
    LoadChrToIndex("chr/ch37300.itc", 0x6)
    LoadChrToIndex("chr/ch37400.itc", 0x7)
    LoadChrToIndex("chr/ch39000.itc", 0x8)
    LoadChrToIndex("chr/ch39200.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH34000")
    OP_8E(0x9, "CH34100")
    OP_8E(0xA, "CH34200")
    OP_8E(0xB, "CH34300")
    OP_8E(0xC, "CH34400")
    OP_8E(0xD, "CH34500")
    OP_8E(0xE, "CH34600")
    OP_8E(0xF, "CH34700")
    OP_8E(0x10, "CH34800")
    OP_8E(0x11, "CH34900")
    OP_8E(0x12, "CH35000")
    OP_8E(0x13, "CH35100")
    OP_8E(0x14, "CH35200")
    OP_8E(0x15, "CH35300")
    OP_8E(0x16, "CH35400")
    OP_8E(0x17, "CH35500")
    OP_8E(0x18, "CH35600")
    OP_8E(0x19, "CH35700")
    OP_8E(0x1A, "CH35800")
    OP_8E(0x1B, "CH35900")
    Jump("loc_1C7A")

    label("loc_1C6B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C7A")

    label("loc_1C7A")

    OP_60(0x0)
    OP_57(0x0)
    OP_DD()
    LoadChrChipPat()
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x8)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    OP_49()
    TalkEnd(0xFE)
    Return()

    # Function_3_43A end

    def Function_4_1D12(): pass

    label("Function_4_1D12")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        "　\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_1D12 end

    def Function_5_1D21(): pass

    label("Function_5_1D21")

    TalkBegin(0xFE)

    #C0002
    ChrTalk(
        0xFE,
        "#0000Fロイド\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "#0100Fエリィ\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "#0200Fティオ\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "#0300Fランディ\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "#0400Fワジ\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "#0500Fノエル曹長\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "#0600Fダドリー捜査官\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "#0700F銀#2Rイン#\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "#0800Fエステル\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "#0900Fヨシュア\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1D21 end

    def Function_6_1DF0(): pass

    label("Function_6_1DF0")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        "#1000Fセルゲイ課長\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "#1100Fキーア\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "#1200Fツァイト\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "#1300Fセシル\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "#1400Fアリオス\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "#1500Fシズク\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "#1600Fヴァルド\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "#1700Fイリア\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "#1800Fリーシャ\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "#1900F受付嬢フラン\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "#2000Fソーニャ副司令\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "#2100Fグレイス\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "#2200Fイアン弁護士\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "#2300Fヨナ\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1DF0 end

    def Function_7_1F15(): pass

    label("Function_7_1F15")

    TalkBegin(0xFE)

    #C0026
    ChrTalk(
        0xFE,
        "#2500Fマクダエル市長\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "#2600F秘書アーネスト\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "#2700Fハルトマン議長\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "#2800Fディーター総裁\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "#2900Fマリアベル\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "#3200Fツァオ\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "#3300Fレン\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "#3400Fキリカ\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "#3500Fレクター\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "#3600Fハロルド\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "#3700Fソフィア\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "#3800Fコリン\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "#3900Fヨルグ老人\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1F15 end

    def Function_8_2032(): pass

    label("Function_8_2032")

    TalkBegin(0xFE)

    #C0039
    ChrTalk(
        0xFE,
        "#5200Fロイド部屋着\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "#5800Fキーア私服\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "#5900Fセシル私服\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "#6000Fシズク外出着\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "#6100Fイリア舞台服\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "#6200Fリーシャ舞台服\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "#6400Fフラン私服\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "#6600Fアーネスト魔人化\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_2032 end

    def Function_9_20F9(): pass

    label("Function_9_20F9")

    EventBegin(0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00000.itp")

    #C0047
    ChrTalk(
        0xFE,
        "#0000Fロイド\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0048
    ChrTalk(
        0xFE,
        "#0001F#1P＃１Ｐ\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "#0002F#2P＃２Ｐ\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "#0003F#3P＃３Ｐ\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "#0004F#4P＃４Ｐ\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "#0005F#5P＃５Ｐ\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "#0006F#6P＃６Ｐ\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "#0007F#7P＃７Ｐ\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "#0008F#8P＃８Ｐ\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "#0009F#9P＃９Ｐ\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        "#0009F#10P＃１０Ｐ\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "#0009F#11P＃１１Ｐ\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "#0009F#12P＃１２Ｐ\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "#0009F#13P＃１３Ｐ\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "#0009F#14P＃１４Ｐ\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "#0009F#15P＃１５Ｐ\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "#0009F#16P＃１６Ｐ\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_9_20F9 end

    def Function_10_2310(): pass

    label("Function_10_2310")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_231C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331A")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ロイド\x01",              # 0
            "エリィ\x01",              # 1
            "ティオ\x01",              # 2
            "ランディ\x01",            # 3
            "ワジ\x01",                # 4
            "ノエル曹長\x01",          # 5
            "ダドリー捜査官\x01",      # 6
            "銀\x01",                  # 7
            "エステル\x01",            # 8
            "ヨシュア\x01",            # 9
            "キャンセル\x01",          # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23DF"),
        (1, "loc_2579"),
        (2, "loc_272D"),
        (3, "loc_28E5"),
        (4, "loc_2A83"),
        (5, "loc_2BED"),
        (6, "loc_2D67"),
        (7, "loc_2ED3"),
        (8, "loc_2FC9"),
        (9, "loc_3183"),
        (SWITCH_DEFAULT, "loc_3315"),
    )


    label("loc_23DF")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0064
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0065
    ChrTalk(
        0xFE,
        "#0000F通常\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "#0001F真剣\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "#0002F微笑\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "#0003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "#0004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "#0005F驚き\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "#0006F溜息\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "#0007F叫び\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "#0008F悲哀\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "#0009F笑い\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "#0010F苦痛\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "#0011F慌て\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "#0012F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_2579")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0078
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0079
    ChrTalk(
        0xFE,
        "#0100F通常\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "#0101F真剣\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "#0102F微笑\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "#0103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "#0104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "#0105F驚き\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "#0106F溜息\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "#0107F叫び\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "#0108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "#0109F笑い\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "#0110F苦痛\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        "#0111Fジト目\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "#0112F照れ驚き\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        "#0113F照れ瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_272D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0093
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0094
    ChrTalk(
        0xFE,
        "#0200F通常\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        "#0201F真剣\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "#0202F微笑\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        "#0203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "#0204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        "#0205F驚き\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        "#0206F溜息\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "#0207F叫び\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "#0208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "#0209F笑い\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "#0210F苦痛\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        "#0211Fジト目\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "#0212F泣き笑い\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "#0213F泣き笑い瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_28E5")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0108
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0109
    ChrTalk(
        0xFE,
        "#0300F通常\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        "#0301F真剣\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        "#0302F微笑\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "#0303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "#0304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        "#0305F驚き\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "#0306F溜息\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "#0307F叫び\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "#0308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        "#0309F笑い\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        "#0310F苦痛\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "#0311F殺意\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "#0312F殺意微笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_2A83")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0122
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0123
    ChrTalk(
        0xFE,
        "#0400F通常\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "#0401F真剣\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "#0402F微笑\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "#0403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "#0404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "#0405F驚き\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "#0406F溜息\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "#0407F叫び\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        "#0409F笑い\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "#0410F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_2BED")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0133
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0134
    ChrTalk(
        0xFE,
        "#0500F通常\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "#0501F真剣\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "#0502F微笑\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "#0503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "#0504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        "#0505F驚き\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "#0506F溜息\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "#0507F叫び\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        "#0508F悲哀\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        "#0509F笑い\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        "#0510F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_2D67")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0145
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0146
    ChrTalk(
        0xFE,
        "#0600F通常\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "#0601F真剣\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "#0602F微笑\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        "#0603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "#0604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "#0605F驚き\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "#0606F溜息\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "#0607F叫び\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "#0608F悲哀\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        "#0610F悔しい\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_2ED3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0156
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0157
    ChrTalk(
        0xFE,
        "#0700F通常\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        "#0702F微笑\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        "#0707F叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_2FC9")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0160
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0161
    ChrTalk(
        0xFE,
        "#0800F通常\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        "#0801F真剣\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        "#0802F微笑\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        "#0803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        "#0804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "#0805F驚き\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "#0806F溜息\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "#0807F叫び\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "#0808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        "#0809F笑い\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "#0810F泣き瞑目\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        "#0811F泣き笑い\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "#0812F泣き笑い瞑目\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "#0813F驚愕\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_3183")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0175
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0176
    ChrTalk(
        0xFE,
        "#0900F通常\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        "#0901F真剣\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        "#0902F微笑\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "#0903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "#0904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "#0905F驚き\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "#0906F溜息\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "#0907F叫び\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "#0908F悲哀\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        "#0909F笑い\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "#0910F感極まる\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "#0911F泣き笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_3315")

    label("loc_3315")

    Jump("loc_231C")

    label("loc_331A")

    EventEnd(0x1)
    Return()

    # Function_10_2310 end

    def Function_11_331D(): pass

    label("Function_11_331D")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3329")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4671")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "セルゲイ課長\x01",        # 0
            "キーア\x01",              # 1
            "ツァイト\x01",            # 2
            "セシル\x01",              # 3
            "アリオス\x01",            # 4
            "シズク\x01",              # 5
            "ヴァルド\x01",            # 6
            "イリア\x01",              # 7
            "リーシャ\x01",            # 8
            "受付嬢フラン\x01",        # 9
            "ソーニャ副司令\x01",      # 10
            "グレイス\x01",            # 11
            "イアン弁護士\x01",        # 12
            "ヨナ\x01",                # 13
            "ヨアヒム准教授\x01",      # 14
            "キャンセル\x01",          # 15
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_344B"),
        (1, "loc_35A1"),
        (2, "loc_3765"),
        (3, "loc_386B"),
        (4, "loc_39C5"),
        (5, "loc_3AFF"),
        (6, "loc_3C15"),
        (7, "loc_3D5F"),
        (8, "loc_3EA9"),
        (9, "loc_4003"),
        (10, "loc_414D"),
        (11, "loc_4287"),
        (12, "loc_43D1"),
        (13, "loc_44E7"),
        (14, "loc_4667"),
        (SWITCH_DEFAULT, "loc_466C"),
    )


    label("loc_344B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0188
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0189
    ChrTalk(
        0xFE,
        "#1000F通常\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "#1001F真剣\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        "#1002F微笑\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        "#1003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "#1005F驚き\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        "#1006F溜息\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "#1007F叫び\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        "#1009F笑い\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "#1010F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_35A1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0198
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0199
    ChrTalk(
        0xFE,
        "#1100F通常\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "#1101F真剣\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        "#1102F微笑\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        "#1103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        "#1104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "#1105F驚き\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        "#1106F溜息\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "#1107F叫び\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "#1108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "#1109F笑い\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        "#1110F通常口開き\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "#1111F思案\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        "#1112F不安\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        "#1113F睡眠\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "#1114F睡眠苦悶\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_3765")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0214
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0215
    ChrTalk(
        0xFE,
        "#1200F通常\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "#1201F真剣\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "#1203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "#1207F叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_386B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0219
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0220
    ChrTalk(
        0xFE,
        "#1300F通常\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "#1301F真剣\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "#1302F微笑\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "#1303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "#1304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        "#1305F驚き\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        "#1306F溜息\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        "#1308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        "#1309F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_39C5")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0229
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0230
    ChrTalk(
        0xFE,
        "#1400F通常\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "#1401F真剣\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        "#1402F微笑\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "#1403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        "#1404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        "#1405F驚き\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "#1407F叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_3AFF")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0237
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0238
    ChrTalk(
        0xFE,
        "#1500F通常\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        "#1501F真剣\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        "#1502F微笑\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        "#1505F驚き\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "#1508F悲哀\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_3C15")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0243
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0244
    ChrTalk(
        0xFE,
        "#1600F通常\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "#1601F真剣\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "#1602F微笑\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        "#1603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        "#1604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        "#1605F驚き\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        "#1607F叫び\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        "#1609F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_3D5F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0252
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0253
    ChrTalk(
        0xFE,
        "#1700F通常\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        "#1701F真剣\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        "#1702F微笑\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        "#1703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        "#1704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        "#1705F驚き\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "#1706F溜息\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        "#1709F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_3EA9")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0261
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0262
    ChrTalk(
        0xFE,
        "#1800F通常\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        "#1801F真剣\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        "#1802F微笑\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        "#1803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        "#1804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        "#1805F驚き\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "#1806F溜息\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        "#1808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        "#1809F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_4003")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0271
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0272
    ChrTalk(
        0xFE,
        "#1900F通常\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        "#1901F真剣\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        "#1902F微笑\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        "#1903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        "#1904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        "#1905F驚き\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        "#1906F溜息\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        "#1909F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_414D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0280
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0281
    ChrTalk(
        0xFE,
        "#2000F通常\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        "#2001F真剣\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        "#2002F微笑\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        "#2003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        "#2004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        "#2005F驚き\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        "#2006F溜息\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_4287")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0288
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0289
    ChrTalk(
        0xFE,
        "#2100F通常\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "#2101F真剣\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        "#2102F微笑\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        "#2103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        "#2104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        "#2105F驚き\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        "#2106F溜息\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        "#2109F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_43D1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0297
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0298
    ChrTalk(
        0xFE,
        "#2200F通常\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        "#2201F真剣\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        "#2202F微笑\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        "#2203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        "#2205F驚き\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_44E7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0303
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0304
    ChrTalk(
        0xFE,
        "#2300F通常\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        "#2301F真剣\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        "#2302F微笑\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        "#2303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        "#2304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        "#2305F驚き\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        "#2306F溜息\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "#2307F叫び\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        "#2309F笑い\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        "#2310F悔しい\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        "#2311F瞑目叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_466C")

    label("loc_4667")

    Jump("loc_466C")

    label("loc_466C")

    Jump("loc_3329")

    label("loc_4671")

    EventEnd(0x1)
    Return()

    # Function_11_331D end

    def Function_12_4674(): pass

    label("Function_12_4674")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4680")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5830")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "マクダエル市長\x01",      # 0
            "秘書アーネスト\x01",      # 1
            "ハルトマン議長\x01",      # 2
            "ディーター総裁\x01",      # 3
            "マリアベル\x01",          # 4
            "マルコーニ会長\x01",      # 5
            "ガルシア\x01",            # 6
            "ツァオ\x01",              # 7
            "レン\x01",                # 8
            "キリカ\x01",              # 9
            "レクター\x01",            # 10
            "ハロルド\x01",            # 11
            "ソフィア\x01",            # 12
            "コリン\x01",              # 13
            "ヨルグ老人\x01",          # 14
            "キャンセル\x01",          # 15
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_47AE"),
        (1, "loc_48D4"),
        (2, "loc_4A7A"),
        (3, "loc_4B90"),
        (4, "loc_4CCA"),
        (5, "loc_4E14"),
        (6, "loc_4E1A"),
        (7, "loc_4E1F"),
        (8, "loc_4F69"),
        (9, "loc_512F"),
        (10, "loc_5259"),
        (11, "loc_53C3"),
        (12, "loc_54E9"),
        (13, "loc_560F"),
        (14, "loc_5735"),
        (SWITCH_DEFAULT, "loc_582B"),
    )


    label("loc_47AE")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0315
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0316
    ChrTalk(
        0xFE,
        "#2500F通常\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        "#2501F真剣\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        "#2503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        "#2505F驚き\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "#2507F叫び\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        "#2509F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_48D4")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0322
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0323
    ChrTalk(
        0xFE,
        "#2600F通常\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        "#2601F真剣\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        "#2603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "#2604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        "#2605F驚き\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        "#2606F溜息\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        "#2610F通常\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        "#2611F悪役通常\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        "#2612F悪役真剣\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "#2613F悪役瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        "#2614F悪役叫び\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        "#2615F悪役瞑目叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_4A7A")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0335
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0336
    ChrTalk(
        0xFE,
        "#2700F通常\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        "#2701F真剣\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        "#2702F微笑\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        "#2703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        "#2705F驚き\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_4B90")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0341
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0342
    ChrTalk(
        0xFE,
        "#2800F通常\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "#2801F真剣\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        "#2803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "#2804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        "#2805F驚き\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        "#2806F溜息\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        "#2809F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_4CCA")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0349
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0350
    ChrTalk(
        0xFE,
        "#2900F通常\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "#2901F真剣\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        "#2902F微笑\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        "#2903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        "#2904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "#2905F驚き\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        "#2906F溜息\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        "#2909F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_4E14")

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_4E1A")

    Jump("loc_582B")

    label("loc_4E1F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0358
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0359
    ChrTalk(
        0xFE,
        "#3200F通常\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        "#3201F真剣\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        "#3202F微笑\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        "#3203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        "#3204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        "#3205F驚き\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        "#3206F溜息\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        "#3209F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_4F69")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0367
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0368
    ChrTalk(
        0xFE,
        "#3300F通常\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        "#3301F真剣\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        "#3302F微笑\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        "#3303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "#3304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        "#3305F驚き\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        "#3306F溜息\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        "#3307F叫び\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        "#3308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        "#3309F笑い\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        "#3310F瞑目叫び\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        "#3311F驚愕\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        "#3312F泣き\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        "#3313F泣き瞑目\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        "#3314F泣き笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_512F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0383
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0384
    ChrTalk(
        0xFE,
        "#3400F通常\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        "#3401F真剣\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        "#3402F微笑\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        "#3403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        "#3404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        "#3405F驚き\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_5259")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0390
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0391
    ChrTalk(
        0xFE,
        "#3500F通常\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        "#3501F真剣\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        "#3502F微笑\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        "#3503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "#3504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        "#3505F驚き\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        "#3506F溜息\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        "#3507F叫び\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        "#3509F笑い\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        "#3510F思案\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_53C3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0401
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0402
    ChrTalk(
        0xFE,
        "#3600F通常\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        "#3601F真剣\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "#3603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        "#3605F驚き\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        "#3608F悲哀\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        "#3609F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_54E9")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0408
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0409
    ChrTalk(
        0xFE,
        "#3700F通常\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        "#3701F真剣\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        "#3707F叫び\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        "#3708F悲哀\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        "#3709F笑い\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        "#3710F悲嘆\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_560F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0415
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0416
    ChrTalk(
        0xFE,
        "#3800F通常\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        "#3802F微笑\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "#3805F驚き\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        "#3809F笑い\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        "#3810F呆然\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        "#3811F泣き\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_5735")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0422
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0423
    ChrTalk(
        0xFE,
        "#3900F通常\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        "#3901F真剣\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        "#3903F瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_582B")

    label("loc_582B")

    Jump("loc_4680")

    label("loc_5830")

    EventEnd(0x1)
    Return()

    # Function_12_4674 end

    def Function_13_5833(): pass

    label("Function_13_5833")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_583F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FB4")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ロイド正装\x01",          # 0
            "ロイド正装眼鏡\x01",      # 1
            "ロイド部屋着\x01",        # 2
            "エリィ正装\x01",          # 3
            "ティオ正装\x01",          # 4
            "ティオ部屋着\x01",        # 5
            "ランディ正装\x01",        # 6
            "ワジ正装\x01",            # 7
            "キーア私服\x01",          # 8
            "セシル私服\x01",          # 9
            "キャンセル\x01",          # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5926"),
        (1, "loc_5926"),
        (2, "loc_592B"),
        (3, "loc_5AC5"),
        (4, "loc_5ACA"),
        (5, "loc_5ACF"),
        (6, "loc_5C87"),
        (7, "loc_5C8C"),
        (8, "loc_5C91"),
        (9, "loc_5E55"),
        (SWITCH_DEFAULT, "loc_5FAF"),
    )


    label("loc_5926")

    Jump("loc_5FAF")

    label("loc_592B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0426
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0427
    ChrTalk(
        0xFE,
        "#5200F通常\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        "#5201F真剣\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        "#5202F微笑\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        "#5203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        "#5204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xFE,
        "#5205F驚き\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        "#5206F溜息\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xFE,
        "#5207F叫び\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        "#5208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        "#5209F笑い\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        "#5210F苦痛\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        "#5211F慌て\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        "#5212F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FAF")

    label("loc_5AC5")

    Jump("loc_5FAF")

    label("loc_5ACA")

    Jump("loc_5FAF")

    label("loc_5ACF")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0440
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0441
    ChrTalk(
        0xFE,
        "#5500F通常\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        "#5501F真剣\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xFE,
        "#5502F微笑\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        "#5503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xFE,
        "#5504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        "#5505F驚き\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xFE,
        "#5506F溜息\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        "#5507F叫び\x02",
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        "#5508F悲哀\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        "#5509F笑い\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        "#5510F苦痛\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        "#5511Fジト目\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xFE,
        "#5512F泣き笑い\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        "#5512F泣き笑い瞑目\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FAF")

    label("loc_5C87")

    Jump("loc_5FAF")

    label("loc_5C8C")

    Jump("loc_5FAF")

    label("loc_5C91")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0455
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0456
    ChrTalk(
        0xFE,
        "#5800F通常\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        "#5801F真剣\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xFE,
        "#5802F微笑\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        "#5803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xFE,
        "#5804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        "#5805F驚き\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        "#5806F溜息\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xFE,
        "#5807F叫び\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        "#5808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        "#5809F笑い\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xFE,
        "#5810F通常口開き\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        "#5811F思案\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xFE,
        "#5812F不安\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xFE,
        "#5813F睡眠\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        "#5814F睡眠苦悶\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FAF")

    label("loc_5E55")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0471
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0472
    ChrTalk(
        0xFE,
        "#5900F通常\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xFE,
        "#5901F真剣\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xFE,
        "#5902F微笑\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xFE,
        "#5903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        "#5904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xFE,
        "#5905F驚き\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        "#5906F溜息\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xFE,
        "#5908F悲哀\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xFE,
        "#5909F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FAF")

    label("loc_5FAF")

    Jump("loc_583F")

    label("loc_5FB4")

    EventEnd(0x1)
    Return()

    # Function_13_5833 end

    def Function_14_5FB7(): pass

    label("Function_14_5FB7")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6788")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "シズク外出着\x01",            # 0
            "イリア舞台服\x01",            # 1
            "リーシャ舞台服\x01",          # 2
            "ノエル私服\x01",              # 3
            "フラン私服\x01",              # 4
            "マクダエル部屋着\x01",        # 5
            "アーネスト魔人化\x01",        # 6
            "ヨアヒム司祭服\x01",          # 7
            "ヨアヒム司祭服白髪\x01",      # 8
            "キャンセル\x01",              # 9
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_60B1"),
        (1, "loc_61C7"),
        (2, "loc_6311"),
        (3, "loc_647F"),
        (4, "loc_6484"),
        (5, "loc_65CE"),
        (6, "loc_65D3"),
        (7, "loc_6779"),
        (8, "loc_677E"),
        (SWITCH_DEFAULT, "loc_6783"),
    )


    label("loc_60B1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0481
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0482
    ChrTalk(
        0xFE,
        "#6000F通常\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        "#6001F真剣\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xFE,
        "#6002F微笑\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xFE,
        "#6005F驚き\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        "#6008F悲哀\x02",
    )

    CloseMessageWindow()
    Jump("loc_6783")

    label("loc_61C7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0487
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0488
    ChrTalk(
        0xFE,
        "#6100F通常\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xFE,
        "#6101F真剣\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        "#6102F微笑\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xFE,
        "#6103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        "#6104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xFE,
        "#6105F驚き\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        "#6106F溜息\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xFE,
        "#6109F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_6783")

    label("loc_6311")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0496
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0497
    ChrTalk(
        0xFE,
        "#6200F通常\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        "#6201F真剣\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        "#6202F微笑\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        "#6203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xFE,
        "#6204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        "#6205F驚き\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        "#6206F溜息\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xFE,
        "#6208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xFE,
        "#6209F笑い\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        "#6210F憂い笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_6783")

    label("loc_647F")

    Jump("loc_6783")

    label("loc_6484")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0507
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0508
    ChrTalk(
        0xFE,
        "#6400F通常\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xFE,
        "#6401F真剣\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xFE,
        "#6402F微笑\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        "#6403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xFE,
        "#6404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xFE,
        "#6405F驚き\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xFE,
        "#6406F溜息\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        "#6409F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_6783")

    label("loc_65CE")

    Jump("loc_6783")

    label("loc_65D3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0516
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0517
    ChrTalk(
        0xFE,
        "#6600F通常\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xFE,
        "#6601F真剣\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        "#6603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xFE,
        "#6604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        "#6605F驚き\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        "#6606F溜息\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xFE,
        "#6610F通常\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xFE,
        "#6611F悪役通常\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        "#6612F悪役真剣\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        "#6613F悪役瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        "#6614F悪役叫び\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        "#6615F悪役瞑目叫び\x02",
    )

    CloseMessageWindow()
    Jump("loc_6783")

    label("loc_6779")

    Jump("loc_6783")

    label("loc_677E")

    Jump("loc_6783")

    label("loc_6783")

    Jump("loc_5FC3")

    label("loc_6788")

    EventEnd(0x1)
    Return()

    # Function_14_5FB7 end

    def Function_15_678B(): pass

    label("Function_15_678B")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6797")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FDA")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ノエル支援課\x01",        # 0
            "ノエル国防軍服\x01",      # 1
            "ワジ支援課\x01",          # 2
            "ワジ聖騎士\x01",          # 3
            "リーシャ新衣装\x01",      # 4
            "キャンセル\x01",          # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_682B"),
        (1, "loc_69D2"),
        (2, "loc_6B79"),
        (3, "loc_6CFE"),
        (4, "loc_6E72"),
        (SWITCH_DEFAULT, "loc_6FD5"),
    )


    label("loc_682B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0529
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0530
    ChrTalk(
        0xFE,
        "#10100F通常\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xFE,
        "#10101F真剣\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xFE,
        "#10102F微笑\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        "#10103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xFE,
        "#10104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xFE,
        "#10105F驚き\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xFE,
        "#10106F溜息\x02",
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xFE,
        "#10107F叫び\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xFE,
        "#10108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xFE,
        "#10109F笑い\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xFE,
        "#10110F苦痛\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xFE,
        "#10111F慌て\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        "#10111F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FD5")

    label("loc_69D2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0543
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0544
    ChrTalk(
        0xFE,
        "#10200F通常\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xFE,
        "#10201F真剣\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xFE,
        "#10202F微笑\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xFE,
        "#10203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xFE,
        "#10204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        "#10205F驚き\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xFE,
        "#10206F溜息\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xFE,
        "#10207F叫び\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xFE,
        "#10208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        "#10209F笑い\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        "#10210F苦痛\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xFE,
        "#10211F慌て\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        "#10211F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FD5")

    label("loc_6B79")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0557
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0558
    ChrTalk(
        0xFE,
        "#10300F通常\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        "#10301F真剣\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xFE,
        "#10302F微笑\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xFE,
        "#10303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        "#10304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        "#10305F驚き\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        "#10306F溜息\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xFE,
        "#10307F叫び\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        "#10308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xFE,
        "#10309F笑い\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xFE,
        "#10310F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FD5")

    label("loc_6CFE")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0569
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0570
    ChrTalk(
        0xFE,
        "#10400F通常\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xFE,
        "#10401F真剣\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        "#10402F微笑\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xFE,
        "#10403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        "#10404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xFE,
        "#10405F驚き\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xFE,
        "#10406F溜息\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xFE,
        "#10407F叫び\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        "#10409F笑い\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xFE,
        "#10410F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FD5")

    label("loc_6E72")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0580
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0581
    ChrTalk(
        0xFE,
        "#10700F通常\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        "#10701F真剣\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xFE,
        "#10702F微笑\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        "#10703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        "#10704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xFE,
        "#10705F驚き\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        "#10706F溜息\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xFE,
        "#10708F悲哀\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        "#10709F笑い\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FD5")

    label("loc_6FD5")

    Jump("loc_6797")

    label("loc_6FDA")

    EventEnd(0x1)
    Return()

    # Function_15_678B end

    def Function_16_6FDD(): pass

    label("Function_16_6FDD")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A8")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ミシェル\x01",                  # 0
            "アッバス\x01",                  # 1
            "シュリ\x01",                    # 2
            "ケビン神父\x01",                # 3
            "シスター?リース\x01",           # 4
            "シグムント\x01",                # 5
            "シャーリィ\x01",                # 6
            "ノバルティス博士\x01",          # 7
            "カンパネルラ\x01",              # 8
            "アリアンロード\x01",            # 9
            "アリアンロード(兜無)\x01",      # 10
            "キャンセル\x01",                # 11
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_70EC"),
        (1, "loc_7271"),
        (2, "loc_73F6"),
        (3, "loc_757B"),
        (4, "loc_7700"),
        (5, "loc_7885"),
        (6, "loc_7A0A"),
        (7, "loc_7B8F"),
        (8, "loc_7D14"),
        (9, "loc_7E99"),
        (10, "loc_801E"),
        (SWITCH_DEFAULT, "loc_81A3"),
    )


    label("loc_70EC")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0590
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0591
    ChrTalk(
        0xFE,
        "#04000F通常\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xFE,
        "#04001F真剣\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xFE,
        "#04002F微笑\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xFE,
        "#04003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xFE,
        "#04004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        "#04005F驚き\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xFE,
        "#04006F溜息\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        "#04007F叫び\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xFE,
        "#04008F悲哀\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xFE,
        "#04009F笑い\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        "#04010F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_7271")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0602
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0603
    ChrTalk(
        0xFE,
        "#04100F通常\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xFE,
        "#04101F真剣\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xFE,
        "#04102F微笑\x02",
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xFE,
        "#04103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xFE,
        "#04104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xFE,
        "#04105F驚き\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0xFE,
        "#04106F溜息\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xFE,
        "#04107F叫び\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xFE,
        "#04108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xFE,
        "#04109F笑い\x02",
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xFE,
        "#04110F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_73F6")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0614
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0615
    ChrTalk(
        0xFE,
        "#04200F通常\x02",
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0xFE,
        "#04201F真剣\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        "#04202F微笑\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xFE,
        "#04203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        "#04204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0xFE,
        "#04205F驚き\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xFE,
        "#04206F溜息\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xFE,
        "#04207F叫び\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xFE,
        "#04208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        "#04209F笑い\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0xFE,
        "#04210F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_757B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0626
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0627
    ChrTalk(
        0xFE,
        "#04300F通常\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        "#04301F真剣\x02",
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xFE,
        "#04302F微笑\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xFE,
        "#04303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xFE,
        "#04304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        "#04305F驚き\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xFE,
        "#04306F溜息\x02",
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xFE,
        "#04307F叫び\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xFE,
        "#04308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        "#04309F笑い\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xFE,
        "#04310F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_7700")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0638
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0639
    ChrTalk(
        0xFE,
        "#04400F通常\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xFE,
        "#04401F真剣\x02",
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xFE,
        "#04402F微笑\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        "#04403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xFE,
        "#04404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xFE,
        "#04405F驚き\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xFE,
        "#04406F溜息\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xFE,
        "#04407F叫び\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xFE,
        "#04408F悲哀\x02",
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xFE,
        "#04409F笑い\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xFE,
        "#04410F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_7885")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0650
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0651
    ChrTalk(
        0xFE,
        "#04500F通常\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0xFE,
        "#04501F真剣\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        "#04502F微笑\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xFE,
        "#04503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0xFE,
        "#04504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0xFE,
        "#04505F驚き\x02",
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        "#04506F溜息\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0xFE,
        "#04507F叫び\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xFE,
        "#04508F悲哀\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xFE,
        "#04509F笑い\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0xFE,
        "#04510F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_7A0A")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0662
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0663
    ChrTalk(
        0xFE,
        "#04600F通常\x02",
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0xFE,
        "#04601F真剣\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0xFE,
        "#04602F微笑\x02",
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0xFE,
        "#04603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xFE,
        "#04604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xFE,
        "#04605F驚き\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xFE,
        "#04606F溜息\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0xFE,
        "#04607F叫び\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xFE,
        "#04608F悲哀\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0xFE,
        "#04609F笑い\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0xFE,
        "#04610F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_7B8F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0674
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0675
    ChrTalk(
        0xFE,
        "#04700F通常\x02",
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xFE,
        "#04701F真剣\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xFE,
        "#04702F微笑\x02",
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0xFE,
        "#04703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xFE,
        "#04704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0xFE,
        "#04705F驚き\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0xFE,
        "#04706F溜息\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0xFE,
        "#04707F叫び\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0xFE,
        "#04708F悲哀\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0xFE,
        "#04709F笑い\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0xFE,
        "#04710F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_7D14")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0686
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0687
    ChrTalk(
        0xFE,
        "#04800F通常\x02",
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0xFE,
        "#04801F真剣\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0xFE,
        "#04802F微笑\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0xFE,
        "#04803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0xFE,
        "#04804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0xFE,
        "#04805F驚き\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0xFE,
        "#04806F溜息\x02",
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0xFE,
        "#04807F叫び\x02",
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0xFE,
        "#04808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0xFE,
        "#04809F笑い\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0xFE,
        "#04810F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_7E99")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0698
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0699
    ChrTalk(
        0xFE,
        "#04900F通常\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0xFE,
        "#04901F真剣\x02",
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0xFE,
        "#04902F微笑\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0xFE,
        "#04903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0xFE,
        "#04904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0xFE,
        "#04905F驚き\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0xFE,
        "#04906F溜息\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0xFE,
        "#04907F叫び\x02",
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0xFE,
        "#04908F悲哀\x02",
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0xFE,
        "#04909F笑い\x02",
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xFE,
        "#04910F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_801E")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0710
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0711
    ChrTalk(
        0xFE,
        "#13700F通常\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0xFE,
        "#13701F真剣\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0xFE,
        "#13702F微笑\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0xFE,
        "#13703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0xFE,
        "#13704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0xFE,
        "#13705F驚き\x02",
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0xFE,
        "#13706F溜息\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0xFE,
        "#13707F叫び\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0xFE,
        "#13708F悲哀\x02",
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0xFE,
        "#13709F笑い\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0xFE,
        "#13710F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_81A3")

    label("loc_81A3")

    Jump("loc_6FE9")

    label("loc_81A8")

    EventEnd(0x1)
    Return()

    # Function_16_6FDD end

    def Function_17_81AB(): pass

    label("Function_17_81AB")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EB9")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クローディア王太女\x01",      # 0
            "ユリア准佐\x01",              # 1
            "オリヴァルト皇子\x01",        # 2
            "ミュラー中佐\x01",            # 3
            "オズボーン宰相\x01",          # 4
            "ロックスミス大統領\x01",      # 5
            "ガイ\x01",                    # 6
            "ミレイユ准尉\x01",            # 7
            "キャンセル\x01",              # 8
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_828C"),
        (1, "loc_8411"),
        (2, "loc_8596"),
        (3, "loc_871B"),
        (4, "loc_88A0"),
        (5, "loc_8A25"),
        (6, "loc_8BAA"),
        (7, "loc_8D2F"),
        (SWITCH_DEFAULT, "loc_8EB4"),
    )


    label("loc_828C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0722
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0723
    ChrTalk(
        0xFE,
        "#07000F通常\x02",
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xFE,
        "#07001F真剣\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0xFE,
        "#07002F微笑\x02",
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0xFE,
        "#07003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0xFE,
        "#07004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xFE,
        "#07005F驚き\x02",
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0xFE,
        "#07006F溜息\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0xFE,
        "#07007F叫び\x02",
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0xFE,
        "#07008F悲哀\x02",
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0xFE,
        "#07009F笑い\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0xFE,
        "#07010F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_8411")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0734
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0735
    ChrTalk(
        0xFE,
        "#07100F通常\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0xFE,
        "#07101F真剣\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0xFE,
        "#07102F微笑\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0xFE,
        "#07103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xFE,
        "#07104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xFE,
        "#07105F驚き\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xFE,
        "#07106F溜息\x02",
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xFE,
        "#07107F叫び\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xFE,
        "#07108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0xFE,
        "#07109F笑い\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0xFE,
        "#07110F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_8596")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0746
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0747
    ChrTalk(
        0xFE,
        "#07200F通常\x02",
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0xFE,
        "#07201F真剣\x02",
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0xFE,
        "#07202F微笑\x02",
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0xFE,
        "#07203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xFE,
        "#07204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0xFE,
        "#07205F驚き\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0xFE,
        "#07206F溜息\x02",
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0xFE,
        "#07207F叫び\x02",
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0xFE,
        "#07208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0xFE,
        "#07209F笑い\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xFE,
        "#07210F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_871B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0758
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0759
    ChrTalk(
        0xFE,
        "#07300F通常\x02",
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0xFE,
        "#07301F真剣\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0xFE,
        "#07302F微笑\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0xFE,
        "#07303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0xFE,
        "#07304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0xFE,
        "#07305F驚き\x02",
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0xFE,
        "#07306F溜息\x02",
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0xFE,
        "#07307F叫び\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0xFE,
        "#07308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0xFE,
        "#07309F笑い\x02",
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0xFE,
        "#07310F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_88A0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0770
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0771
    ChrTalk(
        0xFE,
        "#07400F通常\x02",
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0xFE,
        "#07401F真剣\x02",
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0xFE,
        "#07402F微笑\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0xFE,
        "#07403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xFE,
        "#07404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0xFE,
        "#07405F驚き\x02",
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0xFE,
        "#07406F溜息\x02",
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xFE,
        "#07407F叫び\x02",
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0xFE,
        "#07408F悲哀\x02",
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0xFE,
        "#07409F笑い\x02",
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0xFE,
        "#07410F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_8A25")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0782
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0783
    ChrTalk(
        0xFE,
        "#07500F通常\x02",
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0xFE,
        "#07501F真剣\x02",
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0xFE,
        "#07502F微笑\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0xFE,
        "#07503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0xFE,
        "#07504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0xFE,
        "#07505F驚き\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0xFE,
        "#07506F溜息\x02",
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0xFE,
        "#07507F叫び\x02",
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0xFE,
        "#07508F悲哀\x02",
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0xFE,
        "#07509F笑い\x02",
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0xFE,
        "#07510F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_8BAA")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0794
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0795
    ChrTalk(
        0xFE,
        "#07800F通常\x02",
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0xFE,
        "#07801F真剣\x02",
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0xFE,
        "#07802F微笑\x02",
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0xFE,
        "#07803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0xFE,
        "#07804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0xFE,
        "#07805F驚き\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0xFE,
        "#07806F溜息\x02",
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0xFE,
        "#07807F叫び\x02",
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0xFE,
        "#07808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0xFE,
        "#07809F笑い\x02",
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0xFE,
        "#07810F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_8D2F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0806
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0807
    ChrTalk(
        0xFE,
        "#07900F通常\x02",
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0xFE,
        "#07901F真剣\x02",
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0xFE,
        "#07902F微笑\x02",
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0xFE,
        "#07903F瞑目\x02",
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0xFE,
        "#07904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0xFE,
        "#07905F驚き\x02",
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0xFE,
        "#07906F溜息\x02",
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0xFE,
        "#07907F叫び\x02",
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0xFE,
        "#07908F悲哀\x02",
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0xFE,
        "#07909F笑い\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0xFE,
        "#07910F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EB4")

    label("loc_8EB4")

    Jump("loc_81B7")

    label("loc_8EB9")

    EventEnd(0x1)
    Return()

    # Function_17_81AB end

    def Function_18_8EBC(): pass

    label("Function_18_8EBC")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8EC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A586")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ソーニャ（国防軍服）\x01",      # 0
            "マリアベル（魔女風）\x01",      # 1
            "ランディ警備隊制服\x01",        # 2
            "ガルシア(ワイシャツ)\x01",      # 3
            "シズク目が見える\x01",          # 4
            "ディーター大統領\x01",          # 5
            "レクター書記官服\x01",          # 6
            "イリア入院服\x01",              # 7
            "フラン入院服\x01",              # 8
            "キリカ後編服\x01",              # 9
            "アッバス（騎士装束）\x01",      # 10
            "シュリ舞台衣装\x01",            # 11
            "キーア13歳\x01",                # 12
            "ミュラー変装版\x01",            # 13
            "キャンセル\x01",                # 14
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_903B"),
        (1, "loc_91C0"),
        (2, "loc_9345"),
        (3, "loc_94CA"),
        (4, "loc_964F"),
        (5, "loc_97D4"),
        (6, "loc_9959"),
        (7, "loc_9ADE"),
        (8, "loc_9C63"),
        (9, "loc_9DE8"),
        (10, "loc_9F6D"),
        (11, "loc_A0F2"),
        (12, "loc_A277"),
        (13, "loc_A3FC"),
        (SWITCH_DEFAULT, "loc_A581"),
    )


    label("loc_903B")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0818
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0819
    ChrTalk(
        0xFE,
        "#10600F通常\x02",
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0xFE,
        "#10601F真剣\x02",
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0xFE,
        "#10602F微笑\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0xFE,
        "#10603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0xFE,
        "#10604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0xFE,
        "#10605F驚き\x02",
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0xFE,
        "#10606F溜息\x02",
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0xFE,
        "#10607F叫び\x02",
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0xFE,
        "#10608F悲哀\x02",
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0xFE,
        "#10609F笑い\x02",
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0xFE,
        "#10610F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_91C0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0830
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0831
    ChrTalk(
        0xFE,
        "#10800F通常\x02",
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0xFE,
        "#10801F真剣\x02",
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0xFE,
        "#10802F微笑\x02",
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0xFE,
        "#10803F瞑目\x02",
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0xFE,
        "#10804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0xFE,
        "#10805F驚き\x02",
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0xFE,
        "#10806F溜息\x02",
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0xFE,
        "#10807F叫び\x02",
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0xFE,
        "#10808F悲哀\x02",
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0xFE,
        "#10809F笑い\x02",
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0xFE,
        "#10810F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_9345")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0842
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0843
    ChrTalk(
        0xFE,
        "#11000F通常\x02",
    )

    CloseMessageWindow()

    #C0844
    ChrTalk(
        0xFE,
        "#11001F真剣\x02",
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0xFE,
        "#11002F微笑\x02",
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0xFE,
        "#11003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0xFE,
        "#11004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0xFE,
        "#11005F驚き\x02",
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0xFE,
        "#11006F溜息\x02",
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0xFE,
        "#11007F叫び\x02",
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0xFE,
        "#11008F悲哀\x02",
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0xFE,
        "#11009F笑い\x02",
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0xFE,
        "#11010F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_94CA")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0854
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0855
    ChrTalk(
        0xFE,
        "#11100F通常\x02",
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0xFE,
        "#11101F真剣\x02",
    )

    CloseMessageWindow()

    #C0857
    ChrTalk(
        0xFE,
        "#11102F微笑\x02",
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0xFE,
        "#11103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0xFE,
        "#11104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0xFE,
        "#11105F驚き\x02",
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0xFE,
        "#11106F溜息\x02",
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0xFE,
        "#11107F叫び\x02",
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0xFE,
        "#11108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0xFE,
        "#11109F笑い\x02",
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0xFE,
        "#11110F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_964F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0866
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0867
    ChrTalk(
        0xFE,
        "#11200F通常\x02",
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0xFE,
        "#11201F真剣\x02",
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0xFE,
        "#11202F微笑\x02",
    )

    CloseMessageWindow()

    #C0870
    ChrTalk(
        0xFE,
        "#11203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0871
    ChrTalk(
        0xFE,
        "#11204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0xFE,
        "#11205F驚き\x02",
    )

    CloseMessageWindow()

    #C0873
    ChrTalk(
        0xFE,
        "#11206F溜息\x02",
    )

    CloseMessageWindow()

    #C0874
    ChrTalk(
        0xFE,
        "#11207F叫び\x02",
    )

    CloseMessageWindow()

    #C0875
    ChrTalk(
        0xFE,
        "#11208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0876
    ChrTalk(
        0xFE,
        "#11209F笑い\x02",
    )

    CloseMessageWindow()

    #C0877
    ChrTalk(
        0xFE,
        "#11210F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_97D4")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0878
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0879
    ChrTalk(
        0xFE,
        "#11300F通常\x02",
    )

    CloseMessageWindow()

    #C0880
    ChrTalk(
        0xFE,
        "#11301F真剣\x02",
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0xFE,
        "#11302F微笑\x02",
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0xFE,
        "#11303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0883
    ChrTalk(
        0xFE,
        "#11304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0884
    ChrTalk(
        0xFE,
        "#11305F驚き\x02",
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0xFE,
        "#11306F溜息\x02",
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0xFE,
        "#11307F叫び\x02",
    )

    CloseMessageWindow()

    #C0887
    ChrTalk(
        0xFE,
        "#11308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0888
    ChrTalk(
        0xFE,
        "#11309F笑い\x02",
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0xFE,
        "#11310F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_9959")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0890
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0891
    ChrTalk(
        0xFE,
        "#11500F通常\x02",
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0xFE,
        "#11501F真剣\x02",
    )

    CloseMessageWindow()

    #C0893
    ChrTalk(
        0xFE,
        "#11502F微笑\x02",
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0xFE,
        "#11503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0xFE,
        "#11504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0xFE,
        "#11505F驚き\x02",
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0xFE,
        "#11506F溜息\x02",
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0xFE,
        "#11507F叫び\x02",
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0xFE,
        "#11508F悲哀\x02",
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0xFE,
        "#11509F笑い\x02",
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0xFE,
        "#11510F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_9ADE")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0902
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0903
    ChrTalk(
        0xFE,
        "#11600F通常\x02",
    )

    CloseMessageWindow()

    #C0904
    ChrTalk(
        0xFE,
        "#11601F真剣\x02",
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0xFE,
        "#11602F微笑\x02",
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0xFE,
        "#11603F瞑目\x02",
    )

    CloseMessageWindow()

    #C0907
    ChrTalk(
        0xFE,
        "#11604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0908
    ChrTalk(
        0xFE,
        "#11605F驚き\x02",
    )

    CloseMessageWindow()

    #C0909
    ChrTalk(
        0xFE,
        "#11606F溜息\x02",
    )

    CloseMessageWindow()

    #C0910
    ChrTalk(
        0xFE,
        "#11607F叫び\x02",
    )

    CloseMessageWindow()

    #C0911
    ChrTalk(
        0xFE,
        "#11608F悲哀\x02",
    )

    CloseMessageWindow()

    #C0912
    ChrTalk(
        0xFE,
        "#11609F笑い\x02",
    )

    CloseMessageWindow()

    #C0913
    ChrTalk(
        0xFE,
        "#11610F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_9C63")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0914
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0915
    ChrTalk(
        0xFE,
        "#11700F通常\x02",
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0xFE,
        "#11701F真剣\x02",
    )

    CloseMessageWindow()

    #C0917
    ChrTalk(
        0xFE,
        "#11702F微笑\x02",
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0xFE,
        "#11703F瞑目\x02",
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0xFE,
        "#11704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0920
    ChrTalk(
        0xFE,
        "#11705F驚き\x02",
    )

    CloseMessageWindow()

    #C0921
    ChrTalk(
        0xFE,
        "#11706F溜息\x02",
    )

    CloseMessageWindow()

    #C0922
    ChrTalk(
        0xFE,
        "#11707F叫び\x02",
    )

    CloseMessageWindow()

    #C0923
    ChrTalk(
        0xFE,
        "#11708F悲哀\x02",
    )

    CloseMessageWindow()

    #C0924
    ChrTalk(
        0xFE,
        "#11709F笑い\x02",
    )

    CloseMessageWindow()

    #C0925
    ChrTalk(
        0xFE,
        "#11710F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_9DE8")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0926
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0927
    ChrTalk(
        0xFE,
        "#12000F通常\x02",
    )

    CloseMessageWindow()

    #C0928
    ChrTalk(
        0xFE,
        "#12001F真剣\x02",
    )

    CloseMessageWindow()

    #C0929
    ChrTalk(
        0xFE,
        "#12002F微笑\x02",
    )

    CloseMessageWindow()

    #C0930
    ChrTalk(
        0xFE,
        "#12003F瞑目\x02",
    )

    CloseMessageWindow()

    #C0931
    ChrTalk(
        0xFE,
        "#12004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0932
    ChrTalk(
        0xFE,
        "#12005F驚き\x02",
    )

    CloseMessageWindow()

    #C0933
    ChrTalk(
        0xFE,
        "#12006F溜息\x02",
    )

    CloseMessageWindow()

    #C0934
    ChrTalk(
        0xFE,
        "#12007F叫び\x02",
    )

    CloseMessageWindow()

    #C0935
    ChrTalk(
        0xFE,
        "#12008F悲哀\x02",
    )

    CloseMessageWindow()

    #C0936
    ChrTalk(
        0xFE,
        "#12009F笑い\x02",
    )

    CloseMessageWindow()

    #C0937
    ChrTalk(
        0xFE,
        "#12010F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_9F6D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0938
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0939
    ChrTalk(
        0xFE,
        "#12100F通常\x02",
    )

    CloseMessageWindow()

    #C0940
    ChrTalk(
        0xFE,
        "#12101F真剣\x02",
    )

    CloseMessageWindow()

    #C0941
    ChrTalk(
        0xFE,
        "#12102F微笑\x02",
    )

    CloseMessageWindow()

    #C0942
    ChrTalk(
        0xFE,
        "#12103F瞑目\x02",
    )

    CloseMessageWindow()

    #C0943
    ChrTalk(
        0xFE,
        "#12104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0944
    ChrTalk(
        0xFE,
        "#12105F驚き\x02",
    )

    CloseMessageWindow()

    #C0945
    ChrTalk(
        0xFE,
        "#12106F溜息\x02",
    )

    CloseMessageWindow()

    #C0946
    ChrTalk(
        0xFE,
        "#12107F叫び\x02",
    )

    CloseMessageWindow()

    #C0947
    ChrTalk(
        0xFE,
        "#12108F悲哀\x02",
    )

    CloseMessageWindow()

    #C0948
    ChrTalk(
        0xFE,
        "#12109F笑い\x02",
    )

    CloseMessageWindow()

    #C0949
    ChrTalk(
        0xFE,
        "#12110F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_A0F2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0950
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0951
    ChrTalk(
        0xFE,
        "#12200F通常\x02",
    )

    CloseMessageWindow()

    #C0952
    ChrTalk(
        0xFE,
        "#12201F真剣\x02",
    )

    CloseMessageWindow()

    #C0953
    ChrTalk(
        0xFE,
        "#12202F微笑\x02",
    )

    CloseMessageWindow()

    #C0954
    ChrTalk(
        0xFE,
        "#12203F瞑目\x02",
    )

    CloseMessageWindow()

    #C0955
    ChrTalk(
        0xFE,
        "#12204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0956
    ChrTalk(
        0xFE,
        "#12205F驚き\x02",
    )

    CloseMessageWindow()

    #C0957
    ChrTalk(
        0xFE,
        "#12206F溜息\x02",
    )

    CloseMessageWindow()

    #C0958
    ChrTalk(
        0xFE,
        "#12207F叫び\x02",
    )

    CloseMessageWindow()

    #C0959
    ChrTalk(
        0xFE,
        "#12208F悲哀\x02",
    )

    CloseMessageWindow()

    #C0960
    ChrTalk(
        0xFE,
        "#12209F笑い\x02",
    )

    CloseMessageWindow()

    #C0961
    ChrTalk(
        0xFE,
        "#12210F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_A277")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0962
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0963
    ChrTalk(
        0xFE,
        "#12300F通常\x02",
    )

    CloseMessageWindow()

    #C0964
    ChrTalk(
        0xFE,
        "#12301F真剣\x02",
    )

    CloseMessageWindow()

    #C0965
    ChrTalk(
        0xFE,
        "#12302F微笑\x02",
    )

    CloseMessageWindow()

    #C0966
    ChrTalk(
        0xFE,
        "#12303F瞑目\x02",
    )

    CloseMessageWindow()

    #C0967
    ChrTalk(
        0xFE,
        "#12304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0968
    ChrTalk(
        0xFE,
        "#12305F驚き\x02",
    )

    CloseMessageWindow()

    #C0969
    ChrTalk(
        0xFE,
        "#12306F溜息\x02",
    )

    CloseMessageWindow()

    #C0970
    ChrTalk(
        0xFE,
        "#12307F叫び\x02",
    )

    CloseMessageWindow()

    #C0971
    ChrTalk(
        0xFE,
        "#12308F悲哀\x02",
    )

    CloseMessageWindow()

    #C0972
    ChrTalk(
        0xFE,
        "#12309F笑い\x02",
    )

    CloseMessageWindow()

    #C0973
    ChrTalk(
        0xFE,
        "#12310F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_A3FC")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0974
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0975
    ChrTalk(
        0xFE,
        "#12400F通常\x02",
    )

    CloseMessageWindow()

    #C0976
    ChrTalk(
        0xFE,
        "#12401F真剣\x02",
    )

    CloseMessageWindow()

    #C0977
    ChrTalk(
        0xFE,
        "#12402F微笑\x02",
    )

    CloseMessageWindow()

    #C0978
    ChrTalk(
        0xFE,
        "#12403F瞑目\x02",
    )

    CloseMessageWindow()

    #C0979
    ChrTalk(
        0xFE,
        "#12404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0980
    ChrTalk(
        0xFE,
        "#12405F驚き\x02",
    )

    CloseMessageWindow()

    #C0981
    ChrTalk(
        0xFE,
        "#12406F溜息\x02",
    )

    CloseMessageWindow()

    #C0982
    ChrTalk(
        0xFE,
        "#12407F叫び\x02",
    )

    CloseMessageWindow()

    #C0983
    ChrTalk(
        0xFE,
        "#12408F悲哀\x02",
    )

    CloseMessageWindow()

    #C0984
    ChrTalk(
        0xFE,
        "#12409F笑い\x02",
    )

    CloseMessageWindow()

    #C0985
    ChrTalk(
        0xFE,
        "#12410F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_A581")

    Jump("loc_8EC8")

    label("loc_A586")

    EventEnd(0x1)
    Return()

    # Function_18_8EBC end

    def Function_19_A589(): pass

    label("Function_19_A589")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A595")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8FB")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ロイド水着\x01",        # 0
            "エリィ水着\x01",        # 1
            "ティオ水着\x01",        # 2
            "ランディ水着\x01",      # 3
            "ワジ水着\x01",          # 4
            "ノエル水着\x01",        # 5
            "フラン水着\x01",        # 6
            "キーア水着\x01",        # 7
            "セシル水着\x01",        # 8
            "イリア水着\x01",        # 9
            "リーシャ水着\x01",      # 10
            "シュリ水着\x01",        # 11
            "キャンセル\x01",        # 12
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A698"),
        (1, "loc_A81D"),
        (2, "loc_A9A2"),
        (3, "loc_AB27"),
        (4, "loc_ACAC"),
        (5, "loc_AE31"),
        (6, "loc_AFD8"),
        (7, "loc_B15D"),
        (8, "loc_B2E2"),
        (9, "loc_B467"),
        (10, "loc_B5EC"),
        (11, "loc_B771"),
        (SWITCH_DEFAULT, "loc_B8F6"),
    )


    label("loc_A698")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0986
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0987
    ChrTalk(
        0xFE,
        "#12500F通常\x02",
    )

    CloseMessageWindow()

    #C0988
    ChrTalk(
        0xFE,
        "#12501F真剣\x02",
    )

    CloseMessageWindow()

    #C0989
    ChrTalk(
        0xFE,
        "#12502F微笑\x02",
    )

    CloseMessageWindow()

    #C0990
    ChrTalk(
        0xFE,
        "#12503F瞑目\x02",
    )

    CloseMessageWindow()

    #C0991
    ChrTalk(
        0xFE,
        "#12504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C0992
    ChrTalk(
        0xFE,
        "#12505F驚き\x02",
    )

    CloseMessageWindow()

    #C0993
    ChrTalk(
        0xFE,
        "#12506F溜息\x02",
    )

    CloseMessageWindow()

    #C0994
    ChrTalk(
        0xFE,
        "#12507F叫び\x02",
    )

    CloseMessageWindow()

    #C0995
    ChrTalk(
        0xFE,
        "#12508F悲哀\x02",
    )

    CloseMessageWindow()

    #C0996
    ChrTalk(
        0xFE,
        "#12509F笑い\x02",
    )

    CloseMessageWindow()

    #C0997
    ChrTalk(
        0xFE,
        "#12510F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_A81D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A0998
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0999
    ChrTalk(
        0xFE,
        "#12600F通常\x02",
    )

    CloseMessageWindow()

    #C1000
    ChrTalk(
        0xFE,
        "#12601F真剣\x02",
    )

    CloseMessageWindow()

    #C1001
    ChrTalk(
        0xFE,
        "#12602F微笑\x02",
    )

    CloseMessageWindow()

    #C1002
    ChrTalk(
        0xFE,
        "#12603F瞑目\x02",
    )

    CloseMessageWindow()

    #C1003
    ChrTalk(
        0xFE,
        "#12604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1004
    ChrTalk(
        0xFE,
        "#12605F驚き\x02",
    )

    CloseMessageWindow()

    #C1005
    ChrTalk(
        0xFE,
        "#12606F溜息\x02",
    )

    CloseMessageWindow()

    #C1006
    ChrTalk(
        0xFE,
        "#12607F叫び\x02",
    )

    CloseMessageWindow()

    #C1007
    ChrTalk(
        0xFE,
        "#12608F悲哀\x02",
    )

    CloseMessageWindow()

    #C1008
    ChrTalk(
        0xFE,
        "#12609F笑い\x02",
    )

    CloseMessageWindow()

    #C1009
    ChrTalk(
        0xFE,
        "#12610F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_A9A2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12700.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1010
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1011
    ChrTalk(
        0xFE,
        "#12700F通常\x02",
    )

    CloseMessageWindow()

    #C1012
    ChrTalk(
        0xFE,
        "#12701F真剣\x02",
    )

    CloseMessageWindow()

    #C1013
    ChrTalk(
        0xFE,
        "#12702F微笑\x02",
    )

    CloseMessageWindow()

    #C1014
    ChrTalk(
        0xFE,
        "#12703F瞑目\x02",
    )

    CloseMessageWindow()

    #C1015
    ChrTalk(
        0xFE,
        "#12704F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1016
    ChrTalk(
        0xFE,
        "#12705F驚き\x02",
    )

    CloseMessageWindow()

    #C1017
    ChrTalk(
        0xFE,
        "#12706F溜息\x02",
    )

    CloseMessageWindow()

    #C1018
    ChrTalk(
        0xFE,
        "#12707F叫び\x02",
    )

    CloseMessageWindow()

    #C1019
    ChrTalk(
        0xFE,
        "#12708F悲哀\x02",
    )

    CloseMessageWindow()

    #C1020
    ChrTalk(
        0xFE,
        "#12709F笑い\x02",
    )

    CloseMessageWindow()

    #C1021
    ChrTalk(
        0xFE,
        "#12710F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_AB27")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12800.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1022
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1023
    ChrTalk(
        0xFE,
        "#12800F通常\x02",
    )

    CloseMessageWindow()

    #C1024
    ChrTalk(
        0xFE,
        "#12801F真剣\x02",
    )

    CloseMessageWindow()

    #C1025
    ChrTalk(
        0xFE,
        "#12802F微笑\x02",
    )

    CloseMessageWindow()

    #C1026
    ChrTalk(
        0xFE,
        "#12803F瞑目\x02",
    )

    CloseMessageWindow()

    #C1027
    ChrTalk(
        0xFE,
        "#12804F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1028
    ChrTalk(
        0xFE,
        "#12805F驚き\x02",
    )

    CloseMessageWindow()

    #C1029
    ChrTalk(
        0xFE,
        "#12806F溜息\x02",
    )

    CloseMessageWindow()

    #C1030
    ChrTalk(
        0xFE,
        "#12807F叫び\x02",
    )

    CloseMessageWindow()

    #C1031
    ChrTalk(
        0xFE,
        "#12808F悲哀\x02",
    )

    CloseMessageWindow()

    #C1032
    ChrTalk(
        0xFE,
        "#12809F笑い\x02",
    )

    CloseMessageWindow()

    #C1033
    ChrTalk(
        0xFE,
        "#12810F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_ACAC")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12900.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1034
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1035
    ChrTalk(
        0xFE,
        "#12900F通常\x02",
    )

    CloseMessageWindow()

    #C1036
    ChrTalk(
        0xFE,
        "#12901F真剣\x02",
    )

    CloseMessageWindow()

    #C1037
    ChrTalk(
        0xFE,
        "#12902F微笑\x02",
    )

    CloseMessageWindow()

    #C1038
    ChrTalk(
        0xFE,
        "#12903F瞑目\x02",
    )

    CloseMessageWindow()

    #C1039
    ChrTalk(
        0xFE,
        "#12904F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1040
    ChrTalk(
        0xFE,
        "#12905F驚き\x02",
    )

    CloseMessageWindow()

    #C1041
    ChrTalk(
        0xFE,
        "#12906F溜息\x02",
    )

    CloseMessageWindow()

    #C1042
    ChrTalk(
        0xFE,
        "#12907F叫び\x02",
    )

    CloseMessageWindow()

    #C1043
    ChrTalk(
        0xFE,
        "#12908F悲哀\x02",
    )

    CloseMessageWindow()

    #C1044
    ChrTalk(
        0xFE,
        "#12909F笑い\x02",
    )

    CloseMessageWindow()

    #C1045
    ChrTalk(
        0xFE,
        "#12910F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_AE31")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13000.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1046
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1047
    ChrTalk(
        0xFE,
        "#13000F通常\x02",
    )

    CloseMessageWindow()

    #C1048
    ChrTalk(
        0xFE,
        "#13001F真剣\x02",
    )

    CloseMessageWindow()

    #C1049
    ChrTalk(
        0xFE,
        "#13002F微笑\x02",
    )

    CloseMessageWindow()

    #C1050
    ChrTalk(
        0xFE,
        "#13003F瞑目\x02",
    )

    CloseMessageWindow()

    #C1051
    ChrTalk(
        0xFE,
        "#13004F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1052
    ChrTalk(
        0xFE,
        "#13005F驚き\x02",
    )

    CloseMessageWindow()

    #C1053
    ChrTalk(
        0xFE,
        "#13006F溜息\x02",
    )

    CloseMessageWindow()

    #C1054
    ChrTalk(
        0xFE,
        "#13007F叫び\x02",
    )

    CloseMessageWindow()

    #C1055
    ChrTalk(
        0xFE,
        "#13008F悲哀\x02",
    )

    CloseMessageWindow()

    #C1056
    ChrTalk(
        0xFE,
        "#13009F笑い\x02",
    )

    CloseMessageWindow()

    #C1057
    ChrTalk(
        0xFE,
        "#13010F苦痛\x02",
    )

    CloseMessageWindow()

    #C1058
    ChrTalk(
        0xFE,
        "#13011F慌て\x02",
    )

    CloseMessageWindow()

    #C1059
    ChrTalk(
        0xFE,
        "#13012F苦笑\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_AFD8")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13100.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1060
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1061
    ChrTalk(
        0xFE,
        "#13100F通常\x02",
    )

    CloseMessageWindow()

    #C1062
    ChrTalk(
        0xFE,
        "#13101F真剣\x02",
    )

    CloseMessageWindow()

    #C1063
    ChrTalk(
        0xFE,
        "#13102F微笑\x02",
    )

    CloseMessageWindow()

    #C1064
    ChrTalk(
        0xFE,
        "#13103F瞑目\x02",
    )

    CloseMessageWindow()

    #C1065
    ChrTalk(
        0xFE,
        "#13104F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1066
    ChrTalk(
        0xFE,
        "#13105F驚き\x02",
    )

    CloseMessageWindow()

    #C1067
    ChrTalk(
        0xFE,
        "#13106F溜息\x02",
    )

    CloseMessageWindow()

    #C1068
    ChrTalk(
        0xFE,
        "#13107F叫び\x02",
    )

    CloseMessageWindow()

    #C1069
    ChrTalk(
        0xFE,
        "#13108F悲哀\x02",
    )

    CloseMessageWindow()

    #C1070
    ChrTalk(
        0xFE,
        "#13109F笑い\x02",
    )

    CloseMessageWindow()

    #C1071
    ChrTalk(
        0xFE,
        "#13110F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_B15D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13200.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1072
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1073
    ChrTalk(
        0xFE,
        "#13200F通常\x02",
    )

    CloseMessageWindow()

    #C1074
    ChrTalk(
        0xFE,
        "#13201F真剣\x02",
    )

    CloseMessageWindow()

    #C1075
    ChrTalk(
        0xFE,
        "#13202F微笑\x02",
    )

    CloseMessageWindow()

    #C1076
    ChrTalk(
        0xFE,
        "#13203F瞑目\x02",
    )

    CloseMessageWindow()

    #C1077
    ChrTalk(
        0xFE,
        "#13204F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1078
    ChrTalk(
        0xFE,
        "#13205F驚き\x02",
    )

    CloseMessageWindow()

    #C1079
    ChrTalk(
        0xFE,
        "#13206F溜息\x02",
    )

    CloseMessageWindow()

    #C1080
    ChrTalk(
        0xFE,
        "#13207F叫び\x02",
    )

    CloseMessageWindow()

    #C1081
    ChrTalk(
        0xFE,
        "#13208F悲哀\x02",
    )

    CloseMessageWindow()

    #C1082
    ChrTalk(
        0xFE,
        "#13209F笑い\x02",
    )

    CloseMessageWindow()

    #C1083
    ChrTalk(
        0xFE,
        "#13210F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_B2E2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13300.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1084
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1085
    ChrTalk(
        0xFE,
        "#13300F通常\x02",
    )

    CloseMessageWindow()

    #C1086
    ChrTalk(
        0xFE,
        "#13301F真剣\x02",
    )

    CloseMessageWindow()

    #C1087
    ChrTalk(
        0xFE,
        "#13302F微笑\x02",
    )

    CloseMessageWindow()

    #C1088
    ChrTalk(
        0xFE,
        "#13303F瞑目\x02",
    )

    CloseMessageWindow()

    #C1089
    ChrTalk(
        0xFE,
        "#13304F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1090
    ChrTalk(
        0xFE,
        "#13305F驚き\x02",
    )

    CloseMessageWindow()

    #C1091
    ChrTalk(
        0xFE,
        "#13306F溜息\x02",
    )

    CloseMessageWindow()

    #C1092
    ChrTalk(
        0xFE,
        "#13307F叫び\x02",
    )

    CloseMessageWindow()

    #C1093
    ChrTalk(
        0xFE,
        "#13308F悲哀\x02",
    )

    CloseMessageWindow()

    #C1094
    ChrTalk(
        0xFE,
        "#13309F笑い\x02",
    )

    CloseMessageWindow()

    #C1095
    ChrTalk(
        0xFE,
        "#13310F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_B467")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13400.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1096
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1097
    ChrTalk(
        0xFE,
        "#13400F通常\x02",
    )

    CloseMessageWindow()

    #C1098
    ChrTalk(
        0xFE,
        "#13401F真剣\x02",
    )

    CloseMessageWindow()

    #C1099
    ChrTalk(
        0xFE,
        "#13402F微笑\x02",
    )

    CloseMessageWindow()

    #C1100
    ChrTalk(
        0xFE,
        "#13403F瞑目\x02",
    )

    CloseMessageWindow()

    #C1101
    ChrTalk(
        0xFE,
        "#13404F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1102
    ChrTalk(
        0xFE,
        "#13405F驚き\x02",
    )

    CloseMessageWindow()

    #C1103
    ChrTalk(
        0xFE,
        "#13406F溜息\x02",
    )

    CloseMessageWindow()

    #C1104
    ChrTalk(
        0xFE,
        "#13407F叫び\x02",
    )

    CloseMessageWindow()

    #C1105
    ChrTalk(
        0xFE,
        "#13408F悲哀\x02",
    )

    CloseMessageWindow()

    #C1106
    ChrTalk(
        0xFE,
        "#13409F笑い\x02",
    )

    CloseMessageWindow()

    #C1107
    ChrTalk(
        0xFE,
        "#13410F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_B5EC")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1108
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1109
    ChrTalk(
        0xFE,
        "#13500F通常\x02",
    )

    CloseMessageWindow()

    #C1110
    ChrTalk(
        0xFE,
        "#13501F真剣\x02",
    )

    CloseMessageWindow()

    #C1111
    ChrTalk(
        0xFE,
        "#13502F微笑\x02",
    )

    CloseMessageWindow()

    #C1112
    ChrTalk(
        0xFE,
        "#13503F瞑目\x02",
    )

    CloseMessageWindow()

    #C1113
    ChrTalk(
        0xFE,
        "#13504F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1114
    ChrTalk(
        0xFE,
        "#13505F驚き\x02",
    )

    CloseMessageWindow()

    #C1115
    ChrTalk(
        0xFE,
        "#13506F溜息\x02",
    )

    CloseMessageWindow()

    #C1116
    ChrTalk(
        0xFE,
        "#13507F叫び\x02",
    )

    CloseMessageWindow()

    #C1117
    ChrTalk(
        0xFE,
        "#13508F悲哀\x02",
    )

    CloseMessageWindow()

    #C1118
    ChrTalk(
        0xFE,
        "#13509F笑い\x02",
    )

    CloseMessageWindow()

    #C1119
    ChrTalk(
        0xFE,
        "#13510F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_B771")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13600.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("チェック用")

    #A1120
    AnonymousTalk(
        0xFF,
        "バスト位置チェック\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C1121
    ChrTalk(
        0xFE,
        "#13600F通常\x02",
    )

    CloseMessageWindow()

    #C1122
    ChrTalk(
        0xFE,
        "#13601F真剣\x02",
    )

    CloseMessageWindow()

    #C1123
    ChrTalk(
        0xFE,
        "#13602F微笑\x02",
    )

    CloseMessageWindow()

    #C1124
    ChrTalk(
        0xFE,
        "#13603F瞑目\x02",
    )

    CloseMessageWindow()

    #C1125
    ChrTalk(
        0xFE,
        "#13604F瞑目微笑\x02",
    )

    CloseMessageWindow()

    #C1126
    ChrTalk(
        0xFE,
        "#13605F驚き\x02",
    )

    CloseMessageWindow()

    #C1127
    ChrTalk(
        0xFE,
        "#13606F溜息\x02",
    )

    CloseMessageWindow()

    #C1128
    ChrTalk(
        0xFE,
        "#13607F叫び\x02",
    )

    CloseMessageWindow()

    #C1129
    ChrTalk(
        0xFE,
        "#13608F悲哀\x02",
    )

    CloseMessageWindow()

    #C1130
    ChrTalk(
        0xFE,
        "#13609F笑い\x02",
    )

    CloseMessageWindow()

    #C1131
    ChrTalk(
        0xFE,
        "#13610F苦痛\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8F6")

    label("loc_B8F6")

    Jump("loc_A595")

    label("loc_B8FB")

    EventEnd(0x1)
    Return()

    # Function_19_A589 end

    def Function_20_B8FE(): pass

    label("Function_20_B8FE")

    TalkBegin(0xFE)

    #C1132
    ChrTalk(
        0xFE,
        (
            "あいうえおかきくけこ\x01",
            "アイウエオカキクケコ\x01",
            "亜意宇絵尾化木区毛故\x02",
        )
    )

    CloseMessageWindow()

    #C1133
    ChrTalk(
        0xFE,
        (
            "導力器#6Rオーブメント#\x01",
            "遊撃士#6R ブレイサー#\x01",
            "遊撃士協会#10R　ブレイサーギルド#\x02",
        )
    )

    CloseMessageWindow()

    #C1134
    ChrTalk(
        0xFE,
        (
            "《身喰らう蛇#10R　 ウ ロ ボ ロ ス#》\x01",
            "《蛇の使徒#8R　ア ン ギ ス#》\x01",
            "《結晶回路#8R　ク オ ー ツ#》\x02",
        )
    )

    CloseMessageWindow()

    #C1135
    ChrTalk(
        0xFE,
        (
            "㈱ハート(株)　?TM(中)\x01",
            "?(C)昭和　　?(R)平成\x01",
            "(C)(R)\x02",
        )
    )

    CloseMessageWindow()

    #C1136
    ChrTalk(
        0xFE,
        (
            "ＡAＢBＣCＤDＥEＦFＧG\x01",
            "ａaｂbｃcｄdｅeｆfｇg\x01",
            "　01234567890123456789ⅠⅡⅢ\x02",
        )
    )

    CloseMessageWindow()

    #C1137
    ChrTalk(
        0xFE,
        (
            "　01234567890123456789.,/+*-\x01",
            "　ABCDEFGHIJKLMNOPQRSTUVWXYZ\x01",
            "　abcdefghijklmnopqrstuvwxyz\x01",
            "　ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ\x01",
            "　ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_B8FE end

    SaveToFile()

Try(main)
