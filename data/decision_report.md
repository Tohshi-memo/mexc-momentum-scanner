# Decision Report

- generated_at: 2026-10-06T01:31:31.251835+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16177**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.27% / filled 20/20。**
- 全期間 MARKET基準: n=16177, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.99% | **+0.94%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.20% | **+0.78%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.72% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +5.24% | **+5.24%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.86% | **+1.72%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.70% | **+1.02%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.87% | **+0.39%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.59% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,284.21** / 初期 $100.00 (+1184.21%)
- 確定: 6234件 (Win 1825 / Loss 1992 / Flat 2417) / skip 6504件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,284.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3611件 (Win 1005 / Loss 845 / Flat 1761) / skip 5977件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RLC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4335件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T01:31:17.645422+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=85898.0
- Funnel: target 1074 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +40.94% | $18,291,255.33 |
| ORCA/USDT:USDT | +22.01% | $2,013,587.32 |
| BR/USDT:USDT | +15.87% | $15,240,277.14 |
| RAY/USDT:USDT | +9.13% | $4,850,252.21 |
| CHIP/USDT:USDT | +8.24% | $2,099,820.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_1h_threshold | +3.49% | +3.46% |
| ZRO/USDT:USDT | below_1h_threshold | +0.95% | +0.92% |
| AXS/USDT:USDT | below_1h_threshold | +0.79% | +0.76% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.64% | +0.61% |
| SOXL/USDT:USDT | below_1h_threshold | +0.53% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
