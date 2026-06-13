# Decision Report

- generated_at: 2026-06-13T21:52:46.388359+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6612**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6612, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +2.47% | **+1.48%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.74% | **+1.22%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.07% | **+0.64%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.13** / 初期 $100.00 (+68.13%)
- 確定: 1485件 (Win 400 / Loss 474 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000350 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $168.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.78** / 初期 $100.00 (-1.22%)
- 確定: 23件 (Win 7 / Loss 10 / Flat 6) / skip 0件
- 成長率目線: 平均log -0.000533 / 幾何平均 -0.053% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0177 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.78

## 5. Latest Market Context

- 更新: 2026-06-13T21:52:41.394006+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=64420.1
- Funnel: target 770 → liquid 131 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +20.75% | $10,353,789.23 |
| MEGA/USDT:USDT | +9.95% | $2,267,970.78 |
| BTW/USDT:USDT | +9.64% | $1,862,738.21 |
| COAI/USDT:USDT | +7.82% | $32,370,923.47 |
| JASMY/USDT:USDT | +5.18% | $1,218,449.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +3.14% | +2.88% |
| H/USDT:USDT | below_1h_threshold | +2.72% | +2.46% |
| RIF/USDT:USDT | below_1h_threshold | +2.20% | +1.94% |
| MEGA/USDT:USDT | below_1h_threshold | +1.97% | +1.71% |
| JASMY/USDT:USDT | below_1h_threshold | +1.88% | +1.62% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
