# Decision Report

- generated_at: 2026-05-12T07:32:50.490780+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4099**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4099, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.16% | **+0.43%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_ATR | 18/20 | 90.0% | -0.77% | **-0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.35% | **+2.51%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.25% | **+2.02%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.50% | **+1.75%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.64% | **+1.72%** |
| MARKET_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.47** / 初期 $100.00 (+11.47%)
- 確定: 235件 (Win 61 / Loss 81 / Flat 93) / skip 425件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $111.47

## 4. Latest Market Context

- 更新: 2026-05-12T07:32:47.443640+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81028.2
- Funnel: target 762 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +51.59% | $3,234,702.23 |
| SAGA/USDT:USDT | +41.68% | $9,990,574.92 |
| SKYAI/USDT:USDT | +35.80% | $43,305,824.74 |
| USELESS/USDT:USDT | +29.64% | $5,914,763.10 |
| GUA/USDT:USDT | +24.78% | $2,266,593.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +4.65% | +4.60% |
| AIOT/USDT:USDT | below_1h_threshold | +3.67% | +3.62% |
| SAHARA/USDT:USDT | below_1h_threshold | +3.57% | +3.53% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.14% | +3.10% |
| RIF/USDT:USDT | below_1h_threshold | +2.56% | +2.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
