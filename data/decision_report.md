# Decision Report

- generated_at: 2026-07-18T08:01:10.419520+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8924**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=8924, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.80% | **+0.72%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.28% | **+0.46%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.76% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.51% | **+0.61%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.84% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.37% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$111.25** / 初期 $100.00 (+11.25%)
- 確定トレード: 115件 (TP 43 / SL 68 / EXP 4)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $111.25
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$361.87** / 初期 $100.00 (+261.87%)
- 確定: 3039件 (Win 942 / Loss 967 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $361.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.34** / 初期 $100.00 (+10.34%)
- 確定: 886件 (Win 208 / Loss 181 / Flat 497) / skip 1449件
- 成長率目線: 平均log +0.000111 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0109 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $110.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.91** / 初期 $100.00 (-0.09%)
- 確定: 179件 (Win 57 / Loss 95 / Flat 27) / pending 4件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000414 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STAR/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.91

## 6. Latest Market Context

- 更新: 2026-07-18T08:01:02.773214+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63994.0
- Funnel: target 885 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +49.59% | $56,020,014.63 |
| ESPORTS/USDT:USDT | +35.40% | $13,804,433.71 |
| TRADOOR/USDT:USDT | +23.01% | $2,627,674.31 |
| BSB/USDT:USDT | +12.15% | $1,311,552.61 |
| VVV/USDT:USDT | +12.12% | $2,834,210.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +1.29% | +1.27% |
| SYN/USDT:USDT | below_1h_threshold | +1.00% | +0.98% |
| LAB/USDT:USDT | below_1h_threshold | +0.93% | +0.90% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.61% | +0.59% |
| STAR/USDT:USDT | below_1h_threshold | +0.50% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
