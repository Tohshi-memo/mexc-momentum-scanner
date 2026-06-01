# Decision Report

- generated_at: 2026-06-01T01:10:56.295170+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5251**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5251, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

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
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.67% | **+1.34%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.34% | **+1.34%** |
| LIMIT_BB3S_LONG | 7/11 | 63.6% | +1.90% | **+1.21%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |
| MARKET_LONG | 20/20 | 100.0% | +1.11% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.24** / 初期 $100.00 (+34.24%)
- 確定: 885件 (Win 206 / Loss 262 / Flat 417) / skip 927件
- 成長率目線: 平均log +0.000333 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $134.24

## 4. Latest Market Context

- 更新: 2026-06-01T01:10:54.154409+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=73561.5
- Funnel: target 775 → liquid 130 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1, 4h RSI 76.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +167.37% | $22,605,447.15 |
| H/USDT:USDT | +59.28% | $15,702,798.64 |
| STG/USDT:USDT | +29.74% | $21,835,627.77 |
| HOME/USDT:USDT | +20.86% | $3,467,085.39 |
| PLAY/USDT:USDT | +20.04% | $15,262,264.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.92% | +4.31% |
| APE/USDT:USDT | below_1h_threshold | +1.50% | +1.90% |
| CTR/USDT:USDT | below_1h_threshold | +1.47% | +1.87% |
| STG/USDT:USDT | below_1h_threshold | +1.42% | +1.81% |
| ID/USDT:USDT | below_1h_threshold | +1.17% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
