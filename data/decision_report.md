# Decision Report

- generated_at: 2026-06-10T20:04:44.156894+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6256**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6256, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.54% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.81% | **+0.90%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.88% | **+0.85%** |
| ASK_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.76% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.73** / 初期 $100.00 (+49.73%)
- 確定: 1243件 (Win 309 / Loss 387 / Flat 547) / skip 1574件
- 成長率目線: 平均log +0.000325 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $149.73

## 4. Latest Market Context

- 更新: 2026-06-10T20:04:41.110666+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=61841.5
- Funnel: target 785 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +49.86% | $24,431,044.06 |
| BEAT/USDT:USDT | +14.44% | $122,518,105.47 |
| JCT/USDT:USDT | +9.63% | $2,154,690.50 |
| ESPORTS/USDT:USDT | +5.49% | $22,886,302.84 |
| BSB/USDT:USDT | +4.42% | $6,546,576.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +1.60% | +1.71% |
| BSB/USDT:USDT | below_1h_threshold | +1.33% | +1.44% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.11% | +1.22% |
| LAB/USDT:USDT | below_1h_threshold | +1.00% | +1.11% |
| BEAT/USDT:USDT | below_1h_threshold | +0.68% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
