# Decision Report

- generated_at: 2026-07-26T16:46:20.649036+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9579**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.60% / filled 20/20。**
- 全期間 MARKET基準: n=9579, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.22% | **+2.11%** |
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.45% | **+1.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.65% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.34% | **+0.18%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$454.84** / 初期 $100.00 (+354.84%)
- 確定: 3398件 (Win 1078 / Loss 1105 / Flat 1215) / skip 2742件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $454.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.72** / 初期 $100.00 (+37.72%)
- 確定: 1222件 (Win 338 / Loss 274 / Flat 610) / skip 1768件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0658 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.21** / 初期 $100.00 (+8.21%)
- 確定: 616件 (Win 207 / Loss 238 / Flat 171) / pending 0件 / skip 433件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000135 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.11% 残高後 $108.21

## 6. Latest Market Context

- 更新: 2026-07-26T16:46:11.113912+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64795.8
- Funnel: target 898 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +10.91% | $17,549,594.75 |
| CROSS/USDT:USDT | +4.15% | $1,085,472.78 |
| ETHFI/USDT:USDT | +2.19% | $2,127,535.23 |
| BANK/USDT:USDT | +2.02% | $75,582,649.79 |
| ANSEM/USDT:USDT | +1.86% | $1,082,464.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CROSS/USDT:USDT | below_1h_threshold | +4.16% | +4.06% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.25% | +2.15% |
| BANK/USDT:USDT | below_1h_threshold | +1.93% | +1.83% |
| ONDO/USDT:USDT | below_1h_threshold | +1.92% | +1.83% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.87% | +1.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
