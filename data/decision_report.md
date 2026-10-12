# Decision Report

- generated_at: 2026-10-12T20:11:22.515738+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16607**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=16607, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.08% | **+0.70%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.69% | **+0.51%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.75** / 初期 $100.00 (+1191.75%)
- 確定: 6292件 (Win 1845 / Loss 2016 / Flat 2431) / skip 6876件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,291.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$272.12** / 初期 $100.00 (+172.12%)
- 確定: 3639件 (Win 1010 / Loss 855 / Flat 1774) / skip 6379件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0670 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RSR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $272.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4768件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-12T20:11:10.662442+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=83030.9
- Funnel: target 1089 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OGN/USDT:USDT | +16.47% | $3,673,505.98 |
| STX/USDT:USDT | +11.63% | $5,167,543.71 |
| XAI/USDT:USDT | +5.15% | $1,139,679.48 |
| RENDER/USDT:USDT | +5.09% | $10,583,480.96 |
| STRK/USDT:USDT | +4.66% | $73,263,926.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RENDER/USDT:USDT | below_1h_threshold | +2.56% | +2.32% |
| CT/USDT:USDT | below_1h_threshold | +2.26% | +2.02% |
| PLUME/USDT:USDT | below_1h_threshold | +1.73% | +1.49% |
| IO/USDT:USDT | below_1h_threshold | +1.38% | +1.13% |
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +1.30% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
