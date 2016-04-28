# -*- coding: utf-8 -*-
class ElementCruiseShip:
    ID_HOME_SEARCH = "mangocity.activity:id/header_home" #邮轮首页搜索
    ID_SHIP_LINE = "mangocity.activity:id/mailsteamer_lane_tv"#邮轮航线
    ID_PORT = "mangocity.activity:id/mailsteamer_port_tv"#出发港口  mangocity.activity:id/mailsteamer_port_ly
    ID_SHIP_SEARCH = "mangocity.activity:id/mailsteamer_search_btn" #邮轮搜索
    XPATH_FIRST_LINE = "//android.widget.ListView/android.widget.RelativeLayout[contains(@index,0)]" ##邮轮航线选择第一个
    XPATH_FIRST_PORT = "//android.widget.ListView/android.widget.RelativeLayout[contains(@index,0)]" #出发港口选择第一个  不限
    XPATH_FIRST_PORTS = "//android.widget.ListView/android.widget.RelativeLayout[contains(@text,'梵蒂冈')]"  # 出发港口选择第一个  不限
    ID_LIST_LINE = "mangocity.activity:id/frm_cruiseship_listview"
    ID_CRUISE_BK = "mangocity.activity:id/wiki" #邮轮百科
    ID_PIC_OF_CRUISE_BK = "mangocity.activity:id/whatplay_introduce_img" #邮轮百科页面大图
    ID_BARGAIN="mangocity.activity:id/product_title"#特价限时抢购标题
    ID_MORE_DATE = "mangocity.activity:id/more_date"  # 更多航期
    XPATH_LAST_DATE = "//android.widget.ListView/android.widget.RelativeLayout[last()]"  # 选最后一个航期
    XPATH_FIRST_RESERVE = "//android.widget.ListView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Button[contains(@index,2)]"

    #'''填写订单'''
    ID_ORDER_USERNAME = "mangocity.activity:id/et_link_man"  # 用户名
    ID_ORDER_SUBMIT = "mangocity.activity:id/btn_submit_order"  # 提交订单
    ID_ORDER_SUCESS = "mangocity.activity:id/frm_cruiseship_comp_iv_success"# 订单提交成功提示语

    ## 订单详情
    # XPATH_CHECK_ORDER="//android.widget.TextView[contains(@text,'查看订单详情')]"

    #邮轮首页
    ID_TOPAD = "mangocity.activity:id/frm_topAd_viewpage"#珍格格广告ID
    ID_BAOCHUAN = "mangocity.activity:id/baochuang" #芒果包船
    ID_CRUISE_TITLE = "mangocity.activity:id/header_title"#邮轮详情标题
    ID_PIC_OF_BAOCHUAN = "mangocity.activity:id/charteredboadt_img"#邮轮包船页面大图
    XPATH_RH = "//android.widget.TextView[contains(@index,0)]"#日韩标题
    XPATH_DNY = "//android.widget.TextView[contains(@index,2)]"#东南亚
    XPATH_DZH = "//android.widget.TextView[contains(@index,4)]"#地中海
    XPATH_ALSJ = "//android.widget.TextView[contains(@index,6)]"#阿拉斯加
    ID_AREALIST = "mangocity.activity:id/area_list"#地域列表
    ID_AREA_FIRST = "mangocity.activity:id/title" #第一个地域

    #产品列表筛选项
    ID_BACK_HOME = "mangocity.activity:id/header_home" #返回主页
    ID_SCREEN_LIST = "mangocity.activity:id/frm_public_bottom_screen"#筛选因子列表
    ID_RECOMMEND = "mangocity.activity:id/frm_public_bottom_screen_one_ll" #芒果推荐
    ID_PRICE_SORT = "mangocity.activity:id/frm_public_bottom_screen_two_ll"#价格排序
    ID_TRAVEL_DAY = "mangocity.activity:id/frm_public_bottom_screen_three_ll"#游玩天数
    ID_SCREENING= "mangocity.activity:id/frm_public_bottom_screen_four_ll" #筛选
    XPATH_PRICE_FIRST = "//android.widget.LinearLayout[contains(@index,1)]/android.widget.RelativeLayout/" \
                        "android.widget.RelativeLayout[contains(@index,1)]/android.widget.TextView[last()]" #第一个价格
    XPATH_PRICE_SECOND = "//android.widget.LinearLayout[contains(@index,2)]/android.widget.RelativeLayout/" \
                         "android.widget.RelativeLayout[2]/android.widget.TextView[last()]"#第二个价格
    XPATH_CHOSE_LASTDAY = "//android.widget.ListView/android.widget.RelativeLayout[last()]"#选最后一个游玩天数  即15天以上
    ID_CHOOSEN_FACTOR = "mangocity.activity:id/frm_public_bottom_screen_three_tv" #游玩天数显示
    ID_RED_POINT = "mangocity.activity:id/frm_public_bottom_screen_three_img_ring"#小红点
    ID_NO_DATA = "mangocity.activity:id/tv_no_data_nodata"  #暂无内容提示
    XPATH_SCREEN_BRAND = "//android.widget.ListView[contains(@index,1)]/android.widget.RelativeLayout[2]"#选择第一个品牌  皇家加勒比邮轮
    XPATH_SELECT_IMG = "//android.widget.ListView[contains(@index,1)]/android.widget.RelativeLayout[2]/android.widget.ImageView" #筛选邮轮品牌标志 √
    XPATH_CLEAR_IMG = "//android.widget.ListView[contains(@index,1)]/android.widget.RelativeLayout[1]/android.widget.ImageView"
    ID_CLEAR = "mangocity.activity:id/mailsteamer_product_reset_bt" #清除选项按钮
    ID_SURE = "mangocity.activity:id/mailsteamer_product_sure_bt" #确认按钮
    XPATH_BRAND_FIRST = "//android.widget.LinearLayout[contains(@index,1)]/android.widget.RelativeLayout/" \
                        "android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"#航线列表 搜索出来的邮轮品牌























