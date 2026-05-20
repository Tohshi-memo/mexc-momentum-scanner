# Decision Report

- generated_at: 2026-05-20T05:13:41.641014+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4525**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4525, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.88% | **+0.48%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.36% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.98% | **+1.64%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.72% | **+1.03%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.11% | **+0.95%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.35% | **+0.94%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.90% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.41** / 初期 $100.00 (+24.41%)
- 確定: 487件 (Win 128 / Loss 167 / Flat 192) / skip 599件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $124.41

## 4. Latest Market Context

- 更新: 2026-05-20T05:13:39.311362+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.59% price=77200.4
- Funnel: target 764 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +36.52% | $19,732,147.67 |
| PROMPT/USDT:USDT | +33.82% | $12,680,340.69 |
| LIT/USDT:USDT | +27.47% | $7,194,032.73 |
| FIDA/USDT:USDT | +27.34% | $1,449,455.12 |
| ZEST/USDT:USDT | +16.47% | $1,919,247.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +3.38% | +2.80% |
| PROMPT/USDT:USDT | below_1h_threshold | +2.89% | +2.30% |
| VVV/USDT:USDT | below_1h_threshold | +1.99% | +1.40% |
| ONDO/USDT:USDT | below_1h_threshold | +1.78% | +1.19% |
| XAN/USDT:USDT | below_1h_threshold | +1.50% | +0.91% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
