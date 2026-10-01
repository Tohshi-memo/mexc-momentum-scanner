# Decision Report

- generated_at: 2026-10-01T23:01:21.052451+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15950**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=15950, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.56% | **+1.41%** |
| LIMIT_6PCT | 5/20 | 25.0% | +5.55% | **+1.39%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.77% | **+1.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +4.45% | **+4.45%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.92% | **+0.82%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.80% | **+0.68%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +0.50% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.40** / 初期 $100.00 (+1210.40%)
- 確定: 6057件 (Win 1795 / Loss 1954 / Flat 2308) / skip 6454件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,310.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.39** / 初期 $100.00 (+176.39%)
- 確定: 3603件 (Win 1005 / Loss 843 / Flat 1755) / skip 5758件
- 成長率目線: 平均log +0.000282 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0750 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $276.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4116件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000325 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T23:01:10.333650+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=84671.6
- Funnel: target 1097 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +85.88% | $2,994,494.04 |
| SI/USDT:USDT | +16.61% | $4,443,395.04 |
| LONGXIA/USDT:USDT | +14.21% | $12,066,641.25 |
| MAGMA/USDT:USDT | +12.57% | $1,484,550.71 |
| UAI/USDT:USDT | +10.68% | $2,083,035.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKAMSTOCK/USDT:USDT | below_1h_threshold | +1.15% | +1.19% |
| BATON/USDT:USDT | below_1h_threshold | +0.95% | +0.99% |
| GRASS/USDT:USDT | below_1h_threshold | +0.85% | +0.90% |
| SOXL/USDT:USDT | below_1h_threshold | +0.72% | +0.76% |
| KORU/USDT:USDT | below_1h_threshold | +0.58% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
