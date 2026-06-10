# Decision Report

- generated_at: 2026-06-10T09:54:57.015169+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6208**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6208, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.01% | **+0.35%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.88% | **+0.09%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.02** / 初期 $100.00 (+52.02%)
- 確定: 1224件 (Win 306 / Loss 380 / Flat 538) / skip 1545件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $152.02

## 4. Latest Market Context

- 更新: 2026-06-10T09:54:51.730991+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=61279.9
- Funnel: target 785 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +49.33% | $10,865,863.54 |
| ESPORTS/USDT:USDT | +33.76% | $27,130,509.17 |
| KAT/USDT:USDT | +27.15% | $1,069,915.10 |
| BTW/USDT:USDT | +20.38% | $30,904,199.27 |
| BEAT/USDT:USDT | +16.25% | $103,784,016.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLFI/USDT:USDT | below_1h_threshold | +2.97% | +2.89% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.81% | +1.72% |
| SENT/USDT:USDT | below_1h_threshold | +1.75% | +1.66% |
| KAT/USDT:USDT | below_1h_threshold | +1.67% | +1.59% |
| WLD/USDT:USDT | below_1h_threshold | +1.48% | +1.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
