# Decision Report

- generated_at: 2026-08-01T01:26:24.936055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10042**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.10% / filled 20/20。**
- 全期間 MARKET基準: n=10042, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.55% | **+1.39%** |
| MARKET | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_BB3S | 4/20 | 20.0% | +1.52% | **+0.30%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.24% | **+0.81%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.87% | **+0.43%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.58% | **+0.38%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.18% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$575.43** / 初期 $100.00 (+475.43%)
- 確定: 3594件 (Win 1150 / Loss 1175 / Flat 1269) / skip 3009件
- 成長率目線: 平均log +0.000487 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $575.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2174件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.78** / 初期 $100.00 (+11.78%)
- 確定: 864件 (Win 280 / Loss 342 / Flat 242) / pending 6件 / skip 648件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.78

## 6. Latest Market Context

- 更新: 2026-08-01T01:26:14.185335+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=62938.4
- Funnel: target 921 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +26.89% | $1,138,914.24 |
| GIGGLE/USDT:USDT | +19.19% | $22,200,388.90 |
| US/USDT:USDT | +17.48% | $2,447,428.95 |
| 1000RATS/USDT:USDT | +15.28% | $17,909,630.68 |
| KOMA/USDT:USDT | +15.26% | $17,957,387.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.93% | +4.88% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.90% | +2.86% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +2.87% | +2.82% |
| BANK/USDT:USDT | below_1h_threshold | +1.72% | +1.67% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.63% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
