import Br_lan
import str2hex
import Rules
import Output
import PSR

print('**************************************************')
print("NOTE:please input with '-', like 12-34-56-78-90-12")
print('**************************************************')
print()

# 输入从管理界面获取到的RE后端的2.4GHz无线MAC地址，以及5GHz无线MAC地址
ra0 = input("Please input 2.4GHz MAC shown on management page of RE: \n")
rai0 = input("Please input 5GHz MAC shown on management page of RE: \n")

# 输出br-lan的值
def print_brlan(ra0):
    ra0 = ra0.split('-')
    br_lan = Br_lan.get_br_lan(ra0)
    br_lan_print = Output.output_res(br_lan)
    # print('**************************************************')
    # print('br-lan:', br_lan_print)
    return br_lan_print


# 计算2.4G转换后的MAC地址
def print_apcli0(ra0):
    ra0 = ra0.split('-')
    ra0 = str2hex.MAC_transfer(ra0)
    Rule_dic = {
        '4': Rules.rules_04(ra0),
        '5': Rules.rules_05(ra0),
        '6': Rules.rules_06(ra0),
        '7': Rules.rules_07(ra0),
        '8': Rules.rules_08(ra0)
    }
    Rule_num = input("Please input 2.4GHz MAC transfer rule number: \n")
    apcli0 = Rule_dic.get(Rule_num)
    #apcli0 = Rules.rules_04(ra0)
    apcli0_print = Output.output_res(apcli0)
    # print('**************************************************')
    # print('apcli0:',apcli0_print)
    return apcli0_print

# 计算5G转换后的MAC地址


def print_apclii0(rai0):
    rai0 = rai0.split('-')
    rai0 = str2hex.MAC_transfer(rai0)
    Rule_dic = {
        '4': Rules.rules_04(rai0),
        '5': Rules.rules_05(rai0),
        '6': Rules.rules_06(rai0),
        '7': Rules.rules_07(rai0),
        '8': Rules.rules_08(rai0)
    }
    Rule_num = input("Please input 5GHz MAC transfer rule number: \n")
    apclii0 = Rule_dic.get(Rule_num)
    #apclii0 = Rules.rules_05(rai0)
    # print(apclii0)
    # print(type(apclii0))
    apclii0_print = Output.output_res(apclii0)
    # print('**************************************************')
    # print('apclii0:',apclii0_print)
    return apclii0_print

#计算PSR2转换后的固定前缀
def print_psr2(ra0):
    ra0 = ra0.split('-')
    br_lan = Br_lan.get_br_lan(ra0)
    psr2_prefix = PSR.psr_02(br_lan)
    psr2_print = Output.output_res(psr2_prefix)
    # print('**************************************************')
    # print('psr2_prefix:',psr2_print)
    return psr2_print

brlan = print_brlan(ra0)
apcli0 = print_apcli0(ra0)
apclii0 = print_apclii0(rai0)
psr2 = print_psr2(ra0)

print('\n***********************BR-LAN*********************\n',
      brlan,
      '\n***********************APCLI0*********************\n',
      apcli0,
      '\n***********************APCLII0********************\n',
      apclii0,
      '\n***********************PSR2***********************\n',
      psr2)