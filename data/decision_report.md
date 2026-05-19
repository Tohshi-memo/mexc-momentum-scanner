# Decision Report

- generated_at: 2026-05-19T22:38:37.087145+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4508**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4508, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_BB3S | 6/12 | 50.0% | +1.25% | **+0.63%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 596件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T22:38:34.802465+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=76680.7
- Funnel: target 759 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +38.75% | $6,339,965.91 |
| EDEN/USDT:USDT | +27.99% | $15,564,552.43 |
| BSB/USDT:USDT | +17.38% | $34,778,866.43 |
| LIT/USDT:USDT | +14.85% | $3,273,274.94 |
| BANANAS31/USDT:USDT | +14.26% | $1,350,400.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +2.48% | +2.82% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.35% | +1.69% |
| HOME/USDT:USDT | below_1h_threshold | +1.19% | +1.53% |
| XMR/USDT:USDT | below_1h_threshold | +0.34% | +0.68% |
| PLAY/USDT:USDT | below_1h_threshold | +0.27% | +0.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
