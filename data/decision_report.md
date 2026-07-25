# Decision Report

- generated_at: 2026-07-25T07:26:21.155412+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9492**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9492, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.00% | **-0.00%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.24% | **-0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.83% | **-0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +4.22% | **+2.74%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.09% | **+2.63%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.01% | **+1.50%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.52% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$423.36** / 初期 $100.00 (+323.36%)
- 確定: 3326件 (Win 1048 / Loss 1077 / Flat 1201) / skip 2727件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $423.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1738件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1322 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$105.42** / 初期 $100.00 (+5.42%)
- 確定: 542件 (Win 181 / Loss 209 / Flat 152) / pending 6件 / skip 417件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000397 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $105.42

## 6. Latest Market Context

- 更新: 2026-07-25T07:26:14.234510+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63994.7
- Funnel: target 898 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +90.46% | $67,839,832.39 |
| EUL/USDT:USDT | +41.71% | $2,524,773.07 |
| AKE/USDT:USDT | +27.22% | $46,362,928.97 |
| ZAMA/USDT:USDT | +17.76% | $4,714,375.05 |
| B2/USDT:USDT | +15.77% | $3,108,400.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAITO/USDT:USDT | below_1h_threshold | +2.21% | +2.19% |
| SLX/USDT:USDT | below_1h_threshold | +1.14% | +1.12% |
| UB/USDT:USDT | below_1h_threshold | +0.96% | +0.94% |
| RIF/USDT:USDT | below_1h_threshold | +0.89% | +0.87% |
| BANK/USDT:USDT | below_1h_threshold | +0.88% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
