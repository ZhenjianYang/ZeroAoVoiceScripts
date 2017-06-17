from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0000.bin",                # FileName
        "e0000",                    # MapName
        "e0000",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0000",                  # 0
    ))

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_A4",           # 01, 1
        "Function_2_A5",           # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    Event(0, 2)
    Return()

    # Function_0_A0 end

    def Function_1_A4(): pass

    label("Function_1_A4")

    Return()

    # Function_1_A4 end

    def Function_2_A5(): pass

    label("Function_2_A5")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "イベント閲覧\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Return()

    # Function_2_A5 end

    SaveToFile()

Try(main)
