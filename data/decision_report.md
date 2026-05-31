# Decision Report

- generated_at: 2026-05-31T15:36:09.534358+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5202**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5202, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.68% | **-1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_BB3S | 5/14 | 35.7% | -1.07% | **-0.38%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -1.17% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.77% | **+1.80%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.89% | **+1.47%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.84% | **+1.28%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.06** / 初期 $100.00 (+28.06%)
- 確定: 837件 (Win 193 / Loss 249 / Flat 395) / skip 926件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $128.06

## 4. Latest Market Context

- 更新: 2026-05-31T15:36:05.452271+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=73710.6
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.4 >= 65=1, 4h RSI 67.0 >= 65=1, 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +44.37% | $11,451,285.85 |
| AIA/USDT:USDT | +37.11% | $4,933,034.82 |
| ALLO/USDT:USDT | +36.01% | $25,418,790.05 |
| STG/USDT:USDT | +31.45% | $4,910,872.99 |
| PORTAL/USDT:USDT | +29.87% | $9,722,940.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +4.06% | +3.87% |
| STG/USDT:USDT | below_1h_threshold | +3.67% | +3.48% |
| VVV/USDT:USDT | below_1h_threshold | +2.73% | +2.54% |
| NEAR/USDT:USDT | below_1h_threshold | +2.67% | +2.48% |
| UP/USDT:USDT | below_1h_threshold | +2.01% | +1.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
