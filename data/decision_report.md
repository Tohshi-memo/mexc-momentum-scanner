# Decision Report

- generated_at: 2026-07-27T01:46:19.500280+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9588**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.94% / filled 20/20。**
- 全期間 MARKET基準: n=9588, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.25% | **+2.13%** |
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_ATR | 15/20 | 75.0% | +2.01% | **+1.51%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.98% | **+0.69%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定トレード: 143件 (TP 49 / SL 89 / EXP 5)
- 最新: PRL/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.40
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$450.30** / 初期 $100.00 (+350.30%)
- 確定: 3400件 (Win 1078 / Loss 1107 / Flat 1215) / skip 2749件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $450.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1223件 (Win 338 / Loss 275 / Flat 610) / skip 1776件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0368 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.21** / 初期 $100.00 (+8.21%)
- 確定: 616件 (Win 207 / Loss 238 / Flat 171) / pending 1件 / skip 440件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000062 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.11% 残高後 $108.21

## 6. Latest Market Context

- 更新: 2026-07-27T01:46:12.457128+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=65065.9
- Funnel: target 898 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESP/USDT:USDT | +27.90% | $6,655,643.49 |
| SAFE/USDT:USDT | +17.97% | $1,536,237.51 |
| 4/USDT:USDT | +17.13% | $2,344,026.95 |
| AKE/USDT:USDT | +11.08% | $17,604,892.56 |
| UB/USDT:USDT | +9.77% | $3,928,180.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +2.52% | +2.59% |
| DIA/USDT:USDT | below_1h_threshold | +2.27% | +2.33% |
| 4/USDT:USDT | below_1h_threshold | +2.25% | +2.32% |
| ONDO/USDT:USDT | below_1h_threshold | +2.14% | +2.20% |
| AKE/USDT:USDT | below_1h_threshold | +2.00% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
