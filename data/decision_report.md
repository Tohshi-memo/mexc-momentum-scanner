# Decision Report

- generated_at: 2026-06-03T12:57:49.077609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5544**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5544, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.97% | **+0.82%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.64% | **+0.58%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.63% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.85** / 初期 $100.00 (+33.85%)
- 確定: 998件 (Win 239 / Loss 308 / Flat 451) / skip 1107件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZORA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $133.85

## 4. Latest Market Context

- 更新: 2026-06-03T12:57:46.368806+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=67070.3
- Funnel: target 771 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +43.06% | $1,138,356.67 |
| CLO/USDT:USDT | +38.31% | $5,119,455.30 |
| BP/USDT:USDT | +36.02% | $1,113,799.93 |
| EPIC/USDT:USDT | +34.19% | $3,483,993.32 |
| LIT/USDT:USDT | +29.06% | $9,921,313.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +4.15% | +4.11% |
| LIT/USDT:USDT | below_1h_threshold | +3.69% | +3.65% |
| ZEC/USDT:USDT | below_1h_threshold | +3.45% | +3.40% |
| HYUNDAISTOCK/USDT:USDT | below_1h_threshold | +3.28% | +3.24% |
| MYX/USDT:USDT | below_1h_threshold | +3.01% | +2.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
