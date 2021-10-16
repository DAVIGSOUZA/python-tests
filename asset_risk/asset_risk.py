# DESAFIO:
# Calcular o risco de investimento em um ativo da primeira empresa com capital aberto do ranking do MSSP Alert 2021 com
# base nos últimos 5 anos.

# QUAL É A PRIMEIRA EMPRESA COM CAPITAL ABERTO DO RANKING?
# 1º - AT&T cybersecurity - Código na bolsa de Nova York (NYSE): T
# 8º - ACCENTURE - NYSE : ACN

# Apesar da AT&T ser a primeira, no ranking consta como AT&T cybersecurity, definindo um braço especifico da empresa. Já
# a ACCENTURE, apesar de existir outras linhas de negócios, não é listado o braço especifico de cybersecurity da empresa
# no ranking do MSSP alert.

# Ainda é possível que alguma empresa entre a 2ª e 7ª posição tenha capital aberto e essa informação não tenha sido
# detectada pela minha analise.

# Vale salientar que a 4ª posição (Neustar) abriu capital em 2005 na NYSE(cód: NSR) porém em 2017 foi concretizada a
# aquisição da empresa pela Golden Gate Capital fazendo a Neustar uma companhia de capital privado novamente.

import datetime as dt
import numpy as np
import pandas as pd
import pandas_datareader as pdr


def capm_us_market(ticker):
    today = dt.date.today()
    timedelta = dt.timedelta(days=1825)
    five_years_ago = today - timedelta

    # get market data
    ticker_data = pdr.get_data_yahoo(ticker, five_years_ago, today).resample('Y').last()
    sp500_data = pdr.get_data_yahoo('^GSPC', five_years_ago, today).resample('Y').last()

    data = pd.DataFrame({'stock': ticker_data['Adj Close'], 'sp': sp500_data['Adj Close']})

    returns = np.log(data / data.shift(1))

    annual_cov = returns.cov()

    beta = annual_cov.iloc[0, 1]/annual_cov.iloc[1, 1]

    # risk free annual return
    risk_free = 0.025

    # SP500 last 5 years average annual return
    market_risk = returns['sp'].mean()

    capm = risk_free + beta *(market_risk - risk_free)

    # console returns
    print('----------------------------------------------------------------------')
    print('Retorno anual dos juros básicos da economia americana:', risk_free)
    print("Retorno anual médio dos últimos 5 anos do SP500: ", market_risk)
    print("Retorno anual médio dos últimos 5 anos de", ticker, ": ", returns['stock'].mean())
    print(ticker, "Beta: ", beta)
    print(ticker, "CAPM: ", capm)


print("β < 1 = Ativo defensivo, ação oscila menos que o SP500")
print("β > 1 = Ativo agressivo, ação oscila mais que o SP500")
print("β < 0 = Ativo descorelacionado, ação oscila no sentido oposto ao SP500")
print('----------------------------------------------------------------------')
print('CAPM retorna a taxa de atratividade, usada para descontar os fluxos de caixa previstos de um investimento')
print('uma ação mais volátil(β maior) retornará um CAPM maior pois é esperado um prêmio maior para ativos mais arriscados')

# # AT&T
capm_us_market('T')
# # ACCENTURE
capm_us_market('ACN')

# # GOOGLE
# capm_us_market('GOOG')
# # AMAZON
# capm_us_market('AMZN')
# # MICROSOFT
# capm_us_market('MSFT')
# # APPLE
# capm_us_market('AAPL')
# # AMD
# capm_us_market('AMD')
# # NVIDIA
# capm_us_market('NVDA')
# # TESLA
# capm_us_market('TSLA')