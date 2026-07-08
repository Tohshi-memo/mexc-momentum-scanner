# Decision Report

- generated_at: 2026-07-08T17:04:52.465521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8490**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.27% / filled 20/20。**
- 全期間 MARKET基準: n=8490, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.80% | **+1.80%** |
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.69% | **+1.02%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.70% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.03% | **+0.67%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.27% | **+0.19%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.12% | **-0.10%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.20% | **-0.13%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.25% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$105.15** / 初期 $100.00 (+5.15%)
- 確定トレード: 78件 (TP 29 / SL 48 / EXP 1)
- 最新: VANRY/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.69** / 初期 $100.00 (+221.69%)
- 確定: 2682件 (Win 849 / Loss 900 / Flat 933) / skip 2369件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.50% 残高後 $321.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1259件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-08T17:04:43.140748+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=62055.2
- Funnel: target 851 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VANRY/USDT:USDT | +22.28% | $4,850,585.96 |
| TLM/USDT:USDT | +11.56% | $3,997,203.30 |
| KORU/USDT:USDT | +7.64% | $7,164,734.36 |
| POWER/USDT:USDT | +7.16% | $1,762,959.61 |
| ALLO/USDT:USDT | +7.00% | $10,113,135.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +3.23% | +3.28% |
| UNI/USDT:USDT | below_1h_threshold | +1.57% | +1.62% |
| VELVET/USDT:USDT | below_1h_threshold | +1.53% | +1.58% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.50% | +1.55% |
| YFI/USDT:USDT | below_1h_threshold | +1.49% | +1.54% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
