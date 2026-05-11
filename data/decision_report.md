# Decision Report

- generated_at: 2026-05-11T10:38:09.599536+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4024**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4024, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.87% | **+0.70%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.70% | **+0.42%** |
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.17% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.94% | **+0.56%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.79% | **+0.39%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.71% | **+0.37%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.56% | **+0.28%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.44% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 367件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T10:38:06.583497+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=81036.8
- Funnel: target 761 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +34.22% | $12,820,875.07 |
| B/USDT:USDT | +30.23% | $10,321,103.40 |
| SAGA/USDT:USDT | +24.09% | $2,603,833.73 |
| TROLLSOL/USDT:USDT | +16.61% | $4,647,569.01 |
| ALCH/USDT:USDT | +16.48% | $4,748,466.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TIA/USDT:USDT | below_1h_threshold | +3.64% | +3.50% |
| CRV/USDT:USDT | below_1h_threshold | +2.61% | +2.47% |
| UB/USDT:USDT | below_1h_threshold | +2.12% | +1.98% |
| H/USDT:USDT | below_1h_threshold | +1.69% | +1.55% |
| OPG/USDT:USDT | below_1h_threshold | +1.60% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
