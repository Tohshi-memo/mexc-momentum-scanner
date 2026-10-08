# Decision Report

- generated_at: 2026-10-08T04:41:24.321574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16310**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.85% / filled 20/20。**
- 全期間 MARKET基準: n=16310, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.96% | **+1.76%** |
| LIMIT_BB3S | 5/17 | 29.4% | +4.41% | **+1.30%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.34% | **+0.94%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.17% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.59% | **+0.40%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.33% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.12** / 初期 $100.00 (+21.12%)
- 確定トレード: 234件 (TP 86 / SL 141 / EXP 7)
- 最新: LONGXIA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,322.43** / 初期 $100.00 (+1222.43%)
- 確定: 6278件 (Win 1845 / Loss 2011 / Flat 2422) / skip 6593件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORCA/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,322.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6089件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4470件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000346 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-08T04:41:15.208731+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=82545.5
- Funnel: target 1073 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MET/USDT:USDT | +38.46% | $13,338,252.33 |
| W/USDT:USDT | +19.82% | $2,491,635.28 |
| BSPSTOCK/USDT:USDT | +17.79% | $1,130,714.01 |
| JUP/USDT:USDT | +17.42% | $22,943,790.57 |
| ACE/USDT:USDT | +13.49% | $1,991,411.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +1.51% | +1.72% |
| HEMI/USDT:USDT | below_1h_threshold | +1.19% | +1.40% |
| UAI/USDT:USDT | below_1h_threshold | +1.16% | +1.37% |
| BEAT/USDT:USDT | below_1h_threshold | +0.34% | +0.55% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.15% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
