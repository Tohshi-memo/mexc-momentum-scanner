# Decision Report

- generated_at: 2026-07-21T07:51:20.989306+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9160**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9160, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.11% | **+0.11%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.08% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.00% | **+1.70%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.94% | **+0.61%** |
| MARKET_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.50% | **+0.30%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$424.12** / 初期 $100.00 (+324.12%)
- 確定: 3222件 (Win 1012 / Loss 1026 / Flat 1184) / skip 2499件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $424.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.87** / 初期 $100.00 (+31.87%)
- 確定: 1121件 (Win 298 / Loss 234 / Flat 589) / skip 1450件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1035 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $131.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 293件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000215 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T07:51:12.910161+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=66155.0
- Funnel: target 885 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +129.83% | $3,999,128.33 |
| ERA/USDT:USDT | +50.77% | $6,006,818.26 |
| ZHIPUSTOCK/USDT:USDT | +35.31% | $2,951,594.77 |
| VVV/USDT:USDT | +11.21% | $1,727,090.80 |
| BLESS/USDT:USDT | +10.75% | $2,447,987.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +4.43% | +4.03% |
| US/USDT:USDT | below_1h_threshold | +4.32% | +3.92% |
| MVLL/USDT:USDT | below_1h_threshold | +3.46% | +3.06% |
| ON/USDT:USDT | below_1h_threshold | +3.45% | +3.06% |
| UB/USDT:USDT | below_1h_threshold | +2.73% | +2.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
