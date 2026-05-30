# Decision Report

- generated_at: 2026-05-30T08:39:38.069238+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5112**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5112, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.17% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.59% | **+1.35%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.49% | **+1.11%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 767件 (Win 179 / Loss 230 / Flat 358) / skip 906件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-30T08:39:35.319487+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=73506.2
- Funnel: target 773 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1, 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +70.52% | $15,539,152.43 |
| VTHO/USDT:USDT | +33.15% | $1,157,036.69 |
| LAB/USDT:USDT | +21.79% | $124,440,643.08 |
| XLM/USDT:USDT | +16.39% | $448,327,843.03 |
| ID/USDT:USDT | +15.24% | $6,772,178.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ID/USDT:USDT | below_1h_threshold | +4.29% | +4.30% |
| SNOWSTOCK/USDT:USDT | below_1h_threshold | +3.28% | +3.30% |
| BILL/USDT:USDT | below_1h_threshold | +3.09% | +3.11% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.04% | +2.05% |
| GRASS/USDT:USDT | below_1h_threshold | +1.52% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
