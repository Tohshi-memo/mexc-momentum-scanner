# Decision Report

- generated_at: 2026-05-10T10:32:44.941435+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3960**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3960, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.48% | **+0.05%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.23% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.34% | **+1.50%** |
| MARKET_LONG | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.05% | **+0.79%** |
| ASK_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.71% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 324件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T10:32:41.746551+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80775.9
- Funnel: target 769 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +60.20% | $1,697,767.93 |
| LAYER/USDT:USDT | +52.05% | $7,360,810.85 |
| GIGA/USDT:USDT | +28.86% | $1,054,431.79 |
| XEC/USDT:USDT | +27.91% | $2,701,879.34 |
| SATO/USDT:USDT | +26.58% | $6,394,159.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +3.53% | +3.52% |
| REZ/USDT:USDT | below_1h_threshold | +3.41% | +3.40% |
| BILL/USDT:USDT | below_1h_threshold | +3.00% | +2.99% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.57% | +1.56% |
| SUI/USDT:USDT | below_1h_threshold | +1.46% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
