# Decision Report

- generated_at: 2026-07-31T06:51:27.848789+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9970**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9970, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.44% | **+0.97%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.14% | **+0.92%** |
| LIMIT_10PCT | 2/20 | 10.0% | +7.36% | **+0.74%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.38% | **+0.68%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.83% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.25% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.35% | **+0.19%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.24% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$552.25** / 初期 $100.00 (+452.25%)
- 確定: 3561件 (Win 1137 / Loss 1160 / Flat 1264) / skip 2970件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $552.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.49** / 初期 $100.00 (+41.49%)
- 確定: 1264件 (Win 355 / Loss 290 / Flat 619) / skip 2117件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1486 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $141.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.37** / 初期 $100.00 (+10.37%)
- 確定: 807件 (Win 262 / Loss 321 / Flat 224) / pending 4件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000471 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $110.37

## 6. Latest Market Context

- 更新: 2026-07-31T06:51:17.681810+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=64224.4
- Funnel: target 920 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +53.66% | $10,173,955.66 |
| MMT/USDT:USDT | +36.08% | $11,863,002.98 |
| AXTISTOCK/USDT:USDT | +30.13% | $4,453,643.13 |
| BULLA/USDT:USDT | +23.90% | $1,243,702.99 |
| GIGGLE/USDT:USDT | +18.13% | $1,855,949.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +4.37% | +4.54% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.80% | +3.97% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.17% | +3.34% |
| KORU/USDT:USDT | below_1h_threshold | +3.16% | +3.33% |
| SNXX/USDT:USDT | below_1h_threshold | +3.02% | +3.19% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
