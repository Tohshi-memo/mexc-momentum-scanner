# Decision Report

- generated_at: 2026-05-03T19:18:20.744869+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3104**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3104, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.79% | **-2.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.37% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 6/20 | 30.0% | +0.34% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +5.90% | **+3.83%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +4.05% | **+3.24%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +5.56% | **+2.78%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.51% | **+2.26%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +6.00% | **+1.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T19:18:18.903766+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78666.4
- Funnel: target 755 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +51.64% | $300,442,246.18 |
| SKYAI/USDT:USDT | +22.11% | $25,326,195.31 |
| MERL/USDT:USDT | +12.01% | $1,054,163.95 |
| H/USDT:USDT | +9.76% | $7,844,795.39 |
| BB/USDT:USDT | +7.23% | $1,570,154.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.62% | +3.67% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.52% | +3.57% |
| GENIUS/USDT:USDT | below_1h_threshold | +3.23% | +3.28% |
| H/USDT:USDT | below_1h_threshold | +3.02% | +3.07% |
| MERL/USDT:USDT | below_1h_threshold | +2.31% | +2.36% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
