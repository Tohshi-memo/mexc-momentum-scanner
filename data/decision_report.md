# Decision Report

- generated_at: 2026-10-22T20:56:25.112475+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17169**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.12% / filled 20/20。**
- 全期間 MARKET基準: n=17169, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.12% | **+2.12%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.45% | **+1.23%** |
| LIMIT_BB3S | 5/19 | 26.3% | +2.37% | **+0.62%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.88% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +2.19% | **+0.87%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.17% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.04** / 初期 $100.00 (+1242.04%)
- 確定: 6529件 (Win 1897 / Loss 2083 / Flat 2549) / skip 7201件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,342.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.63** / 初期 $100.00 (+177.63%)
- 確定: 3849件 (Win 1055 / Loss 899 / Flat 1895) / skip 6731件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0440 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $277.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5331件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T20:56:12.723882+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=81189.7
- Funnel: target 1096 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +45.75% | $6,358,087.59 |
| DNA/USDT:USDT | +13.81% | $2,612,107.83 |
| SOXS/USDT:USDT | +4.68% | $25,147,817.98 |
| ALT/USDT:USDT | +4.30% | $5,159,487.67 |
| SQQQ/USDT:USDT | +2.43% | $1,609,661.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +1.12% | +1.46% |
| IBMSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +1.22% |
| DASH/USDT:USDT | below_1h_threshold | +0.67% | +1.00% |
| ALT/USDT:USDT | below_1h_threshold | +0.65% | +0.99% |
| VLOSTOCK/USDT:USDT | below_1h_threshold | +0.58% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
