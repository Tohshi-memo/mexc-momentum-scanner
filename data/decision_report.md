# Decision Report

- generated_at: 2026-05-12T17:02:59.233101+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4147**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4147, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| ASK | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.55% | **+1.16%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.51% | **+0.98%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.94% | **+0.89%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.88% | **+0.57%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.57** / 初期 $100.00 (+20.57%)
- 確定: 283件 (Win 81 / Loss 96 / Flat 106) / skip 425件
- 成長率目線: 平均log +0.000661 / 幾何平均 +0.066% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $120.57

## 4. Latest Market Context

- 更新: 2026-05-12T17:02:55.863172+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=80016.1
- Funnel: target 763 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +18.89% | $2,931,561.22 |
| IRYS/USDT:USDT | +5.43% | $2,039,011.88 |
| COAI/USDT:USDT | +4.67% | $1,100,435.03 |
| GUA/USDT:USDT | +4.17% | $4,093,929.40 |
| LAB/USDT:USDT | +3.55% | $167,609,974.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +1.86% | +1.80% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.32% | +1.26% |
| LAB/USDT:USDT | below_1h_threshold | +1.21% | +1.15% |
| COAI/USDT:USDT | below_1h_threshold | +0.93% | +0.87% |
| B/USDT:USDT | below_1h_threshold | +0.90% | +0.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
