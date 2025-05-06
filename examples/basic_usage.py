from browser_use import BrowserUse

def main():
    # 初始化浏览器
    browser = BrowserUse()
    
    # 打开网页
    browser.open("https://www.example.com")
    
    # 获取页面标题
    title = browser.get_title()
    print(f"Page title: {title}")
    
    # 截图
    browser.screenshot("example.png")
    
    # 关闭浏览器
    browser.close()

if __name__ == "__main__":
    main()