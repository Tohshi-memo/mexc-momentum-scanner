# Decision Report

- generated_at: 2026-05-14T08:08:00.770679+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4276**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=4276, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.44% | **+1.08%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.21% | **+1.03%** |
| LIMIT_BB3S | 4/16 | 25.0% | +4.06% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.07% | **+4.07%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.16% | **+0.86%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.69% | **+0.67%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 344件 (Win 94 / Loss 125 / Flat 125) / skip 493件
- 成長率目線: 平均log +0.000510 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T08:07:57.554606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=79648.0
- Funnel: target 766 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +27.28% | $2,090,134.58 |
| UP/USDT:USDT | +22.36% | $5,322,059.07 |
| CSCOSTOCK/USDT:USDT | +20.27% | $5,210,533.36 |
| PIEVERSE/USDT:USDT | +19.70% | $1,503,259.96 |
| STAR/USDT:USDT | +17.84% | $1,360,582.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +4.17% | +4.23% |
| JCT/USDT:USDT | below_1h_threshold | +1.49% | +1.56% |
| UP/USDT:USDT | below_1h_threshold | +1.34% | +1.41% |
| RIF/USDT:USDT | below_1h_threshold | +1.24% | +1.30% |
| AIN/USDT:USDT | below_1h_threshold | +1.08% | +1.14% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
