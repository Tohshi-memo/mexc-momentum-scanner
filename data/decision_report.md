# Decision Report

- generated_at: 2026-05-06T21:27:38.701405+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3500**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3500, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/12 | 33.3% | +1.90% | **+0.63%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.28% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +4.62% | **+2.31%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.94% | **+0.89%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.01% | **+0.86%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.38% | **+0.83%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 52件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T21:27:35.898811+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=81401.9
- Funnel: target 764 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +55.05% | $12,784,852.46 |
| ZEREBRO/USDT:USDT | +13.01% | $1,339,695.84 |
| BILL/USDT:USDT | +8.94% | $7,504,785.83 |
| LAB/USDT:USDT | +8.22% | $238,941,167.22 |
| UB/USDT:USDT | +7.85% | $1,799,971.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +2.34% | +2.31% |
| LAB/USDT:USDT | below_1h_threshold | +2.30% | +2.27% |
| OP/USDT:USDT | below_1h_threshold | +2.06% | +2.03% |
| ORDI/USDT:USDT | below_1h_threshold | +1.93% | +1.90% |
| SIREN/USDT:USDT | below_1h_threshold | +1.72% | +1.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
