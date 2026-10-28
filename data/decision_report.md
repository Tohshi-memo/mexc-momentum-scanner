# Decision Report

- generated_at: 2026-10-28T16:06:35.060147+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17727**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.80% / filled 20/20。**
- 全期間 MARKET基準: n=17727, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.80% | **+1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.32% | **+2.21%** |
| MARKET | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.90% | **+1.71%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.54% | **+1.15%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.56% | **+1.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.13% | **+0.23%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,543.68** / 初期 $100.00 (+1443.68%)
- 確定: 6771件 (Win 1970 / Loss 2170 / Flat 2631) / skip 7517件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,543.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$357.99** / 初期 $100.00 (+257.99%)
- 確定: 4248件 (Win 1153 / Loss 969 / Flat 2126) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0624 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $357.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5886件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000270 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T16:06:23.797399+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=80524.0
- Funnel: target 1083 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +3.08% | $16,633,163.64 |
| BLESS/USDT:USDT | +2.96% | $20,506,709.01 |
| CAP/USDT:USDT | +2.45% | $1,082,477.91 |
| EVAA/USDT:USDT | +2.16% | $20,394,678.70 |
| CBRSSTOCK/USDT:USDT | +0.81% | $2,248,658.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.59% | +3.59% |
| Q/USDT:USDT | below_1h_threshold | +2.99% | +2.99% |
| INIT/USDT:USDT | below_1h_threshold | +2.39% | +2.40% |
| CAP/USDT:USDT | below_1h_threshold | +2.18% | +2.18% |
| SNXX/USDT:USDT | below_1h_threshold | +2.03% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
