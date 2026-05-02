# Decision Report

- generated_at: 2026-05-02T09:57:02.420747+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2890**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2890, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.92% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.15% | **+2.15%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.26% | **+2.12%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.91% | **+2.04%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.93% | **+1.47%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T09:57:00.047974+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=78272.0
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.5 >= 65=1, 4h RSI 78.4 >= 65=1, 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +190.56% | $102,292,895.54 |
| TAC/USDT:USDT | +25.63% | $1,241,014.09 |
| BIO/USDT:USDT | +22.69% | $1,764,556.66 |
| KNC/USDT:USDT | +20.43% | $1,746,369.93 |
| IRYS/USDT:USDT | +18.75% | $1,428,157.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.22% | +4.22% |
| NAORIS/USDT:USDT | below_1h_threshold | +4.22% | +4.22% |
| MOVR/USDT:USDT | below_1h_threshold | +3.81% | +3.81% |
| BIO/USDT:USDT | below_1h_threshold | +3.60% | +3.61% |
| INJ/USDT:USDT | below_1h_threshold | +2.39% | +2.39% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
