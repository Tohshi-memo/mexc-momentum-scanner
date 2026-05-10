# Decision Report

- generated_at: 2026-05-10T13:03:03.316498+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3963**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3963, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.24% | **+0.18%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.25% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.85% | **+1.57%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.44% | **+0.35%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.06% | **+0.31%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.27% | **+0.23%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.48% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 327件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T13:03:00.162565+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80905.6
- Funnel: target 769 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +65.82% | $2,158,765.32 |
| LAYER/USDT:USDT | +35.54% | $9,147,961.06 |
| GIGA/USDT:USDT | +21.31% | $1,217,253.47 |
| XEC/USDT:USDT | +19.04% | $3,195,175.60 |
| BAS/USDT:USDT | +17.90% | $1,188,231.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.10% | +2.09% |
| BILL/USDT:USDT | below_1h_threshold | +1.50% | +1.48% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +1.44% | +1.42% |
| LUNC/USDT:USDT | below_1h_threshold | +1.25% | +1.23% |
| UNI/USDT:USDT | below_1h_threshold | +1.13% | +1.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
