# Decision Report

- generated_at: 2026-06-09T08:42:45.757755+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6124**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6124, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.67% | **-1.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.96% | **+1.96%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.48% | **+1.92%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.43% | **+1.58%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +4.38% | **+1.31%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.59% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.99** / 初期 $100.00 (+54.99%)
- 確定: 1164件 (Win 292 / Loss 358 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $154.99

## 4. Latest Market Context

- 更新: 2026-06-09T08:42:42.673139+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=62953.0
- Funnel: target 774 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +62.92% | $22,938,420.53 |
| SLX/USDT:USDT | +42.62% | $3,405,671.77 |
| POWER/USDT:USDT | +13.72% | $1,917,608.59 |
| LIGHT/USDT:USDT | +10.37% | $1,125,616.32 |
| FOLKS/USDT:USDT | +10.20% | $1,781,143.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +4.18% | +4.52% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.83% | +4.17% |
| STG/USDT:USDT | below_1h_threshold | +3.23% | +3.58% |
| CTR/USDT:USDT | below_1h_threshold | +2.45% | +2.80% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.16% | +2.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
