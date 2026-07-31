# Decision Report

- generated_at: 2026-07-31T22:46:34.879269+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10031**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10031, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/18 | 27.8% | +3.30% | **+0.92%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.47% | **+1.73%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.52%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.86% | **+1.29%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.26% | **+1.24%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$567.45** / 初期 $100.00 (+467.45%)
- 確定: 3583件 (Win 1147 / Loss 1170 / Flat 1266) / skip 3009件
- 成長率目線: 平均log +0.000485 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $567.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2164件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0863 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.18** / 初期 $100.00 (+12.18%)
- 確定: 857件 (Win 279 / Loss 338 / Flat 240) / pending 6件 / skip 647件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000366 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $112.18

## 6. Latest Market Context

- 更新: 2026-07-31T22:46:22.339506+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=62924.9
- Funnel: target 921 → liquid 174 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +28.83% | $1,148,198.46 |
| GIGGLE/USDT:USDT | +15.62% | $18,902,235.63 |
| TLM/USDT:USDT | +15.34% | $1,342,416.95 |
| FLOW/USDT:USDT | +15.00% | $1,117,695.59 |
| AKE/USDT:USDT | +12.46% | $16,392,846.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.47% | +2.47% |
| ORDI/USDT:USDT | below_1h_threshold | +1.62% | +1.62% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.62% | +1.62% |
| UNI/USDT:USDT | below_1h_threshold | +1.43% | +1.43% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.32% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
