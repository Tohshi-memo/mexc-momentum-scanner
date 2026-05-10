# Decision Report

- generated_at: 2026-05-10T16:22:41.496541+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3970**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3970, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.34% | **-2.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.25% | **+0.04%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.02% | **+0.01%** |
| LIMIT_BB3S | 4/18 | 22.2% | -0.19% | **-0.04%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.55% | **-0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +4.89% | **+2.44%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.94% | **+1.77%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.09% | **+1.56%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.37% | **+1.54%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +3.63% | **+1.27%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 333件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T16:22:38.017106+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=81306.2
- Funnel: target 769 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASED/USDT:USDT | +5.39% | $2,372,631.15 |
| TRUTH/USDT:USDT | +3.95% | $1,297,970.87 |
| WLD/USDT:USDT | +3.38% | $18,657,747.91 |
| INX/USDT:USDT | +3.25% | $17,357,665.20 |
| XPL/USDT:USDT | +2.33% | $3,821,647.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUTH/USDT:USDT | below_1h_threshold | +4.18% | +4.28% |
| WLD/USDT:USDT | below_1h_threshold | +3.42% | +3.51% |
| INX/USDT:USDT | below_1h_threshold | +3.26% | +3.35% |
| XPL/USDT:USDT | below_1h_threshold | +2.34% | +2.43% |
| SUI/USDT:USDT | below_1h_threshold | +1.94% | +2.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
