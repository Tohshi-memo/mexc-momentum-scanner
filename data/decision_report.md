# Decision Report

- generated_at: 2026-08-05T04:01:24.602074+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10349**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10349, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-3.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.25% | **-3.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.69% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.44% | **+2.58%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.53% | **+1.94%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.92% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.85** / 初期 $100.00 (+506.85%)
- 確定: 3746件 (Win 1188 / Loss 1224 / Flat 1334) / skip 3164件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $606.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.02** / 初期 $100.00 (+41.02%)
- 確定: 1287件 (Win 361 / Loss 299 / Flat 627) / skip 2473件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0687 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $141.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.02** / 初期 $100.00 (+19.02%)
- 確定: 1105件 (Win 357 / Loss 425 / Flat 323) / pending 4件 / skip 716件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.02

## 6. Latest Market Context

- 更新: 2026-08-05T04:01:14.157238+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64155.1
- Funnel: target 939 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +84.53% | $8,924,771.44 |
| TAKE/USDT:USDT | +36.80% | $1,533,554.48 |
| CASHCAT/USDT:USDT | +31.73% | $1,169,805.81 |
| MARSCOIN/USDT:USDT | +30.68% | $1,143,386.23 |
| BLESS/USDT:USDT | +29.83% | $21,216,540.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_1h_threshold | +3.59% | +3.58% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.85% |
| MVLL/USDT:USDT | below_1h_threshold | +2.82% | +2.81% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.00% | +1.99% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.98% | +1.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
