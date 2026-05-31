# Decision Report

- generated_at: 2026-05-31T19:10:59.495057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5216**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5216, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.00% | **+4.00%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.25% | **+1.79%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.14% | **+1.41%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.66% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.87** / 初期 $100.00 (+29.87%)
- 確定: 851件 (Win 197 / Loss 253 / Flat 401) / skip 926件
- 成長率目線: 平均log +0.000307 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $129.87

## 4. Latest Market Context

- 更新: 2026-05-31T19:10:56.682172+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=73574.8
- Funnel: target 773 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +40.00% | $10,891,841.99 |
| HOME/USDT:USDT | +11.39% | $2,462,437.93 |
| BSB/USDT:USDT | +8.29% | $4,526,916.96 |
| UB/USDT:USDT | +7.29% | $6,662,744.59 |
| SKYAI/USDT:USDT | +7.01% | $4,852,788.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.27% | +2.27% |
| HOME/USDT:USDT | below_1h_threshold | +0.96% | +0.96% |
| PORTAL/USDT:USDT | below_1h_threshold | +0.92% | +0.92% |
| AIA/USDT:USDT | below_1h_threshold | +0.38% | +0.38% |
| RENDER/USDT:USDT | below_1h_threshold | +0.34% | +0.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
