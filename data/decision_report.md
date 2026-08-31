# Decision Report

- generated_at: 2026-08-31T14:11:31.796916+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13179**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=13179, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.95% | **+0.86%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.77% | **+0.71%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.64% | **+0.51%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.38% | **+0.34%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.76% | **+0.34%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.34% | **+0.25%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.14% | **+0.06%** |
| MARKET_LONG | 20/20 | 100.0% | -0.17% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4876件 (Win 1485 / Loss 1609 / Flat 1782) / skip 4864件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.38** / 初期 $100.00 (+73.38%)
- 確定: 2176件 (Win 603 / Loss 528 / Flat 1045) / skip 4414件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0025 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2084件 (Win 610 / Loss 812 / Flat 662) / pending 0件 / skip 2565件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000506 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-31T14:11:18.014910+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77910.2
- Funnel: target 1031 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKR/USDT:USDT | +81.48% | $58,147,659.69 |
| PONS/USDT:USDT | +45.15% | $2,403,569.43 |
| HEMI/USDT:USDT | +40.91% | $8,369,097.66 |
| BASECAT/USDT:USDT | +31.82% | $2,058,572.03 |
| ZORA/USDT:USDT | +30.76% | $15,392,708.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TESLA/USDT:USDT | below_1h_threshold | +4.19% | +4.09% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.45% | +3.36% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +2.85% | +2.75% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.32% |
| SOXL/USDT:USDT | below_1h_threshold | +1.91% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
