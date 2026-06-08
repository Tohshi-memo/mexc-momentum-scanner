# Decision Report

- generated_at: 2026-06-08T00:01:20.772150+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6010**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6010, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.34% | **+0.40%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 2/18 | 11.1% | +0.90% | **+0.10%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.13% | **+0.96%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.03% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.63** / 初期 $100.00 (+54.63%)
- 確定: 1127件 (Win 276 / Loss 341 / Flat 510) / skip 1444件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $154.63

## 4. Latest Market Context

- 更新: 2026-06-08T00:01:18.117300+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=63230.8
- Funnel: target 772 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +25.48% | $4,225,019.17 |
| PIPPIN/USDT:USDT | +24.81% | $5,189,212.88 |
| BLESS/USDT:USDT | +22.53% | $8,680,702.70 |
| BEAT/USDT:USDT | +17.87% | $83,211,964.13 |
| BTW/USDT:USDT | +14.66% | $15,852,067.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.00% | +2.10% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.01% | +1.12% |
| INJ/USDT:USDT | below_1h_threshold | +0.42% | +0.53% |
| BLESS/USDT:USDT | below_1h_threshold | +0.34% | +0.45% |
| MYX/USDT:USDT | below_1h_threshold | +0.20% | +0.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
