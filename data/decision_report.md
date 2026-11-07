# Decision Report

- generated_at: 2026-11-07T17:46:24.603326+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18391**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18391, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 10/20 | 50.0% | +1.95% | **+0.98%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.89% | **+0.53%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.07% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.22% | **+0.92%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,499.42** / 初期 $100.00 (+1399.42%)
- 確定: 7087件 (Win 2036 / Loss 2262 / Flat 2789) / skip 7865件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,499.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4754件 (Win 1277 / Loss 1047 / Flat 2430) / skip 7048件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1069 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6550件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000378 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T17:46:08.816314+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=75824.1
- Funnel: target 1089 → liquid 128 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +24.93% | $13,364,847.00 |
| ONE/USDT:USDT | +14.00% | $26,020,870.70 |
| ESPORTS/USDT:USDT | +6.08% | $1,241,255.23 |
| BTW/USDT:USDT | +4.23% | $5,569,008.58 |
| ARIA/USDT:USDT | +4.10% | $1,693,050.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +3.78% | +3.63% |
| USELESS/USDT:USDT | below_1h_threshold | +3.38% | +3.24% |
| CLANKER/USDT:USDT | below_1h_threshold | +3.08% | +2.93% |
| BTW/USDT:USDT | below_1h_threshold | +1.58% | +1.44% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.16% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
