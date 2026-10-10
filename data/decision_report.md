# Decision Report

- generated_at: 2026-10-10T07:31:10.033307+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16479**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.50% / filled 20/20。**
- 全期間 MARKET基準: n=16479, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.55% | **+0.41%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.38% | **+0.31%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +0.18% | **+0.12%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.06% | **+0.03%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.04% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,303.26** / 初期 $100.00 (+1203.26%)
- 確定: 6286件 (Win 1845 / Loss 2014 / Flat 2427) / skip 6754件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LPT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.46% 残高後 $1,303.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3636件 (Win 1010 / Loss 853 / Flat 1773) / skip 6254件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0069 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4638件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000150 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-10T07:31:01.892304+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=82599.6
- Funnel: target 1089 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGIC/USDT:USDT | +52.69% | $16,759,145.18 |
| CAP/USDT:USDT | +28.10% | $1,824,334.17 |
| RLC/USDT:USDT | +16.95% | $46,062,208.21 |
| PIXEL/USDT:USDT | +15.73% | $5,760,460.47 |
| BAT/USDT:USDT | +13.72% | $15,788,159.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TMX/USDT:USDT | below_1h_threshold | +2.38% | +2.50% |
| UAI/USDT:USDT | below_1h_threshold | +2.02% | +2.14% |
| BAT/USDT:USDT | below_1h_threshold | +1.53% | +1.65% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.45% | +1.57% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.68% | +0.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
