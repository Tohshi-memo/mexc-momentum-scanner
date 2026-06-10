# Decision Report

- generated_at: 2026-06-10T22:45:02.181084+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6275**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6275, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.61% | **+0.51%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.73% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.56% | **+1.41%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.20% | **+1.10%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.01% | **+1.01%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |
| ASK_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.70** / 初期 $100.00 (+49.70%)
- 確定: 1261件 (Win 317 / Loss 395 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000320 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $149.70

## 4. Latest Market Context

- 更新: 2026-06-10T22:44:58.801457+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=61482.9
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +76.82% | $35,281,773.54 |
| BEAT/USDT:USDT | +23.16% | $177,273,630.86 |
| STRAX/USDT:USDT | +13.62% | $1,257,673.55 |
| FOLKS/USDT:USDT | +6.31% | $12,118,511.07 |
| POWER/USDT:USDT | +5.54% | $1,480,212.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_relative_strength | +5.05% | +4.80% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.64% | +2.39% |
| XMR/USDT:USDT | below_1h_threshold | +2.36% | +2.11% |
| MYX/USDT:USDT | below_1h_threshold | +1.34% | +1.09% |
| KITE/USDT:USDT | below_1h_threshold | +1.15% | +0.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
