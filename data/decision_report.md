# Decision Report

- generated_at: 2026-05-10T19:38:38.171077+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3984**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3984, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.05% | **+0.03%** |
| LIMIT_BB3S | 4/14 | 28.6% | -0.80% | **-0.23%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.47% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.50% | **+1.20%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| ASK_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.78% | **+1.07%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.92% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 347件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T19:38:34.947620+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=81401.1
- Funnel: target 769 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +28.34% | $1,255,883.83 |
| TROLLSOL/USDT:USDT | +23.40% | $3,686,309.96 |
| ALCH/USDT:USDT | +22.13% | $2,456,655.61 |
| B/USDT:USDT | +15.92% | $2,055,940.93 |
| SUI/USDT:USDT | +14.47% | $593,174,879.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.46% | +4.25% |
| ENS/USDT:USDT | below_1h_threshold | +3.30% | +3.10% |
| FHE/USDT:USDT | below_1h_threshold | +2.88% | +2.68% |
| JUP/USDT:USDT | below_1h_threshold | +2.77% | +2.57% |
| FET/USDT:USDT | below_1h_threshold | +2.56% | +2.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
