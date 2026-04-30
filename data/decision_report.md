# Decision Report

- generated_at: 2026-04-30T21:46:04.525864+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2736**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2736, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.68% | **+1.07%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.09% | **+2.47%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.23% | **+2.12%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.86% | **+1.74%** |
| ASK_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T21:45:57.861728+00:00 / 保存件数 110/288
- BTC: STAGNANT 1h -0.14% price=76343.6
- Funnel: target 756 → liquid 223 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +20.67% | $12,973,908.18 |
| AIOT/USDT:USDT | +15.34% | $17,129,605.84 |
| ORCA/USDT:USDT | +13.89% | $3,091,150.16 |
| GENIUS/USDT:USDT | +13.21% | $1,109,045.02 |
| DRIFT/USDT:USDT | +11.14% | $1,272,036.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_1h_threshold | +4.91% | +5.05% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +4.55% | +4.69% |
| ZBCN/USDT:USDT | below_1h_threshold | +3.06% | +3.21% |
| ENSO/USDT:USDT | below_1h_threshold | +1.71% | +1.85% |
| APE/USDT:USDT | below_1h_threshold | +1.45% | +1.59% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
