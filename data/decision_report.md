# Decision Report

- generated_at: 2026-06-07T09:10:06.709290+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5938**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5938, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.16% | **-2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +2.57% | **+0.90%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.96% | **+1.96%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +6.42% | **+1.93%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.96% | **+1.48%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.80% | **+1.26%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$143.72** / 初期 $100.00 (+43.72%)
- 確定: 1057件 (Win 258 / Loss 323 / Flat 476) / skip 1442件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $143.72

## 4. Latest Market Context

- 更新: 2026-06-07T09:10:03.797848+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=62765.9
- Funnel: target 771 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +56.13% | $10,205,276.98 |
| FIDA/USDT:USDT | +55.13% | $6,536,819.45 |
| LAB/USDT:USDT | +40.45% | $63,057,020.86 |
| BSB/USDT:USDT | +27.09% | $6,414,785.67 |
| EDEN/USDT:USDT | +26.44% | $3,196,147.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +2.51% | +2.61% |
| LAB/USDT:USDT | below_1h_threshold | +1.81% | +1.90% |
| SIREN/USDT:USDT | below_1h_threshold | +1.24% | +1.33% |
| LUNC/USDT:USDT | below_1h_threshold | +1.23% | +1.33% |
| ZEC/USDT:USDT | below_1h_threshold | +0.86% | +0.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
