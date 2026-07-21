# Decision Report

- generated_at: 2026-07-21T14:21:23.747982+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9181**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9181, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.80% | **-1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_BB3S | 8/18 | 44.4% | +0.78% | **+0.34%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.21% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.79% | **+1.43%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.12% | **+1.09%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.16** / 初期 $100.00 (+326.16%)
- 確定: 3243件 (Win 1021 / Loss 1035 / Flat 1187) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COINBASE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $426.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.73** / 初期 $100.00 (+32.73%)
- 確定: 1142件 (Win 308 / Loss 243 / Flat 591) / skip 1450件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0807 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COINBASE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $132.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000215 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T14:21:17.397897+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=66825.5
- Funnel: target 885 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +99.83% | $1,300,245.59 |
| JIMOTHY/USDT:USDT | +80.43% | $5,007,544.39 |
| ERA/USDT:USDT | +64.05% | $12,033,243.74 |
| ESPORTS/USDT:USDT | +40.44% | $7,616,418.58 |
| ONE/USDT:USDT | +35.00% | $1,125,930.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.46% | +4.34% |
| ESPORTS/USDT:USDT | below_1h_threshold | +4.37% | +4.25% |
| POETSTOCK/USDT:USDT | below_1h_threshold | +3.47% | +3.36% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.40% | +2.28% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.36% | +2.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
