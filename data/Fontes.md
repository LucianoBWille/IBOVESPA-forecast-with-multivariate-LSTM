## Brasil
### IBOVESPA
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [Ibovespa (IBOV)](https://br.investing.com/indices/bovespa-historical-data)
* [Ibovespa Futuros](https://br.investing.com/indices/ibovespa-futures-historical-data)

### PIB
Dados em arquivo CSV baixado do site do IBGE, que se encontra [neste link](https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9300-contas-nacionais-trimestrais.html?=&t=series-historicas).

### IPCA
Dados em arquivo CSV baixado do site do IBGE, que se encontra [neste link](https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9258-indice-nacional-de-precos-ao-consumidor.html?=&t=series-historicas).

### INPC
Dados em arquivo CSV baixado do site do IBGE, que se encontra [neste link](https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9258-indice-nacional-de-precos-ao-consumidor.html?=&t=series-historicas).

### Taxa Selic
Dados em tabela no site do Banco Central do Brasil, que se encontra [neste link](https://www.bcb.gov.br/controleinflacao/historicotaxasjuros).

A tabela é transformada em uma string CSV executando o seguinte código no console.
``` javascript
rows = document.getElementsByTagName('tbody')[0].querySelectorAll('tr')
data = [["Date", "Meta Selic", "Acumulo periodo"]];
rows.forEach((row) => {
    cols = row.querySelectorAll("td");
    data.push([cols[1].innerText.replaceAll("/", "-"),cols[4].innerText.replaceAll(",", "."),cols[6].innerText.replaceAll(",", ".")]);
});
csv = data.map((row) => row.join("; ")).join("\n");
```
O valor de da variável `csv` é então copiado para o arquivo `SELIC.csv`.

### Câmbio dólar
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [USD/BRL - Dólar Americano Real Brasileiro](https://br.investing.com/currencies/usd-brl-historical-data)
* [BRL/USD - Real Brasileiro Dólar Americano](https://br.investing.com/currencies/brl-usd-historical-data)
* [Dólar Comercial USD BRL Futuro](https://br.investing.com/currencies/usd-brl-bmf-futures-historical-data)

## EUA
### Dow Jones
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [Dow Jones Industrial Average (DJI)](https://br.investing.com/indices/us-30-historical-data)
* [Dow Jones Futuros](https://br.investing.com/indices/us-30-futures-historical-data)

### S&P 500
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [S&P 500 (SPX)](https://br.investing.com/indices/us-spx-500-historical-data)
* [S&P 500 Futuros](https://br.investing.com/indices/us-spx-500-futures-historical-data)

### Nasdaq
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [NASDAQ Composite (IXIC)](https://br.investing.com/indices/nasdaq-composite-historical-data)
* [Nasdaq 100 (NDX)](https://br.investing.com/indices/nq-100-historical-data)
* [Nasdaq 100 Futuros](https://br.investing.com/indices/nq-100-futures-historical-data)

## Ásia-Pacífico:
### Shanghai Stock Exchange
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [Shanghai Composite (SSEC)](https://br.investing.com/indices/shanghai-composite-historical-data)
* [Shanghai SE 50 (SSE50)](https://br.investing.com/indices/shanghai-se-50-historical-data)
* [SSE 50 Futures](https://www.investing.com/indices/sse-50-futures-historical-data)

### Nikkei
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [Nikkei 225 (N225)](https://br.investing.com/indices/japan-ni225-historical-data)
* [Nikkei 225 Futures](https://www.investing.com/indices/japan-225-futures-historical-data)

### Hang Seng Index
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [Hang Seng (HSI)](https://br.investing.com/indices/hang-sen-40-historical-data)
* [Hang Seng Futures](https://www.investing.com/indices/hong-kong-40-futures)

### Kospi
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [KOSPI (KS11)](https://br.investing.com/indices/kospi-historical-data)
* [KOSPI 200 Futuros](https://br.investing.com/indices/korea-200-futures-historical-data)

### ASX 200
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [S&P/ASX 200 (AXJO)](https://br.investing.com/indices/aus-200-historical-data)
* [S&P/ASX 200 Futures](https://www.investing.com/indices/australia-200-futures-historical-data)

## Europa:
### FTSE 100
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [FTSE 100](https://br.investing.com/indices/uk-100-historical-data)
* [FTSE 100 Futures](https://www.investing.com/indices/uk-100-futures-historical-data)

### DAX
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [DAX (GDAXI)](https://br.investing.com/indices/germany-30-historical-data)
* [DAX Futures](https://www.investing.com/indices/germany-30-futures-historical-data)

### CAC 40
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [CAC 40 (FCHI)](https://br.investing.com/indices/france-40-historical-data)
* [CAC 40 Futures](https://www.investing.com/indices/france-40-futures-historical-data)

### FTSE MIB
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [FTSE MIB (FTMIB)](https://br.investing.com/indices/it-mib-40-historical-data)
* [FTSE MIB Futuros](https://br.investing.com/indices/italy-40-futures-historical-data)

### STOXX 600
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [STOXX 600 (STOXX)](https://br.investing.com/indices/stoxx-600-historical-data)
* [EURO STOXX 600 Futures](https://www.investing.com/indices/euro-stoxx-600-historical-data)

## Commodities:
### Petróleo WTI
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [WTI/USD - Preço spot do petróleo WTI Dólar Americano](https://br.investing.com/currencies/wti-usd-historical-data)
* [Petróleo WTI Futuros](https://br.investing.com/commodities/crude-oil-historical-data)

### Petróleo Brent
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [XBR/USD - Brent Spot Dólar Americano](https://br.investing.com/currencies/xbr-usd-historical-data)
* [Petróleo Brent Futuros](https://br.investing.com/commodities/brent-oil-historical-data)

### Minério de Ferro
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [Minério de ferro refinado 62% Fe CFR Futuros - (TIOc1)](https://br.investing.com/commodities/iron-ore-62-cfr-futures-historical-data)
* [Iron Ore 62% CFR - (TIOc2)](https://br.investing.com/commodities/iron-ore-62-cfr-futures-historical-data?cid=1178176)
* [Iron Ore 62% CFR - (TIOc3)](https://br.investing.com/commodities/iron-ore-62-cfr-futures-historical-data?cid=1178177)
* [Minério de ferro 62% Futuros - Mai 25 (DCIOK5)](https://br.investing.com/commodities/iron-ore-62-cfr-futures-historical-data?cid=961741)

## Criptoativos
### Bitcoin
Dados em arquivo CSV baixado do Investing.com, nos seguintes links:
* [Bitcoin](https://br.investing.com/crypto/bitcoin/historical-data)
* [Bitcoin BRL (BTC/BRL)](https://br.investing.com/indices/investing.com-btc-brl-historical-data)
* [Bitcoin CME Futuro (BTCc1)](https://br.investing.com/crypto/bitcoin/bitcoin-futures-historical-data?cid=1178665)
* [Bitcoin CME Futuro (BTCc2)](https://br.investing.com/crypto/bitcoin/bitcoin-futures-historical-data)