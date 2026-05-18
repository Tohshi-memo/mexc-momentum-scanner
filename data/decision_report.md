# Decision Report

- generated_at: 2026-05-18T12:49:24.634105+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4442**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4442, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.28% | **+0.26%** |
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.74** / 初期 $100.00 (-4.26%)
- 確定トレード: 53件 (TP 13 / SL 37 / EXP 3)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.02** / 初期 $100.00 (+22.02%)
- 確定: 439件 (Win 114 / Loss 148 / Flat 177) / skip 564件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.02

## 4. Latest Market Context

- 更新: 2026-05-18T12:49:22.636803+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=77653.9
- Funnel: target 768 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRAC/USDT:USDT | +48.47% | $1,097,565.17 |
| FIDA/USDT:USDT | +39.82% | $9,883,976.72 |
| BSB/USDT:USDT | +16.62% | $18,248,317.71 |
| OPENLEDGER/USDT:USDT | +14.61% | $1,539,519.18 |
| RIVER/USDT:USDT | +7.64% | $9,889,081.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +3.71% | +3.20% |
| BEAT/USDT:USDT | below_1h_threshold | +2.86% | +2.35% |
| VVV/USDT:USDT | below_1h_threshold | +2.49% | +1.98% |
| AKT/USDT:USDT | below_1h_threshold | +2.41% | +1.89% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.38% | +1.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
