# Decision Report

- generated_at: 2026-05-10T15:53:08.155368+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3968**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3968, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_BB3S | 3/17 | 17.6% | +0.47% | **+0.08%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.25% | **+0.04%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.02% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.86% | **+1.93%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.99% | **+1.00%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.17% | **+0.93%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.99% | **+0.89%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.23% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 331件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T15:53:04.749002+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=81365.1
- Funnel: target 769 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1, 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +71.83% | $2,694,991.55 |
| LAYER/USDT:USDT | +36.90% | $10,234,723.84 |
| GIGA/USDT:USDT | +32.51% | $1,409,526.06 |
| TRUTH/USDT:USDT | +27.96% | $1,207,139.06 |
| BIANRENSHENG/USDT:USDT | +24.68% | $1,057,899.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_relative_strength | +5.13% | +4.61% |
| LAB/USDT:USDT | below_relative_strength | +5.10% | +4.58% |
| S/USDT:USDT | below_1h_threshold | +4.16% | +3.64% |
| ATOM/USDT:USDT | below_1h_threshold | +3.97% | +3.45% |
| FHE/USDT:USDT | below_1h_threshold | +3.77% | +3.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
