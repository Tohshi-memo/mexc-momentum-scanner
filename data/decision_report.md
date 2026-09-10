# Decision Report

- generated_at: 2026-09-10T07:31:25.681521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14156**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14156, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.65% | **+0.99%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.36% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,053.72** / 初期 $100.00 (+953.72%)
- 確定: 5336件 (Win 1605 / Loss 1722 / Flat 2009) / skip 5381件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,053.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$206.73** / 初期 $100.00 (+106.73%)
- 確定: 2750件 (Win 761 / Loss 646 / Flat 1343) / skip 4817件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1016 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $206.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.93** / 初期 $100.00 (+21.93%)
- 確定: 2661件 (Win 785 / Loss 1016 / Flat 860) / pending 0件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.93

## 6. Latest Market Context

- 更新: 2026-09-10T07:31:15.210134+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=78006.3
- Funnel: target 1064 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +47.62% | $3,712,894.22 |
| CATE/USDT:USDT | +27.24% | $2,653,318.95 |
| KAS/USDT:USDT | +9.16% | $5,054,301.12 |
| REZ/USDT:USDT | +6.80% | $1,162,190.67 |
| VET/USDT:USDT | +5.20% | $5,689,566.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +4.09% | +4.57% |
| KAS/USDT:USDT | below_1h_threshold | +1.91% | +2.39% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.22% | +1.71% |
| FF/USDT:USDT | below_1h_threshold | +0.61% | +1.10% |
| SOXS/USDT:USDT | below_1h_threshold | +0.41% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
