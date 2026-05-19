# Decision Report

- generated_at: 2026-05-19T17:38:51.538350+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4484**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4484, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.93% | **+0.46%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.31% | **+3.24%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 572件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T17:38:48.977355+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=76899.9
- Funnel: target 760 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +17.16% | $6,421,424.40 |
| BSB/USDT:USDT | +16.48% | $9,594,658.81 |
| LAB/USDT:USDT | +8.45% | $86,050,535.00 |
| VVV/USDT:USDT | +6.73% | $6,441,887.73 |
| LIT/USDT:USDT | +6.71% | $1,897,985.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENJ/USDT:USDT | below_1h_threshold | +3.55% | +3.49% |
| SIREN/USDT:USDT | below_1h_threshold | +2.46% | +2.41% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.39% | +2.33% |
| VVV/USDT:USDT | below_1h_threshold | +2.12% | +2.07% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.82% | +1.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
