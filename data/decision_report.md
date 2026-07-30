# Decision Report

- generated_at: 2026-07-30T01:11:33.152734+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9847**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.78% / filled 20/20。**
- 全期間 MARKET基準: n=9847, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.78% | **+3.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.78% | **+3.78%** |
| LIMIT_1PCT | 14/20 | 70.0% | +2.35% | **+1.65%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.09% | **+1.25%** |
| LIMIT_ATR | 7/20 | 35.0% | +2.46% | **+0.86%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.98% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | -1.16% | **-0.76%** |
| MARKET_LONG | 20/20 | 100.0% | -1.11% | **-1.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.66** / 初期 $100.00 (+21.66%)
- 確定トレード: 167件 (TP 66 / SL 96 / EXP 5)
- 最新: KIOXIASTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.66
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2889件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2016件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 0件 / skip 558件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000481 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-30T01:11:17.135054+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63732.7
- Funnel: target 911 → liquid 180 → pre 50 → checked 50 → surge 4 → strict 4
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +14.23% | $14,225,270.57 |
| MSFU/USDT:USDT | +13.46% | $4,464,569.74 |
| RE/USDT:USDT | +13.17% | $7,908,146.84 |
| ADVANTESTSTOCK/USDT:USDT | +12.93% | $1,550,126.73 |
| KIOXIASTOCK/USDT:USDT | +10.43% | $1,020,487.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +3.52% | +3.43% |
| ACH/USDT:USDT | below_1h_threshold | +3.18% | +3.09% |
| EVAA/USDT:USDT | below_1h_threshold | +2.66% | +2.56% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.62% | +2.53% |
| QXOSTOCK/USDT:USDT | below_1h_threshold | +1.49% | +1.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
