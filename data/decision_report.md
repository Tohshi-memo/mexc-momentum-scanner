# Decision Report

- generated_at: 2026-05-03T16:47:15.855217+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3088**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3088, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.68% | **+1.09%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.05% | **+0.79%** |
| LIMIT_BB3S | 6/15 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.64% | **+1.19%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.67% | **+0.92%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.01% | **+0.91%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.97% | **+0.63%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T16:47:09.869519+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78685.7
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +19.57% | $331,434,499.99 |
| SKYAI/USDT:USDT | +10.26% | $24,492,226.46 |
| AIOT/USDT:USDT | +4.41% | $2,312,928.06 |
| TST/USDT:USDT | +2.91% | $5,067,269.52 |
| TAG/USDT:USDT | +2.81% | $10,316,353.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.34% | +4.27% |
| TAG/USDT:USDT | below_1h_threshold | +2.81% | +2.73% |
| TST/USDT:USDT | below_1h_threshold | +2.49% | +2.41% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.37% | +2.29% |
| TAC/USDT:USDT | below_1h_threshold | +1.96% | +1.88% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
