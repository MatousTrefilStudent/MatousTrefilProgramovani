# Vibecoding
Vytvořil: Matouš Trefil

Vibecoding je způsob vývoje softwaru, při kterém je část kódu generována umělou inteligencí.  
Hlavním cílem je efektivnější tvorba programového kódu prostřednictvím spolupráce mezi vývojářem a nástroji umělé inteligence.


## Způsob práce

1. **Nastavení vývojového prostředí**  
   Vývojář připraví pracovní prostředí, které zahrnuje nástroje s podporou umělé inteligence, jako jsou kódoví asistenti, generátory funkcí nebo automatické nástroje pro tvorbu dokumentace.

2. **Definování požadavků a kontextu**  
   Vývojář specifikuje cíle, požadavky a kontext úkolu, aby AI mohla generovat relevantní a smysluplné návrhy.

3. **Generování návrhů AI**  
   Na základě zadaných parametrů umělá inteligence vytváří první verze kódu nebo doprovodných materiálů.

4. **Revize a úpravy ze strany vývojáře**  
   Vývojář kontroluje, hodnotí a upravuje generované návrhy, zajišťuje jejich správnost, kvalitu a integraci do stávajícího kódu.

5. **Iterativní opakování procesu**  
   Vývojář a AI opakovaně spolupracují v cyklech generování, revize a ladění, dokud není dosaženo požadované kvality výsledného řešení.


## Příklady nástrojů
### <img src="pics/github_copilot_logo.png" alt="GitHub Copilot logo" align="right" width="100">

### 1. GitHub Copilot

AI asistent integrovaný do editorů jako Visual Studio Code, který nabízí návrhy kódu v reálném čase.
- **Cena**: $0–$39/měsíc – nabízí bezplatný plán a několik placených variant s různými funkcemi.
- **Výhody**:
  - Silná integrace s GitHubem a široká podpora IDE.
  - Pokročilé modely AI, včetně Google Gemini 2.5 Pro pro prémiové uživatele.
- **Nevýhody**:
  - Bezplatný plán má omezený přístup k modelům a nízký počet požadavků.
  - Některé funkce jsou povinné a nelze je deaktivovat, což může být pro některé uživatele rušivé.

### <img src="pics/tabnine_logo.png" alt="Tabnine logo" align="right" width="100">

### 2. Tabnine

AI doplněk pro více editorů, který generuje kódové fragmenty a pomáhá s automatickým dokončováním.
- **Cena**: $0–$39/uživatel/měsíc – nabízí bezplatný plán a několik placených variant s různými funkcemi.
- **Výhody**:
  - Vysoká úroveň ochrany soukromí a bezpečnosti dat.
  - Podpora pro různé IDE a jazyky.
- **Nevýhody**:
  - Bezplatný plán je velmi omezený a vhodný pouze pro základní použití.
  - Vyšší cena pro pokročilé plány ve srovnání s některými konkurenty.


### <img src="pics/amazon_codewhisperer_logo.png" alt="Amazon CodeWhisperer logo" align="right" width="100">

### 3. Amazon CodeWhisperer

AI nástroj pro automatizované generování kódu zaměřený na cloudové služby a aplikace.
- **Cena**: $0–$19/uživatel/měsíc – nabízí bezplatný plán a placený plán pro profesionální použití.
- **Výhody**:
  - Silná integrace s AWS a cloudovými službami.
  - Podpora pro více jazyků a rámců.
- **Nevýhody**:
  - Méně široká podpora IDE ve srovnání s některými konkurenty.
  - Některé funkce mohou vyžadovat pokročilé nastavení a konfiguraci.

### <img src="pics/cursor_AI_logo.jpg" alt="Cursor AI logo" align="right" width="100">

### 4. Cursor AI

Pokročilý AI kódový editor založený na Visual Studio Code, integrovaný s modely jako GPT-4, Claude a Gemini, který nabízí generování, refaktoring a ladění kódu.
- **Cena**: Zdarma s omezením, placené plány od $20/měsíc s neomezeným využitím a pokročilými funkcemi.
- **Výhody**:
  - Podpora více jazyků a pokročilé AI funkce včetně ladění a vysvětlování kódu.
  - Integrace s GitHubem a dalšími nástroji pro efektivní workflow.
- **Nevýhody**:
  - Některé problémy s kvalitou výstupu




## Nejdůležitější principy

- **Kontrola kvality nad generovaným kódem**  
  Kód vytvořený umělou inteligencí musí být systematicky ověřován z hlediska funkčnosti, výkonu, bezpečnosti a souladu s interními standardy projektu.
  Součástí tohoto procesu může být automatizované testování, statická analýza nebo manuální revize kódu vývojářem.
  Cílem je zajistit, aby výsledný kód odpovídal požadovaným technickým parametrům a neobsahoval chyby vzniklé v důsledku chybné interpretace zadání AI modelem.

