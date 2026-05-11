# Decision Report

- generated_at: 2026-05-11T09:08:07.618191+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4023**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=4023, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.91% | **+0.68%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.70% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.35% | **+0.35%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.38% | **+0.21%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.17% | **+0.10%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.07% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 366件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T09:08:04.701208+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80802.4
- Funnel: target 760 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +38.63% | $11,911,652.83 |
| B/USDT:USDT | +29.84% | $8,301,956.26 |
| TROLLSOL/USDT:USDT | +17.30% | $4,704,354.08 |
| ALCH/USDT:USDT | +17.11% | $4,650,229.45 |
| SAGA/USDT:USDT | +16.08% | $1,996,110.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.94% | +3.85% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.49% | +1.39% |
| UB/USDT:USDT | below_1h_threshold | +1.34% | +1.25% |
| OPG/USDT:USDT | below_1h_threshold | +0.96% | +0.87% |
| ORCA/USDT:USDT | below_1h_threshold | +0.89% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
