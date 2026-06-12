# Decision Report

- generated_at: 2026-06-12T18:01:13.003225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6533**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=6533, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| ASK | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.98% | **+1.09%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.22% | **+0.97%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.79% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.46% | **+0.99%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +5.66% | **+0.57%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.20% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$94.22** / 初期 $100.00 (-5.78%)
- 確定トレード: 22件 (TP 3 / SL 18 / EXP 1)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $94.22
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.65** / 初期 $100.00 (+64.65%)
- 確定: 1406件 (Win 387 / Loss 459 / Flat 560) / skip 1688件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NAORIS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $164.65

## 4. Latest Market Context

- 更新: 2026-06-12T18:01:09.896942+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63873.3
- Funnel: target 774 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +11.75% | $64,988,383.31 |
| PLAY/USDT:USDT | +11.07% | $8,878,664.95 |
| H/USDT:USDT | +9.84% | $28,913,914.91 |
| HOME/USDT:USDT | +7.25% | $3,012,139.09 |
| SPCXSTOCK/USDT:USDT | +6.36% | $209,416,083.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENJ/USDT:USDT | below_1h_threshold | +0.55% | +0.50% |
| PLAY/USDT:USDT | below_1h_threshold | +0.47% | +0.41% |
| BTW/USDT:USDT | below_1h_threshold | +0.46% | +0.40% |
| SIREN/USDT:USDT | below_1h_threshold | +0.35% | +0.29% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.28% | +0.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
