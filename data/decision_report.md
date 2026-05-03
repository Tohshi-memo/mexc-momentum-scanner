# Decision Report

- generated_at: 2026-05-03T17:17:15.935841+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3091**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3091, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/16 | 31.2% | +2.57% | **+0.80%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.81% | **+0.69%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.02% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.36% | **+1.65%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.92% | **+1.15%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.11% | **+1.05%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T17:17:11.168743+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78661.9
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +23.50% | $309,995,052.89 |
| SKYAI/USDT:USDT | +14.46% | $23,121,400.53 |
| BB/USDT:USDT | +5.78% | $1,297,781.48 |
| AIOT/USDT:USDT | +5.17% | $2,189,201.67 |
| TST/USDT:USDT | +5.04% | $5,147,611.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BB/USDT:USDT | below_1h_threshold | +2.62% | +2.57% |
| SIREN/USDT:USDT | below_1h_threshold | +2.31% | +2.26% |
| ORDI/USDT:USDT | below_1h_threshold | +1.86% | +1.81% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.76% | +1.71% |
| UB/USDT:USDT | below_1h_threshold | +1.32% | +1.26% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
