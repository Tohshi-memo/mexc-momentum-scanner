# Decision Report

- generated_at: 2026-05-10T13:47:38.742452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3966**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3966, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.24% | **+0.18%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.25% | **+0.04%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.02% | **+0.01%** |
| LIMIT_ATR | 12/20 | 60.0% | -0.08% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +3.59% | **+1.97%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.00% | **+0.55%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.62% | **+0.46%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.79% | **+0.39%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.94% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 329件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T13:47:35.580239+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80923.3
- Funnel: target 769 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +62.75% | $2,275,118.59 |
| LAYER/USDT:USDT | +37.96% | $9,455,313.24 |
| GIGA/USDT:USDT | +26.10% | $1,261,503.34 |
| BILL/USDT:USDT | +20.57% | $43,367,721.75 |
| BAS/USDT:USDT | +20.42% | $1,308,238.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +4.41% | +4.37% |
| W/USDT:USDT | below_1h_threshold | +3.53% | +3.49% |
| UNI/USDT:USDT | below_1h_threshold | +3.49% | +3.45% |
| MITO/USDT:USDT | below_1h_threshold | +3.14% | +3.10% |
| BAS/USDT:USDT | below_1h_threshold | +2.65% | +2.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
