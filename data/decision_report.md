# Decision Report

- generated_at: 2026-05-12T06:37:47.074211+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4098**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4098, expectancy=-0.13%
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
| LIMIT_ATR | 18/20 | 90.0% | -0.19% | **-0.17%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.89% | **+2.31%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.83% | **+2.11%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.74% | **+1.57%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.17% | **+1.52%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.80% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.47** / 初期 $100.00 (+11.47%)
- 確定: 234件 (Win 61 / Loss 81 / Flat 92) / skip 425件
- 成長率目線: 平均log +0.000464 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAHARA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $111.47

## 4. Latest Market Context

- 更新: 2026-05-12T06:37:43.993013+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=81146.4
- Funnel: target 762 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +50.28% | $2,951,977.57 |
| SAGA/USDT:USDT | +44.54% | $9,431,097.64 |
| GUA/USDT:USDT | +33.79% | $1,990,418.03 |
| SKYAI/USDT:USDT | +31.83% | $42,899,646.04 |
| USELESS/USDT:USDT | +27.07% | $5,317,873.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAHARA/USDT:USDT | below_1h_threshold | +4.38% | +4.43% |
| GIGA/USDT:USDT | below_1h_threshold | +4.18% | +4.23% |
| FF/USDT:USDT | below_1h_threshold | +3.88% | +3.93% |
| RIF/USDT:USDT | below_1h_threshold | +3.58% | +3.63% |
| UB/USDT:USDT | below_1h_threshold | +3.24% | +3.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
