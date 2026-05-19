# Decision Report

- generated_at: 2026-05-19T16:18:41.100322+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4478**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4478, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.03% | **+0.02%** |
| ASK | 20/20 | 100.0% | -0.28% | **-0.28%** |
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.76% | **+1.66%** |
| MARKET_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| ASK_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.94% | **+0.59%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.97% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 566件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T16:18:36.026987+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=76481.4
- Funnel: target 764 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +12.12% | $6,974,720.30 |
| LAB/USDT:USDT | +6.96% | $80,810,289.55 |
| EDEN/USDT:USDT | +4.45% | $3,947,062.26 |
| AT/USDT:USDT | +2.25% | $2,723,353.61 |
| VVV/USDT:USDT | +2.14% | $5,721,935.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +4.53% | +4.54% |
| AT/USDT:USDT | below_1h_threshold | +2.26% | +2.27% |
| VVV/USDT:USDT | below_1h_threshold | +2.25% | +2.26% |
| H/USDT:USDT | below_1h_threshold | +1.47% | +1.48% |
| LIT/USDT:USDT | below_1h_threshold | +1.46% | +1.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
