# Decision Report

- generated_at: 2026-06-06T20:21:41.906234+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5899**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5899, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +6.33% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +6.17% | **+4.63%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.40% | **+1.36%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$136.04** / 初期 $100.00 (+36.04%)
- 確定: 1032件 (Win 247 / Loss 317 / Flat 468) / skip 1428件
- 成長率目線: 平均log +0.000298 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $136.04

## 4. Latest Market Context

- 更新: 2026-06-06T20:21:38.422813+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=60546.7
- Funnel: target 771 → liquid 128 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +37.93% | $17,298,086.76 |
| LAB/USDT:USDT | +37.33% | $50,332,738.03 |
| BTW/USDT:USDT | +36.05% | $14,873,457.21 |
| FIDA/USDT:USDT | +27.70% | $1,970,608.86 |
| BLUAI/USDT:USDT | +10.68% | $7,201,671.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.65% | +4.68% |
| ALLO/USDT:USDT | below_1h_threshold | +2.56% | +2.59% |
| LAB/USDT:USDT | below_1h_threshold | +1.65% | +1.68% |
| HOME/USDT:USDT | below_1h_threshold | +1.54% | +1.57% |
| BABY/USDT:USDT | below_1h_threshold | +1.25% | +1.28% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
