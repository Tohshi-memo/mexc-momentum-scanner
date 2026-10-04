# Decision Report

- generated_at: 2026-10-04T02:46:22.641945+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16086**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=16086, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.98% | **+1.88%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.92% | **+1.53%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.60% | **+1.04%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.48% | **+0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.05% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.26** / 初期 $100.00 (+1191.26%)
- 確定: 6149件 (Win 1812 / Loss 1972 / Flat 2365) / skip 6498件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPORTFUN/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,291.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3608件 (Win 1005 / Loss 845 / Flat 1758) / skip 5889件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0280 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4245件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000301 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-04T02:46:11.310148+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=84755.8
- Funnel: target 1086 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +17.46% | $1,571,451.95 |
| BATON/USDT:USDT | +15.68% | $1,199,039.54 |
| QNT/USDT:USDT | +9.76% | $249,891,700.35 |
| AKE/USDT:USDT | +9.56% | $4,026,292.42 |
| PUMPFUN/USDT:USDT | +8.93% | $43,305,008.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +3.61% | +3.62% |
| AIN/USDT:USDT | below_1h_threshold | +2.80% | +2.81% |
| BEAT/USDT:USDT | below_1h_threshold | +2.20% | +2.21% |
| AXS/USDT:USDT | below_1h_threshold | +1.52% | +1.53% |
| LTC/USDT:USDT | below_1h_threshold | +1.27% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
