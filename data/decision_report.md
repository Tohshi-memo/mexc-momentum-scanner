# Decision Report

- generated_at: 2026-10-31T15:56:18.156701+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17906**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=17906, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.53% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.29% | **+0.26%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.15% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 257件 (TP 95 / SL 154 / EXP 8)
- 最新: JCT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.74** / 初期 $100.00 (+1385.74%)
- 確定: 6820件 (Win 1976 / Loss 2188 / Flat 2656) / skip 7647件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAMX/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,485.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$369.63** / 初期 $100.00 (+269.63%)
- 確定: 4406件 (Win 1184 / Loss 983 / Flat 2239) / skip 6911件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0726 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $369.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6068件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-31T15:56:07.210589+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=77560.0
- Funnel: target 1089 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +43.88% | $20,351,440.35 |
| AIN/USDT:USDT | +36.15% | $22,950,292.61 |
| RSR/USDT:USDT | +19.92% | $1,051,457.14 |
| UAI/USDT:USDT | +17.01% | $1,309,245.78 |
| RUNE/USDT:USDT | +13.70% | $2,125,783.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +3.95% | +3.72% |
| LIT/USDT:USDT | below_1h_threshold | +2.76% | +2.53% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.50% | +2.27% |
| ZRO/USDT:USDT | below_1h_threshold | +2.44% | +2.21% |
| AIN/USDT:USDT | below_1h_threshold | +2.35% | +2.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
