# Decision Report

- generated_at: 2026-07-06T05:14:51.156831+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8370**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.53% / filled 20/20。**
- 全期間 MARKET基準: n=8370, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| MARKET | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.49% | **+1.04%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.89% | **+0.45%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.81% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$318.73** / 初期 $100.00 (+218.73%)
- 確定: 2622件 (Win 832 / Loss 886 / Flat 904) / skip 2309件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $318.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1142件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T05:14:46.021016+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=63187.3
- Funnel: target 836 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRB/USDT:USDT | +13.15% | $8,772,073.36 |
| ZEROC0MPUTE/USDT:USDT | +12.04% | $1,587,584.02 |
| BILL/USDT:USDT | +10.53% | $1,205,081.63 |
| EPIC/USDT:USDT | +10.20% | $4,189,359.15 |
| LIT/USDT:USDT | +8.92% | $14,036,886.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEROC0MPUTE/USDT:USDT | below_1h_threshold | +2.06% | +2.15% |
| EPIC/USDT:USDT | below_1h_threshold | +1.35% | +1.43% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.17% | +1.26% |
| VELVET/USDT:USDT | below_1h_threshold | +1.07% | +1.16% |
| NES/USDT:USDT | below_1h_threshold | +1.05% | +1.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
