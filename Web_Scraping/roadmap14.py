from playwright.async_api import async_playwright
import asyncio

async def test():
    async with async_playwright() as pw:
        browser1 = await pw.chromium.launch(headless=False)
        context = await browser1.new_context()
        tab1 = await context.new_page()
        await tab1.goto("https://practicetestautomation.com/practice-test-login/")

        await tab1.fill("input#username","student")
        await tab1.fill("input#password","Password123")
        print("Teste")
        await tab1.get_by_role("button",name="Submit").click()
        await tab1.wait_for_timeout(1000)
        print("Sucesso")
        print("A sair")
        await tab1.get_by_role("link", name="Log out").click()
        '''
        tab2 = await context.new_page()
        await tab2.goto("https://google.com")
        await tab1.close()
        await tab2.get_by_role("button",name="Aceitar tudo").click()
        await tab2.wait_for_timeout(2000)

        pesquisa = tab2.locator("textarea[name=q]")
        await pesquisa.fill("Playwright")
        await tab2.wait_for_timeout(1000)
        await pesquisa.press("Enter")

        list_link = []
        try:
            link = "a:has(h3)"
            await tab2.wait_for_selector(link, timeout=70000)
            primeiro = tab2.locator(link).first
            link_1 = await primeiro.get_attribute("href")

            list_link.append(link_1)
            print(", ".join(list_link))
        except Exception as e:
            print(e)
            print(f"\nTempo esgotado ou erro: Não conseguiste resolver o CAPTCHA a tempo (ou o Google bloqueou totalmente).")
        '''
        tab3 = await context.new_page()
        await tab3.goto("https://the-internet.herokuapp.com/dropdown")
        #await tab2.close()
        option = await tab3.locator("#dropdown").select_option("2")
        print(", ".join(option))
        await tab3.wait_for_timeout(5000)
        
        tab4 = await context.new_page()
        await tab4.goto("https://automationintesting.online/")
        await tab3.close()

        await tab4.fill("input[data-testid=ContactName]", "Moisés")
        await tab4.wait_for_timeout(1000)
        await tab4.fill("input[data-testid=ContactEmail]", "moises@gmail.com")
        await tab4.wait_for_timeout(1000)
        await tab4.fill("input[data-testid=ContactPhone]", "912964417")
        await tab4.wait_for_timeout(1000)
        await tab4.fill("input[data-testid=ContactSubject]", "Teste")
        await tab4.wait_for_timeout(1000)
        await tab4.fill("textarea[data-testid=ContactDescription]", "Isto é um teste")
        await tab4.wait_for_timeout(3000)
        async with tab4.expect_request(lambda request: request.method == "POST") as info_pedido:
            await tab4.get_by_role("button",name="Submit").click()
        pedido_capturado = await info_pedido.value

        print(f"Para onde foram enviados: {pedido_capturado.url}")
        print(f"O que foi dentro do 'pacote':\n{pedido_capturado.post_data}")

        tab5 = await context.new_page()
        await tab5.goto("https://www.ebay.com/")
        await tab4.close()
        pesquisa_ebay = tab5.locator("input[name='_nkw']")
        await pesquisa_ebay.fill("RAM DDR5 32 GB")
        barra_lateral = await tab5.locator("#gh-cat").select_option("58058")
        print(", ".join(barra_lateral))
        await pesquisa_ebay.press("Enter")
        await tab5.check("[aria-label='32 GB']")

        await tab5.wait_for_timeout(5000)

        tab6 = await context.new_page()
        await tab6.goto("https://www.selenium.dev/selenium/web/web-form.html")
        await tab5.close()

        checkboxes = await tab6.locator("input[type='checkbox']").all()
        for checkbox in checkboxes:
            if not await checkbox.is_checked():
                print("Checkbox desmarcada encontrada! A marcar")
                await checkbox.check()
            else:
                print("Esta checkbox já estava marcada.")
            await tab6.wait_for_timeout(5000)
        await tab6.get_by_role("button", name="Submit").click()
        
        await tab6.wait_for_timeout(5000)
asyncio.run(test())
