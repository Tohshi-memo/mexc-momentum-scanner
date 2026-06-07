# Decision Report

- generated_at: 2026-06-07T14:50:16.132088+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5965**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5965, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.93% | **-1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +1.02% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.45% | **+2.89%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.59% | **+2.76%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.57% | **+2.50%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +5.17% | **+2.07%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.71% | **+1.48%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.82** / 初期 $100.00 (+48.82%)
- 確定: 1082件 (Win 264 / Loss 327 / Flat 491) / skip 1444件
- 成長率目線: 平均log +0.000367 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $148.82

## 4. Latest Market Context

- 更新: 2026-06-07T14:50:09.522230+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=61771.5
- Funnel: target 768 → liquid 126 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1, 4h RSI 81.7 >= 65=1, 4h RSI 70.3 >= 65=1, 4h RSI 77.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +67.01% | $9,152,062.89 |
| SIREN/USDT:USDT | +60.51% | $23,900,057.01 |
| BSB/USDT:USDT | +55.20% | $9,687,420.14 |
| BLESS/USDT:USDT | +41.67% | $5,742,474.50 |
| LAB/USDT:USDT | +38.86% | $63,870,405.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +4.42% | +4.26% |
| ZEC/USDT:USDT | below_1h_threshold | +3.63% | +3.47% |
| VVV/USDT:USDT | below_1h_threshold | +3.61% | +3.46% |
| H/USDT:USDT | below_1h_threshold | +3.51% | +3.35% |
| UB/USDT:USDT | below_1h_threshold | +3.44% | +3.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
