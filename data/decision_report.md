# Decision Report

- generated_at: 2026-11-04T15:06:39.832108+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18126**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18126, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.84% | **+0.42%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_BB3S | 10/18 | 55.6% | +0.44% | **+0.24%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.39% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.50% | **+0.53%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.10% | **+0.50%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.10% | **+0.44%** |
| MARKET_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,505.42** / 初期 $100.00 (+1405.42%)
- 確定: 6945件 (Win 2008 / Loss 2226 / Flat 2711) / skip 7742件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,505.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$374.08** / 初期 $100.00 (+274.08%)
- 確定: 4537件 (Win 1216 / Loss 1018 / Flat 2303) / skip 7000件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $374.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6287件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000099 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T15:06:23.774040+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.28% price=80332.1
- Funnel: target 1078 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +61.99% | $5,877,219.94 |
| JCT/USDT:USDT | +21.39% | $5,639,961.61 |
| IDOL/USDT:USDT | +17.07% | $7,155,152.47 |
| USELESS/USDT:USDT | +15.46% | $3,723,694.19 |
| FLUID/USDT:USDT | +15.17% | $1,574,682.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLUID/USDT:USDT | below_1h_threshold | +3.74% | +2.46% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +3.57% | +2.30% |
| IDOL/USDT:USDT | below_1h_threshold | +3.18% | +1.90% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +2.93% | +1.66% |
| ENA/USDT:USDT | below_1h_threshold | +2.90% | +1.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
