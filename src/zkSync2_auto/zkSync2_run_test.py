import selenium_metamask_automation as auto
import time
import wallet
import random
from config import global_config
import os


def runTest(address):
    # 指定chromedriver路径
    driver_path = os.path.abspath(r"..")+global_config.get('path', 'driver_path').strip()
    driver = auto.launchSeleniumWebdriver(driver_path)

    time.sleep(8)
    # 打开zkSync2.0测试网
    wait_time = global_config.get('config', 'time')
    driver.implicitly_wait(wait_time)
    driver.get('https://portal.zksync.io/')

    print('start into  https://portal.zksync.io.. ')
    seed_phrase="sword pig blossom wire peasant pave gesture upon excuse trash usage cousin shallow cloth learn about noble future surprise deliver belt memory desk pigeon"
    password = 'BCQ123456'
    address='0xd7620b6e03ebfb5e14a91bc020b0ae1517d0a227'

    # 导入助记词
    time.sleep(8)
    auto.metamaskSetup(seed_phrase, password,1)
    network_name = 'Goerli 测试网络'
    # 切换到测试网络
    auto.changeMetamaskNetwork(network_name)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_xpath('//span[text()="MetaMask"]').click()
    # 连接钱包
    auto.connectToWebsite()

    # Faucet
    #首页切到[faucet(index=4)]菜单
    print('start Faucet')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/nav/div[1]/a[4]').click()
    # driver.find_element_by_xpath("//button[text()='Go to Faucet']").click()
    time.sleep(5)
    print('start Request Funds from Faucet')
    # 此处获取测试币可能受zkSync影响造成 失败/无法实时到账
    driver.find_element_by_xpath("//button[text()='Request Funds from Faucet']").click()
    time.sleep(3)
    print('start button ok')
    driver.find_element_by_xpath("//button[text()=' OK ']").click()
    print('Faucet Success')

    # Deposit
    #首页切到[Bridge(index=2)]菜单
    #找到Deposit按钮
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/nav/div[1]/a[2]').click()
    driver.find_element_by_xpath("//a[text()='Deposit']").click()
    time.sleep(5)
    inputs = driver.find_elements_by_xpath('//input')
    inputs[0].send_keys('0.01')
    time.sleep(1)
    driver.find_element_by_xpath("//button[text()='Deposit']").click()
    # 确认交易
    print('start confirmApprovalFromMetamask')
    auto.confirmApprovalFromMetamask()
    print('Deposit Success')

    # Withdraw
    print('start Withdraw...')
    driver.find_element_by_xpath("//a[text()='Withdraw']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//p[text()='ETH']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//p[text()='USDC']").click()
    time.sleep(5)
    inputs = driver.find_elements_by_xpath('//input')
    value = random.randint(1, 20)
    inputs[0].send_keys(value)
    driver.find_element_by_xpath("//p[text()='ETH']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//p[text()='LINK']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[text()='Withdraw']").click()
    print('start addAndChangeNetwork')
    auto.addAndChangeNetwork()
    print('start signConfirm')
    auto.signConfirm()
    print('Withdraw Success')

    # Transfer
    driver.find_element_by_xpath("//a[text()=' Wallet']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[text()='Transfer']").click()
    print('start Transfer')
    time.sleep(3)
    inputs = driver.find_elements_by_xpath('//input')
    transfer_addr = global_config.get('config', 'transfer_address').strip()
    inputs[0].send_keys(transfer_addr)
    driver.find_element_by_xpath("//p[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//p[text()='USDC']").click()
    time.sleep(1)
    inputs[1].send_keys('5')
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='Transfer']").click()
    print('start signConfirm')
    auto.signConfirm()
    print('Transfer Success')

    # 退出
    screenshot_path = global_config.get('path', 'result_path').strip()
    driver.get_screenshot_as_file(str(screenshot_path) + address + '.png')
    driver.quit()
