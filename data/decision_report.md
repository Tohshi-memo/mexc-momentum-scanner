# Decision Report

- generated_at: 2026-07-17T17:26:19.620044+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8869**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8869, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.39% | **+1.19%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.91% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| LIMIT_6PCT_LONG | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.82% | **+1.41%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.80% | **+1.26%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +4.14% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$355.26** / 初期 $100.00 (+255.26%)
- 確定: 2984件 (Win 929 / Loss 951 / Flat 1104) / skip 2446件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.07% 残高後 $355.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.02** / 初期 $100.00 (+10.02%)
- 確定: 831件 (Win 198 / Loss 172 / Flat 461) / skip 1449件
- 成長率目線: 平均log +0.000115 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0650 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $110.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.06** / 初期 $100.00 (-0.94%)
- 確定: 134件 (Win 42 / Loss 75 / Flat 17) / pending 6件 / skip 205件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000221 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.06

## 6. Latest Market Context

- 更新: 2026-07-17T17:26:11.510475+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.70% price=64001.7
- Funnel: target 885 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +19.45% | $1,125,321.90 |
| AKE/USDT:USDT | +5.79% | $40,108,356.35 |
| KIOXIASTOCK/USDT:USDT | +5.40% | $1,442,980.21 |
| ARX/USDT:USDT | +5.37% | $1,188,823.26 |
| MVLL/USDT:USDT | +4.23% | $2,098,364.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARX/USDT:USDT | below_1h_threshold | +2.87% | +2.16% |
| BANK/USDT:USDT | below_1h_threshold | +2.79% | +2.09% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.74% | +2.04% |
| GALA/USDT:USDT | below_1h_threshold | +2.69% | +1.99% |
| METASTOCK/USDT:USDT | below_1h_threshold | +2.64% | +1.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
