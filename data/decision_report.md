# Decision Report

- generated_at: 2026-11-04T11:31:20.865193+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18118**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.99% / filled 20/20。**
- 全期間 MARKET基準: n=18118, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.62% | **+0.49%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.74% | **+0.41%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.72% | **+0.28%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.28% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.15% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,508.26** / 初期 $100.00 (+1408.26%)
- 確定: 6937件 (Win 2005 / Loss 2223 / Flat 2709) / skip 7742件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,508.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$373.57** / 初期 $100.00 (+273.57%)
- 確定: 4531件 (Win 1213 / Loss 1015 / Flat 2303) / skip 6998件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $373.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6277件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000124 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T11:31:08.019725+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78656.7
- Funnel: target 1073 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +29.92% | $4,205,490.71 |
| BMT/USDT:USDT | +18.52% | $1,728,396.35 |
| LSK/USDT:USDT | +14.32% | $3,671,270.47 |
| IDOL/USDT:USDT | +13.65% | $8,837,268.52 |
| USELESS/USDT:USDT | +12.46% | $3,403,944.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_1h_threshold | +2.73% | +2.64% |
| AXIS/USDT:USDT | below_1h_threshold | +2.62% | +2.53% |
| IDOL/USDT:USDT | below_1h_threshold | +2.61% | +2.53% |
| MVLL/USDT:USDT | below_1h_threshold | +2.48% | +2.40% |
| LIT/USDT:USDT | below_1h_threshold | +1.76% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
