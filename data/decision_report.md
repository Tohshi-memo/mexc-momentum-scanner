# Decision Report

- generated_at: 2026-06-01T01:30:15.694330+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5254**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5254, expectancy=-0.06%
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
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.81% | **+1.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.26% | **+1.14%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.66% | **+1.00%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.55% | **+0.89%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.54% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.35** / 初期 $100.00 (+34.35%)
- 確定: 888件 (Win 207 / Loss 264 / Flat 417) / skip 927件
- 成長率目線: 平均log +0.000333 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $134.35

## 4. Latest Market Context

- 更新: 2026-06-01T01:30:12.838954+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=73570.0
- Funnel: target 775 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1, 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +166.08% | $23,172,182.11 |
| H/USDT:USDT | +58.37% | $16,855,122.23 |
| STG/USDT:USDT | +27.86% | $21,923,934.02 |
| HOME/USDT:USDT | +20.14% | $3,606,462.88 |
| PLAY/USDT:USDT | +20.01% | $15,574,517.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.29% | +3.68% |
| APE/USDT:USDT | below_1h_threshold | +2.22% | +2.60% |
| ID/USDT:USDT | below_1h_threshold | +1.88% | +2.26% |
| NEX/USDT:USDT | below_1h_threshold | +1.70% | +2.09% |
| MEGA/USDT:USDT | below_1h_threshold | +1.65% | +2.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