- **Odpovědnost za výsledek**  
  Použití umělé inteligence při programování nemění odpovědnost za výsledný produkt.
  Vývojář nebo tým zůstává garantem správnosti, bezpečnosti a právní bezvadnosti kódu.
  To zahrnuje i dohled nad tím, jak jsou AI nástroje používány, jaké zdroje dat využívají a jaký dopad může mít jejich výstup na finální aplikaci.

- **Vhodné využití AI**  
  Umělá inteligence by měla být nasazována především v oblastech, kde přináší měřitelné zefektivnění práce – například při generování opakujících se struktur nebo návrhu dokumentace.
  Rozhodovací a návrhové procesy by však měly zůstat primárně v kompetenci člověka.


## Cíl a přínosy

Cílem vibecodingu je:
- zrychlení procesu vývoje,
- snížení množství rutinní práce programátora,
- zvýšení důrazu na koncepční a tvůrčí aspekty programování.

Díky využití AI lze zjednodušit implementační část vývoje a věnovat více času návrhu architektury, testování a optimalizaci.


## Úskalí a nevýhody

Nevýhody vibecodingu jsou:
- závislost na kvalitě a přesnosti výstupů generovaných umělou inteligencí,
- riziko snížení porozumění kódu ze strany vývojáře při nadměrném spoléhání na AI,
- potřeba dodatečné validace a testování generovaného kódu.

Tyto faktory mohou ovlivnit kvalitu, udržovatelnost a spolehlivost výsledného softwaru.  
V praxi je proto vhodné vibecoding využívat jako doplňkový přístup, nikoli jako plnohodnotnou náhradu tradičního vývoje.


## Dopad vibecodingu na seniorní a juniory programátory

Vibecoding má odlišný dopad na seniorní a juniorní vývojáře vzhledem k jejich zkušenostem a schopnostem práce s AI generovaným kódem.

### Seniorní programátoři

- Seniorní vývojáři mohou vibecoding využít k automatizaci rutinních úkolů, což jim umožňuje soustředit se na komplexní architektonické a designové problémy.
- Mají zkušenosti, díky kterým mohou efektivně vyhodnocovat a upravovat kód generovaný AI, což zvyšuje kvalitu výsledného produktu.
- Vibecoding jim může zjednodušit spolupráci v týmu, protože mohou rychleji vytvářet prototypy a návrhy.

### Juniorní programátoři

- Pro juniory může vibecoding představovat silnou podporu při učení a psaní kódu, protože AI může nabídnout návrhy a vzory řešení.
- Vibecoding může zkrátit dobu potřebnou k dosažení produktivní úrovně, ale zároveň je důležité, aby si osvojili kritické myšlení a kontrolu kvality kódu.
- Existuje riziko, že bez dostatečného dohledu a zkušeností budou akceptovat nevhodné nebo nekvalitní návrhy AI. 

## Příklad

Tenhle markdown soubor byl vibecodovaný

## Názor

Podle mého názoru je vibecoding velmi užitečný přístup k programování, který dokáže výrazně zefektivnit práci vývojáře. Nejde jen o pomoc při psaní jednoduchých a často se opakujících částí kódu, ale i o podporu při řešení složitějších úloh, kde může umělá inteligence nabídnout nečekaná a inspirativní řešení.

U složitějších částí kódu je však nezbytné výsledky pečlivě otestovat a ověřit jejich logiku, aby vývojář skutečně porozuměl tomu, co AI vytvořila. Pouze tak lze zajistit, že generovaný kód bude nejen funkční, ale i udržitelný a bezpečný.

Osobně používám GitHub Copilot a Tabnine ve svých projektech. Copilot mi nejvíce pomáhá při tvorbě komplexnějších částí aplikace, například při návrhu struktur nebo implementaci algoritmů – často navrhne celé bloky kódu, které pak jen upravím pro svůj konkrétní kontext. Tabnine naopak využívám pro rychlé doplňování kratších úseků, kde nechci, aby AI příliš „přemýšlela“ a generovala složitá řešení.

Kombinace těchto nástrojů mi umožňuje pracovat rychleji, přitom si zachovávám plnou kontrolu nad výsledkem. Myslím si, že vibecoding není náhradou lidského myšlení, ale spíše rozšířením schopností vývojáře – podobně jako když zkušený programátor spolupracuje s pomocníkem, který dokáže okamžitě reagovat na jeho potřeby.