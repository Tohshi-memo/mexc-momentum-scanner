# Decision Report

- generated_at: 2026-06-07T16:16:47.957151+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5978**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5978, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.11% | **-2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -1.99% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.85% | **+2.28%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.29% | **+2.14%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.82% | **+1.72%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.03% | **+1.67%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.85% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.20** / 初期 $100.00 (+49.20%)
- 確定: 1095件 (Win 265 / Loss 329 / Flat 501) / skip 1444件
- 成長率目線: 平均log +0.000365 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $149.20

## 4. Latest Market Context

- 更新: 2026-06-07T16:16:44.275571+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=62166.8
- Funnel: target 768 → liquid 122 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.9 >= 65=1, 4h RSI 80.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +16.18% | $1,028,935.41 |
| ESPORTS/USDT:USDT | +6.36% | $3,191,318.66 |
| PIPPIN/USDT:USDT | +4.47% | $1,850,771.44 |
| SKYAI/USDT:USDT | +4.18% | $45,495,627.96 |
| RAVE/USDT:USDT | +4.00% | $1,833,241.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +4.48% | +4.32% |
| RAVE/USDT:USDT | below_1h_threshold | +4.09% | +3.94% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.08% | +3.93% |
| VELVET/USDT:USDT | below_1h_threshold | +3.03% | +2.87% |
| BEAT/USDT:USDT | below_1h_threshold | +3.01% | +2.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
