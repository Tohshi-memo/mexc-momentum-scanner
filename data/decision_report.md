# Decision Report

- generated_at: 2026-11-13T06:01:22.625628+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18786**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=18786, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.56% | **+1.41%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.54% | **+1.31%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.06% | **+1.34%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.26% | **+0.88%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.75% | **+0.72%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,741.26** / 初期 $100.00 (+1641.26%)
- 確定: 7256件 (Win 2090 / Loss 2324 / Flat 2842) / skip 8091件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,741.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$404.31** / 初期 $100.00 (+304.31%)
- 確定: 4805件 (Win 1295 / Loss 1065 / Flat 2445) / skip 7392件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0680 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` TP_HIT account +0.69% 残高後 $404.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6945件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T06:01:09.801784+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=67907.8
- Funnel: target 1105 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOR/USDT:USDT | +50.60% | $1,689,563.07 |
| BARD/USDT:USDT | +47.87% | $10,490,476.59 |
| ARIA/USDT:USDT | +37.29% | $9,334,589.65 |
| AKE/USDT:USDT | +12.86% | $8,050,405.85 |
| CBRSSTOCK/USDT:USDT | +11.20% | $3,528,520.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.17% | +2.47% |
| NVD/USDT:USDT | below_1h_threshold | +1.36% | +1.66% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.83% | +1.13% |
| H/USDT:USDT | below_1h_threshold | +0.38% | +0.68% |
| ARIA/USDT:USDT | below_1h_threshold | +0.22% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
