# Decision Report

- generated_at: 2026-08-06T05:36:37.590111+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10529**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10529, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_7PCT | 9/20 | 45.0% | +4.36% | **+1.96%** |
| LIMIT_6PCT | 11/20 | 55.0% | +1.93% | **+1.06%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.68% | **+3.32%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.95% | **+1.92%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.04% | **+1.52%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3771件 (Win 1195 / Loss 1236 / Flat 1340) / skip 3319件
- 成長率目線: 平均log +0.000477 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.11** / 初期 $100.00 (+40.11%)
- 確定: 1367件 (Win 379 / Loss 321 / Flat 667) / skip 2573件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0521 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $140.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 859件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000272 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T05:36:23.426007+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=64868.5
- Funnel: target 952 → liquid 188 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.8 >= 65=1, 4h RSI 84.8 >= 65=1, 4h RSI 86.6 >= 65=1, 4h RSI 73.2 >= 65=1, 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +132.06% | $50,594,460.37 |
| DODO/USDT:USDT | +69.10% | $8,246,824.70 |
| BLESS/USDT:USDT | +64.16% | $119,556,493.60 |
| HFT/USDT:USDT | +33.54% | $5,759,537.37 |
| BICO/USDT:USDT | +28.02% | $11,808,854.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.88% | +4.61% |
| CAP/USDT:USDT | below_1h_threshold | +4.14% | +3.87% |
| RESOLV/USDT:USDT | below_1h_threshold | +2.22% | +1.95% |
| ZBT/USDT:USDT | below_1h_threshold | +1.73% | +1.46% |
| IONQSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
