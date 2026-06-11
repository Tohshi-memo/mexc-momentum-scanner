# Decision Report

- generated_at: 2026-06-11T01:22:54.189320+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6288**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6288, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +2.47% | **+1.36%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.96% | **+0.81%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 3/20 | 15.0% | +5.26% | **+0.79%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.14% | **+0.68%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.78% | **+0.62%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1270件 (Win 319 / Loss 401 / Flat 550) / skip 1579件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T01:22:51.043698+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=62118.4
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +97.20% | $45,067,537.47 |
| BEAT/USDT:USDT | +25.29% | $187,878,911.90 |
| FIGHT/USDT:USDT | +19.54% | $1,073,236.46 |
| FOLKS/USDT:USDT | +12.03% | $12,668,562.87 |
| STRAX/USDT:USDT | +8.65% | $1,278,845.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +2.27% | +1.75% |
| RUNE/USDT:USDT | below_1h_threshold | +1.85% | +1.33% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.85% | +1.32% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.80% | +1.28% |
| CRV/USDT:USDT | below_1h_threshold | +1.61% | +1.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
