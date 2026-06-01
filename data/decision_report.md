# Decision Report

- generated_at: 2026-06-01T01:35:24.149667+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5256**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5256, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.19% | **+0.48%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.15% | **+1.40%** |
| LIMIT_BB3S_LONG | 8/11 | 72.7% | +1.77% | **+1.29%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.13% | **+1.25%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.47% | **+1.25%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.01% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.01** / 初期 $100.00 (+33.01%)
- 確定: 890件 (Win 207 / Loss 266 / Flat 417) / skip 927件
- 成長率目線: 平均log +0.000321 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $133.01

## 4. Latest Market Context

- 更新: 2026-06-01T01:35:20.585183+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=73579.2
- Funnel: target 777 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1, 4h RSI 73.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +144.16% | $23,511,089.72 |
| H/USDT:USDT | +64.38% | $17,069,944.79 |
| STG/USDT:USDT | +25.04% | $21,963,396.21 |
| PLAY/USDT:USDT | +19.84% | $15,672,466.16 |
| HOME/USDT:USDT | +17.91% | $3,630,050.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_1h_threshold | +2.13% | +2.51% |
| WLD/USDT:USDT | below_1h_threshold | +2.13% | +2.50% |
| NEX/USDT:USDT | below_1h_threshold | +2.04% | +2.41% |
| APE/USDT:USDT | below_1h_threshold | +1.93% | +2.31% |
| ID/USDT:USDT | below_1h_threshold | +1.88% | +2.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
