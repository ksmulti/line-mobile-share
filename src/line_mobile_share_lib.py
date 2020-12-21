import json
from selenium.webdriver.common.by import By
from common_lib import CommonCore
import random
import time
import os

class LineMobilesShareCore(CommonCore):
    def __init__(self):
        self._name = __name__
        CommonCore.__init__(self)

    def Index(self):
        self._browser.get('https://mypage-mobile.line.me/mypage/login/')
        self.WaitPageSteady('loginAccount', By.NAME)
        print("Loading index OK!")

    def Login(self):
        edit_user = self.WaitPageSteady('loginAccount', By.NAME)
        edit_password = self.WaitPageSteady("loginPassword", By.NAME)
        edit_user.send_keys(self._settings["account"])
        edit_password.send_keys(self._settings["password"])

        btn_login = self.WaitPageSteady('FnNextBtn')
        btn_login.click()

        self.WaitPageSteady("FnDisplayBtn")
        print("Login OK!")

    def GetShareLink(self):
        btn_get_share_code = self.WaitPageSteady("招待URL発行")
        btn_get_share_code.click()


        input_price = self.WaitPageSteady("chargeInstructAmt")
        input_price.send_keys('1')
        edit_password = self.WaitPageSteady('chargeBetPassword')
        edit_password.send_keys(self._settings["boat_race_pin_vote"])
        btn_confirm = self.WaitPageSteady('executeCharge')
        btn_confirm.click()

        btn_confirm = self.WaitPageSteady("ok", By.ID)
        btn_confirm.click()

        self.WaitPageSteady("payment", By.ID)
        print("ChargeMoney OK!")

