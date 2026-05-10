# Decision Report

- generated_at: 2026-05-10T17:48:01.988579+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3976**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3976, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.08% | **-2.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.08% | **+0.05%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_BB3S | 4/17 | 23.5% | -0.57% | **-0.14%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.52% | **-0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.65% | **+1.82%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.74% | **+1.50%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.54% | **+1.41%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.73% | **+1.30%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.13% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 198件 (Win 48 / Loss 66 / Flat 84) / skip 339件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T17:47:53.236601+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=81351.0
- Funnel: target 769 → liquid 163 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=1, 4h RSI 75.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRUTH/USDT:USDT | +11.02% | $1,879,104.66 |
| B/USDT:USDT | +10.05% | $1,197,123.16 |
| TROLLSOL/USDT:USDT | +9.92% | $3,206,633.64 |
| FHE/USDT:USDT | +8.73% | $1,897,796.00 |
| SUI/USDT:USDT | +7.83% | $485,967,678.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +4.33% | +4.31% |
| SUI/USDT:USDT | below_1h_threshold | +3.73% | +3.72% |
| TRIA/USDT:USDT | below_1h_threshold | +3.71% | +3.69% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.25% | +2.24% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.15% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
