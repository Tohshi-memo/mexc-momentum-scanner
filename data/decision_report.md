# Decision Report

- generated_at: 2026-08-06T13:51:30.475225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10615**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10615, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.47% | **+0.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_FIB1272_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$596.41** / 初期 $100.00 (+496.41%)
- 確定: 3795件 (Win 1203 / Loss 1249 / Flat 1343) / skip 3381件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $596.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$145.07** / 初期 $100.00 (+45.07%)
- 確定: 1444件 (Win 404 / Loss 340 / Flat 700) / skip 2582件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0766 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $145.07

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 943件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T13:51:18.876914+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64422.6
- Funnel: target 958 → liquid 193 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.4 >= 65=1, 4h RSI 91.2 >= 65=1, 4h RSI 66.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HFT/USDT:USDT | +78.57% | $5,487,244.88 |
| CTSI/USDT:USDT | +73.90% | $2,748,416.69 |
| CASHCAT/USDT:USDT | +64.86% | $2,323,944.87 |
| BICO/USDT:USDT | +58.16% | $11,380,074.43 |
| ZBT/USDT:USDT | +49.81% | $4,931,068.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.25% | +3.20% |
| HOME/USDT:USDT | below_1h_threshold | +2.61% | +2.56% |
| RESOLV/USDT:USDT | below_1h_threshold | +2.49% | +2.45% |
| CTSI/USDT:USDT | below_1h_threshold | +2.13% | +2.09% |
| ZRO/USDT:USDT | below_1h_threshold | +1.99% | +1.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
