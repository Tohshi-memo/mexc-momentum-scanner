# Decision Report

- generated_at: 2026-05-19T18:54:16.890382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4494**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4494, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.65% | **+0.32%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +3.39% | **+1.69%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.37% | **+1.31%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.30% | **+1.27%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.03% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 582件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T18:54:12.578430+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=76831.1
- Funnel: target 760 → liquid 139 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +55.06% | $16,243,171.09 |
| EDEN/USDT:USDT | +37.83% | $10,211,230.05 |
| VVV/USDT:USDT | +14.06% | $9,101,785.46 |
| LIT/USDT:USDT | +8.94% | $2,009,538.29 |
| FIGHT/USDT:USDT | +8.46% | $1,134,339.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +2.69% | +2.67% |
| SPACE/USDT:USDT | below_1h_threshold | +2.29% | +2.27% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.99% | +1.98% |
| LAB/USDT:USDT | below_1h_threshold | +1.41% | +1.40% |
| LIT/USDT:USDT | below_1h_threshold | +1.21% | +1.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
