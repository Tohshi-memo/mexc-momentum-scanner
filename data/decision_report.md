# Decision Report

- generated_at: 2026-05-18T21:28:37.260336+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4453**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4453, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.33% | **+0.17%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -1.41% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.49% | **+1.62%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.60% | **+1.44%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.51% | **+1.00%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.46% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定: 450件 (Win 117 / Loss 154 / Flat 179) / skip 564件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RON/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $120.68

## 4. Latest Market Context

- 更新: 2026-05-18T21:28:35.300097+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=76979.1
- Funnel: target 763 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +43.90% | $4,830,283.81 |
| ONDO/USDT:USDT | +7.97% | $30,882,851.30 |
| INJ/USDT:USDT | +5.84% | $18,774,978.41 |
| TRAC/USDT:USDT | +4.96% | $1,325,487.45 |
| AKT/USDT:USDT | +4.92% | $1,572,776.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +4.87% | +4.72% |
| AERO/USDT:USDT | below_1h_threshold | +3.25% | +3.10% |
| AKT/USDT:USDT | below_1h_threshold | +2.23% | +2.09% |
| HYPE/USDT:USDT | below_1h_threshold | +2.21% | +2.06% |
| UNI/USDT:USDT | below_1h_threshold | +1.34% | +1.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
