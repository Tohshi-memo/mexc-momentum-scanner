# Decision Report

- generated_at: 2026-06-18T04:38:39.418911+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7003**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7003, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.32% | **+0.08%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.35% | **-0.10%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |
| ASK | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.12% | **+2.12%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.87% | **+0.57%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.13** / 初期 $100.00 (+115.13%)
- 確定: 1849件 (Win 515 / Loss 583 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $215.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.40** / 初期 $100.00 (+5.40%)
- 確定: 276件 (Win 76 / Loss 71 / Flat 129) / skip 138件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0601 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.40

## 5. Latest Market Context

- 更新: 2026-06-18T04:38:31.082642+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=63930.0
- Funnel: target 792 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +113.28% | $35,034,122.78 |
| O/USDT:USDT | +64.62% | $2,053,219.97 |
| SYN/USDT:USDT | +50.63% | $4,616,947.96 |
| HOME/USDT:USDT | +39.61% | $1,428,577.24 |
| H/USDT:USDT | +29.10% | $33,857,127.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.06% | +3.57% |
| PLAY/USDT:USDT | below_1h_threshold | +3.06% | +3.56% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.29% | +2.80% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.11% | +1.61% |
| BASED/USDT:USDT | below_1h_threshold | +0.67% | +1.18% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
