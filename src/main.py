# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
import zkSync2_auto.zkSync2_run_test
import wallet
import zkSync2_auto.muteSwitch_run_test
if __name__ == '__main__':
    # print_hi('PyCharm')
    # walletList=wallet.getWallet()

    # zkSync2_auto.zkSync2_run_test.runTest("")
    zkSync2_auto.muteSwitch_run_test.runMuteSwitchTestnet("0x99467f01970c77534d0ea312aee7209728e123b7")
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
