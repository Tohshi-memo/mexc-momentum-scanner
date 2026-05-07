# Decision Report

- generated_at: 2026-05-07T05:52:30.227934+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3574**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3574, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.33% | **-1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.85% | **+0.21%** |
| LIMIT_BB3S | 5/15 | 33.3% | +0.49% | **+0.16%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.00% | **-0.00%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.07% | **-0.07%** |
| ASK | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.99% | **+1.79%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.06% | **+1.13%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.11%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +3.78% | **+0.95%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.68% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.78** / 初期 $100.00 (+7.78%)
- 確定: 68件 (Win 26 / Loss 25 / Flat 17) / skip 67件
- 成長率目線: 平均log +0.001101 / 幾何平均 +0.110% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $107.78

## 4. Latest Market Context

- 更新: 2026-05-07T05:52:26.784754+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80982.2
- Funnel: target 770 → liquid 186 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1, 4h RSI 77.5 >= 65=1, 4h RSI 70.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +234.24% | $1,730,671.27 |
| B3/USDT:USDT | +100.22% | $9,392,409.66 |
| DOGS/USDT:USDT | +82.85% | $11,756,983.98 |
| PENGUIN/USDT:USDT | +55.36% | $1,373,501.47 |
| HMSTR/USDT:USDT | +31.80% | $1,149,010.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +4.14% | +4.09% |
| OP/USDT:USDT | below_1h_threshold | +3.81% | +3.76% |
| S/USDT:USDT | below_1h_threshold | +3.59% | +3.54% |
| BLESS/USDT:USDT | below_1h_threshold | +2.98% | +2.93% |
| BILL/USDT:USDT | below_1h_threshold | +2.56% | +2.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
