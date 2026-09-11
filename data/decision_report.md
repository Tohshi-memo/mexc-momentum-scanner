# Decision Report

- generated_at: 2026-09-11T18:16:27.502392+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14244**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=14244, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.02% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.02% | **+0.31%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.04% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +5.30% | **+3.97%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.08% | **+0.86%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.73%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.51% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 210件 (TP 78 / SL 127 / EXP 5)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,101.01** / 初期 $100.00 (+1001.01%)
- 確定: 5401件 (Win 1629 / Loss 1748 / Flat 2024) / skip 5404件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,101.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2818件 (Win 775 / Loss 655 / Flat 1388) / skip 4837件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0013 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.69** / 初期 $100.00 (+23.69%)
- 確定: 2736件 (Win 810 / Loss 1049 / Flat 877) / pending 4件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.69

## 6. Latest Market Context

- 更新: 2026-09-11T18:16:16.400365+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=77098.2
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 85.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +25.08% | $6,966,002.71 |
| LAB/USDT:USDT | +21.69% | $5,363,939.64 |
| BEAT/USDT:USDT | +6.55% | $7,757,431.13 |
| FOLKS/USDT:USDT | +2.39% | $1,170,914.26 |
| HNT/USDT:USDT | +2.31% | $1,895,559.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.26% | +2.77% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.97% | +2.48% |
| RIVER/USDT:USDT | below_1h_threshold | +1.87% | +2.38% |
| MET/USDT:USDT | below_1h_threshold | +1.30% | +1.81% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
