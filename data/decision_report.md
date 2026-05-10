# Decision Report

- generated_at: 2026-05-10T13:32:37.563315+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3965**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3965, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.24% | **+0.18%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.25% | **+0.04%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.02% | **+0.01%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.08% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +3.59% | **+1.97%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.96% | **+0.77%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.69% | **+0.59%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.00% | **+0.55%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.79% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 328件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T13:32:34.419088+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=80894.0
- Funnel: target 769 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +61.22% | $2,241,983.67 |
| LAYER/USDT:USDT | +36.17% | $9,385,414.64 |
| GIGA/USDT:USDT | +24.42% | $1,238,338.02 |
| XEC/USDT:USDT | +19.17% | $3,280,023.10 |
| BAS/USDT:USDT | +18.53% | $1,256,903.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MITO/USDT:USDT | below_1h_threshold | +3.09% | +3.08% |
| GIGA/USDT:USDT | below_1h_threshold | +2.84% | +2.84% |
| UNI/USDT:USDT | below_1h_threshold | +2.61% | +2.60% |
| LUNC/USDT:USDT | below_1h_threshold | +2.34% | +2.33% |
| SPACEX/USDT:USDT | below_1h_threshold | +2.33% | +2.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
